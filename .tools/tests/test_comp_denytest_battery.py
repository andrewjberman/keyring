"""Offline battery for .tools/comp-denytest.py -- NFRA_COMPEFFICACY CE-t-11.

Every arm is fixture/stub-driven. ZERO live IAM evaluation occurs: the only subprocess that
looks like AWS is replaced by a function that records timeout= and raises TimeoutExpired.

Run: python .tools/tests/test_comp_denytest_battery.py
     python -m pytest -q .tools/tests/test_comp_denytest_battery.py
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


RESULTS: list[tuple[str, bool, str]] = []
_RAN = False
_MOD = None


def _workspace() -> Path:
    return Path(__file__).resolve().parents[2]


def _tool() -> Path:
    return _workspace() / ".tools" / "comp-denytest.py"


def _load(path: Path | None = None, name: str = "comp_denytest_battery_import"):
    tool = path or _tool()
    sys.path.insert(0, str(tool.parent))
    spec = importlib.util.spec_from_file_location(name, str(tool))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _mod():
    global _MOD
    if _MOD is None:
        _MOD = _load()
    return _MOD


def _record(arm: str, ok: bool, detail: str = "") -> None:
    RESULTS.append((arm, ok, detail))


def _capture_main(mod, argv: list[str], simulate_fn=None) -> tuple[int, str]:
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture), contextlib.redirect_stderr(capture):
        rc = mod.main(argv, simulate_fn=simulate_fn)
    return rc, capture.getvalue()


def _run(args: list[str], tool: Path | None = None) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, str(tool or _tool())] + args,
                          cwd=str(_workspace()), capture_output=True, text=True, timeout=30)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def _policy_change(address: str, actions: list[str], before: list[dict],
                   after: list[dict]) -> dict:
    def doc(rows):
        return json.dumps({"Version": "2012-10-17", "Statement": rows})

    return {
        "type": "aws_iam_role_policy",
        "address": address,
        "change": {
            "actions": actions,
            "before": {"role": "fixture-role", "policy": doc(before)},
            "after": {"role": "fixture-role", "policy": doc(after)},
        },
    }


def _write_plan(root: Path, name: str, changes: list[dict]) -> Path:
    path = root / (name + ".plan.json")
    path.write_text(json.dumps({"resource_changes": changes}), encoding="utf-8")
    return path


def _args(plan: Path, budget: str = "1") -> list[str]:
    return ["--from-plan", str(plan),
            "--principal", "arn:aws:iam::123:role/fixture-role",
            "--resource", "arn:aws:s3:::fixture/denied",
            "--action", "s3:GetObject", "--budget", budget]


def _mutant_path(kind: str) -> Path:
    return _tool().parent / ("_tmp_denytest_mutant_%s_%d.py" % (kind, os.getpid()))


def _write_mutant(kind: str, needle: str, replacement: str) -> Path:
    source = _tool().read_text(encoding="utf-8")
    count = source.count(needle)
    assert count == 1, "mutant %s expected one source target, found %d" % (kind, count)
    path = _mutant_path(kind)
    path.write_text(source.replace(needle, replacement, 1), encoding="utf-8")
    return path


def _run_battery() -> None:
    global _RAN
    if _RAN:
        return
    _RAN = True
    mod = _mod()
    states = (
        "SUBJECT_ABSENT_FROM_CORPUS",
        "PRESENT_WITH_ZERO_RESULTS",
        "PARTIAL_OR_BLIND",
        "NOT_APPLICABLE",
    )
    deny = {"Sid": "D", "Effect": "Deny", "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::fixture/denied"}

    # ARM 1: one real tool invocation prints all four ratified state tokens, pairwise distinct.
    rc, out = _run(["--offline-self-test"])
    counts = {state: out.count("ANSWER-STATE: " + state) for state in states}
    _record("DENY-AC2-FOUR-STATES-ONE-OFFLINE-INVOCATION",
            rc == 0 and counts == {state: 1 for state in states}
            and "4/4 PASS; ZERO live IAM calls" in out,
            "rc=%d counts=%r" % (rc, counts))

    with tempfile.TemporaryDirectory(prefix="comp-denytest-battery-") as td:
        root = Path(td)
        zero_plan = _write_plan(root, "zero", [
            _policy_change("aws_iam_role_policy.zero", ["no-op"], [], [])])
        deny_plan = _write_plan(root, "deny", [
            _policy_change("aws_iam_role_policy.deny", ["update"], [], [deny])])

        # ARM 2: the default fixture run says that zero population without an IAM change is correct.
        rc2, out2 = _capture_main(mod, _args(zero_plan))
        _record("DENY-AC1-CORRECT-ZERO-IN-TOOL-VOICE",
                rc2 == 0 and "ANSWER-STATE: PRESENT_WITH_ZERO_RESULTS" in out2
                and "zero population without an IAM change is CORRECT" in out2,
                "rc=%d output=%r" % (rc2, out2[:300]))

        def conditioned(_principal, _resource, _action, _context, timeout_s=None):
            del timeout_s
            return mod.SimulationOutcome(decision="implicitDeny",
                                         missing_context=("aws:SourceVpc",))

        def clean(_principal, _resource, _action, _context, timeout_s=None):
            del timeout_s
            return mod.SimulationOutcome(decision="explicitDeny")

        def finding(_principal, _resource, _action, _context, timeout_s=None):
            del timeout_s
            return mod.SimulationOutcome(decision="implicitDeny")

        # ARMS 3-5: all three verdict values are pairwise distinct; conditioned false-deny is rc 2.
        rc3, out3 = _capture_main(mod, _args(deny_plan), conditioned)
        rc4, out4 = _capture_main(mod, _args(deny_plan), clean)
        rc5, out5 = _capture_main(mod, _args(deny_plan), finding)
        _record("DENY-AC2-CONDITIONED-FALSE-DENY-NOT-DECIDABLE",
                rc3 == 2 and "ANSWER-STATE: PARTIAL_OR_BLIND" in out3
                and "STATE: NOT-DECIDABLE" in out3 and "RESULT: PASS" not in out3,
                "rc=%d output=%r" % (rc3, out3[-500:]))
        _record("DENY-AC4-RC-VOCABULARY-PAIRWISE-DISTINCT",
                (rc4, rc5, rc3) == (0, 1, 2)
                and "RESULT: PASS" in out4 and "RESULT: FAIL" in out5,
                "clean/fail/not-decidable=%r" % ((rc4, rc5, rc3),))

        # ARM 6: exercise production simulate(); timeout= receives Clock.remaining(), expiry is rc 2.
        real_run = mod.subprocess.run
        real_aws = mod.AWS
        seen_timeout = []

        def timing_out(*_args, **kwargs):
            seen_timeout.append(kwargs.get("timeout"))
            raise subprocess.TimeoutExpired(cmd="aws-fixture", timeout=kwargs.get("timeout"))

        try:
            mod.AWS = "aws-fixture"
            mod.subprocess.run = timing_out
            rc6, out6 = _capture_main(mod, _args(deny_plan, "0.25"))
        finally:
            mod.subprocess.run = real_run
            mod.AWS = real_aws
        _record("DENY-AC4-TIMEOUT-CARRIER-AND-RC-CONSUMER",
                rc6 == 2 and len(seen_timeout) == 1
                and seen_timeout[0] is not None and 0 < seen_timeout[0] <= 0.25
                and "BUDGET REACHED" in out6 and "STATE: NOT-DECIDABLE" in out6,
                "rc=%d timeout=%r output=%r" % (rc6, seen_timeout, out6[-500:]))

        # ARM 7: the public help carries the whole rc vocabulary and Rule-T/non-application facts.
        rc7, out7 = _run(["--help"])
        _record("DENY-AC4-HELP-DISCLOSES-CARRIER-AND-RCS",
                rc7 == 0 and "RC VOCABULARY" in out7 and "0  clean" in out7
                and "1  fail" in out7 and "2  NOT-DECIDABLE" in out7
                and "COMP_BUDGET_S" in out7 and "no corpus-width loop" in out7,
                "rc=%d" % rc7)

        # ARM 8 (RED): collapse the answer-state printer; the built-in 4-state check must fail.
        mutant1 = None
        try:
            mutant1 = _write_mutant(
                "state_collapse",
                '    print(f"ANSWER-STATE: {state}")\n',
                '    print("ANSWER-STATE: PARTIAL_OR_BLIND")  # MUTANT: all states collapse\n',
            )
            mrc1, mout1 = _run(["--offline-self-test"], mutant1)
            _record("DENY-AC5-MUTANT-STATE-COLLAPSE-RED",
                    mrc1 != 0 and "4/4 PASS" not in mout1,
                    "mutant rc=%d summary=%r" % (mrc1, mout1[-180:]))
        finally:
            if mutant1 is not None and mutant1.exists():
                mutant1.unlink()

        # ARM 9 (RED): return clean from the undecidable branch; the rc-only predicate catches it.
        mutant2 = None
        try:
            mutant2 = _write_mutant(
                "clean_on_undecidable",
                "        return RC_NOT_DECIDABLE\n",
                "        return RC_CLEAN  # MUTANT: unreadable simulation now looks clean\n",
            )
            mm2 = _load(mutant2, "comp_denytest_mutant_clean_%d" % os.getpid())

            def mm2_conditioned(_principal, _resource, _action, _context, timeout_s=None):
                del timeout_s
                return mm2.SimulationOutcome(decision="implicitDeny",
                                             missing_context=("aws:SourceVpc",))

            mrc2, mout2 = _capture_main(mm2, _args(deny_plan), mm2_conditioned)
            _record("DENY-AC5-MUTANT-CLEAN-ON-UNDECIDABLE-RED",
                    mrc2 == 0 and "STATE: NOT-DECIDABLE" in mout2,
                    "mutant exposes defect as rc=%d" % mrc2)
        finally:
            if mutant2 is not None and mutant2.exists():
                mutant2.unlink()

        # ARM 10 (RED): remove timeout= from subprocess.run; carrier predicate sees None.
        mutant3 = None
        try:
            mutant3 = _write_mutant(
                "timeout_removed",
                "                             timeout=timeout_s)\n",
                "                             timeout=None)  # MUTANT: Rule T carrier removed\n",
            )
            mm3 = _load(mutant3, "comp_denytest_mutant_timeout_%d" % os.getpid())
            mm3_real_run = mm3.subprocess.run
            mm3_real_aws = mm3.AWS
            mutant_timeout = []

            def mutant_run(*_args, **kwargs):
                mutant_timeout.append(kwargs.get("timeout"))
                raise subprocess.TimeoutExpired(cmd="aws-fixture", timeout=kwargs.get("timeout"))

            try:
                mm3.AWS = "aws-fixture"
                mm3.subprocess.run = mutant_run
                mm3.simulate("arn:aws:iam::123:role/r", "arn:aws:s3:::fixture/x",
                             "s3:GetObject", [], timeout_s=0.25)
            finally:
                mm3.subprocess.run = mm3_real_run
                mm3.AWS = mm3_real_aws
            _record("DENY-AC5-MUTANT-TIMEOUT-REMOVED-RED",
                    mutant_timeout == [None],
                    "mutant subprocess timeout=%r (production arm saw %r)" %
                    (mutant_timeout, seen_timeout))
        finally:
            if mutant3 is not None and mutant3.exists():
                mutant3.unlink()


def _report() -> int:
    _run_battery()
    failures = [row for row in RESULTS if not row[1]]
    for arm, ok, detail in RESULTS:
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", arm,
                                "" if ok else " -- " + detail[:300]))
    print("COMP-DENYTEST BATTERY: %d/%d PASS" % (len(RESULTS) - len(failures), len(RESULTS)))
    return 1 if failures else 0


def test_all_arms_pass():
    _run_battery()
    failures = [(arm, detail) for arm, ok, detail in RESULTS if not ok]
    assert not failures, "comp-denytest battery failures: %r" % failures


if __name__ == "__main__":
    sys.exit(_report())
