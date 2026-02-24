import json
import time
import requests
import argparse
import concurrent.futures
from pathlib import Path


def iter_requests(items, base_url):
    for item in items:
        if "request" in item:
            req = item["request"]
            method = req.get("method", "GET").upper()
            url_obj = req.get("url", {})
            raw = url_obj.get("raw")
            if not raw:
                host = url_obj.get("host", [])
                path = "/".join(url_obj.get("path", []))
                query = url_obj.get("query", [])
                qstr = "&".join(f"{q['key']}={q['value']}" for q in query) if query else ""
                host_raw = host[0] if host else base_url
                raw = f"{host_raw}/{path}" + (f"?{qstr}" if qstr else "")
            url = raw.replace("{{base_url}}", base_url)
            yield item.get("name", url), method, url
        elif "item" in item:
            yield from iter_requests(item["item"], base_url)


def run_collection(collection_path: Path, report_path: Path, base_url: str | None, timeout: float, filter_folder: str | None, concurrency: int, retries: int, json_out: Path | None):
    with collection_path.open("r", encoding="utf-8") as f:
        collection = json.load(f)

    variables = {v["key"]: v["value"] for v in collection.get("variable", [])}
    base = base_url or variables.get("base_url") or "http://localhost:8000"

    def flatten(items):
        for it in items:
            if "item" in it and "request" not in it:
                fname = it.get("name", "")
                if filter_folder and fname != filter_folder:
                    yield from flatten(it.get("item", []))
                else:
                    yield from flatten(it.get("item", []))
            else:
                yield it

    raw_items = list(flatten(collection.get("item", [])))
    reqs = list(iter_requests(raw_items, base))
    print(f"Base URL: {base}")
    print(f"Running {len(reqs)} requests...")

    def do_request(entry):
        name, method, url = entry
        attempts = 0
        while True:
            t0 = time.perf_counter()
            try:
                resp = requests.request(method, url, timeout=timeout)
                dt_ms = (time.perf_counter() - t0) * 1000.0
                size = len(resp.content or b"")
                ok = 200 <= resp.status_code < 300
                valid_json = None
                validation_error = None
                if ok and resp.content:
                    ct = (resp.headers.get("content-type") or "").split(";")[0].strip().lower()
                    if ct == "application/json":
                        try:
                            resp.json()
                            valid_json = True
                        except (ValueError, requests.exceptions.JSONDecodeError) as e:
                            valid_json = False
                            validation_error = str(e)[:80]
                elif ok and (resp.headers.get("content-type") or "").startswith("application/json") and size == 0:
                    valid_json = False
                    validation_error = "Empty body"
                return {
                    "name": name,
                    "method": method,
                    "url": url,
                    "status": resp.status_code,
                    "time_ms": dt_ms,
                    "size": size,
                    "success": ok,
                    "valid_json": valid_json,
                    "validation_error": validation_error,
                }
            except Exception as e:
                dt_ms = (time.perf_counter() - t0) * 1000.0
                attempts += 1
                if attempts > retries:
                    return {
                        "name": name,
                        "method": method,
                        "url": url,
                        "status": 0,
                        "time_ms": dt_ms,
                        "size": 0,
                        "success": False,
                        "valid_json": None,
                        "validation_error": str(e)[:80] if e else None,
                    }

    results = []
    if concurrency > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as ex:
            for r in ex.map(do_request, reqs):
                results.append(r)
    else:
        for entry in reqs:
            results.append(do_request(entry))

    total = len(results)
    successes = sum(1 for r in results if r["success"])
    failures = total - successes
    invalid = sum(1 for r in results if r.get("valid_json") is False)
    avg = sum(r["time_ms"] for r in results) / total if total else 0.0
    min_t = min((r["time_ms"] for r in results), default=0.0)
    max_t = max((r["time_ms"] for r in results), default=0.0)

    print(f"Passed: {successes}, Failed: {failures}, Invalid JSON: {invalid}")
    print(f"Report: {report_path}")

    lines = []
    lines.append("# Endpoint Test Report\n")
    lines.append(f"\n**Generated:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    lines.append("## Summary\n\n")
    lines.append(f"- **Total Endpoints Tested:** {total}\n")
    lines.append(f"- **Successful (2xx):** {successes} ({(successes/total*100.0) if total else 0:.1f}%)\n")
    lines.append(f"- **Failed:** {failures} ({(failures/total*100.0) if total else 0:.1f}%)\n")
    lines.append(f"- **Invalid response (non-JSON or parse error):** {invalid}\n\n")
    lines.append("### Performance Metrics\n\n")
    lines.append(f"- **Average Response Time:** {avg:.2f} ms\n")
    lines.append(f"- **Minimum Response Time:** {min_t:.2f} ms\n")
    lines.append(f"- **Maximum Response Time:** {max_t:.2f} ms\n\n")
    lines.append("---\n\n## Validation issues\n\n")
    issues = [r for r in results if not r["success"] or r.get("valid_json") is False]
    if not issues:
        lines.append("None.\n\n")
    else:
        for r in issues:
            lines.append(f"- **{r['name']}** `{r['method']} {r['url']}`\n")
            if not r["success"]:
                lines.append(f"  - HTTP {r['status']}\n")
            if r.get("valid_json") is False and r.get("validation_error"):
                lines.append(f"  - Invalid JSON: {r['validation_error']}\n")
        lines.append("\n")

    lines.append("---\n\n## Detailed Results\n\n")

    for r in results:
        lines.append(f"### {r['name']}\n\n")
        lines.append(f"- **URL:** `{r['method']} {r['url']}`\n")
        lines.append(f"- **Status Code:** {r['status']}\n")
        lines.append(f"- **Response Time:** {r['time_ms']:.2f} ms\n")
        lines.append(f"- **Response Size:** {r['size']} bytes\n")
        lines.append(f"- **Success:** {'True' if r['success'] else 'False'}\n")
        vj = r.get("valid_json")
        if vj is True:
            lines.append(f"- **Valid JSON:** Yes\n\n")
        elif vj is False:
            lines.append(f"- **Valid JSON:** No ({r.get('validation_error', '')})\n\n")
        else:
            lines.append(f"- **Valid JSON:** N/A\n\n")

    report_path.write_text("".join(lines), encoding="utf-8")

    if json_out:
        json_out.write_text(json.dumps({
            "summary": {
                "total": total,
                "successes": successes,
                "failures": failures,
                "invalid_json": invalid,
                "avg_ms": avg,
                "min_ms": min_t,
                "max_ms": max_t,
            },
            "results": results,
        }, indent=2), encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Postman collection against API and generate report")
    parser.add_argument("--base-url", default=None, help="Base URL (default: use collection variable or http://localhost:8000)")
    parser.add_argument("--collection", default=str(Path(__file__).resolve().parents[1] / "docs" / "postman_collection.json"))
    parser.add_argument("--report", default=str(Path(__file__).resolve().parents[1] / "docs" / "endpoint_test_report.md"))
    parser.add_argument("--json-out", default="", help="Optional JSON results output path")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--retries", type=int, default=0)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--folder", default="", help="Run only a specific top-level folder name")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]
    coll = Path(args.collection)
    report = Path(args.report)
    json_out = Path(args.json_out) if args.json_out else None
    run_collection(
        collection_path=coll,
        report_path=report,
        base_url=args.base_url,
        timeout=args.timeout,
        filter_folder=(args.folder or None),
        concurrency=max(1, args.concurrency),
        retries=max(0, args.retries),
        json_out=json_out,
    )


