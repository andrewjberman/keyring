"""BR-1/BR-3 acceptance for un-skippable comp-read enumeration claims.

The first three arms exercise the exact downstream filter from
BRIEF_20260903_COMP_READ_ENUMERATION_UNSKIPPABLE.md.  A synthetic ERROR row uses
line 0: the brief also says line -1, but its mandated ``^[0-9]+`` receiver
cannot retain a negative number.  Zero is the filter-safe synthetic-line
sentinel; the ERROR tag keeps it distinct from ABSENT.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import jsonschema


WS = Path(__file__).resolve().parents[2]
TOOL = WS / ".tools" / "comp-read"
SCHEMA = WS / "org" / "standards" / "COMP_READ_ENUMERATE.schema.json"
ROW_RE = re.compile(
    r"^\s+(-?\d+)\s+([A-Z][A-Z0-9-]*)\s+"
    r"(WHOLE|SUB|ABSENT|ERROR)\s+hit\s+(\d+)/(\d+)\s+(.*)$"
)


def run_tool(path: Path, pattern: str, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(TOOL), str(path), "--enumerate", pattern, *extra],
        cwd=WS,
        capture_output=True,
        text=True,
        timeout=120,
    )


def exact_filter(path: Path, pattern: str) -> tuple[int, list[str]]:
    producer = subprocess.Popen(
        [sys.executable, str(TOOL), str(path), "--enumerate", pattern],
        cwd=WS,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert producer.stdout is not None
    receiver = subprocess.run(
        ["grep", "-E", r"^\s+[0-9]+ "],
        stdin=producer.stdout,
        capture_output=True,
        text=True,
        timeout=120,
    )
    producer.stdout.close()
    producer.wait(timeout=120)
    return producer.returncode, [line for line in receiver.stdout.splitlines() if line]


def specimen(tmp_path: Path) -> Path:
    path = tmp_path / "enumerate.md"
    path.write_text(
        "# needle heading\n"
        "needle whole\n"
        "prefixneedle substring\n"
        "plain prose\n",
        encoding="utf-8",
    )
    return path


def parsed_rows(lines: list[str]) -> list[re.Match[str]]:
    rows = [ROW_RE.match(line) for line in lines]
    assert all(rows), "non-conforming row(s): %r" % lines
    return [row for row in rows if row is not None]


def test_three_hit_rows_survive_exact_filter_with_claim(tmp_path: Path) -> None:
    rc, lines = exact_filter(specimen(tmp_path), "needle")
    rows = parsed_rows(lines)
    assert rc == 0
    assert len(rows) == 3
    assert [int(row.group(4)) for row in rows] == [1, 2, 3]
    assert {int(row.group(5)) for row in rows} == {3}
    assert {row.group(3) for row in rows} <= {"WHOLE", "SUB"}


def test_zero_hit_is_one_filter_safe_absent_row(tmp_path: Path) -> None:
    rc, lines = exact_filter(specimen(tmp_path), "definitely-absent")
    rows = parsed_rows(lines)
    assert rc == 0
    assert len(rows) == 1
    assert rows[0].group(1, 2, 3, 4, 5) == ("0", "ENUMERATE", "ABSENT", "0", "0")


def test_bad_pattern_is_one_filter_safe_error_row(tmp_path: Path) -> None:
    rc, lines = exact_filter(specimen(tmp_path), "[")
    rows = parsed_rows(lines)
    assert rc == 2
    assert len(rows) == 1
    assert rows[0].group(1, 2, 3, 4, 5) == ("0", "ERROR", "ERROR", "0", "0")


def test_header_and_trailer_bracket_every_text_enumeration(tmp_path: Path) -> None:
    out = run_tool(specimen(tmp_path), "needle").stdout.splitlines()
    assert out[0].startswith("comp-read: ")
    assert out[-1].startswith("ENUMERATE-END: 3 hit(s) | 2 whole | 1 sub |")


def test_width_truncates_rows_not_summary(tmp_path: Path) -> None:
    result = run_tool(specimen(tmp_path), "needle", "--width", "8")
    rows = parsed_rows([line for line in result.stdout.splitlines() if ROW_RE.match(line)])
    assert rows
    assert all(len(row.group(6)) <= 8 for row in rows)
    assert "ENUMERATE: 3 hit(s) across 4 lines" in result.stdout


def test_band_filters_rows_but_keeps_full_band_counts(tmp_path: Path) -> None:
    result = run_tool(specimen(tmp_path), "needle", "--band", "HEADING")
    rows = parsed_rows([line for line in result.stdout.splitlines() if ROW_RE.match(line)])
    assert rows and {row.group(2) for row in rows} == {"HEADING"}
    assert re.search(r"^\s+HEADING\s+1\s*$", result.stdout, re.MULTILINE)
    assert re.search(r"^\s+PROSE\s+2\s*$", result.stdout, re.MULTILINE)


def test_json_validates_and_requires_summary(tmp_path: Path) -> None:
    result = run_tool(specimen(tmp_path), "needle", "--json")
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft7Validator(schema).validate(payload)
    assert payload["summary"]["hits"] == 3
    assert len(payload["rows"]) == 3
    missing = dict(payload)
    missing.pop("summary")
    assert list(jsonschema.Draft7Validator(schema).iter_errors(missing))


def test_digest_mode_is_unchanged() -> None:
    result = subprocess.run(
        [sys.executable, str(TOOL), str(TOOL), "--for", "enumeration implementation"],
        cwd=WS,
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert result.returncode == 0
    assert "SHAPE" in result.stdout and "UNREAD LEDGER" in result.stdout
    assert "ENUMERATE-END:" not in result.stdout
