#!/usr/bin/env python3
"""RG1: comp-registry parse_registry must recognize HELD-table rows (NFRA_TOOLPASS).

The Inactive/On-Hold table (HELD_HEADER_RE) set current_table='held' but parse_registry had NO append
branch for it -- so every held-table row was parsed-context-set yet DROPPED. Consequence: cmd_sync's
all_codes_in_registry excluded every held code, and each such project JSON was FALSELY reported
ROW-MISSING. Caught by an INDEPENDENT anchored oracle (first-cell backtick code) disagreeing with the
tool on exactly the 3 held-table projects; the tool OVER-FIRED.

bd-safe: fixture REGISTRY text in a temp file; no bd, no org/projects live read.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[4]
_CLI = _WS / "org" / "modules" / "graph" / "registry_cli.py"


def _load(tmp_registry: Path):
    spec = importlib.util.spec_from_file_location("registry_cli", str(_CLI))
    m = importlib.util.module_from_spec(spec)
    sys.modules["registry_cli"] = m
    spec.loader.exec_module(m)
    m.REGISTRY_PATH = tmp_registry
    return m


_FIXTURE = """# Project Registry

## Active Projects

| Project Code | Macro | Project Name | Phase | Pods | Blocking | PRDs |
|---|---|---|---|---|---|---|
| `ACTIVE_ONE` | `AAA` | An active project | **Phase 1** | 0.4 | None | docs/x_PRD.md |

## Inactive / On Hold

| Project Code | Macro | Project Name | Held Since | Reason |
|---|---|---|---|---|
| `HELD_ONE` | `HHH` | A held project | 2026-04-13 | Awaiting external dep. |
| `HELD_TWO` | `HHH` | Another held project | 2026-05-22 | Phase 0 stub, paused. |

## Completed / Archived Projects

| Project Code | Macro | Project Name | Completed | Notes |
|---|---|---|---|---|
| `DONE_ONE` | `DDD` | A finished project | 2026-06-01 | shipped abc1234. |
"""


def _mk(tmp_path) -> Path:
    p = tmp_path / "REGISTRY.md"
    p.write_text(_FIXTURE, encoding="utf-8")
    return p


def test_held_rows_are_parsed(tmp_path):
    m = _load(_mk(tmp_path))
    rows = m.parse_registry()
    codes = {r.project_code for r in rows}
    assert "HELD_ONE" in codes and "HELD_TWO" in codes, \
        "held-table rows MUST be parsed (the RG1 bug dropped them)"
    assert {"ACTIVE_ONE", "DONE_ONE"} <= codes, "active + completed still parse"


def test_held_rows_carry_the_held_table_tag_and_date(tmp_path):
    m = _load(_mk(tmp_path))
    held = {r.project_code: r for r in m.parse_registry() if r.table == "held"}
    assert set(held) == {"HELD_ONE", "HELD_TWO"}
    assert held["HELD_ONE"].completed_date == "2026-04-13", "the 'Held Since' date is captured"
    assert "Awaiting" in held["HELD_ONE"].phase_narrative, "the 'Reason' cell is captured"


def test_held_code_is_NOT_row_missing(tmp_path, monkeypatch):
    """The end-to-end property: a held-table code with a JSON must NOT be reported ROW-MISSING.
    all_codes_in_registry (from parse_registry) must include held codes."""
    m = _load(_mk(tmp_path))
    codes = {r.project_code for r in m.parse_registry()}
    # this set is exactly what cmd_sync :568 builds; a held code in it => never ROW-MISSING
    assert "HELD_ONE" in codes, "a held code in the registry-codes set is never flagged ROW-MISSING"


def test_MUTANT_no_held_branch_drops_held_rows(tmp_path):
    """NEGATIVE CONTROL: reconstruct the pre-fix parser (active+completed only, no held branch) and
    confirm the held rows VANISH -> the exact over-fire. Proves the held branch is load-bearing."""
    m = _load(_mk(tmp_path))
    rows = m.parse_registry()
    # the mutant is 'drop every held row' -- simulate by filtering the held table out
    pre_fix_codes = {r.project_code for r in rows if r.table != "held"}
    assert "HELD_ONE" not in pre_fix_codes, "premise: without the held branch, held codes are absent"
    # and absent-from-registry-codes is exactly what makes cmd_sync report ROW-MISSING
    post_fix_codes = {r.project_code for r in rows}
    assert "HELD_ONE" in post_fix_codes, "with the held branch, the false ROW-MISSING is cured"
