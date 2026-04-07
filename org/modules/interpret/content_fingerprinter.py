"""
In: Interpret -- Content Fingerprinter (D-mode).

Classifies files by extension into 5 archetypal groups.
Works on any directory, any codebase, any client dump.
No assumptions about directory structure or naming conventions.

Groups:
  DOCUMENT  — human-readable prose (md, txt, rst, doc, pdf, html)
  DATA      — structured data (json, yaml, yml, csv, tsv, xml, toml, parquet, sql)
  CODE      — executable source (py, js, ts, go, rs, java, c, cpp, sh, bash, rb, php)
  CONFIG    — environment/build config (env, ini, cfg, conf, dockerfile, makefile, gitignore, lock)
  ASSET     — binary/media (png, jpg, gif, svg, ico, woff, ttf, zip, tar, gz, whl, exe, dll)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .. import ModuleOutput

# ---------------------------------------------------------------------------
# Extension -> group mapping
# ---------------------------------------------------------------------------

_GROUP: dict[str, str] = {}

_DOCUMENT_EXTS = (
    ".md", ".txt", ".rst", ".adoc", ".tex", ".rtf",
    ".doc", ".docx", ".pdf", ".html", ".htm", ".xhtml",
    ".org", ".wiki", ".man",
)
_DATA_EXTS = (
    ".json", ".yaml", ".yml", ".csv", ".tsv", ".xml",
    ".toml", ".parquet", ".avro", ".arrow", ".sql",
    ".sqlite", ".db", ".ndjson", ".jsonl", ".geojson",
    ".xls", ".xlsx", ".ods", ".pkl", ".pickle",
)
_CODE_EXTS = (
    ".py", ".js", ".ts", ".jsx", ".tsx", ".go", ".rs",
    ".java", ".c", ".cpp", ".h", ".hpp", ".cs", ".rb",
    ".php", ".swift", ".kt", ".scala", ".r", ".m",
    ".sh", ".bash", ".zsh", ".fish", ".ps1", ".bat", ".cmd",
    ".lua", ".pl", ".pm", ".ex", ".exs", ".erl", ".hs",
    ".clj", ".lisp", ".el", ".vim", ".zig", ".nim",
    ".ipynb", ".sql",
)
_CONFIG_EXTS = (
    ".env", ".ini", ".cfg", ".conf", ".config",
    ".properties", ".editorconfig", ".prettierrc",
    ".eslintrc", ".babelrc", ".npmrc", ".yarnrc",
    ".gitignore", ".gitattributes", ".dockerignore",
    ".lock", ".sum",
)
_ASSET_EXTS = (
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
    ".bmp", ".webp", ".tiff", ".psd",
    ".woff", ".woff2", ".ttf", ".otf", ".eot",
    ".mp3", ".mp4", ".wav", ".ogg", ".webm", ".avi",
    ".zip", ".tar", ".gz", ".bz2", ".xz", ".7z", ".rar",
    ".whl", ".egg", ".jar", ".war",
    ".exe", ".dll", ".so", ".dylib", ".bin", ".o", ".a",
)

for _ext in _DOCUMENT_EXTS:
    _GROUP[_ext] = "DOCUMENT"
for _ext in _DATA_EXTS:
    _GROUP[_ext] = "DATA"
for _ext in _CODE_EXTS:
    _GROUP[_ext] = "CODE"
for _ext in _CONFIG_EXTS:
    _GROUP[_ext] = "CONFIG"
for _ext in _ASSET_EXTS:
    _GROUP[_ext] = "ASSET"

# Special filenames (no extension or non-standard)
_NAME_GROUP: dict[str, str] = {
    "dockerfile": "CONFIG",
    "makefile": "CONFIG",
    "cmakelists.txt": "CONFIG",
    "rakefile": "CONFIG",
    "gemfile": "CONFIG",
    "procfile": "CONFIG",
    "vagrantfile": "CONFIG",
    "jenkinsfile": "CONFIG",
    "license": "DOCUMENT",
    "readme": "DOCUMENT",
    "changelog": "DOCUMENT",
    "authors": "DOCUMENT",
    "contributing": "DOCUMENT",
    "requirements.txt": "CONFIG",
    "package.json": "CONFIG",
    "tsconfig.json": "CONFIG",
    "pyproject.toml": "CONFIG",
    "setup.py": "CONFIG",
    "setup.cfg": "CONFIG",
    "cargo.toml": "CONFIG",
    "go.mod": "CONFIG",
    "go.sum": "CONFIG",
    "composer.json": "CONFIG",
}


@dataclass
class FileFingerprint:
    """What we know about a file from extension + name alone."""
    path: str
    filename: str
    extension: str
    group: str          # DOCUMENT, DATA, CODE, CONFIG, ASSET, UNKNOWN
    is_binary: bool     # ASSET group = likely binary


def fingerprint(file_path: Path) -> FileFingerprint:
    """Classify a single file by extension and name."""
    ext = file_path.suffix.lower()
    name = file_path.name.lower()
    stem = file_path.stem.lower()

    # Try extension first
    group = _GROUP.get(ext, "")

    # Try special filenames
    if not group:
        group = _NAME_GROUP.get(name, "")
    if not group:
        group = _NAME_GROUP.get(stem, "")

    if not group:
        group = "UNKNOWN"

    return FileFingerprint(
        path=str(file_path),
        filename=file_path.name,
        extension=ext,
        group=group,
        is_binary=(group == "ASSET"),
    )


def execute(inputs: dict, config: dict) -> ModuleOutput:
    """Fingerprint all files from Pe stage.

    Inputs: pe_output (list of FileMetadata from filesystem_scanner)
    """
    from ..perceive.filesystem_scanner import FileMetadata
    pe_output: list[FileMetadata] = inputs.get("pe_output", [])

    results = [fingerprint(Path(m.path)) for m in pe_output]

    counts: dict[str, int] = {}
    for r in results:
        counts[r.group] = counts.get(r.group, 0) + 1

    return ModuleOutput(
        data=results,
        confident=results,
        ambiguous=[],
        mode="D",
        stage="In",
        stats={"total": len(results), "by_group": counts},
    )
