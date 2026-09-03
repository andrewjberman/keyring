#!/usr/bin/env python3
"""Planted-mutant battery for comp-atomcheck v1 (TIGHTENING_ENUMERATION_SPEC J3.6 A1-A4).

A passing assertion never mutated has never been tested. Every arm below plants ONE defect
and asserts the verdict FLIPS -- and each is paired with a negative control on the unmutated
fixture, so an arm that would pass no matter what is visible as such.

Fixtures are SEALED synthetic key lists, never live S3: the runner is read-only by
construction and a mutant must never be written into a production bucket to be exercised.

Run: python .tools/tests/test_atomcheck.py
"""
from __future__ import annotations

import sys
from pathlib import Path

_WS = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(_WS))

from org.modules.graph.atomcheck_cli import (  # noqa: E402
    CONFORMS, NOT_CHECKABLE, NOT_CHECKABLE_ATOMS, PARTIAL_RESIDUE, PRODUCTS, VIOLATES,
    _partition_index, atom1_grammar, atom3_manifests, atom7_spelling, atom8_lineage,
)

CFG = PRODUCTS[("advi", "49financial")]
PASS = FAIL = 0
ARMS: list[str] = []


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        ARMS.append("  PASS  %s" % name)
    else:
        FAIL += 1
        ARMS.append("  FAIL  %s  %s" % (name, detail))


# A clean fixture: two scopes, both declared; every data partition manifested locally.
CLEAN = [
    "canonical/twr_daily/date=2026-08-20/data.parquet",
    "canonical/twr_daily/date=2026-08-20/manifest.json",
    "dimensions/dim_account/date=2026-08-20/data.parquet",
    "dimensions/dim_account/date=2026-08-20/manifest.json",
    "_logs/chain_20260820T124542Z.log",
]


def run(keys):
    parts, uscore, other = _partition_index(keys)
    return parts, uscore, other


_RAN = False


def _run_battery():
    """EVERY piece of work the battery does lives here, so IMPORT IS INERT (the T-16 pass-2 shape,
    03cf4d17ac; NFRA_COMPEFFICACY F6, 92794). Called once per process by test_all_arms_pass (pytest)
    or _report (direct). The atomcheck_cli import stays at module level (first-party, 0.08 s, no subprocess); the arms ran at import before this."""
    global _RAN
    if _RAN:
        return
    _RAN = True
    # --------------------------------------------------------------------------- A2
    # MUTANT, GRAMMAR: a key that violates the product-root grammar -> atom 1 VIOLATES,
    # NAMING it. Silence is FAIL.
    p, u, o = run(CLEAN)
    r = atom1_grammar(CFG, CLEAN, p, u, o)
    check("A2 negative control: clean fixture -> atom 1 CONFORMS",
          r["verdict"] == CONFORMS, r["verdict"] + " | " + r["evidence"])

    MUT_SCOPE = CLEAN + ["reference/ref_txn/date=2026-08-20/data.parquet"]
    p, u, o = run(MUT_SCOPE)
    r = atom1_grammar(CFG, MUT_SCOPE, p, u, o)
    check("A2 mutant undeclared-scope -> atom 1 VIOLATES", r["verdict"] == VIOLATES, r["verdict"])
    check("A2 mutant undeclared-scope -> the row NAMES the offending scope",
          "reference" in r["evidence"], r["evidence"][:120])

    MUT_SHAPE = CLEAN + ["canonical/twr_daily/2026-08-20/data.parquet"]  # no date= partition
    p, u, o = run(MUT_SHAPE)
    r = atom1_grammar(CFG, MUT_SHAPE, p, u, o)
    check("A2 mutant ungrammatical-key -> atom 1 VIOLATES", r["verdict"] == VIOLATES, r["verdict"])
    check("A2 mutant ungrammatical-key -> counted in the 'matching neither' denominator",
          "1 matching neither" in r["denominator"], r["denominator"])

    # --------------------------------------------------------------------------- atom 3
    p, u, o = run(CLEAN)
    r = atom3_manifests(CFG, p, u)
    check("atom3 negative control: clean fixture -> CONFORMS", r["verdict"] == CONFORMS, r["verdict"])

    MUT_MAN = [k for k in CLEAN if k != "canonical/twr_daily/date=2026-08-20/manifest.json"]
    p, u, o = run(MUT_MAN)
    r = atom3_manifests(CFG, p, u)
    check("atom3 mutant drop-manifest -> VIOLATES", r["verdict"] == VIOLATES, r["verdict"])
    check("atom3 mutant drop-manifest -> denominator moves to 1 uncovered",
          "1 uncovered" in r["denominator"], r["denominator"])

    # the SIDECAR convention must also satisfy atom 3 -- and at (scope,table,date) grain, not scope
    SIDE = MUT_MAN + ["canonical/_manifests/2026-08-20/20260821T141728Z__twr_daily.json"]
    p, u, o = run(SIDE)
    r = atom3_manifests(CFG, p, u)
    check("atom3 sidecar convention satisfies coverage -> CONFORMS", r["verdict"] == CONFORMS,
          r["verdict"] + " | " + r["denominator"])

    # GRAIN GUARD: a sidecar for a DIFFERENT table must NOT cover twr_daily. If this arm fails,
    # the leg is resolving coverage at scope grain and manufacturing a pass.
    WRONG_TBL = MUT_MAN + ["canonical/_manifests/2026-08-20/20260821T141728Z__some_other_table.json"]
    p, u, o = run(WRONG_TBL)
    r = atom3_manifests(CFG, p, u)
    check("atom3 GRAIN GUARD: a sidecar for another table does NOT cover this one -> VIOLATES",
          r["verdict"] == VIOLATES, r["verdict"] + " | " + r["denominator"])

    # --------------------------------------------------------------------------- atom 7
    r = atom7_spelling(CFG, CLEAN)
    check("atom7 negative control: date= hyphens are NOT violations -> CONFORMS",
          r["verdict"] == CONFORMS, r["verdict"] + " | " + r["evidence"][:100])

    SIDE_KEYS = ["dimensions/_manifests/2026-08-18/20260819T172917Z__alias_key_expansion.json"]
    r = atom7_spelling(CFG, SIDE_KEYS)
    check("atom7 negative control: {data-as-of} + ISO stamp hyphens are NOT violations",
          r["verdict"] == CONFORMS, r["verdict"] + " | " + r["evidence"][:140])

    MUT_SPELL = CLEAN + ["canonical/twr-daily/date=2026-08-20/data.parquet"]
    r = atom7_spelling(CFG, MUT_SPELL)
    check("atom7 mutant hyphen-in-table -> VIOLATES", r["verdict"] == VIOLATES, r["verdict"])
    check("atom7 mutant hyphen-in-table -> the row NAMES the key",
          "twr-daily" in str(r["evidence"]), str(r["evidence"])[:120])

    # --------------------------------------------------------------------------- A3 (atom 8)
    r = atom8_lineage(CFG)
    check("A3 no lineage declaration -> NOT-CHECKABLE, and NEVER CONFORMS",
          r["verdict"] == NOT_CHECKABLE and r["verdict"] != CONFORMS, r["verdict"])
    check("A3 the NOT-CHECKABLE row carries a why", bool(r.get("why")), str(r))

    import json  # noqa: E402
    import tempfile  # noqa: E402

    tmp = Path(tempfile.mkdtemp())
    (tmp / "lineage.json").write_text(json.dumps({"famA": {"field_ok": "endpoint.x"}}), encoding="utf-8")
    (tmp / "exc.json").write_text(json.dumps([{"id": "D1", "field_paths": ["*allowed*"]}]), encoding="utf-8")
    (tmp / "census.json").write_text(json.dumps(
        {"families": {"famA": {"fields": ["field_ok", "allowed_thing"]}}}), encoding="utf-8")
    cfg2 = dict(CFG)
    for k, v in (("lineage_declaration", "lineage.json"), ("exception_set", "exc.json"),
                 ("served_census", "census.json")):
        cfg2[k] = str((tmp / v).relative_to(tmp))
    import org.modules.graph.atomcheck_cli as ac  # noqa: E402
    _orig_ws = ac._WORKSPACE
    ac._WORKSPACE = tmp
    r = atom8_lineage(cfg2)
    check("A3 negative control: every served field declared or excepted -> CONFORMS",
          r["verdict"] == CONFORMS, r["verdict"] + " | " + str(r["evidence"])[:120])

    (tmp / "census.json").write_text(json.dumps(
        {"families": {"famA": {"fields": ["field_ok", "allowed_thing", "smuggled_field"]}}}),
        encoding="utf-8")
    r = atom8_lineage(cfg2)
    check("A3 mutant planted-undeclared-field -> VIOLATES", r["verdict"] == VIOLATES, r["verdict"])
    check("A3 mutant -> verdict is ILLEGITIMATELY-DERIVED and NAMES the field",
          "ILLEGITIMATELY-DERIVED" in str(r["evidence"]) and "smuggled_field" in str(r["evidence"]),
          str(r["evidence"])[:160])
    ac._WORKSPACE = _orig_ws

    # --------------------------------------------------------------------------- A4 enum honesty
    src = (_WS / "org/modules/graph/atomcheck_cli.py").read_text(encoding="utf-8")
    check("A4 every out-of-scope atom is declared with a why",
          all(len(v) == 2 and v[1] for v in NOT_CHECKABLE_ATOMS.values())
          and all(len(v) == 2 and v[1] for v in PARTIAL_RESIDUE.values()),
          "a NOT-CHECKABLE atom without a why is silence wearing a verdict")
    check("A4 the out-of-scope atoms are exactly {2,4,6} plus the 5/7 residue halves",
          set(NOT_CHECKABLE_ATOMS) == {2, 4, 6} and set(PARTIAL_RESIDUE) == {5, 7},
          str(sorted(NOT_CHECKABLE_ATOMS)) + " " + str(sorted(PARTIAL_RESIDUE)))
    check("A4 no unimplemented atom can print CONFORMS -- its rows are constructed with the "
          "NOT_CHECKABLE constant only",
          'NOT_CHECKABLE, "no v1 leg"' in src and 'NOT_CHECKABLE,\n                         "no v1 leg for this half"' in src,
          "the two residue loops must both emit NOT_CHECKABLE literally")


def _report() -> int:
    _run_battery()
    print("comp-atomcheck planted-mutant battery")
    print("\n".join(ARMS))
    print()
    print("ARMS: %d passed / %d failed / %d total" % (PASS, FAIL, PASS + FAIL))
    return 1 if FAIL else 0


def test_all_arms_pass():
    _run_battery()
    failed = [a.strip() for a in ARMS if a.startswith("  FAIL")]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), PASS + FAIL, failed)
    print("ARMS: %d passed / %d failed / %d total" % (PASS, FAIL, PASS + FAIL))


if __name__ == "__main__":
    sys.exit(_report())
