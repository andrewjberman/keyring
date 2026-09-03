"""NFRA_COMPEFFICACY T-5 battery for comp-schedule's s.4 answer and Rule-T contract.

Run at both required file grains:
  python .tools/tests/test_comp_schedule_battery.py
  python -m pytest -q .tools/tests/test_comp_schedule_battery.py

The production CLI supplies the evidence. Every behavior arm also runs a source mutant and proves
that the arm rejects it; mutant copies are temporary and the production engine is never rewritten.
"""
from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import types
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / ".tools" / "comp-schedule"
RESULTS: list[tuple[str, bool, str]] = []


def _run(*args: str, tool: Path = ENGINE, timeout: int = 180):
    return subprocess.run([sys.executable, str(tool), *args], cwd=ROOT, text=True,
                          capture_output=True, timeout=timeout)


def _record(name: str, ok: bool, detail: str) -> None:
    RESULTS.append((name, ok, detail.replace("\n", " ")[:240]))


def _mutant_run(needle: str, replacement: str, *args: str):
    source = ENGINE.read_text(encoding="utf-8")
    if source.count(needle) != 1:
        raise AssertionError("mutation anchor count != 1 for %r: %d" %
                             (needle, source.count(needle)))
    path = ENGINE.parent / (".comp-schedule-t5-%s.tmp" % uuid.uuid4().hex)
    try:
        path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
        return _run(*args, tool=path)
    finally:
        if path.exists():
            path.unlink()


def _load_mutant(needle: str, replacement: str):
    source = ENGINE.read_text(encoding="utf-8")
    if source.count(needle) != 1:
        raise AssertionError("mutation anchor count != 1 for %r: %d" %
                             (needle, source.count(needle)))
    source = source.replace(needle, replacement, 1)
    name = "comp_schedule_t5_mutant_%s" % uuid.uuid4().hex
    module = types.ModuleType(name)
    module.__file__ = str(ENGINE)
    sys.modules[name] = module
    exec(compile(source, str(ENGINE), "exec"), module.__dict__)
    return module


def _synthetic_main(module, expired: bool):
    """Run the real main/Rule-T branch with a sealed in-memory carrier compile."""
    carrier = module.Carrier("C1", "FIXTURE", "DECIDABLE")
    carrier.denominator = 1
    carrier.gates = [{"id": "G-1", "owner": "fixture", "discharge": "fixture",
                      "last_verified": "fixture", "evidence": ["fixture"], "drift": []}]
    module._compile_budgeted = lambda _clock, cursor=None: ([carrier], 1, expired)
    rendered = {}
    module.render = lambda *_a, **kw: rendered.update(kw)
    old_argv = sys.argv
    try:
        sys.argv = [str(ENGINE), "--budget", "1"]
        rc = module.main()
    finally:
        sys.argv = old_argv
    return rc, rendered


def _run_battery() -> None:
    if RESULTS:
        return

    help_run = _run("--help")
    help_ok = (help_run.returncode == 0 and "--budget <seconds>" in help_run.stdout
               and "COMP_BUDGET_S" in help_run.stdout and "default 90 s" in help_run.stdout
               and "--cursor <START|C1..C5>" in help_run.stdout and "rc" in help_run.stdout.lower())
    _record("HELP-RULE-T-CARRIER", help_ok, help_run.stdout)
    help_mutant = _mutant_run("comp-schedule --budget <seconds>",
                              "comp-schedule --ceiling <seconds>", "--help")
    _record("HELP-RULE-T-CARRIER-RED-MUTANT",
            "--budget <seconds>" not in help_mutant.stdout, help_mutant.stdout)

    cases = _run("--answer-state-cases")
    states = (
        ("SUBJECT_ABSENT_FROM_CORPUS", "STATE_SUBJECT_ABSENT"),
        ("PRESENT_WITH_ZERO_RESULTS", "STATE_PRESENT_ZERO"),
        ("PARTIAL_OR_BLIND", "STATE_PARTIAL_OR_BLIND"),
        ("NOT_APPLICABLE", "STATE_NOT_APPLICABLE"),
    )
    _record("FOUR-STATES-ONE-INVOCATION",
            cases.returncode == 0 and "PASS 4/4 distinct state tokens" in cases.stdout
            and sum(("ANSWER-STATE: " + token) in cases.stdout for token, _ in states) == 4,
            cases.stdout)
    source = ENGINE.read_text(encoding="utf-8")
    for token, const in states:
        expected = "ANSWER-STATE: " + token
        ok = expected in cases.stdout
        _record("STATE-%s" % token, ok, cases.stdout)
        anchor = '%s = "%s"' % (const, token)
        mutant = _mutant_run(anchor, '%s = "MUTANT_%s"' % (const, token),
                             "--answer-state-cases")
        _record("STATE-%s-RED-MUTANT" % token,
                mutant.returncode == 0 and expected not in mutant.stdout, mutant.stdout)

    # A complete real view proves the five live carrier rows retain their own denominator and
    # decidability while gaining a machine-readable answer token. It also proves Rule-T completion.
    complete = _run("--budget", "0")
    carrier_lines = [line for line in complete.stdout.splitlines()
                     if line.startswith("  C") and "denominator=" in line]
    carrier_ok = (complete.returncode == 0 and len(carrier_lines) == 5
                  and all("answer-state=" in line for line in carrier_lines)
                  and all("answer-state=PARTIAL_OR_BLIND" in line and
                          "tool-voice=NOT-DECIDABLE" in line
                          for line in carrier_lines if line.startswith(("  C4", "  C5"))))
    _record("EVERY-CARRIER-ANSWER-TOKEN", carrier_ok, " | ".join(carrier_lines))

    carrier_module = _load_mutant('suffix = "answer-state=%s" % state',
                                  'suffix = "classification=%s" % state')
    fixture = carrier_module.Carrier("C4", "FIXTURE", "SEMI-DECIDABLE")
    fixture.denominator = 2
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        carrier_module.render([fixture])
    _record("EVERY-CARRIER-ANSWER-TOKEN-RED-MUTANT",
            "answer-state=" not in output.getvalue(), output.getvalue())

    completed_ok = ("WITHIN BUDGET: scanned 5 of 5 carriers" in complete.stdout
                    and "BUDGET REACHED:" not in complete.stdout
                    and "REACHED-DENOMINATORS: C1=" in complete.stdout
                    and "C5=" in complete.stdout)
    _record("RULE-T-COMPLETE", completed_ok, complete.stdout[:500])
    complete_module = _load_mutant(
        "terminal = _compbudget.within_budget_line(",
        'terminal = "MUTANT-WITHOUT-COMPLETE" or _compbudget.within_budget_line(')
    _, complete_render = _synthetic_main(complete_module, expired=False)
    _record("RULE-T-COMPLETE-RED-MUTANT",
            "WITHIN BUDGET:" not in complete_render.get("budget_terminal", ""),
            str(complete_render))

    # The live tiny-budget run is deliberately real: it must complete C1 before speaking because a
    # carrier's native denominator is knowable only after that carrier is read.
    cut = _run("--budget", "0.001")
    cut_ok = (cut.returncode == 3 and "BUDGET REACHED: 0.001 s (flag)" in cut.stdout
              and "scanned 0 of 5 carriers" in cut.stdout
              and "ANSWER-STATE: PARTIAL_OR_BLIND" in cut.stdout
              and "tool-voice=NOT-DECIDABLE" in cut.stdout
              and "REACHED-DENOMINATORS: C1=" in cut.stdout
              and "C2=NOT-SCANNED" in cut.stdout and "--cursor START" in cut.stdout)
    _record("RULE-T-PARTIAL-NONCLEAN-RC", cut_ok, cut.stdout[:700])

    partial_module = _load_mutant(
        "return RC_NOT_DECIDABLE if expired else RC_COMPLETE",
        "return RC_COMPLETE")
    partial_rc, partial_render = _synthetic_main(partial_module, expired=True)
    _record("RULE-T-PARTIAL-NONCLEAN-RC-RED-MUTANT",
            partial_rc == 0 and "BUDGET REACHED:" in partial_render.get("budget_terminal", ""),
            "mutant rc=%s render=%r" % (partial_rc, partial_render))

    # Mutation anchors themselves are contract evidence: every one was unique before it ran.
    _record("MUTATION-ANCHORS-UNIQUE", all(source.count('%s = "%s"' % (const, token)) == 1
                                           for token, const in states), "four unique constants")


def _report() -> int:
    _run_battery()
    failed = [(name, detail) for name, ok, detail in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                              "" if ok else " -- " + detail))
    print("COMP-SCHEDULE T5 BATTERY: %d/%d PASS (denominator %d)" %
          (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(name, detail) for name, ok, detail in RESULTS if not ok]
    assert not failed, "comp-schedule T5 battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
