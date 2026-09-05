#!/usr/bin/env python3
"""T20 battery: comp-heat's four answer states are CLI + JSON contracts."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / ".tools" / "comp-heat"
STATES = (
    ("SUBJECT_ABSENT_FROM_CORPUS", 2, ["freshness", "__T20_ABSENT_HEAT__", "--json"], {}),
    ("PRESENT_WITH_ZERO_RESULTS", 0, ["freshness", ".git", "--json"], {}),
    ("PARTIAL_OR_BLIND", 3, ["freshness", "--json"],
     {"COMP_HEATMAP_DIR": "__T20_MISSING_HEATMAP__"}),
    ("NOT_APPLICABLE", 1, ["compare", ".tools/comp-heat", ".tools/comp-heat", "--json"], {}),
)


def run(args, *, tool=TOOL, extra_env=None):
    env = os.environ.copy()
    env.update(extra_env or {})
    return subprocess.run(["python", str(tool), *args], cwd=ROOT, text=True,
                          capture_output=True, env=env, timeout=45)


class CompHeatBattery(unittest.TestCase):
    def test_four_cli_json_answer_states(self):
        for state, rc, args, env in STATES:
            with self.subTest(state=state):
                got = run(args, extra_env=env)
                self.assertEqual(got.returncode, rc, got.stderr)
                payload = json.loads(got.stdout)
                self.assertEqual(payload["answer_state"], state)
                self.assertIn("measured_at_utc", payload["vintage"])
                self.assertTrue(payload["vintage"]["measured_at_utc"].endswith("Z"))
                human = run([arg for arg in args if arg != "--json"], extra_env=env)
                self.assertEqual(human.returncode, rc, human.stderr)
                self.assertIn(f"ANSWER-STATE: {state}", human.stdout)

    def test_red_mutant_per_answer_state_arm(self):
        source = TOOL.read_text(encoding="utf-8")
        for state, _rc, args, env in STATES:
            with self.subTest(state=state), tempfile.NamedTemporaryFile(
                    mode="w", dir=TOOL.parent, prefix=".mutant-comp-heat-", delete=False,
                    encoding="utf-8") as mutant:
                mutant_path = Path(mutant.name)
                mutant.write(source.replace(f'"{state}"', '"MUTANT_COLLAPSED_STATE"', 1))
            try:
                got = run(args, tool=mutant_path, extra_env=env)
                self.assertNotEqual(got.returncode, 124, "a timeout is not a red mutant")
                payload = json.loads(got.stdout)
                self.assertNotEqual(payload.get("answer_state"), state,
                                    "mutant failed to break its paired state arm")
            finally:
                mutant_path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
