"""Production comp-blast battery for T-6: states, Rule-T, and carried trace flags."""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENGINE = ROOT / "org" / "modules" / "graph" / "cli.py"
UNIVERSE = ROOT / "org" / "modules" / "graph" / "comp_blast_universe.py"
SHIM = ROOT / ".tools" / "comp-blast"


def run_blast(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [r"C:\Program Files\Git\bin\bash.exe", ".tools/comp-blast", *args], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120,
    )


class CompBlastBattery(unittest.TestCase):
    def test_help_discloses_carrier_full_rc_and_carry_flags(self):
        p = run_blast("--help")
        self.assertEqual(p.returncode, 0)
        out = p.stdout + p.stderr
        normalized = " ".join(out.split())
        for needle in ("COMP_BUDGET_S", "--cursor", "--exact", "--all",
                       "upstream", "downstream", "rc vocabulary", "6 partial-budget"):
            self.assertIn(needle, normalized)

    def test_one_self_test_invocation_has_four_distinct_ratified_tokens(self):
        p = run_blast("--self-test")
        self.assertEqual(p.returncode, 0)
        tokens = re.findall(r"ANSWER-STATE: ([A-Z_]+)", p.stdout)
        self.assertEqual(tokens, [
            "SUBJECT_ABSENT_FROM_CORPUS", "PRESENT_WITH_ZERO_RESULTS",
            "PARTIAL_OR_BLIND", "NOT_APPLICABLE",
        ])
        self.assertIn("four_distinct_tokens: PASS", p.stdout)

    def test_exact_not_found_is_loud_with_denominator_and_vintage(self):
        p = run_blast("--force", "--exact", "T6-no-such-node")
        self.assertEqual(p.returncode, 3)
        out = p.stdout + p.stderr
        self.assertIn("ANSWER-STATE: SUBJECT_ABSENT_FROM_CORPUS", out)
        self.assertRegex(out, r"denominator: [0-9]+ nodes \(CANONICAL KUZU GRAPH\)")
        self.assertIn("built:", out)
        self.assertNotRegex(out, r"radius\s*[:=]\s*0")

    def test_budget_prefix_is_nonclean_and_cursor_resume_is_complete(self):
        p = run_blast("--force", "arn:aws:s3:::opal-data-bd", "--direction", "down",
                      "--depth", "1", "--budget", "0.001")
        self.assertEqual(p.returncode, 6)
        out = p.stdout + p.stderr
        self.assertIn("BUDGET REACHED", out)
        self.assertIn("ANSWER-STATE: PARTIAL_OR_BLIND", out)
        m = re.search(r"--cursor (down:[^\s]+)", out)
        self.assertIsNotNone(m)
        resume = run_blast("--force", "arn:aws:s3:::opal-data-bd", "--direction", "down",
                           "--depth", "1", "--budget", "0", "--cursor", m.group(1))
        self.assertNotEqual(resume.returncode, 6)
        self.assertIn("WITHIN BUDGET", resume.stdout + resume.stderr)
        self.assertNotIn("PARTIAL_OR_BLIND", resume.stdout + resume.stderr)

    def test_budget_bounds_universe_load_and_discloses_stale_serve(self):
        """AC-7: a stale canonical pin is served immediately; no refresh child is entered."""
        p = run_blast("--exact", "arn:aws:s3:::opal-data-bd", "--direction", "down",
                      "--depth", "1", "--budget", "60")
        self.assertEqual(p.returncode, 0)
        out = p.stdout + p.stderr
        self.assertRegex(out, r"BUDGETED CALL: (SERVING EXISTING GRAPH STALE|existing graph current)")
        if "SERVING EXISTING GRAPH STALE" in out:
            self.assertRegex(out, r"age [0-9.]+h")
        self.assertNotIn("Building trace graph", out)
        self.assertNotIn("kuzu_nessie_load.py", out)

    def test_trace_aliases_and_exact_are_accepted_by_blast(self):
        p = run_blast("--force", "--exact", "arn:aws:s3:::opal-313476888478-globgrph",
                      "--direction", "downstream", "--budget", "0")
        self.assertEqual(p.returncode, 0)
        self.assertIn("PRESENT_WITH_ZERO_RESULTS", p.stdout + p.stderr)
        p_all = run_blast("--force", "--exact", "arn:aws:s3:::opal-313476888478-globgrph",
                          "--all", "--budget", "0")
        self.assertEqual(p_all.returncode, 0)
        self.assertIn("WITHIN BUDGET", p_all.stdout + p_all.stderr)

    def test_red_mutants_each_required_arm(self):
        source = ENGINE.read_text(encoding="utf-8")
        mutants = {
            "not_found_radius": (
                'print(f"ANSWER-STATE: {STATE_SUBJECT_ABSENT}")',
                'print("radius: 0")',
            ),
            "exact_fuzzy": (
                '_blast_resolve_subject(g, query, getattr(args, "exact", False))',
                '_bu.resolve_subject(g, query)',
            ),
            "wrong_alias": (
                '{"upstream": "up", "downstream": "down"}',
                '{"upstream": "down", "downstream": "up"}',
            ),
            "partial_clean": (
                'sys.exit(EXIT_PARTIAL_BUDGET)',
                'sys.exit(0)',
            ),
        }
        for name, (needle, replacement) in mutants.items():
            self.assertIn(needle, source, name)
            mutated = source.replace(needle, replacement, 1)
            self.assertNotEqual(mutated, source, name)
            with tempfile.TemporaryDirectory() as td:
                path = Path(td) / "cli_mutant.py"
                path.write_text(mutated, encoding="utf-8")
                check = subprocess.run([sys.executable, "-m", "py_compile", str(path)],
                                       text=True, capture_output=True)
                self.assertEqual(check.returncode, 0, name)
        source = UNIVERSE.read_text(encoding="utf-8")
        needle = "refresh_allowed = not budgeted"
        self.assertIn(needle, source, "budgeted_refresh_ambush")
        mutated = source.replace(needle, "refresh_allowed = True", 1)
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "universe_mutant.py"
            path.write_text(mutated, encoding="utf-8")
            check = subprocess.run([sys.executable, "-m", "py_compile", str(path)],
                                   text=True, capture_output=True)
            self.assertEqual(check.returncode, 0, "budgeted_refresh_ambush")


if __name__ == "__main__":
    unittest.main()
