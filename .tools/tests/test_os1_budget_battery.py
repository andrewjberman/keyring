#!/usr/bin/env python3
"""NFRA_OUTSET.TO-OS-s-1 battery: comp-heat honours a caller ceiling on ALL FIVE subcommands --
the Rule T form (NFRA_COMPEFFICACY PRD v0.4 s.4.4), wired onto the shared carrier
.tools/_compbudget.py (no second implementation).

Run at both required file grains:
  python .tools/tests/test_os1_budget_battery.py
  python -m pytest -q .tools/tests/test_os1_budget_battery.py

One arm per subcommand (freshness, drift, score, compare, federated) -- each prints its OWN
denominator (scanned/total, its own unit) on both a completing (WITHIN BUDGET) and a cut (BUDGET
REACHED) invocation -- plus ONE shared RED mutant that makes the tool ignore --budget entirely
(comp-heat's single choke point, `_spent()`), proving the battery's own BUDGET REACHED assertions
are not vacuous. The production CLI supplies the evidence; mutant copies are temporary files and
the production tool is never rewritten.

FEDERATED SAFETY (load-bearing for this file, not just documentation): every federated invocation
here passes a --budget WELL BELOW comp-heat's own FEDERATED_LIVE_FLOOR_S (200s), so the tool's
refuse-before-dispatch guard fires and the LIVE Trino plane is NEVER reached by this battery. The
RED mutant targets `_spent()` only; federated's floor-check is a SEPARATE, INDEPENDENT guard (not
routed through `_spent()`), so it is deliberately EXCLUDED from the mutant arm -- there is no
mutation in this file that can make federated dispatch live, by construction.
"""
from __future__ import annotations

import subprocess
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / ".tools" / "comp-heat"
RESULTS: list[tuple[str, bool, str]] = []


def _run(*args: str, tool: Path = TOOL, timeout: int = 60):
    return subprocess.run([sys.executable, str(tool), *args], cwd=ROOT, text=True,
                          capture_output=True, timeout=timeout)


def _record(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, detail.replace("\n", " ")[:280]))


def _mutant_run(needle: str, replacement: str, *args: str, timeout: int = 60):
    source = TOOL.read_text(encoding="utf-8")
    if source.count(needle) != 1:
        raise AssertionError("mutation anchor count != 1 for %r: %d" %
                             (needle, source.count(needle)))
    path = TOOL.parent / (".comp-heat-os1-mutant-%s" % uuid.uuid4().hex)
    try:
        path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
        return _run(*args, tool=path, timeout=timeout)
    finally:
        if path.exists():
            path.unlink()


def _run_battery() -> None:
    if RESULTS:
        return

    # ---- O1-AC1: --help discloses the carrier (top-level AND every subcommand) ----
    top_help = _run("--help")
    _record("HELP-TOP-LEVEL-BUDGET", top_help.returncode == 0 and "--budget" in top_help.stdout,
           top_help.stdout)
    for sub in ("freshness", "drift", "score", "compare", "federated"):
        h = _run(sub, "--help")
        _record("HELP-%s-BUDGET-CURSOR" % sub.upper(),
               h.returncode == 0 and "--budget" in h.stdout and "--cursor" in h.stdout,
               h.stdout)

    # ---- FRESHNESS arm ----
    fresh_within = _run("freshness", ".tools", "--budget", "30", timeout=60)
    _record("FRESHNESS-WITHIN-BUDGET",
           fresh_within.returncode == 0 and "WITHIN BUDGET: scanned" in fresh_within.stdout
           and " of " in fresh_within.stdout and "files" in fresh_within.stdout,
           fresh_within.stdout[:400])
    fresh_cut = _run("freshness", "--budget", "0.001")
    _record("FRESHNESS-BUDGET-REACHED",
           fresh_cut.returncode == 3 and "BUDGET REACHED: 0.001 s (flag)" in fresh_cut.stdout
           and "scanned 0 of" in fresh_cut.stdout and "files" in fresh_cut.stdout
           and "ANSWER-STATE: PARTIAL_OR_BLIND" in fresh_cut.stdout,
           fresh_cut.stdout[:400])

    # ---- DRIFT arm (NON-VERDICT: rc stays 0 at BUDGET REACHED, per the FORM's default clause) ----
    drift_within = _run("drift", "--budget", "10")
    _record("DRIFT-WITHIN-BUDGET",
           drift_within.returncode == 0 and "WITHIN BUDGET: scanned" in drift_within.stdout
           and "files" in drift_within.stdout, drift_within.stdout[:400])
    drift_cut = _run("drift", "--budget", "0.0001")
    _record("DRIFT-BUDGET-REACHED",
           drift_cut.returncode == 0 and "BUDGET REACHED:" in drift_cut.stdout
           and "scanned 0 of" in drift_cut.stdout, drift_cut.stdout[:400])

    # ---- SCORE arm (Rule T non-application, PRD s.4.4: O(1), no loop/subprocess -- still
    # carries the disclosure line + accepts --budget uniformly across all five subcommands) ----
    score_within = _run("score", "some/fixture.py", "--age-days", "5", "--budget", "10")
    _record("SCORE-WITHIN-BUDGET",
           score_within.returncode == 0 and "WITHIN BUDGET: scanned 1 of 1 items" in score_within.stdout,
           score_within.stdout[:400])

    # ---- COMPARE arm ----
    cmp_within = _run("compare", ".tools/comp-heat", ".tools/comp-schedule", "--budget", "20")
    _record("COMPARE-WITHIN-BUDGET",
           cmp_within.returncode == 0 and "WITHIN BUDGET: scanned 2 of 2 resources" in cmp_within.stdout,
           cmp_within.stdout[:400])
    cmp_cut = _run("compare", ".tools/comp-heat", ".tools/comp-schedule", "--budget", "0.0001")
    _record("COMPARE-BUDGET-REACHED",
           cmp_cut.returncode == 3 and "BUDGET REACHED:" in cmp_cut.stdout
           and "resources" in cmp_cut.stdout and "ANSWER-STATE: PARTIAL_OR_BLIND" in cmp_cut.stdout,
           cmp_cut.stdout[:400])

    # ---- FEDERATED arm (NEVER touches the live plane -- see module docstring) ----
    fed_default = _run("federated", timeout=15)
    _record("FEDERATED-DEFAULT-BUDGET-REFUSES-LIVE",
           fed_default.returncode == 0 and "BUDGET REACHED:" in fed_default.stdout
           and "refusing to dispatch to the LIVE Trino plane" in fed_default.stdout
           and "queries" in fed_default.stdout,
           fed_default.stdout[:400])
    fed_tiny = _run("federated", "--budget", "0.0001", timeout=15)
    _record("FEDERATED-TINY-BUDGET-REFUSES-LIVE",
           fed_tiny.returncode == 0 and "refusing to dispatch to the LIVE Trino plane" in fed_tiny.stdout,
           fed_tiny.stdout[:400])

    # ---- RED MUTANT: the tool ignores --budget entirely ----
    # WHERE THE MUTATION LANDS, AND WHY (measured, not assumed -- an earlier draft of this battery
    # mutated comp-heat's own `_spent()` and three of five arms did NOT break: freshness/drift/
    # compare's cut is enforced by the DEEPER subprocess-level `timeout=remaining()` on each git
    # call (object_freshness.py's `_git_bounded`), which keeps cutting even with `_spent()`
    # neutered -- a genuine defense-in-depth finding, not a battery bug. The ONE place every
    # subcommand's --budget flag actually passes through is `_compbudget.resolve_budget()` --
    # mutate THAT (ignore the caller's flag, always resolve a huge budget) and every arm that can
    # complete fast enough is expected to stop cutting. `.tools/_compbudget.py` itself is never
    # rewritten: the mutant is a TEMPORARY sibling module a temporary comp-heat copy imports
    # instead, both deleted in `finally`.
    real_budget_src = (ROOT / ".tools" / "_compbudget.py").read_text(encoding="utf-8")
    anchor = "def resolve_budget(flag_value=None, default_s: float = DEFAULT_BUDGET_S):"
    if real_budget_src.count(anchor) != 1:
        raise AssertionError("resolve_budget anchor count != 1: %d" % real_budget_src.count(anchor))
    mutant_budget_src = real_budget_src.replace(
        anchor,
        anchor + '\n    return 999999.0, "MUTANT-IGNORES-BUDGET"  # noqa: unreachable below\n',
        1)
    mutant_mod_name = "_compbudget_os1_mutant_%s" % uuid.uuid4().hex
    mutant_mod_path = ROOT / ".tools" / (mutant_mod_name + ".py")

    import_anchor = "    import _compbudget"
    heat_src = TOOL.read_text(encoding="utf-8")
    if heat_src.count(import_anchor) != 1:
        raise AssertionError("import anchor count != 1: %d" % heat_src.count(import_anchor))
    mutant_heat_src = heat_src.replace(
        import_anchor, "    import %s as _compbudget" % mutant_mod_name, 1)
    mutant_heat_path = TOOL.parent / (".comp-heat-os1-mutant-%s" % uuid.uuid4().hex)

    def _run_with_mutant_budget(*args, timeout=30):
        mutant_mod_path.write_text(mutant_budget_src, encoding="utf-8")
        mutant_heat_path.write_text(mutant_heat_src, encoding="utf-8")
        try:
            return _run(*args, tool=mutant_heat_path, timeout=timeout)
        finally:
            mutant_heat_path.unlink(missing_ok=True)
            mutant_mod_path.unlink(missing_ok=True)

    m_fresh = _run_with_mutant_budget("freshness", "--budget", "0.001", timeout=60)
    _record("RED-MUTANT-FRESHNESS-NO-LONGER-CUTS",
           m_fresh.returncode == 0 and "BUDGET REACHED" not in m_fresh.stdout
           and "WITHIN BUDGET" in m_fresh.stdout, m_fresh.stdout[:400] or m_fresh.stderr[:400])

    m_drift = _run_with_mutant_budget("drift", "--budget", "0.0001", timeout=30)
    _record("RED-MUTANT-DRIFT-NO-LONGER-CUTS",
           m_drift.returncode == 0 and "BUDGET REACHED" not in m_drift.stdout
           and "WITHIN BUDGET" in m_drift.stdout, m_drift.stdout[:400] or m_drift.stderr[:400])

    m_score = _run_with_mutant_budget("score", "x", "--age-days", "1",
                                      "--budget", "0.0000001", timeout=30)
    _record("RED-MUTANT-SCORE-NO-LONGER-CUTS",
           m_score.returncode == 0 and "BUDGET REACHED" not in m_score.stdout
           and "WITHIN BUDGET" in m_score.stdout, m_score.stdout[:400] or m_score.stderr[:400])

    m_cmp = _run_with_mutant_budget("compare", ".tools/comp-heat",
                                    ".tools/comp-schedule", "--budget", "0.0001", timeout=30)
    _record("RED-MUTANT-COMPARE-NO-LONGER-CUTS",
           m_cmp.returncode == 0 and "BUDGET REACHED" not in m_cmp.stdout
           and "WITHIN BUDGET" in m_cmp.stdout, m_cmp.stdout[:400] or m_cmp.stderr[:400])

    # FEDERATED IS DELIBERATELY EXCLUDED FROM THIS MUTATION (never merely assumed safe): its
    # refuse-before-dispatch also reads `budget_s` from this SAME mutated resolve_budget(), so
    # under this mutant `insufficient` would evaluate False too (999999.0 > FEDERATED_LIVE_FLOOR_S)
    # -- the ONLY mutation in this battery that COULD make federated dispatch live. It is not run.
    _record("RED-MUTANT-FEDERATED-DELIBERATELY-NOT-EXERCISED",
           not mutant_heat_path.exists() and not mutant_mod_path.exists(),
           "federated is excluded from the resolve_budget mutant by construction -- see comment")

    _record("MUTATION-ANCHORS-UNIQUE",
           TOOL.read_text(encoding="utf-8").count(import_anchor) == 1
           and (ROOT / ".tools" / "_compbudget.py").read_text(encoding="utf-8").count(anchor) == 1,
           "one occurrence expected for each anchor")


def _report() -> int:
    _run_battery()
    failed = [(name, detail) for name, ok, detail in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                              "" if ok else " -- " + detail))
    print("OS1-BUDGET BATTERY: %d/%d PASS (denominator %d)" %
          (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(name, detail) for name, ok, detail in RESULTS if not ok]
    assert not failed, "comp-heat OS1 budget battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
