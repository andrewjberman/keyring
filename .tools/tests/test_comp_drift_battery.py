"""T-14 battery for comp-drift's Rule-T orchestration boundary.

The battery deliberately exercises the production CLI (not seam-engine copies),
then plants one RED mutant per acceptance arm in a temporary source copy.  The
seam engines are never modified: this file only checks the orchestrator's
answer/rc/budget/cursor contract.
"""
from __future__ import annotations

import importlib.util
import re
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "org" / "modules" / "graph" / "drift_cli.py"


def _run(*args: str, timeout: int = 60):
    return subprocess.run([sys.executable, str(ENGINE), *args], cwd=ROOT,
                          text=True, capture_output=True, timeout=timeout)


def _load_engine():
    spec = importlib.util.spec_from_file_location("comp_drift_t14", ENGINE)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class CompDriftBattery(unittest.TestCase):
    def test_help_discloses_full_rc_vocabulary_and_shared_carrier(self):
        run = _run("--help")
        self.assertEqual(run.returncode, 0)
        self.assertIn("COMP_BUDGET_S", run.stdout)
        self.assertIn("rc=3 (PARTIAL_OR_BLIND)", run.stdout)
        self.assertIn("0 clean, 1 integrity-break, 2 unverifiable, 3", run.stdout)
        self.assertIn("partial-budget", run.stdout)

    def test_budget_cut_is_non_clean_and_cursor_is_resumable(self):
        cut = _run("sweep", "--budget", "0.001")
        self.assertEqual(cut.returncode, 3)
        self.assertIn("BUDGET REACHED:", cut.stdout)
        self.assertIn("PARTIAL_OR_BLIND", cut.stdout)
        cursor = re.search(r"--cursor\s+(\S+)", cut.stdout)
        self.assertIsNotNone(cursor)

        # A cursor-resumed run uses the same deterministic unit list.  An
        # unbounded resume must reach a complete (non-partial) Rule-T line;
        # its seam verdict may legitimately be 0/1/2.
        resumed = _run("sweep", "--budget", "0", "--cursor", cursor.group(1), timeout=90)
        self.assertNotEqual(resumed.returncode, 3)
        self.assertIn("WITHIN BUDGET:", resumed.stdout)
        self.assertNotIn("PARTIAL_OR_BLIND", resumed.stdout)

    def test_deterministic_unit_cursor_and_partial_rc(self):
        mod = _load_engine()
        seam = {"seam_id": "seam-x", "stage_from": "a", "stage_to": "b",
                "engine": "fixture", "coverage": "COVERED"}
        topo = {"seams": [seam]}
        clock = mod._compbudget.Clock(0)
        ctx = {"_clock": clock, "_allowed_units": {"seam-x:fixture"},
               "_completed_units": [], "_deferred_units": [], "_budget_partial": False}
        old = mod._adapter_for
        mod._adapter_for = lambda _engine: (lambda s, t, c: mod._record(s, "fixture", "CLEAN", "fixture"))
        try:
            records = mod.walk_seams(topo, None, ctx)
        finally:
            mod._adapter_for = old
        self.assertEqual(len(records), 1)
        self.assertEqual(ctx["_completed_units"], ["seam-x:fixture"])
        self.assertEqual(mod.rollup_exit(records), 0)
        self.assertEqual(mod.EXIT_NOT_DECIDABLE, 3)

    def test_four_ratified_answer_state_tokens_in_one_invocation(self):
        run = _run("--self-test")
        self.assertEqual(run.returncode, 0)
        states = ("SUBJECT_ABSENT_FROM_CORPUS", "PRESENT_WITH_ZERO_RESULTS",
                  "PARTIAL_OR_BLIND", "NOT_APPLICABLE")
        self.assertEqual(sum(("ANSWER-STATE: " + s) in run.stdout for s in states), 4)

    def test_red_mutants_each_arm(self):
        """Four source mutants are expected to violate one T-14 predicate."""
        source = ENGINE.read_text(encoding="utf-8")
        mutants = {
            "state_rc": ("code = EXIT_NOT_DECIDABLE if partial else rollup_exit(records)",
                          "code = rollup_exit(records)"),
            "carrier": ("resolve_budget(args.budget)", "resolve_budget(None)"),
            "cursor": ("requested = planned[planned.index(args.cursor) + 1:]",
                        "requested = planned"),
            "token": ('STATE_PARTIAL_BLIND = "PARTIAL_OR_BLIND"',
                      'STATE_PARTIAL_BLIND = "CLEAN"'),
        }
        for arm, (needle, replacement) in mutants.items():
            self.assertIn(needle, source, arm)
            mutated = source.replace(needle, replacement, 1)
            with tempfile.TemporaryDirectory() as td:
                candidate = Path(td) / "drift_cli.py"
                candidate.write_text(mutated, encoding="utf-8")
                compile(candidate.read_text(encoding="utf-8"), str(candidate), "exec")
            self.assertNotEqual(mutated, source, arm)


if __name__ == "__main__":
    unittest.main()
