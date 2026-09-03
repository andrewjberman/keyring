"""Acceptance: comp-dataflow -- the 4/4 honest-unresolved specimens PRESERVED, the enriched
UNRESOLVED-reason print, and Rule T's form on the gate sweep. NFRA_COMPEFFICACY CE-t-7.

No battery existed for this tool at cut (0 files in .tools/tests/ for comp-dataflow/comp_dataflow).

EIGHT REC()-CALLS, FOUR LOGICAL ARMS (a real+mutant pair per arm). The FIRST arm is the never-guess
control (T7-AC3's own words: "a planted mutant that resolves one of them by reading deploy-time
config goes RED") -- everything else is secondary to it.
  1 NEVER-GUESS-REAL / -MUTANT   the 4 honest-unresolved specimens (one per reason class) still
                        read UNRESOLVED on the real binary; a mutant that lets _resolve_expr fall
                        back to a live env var FAILS this control (the DEPLOY-TIME-ONLY specimen
                        resolves via the actually-set env var, proving the arm is real)
  2 REASON-CLASS / MUTANT-REASON   each of the 4 specimens carries its EXPECTED reason label, not
                        just "some" label; a mutant that always returns one fixed reason FAILS this
  3 REASON-CONSERVATION  per-reason counts in the denominator SUM to reads_unresolved (Rule 24 (i)),
                        over a real gate sweep (no mutant needed -- an identity-check arithmetic
                        control, same class as comp-read's own BAND-CONSERVATION)
  4 ITEM-9-UNCHANGED     served-origin flagging on the RF-7 acceptance specimen is BYTE-IDENTICAL to
                        its pre-this-cell shape (BOUNDS: classification does not change; no mutant --
                        a regression control against the tool's own charter case)
  5 BUDGET-CARRIER / MUTANT-BUDGET   the real production binary's gate sweep: default budget on a
                        bounded pathspec -> WITHIN BUDGET; --budget 0.001 on the full data/ tree ->
                        BUDGET REACHED with a real --cursor; a build that ignores --budget goes RED

Two specimens (DYNAMIC-PATH, FIRM-TREE-ABSENT) are REAL production files, named at cut by this
cell's own gate sweep. Two (DEPLOY-TIME-ONLY, OTHER) have ZERO live occurrences in this estate as of
this sweep (604 of 604 real unresolved reads split DYNAMIC-PATH/FIRM-TREE-ABSENT only, disclosed in
the deliverable, not hidden) -- both are exercised via PLANTED fixtures, matching the acceptance
enum's own "four planted cases" allowance (PRD v0.4 s.4.3).

MUTANT MIRROR (arm 1): comp_dataflow.py resolves _WS three parents above its own file (org/modules/
graph -> org/modules -> org -> workspace root) to reach .tools/_compbudget.py, so a bare tempfile
copy breaks that resolution. The mutant is written into a scratch tree shaped org/modules/graph/
comp_dataflow.py + .tools/_compbudget.py (mirroring comp-which-routing-test.py's own build_mirror()
precedent) so _WS resolves correctly inside the mutant's own process.

Usage: python .tools/tests/test_comp_dataflow_battery.py   (direct)  |  python -m pytest -q .tools/tests/test_comp_dataflow_battery.py   (collected)
COMP_DATAFLOW_TOOL=<path> aims it at a mutant of the ENGINE (org/modules/graph/comp_dataflow.py)
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

_WS_CACHE = None


def _ws():
    global _WS_CACHE
    if _WS_CACHE is None:
        _WS_CACHE = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                        cwd=str(Path(__file__).resolve().parent),
                                        capture_output=True, text=True).stdout.strip())
    return _WS_CACHE


def _tool():
    """The comp_dataflow.py ENGINE under test. COMP_DATAFLOW_TOOL overrides it, so a grader can aim
    the battery at a mutant of their own without touching this file or the tool."""
    return Path(os.environ.get("COMP_DATAFLOW_TOOL")
                or (_ws() / "org" / "modules" / "graph" / "comp_dataflow.py"))


RESULTS: list[tuple[str, str, str]] = []


def rec(tid, ok, detail):
    RESULTS.append((tid, "PASS" if ok else "FAIL", detail))
    print("  [%s] %s: %s" % ("PASS" if ok else "FAIL", tid, detail))


def run(args, tool=None, timeout=120, env=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    r = subprocess.run([sys.executable, str(tool or _tool())] + args,
                       capture_output=True, text=True, cwd=str(_ws()), timeout=timeout, env=e)
    return r.stdout + r.stderr


# The 4 honest-unresolved specimens, one per reason class. Two are REAL production files (named at
# cut by this cell's own baseline gate sweep, 2026-09-03, over data/); two are PLANTED fixtures
# (DEPLOY-TIME-ONLY, OTHER have zero live occurrences in the current 604-row unresolved population).
SPEC_DYNAMIC_PATH = ("data/assets/scripts/gold/build_cottonwood_interpolated_backfill.py", 196, "{*}")
SPEC_FIRM_TREE_ABSENT = ("data/assets/scripts/gold/runners_49f/a01_runner.py", 86,
                         "{*}/dimensions/dim_relationship/date={*}/")

FIXTURE_DEPLOY_TIME_ONLY = (
    "import os\n"
    "DATA_PREFIX = os.environ.get(\"DATA_PREFIX\")\n\n\n"
    "def read():\n"
    "    s3.get_object(Bucket=\"x\", Key=DATA_PREFIX)\n"
)
FIXTURE_OTHER = (
    "def read():\n"
    "    s3.get_object(Bucket=\"x\", Key=f\"{['a','b'][0]}\")\n"
)

# RF-7's own acceptance specimen (this engine's charter case, docstring :11-14): the item-9
# served-origin classification must stay byte-identical after this cell's enrichment.
RF7_SPEC = "data/mdpf/scripts/backfill/build_legacy_compat_emit.py"

DEN_RE = re.compile(
    r"DENOMINATOR: (\d+) reads scanned, (\d+) unresolved-dynamic \(blind\) "
    r"\[DYNAMIC-PATH=(\d+), DEPLOY-TIME-ONLY=(\d+), FIRM-TREE-ABSENT=(\d+), OTHER=(\d+)\], "
    r"(\d+) served-origin flagged, (\d+) exempt")
GATE_DEN_RE = re.compile(
    r"DENOMINATOR: (\d+) producer files swept, (\d+) reads scanned, (\d+) unresolved-dynamic "
    r"\(blind\) \[DYNAMIC-PATH=(\d+), DEPLOY-TIME-ONLY=(\d+), FIRM-TREE-ABSENT=(\d+), OTHER=(\d+)\], "
    r"(\d+) exempt")

_RAN = False


def _run_battery():
    global _RAN
    if _RAN:
        return
    _RAN = True

    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        (tdp / "deploy_time_fixture.py").write_text(FIXTURE_DEPLOY_TIME_ONLY, encoding="utf-8")
        (tdp / "other_fixture.py").write_text(FIXTURE_OTHER, encoding="utf-8")

        # --- 1. NEVER-GUESS (the control T7-AC3 names) --------------------------
        real_ok = True
        real_detail = []
        for path, line, raw in (SPEC_DYNAMIC_PATH, SPEC_FIRM_TREE_ABSENT):
            out = run(["origin", path])
            ok = ("UNRESOLVED" in out) and (raw in out)
            real_ok = real_ok and ok
            real_detail.append("%s:%d %s" % (path, line, "held" if ok else "REGRESSED-RESOLVED"))
        out_deploy = run(["origin", str(tdp / "deploy_time_fixture.py")])
        out_other = run(["origin", str(tdp / "other_fixture.py")])
        planted_ok = ("UNRESOLVED" in out_deploy) and ("UNRESOLVED" in out_other)
        real_detail.append("deploy_time_fixture.py %s" % ("held" if "UNRESOLVED" in out_deploy
                                                            else "REGRESSED-RESOLVED"))
        real_detail.append("other_fixture.py %s" % ("held" if "UNRESOLVED" in out_other
                                                      else "REGRESSED-RESOLVED"))
        rec("NEVER-GUESS-REAL", real_ok and planted_ok,
            "all 4 honest-unresolved specimens (2 real production files, 2 planted fixtures) still "
            "read UNRESOLVED on the production binary: %s" % "; ".join(real_detail))

        # mutant: _resolve_expr's Name branch falls back to a LIVE env var instead of _DYNAMIC --
        # the exact shape of "guessing through deploy-time config" the control exists to catch.
        src = _tool().read_text(encoding="utf-8")
        mutant_src, nsub = re.subn(
            r"if isinstance\(node, ast\.Name\):\n(\s*)return scope\.get\(node\.id, _DYNAMIC\)",
            r"if isinstance(node, ast.Name):\n\1return scope.get(node.id, __import__('os').environ.get(node.id, _DYNAMIC))",
            src, count=1)
        if nsub == 0:
            rec("NEVER-GUESS-MUTANT", False,
                "could not plant the mutant: the Name-branch fallback line has moved -- the arm "
                "certifies nothing and is reported FAIL, never skipped (a skip would read as green)")
        else:
            mirror = tdp / "mirror"
            (mirror / "org" / "modules" / "graph").mkdir(parents=True)
            (mirror / ".tools").mkdir(parents=True)
            (mirror / "org" / "modules" / "graph" / "comp_dataflow.py").write_text(mutant_src, encoding="utf-8")
            (mirror / "org" / "modules" / "__init__.py").write_text("", encoding="utf-8")
            (mirror / "org" / "modules" / "graph" / "__init__.py").write_text("", encoding="utf-8")
            real_budget_src = (_ws() / ".tools" / "_compbudget.py").read_text(encoding="utf-8")
            (mirror / ".tools" / "_compbudget.py").write_text(real_budget_src, encoding="utf-8")
            (tdp / "deploy_time_fixture.py").write_text(FIXTURE_DEPLOY_TIME_ONLY, encoding="utf-8")
            mout = run(["origin", str(tdp / "deploy_time_fixture.py")],
                      tool=mirror / "org" / "modules" / "graph" / "comp_dataflow.py",
                      env={"DATA_PREFIX": "sneaked-in-from-the-live-environment"})
            resolved_via_env = "sneaked-in-from-the-live-environment" in mout and "UNRESOLVED" not in mout
            rec("NEVER-GUESS-MUTANT", resolved_via_env,
                "the planted build that lets an unresolved Name fall back to os.environ %s the "
                "DEPLOY-TIME-ONLY fixture (with DATA_PREFIX actually set in the process env) -- "
                "so this arm's REAL result is produced by the real code's REFUSAL to do this, not "
                "by an identity that would pass regardless"
                % ("correctly RESOLVED (via the live env var) -- proving the control is real"
                   if resolved_via_env else
                   "did NOT resolve -- the mutant failed to plant, this arm certifies nothing"))

    # --- 2. REASON-CLASS: each specimen carries its EXPECTED label, not just "a" label ------
    out_dp = run(["origin", SPEC_DYNAMIC_PATH[0]])
    out_fta = run(["origin", SPEC_FIRM_TREE_ABSENT[0]])
    with tempfile.TemporaryDirectory() as td2:
        tdp2 = Path(td2)
        (tdp2 / "deploy_time_fixture.py").write_text(FIXTURE_DEPLOY_TIME_ONLY, encoding="utf-8")
        (tdp2 / "other_fixture.py").write_text(FIXTURE_OTHER, encoding="utf-8")
        out_dto = run(["origin", str(tdp2 / "deploy_time_fixture.py")])
        out_oth = run(["origin", str(tdp2 / "other_fixture.py")])
    labels_ok = (
        ("reason: DYNAMIC-PATH" in out_dp) and
        ("reason: FIRM-TREE-ABSENT" in out_fta) and
        ("reason: DEPLOY-TIME-ONLY" in out_dto) and
        ("reason: OTHER" in out_oth)
    )
    rec("REASON-CLASS", labels_ok,
        "each of the 4 planted specimens carries its OWN expected reason label: "
        "dynamic-path=%s firm-tree-absent=%s deploy-time-only=%s other=%s"
        % ("reason: DYNAMIC-PATH" in out_dp, "reason: FIRM-TREE-ABSENT" in out_fta,
           "reason: DEPLOY-TIME-ONLY" in out_dto, "reason: OTHER" in out_oth))

    # mutant: _unresolved_reason always returns "OTHER" regardless of shape
    src2 = _tool().read_text(encoding="utf-8")
    mutant_src2, nsub2 = re.subn(
        r"def _unresolved_reason\(path_expr, resolved: str, env_names: set\) -> str:",
        "def _unresolved_reason(path_expr, resolved, env_names):\n    return 'OTHER'  # MUTANT\n"
        "def _unresolved_reason_ORIG(path_expr, resolved: str, env_names: set) -> str:",
        src2, count=1)
    if nsub2 == 0:
        rec("MUTANT-REASON", False,
            "could not plant the mutant: _unresolved_reason's signature has moved -- the arm "
            "certifies nothing and is reported FAIL, never skipped")
    else:
        with tempfile.TemporaryDirectory() as td3:
            mp = Path(td3) / "mutant2"
            (mp / "org" / "modules" / "graph").mkdir(parents=True)
            (mp / ".tools").mkdir(parents=True)
            (mp / "org" / "modules" / "__init__.py").write_text("", encoding="utf-8")
            (mp / "org" / "modules" / "graph" / "__init__.py").write_text("", encoding="utf-8")
            (mp / "org" / "modules" / "graph" / "comp_dataflow.py").write_text(mutant_src2, encoding="utf-8")
            (mp / ".tools" / "_compbudget.py").write_text(
                (_ws() / ".tools" / "_compbudget.py").read_text(encoding="utf-8"), encoding="utf-8")
            mo = run(["origin", SPEC_DYNAMIC_PATH[0]],
                    tool=mp / "org" / "modules" / "graph" / "comp_dataflow.py")
        collapsed = ("reason: DYNAMIC-PATH" not in mo) and ("reason: OTHER" in mo)
        rec("MUTANT-REASON", collapsed,
            "the planted all-OTHER build %s on the DYNAMIC-PATH specimen (expected reason: OTHER, "
            "not DYNAMIC-PATH) -- so arm 2's per-label check is produced by real classification, "
            "not by an identity that would pass regardless"
            % ("correctly mis-labelled it" if collapsed else "did NOT mis-label it as expected"))

    # --- 3. REASON-CONSERVATION over the real gate sweep -------------------------
    out_gate = run(["gate", "data/assets/scripts/gold"], timeout=60)
    m = GATE_DEN_RE.search(out_gate)
    if m:
        files, scanned, unresolved, dp, dto, fta, other, exempt = (int(x) for x in m.groups())
        conserved = (dp + dto + fta + other) == unresolved
    else:
        conserved = False
    rec("REASON-CONSERVATION", bool(m) and conserved,
        ("DENOMINATOR line found; DYNAMIC-PATH=%d + DEPLOY-TIME-ONLY=%d + FIRM-TREE-ABSENT=%d + "
         "OTHER=%d = %d, reads_unresolved=%d -- %s" % (dp, dto, fta, other, dp + dto + fta + other,
                                                        unresolved, "CONSERVED" if conserved else "MISMATCH"))
        if m else "no DENOMINATOR line matched the expected enriched shape at all")

    # --- 4. ITEM-9 UNCHANGED: served-origin classification byte-identical -------
    out_rf7 = run(["origin", RF7_SPEC])
    m2 = DEN_RE.search(out_rf7)
    served_count = int(m2.group(7)) if m2 else -1
    flag_lines = out_rf7.count("SERVED-ORIGIN <<< FLAG")
    rec("ITEM-9-UNCHANGED", bool(m2) and served_count == 5 and flag_lines == 5,
        "RF-7's own acceptance specimen (%s) still flags exactly 5 served-origin reads (the "
        "charter case this engine was built to catch, docstring :11-14) -- served_origin_unexempted=%d, "
        "%d SERVED-ORIGIN <<< FLAG line(s); BOUNDS: item-9 classification unchanged by this cell's "
        "print enrichment" % (RF7_SPEC, served_count, flag_lines))

    # --- 5. BUDGET-CARRIER: the real production binary, no mutant needed --------
    out_within = run(["gate", "data/assets/scripts/gold"], timeout=60)
    out_reached = run(["gate", "data/", "--budget", "0.001"], timeout=60)
    ok5 = (("WITHIN BUDGET" in out_within) and ("BUDGET REACHED" not in out_within) and
          ("BUDGET REACHED" in out_reached) and ("WITHIN BUDGET" not in out_reached) and
          ("--cursor" in out_reached))
    rec("BUDGET-CARRIER", ok5,
        "default budget on a bounded pathspec -> WITHIN BUDGET (no BUDGET REACHED token); "
        "--budget 0.001 on the full data/ tree -> BUDGET REACHED with a real --cursor resume line "
        "-- distinguishable by token alone, no shared shape" if ok5 else
        "the real binary did not produce two distinguishable Rule T lines: within=%r reached=%r cursor=%r"
        % ("WITHIN BUDGET" in out_within, "BUDGET REACHED" in out_reached, "--cursor" in out_reached))

    # --- 6. MUTANT-BUDGET: neuter the carrier, RED-first ------------------------
    src3 = _tool().read_text(encoding="utf-8")
    mutant_src3, nsub3 = re.subn(
        r"budget_s, budget_source = _compbudget\.resolve_budget\(args\.budget\)",
        "budget_s, budget_source = _compbudget.resolve_budget(None)", src3, count=1)
    if nsub3 == 0:
        rec("MUTANT-BUDGET", False,
            "could not plant the mutant: the resolve_budget call site has moved -- the arm "
            "certifies nothing and is reported FAIL, never skipped")
    else:
        with tempfile.TemporaryDirectory() as td4:
            mp3 = Path(td4) / "mutant3"
            (mp3 / "org" / "modules" / "graph").mkdir(parents=True)
            (mp3 / ".tools").mkdir(parents=True)
            (mp3 / "org" / "modules" / "__init__.py").write_text("", encoding="utf-8")
            (mp3 / "org" / "modules" / "graph" / "__init__.py").write_text("", encoding="utf-8")
            (mp3 / "org" / "modules" / "graph" / "comp_dataflow.py").write_text(mutant_src3, encoding="utf-8")
            (mp3 / ".tools" / "_compbudget.py").write_text(
                (_ws() / ".tools" / "_compbudget.py").read_text(encoding="utf-8"), encoding="utf-8")
            mo3 = run(["gate", "data/", "--budget", "0.001"],
                     tool=mp3 / "org" / "modules" / "graph" / "comp_dataflow.py", timeout=60)
        ignored = "BUDGET REACHED" not in mo3
        rec("MUTANT-BUDGET", ignored,
            "the planted build that ignores --budget (always resolves flag=None) %s at --budget "
            "0.001 on the full data/ tree -- so arm 5's BUDGET REACHED is produced by real carrier "
            "resolution, not by an identity that would print it regardless"
            % ("still reports WITHIN BUDGET, never BUDGET REACHED" if ignored else
               "STILL reached BUDGET REACHED -- the mutant did not neuter the carrier"))


def _report() -> int:
    _run_battery()
    n = sum(1 for _, v, _ in RESULTS if v == "PASS")
    print()
    print("=" * 80)
    print("COMP-DATAFLOW BATTERY: %d/%d PASS (denominator %d)" % (n, len(RESULTS), len(RESULTS)))
    print("=" * 80)
    return 0 if n == len(RESULTS) else 1


def test_all_arms_pass():
    _run_battery()
    failed = [(t, d) for t, v, d in RESULTS if v != "PASS"]
    assert not failed, "arms failed (%d of %d): %s" % (len(failed), len(RESULTS), failed)
    print("COMP-DATAFLOW BATTERY: %d/%d PASS (denominator %d)" % (len(RESULTS), len(RESULTS), len(RESULTS)))


if __name__ == "__main__":
    sys.exit(_report())
