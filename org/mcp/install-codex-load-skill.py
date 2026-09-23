#!/usr/bin/env python3
"""Install repository-owned skills into Codex as byte-exact personal projections.

The filename is retained for launcher and operator compatibility. The skill set is
the parity manifest ``org/mcp/codex-skills/PARITY.yaml``: every row whose runtime is
``both`` or ``codex`` is projected into ``CODEX_HOME/skills/<name>``. A row marked
``required: true`` (load, log) fails the install when its source is missing or
malformed, exactly as before; any other row whose source is absent or unusable is
skipped with a ``SKIP:`` line on stdout and the install continues, because this runs
at every Codex seat launch. ``--check`` prints per-skill drift and writes nothing.
The public ``install`` function still defaults to ``load``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path


MANIFEST = Path("org/mcp/codex-skills/PARITY.yaml")
# The Codex-native minimum shape; a required row must carry both files.
EXPECTED_FILES = (Path("SKILL.md"), Path("agents/openai.yaml"))
ADMITTED_FILES = frozenset(EXPECTED_FILES)
ADMITTED_SUBTREES = ("templates", "references")
RUNTIMES = ("both", "claude", "codex")
PROJECTED_RUNTIMES = ("both", "codex")
SOURCE_ROOTS = (".claude/skills/", "org/mcp/codex-skills/")
ROW_KEYS = frozenset(
    {"name", "source", "runtime", "equivalent", "required", "not_projected", "note"}
)
_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_KEY = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:[ ](.*)|)$")
_INT = re.compile(r"^-?[0-9]+$")


class InstallError(ValueError):
    """The skill projection cannot be installed safely."""


# ---------------------------------------------------------------- manifest


def _scalar(value: str, lineno: int) -> object:
    """Parse one value of the manifest's restricted YAML subset."""
    if value.startswith('"'):
        if len(value) < 2 or not value.endswith('"'):
            raise InstallError(f"manifest line {lineno}: unterminated quoted string")
        body, out, index = value[1:-1], [], 0
        while index < len(body):
            char = body[index]
            if char == "\\":
                if index + 1 >= len(body) or body[index + 1] not in '"\\':
                    raise InstallError(
                        f"manifest line {lineno}: only \\\" and \\\\ escapes are supported"
                    )
                out.append(body[index + 1])
                index += 2
                continue
            if char == '"':
                raise InstallError(f"manifest line {lineno}: unescaped quote in string")
            out.append(char)
            index += 1
        return "".join(out)
    if value.startswith("["):
        if not value.endswith("]"):
            raise InstallError(f"manifest line {lineno}: unterminated flow list")
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_plain(item.strip(), lineno) for item in inner.split(",")]
    if value == "true":
        return True
    if value == "false":
        return False
    if _INT.match(value):
        return int(value)
    return _plain(value, lineno)


def _plain(value: str, lineno: int) -> str:
    if (
        not value
        or value[0] in "'\"&*!|>%@`{}[],#?:-"
        or ": " in value
        or " #" in value
        or value in ("null", "~", "yes", "no", "on", "off", "True", "False")
    ):
        raise InstallError(
            f"manifest line {lineno}: value {value!r} must be double-quoted"
        )
    return value


def parse_manifest(text: str) -> dict[str, object]:
    """Parse PARITY.yaml without PyYAML (absent on some interpreters).

    Accepts top-level ``key: value`` pairs and one ``skills:`` block list of flat
    mappings. Anything outside that subset is refused rather than guessed.
    """
    top: dict[str, object] = {}
    skills: list[dict[str, object]] | None = None
    current: dict[str, object] | None = None
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        stripped = line.lstrip(" ")
        if not stripped or stripped.startswith("#"):
            continue
        if "\t" in line[: len(line) - len(stripped)]:
            raise InstallError(f"manifest line {lineno}: tab indentation")
        indent = len(line) - len(stripped)
        if indent == 0:
            match = _KEY.match(stripped)
            if not match:
                raise InstallError(f"manifest line {lineno}: expected 'key: value'")
            key, value = match.group(1), (match.group(2) or "").strip()
            if key in top:
                raise InstallError(f"manifest line {lineno}: duplicate key {key}")
            if key == "skills":
                if value:
                    raise InstallError(f"manifest line {lineno}: skills must be a block list")
                skills, current = [], None
                top[key] = skills
            else:
                if not value:
                    raise InstallError(f"manifest line {lineno}: empty value for {key}")
                top[key] = _scalar(value, lineno)
                skills, current = None, None
            continue
        if skills is None:
            raise InstallError(f"manifest line {lineno}: indented line outside skills")
        if stripped.startswith("- "):
            current = {}
            skills.append(current)
            stripped = stripped[2:].lstrip(" ")
        elif current is None:
            raise InstallError(f"manifest line {lineno}: expected '- ' list item")
        match = _KEY.match(stripped)
        if not match or not (match.group(2) or "").strip():
            raise InstallError(f"manifest line {lineno}: expected 'key: value'")
        key, value = match.group(1), match.group(2).strip()
        if key in current:
            raise InstallError(f"manifest line {lineno}: duplicate key {key}")
        current[key] = _scalar(value, lineno)
    return top


def validate_manifest(data: dict[str, object]) -> list[dict[str, object]]:
    if data.get("version") != 1:
        raise InstallError("manifest version must be 1")
    rows = data.get("skills")
    if not isinstance(rows, list) or not rows:
        raise InstallError("manifest has no skills")
    seen: set[str] = set()
    for row in rows:
        name = row.get("name")
        label = name if isinstance(name, str) else repr(name)
        unknown = sorted(set(row) - ROW_KEYS)
        if unknown:
            raise InstallError(f"manifest row {label}: unknown keys {unknown}")
        if not isinstance(name, str) or not _NAME.match(name) or len(name) > 64:
            raise InstallError(f"manifest row {label}: name must be hyphen-case")
        if name in seen:
            raise InstallError(f"manifest row {name}: duplicate name")
        seen.add(name)
        source = row.get("source")
        if (
            not isinstance(source, str)
            or not source.startswith(SOURCE_ROOTS)
            or "\\" in source
            or ".." in source.split("/")
            or source.rstrip("/").split("/")[-1] != name
        ):
            raise InstallError(
                f"manifest row {name}: source must be .claude/skills/{name} "
                f"or org/mcp/codex-skills/{name}"
            )
        runtime = row.get("runtime")
        if runtime not in RUNTIMES:
            raise InstallError(f"manifest row {name}: runtime must be one of {RUNTIMES}")
        equivalent = row.get("equivalent")
        if runtime != "both" and not (isinstance(equivalent, str) and equivalent):
            raise InstallError(f"manifest row {name}: single-runtime row needs equivalent")
        if equivalent is not None and not isinstance(equivalent, str):
            raise InstallError(f"manifest row {name}: equivalent must be a string")
        required = row.get("required", False)
        if not isinstance(required, bool):
            raise InstallError(f"manifest row {name}: required must be true or false")
        if required and runtime not in PROJECTED_RUNTIMES:
            raise InstallError(f"manifest row {name}: only a projected row can be required")
        excluded = row.get("not_projected", [])
        if not isinstance(excluded, list) or not all(
            isinstance(item, str) and item for item in excluded
        ):
            raise InstallError(f"manifest row {name}: not_projected must be a list")
        if "note" in row and not isinstance(row["note"], str):
            raise InstallError(f"manifest row {name}: note must be a string")
    return rows


def load_manifest(workspace: Path) -> list[dict[str, object]]:
    path = workspace / MANIFEST
    if not path.is_file():
        raise InstallError(f"parity manifest not found: {path}")
    return validate_manifest(parse_manifest(path.read_text(encoding="utf-8")))


def projected_rows(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    return [row for row in rows if row["runtime"] in PROJECTED_RUNTIMES]


def _row(rows: list[dict[str, object]], skill_name: str) -> dict[str, object]:
    for row in rows:
        if row["name"] == skill_name:
            if row["runtime"] not in PROJECTED_RUNTIMES:
                raise InstallError(
                    f"skill {skill_name} is runtime {row['runtime']}, not projected into Codex"
                )
            return row
    raise InstallError(f"unknown canonical skill: {skill_name}")


# ---------------------------------------------------------------- shape


def _digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _files(root: Path) -> set[Path]:
    return {
        item.relative_to(root)
        for item in root.rglob("*")
        if item.is_file() and "__pycache__" not in item.parts
    }


def _admitted(relative: Path) -> bool:
    return relative in ADMITTED_FILES or (
        len(relative.parts) >= 2 and relative.parts[0] in ADMITTED_SUBTREES
    )


def _frontmatter_name(skill_md: Path) -> str | None:
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for line in lines[1:]:
        if line.strip() == "---":
            return None
        if line.startswith("name:"):
            return line[len("name:"):].strip().strip("\"'")
    return None


def source_shape(workspace: Path, row: dict[str, object]) -> tuple[Path, list[Path]]:
    """Return the source directory and the sorted files that project into Codex."""
    name = str(row["name"])
    source = workspace / str(row["source"])
    if not source.is_dir():
        raise InstallError(f"source absent: {row['source']}")
    required = EXPECTED_FILES if row.get("required") else (Path("SKILL.md"),)
    missing = [str(item) for item in required if not (source / item).is_file()]
    if missing:
        raise InstallError("canonical skill is incomplete: " + ", ".join(missing))
    excluded = {Path(item) for item in row.get("not_projected", [])}
    present = _files(source)
    absent_exclusions = sorted(str(item) for item in excluded - present)
    if absent_exclusions:
        raise InstallError(f"not_projected files absent from source: {absent_exclusions}")
    projected = present - excluded
    extra = sorted(str(item) for item in projected if not _admitted(item))
    if extra:
        raise InstallError(f"unexpected canonical skill shape; extra={extra}, missing=[]")
    declared = _frontmatter_name(source / "SKILL.md")
    if declared != name:
        raise InstallError(
            f"SKILL.md frontmatter name is {declared!r}, manifest name is {name!r}"
        )
    return source, sorted(projected, key=lambda item: item.as_posix())


# ---------------------------------------------------------------- install


def _copy_verified(source_file: Path, target_file: Path) -> None:
    target_file.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="wb", dir=target_file.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(source_file.read_bytes())
    try:
        temporary.replace(target_file)
    finally:
        temporary.unlink(missing_ok=True)
    if _digest(target_file) != _digest(source_file):
        raise InstallError(f"sha256 mismatch after copy: {target_file}")


def install(
    workspace: Path,
    codex_home: Path,
    skill_name: str = "load",
    rows: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    workspace = workspace.resolve()
    if rows is None:
        rows = load_manifest(workspace)
    row = _row(rows, skill_name)
    source, files = source_shape(workspace, row)
    target = codex_home.expanduser().resolve() / "skills" / skill_name

    if target.is_dir():
        unexpected = sorted(str(item) for item in _files(target) - set(files))
        if unexpected:
            raise InstallError(
                f"refusing to overwrite the {skill_name} skill with unexpected files: "
                + ", ".join(unexpected)
            )

    changed: list[str] = []
    for relative in files:
        source_file = source / relative
        target_file = target / relative
        if target_file.is_file() and _digest(target_file) == _digest(source_file):
            continue
        _copy_verified(source_file, target_file)
        changed.append(relative.as_posix())

    return {
        "document_kind": "codex_skill_install_receipt",
        "skill": skill_name,
        "source": str(source),
        "target": str(target),
        "changed": changed,
        "files": {relative.as_posix(): _digest(target / relative) for relative in files},
    }


def install_all(workspace: Path, codex_home: Path) -> dict[str, object]:
    workspace = workspace.resolve()
    rows = load_manifest(workspace)
    receipts: list[dict[str, object]] = []
    skipped: list[dict[str, str]] = []
    for row in projected_rows(rows):
        name = str(row["name"])
        try:
            receipts.append(install(workspace, codex_home, name, rows))
        except (OSError, InstallError) as exc:
            if row.get("required"):
                raise InstallError(f"{name}: {exc}") from exc
            skipped.append({"skill": name, "reason": str(exc)})
    return {
        "document_kind": "codex_skill_install_set_receipt",
        "manifest": MANIFEST.as_posix(),
        "skills": receipts,
        "skipped": skipped,
    }


# ---------------------------------------------------------------- check


def check(workspace: Path, codex_home: Path) -> dict[str, object]:
    """Compare every manifest row with its installed projection. Writes nothing."""
    workspace = workspace.resolve()
    rows = load_manifest(workspace)
    skills_root = codex_home.expanduser().resolve() / "skills"
    results: list[dict[str, object]] = []
    for row in rows:
        name = str(row["name"])
        entry: dict[str, object] = {"skill": name, "runtime": row["runtime"]}
        results.append(entry)
        if row["runtime"] not in PROJECTED_RUNTIMES:
            entry.update(status="not-projected", equivalent=row.get("equivalent", ""))
            continue
        try:
            source, files = source_shape(workspace, row)
        except (OSError, InstallError) as exc:
            absent = not (workspace / str(row["source"])).is_dir()
            entry.update(status="source-absent" if absent else "source-invalid", reason=str(exc))
            continue
        target = skills_root / name
        if not target.is_dir():
            entry.update(status="not-installed", files=len(files))
            continue
        installed = _files(target)
        expected = set(files)
        changed = sorted(
            item.as_posix()
            for item in expected & installed
            if _digest(target / item) != _digest(source / item)
        )
        missing = sorted(item.as_posix() for item in expected - installed)
        stale = sorted(item.as_posix() for item in installed - expected)
        drift = bool(changed or missing or stale)
        entry.update(
            status="drift" if drift else "in-sync",
            files=len(files),
            changed=changed,
            missing=missing,
            stale=stale,
        )
    counts: dict[str, int] = {}
    for entry in results:
        counts[str(entry["status"])] = counts.get(str(entry["status"]), 0) + 1
    return {
        "document_kind": "codex_skill_parity_check",
        "manifest": MANIFEST.as_posix(),
        "codex_home": str(codex_home.expanduser().resolve()),
        "rows": len(results),
        "counts": counts,
        "skills": results,
    }


def render_check(report: dict[str, object]) -> list[str]:
    lines: list[str] = []
    for entry in report["skills"]:
        name, status = entry["skill"], entry["status"]
        if status == "in-sync":
            lines.append(f"OK: {name} in sync ({entry['files']} files)")
        elif status == "drift":
            lines.append(
                f"WARN: {name} drift: changed={entry['changed']} "
                f"missing={entry['missing']} stale={entry['stale']}"
            )
        elif status == "not-installed":
            lines.append(f"WARN: {name} not installed ({entry['files']} source files)")
        elif status == "source-absent":
            lines.append(f"SKIP: {name} {entry['reason']}")
        elif status == "source-invalid":
            lines.append(f"WARN: {name} source invalid: {entry['reason']}")
        else:
            lines.append(
                f"SKIP: {name} runtime={entry['runtime']} not projected; "
                f"codex uses: {entry['equivalent']}"
            )
    summary = " ".join(f"{key}={value}" for key, value in sorted(report["counts"].items()))
    lines.append(
        f"check: rows={report['rows']} {summary} "
        f"(manifest {report['manifest']}; codex_home {report['codex_home']})"
    )
    return lines


# ---------------------------------------------------------------- cli


def _ascii(line: str) -> str:
    return line.encode("ascii", "replace").decode("ascii")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=os.getcwd())
    parser.add_argument("--codex-home", help="target CODEX_HOME (default: $CODEX_HOME, then ~/.codex)")
    parser.add_argument("--format", choices=("json", "quiet", "text"))
    parser.add_argument(
        "--check", action="store_true", help="print per-skill drift against CODEX_HOME; write nothing"
    )
    args = parser.parse_args(argv)

    configured_home = args.codex_home or os.environ.get("CODEX_HOME")
    codex_home = Path(configured_home) if configured_home else Path.home() / ".codex"
    try:
        if args.check:
            report = check(Path(args.workspace), codex_home)
        else:
            receipt = install_all(Path(args.workspace), codex_home)
    except (OSError, InstallError) as exc:
        print(_ascii(f"ERROR: install-codex-skills: {exc}"), file=sys.stderr)
        return 2

    if args.check:
        if args.format == "json":
            print(json.dumps(report, indent=2, sort_keys=True))
        else:
            for line in render_check(report):
                print(_ascii(line))
        return 0
    if args.format in (None, "json"):
        print(json.dumps(receipt, indent=2, sort_keys=True))
    else:
        # stdout, never stderr: the launcher runs this under PowerShell with
        # ErrorActionPreference Stop and 2>&1, where any stderr line throws.
        for item in receipt["skipped"]:
            print(_ascii(f"SKIP: {item['skill']}: {item['reason']}"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
