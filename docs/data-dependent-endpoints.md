# Data-dependent and parser-dependent API behavior

Several list endpoints can return empty arrays depending on (1) the game descriptor file on the server, (2) parser logic that matches on exact class names or FullName, or (3) filter/value mismatches. This document summarizes causes and fixes.

## Root causes

### 1. Game data file differences

- The API reads from `Docs/en-US.json` (or the descriptor path in use). If the live server was built without this file (e.g. not committed, or different branch), the parser fails to load and endpoints return 500, not empty arrays.
- If the descriptor is from a **different game version** or **export tool**, class names and structure can differ. The parser was updated to accept multiple class-name variants where known (see below).

### 2. Parser dependency on exact ClassName / FullName

The parser looks up classes by **exact** `ClassName` (e.g. `Build_PowerStorage_C`). Game updates sometimes rename classes (e.g. `Build_PowerStorageMk1_C`, `Build_ConveyorAttachmentSplitter_C`). The following were fixed to try both legacy and new names:

| Endpoint | Legacy class name | Newer / alternate name |
|----------|-------------------|-------------------------|
| `/power/storage` | `Build_PowerStorage_C`, `Desc_PowerStorage_C` | `Build_PowerStorageMk1_C`, `Desc_PowerStorageMk1_C` |
| `/logistics/splitters` | `Build_ConveyorSplitter_C` (and Smart, Programmable) | `Build_ConveyorAttachmentSplitter_C` (and Smart, Programmable) |
| `/logistics/mergers` | `Build_ConveyorMerger_C` | `Build_ConveyorAttachmentMerger_C` |
| `/logistics/fluid-buffers` | `Build_FluidBuffer_C`, `Desc_PipelineJunctionCross_C` | `Build_PipeStorageTank_C`, `Desc_PipelineJunction_Cross_C` |

- **Items `item_type=raw_resource`**: Previously only set when `FullName` contained the substring `"RawResources"`. Some exports do not set `FullName` on descriptor classes. The parser now also treats as `raw_resource` any item whose `ClassName` matches the same patterns used by `extract_raw_resources()` (e.g. `Desc_OreIron_C`, `Desc_Coal_C`, `Desc_Stone_C`).

### 3. Filter / value mismatches

- **`/recipes?building=Constructor`**: Recipes are filtered by `produced_in`, which is parsed from `mProducedIn` in the descriptor. The parser expects paths containing `Build_XXX.Build_XXX_C` and normalizes building names (e.g. strips `Mk1`). If the descriptor format or building names differ, `produced_in` can be empty and the filter returns no recipes. After the parser fix that correctly parses this format, the response is only empty if the descriptor has no recipes with Constructor in `mProducedIn`.
- **`/items?item_type=raw_resource`**: See above; fixed by adding class-name fallback for raw resources.
- **`/progression/unlocks?unlock_type=building`**: Building unlocks are only discovered when the parser finds unlock objects with `Class == "BP_UnlockBuildable_C"` and non-empty `mBuildables`. If the descriptor uses a different class name for buildable unlocks, or does not populate `mBuildables`, the list of unlocks with `unlock_type=building` is empty. This is **data-dependent**; no parser change was made for this.

## Endpoints that may return empty lists

| Endpoint | When it can be empty | Cause |
|----------|----------------------|--------|
| `/transportation/freight-platforms` | Descriptor missing `Build_TrainDockingStation_C` or `Build_TrainDockingStationLiquid_C` | (1) Data |
| `/power/storage` | Descriptor had only `Build_PowerStorageMk1_C` | (2) Fixed: parser now tries both names |
| `/logistics/splitters` | Descriptor had only `Build_ConveyorAttachmentSplitter*` | (2) Fixed: parser now tries both naming schemes |
| `/logistics/mergers` | Descriptor had only `Build_ConveyorAttachmentMerger_C` | (2) Fixed: parser now tries both names |
| `/logistics/fluid-buffers` | Descriptor used `Build_PipeStorageTank_C` or `Desc_PipelineJunction_Cross_C` | (2) Fixed: parser now tries alternate names |
| `/recipes?building=...` | `mProducedIn` format different or building name not normalized as expected | (3) Data-dependent |
| `/items?item_type=raw_resource` | Descriptor had no `FullName` on raw resource classes | (2) Fixed: raw_resource inferred from class name patterns |
| `/progression/unlocks?unlock_type=building` | Descriptor has no `BP_UnlockBuildable_C` or empty `mBuildables` | (1)/(2) Data-dependent |

## Recommendations

- **Deploy**: Ensure `Docs/en-US.json` (or the chosen descriptor) is included in the build and is from a supported Satisfactory version.
- **Empty lists**: If an endpoint still returns `[]` after these fixes, compare the descriptor on the server with the class names and structure in `src/parsers/game_descriptor_parser.py` (e.g. `_get_class_by_name` / `_get_class_by_any_name` and the extract methods). Add additional fallback class names if a new game version uses different names.
- **Unlocks building**: If `/progression/unlocks?unlock_type=building` stays empty, verify in the descriptor that buildable unlocks exist and use the expected `Class` and `mBuildables` format; extend the parser if the format differs.
