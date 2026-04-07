"""
In: Interpret -- Corpus Fingerprinter (D-mode).

Extended fingerprinting for unstructured/messy data. Works on any file
type — PDFs, CSVs, XLSX, Python scripts, plain text, binary. Extracts
15-20 signals per file without any LLM involvement.

Complements content_fingerprinter.py (which handles markdown/YAML/JSON
for structured codebases). This module handles the rest.

Spec: ONT.CORE.KF_EXECUTION_MODES Section 3.2 (extended)
"""

from __future__ import annotations

import math
import re
import subprocess
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .. import ModuleOutput
from ..perceive.filesystem_scanner import FileMetadata


@dataclass
class CorpusFingerprint:
    """Extended content signals for any file type."""
    path: str = ""

    # Basic type signals
    mime_type: str = ""              # from file --mime-type
    encoding: str = ""               # utf-8, ascii, binary, unknown
    is_text: bool = False
    is_binary: bool = False

    # Content shape
    char_count: int = 0
    line_count: int = 0
    letter_ratio: float = 0.0       # letters / total chars
    digit_ratio: float = 0.0        # digits / total chars
    whitespace_ratio: float = 0.0
    entropy: float = 0.0            # Shannon entropy of byte distribution

    # Text structure (only for text files)
    has_header_row: bool = False     # First line looks like a CSV/TSV header
    delimiter: str = ""              # Detected delimiter (comma, tab, pipe, semicolon)
    column_count: int = 0            # If delimited, how many columns
    has_paragraphs: bool = False     # Double-newline separated blocks
    paragraph_count: int = 0
    avg_line_length: float = 0.0

    # Code signals
    has_imports: bool = False        # import/require/include statements
    has_functions: bool = False      # def/function/func/fn definitions
    has_classes: bool = False        # class definitions
    language_hint: str = ""          # python, javascript, java, etc.

    # Document signals
    has_yaml_frontmatter: bool = False
    has_markdown_headings: bool = False
    heading_count: int = 0

    # Content samples (for downstream cluster features)
    first_lines: list[str] = field(default_factory=list)   # First 10 lines
    sample_lines: list[str] = field(default_factory=list)   # 5 random lines from middle

    # Derived classification signal
    content_class: str = ""         # narrative, tabular, code, config, binary, mixed


# --- Regex patterns ---
_IMPORT_RE = re.compile(r"^\s*(import |from |require\(|#include |using )", re.MULTILINE)
_FUNC_RE = re.compile(r"^\s*(def |function |func |fn |public |private |protected )", re.MULTILINE)
_CLASS_RE = re.compile(r"^\s*(class |struct |interface |enum )", re.MULTILINE)
_HEADING_RE = re.compile(r"^#{1,6}\s+", re.MULTILINE)
_YAML_FM_RE = re.compile(r"^---\s*\n", re.MULTILINE)
_PARAGRAPH_RE = re.compile(r"\n\s*\n")

# Language detection by extension
_LANG_MAP = {
    ".py": "python", ".js": "javascript", ".ts": "typescript",
    ".java": "java", ".go": "go", ".rs": "rust", ".rb": "ruby",
    ".c": "c", ".cpp": "cpp", ".h": "c_header", ".cs": "csharp",
    ".sh": "bash", ".bash": "bash", ".zsh": "zsh",
    ".sql": "sql", ".r": "r", ".R": "r",
    ".html": "html", ".css": "css", ".xml": "xml",
    ".toml": "toml", ".ini": "ini", ".cfg": "config",
}

# Delimiter detection
_DELIMITERS = [(",", "comma"), ("\t", "tab"), ("|", "pipe"), (";", "semicolon")]


def _detect_mime(file_path: Path) -> str:
    """Detect MIME type using file command (available in Linux/Docker)."""
    try:
        result = subprocess.run(
            ["file", "--mime-type", "-b", str(file_path)],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    # Fallback by extension
    ext = file_path.suffix.lower()
    fallback = {
        ".pdf": "application/pdf", ".csv": "text/csv",
        ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        ".xls": "application/vnd.ms-excel",
        ".doc": "application/msword",
        ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ".ppt": "application/vnd.ms-powerpoint",
        ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ".png": "image/png", ".jpg": "image/jpeg", ".gif": "image/gif",
        ".zip": "application/zip", ".tar": "application/x-tar",
        ".gz": "application/gzip",
    }
    return fallback.get(ext, "application/octet-stream")


def _shannon_entropy(data: bytes) -> float:
    """Calculate Shannon entropy of byte distribution."""
    if not data:
        return 0.0
    freq = Counter(data)
    length = len(data)
    return -sum(
        (count / length) * math.log2(count / length)
        for count in freq.values()
    )


def _detect_delimiter(lines: list[str]) -> tuple[str, str, int]:
    """Detect the most likely delimiter from first 10 lines.

    Returns (delimiter_char, delimiter_name, column_count).
    """
    if len(lines) < 2:
        return "", "", 0

    best_delim = ""
    best_name = ""
    best_consistency = 0
    best_cols = 0

    for delim, name in _DELIMITERS:
        counts = [line.count(delim) for line in lines[:10] if line.strip()]
        if not counts or max(counts) == 0:
            continue
        # Consistency: how uniform are the column counts?
        col_count = counts[0] + 1
        consistent = sum(1 for c in counts if c + 1 == col_count)
        consistency = consistent / len(counts)
        if consistency > best_consistency and col_count >= 2:
            best_consistency = consistency
            best_delim = delim
            best_name = name
            best_cols = col_count

    if best_consistency >= 0.7:
        return best_delim, best_name, best_cols
    return "", "", 0


def _detect_header(first_line: str, delimiter: str) -> bool:
    """Check if the first line looks like a CSV/TSV header."""
    if not delimiter or not first_line:
        return False
    fields = first_line.split(delimiter)
    # Headers tend to be short strings without digits
    alpha_fields = sum(1 for f in fields if f.strip().isalpha() or "_" in f.strip())
    return alpha_fields / max(len(fields), 1) >= 0.6


def fingerprint_file(file_path: Path) -> CorpusFingerprint:
    """Extract extended fingerprint from any file type."""
    fp = CorpusFingerprint(path=str(file_path))

    # MIME type
    fp.mime_type = _detect_mime(file_path)
    fp.is_binary = not fp.mime_type.startswith("text/") and fp.mime_type not in (
        "application/json", "application/xml", "application/javascript",
    )

    # Read raw bytes for entropy
    try:
        raw = file_path.read_bytes()
        fp.entropy = _shannon_entropy(raw[:10000])  # First 10KB
    except Exception:
        raw = b""

    # Language hint from extension
    fp.language_hint = _LANG_MAP.get(file_path.suffix.lower(), "")

    # For binary files, we're done with content analysis
    if fp.is_binary:
        fp.content_class = "binary"
        fp.char_count = len(raw)
        return fp

    # Read as text
    try:
        content = file_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        fp.is_binary = True
        fp.content_class = "binary"
        return fp

    fp.is_text = True
    fp.encoding = "utf-8"
    fp.char_count = len(content)

    lines = content.split("\n")
    fp.line_count = len(lines)
    fp.first_lines = [l.rstrip() for l in lines[:10]]

    # Sample from middle
    if len(lines) > 20:
        import random
        mid = lines[len(lines) // 4 : 3 * len(lines) // 4]
        fp.sample_lines = random.sample(mid, min(5, len(mid)))
    else:
        fp.sample_lines = lines[:5]

    # Character ratios
    if fp.char_count > 0:
        letters = sum(1 for c in content if c.isalpha())
        digits = sum(1 for c in content if c.isdigit())
        whites = sum(1 for c in content if c.isspace())
        fp.letter_ratio = letters / fp.char_count
        fp.digit_ratio = digits / fp.char_count
        fp.whitespace_ratio = whites / fp.char_count

    # Line length stats
    non_empty = [len(l) for l in lines if l.strip()]
    fp.avg_line_length = sum(non_empty) / max(len(non_empty), 1)

    # Delimiter detection
    delim, delim_name, col_count = _detect_delimiter(lines)
    fp.delimiter = delim_name
    fp.column_count = col_count
    if delim:
        fp.has_header_row = _detect_header(lines[0] if lines else "", delim)

    # Paragraph detection
    paragraphs = _PARAGRAPH_RE.split(content)
    fp.paragraph_count = len([p for p in paragraphs if p.strip()])
    fp.has_paragraphs = fp.paragraph_count >= 3

    # Code signals
    fp.has_imports = bool(_IMPORT_RE.search(content))
    fp.has_functions = bool(_FUNC_RE.search(content))
    fp.has_classes = bool(_CLASS_RE.search(content))

    # Markdown signals
    fp.has_markdown_headings = bool(_HEADING_RE.search(content))
    fp.heading_count = len(_HEADING_RE.findall(content))

    # YAML frontmatter
    fp.has_yaml_frontmatter = content.startswith("---\n")

    # Derive content class
    fp.content_class = _classify_content(fp)

    return fp


def _classify_content(fp: CorpusFingerprint) -> str:
    """Derive a high-level content class from signals."""
    if fp.is_binary:
        return "binary"

    # Code
    if fp.has_functions or fp.has_classes or (fp.has_imports and fp.language_hint):
        return "code"

    # Tabular data
    if fp.delimiter and fp.column_count >= 2:
        return "tabular"

    # Configuration (YAML/TOML/INI without prose)
    if fp.language_hint in ("toml", "ini", "config") or (
        fp.has_yaml_frontmatter and not fp.has_paragraphs
    ):
        return "config"

    # Narrative prose
    if fp.has_paragraphs and fp.letter_ratio > 0.5 and fp.avg_line_length > 40:
        return "narrative"

    # Structured document (markdown with headings)
    if fp.has_markdown_headings and fp.heading_count >= 2:
        return "document"

    # Data (high digit ratio)
    if fp.digit_ratio > 0.3:
        return "data"

    # Mixed / unknown
    return "mixed"


def execute(inputs: dict, config: dict) -> ModuleOutput:
    """Fingerprint all files from Pe output with extended signals.

    Inputs:
        pe_output: list[FileMetadata]
    """
    pe_output: list[FileMetadata] = inputs.get("pe_output", [])

    fingerprints = []
    for meta in pe_output:
        fp = fingerprint_file(Path(meta.path))
        fingerprints.append(fp)

    # Content class distribution
    class_counts: dict[str, int] = {}
    for fp in fingerprints:
        c = fp.content_class or "unknown"
        class_counts[c] = class_counts.get(c, 0) + 1

    return ModuleOutput(
        data=fingerprints,
        confident=fingerprints,
        ambiguous=[],
        mode="D",
        stage="In",
        stats={
            "total_fingerprinted": len(fingerprints),
            "content_class_distribution": class_counts,
            "text_count": sum(1 for fp in fingerprints if fp.is_text),
            "binary_count": sum(1 for fp in fingerprints if fp.is_binary),
        },
    )
