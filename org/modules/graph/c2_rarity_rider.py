#!/usr/bin/env python3
"""c2_rarity_rider -- NFRA_ONTOLOGY.R1-RARITY LEG 2: the RARITY-COORDINATE rider rows.

Emits, per canonical C2 family, the rarity COORDINATES per 4.0.0_SA_CRO base's spec
(C2_RARITY_COORDINATE_RIDER_SPEC_20260820.md, sec.1 fields / sec.3 production rule; Rule-24 record
= spec sec.2, CITED not re-run -- adoption noted). THE RIDER STAGES AXES AND COMPUTES NO VERDICT
(Andrew-direct 2026-08-20: the agents do the inferring; a pre-computed "suspicious" flag would be
the alarm-shaped deliverable the moratorium names).

PRODUCE-TIME HONESTY, tonight's measured state (composer finding 64141):
  - recurrence.basis = FIRST_PASS_HAND_COUNT for ALL twelve families: the composer materializes the
    SERVED_LINEAGE spine (45 instances, measured) but family resolution is structurally unreachable
    through the graph today (zero served-key S3Key nodes -> no producer join -> no trigger
    discriminator), so NO family carries a measured per-family figure. MEASURED_INSTANCE_SET
    activates per family the day the composer resolves it -- the axis exists to make that
    transition visible.
  - ESTATE rows carry the canonical's hand-counted first_pass_recurrence; the rarity_denominator is
    the SUM OF HAND COUNTS, declared as such (a hand-count denominator, never a measured census).
  - FIRM rows are PRODUCED (both populations per family, Andrew's ruling) with recurrence = null +
    absence_semantic NO_FIGURE_EXISTS (S6: a DECLARED absence -- the hand count is estate-wide
    only; a fabricated firm zero would be FALSE, not conservative).
  - The measured spine population (45) rides as `served_lineage_spine` CONTEXT with its scope
    declared -- never presented as a per-family recurrence.
  - nearest_family/distance under the canonical `shape` strings, `policy: NONE_RATIFIED` declared;
    metric_ref names the metric AND version (a distance without metric_ref is not a coordinate).
  - d3_preserving = UNKNOWN_NO_D3_DECLARED everywhere (today's D3 population ~0); the self-test's
    positive control proves a declared-D3 pair reads PRESERVED/NOT_PRESERVED, so UNKNOWN is a
    measured default, not a hardcode.

Author: 0.8.0_AE_CloudComp (NFRA_ONTOLOGY.R1-RARITY, COO GO 64034; design ratified CRO 64086).
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
CANONICAL_YAML = os.path.join(_HERE, "NFRA_ONTOLOGY_C2C3_CANONICAL.yaml")
INSTANCE_SET_DEFAULT = os.path.join(WS, "org", "tier2_senior", "0.8.0_AE_CloudComp", "deliverables",
                                    "NFRA_ONTOLOGY.R1-RARITY", "c2_canonical_instances_20260821.json")
METRIC_REF = "role-token-levenshtein@0.1 (over the canonical `shape` strings; policy: NONE_RATIFIED -- "
METRIC_REF += "the substitution policy defines identity when ratified; this metric only PROPOSES)"
FIRM_TREES = ("bd", "inf", "cot", "mdpf")


def _families() -> dict:
    """Parse the twelve families (name, shape, first_pass_recurrence) text-surgically from the
    canonical -- the canonical is CITED, never rewritten; a parse that finds != 12 REFUSES."""
    fams, name, shape, fpr = {}, None, None, None
    in_block = False
    for line in open(CANONICAL_YAML, encoding="utf-8"):
        if line.startswith("c2_motif_families:"):
            in_block = True
            continue
        if in_block and line and not line.startswith(" ") and not line.startswith("#"):
            break
        if not in_block:
            continue
        m = re.match(r"^  ([a-z][a-z0-9-]*):\s*$", line)
        if m:
            if name and shape is not None and fpr is not None:
                fams[name] = {"shape": shape, "first_pass_recurrence": fpr}
            name, shape, fpr = m.group(1), None, None
            continue
        m = re.match(r"^    shape:\s*'(.*)'\s*$", line)
        if m:
            shape = m.group(1)
        m = re.match(r"^    first_pass_recurrence:\s*(\d+)\s*$", line)
        if m:
            fpr = int(m.group(1))
    if name and shape is not None and fpr is not None:
        fams[name] = {"shape": shape, "first_pass_recurrence": fpr}
    if len(fams) != 12:
        raise RuntimeError("REFUSED: parsed %d families from the canonical, expected 12 -- the parse is wrong "
                           "or the canonical moved; not emitting against an unverified family set" % len(fams))
    return fams


def _tokens(shape: str) -> list:
    """Role-token sequence of a shape string: 'Trigger(cron) -> Producer -> Store(raw/bronze)' ->
    ['Trigger(cron)', 'Producer', 'Store(raw/bronze)'] -- qualifiers kept (they discriminate)."""
    return [t.strip() for t in shape.split("->") if t.strip()]


def _lev(a: list, b: list) -> int:
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (0 if x == y else 1)))
        prev = cur
    return prev[-1]


def d3_preserving(family: str, nearest: str, d3_declarations: dict | None) -> tuple:
    """UNKNOWN_NO_D3_DECLARED unless BOTH families carry declared D3 obligations, in which case
    compare them (spec sec.3 step 4). The rider MUST NOT emit PRESERVED by default."""
    d3 = d3_declarations or {}
    a, b = d3.get(family), d3.get(nearest)
    if a is None or b is None:
        return ("UNKNOWN_NO_D3_DECLARED",
                "D3 obligations declared: %s=%s, %s=%s -- both required to compare"
                % (family, "yes" if a is not None else "no", nearest, "yes" if b is not None else "no"))
    return (("PRESERVED", "declared obligation sets equal") if sorted(a) == sorted(b)
            else ("NOT_PRESERVED", "declared obligation sets differ: %s vs %s" % (sorted(a), sorted(b))))


def _git_head() -> str:
    r = subprocess.run(["git", "-C", WS, "rev-parse", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip()[:12] if r.returncode == 0 else "UNKNOWN"


def build_rows(instance_set_path: str | None = None, d3_declarations: dict | None = None) -> dict:
    fams = _families()
    inst_doc, inst_ref, spine = None, None, {}
    path = instance_set_path or INSTANCE_SET_DEFAULT
    if os.path.isfile(path):
        inst_doc = json.load(open(path, encoding="utf-8"))
        inst_ref = {"path": os.path.relpath(path, WS).replace("\\", "/"),
                    "graph_vintage": inst_doc.get("graph_vintage"),
                    "spine_instances": inst_doc.get("counts", {}).get("spine_instances"),
                    "family_resolved": inst_doc.get("counts", {}).get("family_resolved")}
        spine = inst_doc.get("counts", {})
    hand_total = sum(f["first_pass_recurrence"] for f in fams.values())
    vintage = {"canonical_head": _git_head(), "canonical_file": "org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml",
               "instance_set": inst_ref, "metric_ref": METRIC_REF,
               "emitted_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    rows = []
    for f in sorted(fams):
        toks = _tokens(fams[f]["shape"])
        dists = {g: _lev(toks, _tokens(fams[g]["shape"])) for g in fams if g != f}
        nearest = min(sorted(dists), key=lambda g: dists[g])
        d3v, d3basis = d3_preserving(f, nearest, d3_declarations)
        common = {"family": f, "shape": fams[f]["shape"],
                  "nearest_family": nearest, "distance": dists[nearest], "metric_ref": METRIC_REF,
                  "nearest_note": "PROPOSAL device only (Response II sec.2.4): identity is decided by the "
                                  "substitution policy, never by distance",
                  "d3_preserving": d3v, "d3_basis": d3basis, "policy": "NONE_RATIFIED", "vintage": vintage}
        rows.append({**common, "population_scope": "ESTATE",
                     "recurrence": fams[f]["first_pass_recurrence"],
                     "recurrence_basis": "FIRST_PASS_HAND_COUNT",
                     "rarity_denominator": hand_total,
                     "denominator_basis": "sum of the canonical's hand counts over 12 families -- a hand-count "
                                          "denominator, never a measured census"})
        for t in FIRM_TREES:
            rows.append({**common, "population_scope": "FIRM:%s" % t,
                         "recurrence": None, "recurrence_basis": "FIRST_PASS_HAND_COUNT",
                         "rarity_denominator": None,
                         "absence_semantic": "NO_FIGURE_EXISTS: the hand count is estate-wide only and the "
                                             "measured instance set does not yet resolve families -- a DECLARED "
                                             "absence (S6); a fabricated firm zero would be FALSE, not conservative"})
    return {"producer": "NFRA_ONTOLOGY.R1-RARITY LEG 2 (0.8.0_AE_CloudComp)",
            "spec": "org/tier1_exec/4.0.0_SA_CRO/deliverables/C2_RARITY_COORDINATE_RIDER_SPEC_20260820.md "
                    "(sec.2 Rule-24 record CITED; adoption noted per Rule 24's adoption-is-authoring clause)",
            "no_verdict": "THE RIDER STAGES AXES AND COMPUTES NO VERDICT -- no suspicious/alert/flag field "
                          "exists anywhere in these rows (Andrew-direct: the agents do the inferring)",
            "served_lineage_spine": {"note": "MEASURED context, scope declared -- never a per-family recurrence: "
                                             "the composer materializes the SERVED_LINEAGE spine; family "
                                             "resolution awaits the served-key/producer plane (finding 64141)",
                                     "spine_instances": spine.get("spine_instances"),
                                     "family_resolved": spine.get("family_resolved"),
                                     "family_unresolved": spine.get("family_unresolved")},
            "denominators": {"families": len(fams), "rows": len(rows),
                             "rows_per_family": 1 + len(FIRM_TREES),
                             "estate_hand_count_total": hand_total},
            "rows": rows}


def self_test() -> int:
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    doc = build_rows(instance_set_path="__no_such_file__")
    rows = doc["rows"]
    chk("1 twelve families x (1 ESTATE + 4 FIRM) = 60 rows, denominators printed",
        doc["denominators"]["families"] == 12 and len(rows) == 60 and doc["denominators"]["rows"] == 60)
    est = [r for r in rows if r["population_scope"] == "ESTATE"]
    firm = [r for r in rows if r["population_scope"].startswith("FIRM:")]
    chk("2 ESTATE rows: hand-count recurrence + the hand-count denominator beside EVERY recurrence, basis declared",
        len(est) == 12 and all(isinstance(r["recurrence"], int) and r["rarity_denominator"] == doc["denominators"]["estate_hand_count_total"]
                               and r["recurrence_basis"] == "FIRST_PASS_HAND_COUNT" for r in est))
    chk("3 FIRM rows: recurrence null with a DECLARED absence semantic (never a fabricated zero)",
        len(firm) == 48 and all(r["recurrence"] is None and "NO_FIGURE_EXISTS" in r["absence_semantic"] for r in firm))
    chk("4 every row: nearest_family != family, distance under a NAMED metric_ref, policy NONE_RATIFIED, vintage present",
        all(r["nearest_family"] != r["family"] and isinstance(r["distance"], int) and "@" in r["metric_ref"]
            and r["policy"] == "NONE_RATIFIED" and r["vintage"]["canonical_head"] for r in rows))
    chk("5 d3_preserving defaults UNKNOWN_NO_D3_DECLARED on every row (today's D3 population)",
        all(r["d3_preserving"] == "UNKNOWN_NO_D3_DECLARED" for r in rows))
    # POSITIVE CONTROL: a declared-D3 pair must read PRESERVED / NOT_PRESERVED -- proving UNKNOWN is a
    # measured default, not a hardcode (the rider MUST NOT emit PRESERVED by default, and must be ABLE to)
    v1, _ = d3_preserving("a", "b", {"a": ["obligation-x"], "b": ["obligation-x"]})
    v2, _ = d3_preserving("a", "b", {"a": ["obligation-x"], "b": ["obligation-y"]})
    chk("6 POSITIVE CONTROL: declared-D3 pairs read PRESERVED (equal sets) / NOT_PRESERVED (differing) -- "
        "UNKNOWN is measured, not hardcoded", v1 == "PRESERVED" and v2 == "NOT_PRESERVED")
    # scope: the ROWS (the axis surfaces a consumer reads) -- the doc-level `no_verdict` DISCLAIMER
    # legitimately names the banned tokens while asserting their absence; scanning it would fail the
    # test on its own guarantee (caught on first run: the check tripped on the disclaimer, not a row)
    rows_blob = json.dumps(doc["rows"]).lower()
    chk("7 NO VERDICT on any ROW: no suspicious/alert/flag/anomal token or key in the emitted rows",
        not any(t in rows_blob for t in ("suspicious", "alert", '"flag"', "anomal"))
        and not any(set(r.keys()) & {"flag", "alert", "suspicious", "verdict"} for r in rows))
    d1, d2 = build_rows(instance_set_path="__no_such_file__"), build_rows(instance_set_path="__no_such_file__")

    def strip(x):
        return json.dumps({**x, "rows": [{k: v for k, v in r.items() if k != "vintage"} for r in x["rows"]]},
                          sort_keys=True, default=str)
    chk("8 TWO-RUN BYTE REPRODUCIBILITY over the same inputs (vintage timestamps excluded)", strip(d1) == strip(d2))
    n = sum(1 for x in ok if x)
    print("--- c2_rarity_rider self-test: %d/%d passed ---" % (n, len(ok)))
    return 0 if n == len(ok) else 1


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or "--help" in args or "-h" in args:
        print("c2_rarity_rider -- R1 LEG 2. --emit <path> [--instances <set.json>] | --self-test | --help. "
              "Unknown flags REFUSE (rc 2). The rider stages axes; it computes NO verdict.")
        return 0
    if "--self-test" in args:
        return self_test()
    if args[0] != "--emit":
        print("c2_rarity_rider: UNKNOWN argument %r -- REFUSED (rc 2)." % args[0], file=sys.stderr)
        return 2
    try:
        inst = args[args.index("--instances") + 1] if "--instances" in args else None
        doc = build_rows(instance_set_path=inst)
        json.dump(doc, open(args[1], "w", encoding="utf-8"), indent=1)
        d = doc["denominators"]
        print("c2_rarity_rider: %d rows (%d families x %d) | estate hand-count denominator %d | spine context %s | wrote %s"
              % (d["rows"], d["families"], d["rows_per_family"], d["estate_hand_count_total"],
                 doc["served_lineage_spine"]["spine_instances"], args[1]))
        return 0
    except Exception as e:  # noqa: BLE001
        print("c2_rarity_rider: ERROR (%s: %s)" % (type(e).__name__, e), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
