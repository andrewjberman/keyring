#!/usr/bin/env python3
"""clobber_scan -- OUTPUT-KEY COLLISION scanner (comp-clobber engine).

Finds the class comp-dups CANNOT: two or more DISTINCT producers that write the SAME
sink (an S3 key, a DynamoDB table). comp-dups scans code/TF BODIES (same code, twice);
this scans WRITE TARGETS (different code, one destination) -- the "two writers race one
key" defect (the 2026-07-21 aum-timeseries freeze: build_legacy_compat_emit.py's frozen
11:30 emit clobbering the mdpf-daily-runner's fresh ~15:00 write of the SAME served key).

ADVISORY / read-only. STATIC mode finds candidates by CODE (2+ producer files that name the
same TERMINAL artifact). LIVE mode is the runtime ORACLE: version-history etag-lineage --
an etag family that REAPPEARS after a different one intervened = an ACTIVE clobber, and it
catches clobbers the static scan cannot (writers that reach one served key by different code
paths, e.g. a direct json/ write vs a platinum/->json publish).

  comp-clobber                       static scan: TERMINAL artifacts written by 2+ producers (ranked)
  comp-clobber --json                emit JSON
  comp-clobber --min-writers N       only sinks with >= N writers (default 2)
  comp-clobber --include-partitioned also show shared partitioned/prefix sinks (low signal)
  comp-clobber --path P [P ...]      restrict the static scan to these roots (default data/ infra/)
  comp-clobber --live BUCKET KEY     LIVE version-history etag-lineage confirm for one S3 key
  comp-clobber --sweep BUCKET PREFIX LIVE sweep -- interleave-check EVERY key under a prefix (find all
                                     actively-clobbered served artifacts in one pass)
  comp-clobber self-test             falsifiable unit tests of the interleave oracle + static

CAVEAT (static mode): keys are matched by literal path; a `Key=` without a same-window Bucket is
bucket-blind, so the SAME key path in two different buckets (e.g. bd vs inf `gold/trigger-pending.json`)
reads as a candidate but is NOT a clobber. The LIVE/sweep modes are bucket-exact and are the oracle.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))            # org/modules/graph
_WS = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))  # graph->modules->org->repo root

_HELD = ("data/black_diamond/", "data/canonical/schwab/silver/")
_SKIP_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "portal"}
_SCAN_EXT = (".py", ".sh", ".tf", ".json")

_WRITE_VERB = re.compile(
    r"put_object|upload_file|upload_fileobj|copy_object|"
    r"aws\s+s3\s+(?:cp|sync|mv)|s3\.(?:Object|meta)|"
    r"put_item|batch_write_item|update_item|TransactWriteItems|write_batch",
    re.I,
)
# GREEDY full-key literal after a known layer prefix (captures the whole path, not a stub).
_S3_KEY = re.compile(
    r"""["']((?:json|platinum|gold|silver|bronze|views|raw|portal|meta|uploads|processed)"""
    r"""/[A-Za-z0-9_./{}$*=-]+)["']"""
)
_S3_URL = re.compile(r"s3://([a-z0-9.-]+)/([A-Za-z0-9_./{}$*=-]+)")
_VAR_BIND = re.compile(r"""^\s*([A-Z_][A-Z0-9_]*)\s*=\s*["']([^"']+)["']""")
_DDB_TABLE = re.compile(r"""TableName\s*=\s*["']([A-Za-z0-9_.-]+)["']|Table\(\s*["']([A-Za-z0-9_.-]+)["']""")

_PART_RE = re.compile(r"\{\}|date=|/\*|partition|\$\{|%[sd]")


def _rel(p):
    return os.path.relpath(p, _WS).replace("\\", "/")


def _iter_files(roots):
    for root in roots:
        base = os.path.join(_WS, root)
        if os.path.isfile(base):
            yield base
            continue
        for dp, dns, fns in os.walk(base):
            dns[:] = [d for d in dns if d not in _SKIP_DIRS]
            for fn in fns:
                if fn.endswith(_SCAN_EXT):
                    yield os.path.join(dp, fn)


def _normalize_key(k):
    k = re.sub(r"\{[^}]*\}", "{}", k)
    k = re.sub(r"%[sd]", "{}", k)
    k = re.sub(r"\$\{?[A-Za-z_][A-Za-z0-9_]*\}?", "{}", k)
    k = re.sub(r"date=\d{4}-\d{2}-\d{2}", "date={}", k)
    return k.strip("/")


def _is_terminal(key):
    """A specific named artifact (a served file), NOT a partitioned/templated prefix."""
    if _PART_RE.search(key):
        return False
    return key.endswith((".json", ".csv")) or (key.endswith(".parquet") and "date=" not in key)


def detect_interleave(etags):
    """PURE oracle: an etag that reappears AFTER a different etag intervened = clobber signature.
    [A,A,B,B] -> no (monotonic progression). [A,B,A] -> {A} (A came back after B). """
    interleaved, order = set(), []
    for e in etags:
        if order and e in order[:-1] and order[-1] != e:
            interleaved.add(e)
        order.append(e)
    return interleaved


def static_scan(roots, min_writers=2, include_held=False, include_partitioned=False):
    sinks = {}

    def add(kind, key, f, line):
        key = _normalize_key(key) if kind == "s3" else key
        if not key:
            return
        rec = sinks.setdefault((kind, key), {"kind": kind, "key": key, "writers": {}})
        rec["writers"].setdefault(f, []).append(line)

    # PRECISION: a key counts as WRITTEN by a file only when it sits on/next to an actual
    # write CALL -- not merely present in a producer file (that over-counts READERS of a
    # shared key). We window each write call over its own line + the next 3 (Key= often
    # trails onto a following line in a multi-line put_object).
    for path in _iter_files(roots):
        rp = _rel(path)
        if not include_held and any(h in rp for h in _HELD):
            continue
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                lines = fh.readlines()
        except Exception:
            continue
        text = "".join(lines)
        if not _WRITE_VERB.search(text):
            continue
        var_keys = {}
        for m in _VAR_BIND.finditer(text):
            v = m.group(2)
            if _S3_KEY.match(f'"{v}"') or v.startswith("s3://"):
                var_keys[m.group(1)] = v
        n = len(lines)
        for i, ln in enumerate(lines, 1):
            if not _WRITE_VERB.search(ln):
                continue
            window = "".join(lines[i - 1:min(n, i + 3)])   # the call line + 3 trailing
            for m in _S3_KEY.finditer(window):
                add("s3", m.group(1), rp, i)
            for m in _S3_URL.finditer(window):
                add("s3", m.group(2), rp, i)
            for m in _DDB_TABLE.finditer(window):
                add("ddb", m.group(1) or m.group(2), rp, i)
            # a VAR-bound key referenced inside the write window
            for v, key in var_keys.items():
                if re.search(rf"\b{re.escape(v)}\b", window):
                    if key.startswith("s3://"):
                        mm = _S3_URL.search(key)
                        if mm:
                            add("s3", mm.group(2), rp, i)
                    else:
                        add("s3", key, rp, i)

    cols = []
    for rec in sinks.values():
        if len(rec["writers"]) < min_writers:
            continue
        terminal = rec["kind"] == "ddb" or _is_terminal(rec["key"])
        if not terminal and not include_partitioned:
            continue
        cols.append({**rec, "n_writers": len(rec["writers"]),
                     "writer_files": sorted(rec["writers"]), "terminal": terminal})
    # terminal (high-signal) first, then by writer count
    cols.sort(key=lambda r: (not r["terminal"], -r["n_writers"], r["key"]))
    return cols, len(sinks)


def live_confirm(bucket, key):
    import boto3
    s3 = boto3.client("s3")
    vers = sorted(
        (v for v in s3.list_object_versions(Bucket=bucket, Prefix=key).get("Versions", []) if v["Key"] == key),
        key=lambda x: x["LastModified"],
    )
    rows = [{"ts": v["LastModified"].isoformat(), "etag": v["ETag"].strip('"')[:8], "size": v["Size"]} for v in vers]
    interleaved = detect_interleave([r["etag"] for r in rows])
    return {"bucket": bucket, "key": key, "n_versions": len(rows),
            "distinct_etags": len({r["etag"] for r in rows}),
            "interleaved_etags": sorted(interleaved), "active_clobber": bool(interleaved),
            "recent": rows[-14:]}


def sweep(bucket, prefix, max_keys=400):
    """Run the interleave ORACLE across EVERY key under a prefix -- find all actively
    clobbered served artifacts in one pass (Andrew's 'run it on various call points')."""
    import boto3
    s3 = boto3.client("s3")
    # collect versions per key
    per_key = {}
    tok = None
    while True:
        kw = dict(Bucket=bucket, Prefix=prefix)
        if tok:
            kw["KeyMarker"] = tok
        resp = s3.list_object_versions(**kw)
        for v in resp.get("Versions", []):
            per_key.setdefault(v["Key"], []).append(v)
        if not resp.get("IsTruncated") or len(per_key) >= max_keys:
            break
        tok = resp.get("NextKeyMarker")
    hits = []
    for key, vs in sorted(per_key.items()):
        if len(vs) < 3:
            continue
        vs = sorted(vs, key=lambda x: x["LastModified"])
        etags = [v["ETag"].strip('"')[:8] for v in vs]
        inter = detect_interleave(etags)
        if inter:
            latest = vs[-1]
            hits.append({"key": key, "n_versions": len(vs), "distinct_etags": len(set(etags)),
                         "interleaved": sorted(inter),
                         "latest_ts": latest["LastModified"].isoformat(),
                         "latest_etag": latest["ETag"].strip('"')[:8]})
    return {"bucket": bucket, "prefix": prefix, "keys_scanned": len(per_key), "clobbered": hits}


def _fmt(cols, denom, min_writers, include_partitioned):
    out = ["=" * 78,
           "comp-clobber -- output-key collisions (2+ producers -> one sink). ADVISORY.",
           "=" * 78,
           f"scanned {denom} distinct write-sink(s); {len(cols)} multi-writer "
           f"(>= {min_writers}){'' if include_partitioned else ' [terminal artifacts only; --include-partitioned for prefixes]'}."]
    term = [c for c in cols if c["terminal"]]
    part = [c for c in cols if not c["terminal"]]
    if term:
        out.append("\n--- TERMINAL-ARTIFACT clobbers (HIGH signal: 2+ writers name one served file/table) ---")
    for c in term:
        out.append(f"\n[{c['kind'].upper()} CLOBBER x{c['n_writers']}]  {c['key']}")
        for f in c["writer_files"]:
            lns = c["writers"][f]
            loc = f"L{','.join(str(x) for x in lns[:4])}" if any(lns) else "(var-bound)"
            out.append(f"    <- {f}  {loc}")
    if part:
        out.append(f"\n--- PARTITIONED/PREFIX collisions ({len(part)}; low signal -- shared pipeline prefixes) ---")
        for c in part[:15]:
            out.append(f"  [x{c['n_writers']}] {c['key']}")
    if not cols:
        out.append("  (no multi-writer terminal sinks in scope)")
    out.append("\n>> STATIC = a code CANDIDATE. The ORACLE is runtime: comp-clobber --live <bucket> <key>")
    out.append("   (an etag-lineage that REAPPEARS after another intervened = an ACTIVE clobber;")
    out.append("    catches writers that reach one key by different paths, e.g. json/ direct vs platinum/->json publish).")
    return "\n".join(out)


def _self_test():
    print("clobber_scan self-test:")
    # 1. interleave oracle -- the heart of the LIVE clobber detection (deterministic)
    clob = detect_interleave(["a", "b", "c", "a"])                # a returns after b,c -> {a}
    prog = detect_interleave(["a", "a", "b", "b", "c"])           # monotonic -> NOT a clobber
    t1 = clob == {"a"}
    t2 = prog == set()
    # the exact aum-timeseries shape (fresh etags interleaved with a frozen one)
    aum = detect_interleave(["fb", "fb", "x1", "fb", "x2", "fb", "x3", "fb", "fb"])
    t3 = "fb" in aum
    print(f"  [interleave: A,A,B,A,B,A -> {{a}}]        {'PASS' if t1 else 'FAIL'} ({sorted(clob)})")
    print(f"  [progression: A,A,B,B,C -> no clobber]  {'PASS' if t2 else 'FAIL'} ({sorted(prog)})")
    print(f"  [aum-shape: frozen fb reappears]        {'PASS' if t3 else 'FAIL'} ({sorted(aum)})")
    # 2. static scan runs + a fabricated terminal key is absent (negative control)
    cols, denom = static_scan(["data", "infra"])
    t4 = denom > 0
    t5 = not any(c["key"] == "json/does-not-exist-xyzzy.json" for c in cols)
    print(f"  [static: scanned sinks > 0]             {'PASS' if t4 else 'FAIL'} (denom={denom})")
    print(f"  [static: fabricated key absent]         {'PASS' if t5 else 'FAIL'}")
    ok = all([t1, t2, t3, t4, t5])
    print(f"  => {'PASS 5/5' if ok else 'FAIL'}")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(prog="comp-clobber", description="output-key collision scanner")
    ap.add_argument("mode", nargs="?", default="scan", choices=["scan", "self-test"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--min-writers", type=int, default=2)
    ap.add_argument("--include-partitioned", action="store_true")
    ap.add_argument("--path", nargs="+", default=None)
    ap.add_argument("--live", nargs=2, metavar=("BUCKET", "KEY"), default=None)
    ap.add_argument("--sweep", nargs=2, metavar=("BUCKET", "PREFIX"), default=None)
    ap.add_argument("--allow-held", action="store_true")
    args = ap.parse_args(argv)

    if args.mode == "self-test":
        return _self_test()
    if args.sweep:
        res = sweep(args.sweep[0], args.sweep[1])
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"LIVE sweep  s3://{res['bucket']}/{res['prefix']}  "
                  f"({res['keys_scanned']} keys; {len(res['clobbered'])} ACTIVELY CLOBBERED)")
            for h in res["clobbered"]:
                print(f"  !! {h['key']}  versions={h['n_versions']} etags={h['distinct_etags']} "
                      f"interleaved={h['interleaved']}  latest={h['latest_ts']} ({h['latest_etag']})")
            if not res["clobbered"]:
                print("  (no interleaved etag-lineages -- no active clobber under this prefix)")
        return 0
    if args.live:
        res = live_confirm(args.live[0], args.live[1])
        if args.json:
            print(json.dumps(res, indent=2))
        else:
            print(f"LIVE clobber-check  s3://{res['bucket']}/{res['key']}")
            print(f"  versions={res['n_versions']}  distinct_etags={res['distinct_etags']}  "
                  f"ACTIVE_CLOBBER={res['active_clobber']}  interleaved={res['interleaved_etags']}")
            for r in res["recent"]:
                print(f"    {r['ts']}  etag={r['etag']}  size={r['size']}")
        return 0

    roots = args.path or ["data", "infra"]
    cols, denom = static_scan(roots, args.min_writers, args.allow_held, args.include_partitioned)
    if args.json:
        print(json.dumps({"denominator": denom, "collisions": cols}, indent=2))
    else:
        print(_fmt(cols, denom, args.min_writers, args.include_partitioned))
    return 0


if __name__ == "__main__":
    sys.exit(main())
