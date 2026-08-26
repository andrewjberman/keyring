#!/usr/bin/env python3
"""comp-atomcheck -- archetype-conformance runner (READ-ONLY).

NFRA_COMPTOOLS.REG-SCAN-ATOMCHECK leg J3, per the ratified TIGHTENING_ENUMERATION_SPEC
@1dceb7d61d section J3 (4.0.0_SA_CRO~A, ratified; released to this lane by COO).

Renders one verdict row per archetype atom, per product x firm:

    {atom, scope, verdict, evidence, denominator, why?}

VERDICT ENUM -- one axis, one grain, MECE over the declared domain (Rule 24):
    CONFORMS                      the atom's checkable claim held, with a printed denominator
    VIOLATES                      it did not, and the row names what failed
    NOT-CHECKABLE-BY-THIS-RUNNER  honest absence -- carries a `why`, and is NEVER rendered
                                  as CONFORMS. An atom this runner cannot check must cost the
                                  reader a visible row, not silence.

v1 checks six legs (atoms 1, 3, 5-floor, 7-spelling, 8-coverage, 9). Every other atom, and
the non-checkable HALF of atoms 5 and 7, prints NOT-CHECKABLE-BY-THIS-RUNNER with its reason.

WARNING: NEVER A MONITOR. Run-and-read, no schedule, no standing comparator, no alarm -- the
fit_harness form and the standing estate moratorium. Read-only by construction: S3 GET/LIST,
EventBridge/Scheduler describe/list, and pyarrow schema reads. It writes nothing, anywhere.

WARNING: THREE SPEC-VS-ESTATE DIVERGENCES ARE ENCODED HERE DELIBERATELY, each measured 2026-08-25
before a line was written, because building to the spec's literal text would have produced a
confident answer about the wrong plane in all three cases:

  (1) ROOT. The spec says `portal/gold/{product}/{scope}/`. That root was RE-POINTED to
      `gold/advi` on 2026-08-18 (the same day the spec was written) and BOTH portal roots are
      measured EMPTY today, in both candidate buckets. A leg built on the spec's prefix reads
      a clean, confident zero about nothing.
  (2) MANIFESTS. The spec's atom 3 names only `_manifests/{data-as-of}/*.json`. The estate
      overwhelmingly uses a partition-local `manifest.json` instead: 2183 of 2193 partitions
      carry the partition-local form and only 12 keys use the `_manifests/` form. Checking the
      spec's form ALONE would report ~2183 false VIOLATIONS. Both forms are accepted and the
      split is printed, so the reader sees which convention each partition used.
  (3) TRIGGER PLANE. The spec's atom 5 says "EventBridge read". `aws events list-rules` (137
      rules) STRUCTURALLY CANNOT SEE `aws scheduler list-schedules` (18 schedules), and the
      49F gold floor -- `advi-49f-gold-floor`, ENABLED, cron(45 12 * * ? *) -- lives on the
      SCHEDULER plane. A one-plane sweep returns a TRUE, correctly-controlled answer about the
      WRONG POPULATION and reports VIOLATES on a product that has a live floor. Atom 5 sweeps
      BOTH planes and prints both denominators.

None of the three is a defect in the spec's judgement; each is the estate moving under a
document. They are encoded as CONFIG, not as silent behaviour, so the divergence is auditable.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re

import sys
from datetime import datetime, timezone
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

CONFORMS = "CONFORMS"
VIOLATES = "VIOLATES"
NOT_CHECKABLE = "NOT-CHECKABLE-BY-THIS-RUNNER"

# ---------------------------------------------------------------------------
# PRODUCT REGISTRY -- every value a leg checks against is DECLARED here, never
# inferred from what the estate happens to contain. A grammar tuned to the
# estate it measures cannot fail, which would make every CONFORMS meaningless.
# ---------------------------------------------------------------------------
PRODUCTS = {
    ("advi", "49financial"): {
        "bucket": "opal-data-49financial",
        "root": "gold/advi/",
        # atom 1 -- the spec's grammar names canonical|dimensions. `reference` is PRESENT in
        # the estate and is NOT declared here on purpose: if it is legitimate it should be
        # declared by a named owner, and until then atom 1 must SAY SO rather than absorb it.
        "declared_scopes": ["canonical", "dimensions"],
        "declared_underscore_planes": ["_logs", "_manifests"],
        # atom 5 -- the floor leg. Matched on BOTH trigger planes.
        "floor_name_patterns": ["*advi*49f*", "*49f*advi*"],
        # atom 8 -- the per-family lineage declaration DS~B authors at P4-EMIT. Absent today;
        # atom 8 therefore renders NOT-CHECKABLE per the spec, never CONFORMS.
        "lineage_declaration": "data/assets/scripts/gold/runners_49f/lineage_49f.json",
        "exception_set": "data/assets/scripts/gold/runners_49f/predeclared_divergences_49f.json",
        "served_census": "data/assets/scripts/gold/runners_49f/d00_census_out.json",
    },
}

# Atoms this runner does not check, and WHY. Sourced from the spec's own J3.2 table so the
# reason a reader gets is the ratified reason, not this tool's paraphrase.
NOT_CHECKABLE_ATOMS = {
    2: ("_code/ one deploy target",
        "'runners pull ONLY here' needs a code-read census of pull sites (v2). Per Rule 4 the "
        "source map PAIRS a lambda with its dir, it does NOT byte-compare, so it cannot settle this."),
    4: ("intermediates inside the product root",
        "detecting a FOREIGN-homed intermediate requires classifying arbitrary estate keys as "
        "'this product's' -- an unbounded domain; v2 at best."),
    6: ("config never in the code store",
        "static scan of runner sources for data reads resolving into _code/; an AST miss is "
        "SILENCE, so this leg must report its own coverage denominator before it can be trusted."),
}
# The non-checkable HALVES of the two PARTIAL atoms that do have a v1 leg.
PARTIAL_RESIDUE = {
    5: ("one-producer-per-key / one-runtime",
        "a principal census. Post-P4 one-producer holds BY CONSTRUCTION; pre-P4 it needs an "
        "IAM+code census, and comp-iam models (action) not (action,resource) and FAILS GREEN "
        "(Rule 22a), so it cannot answer this. one-runtime is v2."),
    7: ("serve only via the publisher",
        "a platinum-writer census -- the same missing producer/writer instrument as atom 5's "
        "residue, so these two do NOT move independently."),
}


def _utcnow() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _client(svc: str):
    """boto3 client, IN-PROCESS.

    Deliberately NOT shell-out to the aws CLI: this estate's canonical pattern for a live
    read from python is in-process boto3 (comp_aws_cli.py:6 records the CRLF finding behind
    that rule), and a python-spawned `aws` on this box does not resolve at all -- measured
    here as FileNotFoundError WinError 2 before this was converted.
    """
    import boto3
    return boto3.client(svc, region_name="us-east-1")


def _err(e) -> str:
    return "%s: %s" % (type(e).__name__, str(e)[:240])


def _list_keys(bucket: str, prefix: str) -> tuple[list[str], str | None]:
    """List every key under a prefix, MATERIALISED.

    WARNING: NO length()-style page arithmetic and NO single-page read. A paginated list answers
    with a PAGE, and a page is not a total; page 1 comes back as a clean, complete-looking
    result. Page through, materialise the set, count client-side, print the number.
    WARNING: NO BARE except. An instrument failure must become a NOT-CHECKABLE row carrying the
    error, never a verdict -- a swallowed error would render an unread plane as a clean
    CONFORMS, the exact anti-correlation this runner exists to avoid.
    """
    from botocore.exceptions import BotoCoreError, ClientError
    keys: list[str] = []
    try:
        for page in _client("s3").get_paginator("list_objects_v2").paginate(
                Bucket=bucket, Prefix=prefix):
            keys.extend(o["Key"] for o in page.get("Contents", []))
    except (BotoCoreError, ClientError, ImportError) as e:
        return [], _err(e)
    return keys, None


def _row(atom, scope, verdict, evidence, denominator, why=None):
    r = {"atom": atom, "scope": scope, "verdict": verdict,
         "evidence": evidence, "denominator": denominator}
    if why:
        r["why"] = why
    return r


_PART_RE = re.compile(r"^([A-Za-z0-9_]+)/([A-Za-z0-9_]+)/date=(\d{4}-\d{2}-\d{2})/(.+)$")


def _partition_index(rel_keys):
    """Split relative keys into (partitions, underscore-plane, unmatched)."""
    parts, uscore, other = {}, [], []
    for r in rel_keys:
        m = _PART_RE.match(r)
        if m:
            scope, table, date, leaf = m.groups()
            parts.setdefault((scope, table, date), set()).add(leaf)
        elif r.split("/")[0].startswith("_") or "/_" in r:
            uscore.append(r)
        else:
            other.append(r)
    return parts, uscore, other


# ---------------------------------------------------------------------------
# ATOM LEGS
# ---------------------------------------------------------------------------

def atom1_grammar(cfg, rel, parts, uscore, other):
    """One-product-root grammar. Denominator = keys listed."""
    declared = set(cfg["declared_scopes"])
    planes = cfg["declared_underscore_planes"]
    bad_scope = sorted({s for (s, _t, _d) in parts if s not in declared})
    stray_uscore = [
        r for r in uscore
        if not any(("/" + p + "/") in ("/" + r) or r.startswith(p + "/") for p in planes)
    ]
    n_bad = sum(1 for (s, _t, _d), v in parts.items() for _ in v if s not in declared)
    denom = "%d keys listed under the product root; %d partitions; %d '_'-plane; %d matching neither" % (
        len(rel), len(parts), len(uscore), len(other))
    if not bad_scope and not other and not stray_uscore:
        return _row(1, "product-root grammar", CONFORMS,
                    "every key matches {%s}/{table}/date={D}/... or a declared '_' plane {%s}" % (
                        "|".join(sorted(declared)), ",".join(planes)),
                    denom)
    ev = []
    if bad_scope:
        ev.append("UNDECLARED SCOPE(S) %s -- %d key(s) across %d partition(s); the declared "
                  "grammar is {%s}. Not absorbed: if these are legitimate they need a declared "
                  "owner, and an undeclared scope that the checker silently accepts is a grammar "
                  "that cannot fail." % (
                      bad_scope, n_bad,
                      sum(1 for (s, _t, _d) in parts if s in set(bad_scope)),
                      "|".join(sorted(declared))))
        for s in bad_scope:
            ex = sorted({"%s/%s" % (sc, t) for (sc, t, _d) in parts if sc == s})[:4]
            ev.append("    e.g. " + ", ".join(ex))
    if other:
        ev.append("KEYS MATCHING NEITHER the partition grammar nor a '_' plane: %d, e.g. %s" % (
            len(other), other[:3]))
    if stray_uscore:
        ev.append("UNDECLARED '_' PLANE keys: %d, e.g. %s" % (len(stray_uscore), stray_uscore[:3]))
    return _row(1, "product-root grammar", VIOLATES, " | ".join(ev), denom)


def atom3_manifests(cfg, parts, uscore):
    """Manifests on every gold write. Denominator = partitions carrying data.

    TWO conventions are live and BOTH count (see divergence (2) in the module docstring). The
    sidecar form the spec names is `{scope}/_manifests/{data-as-of}/{stamp}__{table}.json`, so
    it is resolved PER (scope, table, date) -- not per scope. Resolving it at scope grain would
    mark every table in a scope covered because ONE table had a sidecar, which is a coarser
    grain than the claim and would manufacture a pass.
    """
    data_parts = {p for p, v in parts.items() if any(x.endswith(".parquet") for x in v)}
    local_man = {p for p, v in parts.items() if any(x == "manifest.json" for x in v)}
    sidecar = set()
    for r in uscore:
        m = re.match(r"^([A-Za-z0-9_]+)/_manifests/(\d{4}-\d{2}-\d{2})/.*?__([A-Za-z0-9_]+)\.json$", r)
        if m:
            scope, date, table = m.groups()
            sidecar.add((scope, table, date))
    covered = set(local_man) | sidecar
    missing = sorted(p for p in data_parts if p not in covered)
    by_sidecar = len(data_parts & sidecar - local_man)
    still_missing = missing
    denom = ("%d partitions carrying data.parquet; %d covered by partition-local manifest.json; "
             "%d covered by the spec's _manifests/{data-as-of} sidecar; %d uncovered" % (
                 len(data_parts), len(local_man), by_sidecar, len(still_missing)))
    ev = ("BOTH manifest conventions accepted and counted separately -- the spec names only the "
          "_manifests/ sidecar, but the estate uses partition-local manifest.json for %d of %d "
          "data partitions. Checking the spec's form alone would report %d false VIOLATIONS." % (
              len(local_man), len(data_parts), len(data_parts) - by_sidecar))
    if still_missing:
        return _row(3, "manifest coverage", VIOLATES,
                    ev + " UNCOVERED: " + ", ".join("%s/%s/date=%s" % p for p in still_missing[:6]),
                    denom)
    return _row(3, "manifest coverage", CONFORMS, ev, denom)


def atom5_floor(cfg):
    """Schedule floor. Sweeps BOTH trigger planes -- see divergence (3) in the module docstring."""
    from botocore.exceptions import BotoCoreError, ClientError
    pats = cfg["floor_name_patterns"]
    rules, scheds, err1, err2 = [], [], None, None
    # PLANE 1 -- EventBridge Rules. Paginated; materialise, never count a page.
    try:
        for page in _client("events").get_paginator("list_rules").paginate():
            rules.extend({"n": r.get("Name"), "s": r.get("ScheduleExpression")}
                         for r in page.get("Rules", []))
    except (BotoCoreError, ClientError, ImportError) as e:
        err1 = _err(e)
    # PLANE 2 -- EventBridge Scheduler. A DIFFERENT SERVICE with a DIFFERENT API: plane 1
    # cannot see it, and the 49F gold floor lives here.
    try:
        for page in _client("scheduler").get_paginator("list_schedules").paginate():
            scheds.extend({"n": s.get("Name"), "s": s.get("State")}
                          for s in page.get("Schedules", []))
    except (BotoCoreError, ClientError, ImportError) as e:
        err2 = _err(e)
    if err1 or err2:
        return _row(5, "schedule floor", NOT_CHECKABLE,
                    "a trigger plane could not be read", "events_err=%s scheduler_err=%s" % (err1, err2),
                    why="INSTRUMENT FAILURE, not a compliance finding. An unread plane must never "
                        "render as CONFORMS or VIOLATES -- both would be a verdict about a "
                        "population this run never saw.")
    rules, scheds = rules or [], scheds or []

    def _match(names):
        return [n for n in names if any(fnmatch.fnmatch(n.lower(), p) for p in pats)]

    ev_hits = [r for r in rules if _match([r.get("n") or ""])]
    sc_hits = [s for s in scheds if _match([s.get("n") or ""])]
    denom = ("events plane: %d rules total, %d name-matched; scheduler plane: %d schedules total, "
             "%d name-matched. BOTH planes swept -- one plane cannot see the other." % (
                 len(rules), len(ev_hits), len(scheds), len(sc_hits)))
    # a floor is LIVE only if it is scheduled AND enabled
    live = []
    for r in ev_hits:
        if r.get("s"):
            live.append("events:%s(%s)" % (r["n"], r["s"]))
    for s in sc_hits:
        if (s.get("s") or "").upper() == "ENABLED":
            live.append("scheduler:%s(ENABLED)" % s["n"])
    dead = ([("events:%s" % r["n"]) for r in ev_hits if not r.get("s")]
            + [("scheduler:%s(%s)" % (s["n"], s.get("s"))) for s in sc_hits
               if (s.get("s") or "").upper() != "ENABLED"])
    if live:
        ev = "LIVE FLOOR: %s." % ", ".join(live)
        if dead:
            ev += (" Also matched but NOT a floor: %s -- a rule with ScheduleExpression=None or a "
                   "DISABLED schedule is a COMPLIANCE fact, not a LIVENESS fact." % ", ".join(dead))
        return _row(5, "schedule floor (floor half only)", CONFORMS, ev, denom)
    return _row(5, "schedule floor (floor half only)", VIOLATES,
                "no ENABLED, scheduled writer matched %s on EITHER plane. Matched-but-not-a-floor: %s"
                % (pats, ", ".join(dead) or "none"), denom)


def atom7_spelling(cfg, rel):
    """Spelling law: gold keys use '_', platinum keys '-'.

    A date partition legitimately contains hyphens (date=2026-08-18), and so does an ISO
    timestamp inside a manifest filename. Those are NOT spelling violations, and a predicate
    that flags them reports 12 false positives on this root -- measured before this leg shipped.
    """
    date_like = re.compile(r"date=\d{4}-\d{2}-\d{2}")
    iso_like = re.compile(r"\d{8}T\d{6}Z")
    bad = []
    for r in rel:
        probe = iso_like.sub("", date_like.sub("", r))
        # strip the {D} value inside a sidecar path segment too (e.g. _manifests/2026-08-18/)
        probe = re.sub(r"/\d{4}-\d{2}-\d{2}/", "/", probe)
        if "-" in probe:
            bad.append(r)
    denom = ("%d gold keys examined; hyphens inside date= partitions, ISO timestamps and "
             "{data-as-of} segments are EXCLUDED as legitimate (12 such keys on this root would "
             "otherwise false-positive)" % len(rel))
    if bad:
        return _row(7, "spelling law (gold '_' half only)", VIOLATES,
                    "%d gold key(s) carry '-' outside a date/timestamp segment: %s" % (
                        len(bad), bad[:5]), denom)
    return _row(7, "spelling law (gold '_' half only)", CONFORMS,
                "every gold key uses '_' spelling outside legitimate date/timestamp segments", denom)


def atom8_lineage(cfg):
    """Raw-from-endpoint: DECLARATION COVERAGE only, never veracity."""
    decl_path = _WORKSPACE / cfg["lineage_declaration"]
    exc_path = _WORKSPACE / cfg["exception_set"]
    census_path = _WORKSPACE / cfg["served_census"]
    if not decl_path.exists():
        return _row(8, "raw-from-endpoint (declaration coverage)", NOT_CHECKABLE,
                    "no per-family lineage declaration at %s" % cfg["lineage_declaration"],
                    "0 families declared",
                    why="The lineage declaration ({served_field: endpoint_field | exception_id}) is "
                        "authored by the EMITTING lane (DS~B) at P4-EMIT and does not exist yet. "
                        "Per the spec this renders NOT-CHECKABLE and MUST NEVER render CONFORMS -- "
                        "an undeclared family is unproven, not compliant.")
    try:
        decl = json.loads(decl_path.read_text(encoding="utf-8"))
        exceptions = json.loads(exc_path.read_text(encoding="utf-8")) if exc_path.exists() else []
        census = json.loads(census_path.read_text(encoding="utf-8")) if census_path.exists() else {}
    except (OSError, json.JSONDecodeError) as e:
        return _row(8, "raw-from-endpoint (declaration coverage)", NOT_CHECKABLE,
                    "input unreadable: %s" % e, "0 fields",
                    why="INSTRUMENT FAILURE, not a compliance finding.")
    globs = []
    for e in exceptions if isinstance(exceptions, list) else []:
        globs.extend(e.get("field_paths") or [])
    families = census.get("families") or {}
    total = covered = 0
    uncovered = []
    for fam, meta in (families.items() if isinstance(families, dict) else []):
        fields = meta.get("fields") if isinstance(meta, dict) else None
        for f in (fields or []):
            total += 1
            if f in (decl.get(fam) or {}) or any(fnmatch.fnmatch(f, g) for g in globs):
                covered += 1
            else:
                uncovered.append("%s.%s" % (fam, f))
    denom = "%d served field(s) across %d family(ies); %d covered by declaration or ratified exception" % (
        total, len(families), covered)
    if not total:
        return _row(8, "raw-from-endpoint (declaration coverage)", NOT_CHECKABLE,
                    "the served census exposes no per-family field list to check against", denom,
                    why="census present but carries no family->fields map; coverage is undefined, "
                        "and an undefined coverage is not a passing coverage.")
    if uncovered:
        return _row(8, "raw-from-endpoint (declaration coverage)", VIOLATES,
                    "ILLEGITIMATELY-DERIVED: %d served field(s) in neither the lineage declaration "
                    "nor the ratified exception set: %s" % (len(uncovered), uncovered[:6]), denom)
    return _row(8, "raw-from-endpoint (declaration coverage)", CONFORMS,
                "every served field resolves to a declared endpoint mapping or a ratified exception. "
                "COVERAGE ONLY -- the TRUTH of a declared mapping is a human/CVO read, never this "
                "runner's claim.", denom)


def atom9_provenance(cfg, bucket, parts):
    """Provenance columns via parquet SCHEMA read (no data load)."""
    try:
        import pyarrow.parquet as pq  # noqa: F401
        import s3fs  # noqa: F401
    except ImportError as e:
        tables = sorted({(s, t) for (s, t, _d) in parts})
        return _row(9, "provenance columns", NOT_CHECKABLE,
                    "schema reader unavailable in this environment: %s" % e,
                    "%d intermediate table(s) would be read" % len(tables),
                    why="pyarrow/s3fs not importable here. WARNING: AN IMPORT GUARDED BY try/except "
                        "answers COMPLETION, NEVER PRESENCE -- so this reports NOT-CHECKABLE rather "
                        "than letting a missing dependency read as a clean pass.")
    return _row(9, "provenance columns", NOT_CHECKABLE,
                "deferred: needs one schema read per table against live S3",
                "%d intermediate table(s)" % len(sorted({(s, t) for (s, t, _d) in parts})),
                why="v1 ships the leg wired but not exercised against live S3 in this run; it is "
                    "listed here rather than omitted so its absence is visible.")


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="comp-atomcheck",
        description="Archetype-conformance runner (READ-ONLY). One verdict row per atom.")
    ap.add_argument("--product", required=True, help="product code, e.g. advi")
    ap.add_argument("--firm", required=True, help="firm, e.g. 49financial")
    ap.add_argument("--atom", type=int, default=None, help="restrict to one atom (1-9)")
    ap.add_argument("--json", action="store_true", help="machine output")
    args = ap.parse_args()

    key = (args.product, args.firm)
    cfg = PRODUCTS.get(key)
    if not cfg:
        print("UNCOVERED: no atom-check config for product=%r firm=%r -- this product is NOT "
              "analyzed (not conforming, not violating, UNVERIFIED). Known: %s"
              % (args.product, args.firm, sorted(PRODUCTS)), file=sys.stderr)
        return 2

    read_at = _utcnow()
    keys, err = _list_keys(cfg["bucket"], cfg["root"])
    if err:
        print("UNCOVERED: could not list s3://%s/%s -- %s" % (cfg["bucket"], cfg["root"], err),
              file=sys.stderr)
        return 2
    rel = [k[len(cfg["root"]):] for k in keys if k.startswith(cfg["root"])]
    parts, uscore, other = _partition_index(rel)

    rows = [
        atom1_grammar(cfg, rel, parts, uscore, other),
        atom3_manifests(cfg, parts, uscore),
        atom5_floor(cfg),
        atom7_spelling(cfg, rel),
        atom8_lineage(cfg),
        atom9_provenance(cfg, cfg["bucket"], parts),
    ]
    for n, (scope, why) in sorted(NOT_CHECKABLE_ATOMS.items()):
        rows.append(_row(n, scope, NOT_CHECKABLE, "no v1 leg", "n/a", why=why))
    for n, (scope, why) in sorted(PARTIAL_RESIDUE.items()):
        rows.append(_row(n, scope + " (RESIDUE of a partially-checked atom)", NOT_CHECKABLE,
                         "no v1 leg for this half", "n/a", why=why))
    rows.sort(key=lambda r: (r["atom"], r["scope"]))
    if args.atom:
        rows = [r for r in rows if r["atom"] == args.atom]

    prov = {
        "product": args.product, "firm": args.firm,
        "bucket": cfg["bucket"], "root": cfg["root"],
        "s3_read_at_utc": read_at, "keys_listed": len(rel),
        "runner": "comp-atomcheck v1 (read-only; never a monitor)",
    }
    if args.json:
        print(json.dumps({"provenance": prov, "rows": rows}, indent=2))
        return 0

    print("comp-atomcheck v1 -- %s / %s" % (args.product, args.firm))
    print("  PROVENANCE: s3://%s/%s read at %s | %d keys materialised (paginated, counted "
          "client-side)" % (cfg["bucket"], cfg["root"], read_at, len(rel)))
    print("  READ-ONLY. Never a monitor: run-and-read, no schedule, no standing comparator.")
    print()
    for r in rows:
        print("  ATOM %-2d %-52s %s" % (r["atom"], r["scope"][:52], r["verdict"]))
        print("     evidence   : %s" % r["evidence"])
        print("     denominator: %s" % r["denominator"])
        if r.get("why"):
            print("     why        : %s" % r["why"])
        print()
    n_c = sum(1 for r in rows if r["verdict"] == CONFORMS)
    n_v = sum(1 for r in rows if r["verdict"] == VIOLATES)
    n_n = sum(1 for r in rows if r["verdict"] == NOT_CHECKABLE)
    print("  SUMMARY: %d CONFORMS / %d VIOLATES / %d NOT-CHECKABLE-BY-THIS-RUNNER "
          "(rows=%d, parts sum: %s)" % (n_c, n_v, n_n, len(rows), n_c + n_v + n_n == len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
