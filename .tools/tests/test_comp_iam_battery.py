"""Battery for org/modules/graph/iam_cli.py (comp-iam) -- NFRA_COMPEFFICACY TO-CE-T-8, T8-AC3/AC5.

WHAT THIS FILE ADDS (on top of iam_cli.py's own OWN offline `_simulate_self_test`, which this cell
extended in-place with case 6, the Rule T DEFERRED bucket -- ZERO AWS calls, stub client):

  T8-AC3 (effective-deny THREE-STATE, machine-rejectable): `_simulate_self_test` grades its five
  original cases by RETURN CODE only. That is provably NOT the same claim as "the printed STATE:
  token is correct" -- a regression that flips a STATE line's TEXT while leaving every rc unchanged
  would sail through `_simulate_self_test` reporting "OK: all simulate self-test cases pass" and
  rc=0, because nothing in that suite reads its own stdout. ARM 1 closes that gap from OUTSIDE the
  self-test, by running `simulate-self-test` as a real subprocess and taking a CENSUS of the
  `STATE: <TOKEN>` lines it prints (all three tokens are enumerated, all six cases contribute):
  case 1 (multi-ARN refusal) prints none (refused before any decision); case 2 (control-proven
  deny) -> DENIED; cases 3, 4, 6 (missing-context / control-also-denies / DEFERRED -- the "no
  parsed deny is never allowed" family) -> NOT-DECIDABLE; case 5 (real allow) -> ALLOWED. Expected
  census: {ALLOWED: 1, DENIED: 1, NOT-DECIDABLE: 3}. ARM 2 is the RED-FIRST control proving ARM 1
  can fail: a planted mutant flips case 3's line from `STATE: NOT-DECIDABLE` to `STATE: ALLOWED`
  (the exact false-deny-mode-2 shape CLAUDE.md 22a describes, now misreported as a GRANT) while
  leaving `return 2` untouched -- so the self-test's OWN internal rc-based checks still report
  "OK: all simulate self-test cases pass" on the mutant. ARM 1's census predicate must (and does)
  disagree with that verdict: it is the only one of the two that reads the token, not the rc.

  T8-AC5 (Rule T's carrier wired on every corpus-width sweep and AWS-plane call, with a control
  that can fail): resource-sweep and attach-census both call the real, unmocked `_build()` (a
  Terraform parse over this repo -- no AWS, no network, ~8-10s per call on this box) so these arms
  are real subprocess runs of the production tool, not stubs. ARM 3 confirms a generous/default
  budget completes the full lambda population (`WITHIN BUDGET: scanned N of N lambda`). ARM 4
  confirms `--resume-after <first-lambda-by-sort-order>` reduces the reported denominator by
  EXACTLY ONE relative to the unfiltered run (the ground-truth N and the resume point are both
  taken from one direct, in-process `_build()` call -- never hard-coded, since the estate's lambda
  population changes over time; hard-coding a name here would be exactly the "sprint display dates
  are derived, never typed" mistake one surface over). ARM 5 confirms a budget too small to
  complete even one lambda prints `BUDGET REACHED ... NO CURSOR YET` (the genuinely-indivisible-so-
  far case) rather than a silent full scan. ARM 6/7 cover attach-census's DISCLOSED NON-APPLICATION
  half (Rule T PRD s.4.4): a call with no internal resumption point states honestly that it ran to
  completion past budget rather than faking a partial abort. ARM 8 is the RED-FIRST control for
  ARM 5: a mutant that neuters resource-sweep's per-iteration `clock.remaining()` check (the exact
  "a budget that's silently ignored" defect) must make the BUDGET-REACHED predicate fail against a
  tiny budget it used to catch cleanly.

MUTANT FIXTURE PLACEMENT (the comp-find battery's fixture-defect-2 lesson, one layer stricter
here): iam_cli.py computes `_WORKSPACE = Path(__file__).resolve().parent.parent.parent.parent`
(3 parents up from its OWN directory) and inserts THAT into sys.path -- a mutant copy dropped in
a temp dir at the wrong nesting depth silently resolves the WRONG workspace root and either
crashes on import or (worse) silently reads a different repo's Terraform tree. Every mutant here
is therefore written BESIDE the real file, inside org/modules/graph/ itself, as a disposable
`_tmp_iam_mutant_<kind>_<pid>.py`, removed in a `finally`.

SKIP (recorded, not silent) if `_build()` cannot run here at all (e.g. the Terraform tree is
absent on this box) -- a fixture that cannot represent the population cannot score sweep/census
arms; the STATE-token arms (1, 2) do not depend on `_build()` and always run.

Run: python .tools/tests/test_comp_iam_battery.py    |    pytest -q .tools/tests/test_comp_iam_battery.py
"""
from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

RESULTS: list[tuple[str, bool | None, str]] = []
_WS_CACHE = None
_RAN = False
_IAM_MOD = None

WITHIN_RE = re.compile(r"WITHIN BUDGET: scanned (\d+) of (\d+) lambda")
STATE_TOKENS = ("ALLOWED", "DENIED", "NOT-DECIDABLE")
EXPECTED_STATE_COUNTS = {"ALLOWED": 1, "DENIED": 1, "NOT-DECIDABLE": 3}


def _ws() -> Path:
    global _WS_CACHE
    if _WS_CACHE is None:
        _WS_CACHE = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                        cwd=str(Path(__file__).resolve().parent),
                                        capture_output=True, text=True).stdout.strip())
    return _WS_CACHE


def _tool() -> Path:
    return _ws() / "org" / "modules" / "graph" / "iam_cli.py"


def rec(tid: str, ok: bool | None, detail: str = "") -> None:
    RESULTS.append((tid, ok, detail))


def run(args: list[str], tool: Path | None = None, timeout: int = 60) -> tuple[int, str]:
    r = subprocess.run([sys.executable, str(tool or _tool())] + args,
                       capture_output=True, text=True, timeout=timeout, cwd=str(_ws()))
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def _state_token_counts(out: str) -> dict:
    return {tok: len(re.findall(r"STATE: %s\b" % re.escape(tok), out)) for tok in STATE_TOKENS}


def _iam_module():
    """Direct in-process import of the real file (by path, so __file__/_WORKSPACE resolve
    correctly) -- used ONLY to derive ground-truth (the sorted lambda population) for ARM 4,
    never to bypass the subprocess arms' external-observer posture."""
    global _IAM_MOD
    if _IAM_MOD is None:
        # iam_cli.py imports sibling modules (comp_iam_census et al.) assuming its OWN directory is
        # on sys.path -- true automatically under `python iam_cli.py ...` (script-dir-on-path), NOT
        # true under spec_from_file_location/exec_module. Fixture defect found on first run here:
        # exec_module raised ModuleNotFoundError for a sibling that every subprocess arm resolves
        # fine. Mirror the script-run behaviour explicitly rather than silently reading it as
        # "not exercisable" (which this fixture bug did on its first version).
        sys.path.insert(0, str(_tool().parent))
        spec = importlib.util.spec_from_file_location("iam_cli_battery_import", str(_tool()))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _IAM_MOD = mod
    return _IAM_MOD


def _build_exercisable() -> tuple[bool, str]:
    try:
        _iam_module()._build()
        return True, ""
    except Exception as exc:  # pragma: no cover -- environment-dependent
        return False, "%s: %s" % (type(exc).__name__, exc)


def _mutant_path(kind: str) -> Path:
    return _tool().parent / ("_tmp_iam_mutant_%s_%d.py" % (kind, os.getpid()))


def _write_mutant(kind: str, needle: str, replacement: str) -> Path:
    src = _tool().read_text(encoding="utf-8")
    n = src.count(needle)
    assert n == 1, ("fixture assumption broken for mutant %r -- iam_cli.py's source no longer "
                     "contains the targeted block exactly once (found %d)" % (kind, n))
    p = _mutant_path(kind)
    p.write_text(src.replace(needle, replacement, 1), encoding="utf-8")
    return p


def _run_battery() -> None:
    global _RAN
    if _RAN:
        return
    _RAN = True

    # ---------------- ARM 1: T8-AC3 STATE-token census (real code) ----------------
    rc, out = run(["simulate-self-test"])
    counts = _state_token_counts(out)
    rec("IAM-AC3-STATE-TOKEN-CENSUS", rc == 0 and counts == EXPECTED_STATE_COUNTS,
        "rc=%d counts=%r expected=%r" % (rc, counts, EXPECTED_STATE_COUNTS))

    # ---------------- ARM 2 (red-first): mutant flips false-deny-mode-2 to ALLOWED ----------------
    needle = (
        '        for k in t_missing:\n'
        '            print(f"    --context {k}=<type>:<value>")\n'
        '        print(f"STATE: {STATE_NOT_DECIDABLE}")\n'
        '        return 2\n'
    )
    replacement = (
        '        for k in t_missing:\n'
        '            print(f"    --context {k}=<type>:<value>")\n'
        '        print(f"STATE: {STATE_ALLOWED}")\n'  # MUTANT: false-deny-mode-2 now misreads as a grant
        '        return 2\n'
    )
    mutant1 = None
    try:
        mutant1 = _write_mutant("state_flip", needle, replacement)
        mrc, mout = run(["simulate-self-test"], tool=mutant1)
        mutant_internal_still_green = "OK: all simulate self-test cases pass" in mout and mrc == 0
        mutant_counts = _state_token_counts(mout)
        arm2_ok = mutant_internal_still_green and mutant_counts != EXPECTED_STATE_COUNTS
        rec("IAM-AC3-MUTANT-FALSE-ALLOW-DETECTED", arm2_ok,
            "mutant self-test internal verdict green=%s (proves rc-only grading is insufficient); "
            "census=%r (ARM 1's predicate correctly disagrees)" % (mutant_internal_still_green, mutant_counts))
    finally:
        if mutant1 is not None and mutant1.exists():
            mutant1.unlink()

    # ---------------- resource-sweep / attach-census: needs a real _build() ----------------
    buildable, why = _build_exercisable()
    if not buildable:
        skip = "SKIP: org/modules/graph iam _build() not exercisable here (%s)" % why
        for tid in ("IAM-AC5-SWEEP-WITHIN-BUDGET", "IAM-AC5-SWEEP-RESUME-AFTER",
                    "IAM-AC5-SWEEP-BUDGET-REACHED-NO-CURSOR", "IAM-AC5-ATTACH-CENSUS-WITHIN-BUDGET",
                    "IAM-AC5-ATTACH-CENSUS-DISCLOSED-NONAPPLICATION",
                    "IAM-AC5-MUTANT-BUDGET-IGNORED-DETECTED"):
            rec(tid, None, skip)
        return

    mod = _iam_module()
    profiles, _roles, _ = mod._build()
    lambdas = sorted((p for p in profiles if p.service_type == 'lambda'), key=lambda p: p.name)
    total_n = len(lambdas)
    first_name = lambdas[0].name if lambdas else None

    # ---------------- ARM 3: default/generous budget completes the full population ----------------
    rc, out = run(["resource-sweep", "--budget", "0"])
    m = WITHIN_RE.search(out)
    arm3_ok = bool(m) and m.group(1) == m.group(2) and int(m.group(1)) == total_n
    rec("IAM-AC5-SWEEP-WITHIN-BUDGET", arm3_ok,
        "match=%r total_n(direct _build)=%d" % (m.groups() if m else None, total_n))

    # ---------------- ARM 4: --resume-after reduces the denominator by exactly one ----------------
    if first_name is None:
        rec("IAM-AC5-SWEEP-RESUME-AFTER", None, "SKIP: zero lambdas with a mapped role on this box")
    else:
        rc, out = run(["resource-sweep", "--budget", "0", "--resume-after", first_name])
        m2 = WITHIN_RE.search(out)
        arm4_ok = bool(m2) and m2.group(1) == m2.group(2) and int(m2.group(1)) == total_n - 1
        rec("IAM-AC5-SWEEP-RESUME-AFTER", arm4_ok,
            "resume_after=%r match=%r expected=%d" % (first_name, m2.groups() if m2 else None, total_n - 1))

    # ---------------- ARM 5: a budget too small for even one lambda -> NO CURSOR YET ----------------
    rc, out = run(["resource-sweep", "--budget", "0.00001"])
    arm5_ok = "BUDGET REACHED" in out and "NO CURSOR YET" in out and "WITHIN BUDGET" not in out
    rec("IAM-AC5-SWEEP-BUDGET-REACHED-NO-CURSOR", arm5_ok, out[:300])

    # ---------------- ARM 6: attach-census, generous budget -> WITHIN BUDGET ----------------
    rc, out = run(["attach-census", "--budget", "0"])
    arm6_ok = "WITHIN BUDGET: scanned 1 of 1 build_pass" in out
    rec("IAM-AC5-ATTACH-CENSUS-WITHIN-BUDGET", arm6_ok, out[:300])

    # ---------------- ARM 7: attach-census, tiny budget -> honest disclosed non-application ----------------
    rc, out = run(["attach-census", "--budget", "0.00001"])
    arm7_ok = ("NOT WITHIN BUDGET" in out and "RAN TO COMPLETION" in out
               and "Disclosed non-application" in out)
    rec("IAM-AC5-ATTACH-CENSUS-DISCLOSED-NONAPPLICATION", arm7_ok, out[:300])

    # ---------------- ARM 8 (red-first): mutant neuters the per-iteration budget check ----------------
    needle2 = (
        "    for _idx, p in enumerate(lambdas):\n"
        "        remaining = clock.remaining()\n"
        "        if remaining is not None and remaining <= 0:\n"
        "            budget_exhausted_at = _idx\n"
        "            break\n"
    )
    replacement2 = (
        "    for _idx, p in enumerate(lambdas):\n"
        "        remaining = clock.remaining()\n"
        "        if False and remaining is not None and remaining <= 0:\n"  # MUTANT: budget check disabled
        "            budget_exhausted_at = _idx\n"
        "            break\n"
    )
    mutant2 = None
    try:
        mutant2 = _write_mutant("budget_ignored", needle2, replacement2)
        mrc, mout = run(["resource-sweep", "--budget", "0.00001"], tool=mutant2)
        mutant_ignores_budget = "BUDGET REACHED" not in mout and "WITHIN BUDGET" in mout
        rec("IAM-AC5-MUTANT-BUDGET-IGNORED-DETECTED", mutant_ignores_budget,
            "mutant output under a 0.00001s budget still says WITHIN BUDGET (silently ignored the "
            "ceiling) -- ARM 5's predicate correctly fails against this mutant: %r" % mout[:300])
    finally:
        if mutant2 is not None and mutant2.exists():
            mutant2.unlink()


def _report() -> int:
    _run_battery()
    fails = [r for r in RESULTS if r[1] is False]
    for tid, ok, detail in RESULTS:
        label = "SKIP" if ok is None else ("PASS" if ok else "FAIL")
        print("  [%s] %s%s" % (label, tid, "" if ok or ok is None else "  -- " + detail[:200]))
    n_scored = len([r for r in RESULTS if r[1] is not None])
    n_pass = n_scored - len(fails)
    print("COMP-IAM BATTERY: %d/%d PASS (denominator %d, %d SKIP)"
          % (n_pass, n_scored, len(RESULTS), len(RESULTS) - n_scored))
    return 1 if fails else 0


def test_all_arms_pass():
    """pytest entry. Fails on any FAIL row; the denominator is len(RESULTS)."""
    _run_battery()
    fails = [(t, d) for t, ok, d in RESULTS if ok is False]
    assert not fails, "comp-iam battery arms failed (%d of %d): %r" % (len(fails), len(RESULTS), fails)


if __name__ == "__main__":
    sys.exit(_report())
