#!/usr/bin/env python3
"""NFRA_OUTSET.TO-OS-s-17 battery: a proposal must CITE THE TOOL ROW behind it at <row>@<vintage>,
and the anti-fabrication check it sits beside must keep working.

Run at both required file grains:
  python .tools/tests/test_os17_tool_row.py
  python -m pytest -q .tools/tests/test_os17_tool_row.py

WARN: THE FIRST CONSTRAINT ON THIS CELL IS THAT `evidence_resolves()` MUST SURVIVE. It is a control
that was MEASURED BROKEN on 2026-08-06 -- a prefix match passed 7 of 7 live author calls including a
planted fabrication -- and then repaired. Making a citation criterion pass by weakening it would
trade a proven control for a new one. So the tool-row gate is added BESIDE it, in series, with its
own refusal code; arm D asserts the anti-fabrication limb still fires, and RED MUTANT 1 (arm F)
weakens `evidence_resolves` back to an always-true match and requires arm D's assertion to go RED.
A control nobody has watched fail is a promise.

WHY THE DECISION IS TESTABLE AT ALL: the author loop used to inline it, so the only way to check
which gate refused first was to read the source and believe it. OS-s-17 extracts
`citation_verdict()` -- one named function returning (ok, code, reason) -- and every arm below
exercises THAT, with no model call anywhere in this file.

NO NETWORK, NO AWS, NO MODEL. The strata are produced by the runner's own `_stratum_propagation`,
which needs no repo and no credentials.
"""
from __future__ import annotations

import importlib.util
import os
import shutil
import tempfile
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "infra" / "aws" / "ec2" / "estate-report-runner" / "estate_report_runner.py"

RUNNER_ENV = {
    "ESTATE_REPORT_BUCKET": "os17-battery-not-a-real-bucket",
    "ESTATE_GITHUB_SECRET_ID": "x", "ESTATE_KIMI_SECRET_ID": "x",
    "ESTATE_KIMI_URL": "http://127.0.0.1:1", "ESTATE_KIMI_MODEL": "x",
    "ESTATE_REPO_URL": "http://127.0.0.1:1/x.git",
}

# RED MUTANT 1 -- the anti-fabrication limb weakened back to something a fabrication passes.
ANTIFAB_ANCHOR = (
    "    toks = distinctive_tokens(ref)\n"
    "    if not toks:\n"
    "        return False\n"
    "    return any(t in cited for t in toks)"
)
ANTIFAB_MUTANT = (
    "    toks = distinctive_tokens(ref)\n"
    "    if not toks:\n"
    "        return False\n"
    "    return True  # RED MUTANT: the 2026-08-06 defect restored -- format, not content"
)

# RED MUTANT 2 -- the tool-row requirement removed from the decision entirely.
TOOLROW_ANCHOR = (
    '    if not tool_row_resolves(str(parsed.get("tool_row_cited") or ""), stratum):\n'
    '        return (False, "TOOL_ROW_UNRESOLVED",\n'
    '                "tool_row_cited does not resolve to the stratum tool row at its vintage")'
)
TOOLROW_MUTANT = (
    "    if False:  # RED MUTANT: the tool-row gate removed -- pre-OS-s-17 behaviour\n"
    '        return (False, "TOOL_ROW_UNRESOLVED", "unreachable")'
)

# The evidence_ref a candidate was flagged on, and a citation that genuinely quotes it.
REF = "stratum row: opal-session-analytics lambda, 0 co-change pairs"
HONEST = "as shown, opal-session-analytics has 0 co-change pairs in window"
FABRICATED = "the instrument found a clear coupling across the estate this week"

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, ok, str(detail).replace("\n", " ")[:300]))


def _load(path: Path, name: str):
    keep = {k: os.environ.get(k) for k in RUNNER_ENV}
    os.environ.update(RUNNER_ENV)
    try:
        spec = importlib.util.spec_from_file_location(name, str(path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def _mutant(anchor: str, replacement: str, name: str):
    src = RUNNER.read_text(encoding="utf-8")
    if src.count(anchor) != 1:
        raise AssertionError("mutation anchor count != 1 for %s: %d" % (name, src.count(anchor)))
    tmp = tempfile.mkdtemp(prefix="os17-mutant-")
    path = Path(tmp) / "estate_report_runner.py"
    path.write_text(src.replace(anchor, replacement, 1), encoding="utf-8")
    return _load(path, "os17_mut_%s" % uuid.uuid4().hex), tmp


def _fixture(m):
    """A REAL stratum from the runner's own producer, plus the candidate that came off it."""
    st = m._stratum_propagation("PIN9")
    ref = m.tool_row_ref(st)
    cand = {"_group": "A", "evidence_ref": REF, "_tool_row_ref": ref, "entity": "e", "field": "f"}
    return st, ref, {"A": st}, cand


def _run_battery() -> None:                                                # noqa: C901
    if RESULTS:
        return
    m = _load(RUNNER, "os17_runner_%s" % uuid.uuid4().hex)
    st, ref, strata, cand = _fixture(m)

    def verdict(mod, ec, tc, c=None, s=None):
        return mod.citation_verdict({"evidence_cited": ec, "tool_row_cited": tc},
                                    c or cand, s or strata, set())

    # ---- ARM A: a REAL stratum yields a citable tool row, and it resolves against itself ----
    # TWO SHAPES, because the estate has both and they must behave the same way here. The
    # UNCONFIGURED propagation stratum's honest recipe names tool="none" ("there is nothing to
    # re-run") -- that is OS-s-11's design and it is disclosed rather than glossed; a rail-
    # reproducible row naming a real instrument must be citable identically.
    railed = m._stratum("B_relationships", "q?", [{"r": 1}], "git history @351f309e", "denom",
                        reproduce=m._trace("comp-heat drift",
                                           [".tools/comp-heat drift --budget 60 --json"],
                                           "git history @351f309e", "rail-reproducible"))
    ref_railed = m.tool_row_ref(railed)
    _record("A-REAL-STRATUM-YIELDS-A-CITABLE-TOOL-ROW",
            bool(ref) and "@" in ref and ref.startswith(st["stratum"])
            and m.tool_row_resolves(ref, st) is True
            and bool(ref_railed) and m.tool_row_resolves(ref_railed, railed) is True
            and (railed["reproduce"] or {}).get("tool") == "comp-heat drift",
            "runner-produced stratum -> %r (its recipe honestly names tool=%r, the 'nothing ran' "
            "shape) ; a rail-reproducible row -> %r naming tool=%r ; both resolve against their "
            "own stratum"
            % (ref, (st.get("reproduce") or {}).get("tool"), ref_railed,
               (railed.get("reproduce") or {}).get("tool")))

    # ---- ARM B: it is an AND -- half a citation is not a citation ----
    name, _, vintage = (ref or "@").partition("@")
    cases = {"name only": name, "vintage only": vintage, "empty": "",
             "wrong stratum": "B_relationships@" + vintage, "unrelated prose": "the stratum above"}
    refused = {k: (m.tool_row_resolves(v, st) is False) for k, v in cases.items()}
    _record("B-TOOL-ROW-CITATION-IS-AN-AND-NOT-AN-OR",
            all(refused.values()) and m.tool_row_resolves(ref, st) is True,
            "exact citation accepted; refused: %s -- the stratum NAME is guessable from the "
            "prompt's headings and a VINTAGE is shared by every stratum of the day, so either "
            "alone would resolve to a region rather than to a row" % refused)

    # ---- ARM C: no recipe -> no tool row -> FAILS CLOSED with its own code ----
    bare = m._stratum("X_bare", "q", [{"r": 1}], "v", "d")
    cand_bare = dict(cand, _group="X", _tool_row_ref=m.tool_row_ref(bare))
    v_bare = verdict(m, HONEST, "anything at all", c=cand_bare, s={"X": bare})
    _record("C-A-STRATUM-WITH-NO-RECIPE-FAILS-CLOSED",
            m.tool_row_ref(bare) is None and v_bare[0] is False
            and v_bare[1] == "TOOL_ROW_ABSENT" and "untraceable" in v_bare[2],
            "tool_row_ref(no recipe) = %r ; verdict = %s -- 'untraceable' and 'uncited' are "
            "different findings and get different codes" % (m.tool_row_ref(bare), v_bare[:2]))

    # ---- ARM D: THE ANTI-FABRICATION LIMB STILL FIRES (the constraint on this cell) ----
    v_fab = verdict(m, FABRICATED, ref)
    v_ok = verdict(m, HONEST, ref)
    antifab_fires = (v_fab[0] is False and v_fab[1] == "CITATION_UNRESOLVED")
    _record("D-ANTI-FABRICATION-LIMB-STILL-FIRES",
            antifab_fires and v_ok[0] is True
            and m.evidence_resolves(FABRICATED, REF, set()) is False
            and m.evidence_resolves(HONEST, REF, set()) is True,
            "a fabricated evidence_cited is refused as %s even WITH a perfect tool row; an honest "
            "one passes both gates -> %s. The 2026-08-06 control is untouched" % (v_fab[1], v_ok[:2]))

    # ---- ARM E: THE ORDER IS THE CONTRACT -- both-bad reports the anti-fabrication code ----
    v_both = verdict(m, FABRICATED, "nonsense")
    v_tr = verdict(m, HONEST, "nonsense")
    _record("E-GATES-ARE-IN-SERIES-AND-THE-FIRST-ONE-WINS",
            v_both[1] == "CITATION_UNRESOLVED" and v_tr[1] == "TOOL_ROW_UNRESOLVED"
            and v_both[2] != v_tr[2],
            "both-bad -> %s ; only-tool-row-bad -> %s ; distinct reasons=%s. Collapsing them would "
            "hide the more serious finding behind the newer one"
            % (v_both[1], v_tr[1], v_both[2] != v_tr[2]))

    # ---- ARM F: RED MUTANT 1 -- weaken the anti-fabrication limb; arm D must go RED ----
    mut, tmp = _mutant(ANTIFAB_ANCHOR, ANTIFAB_MUTANT, "antifab")
    try:
        st2, ref2, strata2, cand2 = _fixture(mut)
        mv = mut.citation_verdict({"evidence_cited": FABRICATED, "tool_row_cited": ref2},
                                  cand2, strata2, set())
        _record("F-RED-MUTANT-1-WEAKENED-ANTI-FABRICATION-IS-CAUGHT",
                mv[0] is True and antifab_fires,
                "under the mutant a FABRICATED evidence_cited is ACCEPTED (%s) while production "
                "refuses the identical input (%s) -- so arm D is a live control, not a restatement"
                % (mv[1], v_fab[1]))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    # ---- ARM G: RED MUTANT 2 -- remove the tool-row gate; arm B/E must go RED ----
    mut2, tmp2 = _mutant(TOOLROW_ANCHOR, TOOLROW_MUTANT, "toolrow")
    try:
        st3, ref3, strata3, cand3 = _fixture(mut2)
        mv2 = mut2.citation_verdict({"evidence_cited": HONEST, "tool_row_cited": "nonsense"},
                                    cand3, strata3, set())
        _record("G-RED-MUTANT-2-REMOVED-TOOL-ROW-GATE-IS-CAUGHT",
                mv2[0] is True and v_tr[0] is False,
                "under the mutant a proposal citing 'nonsense' as its tool row is ACCEPTED (%s) "
                "while production refuses the identical input (%s) -- the pre-OS-s-17 behaviour, "
                "reproduced and caught" % (mv2[1], v_tr[1]))
    finally:
        shutil.rmtree(tmp2, ignore_errors=True)

    _record("H-MUTATION-ANCHORS-UNIQUE",
            RUNNER.read_text(encoding="utf-8").count(ANTIFAB_ANCHOR) == 1
            and RUNNER.read_text(encoding="utf-8").count(TOOLROW_ANCHOR) == 1,
            "one occurrence expected for each of the two anchors")

    # ---- ARM I: the author prompt SHOWS the tool row and DEMANDS it back ----
    ctx = {"resources": {"e": {"paths": []}}, "nuggets": [], "corpus_coverage": {}}
    prompt = m.build_author_prompt(ctx, cand)
    _record("I-AUTHOR-PROMPT-SHOWS-THE-TOOL-ROW-AND-REQUIRES-IT",
            "THE TOOL ROW THIS RESTS ON" in prompt and ref in prompt
            and '"tool_row_cited"' in prompt and "copied EXACTLY" in prompt
            and "DISCARDED SEPARATELY" in prompt,
            "the prompt carries the row %r, asks for tool_row_cited, and says the two obligations "
            "are discarded separately" % ref)

    # ---- ARM J: an accepted proposal CARRIES the row, so the artifact resolves on its own ----
    ok, _code, _why = verdict(m, HONEST, ref)
    carried = {"tool_row_cited": ref, "tool_row": cand.get("_tool_row")}
    _record("J-AN-ACCEPTED-PROPOSAL-CAN-CARRY-ITS-ROW",
            ok is True and m.tool_row_resolves(carried["tool_row_cited"], st) is True,
            "the citation a proposal carries resolves against the day's own stratum, so a reader "
            "of the artifact re-runs the recipe without leaving the document")


def _report() -> int:
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    print("OS17-TOOL-ROW BATTERY: %d/%d PASS (denominator %d; 0 model calls, 0 AWS, 0 network)"
          % (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    assert not failed, "OS17 tool-row battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
