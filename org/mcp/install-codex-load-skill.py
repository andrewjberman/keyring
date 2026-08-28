#!/usr/bin/env python3
"""Install repository-owned Codex skills as byte-exact personal projections.

The filename is retained for launcher and operator compatibility. The CLI installs every
canonical skill; the public ``install`` function still defaults to ``load`` for callers that
exercise one projection directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path


EXPECTED_FILES = (Path("SKILL.md"), Path("agents/openai.yaml"))
CANONICAL_SKILLS = ("load", "log")


class InstallError(ValueError):
    """The skill projection cannot be installed safely."""


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def install(
    workspace: Path, codex_home: Path, skill_name: str = "load"
) -> dict[str, object]:
    workspace = workspace.resolve()
    if skill_name not in CANONICAL_SKILLS:
        raise InstallError(f"unknown canonical skill: {skill_name}")
    source = workspace / "org" / "mcp" / "codex-skills" / skill_name
    target = codex_home.expanduser().resolve() / "skills" / skill_name

    missing = [str(item) for item in EXPECTED_FILES if not (source / item).is_file()]
    if missing:
        raise InstallError("canonical skill is incomplete: " + ", ".join(missing))

    source_files = {
        item.relative_to(source)
        for item in source.rglob("*")
        if item.is_file() and "__pycache__" not in item.parts
    }
    expected = set(EXPECTED_FILES)
    if source_files != expected:
        extra = sorted(str(item) for item in source_files - expected)
        absent = sorted(str(item) for item in expected - source_files)
        raise InstallError(f"unexpected canonical skill shape; extra={extra}, missing={absent}")

    target.mkdir(parents=True, exist_ok=True)
    target_files = {
        item.relative_to(target)
        for item in target.rglob("*")
        if item.is_file() and "__pycache__" not in item.parts
    }
    unexpected = sorted(str(item) for item in target_files - expected)
    if unexpected:
        raise InstallError(
            f"refusing to overwrite the {skill_name} skill with unexpected files: "
            + ", ".join(unexpected)
        )

    changed: list[str] = []
    for relative in EXPECTED_FILES:
        source_file = source / relative
        target_file = target / relative
        target_file.parent.mkdir(parents=True, exist_ok=True)
        if target_file.is_file() and _digest(target_file) == _digest(source_file):
            continue
        with tempfile.NamedTemporaryFile(
            mode="wb", dir=target_file.parent, delete=False
        ) as handle:
            temporary = Path(handle.name)
            handle.write(source_file.read_bytes())
        try:
            temporary.replace(target_file)
        finally:
            temporary.unlink(missing_ok=True)
        changed.append(relative.as_posix())

    return {
        "document_kind": "codex_skill_install_receipt",
        "skill": skill_name,
        "source": str(source),
        "target": str(target),
        "changed": changed,
        "files": {
            relative.as_posix(): _digest(target / relative)
            for relative in EXPECTED_FILES
        },
    }


def install_all(workspace: Path, codex_home: Path) -> dict[str, object]:
    receipts = [install(workspace, codex_home, name) for name in CANONICAL_SKILLS]
    return {
        "document_kind": "codex_skill_install_set_receipt",
        "skills": receipts,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=os.getcwd())
    parser.add_argument("--codex-home")
    parser.add_argument("--format", choices=("json", "quiet"), default="json")
    args = parser.parse_args(argv)

    configured_home = args.codex_home or os.environ.get("CODEX_HOME")
    codex_home = Path(configured_home) if configured_home else Path.home() / ".codex"
    try:
        receipt = install_all(Path(args.workspace), codex_home)
    except (OSError, InstallError) as exc:
        print(f"install-codex-skills: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
