"""Lane-N acceptance battery for NFRA_COMPEFFICACY TO-CE-T-21.

This deliberately lives beside the pre-existing untracked
``test_comp_system_battery.py``.  The latter is not claimed by this lane; this
file supplies a separately attributable, production-mutant control for each
T-21 behavior.

Direct: ``python .tools/tests/test_comp_system_battery_ae_n.py``
Pytest: ``python -m pytest -q .tools/tests/test_comp_system_battery_ae_n.py``
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
import importlib.util
from pathlib import Path


WS = Path(__file__).resolve().parents[2]
ENGINE = WS / "org" / "modules" / "graph" / "comp_system.py"
STATES = (
    "SUBJECT_ABSENT_FROM_CORPUS",
    "PRESENT_WITH_ZERO_RESULTS",
    "PARTIAL_OR_BLIND",
    "NOT_APPLICABLE",
)


def _run(*args: str, engine: Path = ENGINE, env: dict[str, str] | None = None) -> tuple[int, str]:
    merged = os.environ.copy()
    if env:
        merged.update(env)
    completed = subprocess.run(
        [sys.executable, str(engine), *args],
        cwd=WS,
        capture_output=True,
        text=True,
        timeout=180,
        env=merged,
    )
    return completed.returncode, (completed.stdout or "") + (completed.stderr or "")


def _mutant(label: str, old: str, new: str) -> Path:
    source = ENGINE.read_text(encoding="utf-8")
    if old not in source:
        raise AssertionError(f"{label}: mutation anchor absent: {old!r}")
    mutant = ENGINE.parent / f".mutant-comp-system-lane-n-{label}-{os.getpid()}.py"
    mutant.write_text(source.replace(old, new, 1), encoding="utf-8")
    return mutant


class TestCompSystemLaneN(unittest.TestCase):
    def test_no_fabrication_first_arm_and_red_mutant(self) -> None:
        rc, output = _run("--self-test")
        self.assertEqual(0, rc, output)
        self.assertRegex(output, r"(?m)^  \[PASS\] 0  no-fabrication:")

        mutant = _mutant("no-fabrication", '"compile_complete": False', '"compile_complete": True')
        try:
            mutant_rc, mutant_output = _run("--self-test", engine=mutant)
        finally:
            mutant.unlink(missing_ok=True)
        self.assertEqual(1, mutant_rc, mutant_output)
        self.assertIn("[FAIL] 0  no-fabrication:", mutant_output)

    def test_four_ratified_states_one_invocation_and_red_mutant(self) -> None:
        rc, output = _run("--self-test")
        self.assertEqual(0, rc, output)
        self.assertTrue(all(token in output for token in STATES), output)
        self.assertIn("four planted cases emit four exact tokens", output)

        mutant = _mutant(
            "answer-state",
            'ANSWER_NOT_APPLICABLE = "NOT_APPLICABLE"',
            'ANSWER_NOT_APPLICABLE = "MUTATED_NOT_APPLICABLE"',
        )
        try:
            mutant_rc, mutant_output = _run("--self-test", engine=mutant)
        finally:
            mutant.unlink(missing_ok=True)
        self.assertEqual(1, mutant_rc, mutant_output)
        self.assertIn("ratified answer-state", mutant_output)

    def test_budgeted_check_is_not_decidable_and_red_rc_mutant(self) -> None:
        rc, output = _run("--check", "--budget", "0.001")
        self.assertEqual(3, rc, output)
        self.assertIn("PARTIAL_OR_BLIND (NOT-DECIDABLE)", output)
        self.assertIn("BUDGET REACHED: 0.001 s (flag)", output)
        self.assertIn("scanned 0 of 1 check_verdict", output)

        mutant = _mutant("check-rc", "RC_NOT_DECIDABLE = 3", "RC_NOT_DECIDABLE = 0")
        try:
            mutant_rc, mutant_output = _run("--check", "--budget", "0.001", engine=mutant)
        finally:
            mutant.unlink(missing_ok=True)
        self.assertEqual(0, mutant_rc, mutant_output)
        self.assertIn("NOT-DECIDABLE", mutant_output)

    def test_moved_aside_required_source_is_named_and_red_mutant(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "required-source.json"
            moved_aside = Path(temp_dir) / "required-source.json.aside"
            source.write_text("{}\n", encoding="utf-8")
            source.replace(moved_aside)
            env = {"COMP_SYSTEM_REQUIRED_SOURCE": str(source)}

            rc, output = _run("--check", "--budget", "0", env=env)
            self.assertEqual(3, rc, output)
            self.assertIn("required source unreadable", output)
            self.assertIn(str(source), output)
            self.assertIn("NO COMPLETE RECORD WAS WRITTEN", output)

            mutant = _mutant(
                "required-source",
                'extra = os.environ.get(_EXTRA_REQUIRED_SOURCE_ENV, "").strip()',
                'extra = ""',
            )
            try:
                previous = os.environ.get("COMP_SYSTEM_REQUIRED_SOURCE")
                os.environ["COMP_SYSTEM_REQUIRED_SOURCE"] = str(source)
                spec = importlib.util.spec_from_file_location("comp_system_lane_n_mutant", mutant)
                assert spec is not None and spec.loader is not None
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                mutant_issues = module._required_source_issues()
            finally:
                if 'previous' in locals() and previous is not None:
                    os.environ["COMP_SYSTEM_REQUIRED_SOURCE"] = previous
                else:
                    os.environ.pop("COMP_SYSTEM_REQUIRED_SOURCE", None)
                mutant.unlink(missing_ok=True)
            self.assertFalse(any(str(source) in issue for issue in mutant_issues), mutant_issues)

    def test_help_discloses_rule_t_and_red_documentation_mutant(self) -> None:
        rc, output = _run("--help")
        self.assertEqual(0, rc, output)
        self.assertIn("--budget <seconds> > COMP_BUDGET_S > default 90 s", output)
        self.assertIn("0=current 2=stale 1=error 3=NOT-DECIDABLE", output)

        mutant = _mutant("help", "default 90 s", "default 91 s")
        try:
            mutant_rc, mutant_output = _run("--help", engine=mutant)
        finally:
            mutant.unlink(missing_ok=True)
        self.assertEqual(0, mutant_rc, mutant_output)
        self.assertNotIn("default 90 s", mutant_output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
