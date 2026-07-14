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


def dated_partitions(client, bucket: str, prefix: str, max_keys=None) -> dict:
    """The DATED-PARTITION substrate: keys under a {date}-grammar prefix, one vintage per date found
    in the key.

    PAGINATES TO EXHAUSTION BY DEFAULT (max_keys=None). Fixed 2026-07-14 after CVO~Z REFUTED my
    "matches an independent aws s3 ls" claim: this silently stopped at 2,000 keys
    (`len(keys) >= max_keys` broke the pagination loop), so the root scope reported 1,394 vintages
    against a true 2,273, and a SUBSCOPE reported EXACTLY 2000 -- child(2000) > parent(1394), an
    internal self-refutation that needed no external instrument. **A SILENT CAP IS THE EXACT CLASS
    THIS TOOL EXISTS TO CATCH, AND IT WAS IN THE TOOL.** My "independent" check had evidently shared
    the capped axis, which is why it agreed with itself.

    A cap is now OPT-IN and, when it BINDS, it is DISCLOSED (`truncated: True`, a loud line, and a
    nonzero exit) -- never a silent horizon presented as a complete answer.

    COMPLETENESS: the set of dates PRESENT under the prefix. A gap is a missing partition, and a
    present date is not proof the partition is complete (that is comp-freshness's job)."""
    token, keys = None, []
    pages = 0
    truncated = False
    while True:
        kw = {"Bucket": bucket, "Prefix": prefix, "MaxKeys": 1000}
        if token:
            kw["ContinuationToken"] = token
        resp = client.list_objects_v2(**kw)
        pages += 1
        for o in resp.get("Contents", []):
            keys.append((o["Key"], o.get("LastModified"), o.get("Size"), o.get("ETag")))
        token = resp.get("NextContinuationToken")
        if not token:
            break
        if max_keys is not None and len(keys) >= max_keys:
            truncated = True          # the cap BOUND and there was more -> say so, loudly
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
    completeness = ("dates PRESENT under the prefix (FULL listing, paginated to exhaustion: "
                    "%d keys over %d page(s)); a missing date is a missing partition; presence is "
                    "not completeness (use comp-freshness for that)" % (len(keys), pages))
    if truncated:
        completeness = ("!! TRUNCATED at %d keys (cap) -- this listing is INCOMPLETE and the vintage "
                        "set below is a LOWER BOUND. Re-run without --max-keys." % len(keys))
    return {"substrate": "s3-dated-partitions", "bucket": bucket, "prefix": prefix,
            "completeness": completeness,
            "n_keys_scanned": len(keys), "pages": pages, "truncated": truncated,
            "n_vintages": len(series), "vintages": series}


def object_versions(client, bucket: str, key: str, max_versions=None) -> dict:
    """The OBJECT-VERSION substrate: list_object_versions on a concrete key (needs bucket
    versioning). PAGINATES TO EXHAUSTION (same silent-cap fix as dated_partitions -- the old
    MaxKeys=200 was a horizon presented as a history).

    COMPLETENESS: the full retained version history IF versioning was on for the whole window; an
    EMPTY list on a never-versioned bucket is NOT 'the value never changed'."""
    versions = []
    kmark = vmark = None
    pages = 0
    truncated = False
    while True:
        kw = {"Bucket": bucket, "Prefix": key, "MaxKeys": 1000}
        if kmark:
            kw["KeyMarker"] = kmark
        if vmark:
            kw["VersionIdMarker"] = vmark
        resp = client.list_object_versions(**kw)
        pages += 1
        for v in resp.get("Versions", []):
            if v.get("Key") != key:
                continue
            versions.append({"version_id": v.get("VersionId"),
                             "last_modified": str(v.get("LastModified")),
                             "size": v.get("Size"), "etag": (v.get("ETag") or "").strip('"'),
                             "is_latest": v.get("IsLatest", False)})
        if not resp.get("IsTruncated"):
            break
        kmark = resp.get("NextKeyMarker")
        vmark = resp.get("NextVersionIdMarker")
        if not kmark and not vmark:
            break
        if max_versions is not None and len(versions) >= max_versions:
            truncated = True
            break
    versions.sort(key=lambda x: x["last_modified"])
    if truncated:
        note = ("!! TRUNCATED at %d versions (cap) -- INCOMPLETE; this is a LOWER BOUND."
                % len(versions))
    elif versions:
        note = "full retained version history (paginated to exhaustion, %d page(s))" % pages
    else:
        note = ("NO versions returned -- either the key does not exist OR the bucket is not "
                "versioned. EMPTY here is NOT 'the value never changed'")
    return {"substrate": "s3-object-versions", "bucket": bucket, "key": key,
            "completeness": note, "n_versions": len(versions), "pages": pages,
            "truncated": truncated, "vintages": versions}


def _render(d: dict) -> str:
    L = ["comp-icedrill -- vintage drill",
         "  SUBSTRATE: %s" % d.get("substrate"),
         "  COMPLETENESS: %s" % d.get("completeness")]
    if d.get("truncated"):
        L.insert(1, "  " + "!" * 70)
        L.insert(2, "  !! TRUNCATED LISTING -- THE NUMBERS BELOW ARE A LOWER BOUND, NOT AN ANSWER.")
        L.insert(3, "  " + "!" * 70)
    if d.get("pages"):
        L.append("  SCAN: %d key(s)/version(s) over %d page(s), paginated%s"
                 % (d.get("n_keys_scanned", d.get("n_versions", 0)), d["pages"],
                    " TO EXHAUSTION" if not d.get("truncated") else " UNTIL THE CAP BOUND"))
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
        """A PAGINATING stub. The ORIGINAL returned everything in ONE page -- it was CAP-BLIND BY
        CONSTRUCTION and could NEVER have caught the 2,000-key silent truncation no matter how many
        cases I added to it. A FIXTURE THAT CANNOT REACH THE CAP CANNOT TEST THE CAP. (CVO~Z, F1.)"""
        def __init__(self, contents=None, versions=None, page_size=1000):
            self._c = contents or []
            self._v = versions or []
            self.ps = page_size
            self.pages_served = 0
        def list_objects_v2(self, **kw):
            items = [o for o in self._c if o["Key"].startswith(kw.get("Prefix", ""))]
            start = int(kw.get("ContinuationToken") or 0)
            self.pages_served += 1
            out = {"Contents": items[start:start + self.ps]}
            if start + self.ps < len(items):
                out["NextContinuationToken"] = str(start + self.ps)
            return out
        def list_object_versions(self, **kw):
            items = [v for v in self._v if v["Key"].startswith(kw.get("Prefix", ""))]
            start = int(kw.get("KeyMarker") or 0)
            self.pages_served += 1
            nxt = start + self.ps
            out = {"Versions": items[start:nxt], "IsTruncated": nxt < len(items)}
            if nxt < len(items):
                out["NextKeyMarker"] = str(nxt)
            return out

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

    # ---- THE SCALE CLASS (CVO~Z F1). The original fixtures were single-page: CAP-BLIND BY
    # CONSTRUCTION. These force pagination well past any cap this tool ever shipped.
    big = [{"Key": "silver/x/2026-07-%02d/p-%d.parquet" % ((i % 28) + 1, i),
            "LastModified": _dt.datetime(2026, 7, (i % 28) + 1), "Size": 1, "ETag": "e"}
           for i in range(2500)]
    stub = StubS3(big, page_size=2)
    d_full = dated_partitions(stub, "buck", "silver/x/")
    ck("scale.paginates_to_exhaustion",
       d_full["n_keys_scanned"] == 2500 and not d_full["truncated"] and stub.pages_served > 1,
       f"{d_full['n_keys_scanned']} keys over {d_full['pages']} pages")
    ck("scale.completeness_states_exhaustion", "paginated to exhaustion" in d_full["completeness"])

    d_cap = dated_partitions(StubS3(big, page_size=2), "buck", "silver/x/", max_keys=10)
    ck("scale.bound_cap_DISCLOSED_not_silent",
       d_cap["truncated"] and "TRUNCATED" in d_cap["completeness"]
       and "LOWER BOUND" in d_cap["completeness"],
       f"scanned {d_cap['n_keys_scanned']} and SAID so")

    # THE SELF-REFUTATION INVARIANT CVO~Z USED TO EXPOSE THE BUG: a CHILD scope can never exceed
    # its PARENT. child(2000) > parent(1394) needed no external instrument to prove me wrong.
    parent = dated_partitions(StubS3(big, page_size=500), "buck", "silver/")
    child = dated_partitions(StubS3(big, page_size=500), "buck", "silver/x/")
    ck("scale.parent_ge_child_invariant",
       parent["n_keys_scanned"] >= child["n_keys_scanned"],
       f"parent {parent['n_keys_scanned']} >= child {child['n_keys_scanned']}")

    manyv = [{"Key": "gold/s.json", "VersionId": "v%d" % i,
              "LastModified": _dt.datetime(2026, 7, 1) + _dt.timedelta(seconds=i),
              "Size": 1, "ETag": '"e"', "IsLatest": i == 499} for i in range(500)]
    ov_full = object_versions(StubS3(versions=manyv, page_size=3), "buck", "gold/s.json")
    ck("scale.versions_paginate_to_exhaustion",
       ov_full["n_versions"] == 500 and not ov_full["truncated"],
       f"{ov_full['n_versions']} versions over {ov_full['pages']} pages")

    ok = all(results)
    print("\n" + ("OK: parity + THE SCALE CLASS (exhaustion / disclosed caps / parent>=child); "
                  "empty is a finding" if ok else "ERROR: comp-icedrill self-test FAILED"))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(prog="comp-icedrill",
                                 description="drill an artifact's version/partition vintages across existing substrates (read-only)")
    ap.add_argument("target", nargs="?", help="s3://bucket/prefix or s3://bucket/key.json, or 'ddb'/'graph'")
    ap.add_argument("extra", nargs="?", help="ddb: table name | graph: node")
    ap.add_argument("--pk", default=None, help="ddb: partition-key prefix")
    ap.add_argument("--max-keys", type=int, default=None,
                    help="OPT-IN cap. The DEFAULT IS EXHAUSTION. A cap that BINDS is disclosed "
                         "loudly and exits 2 -- never a silent horizon presented as a full answer.")
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
        d = object_versions(client, bucket, key, max_versions=args.max_keys)
    else:
        d = dated_partitions(client, bucket, key, max_keys=args.max_keys)
    if args.json:
        print(json.dumps(d, indent=1, default=str))
    else:
        print(_render(d))
    # A BOUND CAP IS A FINDING (exit 2): an INCOMPLETE listing must never exit 0 as if it were
    # complete. That is precisely how the silent 2,000-key horizon passed as a full answer.
    if d.get("truncated"):
        return 2
    # empty vintage set is a FINDING (exit 3), never a silent clean.
    return 0 if d.get("vintages") else 3


if __name__ == "__main__":
    sys.exit(main())
