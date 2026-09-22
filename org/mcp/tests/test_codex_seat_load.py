from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
LOAD_SCRIPT = REPO_ROOT / "org" / "mcp" / "codex-seat-load.py"
INSTALL_SCRIPT = REPO_ROOT / "org" / "mcp" / "install-codex-load-skill.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


seat_load = load_module(LOAD_SCRIPT, "codex_seat_load")
skill_install = load_module(INSTALL_SCRIPT, "install_codex_load_skill")


class WorkspaceFixture:
    def __init__(self, root: Path):
        self.root = root
        for relative in (
            "AGENTS.md",
            "org/XXX.md",
            "org/mcp/CODEX_INBOX_MONITOR.md",
        ):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(relative, encoding="utf-8")

        self.base_home = root / "org" / "tier1_exec" / "4.0.0_SA_CRO"
        self.base_home.mkdir(parents=True)
        (self.base_home / "README.md").write_text("role", encoding="utf-8")
        (self.base_home / "prompt.md").write_text("prompt", encoding="utf-8")
        for child in ("task_orders", "logs", "deliverables"):
            (self.base_home / child).mkdir()


class SeatContextTests(unittest.TestCase):
    def write_manifest(self, fixture, seats):
        (fixture.root / seat_load.ROLE_FILES_MANIFEST).write_text(
            json.dumps({"version": 1, "seats": seats}), encoding="utf-8"
        )

    def test_exact_seat_manifest_bounds_reads_and_preserves_other_lanes(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            (fixture.base_home / "old_drive_log.md").write_text("history", encoding="utf-8")
            paths = ["org/tier1_exec/4.0.0_SA_CRO/prompt.md",
                     "org/tier1_exec/4.0.0_SA_CRO/README.md"]
            self.write_manifest(fixture, {"4.0.0_SA_CRO~A": paths})
            bounded = seat_load.build_context(fixture.root, "4.0.0_SA_CRO~A")
            other = seat_load.build_context(fixture.root, "4.0.0_SA_CRO~B")
        self.assertEqual(bounded["role_files"], paths)  # declared order, not alphabetic
        self.assertEqual(bounded["role_files_source"], seat_load.ROLE_FILES_MANIFEST)
        self.assertEqual(bounded["seat_home"], bounded["role_home"])
        self.assertEqual(bounded["inbox"], "org/mcp/inbox/4.0.0_SA_CRO/~A")
        self.assertEqual(other["role_files_source"], "base-role-root")
        self.assertTrue(any(p.endswith("old_drive_log.md") for p in other["role_files"]))

    def test_declared_missing_invalid_or_escaping_files_fail_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            base = ["org/tier1_exec/4.0.0_SA_CRO/README.md",
                    "org/tier1_exec/4.0.0_SA_CRO/prompt.md"]
            for entries in ([], "README.md", [None], base + ["missing.md"],
                            base + ["../outside.md"], base + [base[0]], base[:1],
                            base + [str(fixture.base_home / "README.md")]):
                with self.subTest(entries=entries):
                    self.write_manifest(fixture, {"4.0.0_SA_CRO~A": entries})
                    with self.assertRaises(seat_load.SeatLoadError):
                        seat_load.build_context(fixture.root, "4.0.0_SA_CRO~A")

    def test_bad_manifest_structure_fails_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            for content in ("{broken", "[]", '{"version": 2, "seats": {}}'):
                with self.subTest(content=content):
                    (fixture.root / seat_load.ROLE_FILES_MANIFEST).write_text(content, encoding="utf-8")
                    with self.assertRaises(seat_load.SeatLoadError):
                        seat_load.build_context(fixture.root, "4.0.0_SA_CRO~A")

    def test_irpt_exact_seat_manifests_exist_and_retain_identity(self):
        for base in ("2.0.0_SA_COO", "3.0.0_SA_CVO"):
            for lane in "PMY":
                serial = f"{base}~{lane}"
                with self.subTest(serial=serial):
                    context = seat_load.build_context(REPO_ROOT, serial)
                    self.assertEqual(context["role_files_source"], seat_load.ROLE_FILES_MANIFEST)
                    self.assertEqual(context["seat_home"], f"org/tier1_exec/{base}")
                    self.assertEqual(context["inbox"], f"org/mcp/inbox/{base}/~{lane}")
                    self.assertEqual(len(context["role_files"]), 6)
                    self.assertTrue(context["role_files"][-1].endswith(f"{base.split('_')[-1]}_{lane}.md"))

    def test_base_serial_uses_base_home_and_base_inbox(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            context = seat_load.build_context(fixture.root, "4.0.0_SA_CRO")

        self.assertIsNone(context["lane"])
        self.assertEqual(context["role_home"], "org/tier1_exec/4.0.0_SA_CRO")
        self.assertEqual(context["seat_home"], context["role_home"])
        self.assertEqual(context["inbox"], "org/mcp/inbox/4.0.0_SA_CRO")

    def test_suffixed_serial_reuses_base_home_and_preserves_runtime_identity(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            context = seat_load.build_context(fixture.root, "4.0.0_SA_CRO~A")

        self.assertEqual(context["base_serial"], "4.0.0_SA_CRO")
        self.assertEqual(context["lane"], "A")
        self.assertEqual(context["role_home"], "org/tier1_exec/4.0.0_SA_CRO")
        self.assertEqual(context["seat_home"], context["role_home"])
        self.assertEqual(context["task_orders"], "org/tier1_exec/4.0.0_SA_CRO/task_orders")
        self.assertEqual(context["logs"], "org/tier1_exec/4.0.0_SA_CRO/logs")
        self.assertEqual(context["deliverables"], "org/tier1_exec/4.0.0_SA_CRO/deliverables")
        self.assertEqual(context["inbox"], "org/mcp/inbox/4.0.0_SA_CRO/~A")
        self.assertNotIn("4.0.0_SA_CRO~A", context["inbox"])
        self.assertEqual(context["runtime"], ".runtime/codex-seats/4.0.0_SA_CRO~A")
        self.assertIn("4.0.0_SA_CRO~A", context["status_command"])
        self.assertEqual(
            context["role_files"],
            [
                "org/tier1_exec/4.0.0_SA_CRO/README.md",
                "org/tier1_exec/4.0.0_SA_CRO/prompt.md",
            ],
        )

    def test_invalid_serial_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            with self.assertRaises(seat_load.SeatLoadError):
                seat_load.build_context(fixture.root, "CRO~A")

    def test_exact_lane_home_is_not_required(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            context = seat_load.build_context(fixture.root, "4.0.0_SA_CRO~B")

        self.assertEqual(context["seat_home"], "org/tier1_exec/4.0.0_SA_CRO")
        self.assertEqual(context["inbox"], "org/mcp/inbox/4.0.0_SA_CRO/~B")

    def test_ambiguous_role_home_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            duplicate = fixture.root / "org" / "tier2_senior" / "4.0.0_SA_CRO"
            duplicate.mkdir(parents=True)
            with self.assertRaisesRegex(seat_load.SeatLoadError, "ambiguous"):
                seat_load.build_context(fixture.root, "4.0.0_SA_CRO")

    def test_prompt_is_exact_and_requires_load_skill(self):
        context = {"serial": "4.0.0_SA_CRO~A"}
        prompt = seat_load.build_prompt(context)
        self.assertIn("Use $load", prompt)
        self.assertIn("4.0.0_SA_CRO~A", prompt)
        self.assertIn("do not infer or alter it", prompt)

    def test_cli_json_is_machine_readable(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = WorkspaceFixture(Path(temporary))
            completed = subprocess.run(
                [
                    sys.executable,
                    str(LOAD_SCRIPT),
                    "--workspace",
                    str(fixture.root),
                    "--serial",
                    "4.0.0_SA_CRO~A",
                    "--format",
                    "json",
                ],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(json.loads(completed.stdout)["lane"], "A")


class SkillInstallTests(unittest.TestCase):
    def test_install_is_byte_exact_and_idempotent(self):
        with tempfile.TemporaryDirectory() as temporary:
            codex_home = Path(temporary) / "codex-home"
            first = skill_install.install(REPO_ROOT, codex_home)
            second = skill_install.install(REPO_ROOT, codex_home)
            target = codex_home / "skills" / "load"

            self.assertEqual(
                first["changed"], ["SKILL.md", "agents/openai.yaml"]
            )
            self.assertEqual(second["changed"], [])
            for relative in skill_install.EXPECTED_FILES:
                self.assertEqual(
                    (target / relative).read_bytes(),
                    (REPO_ROOT / "org/mcp/codex-skills/load" / relative).read_bytes(),
                )

    def test_unexpected_target_file_fails_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            codex_home = Path(temporary) / "codex-home"
            target = codex_home / "skills" / "load"
            target.mkdir(parents=True)
            (target / "foreign.txt").write_text("foreign", encoding="utf-8")
            with self.assertRaisesRegex(skill_install.InstallError, "unexpected"):
                skill_install.install(REPO_ROOT, codex_home)

    def test_install_all_projects_load_and_log_byte_exactly(self):
        with tempfile.TemporaryDirectory() as temporary:
            codex_home = Path(temporary) / "codex-home"
            first = skill_install.install_all(REPO_ROOT, codex_home)
            second = skill_install.install_all(REPO_ROOT, codex_home)

            self.assertEqual(
                [item["skill"] for item in first["skills"]], ["load", "log"]
            )
            for name, receipt in zip(
                skill_install.CANONICAL_SKILLS, first["skills"], strict=True
            ):
                self.assertEqual(
                    receipt["changed"], ["SKILL.md", "agents/openai.yaml"]
                )
                self.assertEqual(second["skills"][["load", "log"].index(name)]["changed"], [])
                for relative in skill_install.EXPECTED_FILES:
                    self.assertEqual(
                        (codex_home / "skills" / name / relative).read_bytes(),
                        (
                            REPO_ROOT
                            / "org/mcp/codex-skills"
                            / name
                            / relative
                        ).read_bytes(),
                    )


class LauncherIntegrationTests(unittest.TestCase):
    def test_host_installs_skill_and_injects_prompt_for_new_and_resume(self):
        source = (REPO_ROOT / "org/mcp/start-codex-seat.ps1").read_text(
            encoding="utf-8"
        )
        self.assertIn("install-codex-load-skill.py", source)
        self.assertIn("$load and $log", source)
        self.assertIn("codex-seat-load.py", source)
        self.assertIn("$env:OPAL_AGENT_SERIAL = $Serial", source)
        self.assertIn("--format prompt", source)
        self.assertGreaterEqual(source.count("$startupPrompt"), 8)
        self.assertIn(
            r"""$startupPromptArgument = $startupPrompt.Replace('"', '\"')""",
            source,
        )
        self.assertIn("$ThreadId $startupPromptArgument", source)
        self.assertIn("-C $Workspace $startupPromptArgument", source)

    def test_ajb2_exposes_automatic_load_topology(self):
        source = (REPO_ROOT / ".tools/ajb2.ps1").read_text(encoding="utf-8")
        self.assertIn("org\\mcp\\codex-skills\\{load,log}", source)
        self.assertIn("org\\mcp\\codex-seat-load.py", source)
        self.assertIn("automatic `$load $Serial prompt", source)


if __name__ == "__main__":
    unittest.main()
