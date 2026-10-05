#!/usr/bin/env python3
"""Audit catalog URLs; report restrictions separately from confirmed broken links."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import json
import ssl
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, HTTPSHandler, Request, build_opener

from build_readme import load_entries, load_sections


class RedirectHandler(HTTPRedirectHandler):
    # Python versions before 3.11 do not follow permanent 308 redirects.
    http_error_308 = HTTPRedirectHandler.http_error_302

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return super().redirect_request(req, fp, 307 if code == 308 else code, msg, headers, newurl)


def check(url):
    request = Request(url, headers={"User-Agent": "Always-On-Intelligence resource-link-check/1.0"})
    try:
        opener = build_opener(RedirectHandler, HTTPSHandler(context=ssl.create_default_context()))
        with opener.open(request, timeout=20) as response:
            response.read(512)
            return {"url": url, "status": response.status, "result": "ok", "final_url": response.url}
    except HTTPError as exc:
        result = "broken" if exc.code in (404, 410) else "restricted" if exc.code in (401, 403, 429) else "review"
        return {"url": url, "status": exc.code, "result": result}
    except (URLError, TimeoutError, OSError) as exc:
        return {"url": url, "result": "review", "detail": str(exc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", help="Write a JSON report to this path")
    args = parser.parse_args()
    urls = sorted({url for entry in load_entries(load_sections()[1]) for url in entry["links"].values()})
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(check, urls))
    summary = dict(Counter(row["result"] for row in results))
    print(json.dumps({"checked": len(urls), **summary}))
    for row in results:
        if row["result"] != "ok":
            print(json.dumps(row))
    if args.output:
        with open(args.output, "w", encoding="utf-8") as out:
            json.dump({"summary": summary, "results": results}, out, indent=2)
            out.write("\n")
    # The result is an audit for human review, not a flaky network-based CI gate.


if __name__ == "__main__":
    main()
