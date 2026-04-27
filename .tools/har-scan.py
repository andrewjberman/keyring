#!/usr/bin/env python3
"""har-scan.py — Survey + drill into a HAR file's network activity.

Usage:
  har-scan.py <har-file> [filters...] <mode>

Modes (pick one; default --summary):
  --summary           Counts by host/method/status + unique endpoints
  --list              One-line per matching entry (#idx, status, method, URL)
  --show N            Pretty-print the first N matching entries
  --detail N          Pretty-print entry #N (1-indexed in original HAR)
  --hosts             Just list unique hosts seen
  --endpoints         Just list unique METHOD path combinations

Filters (composable):
  --url <substring>           URL contains <substring> (case-insensitive)
  --url-regex <pattern>       URL matches Python regex
  --method <METHOD>           Filter by HTTP method
  --status <code>             Filter by response status code
  --content-type <substring>  Filter by response Content-Type substring
  --has-body                  Only entries whose request has a body (POST/PUT)

Display tuning:
  --max-body N        Truncate body display at N chars (default 4000; 0 = no truncate)
  --headers-only      Skip request/response bodies
  --no-redact         Show full Authorization/Cookie values (default redacts)
  --raw-body N        Print raw response body of entry #N to stdout (no formatting)

Examples:
  har-scan.py session.har --summary
  har-scan.py session.har --url login --show 1
  har-scan.py session.har --url dataqueries --method POST --list
  har-scan.py session.har --detail 247
  har-scan.py session.har --url query --content-type json --show 2 --max-body 8000
"""

from __future__ import annotations
import argparse
import json
import re
import sys
from collections import Counter
from urllib.parse import urlparse


def load_har(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    entries = data["log"]["entries"]
    print(f"[har-scan] Loaded {len(entries)} entries from {path}", file=sys.stderr)
    return entries


def match(entry: dict, *, url=None, url_regex=None, method=None, status=None,
          content_type=None, has_body=False) -> bool:
    req, resp = entry["request"], entry["response"]
    if url and url.lower() not in req["url"].lower():
        return False
    if url_regex and not re.search(url_regex, req["url"]):
        return False
    if method and req["method"].upper() != method.upper():
        return False
    if status is not None and resp["status"] != status:
        return False
    if content_type:
        ct = next((h["value"] for h in resp.get("headers", [])
                   if h["name"].lower() == "content-type"), "")
        if content_type.lower() not in ct.lower():
            return False
    if has_body:
        body = (req.get("postData") or {}).get("text", "")
        if not body:
            return False
    return True


def filter_entries(entries: list[dict], **filters) -> list[tuple[int, dict]]:
    return [(i, e) for i, e in enumerate(entries, start=1) if match(e, **filters)]


def header(entry_or_headers, name: str) -> str | None:
    """Return value of a header by case-insensitive name."""
    headers = entry_or_headers.get("headers", []) if isinstance(entry_or_headers, dict) else entry_or_headers
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return None


def redact_value(name: str, value: str) -> str:
    if name.lower() in ("authorization", "cookie", "set-cookie",
                        "x-csrf-token", "x-requestverificationtoken"):
        if len(value) > 60:
            return f"{value[:30]}...[REDACTED {len(value)-45} chars]...{value[-15:]}"
    return value


def print_summary(entries: list[dict]) -> None:
    by_host = Counter()
    by_method = Counter()
    by_status = Counter()
    unique_endpoints: set[str] = set()
    for e in entries:
        url = e["request"]["url"]
        u = urlparse(url)
        by_host[u.netloc] += 1
        by_method[e["request"]["method"]] += 1
        by_status[e["response"]["status"]] += 1
        unique_endpoints.add(f"{e['request']['method']:6s} {u.netloc}{u.path}")

    print(f"Total entries matched: {len(entries)}")
    print()
    print("By host:")
    for host, n in by_host.most_common():
        print(f"  {n:6d}  {host}")
    print()
    print("By method:")
    for m, n in by_method.most_common():
        print(f"  {n:6d}  {m}")
    print()
    print("By status:")
    for s, n in sorted(by_status.items()):
        print(f"  {n:6d}  {s}")
    print()
    print(f"Unique METHOD path: {len(unique_endpoints)}")
    print("(Use --endpoints to list them, --url <substring> to drill in)")


def print_hosts(entries: list[dict]) -> None:
    hosts = Counter(urlparse(e["request"]["url"]).netloc for e in entries)
    for host, n in hosts.most_common():
        print(f"{n:6d}  {host}")


def print_endpoints(entries: list[dict]) -> None:
    eps = Counter()
    for e in entries:
        u = urlparse(e["request"]["url"])
        eps[(e["request"]["method"], u.netloc, u.path)] += 1
    for (m, host, path), n in sorted(eps.items(), key=lambda x: -x[1]):
        print(f"{n:5d}  {m:6s}  {host}{path}")


def print_list(matches: list[tuple[int, dict]], max_url: int = 140) -> None:
    for idx, e in matches:
        url = e["request"]["url"]
        if len(url) > max_url:
            url = url[:max_url - 3] + "..."
        print(f"#{idx:6d}  {e['response']['status']:4d}  {e['request']['method']:6s}  {url}")


def print_entry(idx: int, e: dict, max_body: int = 4000,
                headers_only: bool = False, redact: bool = True) -> None:
    req, resp = e["request"], e["response"]
    print(f"=== Entry #{idx} ===")
    print(f"Time: {e['startedDateTime']}    Duration: {e.get('time', 0):.0f}ms")
    print()
    print(f"REQUEST: {req['method']} {req['url']}")
    if req.get("queryString"):
        print()
        print("Query string:")
        for q in req["queryString"]:
            print(f"  {q['name']} = {q['value']}")
    print()
    print(f"Request headers ({len(req.get('headers', []))}):")
    for h in req.get("headers", []):
        v = redact_value(h["name"], h["value"]) if redact else h["value"]
        print(f"  {h['name']}: {v}")
    if req.get("cookies"):
        print()
        print(f"Request cookies ({len(req['cookies'])}):")
        for c in req["cookies"]:
            v = c.get("value", "")
            if redact and len(v) > 40:
                v = f"{v[:20]}...[REDACTED]..."
            print(f"  {c['name']} = {v}")
    if not headers_only and req.get("postData"):
        body = req["postData"].get("text", "")
        mime = req["postData"].get("mimeType", "")
        print()
        print(f"Request body ({mime}, {len(body)} chars):")
        if max_body and len(body) > max_body:
            body = body[:max_body] + f"\n... [truncated {len(body)-max_body} more chars; use --max-body 0 to see all]"
        print(body)
    print()
    print(f"RESPONSE: {resp['status']} {resp.get('statusText', '')}")
    print()
    print(f"Response headers ({len(resp.get('headers', []))}):")
    for h in resp.get("headers", []):
        v = redact_value(h["name"], h["value"]) if redact else h["value"]
        print(f"  {h['name']}: {v}")
    if resp.get("cookies"):
        print()
        print(f"Set cookies ({len(resp['cookies'])}):")
        for c in resp["cookies"]:
            v = c.get("value", "")
            if redact and len(v) > 40:
                v = f"{v[:20]}...[REDACTED]..."
            print(f"  {c['name']} = {v}")
    if not headers_only:
        content = resp.get("content") or {}
        body = content.get("text", "")
        mime = content.get("mimeType", "")
        size = content.get("size", 0)
        print()
        print(f"Response body ({mime}, content.size={size}, captured={len(body)} chars):")
        if body:
            if max_body and len(body) > max_body:
                body = body[:max_body] + f"\n... [truncated {size - max_body if size > max_body else 0} more chars; use --max-body 0 to see all]"
            print(body)
        else:
            print("  [empty or not captured]")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description="Survey + drill into a HAR file's network activity.",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__)
    ap.add_argument("har_file")
    ap.add_argument("--url", help="URL contains substring (case-insensitive)")
    ap.add_argument("--url-regex", help="URL matches Python regex")
    ap.add_argument("--method", help="Filter by HTTP method")
    ap.add_argument("--status", type=int, help="Filter by response status code")
    ap.add_argument("--content-type", help="Filter by response Content-Type substring")
    ap.add_argument("--has-body", action="store_true", help="Only entries whose request has a body")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--show", type=int, metavar="N")
    ap.add_argument("--detail", type=int, metavar="N", help="Drill into entry #N (1-indexed)")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--hosts", action="store_true")
    ap.add_argument("--endpoints", action="store_true")
    ap.add_argument("--max-body", type=int, default=4000)
    ap.add_argument("--headers-only", action="store_true")
    ap.add_argument("--no-redact", action="store_true",
                    help="Show full Authorization/Cookie values (default redacts long ones)")
    ap.add_argument("--raw-body", type=int, metavar="N",
                    help="Print raw response body of entry #N to stdout (no formatting)")
    args = ap.parse_args()

    entries = load_har(args.har_file)

    if args.raw_body:
        if args.raw_body < 1 or args.raw_body > len(entries):
            print(f"Entry #{args.raw_body} out of range (1..{len(entries)})", file=sys.stderr)
            return 1
        e = entries[args.raw_body - 1]
        body = (e["response"].get("content") or {}).get("text", "")
        sys.stdout.write(body)
        return 0

    matches = filter_entries(
        entries,
        url=args.url, url_regex=args.url_regex, method=args.method,
        status=args.status, content_type=args.content_type, has_body=args.has_body,
    )
    print(f"[har-scan] Filter matched {len(matches)} of {len(entries)} entries", file=sys.stderr)

    redact = not args.no_redact

    if args.detail:
        target = next(((i, e) for i, e in matches if i == args.detail), None)
        if target is None:
            target = next(((i, e) for i, e in enumerate(entries, start=1) if i == args.detail), None)
            if target is None:
                print(f"Entry #{args.detail} out of range", file=sys.stderr)
                return 1
        idx, e = target
        print_entry(idx, e, args.max_body, args.headers_only, redact)
    elif args.show:
        for k, (idx, e) in enumerate(matches[: args.show]):
            print_entry(idx, e, args.max_body, args.headers_only, redact)
            if k < min(args.show, len(matches)) - 1:
                print()
    elif args.list:
        print_list(matches)
    elif args.hosts:
        print_hosts([e for _, e in matches])
    elif args.endpoints:
        print_endpoints([e for _, e in matches])
    else:
        print_summary([e for _, e in matches])

    return 0


if __name__ == "__main__":
    sys.exit(main())
