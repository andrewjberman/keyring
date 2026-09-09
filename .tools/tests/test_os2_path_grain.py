#!/usr/bin/env python3
"""NFRA_OUTSET.TO-OS-s-2 battery: `comp-heat freshness <path>` answers at a PATH GRAIN --
that corner's own denominator, from a PATH-SCOPED git call, while the NO-PATH form still
scores the whole repository.

Run at both required file grains:
  python .tools/tests/test_os2_path_grain.py
  python -m pytest -q .tools/tests/test_os2_path_grain.py

WHAT WAS WRONG (the cell, PRD s.7 row OS-s-2): the engine's git calls were unscoped, so every
scoped call paid the whole-history walk and then printed the WHOLE REPO's `scanned n of N`
beside a corner's per-path rows -- two grains in one output, neither labelled. Scoping was a
wrapper-side prefix filter applied AFTER the cost had been paid.

THE ARMS, and the axis each one measures (they are deliberately not all the same instrument --
CLAUDE.md s.2: a second reading through the FIRST reading's method is repetition, not
corroboration):
  A  the CLI's own human render         -- the `denominator:` line exists and names its grain
  B  the CLI's own JSON carrier         -- scanned == total == len(paths), scoped
  C  an INDEPENDENT census (`git ls-files -- <scope>`, not the log walk the engine reads)
                                        -- the tool's denominator equals that corner's census
  D  two corners, side by side          -- the number MOVES with the path (the whole claim)
  E  the NO-PATH form                   -- still scores the whole repository (explicitly required)
  F  PARITY, scoped vs unscoped         -- the DENOMINATOR changed, the ANSWER did not (per-path
                                           band + age agree with the whole-repo run's own rows)
  G  the git argv itself, in process    -- the pathspec really reaches git, with a negative
                                           control (scope=None emits NO pathspec)
  H  RED MUTANT                         -- `_scope_pathspec()` neutered in a TEMPORARY COPY of the
                                           engine (outside the repo, via COMP_HEATMAP_DIR): the
                                           scoped call then returns THE REPO DENOMINATOR again,
                                           which is precisely the defect this cell fixed. If the
                                           mutant did not fire, arms B-D would be vacuous.

The production tool and the production engine are NEVER rewritten by this file: the mutant lives
in a `tempfile.mkdtemp()` directory outside the repository and is removed by its own `finally`.
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / ".tools" / "comp-heat"
ENGINE = ROOT / "org" / "modules" / "heatmap" / "object_freshness.py"
CORNER_A = ".tools"
CORNER_B = "org/modules/heatmap"
# The known, pre-existing engine characteristic (surprise row NFRA_OUTSET-W1-S3): a handful of
# tracked paths never appear in the `git log --name-only` walk, so the YIELD can sit just under an
# `ls-files` census. Measured 10 of 30552 repo-wide, 0 of 387 and 0 of 8 on the two corners. This
# battery therefore asserts a BOUNDED shortfall against the independent census, never bare
# equality -- and PRINTS both numbers so the shortfall is visible rather than absorbed.
CENSUS_SHORTFALL_TOLERANCE = 25

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, str(detail).replace("\n", " ")[:300]))


def _run(*args: str, timeout: int = 90, env: dict | None = None):
    e = dict(os.environ)
    if env:
        e.update(env)
    return subprocess.run([sys.executable, str(TOOL), *args], cwd=str(ROOT), text=True,
                          capture_output=True, timeout=timeout, env=e)


def _run_json(*args: str, timeout: int = 90, env: dict | None = None):
    r = _run(*args, "--json", timeout=timeout, env=env)
    try:
        return r, json.loads(r.stdout)
    except Exception:                                                      # noqa: BLE001
        return r, None


def _census(scope: str | None) -> int:
    """INDEPENDENT instrument: `git ls-files` (the index), NOT the `git log --name-only` walk the
    engine derives its own denominator from. A different plane of the same repository."""
    def n(*extra: str) -> int:
        pathspec = ["--", scope] if scope else []
        out = subprocess.run(["git", "-C", str(ROOT), "ls-files", *extra, *pathspec],
                             capture_output=True, text=True, timeout=60).stdout
        return len([x for x in out.splitlines() if x])
    return n() + n("--others", "--exclude-standard")


def _mutant_scoped_run(scope: str):
    """RED MUTANT: a TEMPORARY COPY of the heatmap engine, outside the repository, whose
    `_scope_pathspec()` always returns [] -- i.e. the scope never reaches git. comp-heat is
    pointed at it with COMP_HEATMAP_DIR (its own documented indirection), so neither
    org/modules/heatmap/ nor .tools/comp-heat is touched."""
    needle = 'return ["--", scope] if scope else []'
    src = ENGINE.read_text(encoding="utf-8")
    if src.count(needle) != 1:
        raise AssertionError("mutation anchor count != 1 for %r: %d" % (needle, src.count(needle)))
    tmp = tempfile.mkdtemp(prefix="os2-mutant-")
    try:
        for f in ("heat_map.py", "object_freshness.py"):
            shutil.copyfile(ENGINE.parent / f, Path(tmp) / f)
        (Path(tmp) / "object_freshness.py").write_text(
            src.replace(needle, "return []  # RED MUTANT: scope never reaches git", 1),
            encoding="utf-8")
        return _run_json("freshness", scope, "--budget", "90", timeout=90,
                         env={"COMP_HEATMAP_DIR": tmp})
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _run_battery() -> None:                                                # noqa: C901
    if RESULTS:
        return

    # ---- ARM A: the human render carries a labelled denominator for a named corner ----
    human = _run("freshness", CORNER_A, "--budget", "60", timeout=90)
    dline = next((ln for ln in human.stdout.splitlines()
                 if ln.strip().startswith("denominator:")), "")
    _record("A-SCOPED-HUMAN-RENDER-PRINTS-DENOMINATOR-AND-GRAIN",
            human.returncode == 0 and bool(dline) and "PATH-SCOPED to this corner" in dline
            and ("-- " + CORNER_A) in dline and "WITHIN BUDGET: scanned" in human.stdout,
            dline or human.stdout[:300] or human.stderr[:300])

    # ---- ARM B: the JSON carrier agrees with itself, at the corner's grain ----
    ra, ja = _run_json("freshness", CORNER_A, "--budget", "60", timeout=90)
    ok_b = (ra.returncode == 0 and ja is not None
            and ja.get("denominator", {}).get("grain") == "PATH-SCOPED"
            and ja["denominator"]["scanned"] == ja["denominator"]["total"]
            == ja["denominator"]["scored"] == len(ja["paths"])
            and ja["denominator"]["prefix_filter_dropped"] == 0)
    _record("B-SCOPED-JSON-SELF-CONSISTENT-AT-CORNER-GRAIN", ok_b,
            json.dumps(ja.get("denominator")) if ja else (ra.stderr[:300] or ra.stdout[:300]))

    # ---- ARM C: against an INDEPENDENT census (git ls-files, not the log walk) ----
    cen_a = _census(CORNER_A)
    tot_a = ja["denominator"]["total"] if ja else -1
    _record("C-SCOPED-DENOMINATOR-MATCHES-INDEPENDENT-CENSUS",
            ja is not None and 0 <= cen_a - tot_a <= CENSUS_SHORTFALL_TOLERANCE,
            "tool denominator=%d of %d ; independent `git ls-files -- %s` census=%d ; "
            "shortfall=%d (tolerance %d)"
            % (tot_a, tot_a, CORNER_A, cen_a, cen_a - tot_a, CENSUS_SHORTFALL_TOLERANCE))

    # ---- ARM D: the number MOVES with the path (two corners, each its own census) ----
    rb, jb = _run_json("freshness", CORNER_B, "--budget", "60", timeout=90)
    cen_b = _census(CORNER_B)
    tot_b = jb["denominator"]["total"] if jb else -1
    _record("D-DENOMINATOR-MOVES-WITH-THE-PATH",
            jb is not None and jb["denominator"]["grain"] == "PATH-SCOPED"
            and 0 <= cen_b - tot_b <= CENSUS_SHORTFALL_TOLERANCE and tot_b != tot_a,
            "%s -> %d (census %d) ; %s -> %d (census %d) ; distinct=%s"
            % (CORNER_A, tot_a, cen_a, CORNER_B, tot_b, cen_b, tot_b != tot_a))

    # ---- ARM E: the NO-PATH form STILL scores the whole repository (the required arm) ----
    rn, jn = _run_json("freshness", "--budget", "90", timeout=110)
    cen_all = _census(None)
    tot_all = jn["denominator"]["total"] if jn else -1
    _record("E-NO-PATH-FORM-STILL-SCORES-THE-WHOLE-REPO",
            jn is not None and jn.get("scope") is None
            and jn["denominator"]["grain"] == "WHOLE-ESTATE"
            and 0 <= cen_all - tot_all <= CENSUS_SHORTFALL_TOLERANCE
            and tot_all > tot_a > tot_b,
            "no-path denominator=%d (whole-repo census %d, shortfall %d) ; %s=%d ; %s=%d"
            % (tot_all, cen_all, cen_all - tot_all, CORNER_A, tot_a, CORNER_B, tot_b))

    # ---- ARM F: PARITY -- the denominator changed, the ANSWER did not ----
    # The scoped run's per-path rows must agree with the whole-repo run's own rows for the same
    # corner. The path SET is compared EXACTLY over every row (that is what a scoping regression
    # would move); band and age are compared exactly over the GIT-SOURCED rows only.
    #
    # WARN: WHY AGE IS NOT COMPARED ON MTIME-SOURCED ROWS, and why that is not a weakening.
    # This arm reads two SEPARATE comp-heat invocations seconds apart. A TRACKED file's age comes
    # from its commit timestamp and is stable between them; an UNTRACKED file's age comes from its
    # live filesystem mtime, so ANY write to the worktree between the two passes -- another seat
    # committing, or this battery's own author saving a file -- moves it and fails the arm. That
    # happened twice: once for 2.0.0_SA_COO at the OS-s-2 drain (age-diff=1, two immediate re-runs
    # both clean) and once here on 2026-09-05. A FLAKY RED IS WORSE THAN A MISSING ARM: it trains
    # every future reader to re-run until green, which is how a real regression gets waved through.
    # The property this arm exists to protect -- "the path-scoped git walk returns the same answer
    # as the unscoped one" -- lives entirely in the git-sourced rows, so restricting the AGE
    # comparison to them removes the race without giving up the discrimination. The mtime rows are
    # still compared on MEMBERSHIP (a scoping regression in the untracked leg still fails the arm)
    # and their count is PRINTED as a stated exclusion, never silently dropped.
    #
    # WARN: AND EVERY DIFFERENCE NAMES ITS MEMBERS. The earlier version printed `age-diff=1` beside an
    # empty `[]`, because the count and the list were different quantities -- a failure that could
    # not be diagnosed from its own output.
    parity_detail, ok_f = "no JSON to compare", False
    head_before = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True,
                                 capture_output=True, timeout=60).stdout.strip()
    if ja is not None and jn is not None:
        scoped = {r["path"]: r for r in ja["paths"]}
        unscoped = {r["path"]: r for r in jn["paths"]
                    if r["path"] == CORNER_A or r["path"].startswith(CORNER_A + "/")}
        shared = set(scoped) & set(unscoped)
        key_diff = sorted(set(scoped) ^ set(unscoped))
        git_rows = sorted(k for k in shared
                          if scoped[k].get("source") == "git" and unscoped[k].get("source") == "git")
        mtime_rows = sorted(shared - set(git_rows))
        band_diff = [(k, scoped[k]["band"], unscoped[k]["band"]) for k in git_rows
                     if scoped[k]["band"] != unscoped[k]["band"]]
        # WARN: THE TOLERANCE MUST EXCEED THE QUANTISATION, AND 0.01 DID NOT.
        # comp-heat publishes age_days as `round(age_days, 2)`, so the value is quantised to 0.01 d
        # steps. Two runs seconds apart can land on adjacent steps -- 141.70 and 141.71 -- whose
        # difference IS the tolerance, and float representation makes it compare as GREATER. That
        # is a boundary artifact, not a divergence, and it fired here on 2026-09-05 for
        # '.tools/deregister-all' (141.7 vs 141.71) on a GIT-SOURCED row.
        # The earlier de-flake (NFRA_OUTSET-W1-S12) removed the mtime race and its falsifier
        # exercised exactly that -- churning an UNTRACKED file's mtime -- so it could not have
        # caught this second, independent mechanism on a TRACKED row. Recorded as
        # NFRA_OUTSET-W1-S18 rather than quietly widened.
        # TWO quanta, so a real divergence (a scoping regression moves a value by DAYS or drops the
        # row from the key set entirely) still fails while an adjacent-step rounding does not.
        AGE_TOLERANCE_D = 0.02
        age_diff = [(k, scoped[k]["age_days"], unscoped[k]["age_days"]) for k in git_rows
                    if abs(scoped[k]["age_days"] - unscoped[k]["age_days"]) > AGE_TOLERANCE_D]
        ok_f = not key_diff and not band_diff and not age_diff and len(scoped) > 0
        head_after = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True,
                                    capture_output=True, timeout=60).stdout.strip()
        parity_detail = (
            "compared %d scoped vs %d unscoped-filtered rows; %d git-sourced (band+age compared) "
            "+ %d mtime-sourced (membership only -- their age is a live filesystem clock): "
            "key-diff=%d %s band-diff=%d %s age-diff(>%.2fd, 2 quanta of the tool's own 0.01d "
            "rounding)=%d %s ; HEAD %s during the arm (%s)"
            % (len(scoped), len(unscoped), len(git_rows), len(mtime_rows),
               len(key_diff), key_diff[:3],
               len(band_diff), band_diff[:3],
               AGE_TOLERANCE_D, len(age_diff), age_diff[:3],
               "held" if head_before == head_after else "MOVED",
               head_before[:10] if head_before == head_after
               else "%s -> %s" % (head_before[:10], head_after[:10])))
    _record("F-SCOPED-ANSWER-IS-PARITY-WITH-THE-UNSCOPED-ANSWER", ok_f, parity_detail)

    # ---- ARM G: the pathspec really reaches git, WITH A NEGATIVE CONTROL ----
    spec = importlib.util.spec_from_file_location("os2_engine_under_test", ENGINE)
    eng = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(eng)
    sys.path.insert(0, str(ROOT / ".tools"))
    import _compbudget                                                       # noqa: E402

    captured: list[list[str]] = []
    original = eng._git_bounded

    def _spy(root, *args, timeout=None):
        captured.append(list(args))
        return original(root, *args, timeout=timeout)

    eng._git_bounded = _spy
    try:
        eng.build_budgeted(str(ROOT), eng.HeatParams(half_life_days=30.0), time.time(),
                           _compbudget.Clock(60.0), scope=CORNER_B)
        scoped_argv = list(captured)
        captured.clear()
        eng.build_budgeted(str(ROOT), eng.HeatParams(half_life_days=30.0), time.time(),
                           _compbudget.Clock(90.0), scope=None)
        unscoped_argv = list(captured)
    finally:
        eng._git_bounded = original

    every_scoped = bool(scoped_argv) and all(av[-2:] == ["--", CORNER_B] for av in scoped_argv)
    log_full_history = any(av[0] == "log" and "--full-history" in av for av in scoped_argv)
    no_pathspec_unscoped = bool(unscoped_argv) and all("--" not in av for av in unscoped_argv)
    _record("G-GIT-ARGV-CARRIES-THE-PATHSPEC-PLUS-NEGATIVE-CONTROL",
            every_scoped and log_full_history and no_pathspec_unscoped,
            "scoped calls=%d all-pathspec=%s log--full-history=%s | NEGATIVE CONTROL unscoped "
            "calls=%d none-carry-a-pathspec=%s"
            % (len(scoped_argv), every_scoped, log_full_history, len(unscoped_argv),
               no_pathspec_unscoped))

    # ---- ARM H: RED MUTANT -- a scoped call that returns the REPO denominator ----
    rm, jm = _mutant_scoped_run(CORNER_B)
    mut_tot = jm["denominator"]["total"] if jm else -1
    mut_dropped = jm["denominator"]["prefix_filter_dropped"] if jm else -1
    _record("H-RED-MUTANT-SCOPED-CALL-RETURNS-THE-REPO-DENOMINATOR",
            jm is not None and mut_tot == tot_all and mut_tot != tot_b and mut_dropped > 0,
            "mutant scoped %s denominator=%d (production scoped=%d, production no-path=%d), "
            "wrapper prefix-filter dropped=%d -- the mutant reproduces the pre-OS-s-2 defect"
            % (CORNER_B, mut_tot, tot_b, tot_all, mut_dropped))

    _record("H2-MUTATION-ANCHOR-UNIQUE",
            ENGINE.read_text(encoding="utf-8").count(
                'return ["--", scope] if scope else []') == 1,
            "exactly one occurrence of the mutated line expected in %s" % ENGINE.name)

    # ---- ARM I: --help discloses the path grain ----
    h = _run("freshness", "--help", timeout=60)
    _record("I-HELP-DISCLOSES-THE-PATH-GRAIN",
            h.returncode == 0 and "PATH-SCOPED" in h.stdout and "denominator" in h.stdout,
            h.stdout[:300])


def _report() -> int:
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    print("OS2-PATH-GRAIN BATTERY: %d/%d PASS (denominator %d)"
          % (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    assert not failed, "comp-heat OS2 path-grain battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
