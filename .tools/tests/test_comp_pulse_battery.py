"""Direct + pytest battery for comp-pulse (NFRA_COMPEFFICACY T18).

Every arm invokes the production engine.  The absent-map arm temporarily moves
the real map aside, as the reflex sees it in production; the engine must say
PARTIAL_OR_BLIND and return its non-clean rc rather than rebuild or print CLEAN.
Each output contract has a sibling production-mutant control: a copied engine
runs from its real sibling directory and loses the asserted token.  A crash is
never scored as a red control.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path


WS = Path(__file__).resolve().parents[2]
ENGINE = WS / "org" / "modules" / "graph" / "comp_pulse.py"
RISK = ENGINE.parent / "nerves-risk-edges.json"
RESULTS: list[tuple[str, bool, str]] = []
_RAN = False


def _run(args: list[str], engine: Path = ENGINE) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, str(engine), *args], cwd=WS,
                          capture_output=True, text=True, timeout=60)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def _record(arm: str, ok: bool, detail: str) -> None:
    RESULTS.append((arm, bool(ok), detail))


@contextmanager
def _map_moved_aside():
    """The real-binary control.  Restore atomically even if an assertion fails."""
    if not RISK.is_file():
        raise RuntimeError("battery precondition failed: danger map is absent before the control")
    parked = RISK.with_name(".%s.t18-battery-%d" % (RISK.name, os.getpid()))
    if parked.exists():
        raise RuntimeError("battery parking path already exists: %s" % parked)
    os.replace(RISK, parked)
    try:
        yield
    finally:
        if parked.exists():
            os.replace(parked, RISK)


def _mutant(marker: str, replacement: str) -> Path:
    source = ENGINE.read_text(encoding="utf-8")
    if marker not in source:
        raise RuntimeError("mutation anchor absent: %s" % marker)
    path = ENGINE.with_name(".mutant-comp-pulse-t18-%d.py" % os.getpid())
    path.write_text(source.replace(marker, replacement), encoding="utf-8")
    return path


def _red_control(arm: str, marker: str, args: list[str], must_lack: str,
                 map_absent: bool = False) -> None:
    mutant = _mutant(marker, "MUTATED_STATE_TOKEN")
    try:
        if map_absent:
            with _map_moved_aside():
                rc, out = _run(args, mutant)
        else:
            rc, out = _run(args, mutant)
        # The engine must execute with its normal rc; only then does a missing
        # marker prove that the paired positive arm is capable of going red.
        _record(arm, rc in (0, 2) and must_lack not in out,
                "rc=%d marker-present=%s" % (rc, must_lack in out))
    finally:
        mutant.unlink(missing_ok=True)


def _run_battery() -> None:
    global _RAN
    if _RAN:
        return
    _RAN = True
    with tempfile.TemporaryDirectory() as work:
        present = Path(work) / "present.py"
        present.write_text("# T18 clean subject\n", encoding="utf-8")
        missing = Path(work) / "missing.py"

        # A clean existing subject is a measured zero, never a default clean.
        rc, out = _run(["diff", str(present)])
        _record("A1-PRESENT-WITH-ZERO", rc == 0 and "ANSWER STATE: PRESENT_WITH_ZERO_RESULTS" in out
                and "REFLEX CLEAN" in out, "rc=%d" % rc)
        _red_control("A1-MUTANT-RED", "ANSWER STATE: PRESENT_WITH_ZERO_RESULTS",
                     ["diff", str(present)], "ANSWER STATE: PRESENT_WITH_ZERO_RESULTS")

        # A nonexistent supplied subject must not be folded into measured zero.
        rc, out = _run(["diff", str(missing)])
        _record("A2-SUBJECT-ABSENT", rc == 2 and "ANSWER STATE: SUBJECT_ABSENT_FROM_CORPUS" in out,
                "rc=%d" % rc)
        _red_control("A2-MUTANT-RED", "SUBJECT_ABSENT_FROM_CORPUS",
                     ["diff", str(missing)], "ANSWER STATE: SUBJECT_ABSENT_FROM_CORPUS")

        # This is the real-binary four-case control: map moved aside, no rebuild,
        # no REFLEX CLEAN, and the non-clean verdict-bearing rc.
        with _map_moved_aside():
            rc, out = _run(["diff", str(present)])
        _record("A3-ABSENT-MAP-PARTIAL", rc == 2 and "ANSWER STATE: PARTIAL_OR_BLIND" in out
                and "NOT-DECIDABLE" in out and "REFLEX CLEAN" not in out, "rc=%d" % rc)
        _red_control("A3-MUTANT-RED", "ANSWER STATE: PARTIAL_OR_BLIND",
                     ["diff", str(present)], "ANSWER STATE: PARTIAL_OR_BLIND", map_absent=True)

        # An explicit no-population mode never inspects another seat's staged
        # work, so this control remains valid in a shared index.
        rc, out = _run(["diff", "--no-population"])
        _record("A4-NOT-APPLICABLE", rc == 0 and "ANSWER STATE: NOT_APPLICABLE" in out,
                "rc=%d" % rc)
        _red_control("A4-MUTANT-RED", "NOT_APPLICABLE", ["diff", "--no-population"],
                     "ANSWER STATE: NOT_APPLICABLE")

        # A tiny real ceiling reaches before a telemetry row, prints Rule T's
        # exact carrier and cursor, and never reports a completed pulse.
        rc, out = _run(["--days", "7", "--budget", "0.000001"])
        _record("B1-PULSE-BUDGET-REACHED", rc == 0 and "BUDGET REACHED:" in out
                and "ANSWER STATE: PARTIAL_OR_BLIND" in out and "NOT-DECIDABLE" in out,
                "rc=%d" % rc)
        _red_control("B1-MUTANT-RED", "ANSWER STATE: PARTIAL_OR_BLIND",
                     ["--days", "7", "--budget", "0.000001"],
                     "ANSWER STATE: PARTIAL_OR_BLIND")

        # `diff` is verdict-bearing: expiry may not return its clean rc 0 or
        # alarm rc 1.  Its distinct rc 2 carries the partial/blind state.
        rc, out = _run(["diff", str(present), "--budget", "0.000001"])
        _record("B2-DIFF-BUDGET-NONCLEAN", rc == 2 and "BUDGET REACHED:" in out
                and "NOT-DECIDABLE" in out and "REFLEX CLEAN" not in out, "rc=%d" % rc)
        _red_control("B2-MUTANT-RED", "NOT-DECIDABLE",
                     ["diff", str(present), "--budget", "0.000001"], "NOT-DECIDABLE")


def _report() -> int:
    _run_battery()
    failures = [(arm, detail) for arm, ok, detail in RESULTS if not ok]
    for arm, ok, detail in RESULTS:
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", arm,
                                 "" if ok else " -- " + detail))
    print("COMP-PULSE BATTERY: %d/%d PASS (denominator %d)" %
          (len(RESULTS) - len(failures), len(RESULTS), len(RESULTS)))
    return 1 if failures else 0


def test_all_arms_pass():
    _run_battery()
    failures = [(arm, detail) for arm, ok, detail in RESULTS if not ok]
    assert not failures, "comp-pulse battery failures: %r" % failures


if __name__ == "__main__":
    raise SystemExit(_report())
