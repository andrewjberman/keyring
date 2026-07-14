"""
comp-icedrill -- drill an artifact to its VERSION / PARTITION history across the substrates we
actually have. The vintage (data-time) axis, the complement to comp-gitdrill's producer (code-time)
axis.

WHY (NFRA_INSTDRILL item 7, 2026-07-14, Andrew-direct). "How did THIS served artifact version over
time" had no single tool -- the answer lived in whichever substrate happened to hold it (dated S3
partitions / S3 object versions / a DynamoDB daily bucket / the Nessie-versioned graph). This drills
it, and the provenance header ALWAYS names WHICH substrate answered and its COMPLETENESS -- a
partition series is not a full version history, and the tool says so rather than implying more than
the substrate carries.

SUBSTRATE NOTE (CVO~Z correction of record, 7a04cd236): the graph estate IS versioned to Iceberg
tables via pyiceberg + Nessie (comp-aws iceberg-commit; the deployed pyiceberg-nessie-deps layer) --
so graph-node vintages come from comp-kuzu's provenance header essentially free. The DATA pipelines
are NOT on Iceberg (verified). Whether DATA artifacts ever move onto Iceberg is a separate substrate
decision for Andrew; v1 drills the substrates that exist and NEVER fabricates an Iceberg history for
a data artifact that has none.

Read-only: ListObjectsV2 / list_object_versions / DDB query -- no writes, no body reads for the
partition axis (Size is in the listing).

Usage:
    comp-icedrill s3://bucket/prefix/           # dated-partition series under a {date} grammar prefix
    comp-icedrill s3://bucket/key.json          # object-version series for a concrete versioned key
    comp-icedrill ddb <table> [--pk <prefix>]   # DynamoDB daily-bucket item vintages
    comp-icedrill graph <node>                  # -> comp-kuzu provenance (the Nessie vintage), pointer
    comp-icedrill --json ...
    comp-icedrill --self-test                   # offline: partition/version extraction parity (stub client)

Author: 1.0.0_SA_CTO~Z (NFRA_INSTDRILL item 7). 2026-07-14. Read-only.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))

_DATE_RX = re.compile(r"(\d{4}-\d{2}-\d{2}|\d{4}/\d{2}/\d{2}|\d{8})")


def _s3():
    import boto3  # lazy; self-test injects a stub
    return boto3.client("s3")


def _split_uri(uri: str):
    m = re.match(r"s3://([^/]+)/(.*)$", uri)
    return (m.group(1), m.group(2)) if m else (None, None)


def dated_partitions(client, bucket: str, prefix: str, max_keys: int = 2000) -> dict:
    """The DATED-PARTITION substrate: keys under a {date}-grammar prefix, one vintage per date found
    in the key. COMPLETENESS: this is the set of dates PRESENT -- a gap is a missing partition, and a
    present date is not proof the partition is complete (that's comp-freshness's job)."""
    token, keys = None, []
    while True:
        kw = {"Bucket": bucket, "Prefix": prefix, "MaxKeys": 1000}
        if token:
            kw["ContinuationToken"] = token
        resp = client.list_objects_v2(**kw)
        for o in resp.get("Contents", []):
            keys.append((o["Key"], o.get("LastModified"), o.get("Size"), o.get("ETag")))
        token = resp.get("NextContinuationToken")
        if not token or len(keys) >= max_keys:
            break
    vintages = {}
    for key, lm, size, etag in keys:
        m = _DATE_RX.search(key)
        if not m:
            continue
        d = m.group(1).replace("/", "-")
        if len(d) == 8:
            d = "%s-%s-%s" % (d[:4], d[4:6], d[6:])
        vintages.setdefault(d, {"date": d, "keys": 0, "example": key,
                                "last_modified": str(lm) if lm else None})
        vintages[d]["keys"] += 1
    series = sorted(vintages.values(), key=lambda v: v["date"])
    return {"substrate": "s3-dated-partitions", "bucket": bucket, "prefix": prefix,
            "completeness": "dates PRESENT under the prefix; a missing date is a missing partition; "
                            "presence is not completeness (use comp-freshness for that)",
            "n_keys_scanned": len(keys), "n_vintages": len(series), "vintages": series}


def object_versions(client, bucket: str, key: str, max_versions: int = 200) -> dict:
    """The OBJECT-VERSION substrate: list_object_versions on a concrete key (needs bucket versioning).
    COMPLETENESS: the full retained version history IF versioning was on for the whole window; a
    version list on a never-versioned bucket is EMPTY, which is not 'the value never changed'."""
    resp = client.list_object_versions(Bucket=bucket, Prefix=key, MaxKeys=max_versions)
    versions = []
    for v in resp.get("Versions", []):
        if v.get("Key") != key:
            continue
        versions.append({"version_id": v.get("VersionId"), "last_modified": str(v.get("LastModified")),
                         "size": v.get("Size"), "etag": (v.get("ETag") or "").strip('"'),
                         "is_latest": v.get("IsLatest", False)})
    versions.sort(key=lambda x: x["last_modified"])
    note = ("full retained version history" if versions
            else "NO versions returned -- either the key does not exist OR the bucket is not "
                 "versioned. EMPTY here is NOT 'the value never changed'")
    return {"substrate": "s3-object-versions", "bucket": bucket, "key": key,
            "completeness": note, "n_versions": len(versions), "vintages": versions}


def _render(d: dict) -> str:
    L = ["comp-icedrill -- vintage drill",
         "  SUBSTRATE: %s" % d.get("substrate"),
         "  COMPLETENESS: %s" % d.get("completeness")]
    if "bucket" in d:
        L.append("  scope: s3://%s/%s" % (d["bucket"], d.get("prefix", d.get("key", ""))))
    vints = d.get("vintages", [])
    L.append("  %d vintage(s):" % len(vints))
    for v in vints[-40:]:
        if "version_id" in v:
            L.append("    %s  %s  %sB  etag=%s%s" % (
                v["last_modified"], (v["version_id"] or "")[:16], v.get("size"),
                (v.get("etag") or "")[:12], "  <- latest" if v.get("is_latest") else ""))
        else:
            L.append("    %s  keys=%-3d  e.g. %s" % (v["date"], v["keys"], v["example"]))
    if not vints:
        L.append("    (none -- see COMPLETENESS above; an empty result is a FINDING, not a clean)")
    return "\n".join(L)


def _self_test() -> int:
    """Offline: partition + version extraction parity against a stub S3 client (no AWS)."""
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    class StubS3:
        def __init__(self, contents=None, versions=None):
            self._c = contents or []
            self._v = versions or []
        def list_objects_v2(self, **kw):
            pref = kw.get("Prefix", "")
            return {"Contents": [o for o in self._c if o["Key"].startswith(pref)]}
        def list_object_versions(self, **kw):
            pref = kw.get("Prefix", "")
            return {"Versions": [v for v in self._v if v["Key"].startswith(pref)]}

    import datetime as _dt
    # dated-partition fixture: 3 dates, one with 2 keys.
    contents = [
        {"Key": "silver/x/2026-07-10/part-0.parquet", "LastModified": _dt.datetime(2026, 7, 10),
         "Size": 10, "ETag": "a"},
        {"Key": "silver/x/2026-07-11/part-0.parquet", "LastModified": _dt.datetime(2026, 7, 11),
         "Size": 11, "ETag": "b"},
        {"Key": "silver/x/2026-07-11/part-1.parquet", "LastModified": _dt.datetime(2026, 7, 11),
         "Size": 12, "ETag": "c"},
    ]
    d = dated_partitions(StubS3(contents), "buck", "silver/x/")
    dates = [v["date"] for v in d["vintages"]]
    ck("partitions.dates_extracted_sorted", dates == ["2026-07-10", "2026-07-11"], str(dates))
    ck("partitions.key_count_per_date",
       [v["keys"] for v in d["vintages"]] == [1, 2], "2026-07-11 has 2 keys")
    ck("partitions.completeness_disclaims", "presence is not completeness" in d["completeness"])

    # object-version fixture: 2 versions, newest last, is_latest surfaced.
    versions = [
        {"Key": "gold/served.json", "VersionId": "v1", "LastModified": _dt.datetime(2026, 7, 9),
         "Size": 100, "ETag": '"e1"', "IsLatest": False},
        {"Key": "gold/served.json", "VersionId": "v2", "LastModified": _dt.datetime(2026, 7, 12),
         "Size": 105, "ETag": '"e2"', "IsLatest": True},
    ]
    ov = object_versions(StubS3(versions=versions), "buck", "gold/served.json")
    ck("versions.count_and_order",
       [v["version_id"] for v in ov["vintages"]] == ["v1", "v2"], "oldest->newest")
    ck("versions.latest_flagged", ov["vintages"][-1]["is_latest"] is True)

    # THE ANTI-FABRICATION CONTROL: an empty version list is a FINDING, never 'never changed'.
    ov_empty = object_versions(StubS3(versions=[]), "buck", "gold/missing.json")
    ck("empty.is_a_finding_not_clean",
       ov_empty["n_versions"] == 0 and "NOT 'the value never changed'" in ov_empty["completeness"])

    ok = all(results)
    print("\n" + ("OK: partition/version parity holds; empty is a finding, substrate + completeness named"
                  if ok else "ERROR: comp-icedrill self-test FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-icedrill",
                                 description="drill an artifact's version/partition vintages across existing substrates (read-only)")
    ap.add_argument("target", nargs="?", help="s3://bucket/prefix or s3://bucket/key.json, or 'ddb'/'graph'")
    ap.add_argument("extra", nargs="?", help="ddb: table name | graph: node")
    ap.add_argument("--pk", default=None, help="ddb: partition-key prefix")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass

    if args.self_test:
        return _self_test()
    if not args.target:
        ap.print_help()
        return 2

    if args.target == "graph":
        node = args.extra or ""
        print("comp-icedrill: graph-node vintages live on the Nessie-versioned surface -- the ONE")
        print("frontier is comp-kuzu's provenance header (built-when / source vintage / commit-distance).")
        print("Run:  comp-kuzu --json \"MATCH (n) WHERE n.id = '%s' RETURN n\"  (reads the header on stderr)"
              % (node or "<id>"))
        print("(comp-icedrill does not re-implement the Nessie catalog read; it points at the ONE surface.)")
        return 0

    if args.target == "ddb":
        table = args.extra
        if not table:
            print("usage: comp-icedrill ddb <table> [--pk <prefix>]", file=sys.stderr)
            return 2
        # DDB daily buckets: defer to comp-freshness ddb (it owns the config + the read); point, not re-implement.
        print("comp-icedrill: DynamoDB daily-bucket vintages are owned by comp-freshness's ddb config.")
        print("Run:  comp-freshness ddb %s%s  (the item-freshness read)"
              % (table, (" --pattern %s" % args.pk) if args.pk else ""))
        return 0

    bucket, key = _split_uri(args.target)
    if not bucket:
        print("NOT AN S3 URI: %s (want s3://bucket/prefix or s3://bucket/key)" % args.target, file=sys.stderr)
        return 2

    client = _s3()
    # a concrete object key (has an extension) -> version history; else a prefix -> partition series.
    if key and re.search(r"\.[A-Za-z0-9]{1,6}$", key):
        d = object_versions(client, bucket, key)
    else:
        d = dated_partitions(client, bucket, key)
    if args.json:
        print(json.dumps(d, indent=1, default=str))
    else:
        print(_render(d))
    # empty vintage set is a FINDING (exit 3), never a silent clean.
    return 0 if d.get("vintages") else 3


if __name__ == "__main__":
    sys.exit(main())
