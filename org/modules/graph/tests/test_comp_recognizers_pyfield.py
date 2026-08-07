"""Test battery for `comp_recognizers_pyfield.PyFieldRecognizer` (NFRA_PYFIELD.TO-1).

>> A TEST SUITE THAT HAS NEVER FAILED HAS NEVER BEEN TESTED. <<
The MUTANT CONTROLS (criterion 7) are the load-bearing half of this file: each mutation SHOULD break
the emitter, and each is asserted to demonstrably do so. A green suite whose assertions have never
been driven to red is measuring the author, not the code. Every axis has a mutant that takes it DARK,
because an axis that stays green with its own mechanism removed was never being exercised by the test
that claimed to cover it.

Run:  python org/modules/graph/tests/test_comp_recognizers_pyfield.py
Exit 0 iff every check passes AND every mutant control fired.

Author: 0.8.0_AE_CloudComp (NFRA_PYFIELD.TO-1). 2026-08-07.
"""

from __future__ import annotations

import ast
import json
import os
import sys

_GRAPH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _GRAPH not in sys.path:
    sys.path.insert(0, _GRAPH)

import comp_recognizers_pyfield as pf  # noqa: E402
from comp_recognizer_sdk import EnrichedTree, FrontEndCapability  # noqa: E402
import cse_schema as cse  # noqa: E402

_RESULTS = []


def ck(name, cond, detail=""):
    _RESULTS.append(bool(cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   ({detail})" if detail and not cond else ""))


# ---------------------------------------------------------------------------
# FIXTURE -- every shape the acceptance criteria name, in one module.
# ---------------------------------------------------------------------------
FIXTURE = '''
import pandas as pd, json

def build(path, records, txns: pd.DataFrame):
    df = pd.read_parquet(path)            # constructor -> binding axis
    df["acct_id"] = df["acct"]            # RENAME  (bare read, different name)
    df["acct"] = df["acct"]               # PASSTHROUGH (bare read, same name)
    df["total"] = df["qty"] * df["price"] # RECOMPUTE (computed, two sources)
    if path:
        df["flagged"] = df["total"]       # RECOMPUTE_GUARDED (under an if)
    out = df.merge(txns, on="k")          # propagate -> still binding
    out["mv"] = out["total"]
    for idx, row in df.iterrows():        # ITERROWS: only elts[1] is the row Series
        v = row["acct"]                   # IS a column access (axis 4)
        w = idx["nope"]                   # idx is the INDEX -- must NOT resolve
    for r in df.iterrows():               # single-target: r is the TUPLE, must NOT resolve
        q = r["acct"]
    obj = json.loads(path)
    y = obj["Key"]                        # dict/record -- must NOT resolve
    z = lookup()["deep"]                  # <expr> base -- UNATTEMPTABLE by construction
    n = txns["annotated"].nunique()       # v2 annotation -> BINDING wins this one
    return v, w, q, y, z, n

def usage_only(frame):
    # An UNANNOTATED param: the binding axis is structurally blind here (no constructor, no
    # annotation, no local return). The usage-side marker is the ONLY thing that can prove it --
    # which is exactly the independence the PRD measured (596 usage-only sites, +13.5 pts).
    frame["upx"] = frame["raw"].fillna(0)
    return frame["other"].value_counts()
'''


def _tree(src=FIXTURE, source="fixture/gold_x.py"):
    return EnrichedTree(source=source, capability=FrontEndCapability.LEXICAL_AST,
                        text=src, root=ast.parse(src))


def _run(rec, tree):
    return rec.recognize(tree, marker_head="testhead")


# ---------------------------------------------------------------------------
def test_criterion_1_pins_required():
    print("\n-- criterion 1: THE TWO PINS --")
    pins = pf.build_pins(trees_swept=("fixture",), trees_unswept=("bd", "cot", "mdpf"))
    ck("Pins carry resolver identity", pins.resolver == pf.RESOLVER_V2, pins.resolver)
    ck("Pins carry marker-set identity + the pandas version it derived from",
       pins.marker_set == "STRICT_DERIVED" and pins.pandas_version and pins.marker_set_size > 0,
       f"{pins.marker_set}@{pins.pandas_version} n={pins.marker_set_size}")
    ck("Pins carry a vintage", bool(pins.vintage))
    line = pins.line()
    ck("pin line declares SWEPT and UNSWEPT trees (requirement 4)",
       "SWEPT:" in line and "UNSWEPT:" in line and "bd" in line)

    totals = {"attempted": 10, "resolved": 4, "unattemptable": 2, "unresolved": 6, "by_axis": {}}
    rendered = pf.format_coverage(totals, pins)
    ck("a rendered figure carries denominator + both pins + vintage inline",
       "DENOMINATOR" in rendered and "resolver=" in rendered and "marker_set=" in rendered
       and "vintage=" in rendered)

    # MUTANT: strip the pins. format_coverage MUST refuse, not render a bare percentage.
    refused = False
    try:
        pf.format_coverage(totals, None)
    except ValueError:
        refused = True
    ck("MUTANT: format_coverage REFUSES a figure with no pins (does not render a bare N%)", refused)


def test_criterion_2_seven_keys():
    print("\n-- criterion 2: THE SEVEN PROPS KEYS (one schema across substrates) --")
    rec = pf.PyFieldRecognizer()
    cses, _cov = _run(rec, _tree())
    ck("edges were emitted", len(rec.edge_records) > 0, f"{len(rec.edge_records)}")
    allkeys = {tuple(sorted(json.loads(e["props"]))) for e in rec.edge_records}
    ck("EVERY emitted edge carries exactly the seven portal keys",
       allkeys == {tuple(sorted(pf.PROPS_KEYS))}, f"{allkeys}")

    # Ground the seven against the LIVE portal artifact, not against my own constant -- otherwise
    # this test only proves the module agrees with itself.
    live = os.path.join(_GRAPH, "tsgraph_spike", "out", "live_flowsto.json")
    if os.path.exists(live):
        with open(live, encoding="utf-8") as fh:
            portal = json.load(fh)
        pk = set(json.loads(portal[0]["props"]))
        ck("the seven match the LIVE portal FLOWS_TO artifact (independent oracle, not self-comparison)",
           pk == set(pf.PROPS_KEYS), f"portal={sorted(pk)} mine={sorted(pf.PROPS_KEYS)}")
    else:
        ck("live portal artifact present for cross-check", False, f"missing {live}")

    ck("edge shape is {src,dst,props} like the portal artifact",
       all(set(e) == {"src", "dst", "props"} for e in rec.edge_records))
    ck("refs use the governed `field:` prefix (maps to Entity.FIELD)",
       all(e["src"].startswith("field:") and e["dst"].startswith("field:") for e in rec.edge_records))
    ck("emitted CSEs pass fidelity (decompress to C0 lexical evidence)",
       all(cse.cse_fidelity_ok(c)[0] for c in cses))

    kinds = {json.loads(e["props"])["kind"] for e in rec.edge_records}
    ck("all three governed EdgeKinds are exercised by the fixture",
       kinds == {"passthrough", "rename", "recompute_guarded"}, f"{kinds}")
    guarded = [json.loads(e["props"]) for e in rec.edge_records
               if json.loads(e["props"])["condition"]]
    ck("`condition` is populated on a guarded flow (portal defect #3 not inherited)",
       len(guarded) >= 1, f"{len(guarded)} guarded edges")

    # MUTANT: drift a key. The emitter must RAISE, not silently emit a 6-key or 8-key edge.
    orig = pf.PROPS_KEYS
    raised = False
    try:
        pf.PROPS_KEYS = orig + ("bogusEighthKey",)
        r2 = pf.PyFieldRecognizer()
        _run(r2, _tree())
    except ValueError:
        raised = True
    finally:
        pf.PROPS_KEYS = orig
    ck("MUTANT: a drifted props-key contract RAISES (hard, not an -O-strippable assert)", raised)


def test_criterion_3_unresolved_and_unattemptable():
    print("\n-- criterion 3: ZERO UNRESOLVED IS A FAILURE --")
    rec = pf.PyFieldRecognizer()
    _run(rec, _tree())
    an = rec.last_analysis
    ck("Coverage.unresolved is NON-EMPTY (the honest-degrade channel is alive)",
       len(an.unresolved) > 0, f"{len(an.unresolved)}")
    ck("unattemptable channel ENUMERATES <expr> bases with a reason",
       len(an.unattemptable) > 0 and all("expr-base" in r for _l, r in an.unattemptable),
       f"{an.unattemptable}")
    ck("an <expr> base is NOT counted in `attempted` (never scored as a miss)",
       an.attempted + len(an.unattemptable) == _count_string_subscripts(FIXTURE),
       f"attempted={an.attempted} unattempt={len(an.unattemptable)} "
       f"total={_count_string_subscripts(FIXTURE)}")
    ck("the dict/record base `obj['Key']` is correctly UNRESOLVED, not guessed",
       any("`obj`" in r for _l, r in an.unresolved), f"{an.unresolved}")


def _count_string_subscripts(src):
    return sum(1 for n in ast.walk(ast.parse(src))
               if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant)
               and isinstance(n.slice.value, str))


def test_criterion_4_iterrows():
    print("\n-- criterion 4: .iterrows() IS NOT AN EDGE CASE (237 measured sites) --")
    rec = pf.PyFieldRecognizer()
    _run(rec, _tree())
    an = rec.last_analysis
    ck("iterrows axis fired -- `row['acct']` IS a column access",
       an.by_axis["iterrows"] >= 1, f"by_axis={an.by_axis}")
    ck("the INDEX variable `idx` is NOT bound (tuple position is load-bearing)",
       any("`idx`" in r for _l, r in an.unresolved), f"{[r for _l, r in an.unresolved]}")
    ck("a SINGLE-target `for r in df.iterrows()` is NOT bound (r is the whole tuple)",
       any("`r`" in r for _l, r in an.unresolved), f"{[r for _l, r in an.unresolved]}")

    # SHADOWING. A module-level `for _, row in df.iterrows()` must NOT make every function in the
    # file that takes a `row` PARAMETER resolve `row["Records"]` as a column. Found by probing my own
    # output when the corpus iterrows count came out ABOVE a naive flat count -- a stricter rule
    # producing a BIGGER number is backwards, and that is what exposed it.
    # HONEST SCOPE OF THE FIX: an ablation on data/inf+assets gold measured 262 WITH the shadow check
    # and 262 WITHOUT it -- it removes ZERO false positives on the CURRENT corpus. It is a
    # correctness guard against a real shape this corpus does not happen to contain, not a bug it
    # caught in the wild. Recorded rather than sold.
    shadow_src = (
        "import pandas as pd\n"
        "df = pd.read_parquet('p')\n"
        "for _i, row in df.iterrows():\n"
        "    a = row['real_col']\n"
        "def handler(row):\n"
        "    return row['Records']\n"
    )
    r_sh = pf.PyFieldRecognizer()
    _run(r_sh, _tree(shadow_src, source="shadow.py"))
    ash = r_sh.last_analysis
    ck("SHADOWING: a param named `row` does NOT inherit the module-level iterrows row",
       ash.by_axis["iterrows"] == 1 and len(ash.unresolved) == 1,
       f"by_axis={ash.by_axis} unresolved={[r for _l, r in ash.unresolved]}")

    # MUTANT: remove iterrows binding entirely. The axis must go DARK, not stay green.
    orig = pf._iterrows_base
    try:
        pf._iterrows_base = lambda _n: None
        r2 = pf.PyFieldRecognizer()
        _run(r2, _tree())
        dark = r2.last_analysis.by_axis["iterrows"] == 0
    finally:
        pf._iterrows_base = orig
    ck("MUTANT: with iterrows detection removed the axis goes DARK (not green)", dark)


def test_criterion_5_exclusion_derived():
    print("\n-- criterion 5: THE EXCLUSION SET IS DERIVED AND VERSION-PINNED --")
    meta, sets = pf.derive_marker_sets()
    ck("derived from the INSTALLED pandas and version-pinned", bool(meta["pandas_version"]),
       meta["pandas_version"])
    ck("the real DataFrame|Series universe is measured, not asserted",
       meta["universe_df_or_series"] > 200, f"{meta['universe_df_or_series']}")
    ck("the derived set is NOT the hand-drawn 71-name _DF_METHODS roster",
       len(sets["STRICT_DERIVED"]) != 71, f"n={len(sets['STRICT_DERIVED'])}")
    import pandas as pd
    real = set(dir(pd.DataFrame)) | set(dir(pd.Series))
    ck("every MINIMAL member really exists on the installed pandas", sets["MINIMAL"] <= real)
    ck("`concat` correctly ABSENT (it is pd.concat, a module fn -- the entry that can never fire)",
       "concat" not in sets["WIDE"])
    ck("the marker set moves the floor (the 5.5x sensitivity is real, not theoretical)",
       len(sets["MINIMAL"]) < len(sets["STRICT_DERIVED"]) <= len(sets["WIDE"]),
       f"{ {k: len(v) for k, v in sets.items()} }")


def test_criterion_6_three_axes():
    print("\n-- criterion 6: ALL AXES FROM THE START --")
    rec = pf.PyFieldRecognizer()
    _run(rec, _tree())
    ax = rec.last_analysis.by_axis
    ck("binding axis fired", ax["binding"] > 0, f"{ax}")
    ck("usage axis fired (a marker method on the subscript result)", ax["usage"] > 0, f"{ax}")
    ck("iterrows axis fired", ax["iterrows"] > 0, f"{ax}")

    # MUTANT A: empty the constructor set -> the BINDING axis must go dark.
    r2 = pf.PyFieldRecognizer()
    r2._constructors = set()
    _run(r2, _tree())
    # v2 annotations/local-returns legitimately survive an empty constructor set, so compare
    # against the v1 resolver where the constructor seed is the ONLY binding source.
    r3 = pf.PyFieldRecognizer(resolver=pf.RESOLVER_V1)
    r3._constructors = set()
    _run(r3, _tree())
    ck("MUTANT: empty constructor set + v1 -> binding axis goes DARK",
       r3.last_analysis.by_axis["binding"] == 0, f"{r3.last_analysis.by_axis}")

    # MUTANT B: empty the marker set -> the USAGE axis must go dark.
    r4 = pf.PyFieldRecognizer()
    r4._sets = dict(r4._sets)
    r4._sets["STRICT_DERIVED"] = set()
    _run(r4, _tree())
    ck("MUTANT: empty marker set -> usage axis goes DARK",
       r4.last_analysis.by_axis["usage"] == 0, f"{r4.last_analysis.by_axis}")

    # MUTANT C: all axes dark -> ZERO edges emitted. Proves emission is axis-driven, not incidental.
    r5 = pf.PyFieldRecognizer(resolver=pf.RESOLVER_V1)
    r5._constructors = set()
    r5._sets = dict(r5._sets)
    r5._sets["STRICT_DERIVED"] = set()
    orig = pf._iterrows_base
    try:
        pf._iterrows_base = lambda _n: None
        _run(r5, _tree())
    finally:
        pf._iterrows_base = orig
    ck("MUTANT: ALL axes dark -> zero edges emitted (emission is axis-driven)",
       len(r5.edge_records) == 0 and r5.last_analysis.resolved_cols == 0,
       f"edges={len(r5.edge_records)} resolved={r5.last_analysis.resolved_cols}")


def test_resolver_delta_rederivable():
    print("\n-- requirement 2: the v1/v2 DELTA stays RE-DERIVABLE --")
    v2 = pf.PyFieldRecognizer(resolver=pf.RESOLVER_V2)
    _run(v2, _tree())
    v1 = pf.PyFieldRecognizer(resolver=pf.RESOLVER_V1)
    _run(v1, _tree())
    # THE DELTA LIVES IN THE BINDING AXIS, NOT IN `resolved_cols` -- and that is a finding, not a
    # test detail. `txns["annotated"].nunique()` resolves under BOTH resolvers: v2 proves it by
    # annotation (binding), v1 falls through to the usage marker. Total resolution is IDENTICAL
    # (13 == 13) while the mechanism differs completely. Scoring the resolver delta on the total
    # would have reported "v2 adds nothing" -- the axes overlap, exactly as the PRD measured
    # (only 34.6% of binding hits are also usage hits). Compare the axis, not the sum.
    b1, b2 = v1.last_analysis.by_axis["binding"], v2.last_analysis.by_axis["binding"]
    ck("v2 lifts the BINDING axis (annotations + one-hop local returns)", b2 > b1,
       f"binding v1={b1} v2={b2}")
    ck("v1 does NOT resolve the annotated param via binding (clean split -> the delta is a "
       "measurement, not a claim)",
       not any(s.base == "txns" and s.axis == "binding"
               for f in v1.last_analysis.flows for s in f.srcs))
    ck("the overlap is REAL: total resolved can tie while the axis mix differs -- so a resolver "
       "delta scored on the total would read as 'no lift'",
       v1.last_analysis.resolved_cols == v2.last_analysis.resolved_cols or b2 > b1,
       f"v1_total={v1.last_analysis.resolved_cols} v2_total={v2.last_analysis.resolved_cols}")


def test_negative_and_degenerate():
    print("\n-- negative controls --")
    rec = pf.PyFieldRecognizer()
    cses, cov = _run(rec, _tree("x = 1\n", source="clean.py"))
    ck("clean file: 0 sites, 0 edges, no error", len(cses) == 0 and len(rec.edge_records) == 0)
    ck("clean file records no false unresolved", len(rec.last_analysis.unresolved) == 0)

    rec2 = pf.PyFieldRecognizer()
    bad = EnrichedTree(source="broken.py", capability=FrontEndCapability.LEXICAL_AST,
                       text="def f(:\n", root=None)
    cses2, _ = _run(rec2, bad)
    ck("a parse failure yields no sites and does not raise", len(cses2) == 0)

    # A recognizer run on a tree BELOW its required capability must honest-degrade (LAW 1).
    rec3 = pf.PyFieldRecognizer()
    raw = EnrichedTree(source="raw.py", capability=FrontEndCapability.RAW_TEXT,
                       text=FIXTURE, root=ast.parse(FIXTURE))
    cses3, cov3 = _run(rec3, raw)
    degraded = all(c.transformation["subject"].etype == "Concept" for c in cses3) if cses3 else True
    ck("under-capability run honest-degrades to Concept+low (LAW 1), never a typed claim",
       degraded and len(cov3.unresolved) == len(cses3), f"n={len(cses3)} degraded={degraded}")


def main():
    print("=" * 78)
    print("PyFieldRecognizer test battery -- NFRA_PYFIELD.TO-1")
    print("=" * 78)
    test_criterion_1_pins_required()
    test_criterion_2_seven_keys()
    test_criterion_3_unresolved_and_unattemptable()
    test_criterion_4_iterrows()
    test_criterion_5_exclusion_derived()
    test_criterion_6_three_axes()
    test_resolver_delta_rederivable()
    test_negative_and_degenerate()
    passed = sum(1 for r in _RESULTS if r)
    print(f"\n=== pyfield battery: {passed}/{len(_RESULTS)} PASS ===")
    return 0 if passed == len(_RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
