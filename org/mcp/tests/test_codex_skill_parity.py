"""R5 parity manifest + installer: manifest parsing, skip-missing-source,
templates/references admission, and the read-only --check mode."""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
INSTALL_SCRIPT = REPO_ROOT / "org" / "mcp" / "install-codex-load-skill.py"
MANIFEST_PATH = REPO_ROOT / "org" / "mcp" / "codex-skills" / "PARITY.yaml"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


skill_install = load_module(INSTALL_SCRIPT, "install_codex_load_skill_parity")

BOTH = [
    "closer", "brief-create", "endpoint", "canonical-flow", "to-check", "prd-check",
    "verify", "seams", "handoff", "open-calls", "next-calls", "log",
]
CLAUDE_ONLY = ["dispatch", "canonical-drive", "watcher"]
CODEX_ONLY = ["load"]


def tree_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if path.is_file():
            digest.update(path.relative_to(root).as_posix().encode("utf-8") + b"\0")
            digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def skill_md(name: str) -> str:
    return f'---\nname: {name}\ndescription: "fixture skill {name}"\n---\n\n# {name}\n'


class Fixture:
    """A throwaway workspace carrying its own PARITY.yaml and skill sources."""

    def __init__(self, root: Path):
        self.root = root
        self.home = root / "codex-home"
        self.rows: list[str] = []

    def skill(self, source: str, name: str, extra: dict[str, str] | None = None,
              openai: bool = False) -> Path:
        directory = self.root / source
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "SKILL.md").write_text(skill_md(name), encoding="utf-8")
        if openai:
            (directory / "agents").mkdir(exist_ok=True)
            (directory / "agents" / "openai.yaml").write_text("interface: {}\n", encoding="utf-8")
        for relative, text in (extra or {}).items():
            path = directory / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return directory

    def row(self, text: str) -> None:
        self.rows.append(text)

    def write_manifest(self) -> None:
        path = self.root / skill_install.MANIFEST
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("version: 1\nskills:\n" + "".join(self.rows), encoding="utf-8")


def standard_fixture(root: Path) -> Fixture:
    fixture = Fixture(root)
    fixture.skill("org/mcp/codex-skills/load", "load", openai=True)
    fixture.row("  - name: load\n    source: org/mcp/codex-skills/load\n"
                "    runtime: codex\n    required: true\n    equivalent: \"none\"\n")
    fixture.skill(".claude/skills/alpha", "alpha", extra={
        "templates/card.md": "card", "references/deep/ref.md": "ref", "engine.py": "print(1)",
    })
    fixture.row("  - name: alpha\n    source: .claude/skills/alpha\n    runtime: both\n"
                "    not_projected: [engine.py]\n")
    fixture.row("  - name: ghost\n    source: .claude/skills/ghost\n    runtime: both\n")
    fixture.skill(".claude/skills/solo", "solo")
    fixture.row("  - name: solo\n    source: .claude/skills/solo\n    runtime: claude\n"
                "    equivalent: \"direct implementation\"\n")
    fixture.write_manifest()
    return fixture


class ManifestTests(unittest.TestCase):
    def test_repo_manifest_rows_match_the_brief_parity_table(self):
        rows = skill_install.load_manifest(REPO_ROOT)
        by_runtime: dict[str, list[str]] = {}
        for row in rows:
            by_runtime.setdefault(row["runtime"], []).append(row["name"])
        self.assertEqual(sorted(by_runtime["both"]), sorted(BOTH))
        self.assertEqual(sorted(by_runtime["claude"]), sorted(CLAUDE_ONLY))
        self.assertEqual(sorted(by_runtime["codex"]), sorted(CODEX_ONLY))
        names = {row["name"] for row in rows}
        for deferred in ("drive", "02check", "yolo", "opencalls"):
            self.assertNotIn(deferred, names)
        by_name = {row["name"]: row for row in rows}
        self.assertEqual(by_name["log"]["source"], "org/mcp/codex-skills/log")
        self.assertEqual(by_name["open-calls"]["source"], ".claude/skills/open-calls")
        self.assertEqual({n for n in names if by_name[n].get("required")}, {"load", "log"})
        for name in ("verify", "seams"):
            self.assertIn("Call 2(b)", by_name[name]["note"])
            self.assertIn("ANDREW_DIRECT_20260902_230xZ", by_name[name]["note"])
        for name in CLAUDE_ONLY + CODEX_ONLY:
            self.assertTrue(by_name[name]["equivalent"])

    def test_stdlib_parser_agrees_with_pyyaml_when_available(self):
        text = MANIFEST_PATH.read_text(encoding="utf-8")
        try:
            import yaml  # noqa: PLC0415
        except ImportError:
            self.skipTest("PyYAML not importable on this interpreter")
        self.assertEqual(skill_install.parse_manifest(text), yaml.safe_load(text))

    def test_manifest_is_ascii(self):
        raw = MANIFEST_PATH.read_bytes()
        self.assertEqual(len(raw), len(raw.decode("utf-8")))

    def test_malformed_manifests_are_refused(self):
        base = "version: 1\nskills:\n"
        cases = {
            "unquoted colon": base + "  - name: a\n    source: .claude/skills/a\n"
                              "    runtime: both\n    note: x: y\n",
            "unknown key": base + "  - name: a\n    source: .claude/skills/a\n"
                           "    runtime: both\n    colour: red\n",
            "no equivalent": base + "  - name: a\n    source: .claude/skills/a\n    runtime: claude\n",
            "duplicate": base + ("  - name: a\n    source: .claude/skills/a\n    runtime: both\n") * 2,
            "bad source": base + "  - name: a\n    source: elsewhere/a\n    runtime: both\n",
            "name mismatch": base + "  - name: a\n    source: .claude/skills/b\n    runtime: both\n",
            "bad runtime": base + "  - name: a\n    source: .claude/skills/a\n    runtime: all\n",
            "wrong version": "version: 2\nskills:\n  - name: a\n    source: .claude/skills/a\n"
                             "    runtime: both\n",
            "bad escape": base + "  - name: a\n    source: .claude/skills/a\n    runtime: both\n"
                          "    note: \"a\\nb\"\n",
        }
        for label, text in cases.items():
            with self.subTest(case=label):
                with self.assertRaises(skill_install.InstallError):
                    skill_install.validate_manifest(skill_install.parse_manifest(text))

    def test_quoted_and_list_values_parse(self):
        text = ('version: 1\nskills:\n  - name: a\n    source: .claude/skills/a\n'
                '    runtime: both\n    note: "x: \\"y\\" \\\\ z"\n    not_projected: [p.py, q.py]\n')
        row = skill_install.parse_manifest(text)["skills"][0]
        self.assertEqual(row["note"], 'x: "y" \\ z')
        self.assertEqual(row["not_projected"], ["p.py", "q.py"])


class InstallTests(unittest.TestCase):
    def test_missing_optional_source_is_skipped_not_fatal(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            receipt = skill_install.install_all(fixture.root, fixture.home)
            self.assertEqual([item["skill"] for item in receipt["skills"]], ["load", "alpha"])
            self.assertEqual([item["skill"] for item in receipt["skipped"]], ["ghost"])
            self.assertIn("source absent", receipt["skipped"][0]["reason"])
            self.assertFalse((fixture.home / "skills" / "ghost").exists())
            self.assertFalse((fixture.home / "skills" / "solo").exists())

    def test_missing_required_source_fails(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            (fixture.root / "org/mcp/codex-skills/load/agents/openai.yaml").unlink()
            with self.assertRaisesRegex(skill_install.InstallError, "load: .*incomplete"):
                skill_install.install_all(fixture.root, fixture.home)

    def test_templates_and_references_are_admitted_byte_exactly(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            receipt = skill_install.install(fixture.root, fixture.home, "alpha")
            self.assertEqual(
                receipt["changed"],
                ["SKILL.md", "references/deep/ref.md", "templates/card.md"],
            )
            target = fixture.home / "skills" / "alpha"
            source = fixture.root / ".claude/skills/alpha"
            for relative in receipt["changed"]:
                self.assertEqual((target / relative).read_bytes(), (source / relative).read_bytes())
            self.assertFalse((target / "engine.py").exists())  # not_projected
            again = skill_install.install(fixture.root, fixture.home, "alpha")
            self.assertEqual(again["changed"], [])

    def test_undeclared_extra_file_skips_an_optional_row(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            (fixture.root / ".claude/skills/alpha/stray.py").write_text("x", encoding="utf-8")
            with self.assertRaisesRegex(skill_install.InstallError, "unexpected canonical skill shape"):
                skill_install.install(fixture.root, fixture.home, "alpha")
            receipt = skill_install.install_all(fixture.root, fixture.home)
            self.assertIn("alpha", [item["skill"] for item in receipt["skipped"]])
            self.assertIn("load", [item["skill"] for item in receipt["skills"]])

    def test_frontmatter_name_must_match_the_row(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            (fixture.root / ".claude/skills/alpha/SKILL.md").write_text("# no frontmatter\n", encoding="utf-8")
            receipt = skill_install.install_all(fixture.root, fixture.home)
            reasons = {item["skill"]: item["reason"] for item in receipt["skipped"]}
            self.assertIn("frontmatter name", reasons["alpha"])

    def test_claude_only_row_is_never_installed(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            with self.assertRaisesRegex(skill_install.InstallError, "not projected"):
                skill_install.install(fixture.root, fixture.home, "solo")

    def test_cli_quiet_prints_skip_on_stdout_and_nothing_on_stderr(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            completed = subprocess.run(
                [sys.executable, str(INSTALL_SCRIPT), "--workspace", str(fixture.root),
                 "--codex-home", str(fixture.home), "--format", "quiet"],
                check=False, capture_output=True, text=True,
            )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stderr, "")
        self.assertEqual(completed.stdout.strip(), "SKIP: ghost: source absent: .claude/skills/ghost")


class CheckTests(unittest.TestCase):
    def run_check(self, fixture: Fixture) -> tuple[int, str]:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            code = skill_install.main(["--workspace", str(fixture.root),
                                       "--codex-home", str(fixture.home), "--check"])
        return code, buffer.getvalue()

    def test_check_writes_nothing_and_does_not_create_codex_home(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            before = tree_digest(fixture.root)
            code, output = self.run_check(fixture)
            self.assertEqual(code, 0)
            self.assertEqual(tree_digest(fixture.root), before)
            self.assertFalse(fixture.home.exists())
            self.assertIn("WARN: load not installed", output)
            self.assertIn("SKIP: ghost source absent", output)
            self.assertIn("SKIP: solo runtime=claude not projected; codex uses: direct implementation", output)
            self.assertIn("check: rows=4", output)

    def test_check_reports_in_sync_then_each_drift_kind_read_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            fixture = standard_fixture(Path(temporary))
            skill_install.install_all(fixture.root, fixture.home)
            code, output = self.run_check(fixture)
            self.assertEqual(code, 0)
            self.assertIn("OK: alpha in sync (3 files)", output)
            self.assertIn("OK: load in sync (2 files)", output)

            target = fixture.home / "skills" / "alpha"
            (target / "SKILL.md").write_text("edited", encoding="utf-8")
            (target / "templates" / "card.md").unlink()
            (target / "templates" / "old.md").write_text("stale", encoding="utf-8")
            before = tree_digest(fixture.home)
            report = skill_install.check(fixture.root, fixture.home)
            self.assertEqual(tree_digest(fixture.home), before)
            alpha = next(item for item in report["skills"] if item["skill"] == "alpha")
            self.assertEqual(alpha["status"], "drift")
            self.assertEqual(alpha["changed"], ["SKILL.md"])
            self.assertEqual(alpha["missing"], ["templates/card.md"])
            self.assertEqual(alpha["stale"], ["templates/old.md"])

    def test_check_is_clean_against_the_repo_manifest_after_a_temp_install(self):
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary) / "codex-home"
            receipt = skill_install.install_all(REPO_ROOT, home)
            report = skill_install.check(REPO_ROOT, home)
        installed = {item["skill"] for item in receipt["skills"]}
        skipped = {item["skill"] for item in receipt["skipped"]}
        self.assertTrue({"load", "log"} <= installed)
        self.assertEqual(installed | skipped, set(BOTH + CODEX_ONLY))
        statuses = {item["skill"]: item["status"] for item in report["skills"]}
        for name in installed:
            self.assertEqual(statuses[name], "in-sync", name)
        for name in skipped:
            self.assertIn(statuses[name], ("source-absent", "source-invalid"), name)


if __name__ == "__main__":
    unittest.main()
