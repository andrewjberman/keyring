#!/usr/bin/env python3
"""
federated_vintage -- the ARTIFACT vintage behind a `comp-heat federated` answer (NFRA_OUTSET OS-s-4).

THE DISTINCTION THIS MODULE EXISTS FOR, and it is the whole of it: a federated answer's vintage is
the BUILD TIME OF THE ARTIFACTS IT JOINED, never the clock at which the query ran. Those two
numbers are always both available and they are almost never the same -- measured on this estate
2026-09-05: the query clock was `now`, while one joined artifact had last been written 50.9 days
earlier. An answer that stamps itself with the query clock is not merely imprecise, it asserts a
freshness the data does not have.

WHAT IT ANSWERS, per fully-qualified table named in the SQL that is about to run (or that WOULD
have run, on a refuse-before-dispatch path -- the vintage of an artifact does not depend on whether
this process queries it):

    build_time   the artifact's own last write, from the OBJECT plane
    claim        `measured` or `absent` -- a value that carries its claim (CLAUDE.md s.4)
    reason       on `absent`: WHY, specifically, in the tool's own voice

WARN: THE CATALOG'S OWN METADATA IS NOT THE ARTIFACT'S BUILD TIME, AND ON THIS ESTATE IT DISAGREES BY
   SEVENTEEN DAYS. `glue get-table` on `code_heat.globgrph.code_heat` reports UpdateTime
   2026-06-29T20:34:47Z; the parquet under its own StorageDescriptor.Location was last written
   2026-07-16T03:40:46Z. Glue's UpdateTime is when the CATALOG ROW changed, not when the DATA did.
   This module therefore uses Glue ONLY to resolve a LOCATION and never as a time source -- a
   catalog read that returned a plausible, well-formed, wrong timestamp is exactly the class of
   silent-blind-read this project has already measured twice (NFRA_OUTSET OS-s-8: a consumer read
   `class` where the producer emits `band`, and a join keyed on a basename that matched 0 of 1774;
   neither raised).

WARN: A MAX OVER A TRUNCATED LISTING IS NOT A MAXIMUM. S3 lists lexicographically, not by time, so the
   newest object can be on any page. When the listing does not COMPLETE inside the caller's ceiling
   this module returns `absent` with that reason, and never the max-so-far -- which would be a
   confident wrong answer indistinguishable in shape from a right one.

READ-ONLY: `glue:GetTable`, `s3:ListBucket`. Nothing is written, nothing is deleted, no query is
dispatched from here.

Author: 0.9.0_WK_NFRA_OUTSET~1 (NFRA_OUTSET OS-s-4). 2026-09-05.
"""

from __future__ import annotations

import datetime as _dt
import re
import time

# Fully-qualified `catalog.schema.table` as it appears after FROM or JOIN. Derived FROM THE SQL that
# is about to run rather than from a fixed list, so `--sql` gets its own correct catalog set instead
# of the default query's.
_FQ_RE = re.compile(r"\b(?:FROM|JOIN)\s+([A-Za-z_]\w*)\.([A-Za-z_]\w*)\.([A-Za-z_]\w*)",
                    re.IGNORECASE)

# An Iceberg table directory under a Nessie warehouse root: `<table>_<uuid4>/`.
_UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

# THE DECLARED REGISTRY. An UNREGISTERED catalog is answered `absent` with that reason -- it is
# never guessed at, because a guessed location that happens to list cleanly is the same silent
# wrong answer as a guessed field name.
#   `code_heat`: Glue-over-parquet. Location resolved LIVE from glue:GetTable
#                (StorageDescriptor.Location), never hardcoded.
#   `iceberg`  : Nessie-backed. NOT in the Glue Data Catalog -- measured 2026-09-05,
#                `glue get-tables --database-name globgrph` returns exactly
#                ['code_heat', 'obs_findings', 'tool_activity'] and `get-databases` returns
#                ['cloudtrail_forensics', 'default', 'globgrph', 'opal_mcp'] with no graph table in
#                any of them. Its data lives under a warehouse root by directory convention.
# Provenance of the federation surface itself: .tools/_trino_fed.py:20-23 (the two catalogs and the
# join key). Provenance of the warehouse root: the live glue:GetTable read above, whose Location is
# `s3://opal-313476888478-globgrph/warehouse/code_heat/`.
CATALOG_REGISTRY = {
    "code_heat": {
        "kind": "glue",
        "glue_database": "globgrph",
        "note": "Glue-over-parquet; the location is read live from the Glue table, never assumed",
    },
    "iceberg": {
        "kind": "nessie-iceberg",
        "bucket": "opal-313476888478-globgrph",
        "warehouse_prefix": "warehouse/globgrph/",
        "note": "Nessie-backed Iceberg; the Nessie pointer is IN-VPC only (same reachability as "
                "the Trino coordinator), so the table directory is located by the "
                "`<table>_<uuid>/` convention and the object plane is the only time source "
                "reachable from here",
    },
}

# Per-table ceiling for the object-plane probe, in seconds. NOT cosmetic: this probe runs against a
# SHARED live plane, and one of the two registered tables carries 134,616 metadata objects (measured
# 2026-09-05: a complete listing took 25.5 s, and the full table 183,447 objects in 36.6 s). A
# vintage disclosure that costs half a minute per call would be paid by every caller forever, so the
# probe is bounded and says so when it stops.
DEFAULT_TABLE_CEILING_S = 3.0
DEFAULT_OBJECT_CAP = 20000

CLAIM_MEASURED = "measured"
CLAIM_ABSENT = "absent"


def _now_utc() -> _dt.datetime:
    """THE QUERY CLOCK. Named, exported and used for exactly one thing -- computing an AGE against a
    build time -- so that the one place it could be mistaken for a vintage is the one place a reader
    looks. It is never returned as a build_time."""
    return _dt.datetime.now(_dt.timezone.utc)


def _iso(ts) -> str:
    if ts is None:
        return "UNREAD"
    return ts.astimezone(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def tables_in_sql(sqls) -> list:
    """Ordered, de-duplicated [(catalog, schema, table)] named by these SQL statements.

    DERIVED, NOT DECLARED: a `--sql` caller joins whatever it joins, and a vintage block that
    recited the DEFAULT query's catalogs beside a custom query's answer would be a well-formed lie.
    """
    seen, out = set(), []
    for sql in sqls or []:
        for m in _FQ_RE.finditer(sql or ""):
            key = (m.group(1).lower(), m.group(2).lower(), m.group(3).lower())
            if key not in seen:
                seen.add(key)
                out.append(key)
    return out


class AwsObjectPlane:
    """The live read surface, isolated behind one small object so the battery can substitute a fake
    one and exercise every branch WITHOUT dispatching to AWS. boto3 is imported lazily: reading this
    module's constants must not require it (the same contract _trino_fed.py holds)."""

    def __init__(self, region: str = "us-east-1"):
        self.region = region
        self._glue = None
        self._s3 = None

    def _c(self, name):
        import boto3
        return boto3.client(name, region_name=self.region)

    def glue_table_location(self, database: str, table: str):
        """(location_uri, error_reason). Glue is a LOCATION source here and never a time source."""
        try:
            if self._glue is None:
                self._glue = self._c("glue")
            t = self._glue.get_table(DatabaseName=database, Name=table)["Table"]
        except Exception as e:                                              # noqa: BLE001
            return None, f"glue:GetTable {database}.{table} failed: {type(e).__name__}"
        loc = (t.get("StorageDescriptor") or {}).get("Location")
        if not loc:
            return None, f"glue table {database}.{table} declares no StorageDescriptor.Location"
        return loc, None

    def list_common_prefixes(self, bucket: str, prefix: str):
        """(list_of_child_prefixes, error_reason) -- ONE delimited call, not a walk."""
        try:
            if self._s3 is None:
                self._s3 = self._c("s3")
            r = self._s3.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter="/")
        except Exception as e:                                              # noqa: BLE001
            return None, f"s3:ListBucket s3://{bucket}/{prefix} failed: {type(e).__name__}"
        return [c["Prefix"] for c in r.get("CommonPrefixes", [])], None

    def iter_object_times(self, bucket: str, prefix: str):
        """Yield (key, LastModified) for every object under the prefix, page by page. The CALLER
        bounds it -- this generator never decides to stop early, so the stopping rule lives in one
        place and is reported by the thing that applied it."""
        if self._s3 is None:
            self._s3 = self._c("s3")
        for page in self._s3.get_paginator("list_objects_v2").paginate(Bucket=bucket,
                                                                       Prefix=prefix):
            for o in page.get("Contents", []):
                yield o["Key"], o["LastModified"]


def _split_s3(uri: str):
    rest = uri[len("s3://"):] if uri.startswith("s3://") else uri
    bucket, _, key = rest.partition("/")
    return bucket, key


def resolve_location(catalog: str, schema: str, table: str, plane):
    """(bucket, prefix, how, reason). `how` names the resolution PATH so a reader can tell a live
    Glue read from a directory-naming convention -- they do not deserve the same trust and the
    output should not present them as if they did."""
    reg = CATALOG_REGISTRY.get(catalog)
    if reg is None:
        return None, None, None, (f"catalog {catalog!r} is not in this tool's vintage registry "
                                  f"(registered: {', '.join(sorted(CATALOG_REGISTRY))}); no "
                                  "location is guessed")
    if reg["kind"] == "glue":
        loc, err = plane.glue_table_location(reg["glue_database"], table)
        if err:
            return None, None, None, err
        b, p = _split_s3(loc)
        return b, p, f"glue:GetTable {reg['glue_database']}.{table} -> {loc}", None
    if reg["kind"] == "nessie-iceberg":
        bucket, root = reg["bucket"], reg["warehouse_prefix"]
        kids, err = plane.list_common_prefixes(bucket, root)
        if err:
            return None, None, None, err
        pat = re.compile(r"^" + re.escape(root + table + "_") + _UUID + r"/$")
        hits = [k for k in (kids or []) if pat.match(k)]
        if len(hits) != 1:
            return None, None, None, (
                f"the `<table>_<uuid>/` convention matched {len(hits)} directory(ies) for "
                f"{table!r} under s3://{bucket}/{root} (denominator: {len(kids or [])} child "
                "prefix(es) scanned); exactly 1 is required, so no location is claimed")
        return bucket, hits[0], (f"s3 directory convention <table>_<uuid>/ under "
                                 f"s3://{bucket}/{root} -> 1 of {len(kids or [])} child "
                                 f"prefix(es)"), None
    return None, None, None, f"catalog {catalog!r} has an unhandled registry kind {reg['kind']!r}"


def _probe_prefix(plane, bucket, prefix, deadline, object_cap):
    """(max_last_modified, scanned, truncated, reason). Returns max_last_modified ONLY when the
    listing COMPLETED: a max over a lexicographic prefix of the keyspace is not a maximum."""
    scanned, newest = 0, None
    try:
        for _key, lm in plane.iter_object_times(bucket, prefix):
            scanned += 1
            if newest is None or lm > newest:
                newest = lm
            if scanned >= object_cap:
                return None, scanned, True, (
                    f"listing stopped at the {object_cap}-object cap under "
                    f"s3://{bucket}/{prefix}; S3 lists lexicographically, not by time, so the "
                    "newest object may be on an unread page and no max is claimed")
            if time.monotonic() > deadline:
                return None, scanned, True, (
                    f"listing did not complete within this table's probe ceiling "
                    f"({scanned} object(s) read under s3://{bucket}/{prefix}); S3 lists "
                    "lexicographically, not by time, so no max is claimed from a partial read")
    except Exception as e:                                                  # noqa: BLE001
        return None, scanned, True, (f"s3:ListBucket s3://{bucket}/{prefix} failed after "
                                     f"{scanned} object(s): {type(e).__name__}")
    if scanned == 0:
        return None, 0, False, f"0 objects under s3://{bucket}/{prefix} -- nothing to date"
    return newest, scanned, False, None


def _artifact_build_time(plane, bucket, prefix, deadline, object_cap):
    """THE ARTIFACT'S BUILD TIME. The single function that produces the value the whole cell is
    about, kept separate from every other concern so that swapping it for the query clock is a
    one-line mutation the battery can perform and detect (O4-AC2's RED mutant)."""
    return _probe_prefix(plane, bucket, prefix, deadline, object_cap)


def vintage_rows(sqls, plane=None, budget_remaining=None,
                 table_ceiling_s: float = DEFAULT_TABLE_CEILING_S,
                 object_cap: int = DEFAULT_OBJECT_CAP) -> list:
    """One row per fully-qualified table named by `sqls`, each carrying its own claim.

    `budget_remaining` is the caller's Rule T remaining seconds (None = unbounded). Every table gets
    at most `table_ceiling_s`, and never more than what the caller has left -- 'every timeout=
    derives from remaining()'.
    """
    plane = plane if plane is not None else AwsObjectPlane()
    rows = []
    for catalog, schema, table in tables_in_sql(sqls):
        row = {"catalog": catalog, "schema": schema, "table": table,
               "fq": f"{catalog}.{schema}.{table}", "build_time": None,
               "claim": CLAIM_ABSENT, "reason": None, "how": None,
               "scanned": 0, "location": None}
        if budget_remaining is not None and budget_remaining <= 0:
            row["reason"] = ("the caller's budget was already spent before this table's vintage "
                             "could be probed; no build time is claimed")
            rows.append(row)
            continue
        ceiling = table_ceiling_s
        if budget_remaining is not None:
            ceiling = min(ceiling, budget_remaining)
        started = time.monotonic()
        bucket, prefix, how, reason = resolve_location(catalog, schema, table, plane)
        if reason:
            row["reason"] = reason
            rows.append(row)
            if budget_remaining is not None:
                budget_remaining -= (time.monotonic() - started)
            continue
        row["how"], row["location"] = how, f"s3://{bucket}/{prefix}"
        newest, scanned, truncated, why = _artifact_build_time(
            plane, bucket, prefix, started + ceiling, object_cap)
        row["scanned"] = scanned
        if newest is None:
            row["reason"] = why
        else:
            row["build_time"], row["claim"] = newest, CLAIM_MEASURED
        if budget_remaining is not None:
            budget_remaining -= (time.monotonic() - started)
        rows.append(row)
    return rows


def render_vintage(rows, now=None) -> list:
    """The VINTAGE block, one line per table plus a header carrying its own denominator."""
    now = now or _now_utc()
    measured = [r for r in rows if r["claim"] == CLAIM_MEASURED]
    cats = sorted({r["catalog"] for r in rows})
    out = [("VINTAGE: %d catalog(s) joined (%s), %d table(s), %d measured / %d UNREAD -- the "
            "ARTIFACT's build time, never the query's clock"
            % (len(cats), ", ".join(cats) or "none", len(rows), len(measured),
               len(rows) - len(measured)))]
    if not rows:
        out.append("  (no fully-qualified catalog.schema.table appears in the SQL about to run -- "
                   "nothing to date, and nothing is assumed)")
        return out
    width = max(len(r["fq"]) for r in rows)
    for r in rows:
        if r["claim"] == CLAIM_MEASURED:
            age = (now - r["build_time"].astimezone(_dt.timezone.utc)).total_seconds() / 86400.0
            out.append("  %s  build_time=%s  claim=measured  age=%.1fd"
                       % (r["fq"].ljust(width), _iso(r["build_time"]), age))
            out.append("      instrument: max(s3 LastModified) over %d of %d object(s) under %s; "
                       "located by %s" % (r["scanned"], r["scanned"], r["location"], r["how"]))
        else:
            out.append("  %s  build_time=UNREAD  claim=absent" % r["fq"].ljust(width))
            out.append("      reason: %s" % (r["reason"] or "no reason recorded"))
    out.append("  the query clock (%s) is NOT a vintage and is printed here only so the two cannot "
               "be confused" % _iso(now))
    return out
