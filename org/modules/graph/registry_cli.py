#!/usr/bin/env python3
"""
comp-registry -- REGISTRY-vs-JSON-vs-PRD narrative drift detection + sync.

Detects drift between `org/projects/REGISTRY.md` row narratives and the
authoritative `org/projects/{CODE}.json` source-of-truth fields
(status / current_phase / blocking / prds[]). Optionally writes corrected
narrative back to REGISTRY under CVO author line via safe-commit.sh.

Usage:
    comp-registry sync ROW=N                   # diff-report for row N (1-indexed) read-only
    comp-registry sync --project CODE          # diff-report by project code read-only
    comp-registry sync --all                   # workspace-wide sweep across all Active rows
    comp-registry sync ROW=N --apply           # write-back JSON-derived narrative to REGISTRY
    comp-registry sync --project CODE --apply  # write-back by project code

Default mode: apply-flag-required (no --apply = read-only diff report).

Per ADHC_COMPIL_V5 PRD v0.1 TO-003 (commit 701103ccf) + CVO brief
92b198aac §3 Fix 3 scope. Author: 3.0.0_SA_CVO per Andrew direct delegation
2026-05-26 ~16:55Z overriding the original [[cvo-self-validation-mitigation-pattern]]
default.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

REGISTRY_PATH = _WORKSPACE / "org" / "projects" / "REGISTRY.md"
PROJECTS_DIR = _WORKSPACE / "org" / "projects"

# Match `<hash>` (7-40 hex) inside backticks
COMMIT_HASH_RE = re.compile(r"`([a-f0-9]{7,40})`")
# Match leading phase keyword: e.g., "Phase 2 TO-001 SHIPPED", "Phase 1 PRD v0.1 CANONICAL"
PHASE_KEYWORD_RE = re.compile(r"\*\*Phase\s+(\d+)\b[^*]{0,200}\*\*")
# Match plain "Phase N ..." in narrative
PHASE_INLINE_RE = re.compile(r"Phase\s+(\d+)\b")
# Match status-string Phase encoding: "phaseN_xxx"
STATUS_PHASE_RE = re.compile(r"^phase(\d+)_", re.IGNORECASE)
# Active vs Completed table header sentinel (match actual REGISTRY.md headers)
# Active:    | Project Code | Macro | Project Name | Phase | Pods | Blocking | PRDs |
# Completed: | Project Code | Macro | Project Name | Completed | Notes |
# Held:      | Project Code | Macro | Project Name | Held Since | Reason |
ACTIVE_HEADER_RE = re.compile(r"^\|\s*Project\s+Code\s*\|\s*Macro\s*\|\s*Project\s+Name\s*\|\s*Phase\s*\|\s*Pods\s*\|\s*Blocking\s*\|\s*PRDs", re.IGNORECASE)
COMPLETED_HEADER_RE = re.compile(r"^\|\s*Project\s+Code\s*\|\s*Macro\s*\|\s*Project\s+Name\s*\|\s*Completed\s*\|\s*Notes", re.IGNORECASE)
HELD_HEADER_RE = re.compile(r"^\|\s*Project\s+Code\s*\|\s*Macro\s*\|\s*Project\s+Name\s*\|\s*Held\s+Since", re.IGNORECASE)
# Match `## ` section header
SECTION_HEADER_RE = re.compile(r"^##\s+")


@dataclass
class RegistryRow:
    line_number: int        # 1-indexed line in REGISTRY.md
    row_index: int          # 1-indexed within enclosing table (Active starts at 1)
    table: str              # "active" or "completed"
    project_code: str
    macro_code: str
    name: str
    phase_narrative: str    # full phase cell text (the long narrative)
    completed_date: str     # only populated for completed table
    pods: str               # only populated for active table
    blocking: str           # only populated for active table
    prd_path: str           # only populated for active table; embedded in completed phase cell


@dataclass
class ProjectJson:
    project_code: str
    path: Path
    raw: dict
    status: str = ""
    current_phase: str = ""
    blocking: str = ""
    prds: list[dict] = field(default_factory=list)
    completed: str = ""

    @property
    def status_phase_num(self) -> str:
        """Extract the leading 'phaseN_' from status field, e.g., 'phase2_to001_shipped' -> '2'."""
        m = STATUS_PHASE_RE.match(self.status or "")
        return m.group(1) if m else ""

    @property
    def latest_commit_refs(self) -> list[str]:
        """Extract commit hashes referenced in current_phase narrative (most recent first by order)."""
        return COMMIT_HASH_RE.findall(self.current_phase or "")

    @property
    def latest_prd_label(self) -> str:
        if not self.prds:
            return ""
        last = self.prds[-1]
        if isinstance(last, dict):
            return last.get("label", "")
        if isinstance(last, str):
            return last
        return ""


@dataclass
class Drift:
    project_code: str
    row_line_number: int
    drift_class: str        # PHASE-LAG / COMMIT-CITATION-LAG / STATUS-MISMATCH / PRD-LABEL-LAG / ROW-MISSING / JSON-MISSING
    description: str
    recommended_update: str = ""


# ---------------------------------------------------------------------------
# REGISTRY.md parser
# ---------------------------------------------------------------------------

def parse_registry() -> list[RegistryRow]:
    """Parse REGISTRY.md and return all rows (active + completed tables)."""
    if not REGISTRY_PATH.exists():
        return []

    lines = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace").splitlines()
    rows: list[RegistryRow] = []
    current_table: str = ""
    row_index_in_table = 0

    for idx, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")

        # Detect table headers
        if ACTIVE_HEADER_RE.match(line):
            current_table = "active"
            row_index_in_table = 0
            continue
        if COMPLETED_HEADER_RE.match(line):
            current_table = "completed"
            row_index_in_table = 0
            continue
        if HELD_HEADER_RE.match(line):
            current_table = "held"
            row_index_in_table = 0
            continue
        # Detect section header — resets table context
        if SECTION_HEADER_RE.match(line):
            current_table = ""
            row_index_in_table = 0
            continue
        # Detect separator row | --- | --- | (skip)
        if re.match(r"^\|\s*-+", line):
            continue
        # Skip non-table lines
        if not line.startswith("|") or not current_table:
            continue

        # Split row by `|` — careful with escaped pipes (rare in narratives)
        # Use a simple split since narratives mostly avoid `|`
        cells = [c.strip() for c in line.split("|")]
        # Remove leading + trailing empty cells from leading/trailing `|`
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]

        # First cell should be a project_code wrapped in backticks
        if not cells or not cells[0].startswith("`") or not cells[0].endswith("`"):
            continue

        project_code = cells[0].strip("`").strip()
        if not project_code:
            continue

        row_index_in_table += 1

        if current_table == "active":
            # Schema: code | macro | name | phase | pods | blocking | prd_path
            if len(cells) < 7:
                continue
            rows.append(RegistryRow(
                line_number=idx,
                row_index=row_index_in_table,
                table="active",
                project_code=project_code,
                macro_code=cells[1].strip("`").strip(),
                name=cells[2],
                phase_narrative=cells[3],
                completed_date="",
                pods=cells[4],
                blocking=cells[5],
                prd_path=cells[6],
            ))
        elif current_table == "completed":
            # Schema: code | macro | name | completed | phase_with_close_summary (5 cols)
            if len(cells) < 5:
                continue
            rows.append(RegistryRow(
                line_number=idx,
                row_index=row_index_in_table,
                table="completed",
                project_code=project_code,
                macro_code=cells[1].strip("`").strip(),
                name=cells[2],
                phase_narrative=cells[4],
                completed_date=cells[3],
                pods="",
                blocking="",
                prd_path="",  # embedded in phase cell for completed rows
            ))

    return rows


# ---------------------------------------------------------------------------
# Project JSON loader
# ---------------------------------------------------------------------------

def load_project_json(project_code: str) -> ProjectJson | None:
    """Load the project JSON if present; return None if absent."""
    path = PROJECTS_DIR / f"{project_code}.json"
    if not path.exists():
        return None
    try:
        raw = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    except json.JSONDecodeError:
        return ProjectJson(project_code=project_code, path=path, raw={})

    return ProjectJson(
        project_code=project_code,
        path=path,
        raw=raw,
        status=str(raw.get("status", "")),
        current_phase=str(raw.get("phase", raw.get("current_phase", ""))),
        blocking=str(raw.get("blocking", "")),
        prds=raw.get("prds", []) if isinstance(raw.get("prds"), list) else [],
        completed=str(raw.get("completed", "")),
    )


# ---------------------------------------------------------------------------
# Drift detection
# ---------------------------------------------------------------------------

def detect_drift(row: RegistryRow, pj: ProjectJson) -> list[Drift]:
    """Return drift findings between a single REGISTRY row and its project JSON."""
    drifts: list[Drift] = []

    # Check: status-phase-num vs phase-narrative cite
    status_phase = pj.status_phase_num
    if status_phase:
        # Find phase-num in narrative (look for "Phase N" mention; pick highest cited)
        narrative_phases = PHASE_INLINE_RE.findall(row.phase_narrative)
        cited_max = max((int(p) for p in narrative_phases), default=0)
        status_n = int(status_phase)
        if cited_max < status_n:
            drifts.append(Drift(
                project_code=row.project_code,
                row_line_number=row.line_number,
                drift_class="PHASE-LAG",
                description=f"JSON status='{pj.status}' indicates Phase {status_n}; REGISTRY narrative cites max Phase {cited_max or 'NONE'}",
                recommended_update=f"Refresh phase narrative to lead with 'Phase {status_n}' per JSON status",
            ))

    # Check: JSON-cited commits also in REGISTRY narrative
    json_commits = set(_short_hashes(pj.latest_commit_refs))
    registry_commits = set(_short_hashes(COMMIT_HASH_RE.findall(row.phase_narrative)))
    missing = json_commits - registry_commits
    if missing and json_commits:
        # Only flag if JSON has at least 1 commit AND >25% of JSON commits are missing from registry
        miss_ratio = len(missing) / len(json_commits)
        if miss_ratio > 0.25 or len(missing) >= 3:
            drifts.append(Drift(
                project_code=row.project_code,
                row_line_number=row.line_number,
                drift_class="COMMIT-CITATION-LAG",
                description=f"JSON cites {len(json_commits)} commits; REGISTRY narrative missing {len(missing)} of them: {sorted(missing)[:5]}",
                recommended_update="Refresh phase narrative to cite JSON-referenced recent commits",
            ))

    # Check: PRD label matches
    if pj.latest_prd_label and row.prd_path:
        # Extract version token (v0.N or vN.M) from each
        json_versions = re.findall(r"v\d+\.\d+(?:\.\d+)?", pj.latest_prd_label)
        registry_versions = re.findall(r"v\d+\.\d+(?:\.\d+)?", row.prd_path)
        if json_versions and registry_versions:
            json_latest = json_versions[-1]
            registry_latest = registry_versions[-1]
            if json_latest != registry_latest:
                # Numeric compare: only flag if JSON > registry
                if _version_tuple(json_latest) > _version_tuple(registry_latest):
                    drifts.append(Drift(
                        project_code=row.project_code,
                        row_line_number=row.line_number,
                        drift_class="PRD-LABEL-LAG",
                        description=f"JSON cites PRD {json_latest}; REGISTRY PRD column cites {registry_latest}",
                        recommended_update=f"Refresh PRD column to reference {json_latest}",
                    ))

    # Check: status='complete' but row in Active table
    if pj.status.lower() == "complete" and row.table == "active":
        drifts.append(Drift(
            project_code=row.project_code,
            row_line_number=row.line_number,
            drift_class="STATUS-MISMATCH",
            description=f"JSON status='complete' but REGISTRY row in Active table (should move to Completed)",
            recommended_update="Move row from Active table to Completed table per Closure Discipline 3-step",
        ))

    return drifts


def detect_drift_for_missing_row(project_code: str, pj: ProjectJson) -> Drift:
    """Project JSON exists but no REGISTRY row found."""
    return Drift(
        project_code=project_code,
        row_line_number=0,
        drift_class="ROW-MISSING",
        description=f"Project JSON exists at {pj.path.relative_to(_WORKSPACE)} but no REGISTRY row found",
        recommended_update="Add REGISTRY row to appropriate Active/Completed table per COO authoring lane",
    )


def detect_drift_for_missing_json(row: RegistryRow) -> Drift:
    """REGISTRY row exists but no project JSON found."""
    return Drift(
        project_code=row.project_code,
        row_line_number=row.line_number,
        drift_class="JSON-MISSING",
        description=f"REGISTRY row {row.row_index} exists but no project JSON found at org/projects/{row.project_code}.json",
        recommended_update="Author project JSON OR remove REGISTRY row if project deprecated",
    )


def _short_hashes(hashes: list[str]) -> list[str]:
    """Normalize to 7-char short hashes for comparison."""
    return [h[:7] for h in hashes if len(h) >= 7]


def _version_tuple(v: str) -> tuple[int, ...]:
    """Parse 'v0.3' or 'v1.0.2' into a comparable tuple."""
    parts = v.lstrip("v").split(".")
    try:
        return tuple(int(p) for p in parts)
    except ValueError:
        return (0,)


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_diff_report(drifts: list[Drift], header_label: str = "") -> str:
    """Format drift findings into a clean stdout report."""
    if not drifts:
        suffix = f" ({header_label})" if header_label else ""
        return f"No drift detected{suffix}.\n"

    out: list[str] = []
    if header_label:
        out.append(f"DRIFT FINDINGS{header_label}")
        out.append("")

    # Group by project_code
    by_project: dict[str, list[Drift]] = {}
    for d in drifts:
        by_project.setdefault(d.project_code, []).append(d)

    for code in sorted(by_project.keys()):
        proj_drifts = by_project[code]
        row_line = proj_drifts[0].row_line_number
        if row_line:
            out.append(f"  {code} (REGISTRY.md:{row_line})")
        else:
            out.append(f"  {code} (NO REGISTRY ROW)")
        for d in proj_drifts:
            out.append(f"    !! {d.drift_class}: {d.description}")
            if d.recommended_update:
                out.append(f"       Fix: {d.recommended_update}")
        out.append("")

    out.append(f"Total: {len(drifts)} drift finding(s) across {len(by_project)} project(s)")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Write-back (apply mode)
# ---------------------------------------------------------------------------

def rebuild_phase_narrative(row: RegistryRow, pj: ProjectJson) -> str:
    """Regenerate REGISTRY phase-cell narrative from JSON source-of-truth.

    Strategy: use JSON `current_phase` as authoritative narrative (it's the
    most up-to-date project-state attestation per COO/CTO/AE authoring lane).
    Preserve REGISTRY narrative's leading **bold-phase marker** style by
    wrapping the first sentence of JSON phase in `**...**`.
    """
    phase = (pj.current_phase or "").strip()
    if not phase:
        return row.phase_narrative

    # Re-wrap first sentence in bold if not already
    if phase.startswith("**"):
        return phase

    # Find first sentence boundary (period, semicolon, or first paren)
    first_end = -1
    for i, ch in enumerate(phase):
        if i > 20 and ch in ".;":
            # Need a space or end after for sentence boundary
            if i + 1 >= len(phase) or phase[i + 1] in " \n":
                first_end = i
                break

    if first_end > 0:
        return f"**{phase[:first_end+1]}** {phase[first_end+2:]}"
    return f"**{phase}**"


def apply_writeback(row: RegistryRow, pj: ProjectJson, dry_run: bool = False) -> tuple[bool, str]:
    """Rewrite the REGISTRY row's phase cell from JSON. Returns (changed, message)."""
    new_phase = rebuild_phase_narrative(row, pj)
    if new_phase == row.phase_narrative:
        return False, f"No change needed for {row.project_code} (already in sync)."

    if not REGISTRY_PATH.exists():
        return False, "REGISTRY.md not found."

    lines = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace").splitlines()
    target_idx = row.line_number - 1
    if target_idx < 0 or target_idx >= len(lines):
        return False, f"Row line {row.line_number} out of range."

    # Replace the phase-cell within the line by splitting on `|`
    line = lines[target_idx]
    cells = line.split("|")
    if cells and cells[0] == "":
        cells_offset = 1
    else:
        cells_offset = 0

    # Active table: phase is at cells[cells_offset+3]; Completed: at cells[cells_offset+4]
    phase_cell_idx = cells_offset + (4 if row.table == "completed" else 3)
    if phase_cell_idx >= len(cells):
        return False, f"Phase cell index {phase_cell_idx} out of range for row."

    cells[phase_cell_idx] = f" {new_phase} "
    new_line = "|".join(cells)
    lines[target_idx] = new_line

    if dry_run:
        return True, f"DRY-RUN: would update REGISTRY.md:{row.line_number} phase narrative for {row.project_code}."

    REGISTRY_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Invoke safe-commit.sh under CVO author line
    safe_commit = _WORKSPACE / ".tools" / "safe-commit.sh"
    if not safe_commit.exists():
        return True, f"REGISTRY.md updated for {row.project_code} but safe-commit.sh not found; commit manually."

    commit_msg = (
        f"comp-registry-sync({row.project_code}): REGISTRY row {row.row_index} "
        f"phase narrative refresh from JSON source-of-truth (status={pj.status})"
    )
    result = subprocess.run(
        [
            "bash",
            str(safe_commit),
            "--author=3.0.0_SA_CVO <3.0.0_SA_CVO@opal.agent>",
            "-m",
            commit_msg,
            "--",
            "org/projects/REGISTRY.md",
        ],
        cwd=str(_WORKSPACE),
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return True, (
            f"REGISTRY.md updated for {row.project_code} but safe-commit.sh failed (exit={result.returncode}); "
            f"stderr:\n{result.stderr.strip()}"
        )
    return True, f"REGISTRY.md updated + committed for {row.project_code} via safe-commit.sh."


# ---------------------------------------------------------------------------
# Command dispatch
# ---------------------------------------------------------------------------

def _parse_row_arg(arg: str) -> int | None:
    """Parse 'ROW=N' or 'row=N' or bare integer."""
    if arg is None:
        return None
    m = re.match(r"(?:ROW|row)\s*=\s*(\d+)$", arg)
    if m:
        return int(m.group(1))
    try:
        return int(arg)
    except ValueError:
        return None


def cmd_sync(args) -> int:
    rows = parse_registry()
    if not rows:
        print("REGISTRY.md not found or empty.", file=sys.stderr)
        return 1

    # Mode resolution
    row_index: int | None = None
    if args.row:
        row_index = _parse_row_arg(args.row)
        if row_index is None:
            print(f"Invalid ROW arg: {args.row}", file=sys.stderr)
            return 1

    selected_rows: list[RegistryRow] = []
    if args.all:
        selected_rows = [r for r in rows if r.table == "active"]
    elif args.project:
        proj_rows = [r for r in rows if r.project_code == args.project]
        if not proj_rows:
            # JSON-without-row case
            pj = load_project_json(args.project)
            if pj:
                drift = detect_drift_for_missing_row(args.project, pj)
                print(format_diff_report([drift], header_label=f" for {args.project}"))
                return 0
            print(f"No REGISTRY row OR project JSON found for: {args.project}", file=sys.stderr)
            return 1
        selected_rows = proj_rows
    elif row_index is not None:
        # Find row by row_index within active table (most common); fall back to scan all
        match = [r for r in rows if r.row_index == row_index and r.table == "active"]
        if not match:
            match = [r for r in rows if r.row_index == row_index]
        if not match:
            print(f"No row at index {row_index} found in REGISTRY.md.", file=sys.stderr)
            return 1
        selected_rows = match
    else:
        print("Specify ROW=N, --project CODE, or --all.", file=sys.stderr)
        return 1

    all_drifts: list[Drift] = []
    applied: list[str] = []
    for row in selected_rows:
        pj = load_project_json(row.project_code)
        if pj is None:
            all_drifts.append(detect_drift_for_missing_json(row))
            continue

        drifts = detect_drift(row, pj)
        all_drifts.extend(drifts)

        if args.apply and drifts:
            # Only attempt writeback if PHASE-LAG or COMMIT-CITATION-LAG present
            applyable = [d for d in drifts if d.drift_class in ("PHASE-LAG", "COMMIT-CITATION-LAG", "PRD-LABEL-LAG")]
            if applyable:
                changed, msg = apply_writeback(row, pj)
                applied.append(msg)

    # Also sweep --all for ROW-MISSING (JSON exists but no row)
    if args.all:
        all_codes_in_registry = {r.project_code for r in rows}
        for jpath in sorted(PROJECTS_DIR.glob("*.json")):
            code = jpath.stem
            if code not in all_codes_in_registry:
                pj = load_project_json(code)
                if pj:
                    all_drifts.append(detect_drift_for_missing_row(code, pj))

    label = ""
    if args.all:
        label = " (workspace-wide sweep)"
    elif args.project:
        label = f" for {args.project}"
    elif row_index is not None:
        label = f" for ROW={row_index}"
    print(format_diff_report(all_drifts, header_label=label))

    if applied:
        print("\nAPPLY RESULTS:")
        for m in applied:
            print(f"  {m}")

    # Exit code: 0 if no drift, 2 if drift detected (so CI can flag)
    return 0 if not all_drifts else 2


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="comp-registry",
        description="REGISTRY-vs-JSON-vs-PRD narrative drift detection + sync.",
    )
    sub = p.add_subparsers(dest="command")

    p_sync = sub.add_parser("sync", help="diff-report (default) or write-back with --apply")
    p_sync.add_argument("row", nargs="?", default=None, help="ROW=N row index")
    p_sync.add_argument("--project", help="project code (e.g., YALP_MKTOVR)")
    p_sync.add_argument("--all", action="store_true", help="workspace-wide sweep")
    p_sync.add_argument("--apply", action="store_true", help="write JSON-derived narrative back to REGISTRY (default: read-only diff)")
    p_sync.add_argument("--target", default="JSON", help="diff target: JSON | PRD | BOTH (default JSON)")
    p_sync.set_defaults(func=cmd_sync)

    args = p.parse_args(argv)
    if not getattr(args, "command", None):
        p.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
