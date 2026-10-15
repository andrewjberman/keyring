#!/usr/bin/env python
"""portal_lookup.py -- the ONLY sanctioned mechanism for answering portal-data questions.

Read-only, structured retrieval from opal-data-portal-v2 (S3) and the news DDB tables,
built so the truncation-misread class is structurally impossible:

  * every listing paginates to completion (token walk) -- a page is never a total;
  * every retrieval prints DENOMINATORS (keys enumerated / matched / read) in the output;
  * objects are read WHOLE and size-verified; gzip ContentEncoding is decoded;
  * objects > 1MB print a schema summary -- retrieve the sub-key you need with --project;
  * the big news table is QUERY-only by date (a full scan of 298k items is refused);
  * any partial/failed retrieval exits NONZERO and says PARTIAL loudly -- report that as
    a retrieval failure, NEVER as "no coverage" (refs/PORTAL_RETRIEVAL.md).

Usage:
  python portal_lookup.py channels
  python portal_lookup.py list <channel> [--match SUB]
  python portal_lookup.py get <channel> <key-or-suffix> [--project a.b.0.c]... [--find SUB] [--full]
  python portal_lookup.py ddb-tables
  python portal_lookup.py ddb-query <table> <key-value> [--limit N]
  python portal_lookup.py ddb-scan <table> [--limit N]        # small tables only

ONE-CALL RETRIEVAL+EXTRACTION (OPAL_ANALYST sec11 S5): `get` extracts in-process --
  --find SUB      case-insensitive KEY-substring walk of the retrieved object: prints every
                  matching field's dot-path + value, with the walk's denominator. The path it
                  prints is --project's input, so unknown-path lookups are ONE subprocess.
  --project PATH  repeatable: each path prints its own PROJECTION (several fields, one call).

This tool performs NO writes. It has no put/delete/update code path.
ASCII-only output (CLAUDE.md code-quality rule). Requires boto3 + stdlib.
Channel map surveyed 2026-08-06; human-readable twin: refs/PORTAL_RETRIEVAL.md.
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys

import boto3

BUCKET = "opal-data-portal-v2"
SUMMARY_BYTES = 1 * 1024 * 1024   # objects above this print a schema summary unless --project/--full
MAX_OBJECT_BYTES = 64 * 1024 * 1024

# name -> {prefix, date_field, note}. Twin of refs/PORTAL_RETRIEVAL.md -- keep in sync.
CHANNELS: dict = {
    "macro":           {"prefix": "json/macro/",            "date_field": "data_as_of",
                        "note": "macro_data.json + macro_data_fred.json + timeseries/{tenor}.json (84 objects)"},
    "valuation":       {"prefix": "json/valuation/",        "date_field": "data_as_of",
                        "note": "valuation_data.json 2.2MB (PROJECT sub-keys) + risk_premium_data.json (ERP, IG/HY OAS)"},
    "sentiment":       {"prefix": "json/sentiment/",        "date_field": "generated_at",
                        "note": "fear-greed-index.json + keyword-sentiments.json + keyword-history-articles/{kw}.json (722 objects)"},
    "positioning":     {"prefix": "json/positioning/",      "date_field": "data_as_of",
                        "note": "positioning_data.json is GZIP-encoded (handled here); holdings_attribution 368KB"},
    "correlations":    {"prefix": "json/correlations/",     "date_field": "data_as_of",
                        "note": "correlation_data.json 152KB"},
    "factor-tilts":    {"prefix": "json/factor-tilts/",     "date_field": "data_as_of",
                        "note": "tier1/tier2 small; tier3-timeseries 3.7MB (PROJECT)"},
    "peers":           {"prefix": "json/peers/",            "date_field": "data_as_of",
                        "note": "month-end basis -- a month-old data_as_of is its NORMAL cadence"},
    "market-regime":   {"prefix": "json/market/",           "date_field": "data_as_of",
                        "note": "market-regime.json + 715KB history"},
    "trending":        {"prefix": "json/trending/",         "date_field": "data_as_of",
                        "note": "latest.json: bullish[10]/bearish[10] with analysis+tickers (semantic-trending is FROZEN -- not served)"},
    "benchmarks":      {"prefix": "json/benchmarks/",       "date_field": "data_as_of",
                        "note": "6 JSON views incl. model_portfolio_benchmarks; NEVER the top-level benchmarks/*.pkl"},
    "mdpf-platinum":   {"prefix": "platinum/mdpf/",         "date_field": "as_of_date",
                        "note": "richest MDPF surface: per-firm mirrors; aggregate_aua daily snapshots (2024-11 on) now sit only under archive/. The legacy json/mdpf/ channel is retired: 0 keys at the G3 measurement 2026-10-14"},
    "pipeline-status": {"prefix": "json/latest/",           "date_field": "generated_at",
                        "note": "manifest.json: last Yang pipeline run + inputs"},
}

# table -> {hash_key, scan_ok, note}. QUERY by hash key is the default access pattern.
DDB_TABLES: dict = {
    "opal-news-articles":        {"hash_key": "article_date", "scan_ok": False,
                                  "note": "298k items -- QUERY by article_date YYYY-MM-DD ONLY; ~350 items/day. FinBERT sentiment per article"},
    "opal-news-trending-daily":  {"hash_key": "date",         "scan_ok": False,
                                  "note": "QUERY by date; ~20 fat items/day (headline, analysis, momentum, tickers)"},
    "opal-keyword-intelligence": {"hash_key": "keyword",      "scan_ok": False,
                                  "note": "QUERY by keyword (or ask by date -- GSI date-index)"},
    "seeking-alpha-article-urls": {"hash_key": "run_date",    "scan_ok": False,
                                  "note": "QUERY by run_date e.g. 2026-04-12_news; URL registry only"},
}


def die_partial(msg: str) -> None:
    print(f"PARTIAL-RETRIEVAL: {msg}")
    print("REPORT THIS AS A RETRIEVAL FAILURE, NOT AS MISSING DATA.")
    sys.exit(2)


def list_keys(prefix: str, match: str | None = None):
    s3 = boto3.client("s3")
    keys, token, pages = [], None, 0
    while True:
        kw = {"Bucket": BUCKET, "Prefix": prefix, "MaxKeys": 1000}
        if token:
            kw["ContinuationToken"] = token
        try:
            resp = s3.list_objects_v2(**kw)
        except Exception as e:  # noqa: BLE001 -- loud typed message beats a stack trace here
            die_partial(f"list_objects_v2 failed on page {pages + 1}: {e}")
        pages += 1
        keys.extend(o["Key"] for o in resp.get("Contents", []))
        if not resp.get("IsTruncated"):
            break
        token = resp.get("NextContinuationToken")
        if not token:
            die_partial(f"IsTruncated with no NextContinuationToken after {len(keys)} keys")
    matched = [k for k in keys if match.lower() in k.lower()] if match else keys
    return keys, matched, pages


def fetch_object(key: str):
    """head + get + size-verify + gzip-decode. Returns (bytes, head)."""
    s3 = boto3.client("s3")
    try:
        head = s3.head_object(Bucket=BUCKET, Key=key)
    except Exception as e:  # noqa: BLE001
        die_partial(f"head_object({key}) failed: {e}")
    size = head["ContentLength"]
    if size > MAX_OBJECT_BYTES:
        die_partial(f"{key} is {size} bytes (> {MAX_OBJECT_BYTES}) -- narrow the request")
    try:
        body = s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()
    except Exception as e:  # noqa: BLE001
        die_partial(f"get_object({key}) failed: {e}")
    if len(body) != size:
        die_partial(f"read {len(body)} of {size} bytes for {key}")
    if head.get("ContentEncoding") == "gzip" or body[:2] == b"\x1f\x8b":
        try:
            body = gzip.decompress(body)
            print(f"(gzip ContentEncoding decoded: {size} -> {len(body)} bytes)")
        except OSError as e:
            die_partial(f"gzip decode failed for {key}: {e}")
    return body, head


def project(doc, path: str):
    """Walk a.b.0.c through dicts/lists."""
    cur = doc
    for part in path.split("."):
        if isinstance(cur, list):
            try:
                cur = cur[int(part)]
            except (ValueError, IndexError):
                return None, f"list index '{part}' invalid (len {len(cur)})"
        elif isinstance(cur, dict):
            if part not in cur:
                return None, f"key '{part}' absent; siblings: {list(cur)[:20]}"
            cur = cur[part]
        else:
            return None, f"cannot descend into {type(cur).__name__} at '{part}'"
    return cur, None


def find_fields(doc, sub: str, path: str = ""):
    """Recursive KEY-substring walk (sec11 S5 one-call extraction). Returns (matches, walked):
    matches = [(dot-path, value)] for every dict key containing sub case-insensitively;
    walked = every dict key visited -- the denominator, so a 0 arrives with the frame that
    makes it evidence of absence rather than a bare zero."""
    matches, walked = [], 0
    if isinstance(doc, dict):
        for k, v in doc.items():
            walked += 1
            p = f"{path}.{k}" if path else str(k)
            if sub.lower() in str(k).lower():
                matches.append((p, v))
            m, w = find_fields(v, sub, p)
            matches.extend(m)
            walked += w
    elif isinstance(doc, list):
        for i, v in enumerate(doc):
            m, w = find_fields(v, sub, f"{path}.{i}" if path else str(i))
            matches.extend(m)
            walked += w
    return matches, walked


def render_value(v) -> str:
    """One-line value render for --find output: scalars whole (capped, cap stated), containers
    as shape -- drill a container with --project <its printed path>."""
    if isinstance(v, dict):
        return f"dict({len(v)} keys)"
    if isinstance(v, list):
        return f"list[{len(v)}]"
    s = json.dumps(v, default=str)
    return s if len(s) <= 200 else s[:200] + f"... ({len(s)} chars total)"


def summarize(doc, indent: str = "  ") -> None:
    if isinstance(doc, dict):
        for k, v in doc.items():
            if isinstance(v, dict):
                print(f"{indent}{k}: dict({len(v)} keys)")
            elif isinstance(v, list):
                print(f"{indent}{k}: list[{len(v)}]")
            else:
                sv = str(v)
                print(f"{indent}{k}: {sv[:80]}")
    elif isinstance(doc, list):
        print(f"{indent}list[{len(doc)}]; first element:")
        if doc:
            summarize(doc[0], indent + "  ")


def cmd_channels(_args) -> None:
    print(f"CHANNELS: {len(CHANNELS)} servable (bucket {BUCKET})")
    for name, c in CHANNELS.items():
        print(f"  {name:16s} s3://{BUCKET}/{c['prefix']:24s} vintage={c['date_field']}")
        print(f"  {'':16s} {c['note']}")


def cmd_list(args) -> None:
    c = CHANNELS.get(args.channel)
    if not c:
        print(f"UNKNOWN CHANNEL '{args.channel}'. Known: {', '.join(CHANNELS)}")
        sys.exit(1)
    keys, matched, pages = list_keys(c["prefix"], args.match)
    print(f"DENOMINATOR: {len(keys)} keys enumerated under {c['prefix']} "
          f"({pages} page(s), COMPLETE walk); {len(matched)} matched.")
    for k in matched[:500]:
        print(f"  {k}")
    if len(matched) > 500:
        print(f"  ... ({len(matched) - 500} more matched keys not printed -- narrow --match)")
    if args.match and not matched and keys:
        print(f"NOTE: 0 matches for '{args.match}' in a COMPLETE {len(keys)}-key listing "
              f"-- this IS evidence of absence (the walk completed).")


def cmd_get(args) -> None:
    c = CHANNELS.get(args.channel)
    if not c:
        print(f"UNKNOWN CHANNEL '{args.channel}'. Known: {', '.join(CHANNELS)}")
        sys.exit(1)
    key = args.key
    if not key.startswith(c["prefix"]):
        keys, matched, _ = list_keys(c["prefix"], key)
        if len(matched) == 1:
            key = matched[0]
            print(f"RESOLVED '{args.key}' -> {key} (1 of {len(keys)} keys matched)")
        elif not matched:
            print(f"NO KEY matching '{args.key}' in a COMPLETE {len(keys)}-key walk of "
                  f"{c['prefix']} -- absence is real here.")
            sys.exit(1)
        else:
            print(f"AMBIGUOUS: '{args.key}' matches {len(matched)} of {len(keys)} keys. Narrow it:")
            for k in matched[:20]:
                print(f"  {k}")
            sys.exit(1)
    body, head = fetch_object(key)
    print(f"OBJECT: s3://{BUCKET}/{key}  ({len(body)} bytes, read COMPLETE)")
    print(f"WRITE TIME (LastModified): {head['LastModified']}")
    try:
        doc = json.loads(body)
    except json.JSONDecodeError:
        print("(not JSON -- raw first 4000 chars below)")
        print(body[:4000].decode("utf-8", errors="replace"))
        return
    df = c.get("date_field")
    # VINTAGE ORDER (CTO msg 33851): the channel's date_field, then _provenance.source_vintages,
    # then nothing -- LastModified is the WRITE TIME and is never reported as a vintage.
    sv = {}
    if isinstance(doc, dict):
        prov = doc.get("_provenance")
        if isinstance(prov, dict) and isinstance(prov.get("source_vintages"), dict):
            sv = prov["source_vintages"]
    dates = sorted({str(v) for v in sv.values() if v})
    if df and isinstance(doc, dict) and df in doc:
        print(f"VINTAGE ({df}): {doc[df]}  <- quote this with every figure")
    elif len(dates) == 1:
        print(f"VINTAGE (_provenance.source_vintages): {dates[0]}  "
              f"<- quote this with every figure")
    elif dates:
        for src, val in sorted(sv.items()):
            print(f"  {src}={val}")
        print(f"VINTAGE (_provenance.source_vintages, oldest of {len(dates)}): {dates[0]}  "
              f"<- quote this with every figure")
    else:
        print(f"VINTAGE: none in the object -- LastModified {head['LastModified']} is the "
              f"WRITE TIME (claim: inferred), never the data vintage; say so when quoting")
    extracted = False
    for path in (args.project or []):
        sub, err = project(doc, path)
        if err:
            print(f"PROJECT FAILED at '{path}': {err}")
            sys.exit(1)
        print(f"PROJECTION {path}:")
        print(json.dumps(sub, indent=2, default=str))
        extracted = True
    if args.find:
        matches, walked = find_fields(doc, args.find)
        print(f"FIND '{args.find}': {len(matches)} match(es) across {walked} keys walked "
              f"(COMPLETE walk of the retrieved object).")
        for p, v in matches[:200]:
            print(f"  {p} = {render_value(v)}")
        if len(matches) > 200:
            print(f"  ... ({len(matches) - 200} more matched keys not printed -- narrow the "
                  f"term or --project one of the paths above)")
        if not matches:
            print("  0 matches in a COMPLETE walk -- absence of the field is real here.")
        extracted = True
    if not extracted:
        if len(body) > SUMMARY_BYTES and not args.full:
            print(f"LARGE OBJECT ({len(body)} bytes > {SUMMARY_BYTES}): schema summary below; "
                  f"use --project a.b.c for the piece you need (--full to force a dump).")
            summarize(doc)
        else:
            print(json.dumps(doc, indent=2, default=str))


def cmd_ddb_tables(_args) -> None:
    print(f"SERVABLE DDB TABLES: {len(DDB_TABLES)}")
    for name, t in DDB_TABLES.items():
        print(f"  {name:28s} query-key={t['hash_key']:14s} {t['note']}")


def cmd_ddb_query(args) -> None:
    t = DDB_TABLES.get(args.table)
    if not t:
        print(f"UNKNOWN TABLE '{args.table}'. Known: {', '.join(DDB_TABLES)}")
        sys.exit(1)
    ddb = boto3.client("dynamodb")
    items, token, pages = [], None, 0
    while True:
        kw = {
            "TableName": args.table,
            "KeyConditionExpression": "#hk = :v",
            "ExpressionAttributeNames": {"#hk": t["hash_key"]},
            "ExpressionAttributeValues": {":v": {"S": args.value}},
        }
        if token:
            kw["ExclusiveStartKey"] = token
        try:
            resp = ddb.query(**kw)
        except Exception as e:  # noqa: BLE001
            die_partial(f"query({args.table}, {t['hash_key']}={args.value}) failed page {pages + 1}: {e}")
        pages += 1
        items.extend(resp.get("Items", []))
        token = resp.get("LastEvaluatedKey")
        if not token:
            break
    shown = items[: args.limit] if args.limit else items
    print(f"DENOMINATOR: {len(items)} item(s) for {t['hash_key']}='{args.value}' "
          f"({pages} page(s), COMPLETE walk); showing {len(shown)}.")
    if args.limit and len(items) > args.limit:
        print("NOTE: display truncated by --limit; the COUNT above is the real total.")
    for it in shown:
        print(json.dumps(it, default=str))


def cmd_ddb_scan(args) -> None:
    t = DDB_TABLES.get(args.table)
    if not t:
        print(f"UNKNOWN TABLE '{args.table}'. Known: {', '.join(DDB_TABLES)}")
        sys.exit(1)
    if not t.get("scan_ok"):
        print(f"SCAN REFUSED for {args.table}: this table is QUERY-only "
              f"(key {t['hash_key']}). A full scan reads the whole table (hundreds of MB "
              f"on the news table) and a partial scan invites the sample-as-total error. "
              f"Use: ddb-query {args.table} <{t['hash_key']}-value>")
        sys.exit(1)
    # (No scan_ok table is currently registered; the path exists for future small tables.)
    print("No scan-permitted tables registered.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("channels").set_defaults(fn=cmd_channels)
    lp = sub.add_parser("list")
    lp.add_argument("channel")
    lp.add_argument("--match")
    lp.set_defaults(fn=cmd_list)
    gp = sub.add_parser("get")
    gp.add_argument("channel")
    gp.add_argument("key")
    gp.add_argument("--project", action="append",
                    help="dot-path into the JSON, e.g. total.histogram or groups.0 "
                         "(repeatable -- each prints its own PROJECTION)")
    gp.add_argument("--find",
                    help="case-insensitive KEY-substring walk: every matching field's "
                         "dot-path + value, with the walk denominator (one-call "
                         "retrieval+extraction, sec11 S5)")
    gp.add_argument("--full", action="store_true", help="force full dump of a large object")
    gp.set_defaults(fn=cmd_get)
    sub.add_parser("ddb-tables").set_defaults(fn=cmd_ddb_tables)
    qp = sub.add_parser("ddb-query")
    qp.add_argument("table")
    qp.add_argument("value", help="hash-key value, e.g. 2026-08-06 or a keyword")
    qp.add_argument("--limit", type=int, default=0, help="display limit (count stays true)")
    qp.set_defaults(fn=cmd_ddb_query)
    sp = sub.add_parser("ddb-scan")
    sp.add_argument("table")
    sp.add_argument("--limit", type=int, default=0)
    sp.set_defaults(fn=cmd_ddb_scan)
    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
