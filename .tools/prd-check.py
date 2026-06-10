#!/usr/bin/env python3
"""
prd-check.py -- show open projects with PRDs, grouped by whether active TOs exist.

Usage:
  python .tools/prd-check.py              # PRDs issued <=14d, not closed
  python .tools/prd-check.py -all         # all open PRDs regardless of age
  python .tools/prd-check.py --project X  # single project code

Output classes:
  ACTIVE TOs  -- project has >=1 non-complete TO file
  NO TOs      -- project has zero active TO files (may have all-closed TOs or none)
"""
from __future__ import annotations

import json
import re
import sys
import os
import glob
from datetime import datetime, timedelta, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
PROJECTS_DIR = WORKSPACE / "org" / "projects"
LOOKBACK_DAYS = 14
SEP = "-" * 56

# ASCII-fold: Windows console cp1252 cannot handle non-ASCII in print output.
_ASCII = {
    "—": "--", "–": "-", "…": "...", "→": "->",
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "✓": "OK", "✗": "x", "×": "x", " ": " ", "•": "*",
    "�": "?",
}


def to_ascii(t: str) -> str:
    for u, a in _ASCII.items():
        t = t.replace(u, a)
    return t.encode("ascii", "replace").decode("ascii")


def clean(t: str) -> str:
    t = to_ascii(str(t or ""))
    return re.sub(r"\s+", " ", t).strip()

COMPLETE_WORDS = {"complete", "completed", "closed", "cancelled", "canceled",
                  "superseded", "done", "merged", "decommissioned", "dropped",
                  "archived", "shipped", "impl-complete", "impl_complete", "implemented"}


def _strip_xml_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def _extract_tag(text: str, tag: str) -> str | None:
    m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL | re.IGNORECASE)
    if not m:
        return None
    return _strip_xml_comments(m.group(1)).strip()


def _classify_status(raw: str) -> str:
    """Return COMPLETE / ACTIVE / PENDING / BLOCKED / UNKNOWN from raw status text."""
    cleaned = _strip_xml_comments(raw).strip().lower()
    # Take first word before space, dash-dash, or newline
    first = re.split(r"[\s\-\n]", cleaned)[0].rstrip(".,;:") if cleaned else ""
    if first in COMPLETE_WORDS:
        return "COMPLETE"
    if first in {"active", "dispatched", "dispatch", "in_progress", "staged", "go"}:
        return "ACTIVE"
    if first in {"pending", "hold", "on-hold", "queued", "waiting"}:
        return "PENDING"
    if first in {"blocked"}:
        return "BLOCKED"
    if not first:
        return "UNKNOWN"
    # Default conservative: assume active if not explicitly complete
    return "ACTIVE"


def _extract_project_code_from_to_id(to_id: str) -> str:
    """ADHC_BDTSCLB.002 -> ADHC_BDTSCLB, MDPF_CADENCE -> MDPF_CADENCE, ADVI_FEREFI.W1 -> ADVI_FEREFI."""
    if not to_id:
        return ""
    # Split at first dot, keep the pre-dot part if it looks like a project code
    parts = to_id.split(".", 1)
    code = parts[0].strip().upper()
    if re.match(r"^[A-Z][A-Z0-9_]{2,}$", code):
        return code
    return to_id.upper()


def _extract_tag_multi(text: str, *tags: str) -> str | None:
    """Try multiple tag names, return first match."""
    for tag in tags:
        v = _extract_tag(text, tag)
        if v:
            return v
    return None


def _extract_md_field(text: str, *labels: str) -> str | None:
    """Extract Markdown bold-label field: **Label:** `value` or **Label:** value."""
    for label in labels:
        m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*`?([^`\n]+?)`?\s*$",
                      text, re.MULTILINE | re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None


def parse_to_file(path: str) -> dict:
    """Parse a TO file. Handles XML (new + old schema) and Markdown formats.
    Never drops -- surfaces parse errors in _error field."""
    fname = Path(path).name
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")

        # --- XML fields (new schema: to_id/assigned_to/issued_date/title/project)
        #     Old schema fallbacks: id / issued_to / date / project_code
        to_id = _extract_tag_multi(text, "to_id") or ""
        # <id> can be a full order-id like "2.0.0_SA_COO-2026-...-049" -- skip if no _
        if not to_id:
            candidate = _extract_tag_multi(text, "id") or ""
            if re.match(r"^[A-Z][A-Z0-9_]{2,}", candidate.upper()):
                to_id = candidate

        project_field = _extract_tag_multi(text, "project", "project_code") or ""
        title = _extract_tag_multi(text, "title") or ""
        assigned_to = _extract_tag_multi(text, "assigned_to", "issued_to") or ""
        issued_by = _extract_tag_multi(text, "issued_by") or ""
        issued_date = _extract_tag_multi(text, "issued_date", "date") or ""
        status_raw = _extract_tag_multi(text, "status") or ""
        priority = (_extract_tag_multi(text, "priority") or "")[:80]

        # --- Markdown fallbacks (format: **Owner:** `serial`, **Status:** ...) ---
        if not assigned_to:
            assigned_to = _extract_md_field(text, "Owner", "Assigned to", "Assignee") or ""
        if not issued_by:
            issued_by = _extract_md_field(text, "From", "Issued by") or ""
        if not status_raw:
            status_raw = _extract_md_field(text, "Status") or ""
        if not issued_date:
            issued_date = _extract_md_field(text, "Date", "Issued") or ""

        # Title fallback: first markdown H1 line, strip the to_id prefix
        if not title:
            m = re.match(r"^#\s+(.+)", text.lstrip(), re.MULTILINE)
            if m:
                header = _strip_xml_comments(m.group(1)).strip()
                # Try to remove the to_id/code prefix: "ADHC_DESIGN.026 -- Title" -> "Title"
                title_m = re.match(r"^[A-Z][A-Z0-9_.\-]+\s*[\-–—:]\s+(.+)", header)
                title = title_m.group(1).strip() if title_m else header
        if not title:
            title = "(no title)"

        # --- Project code resolution: to_id > project field > filename ---
        project_code = _extract_project_code_from_to_id(to_id)
        if not project_code:
            m = re.match(r"^([A-Z][A-Z0-9_]{2,})", project_field)
            project_code = m.group(1) if m else ""
        if not project_code:
            m = re.match(r"^([A-Z][A-Z0-9_]{2,})", fname.upper())
            project_code = m.group(1) if m else "UNKNOWN"

        # Validate issued_date format
        try:
            datetime.strptime(issued_date, "%Y-%m-%d")
        except (ValueError, TypeError):
            issued_date = ""

        return {
            "to_id": to_id or fname.replace(".md", ""),
            "project_code": project_code,
            "title": title,
            "assigned_to": assigned_to or "(unassigned)",
            "issued_by": issued_by,
            "issued_date": issued_date,
            "status_raw": status_raw[:160],
            "status_class": _classify_status(status_raw),
            "priority": priority,
            "path": path,
            "_error": None,
        }
    except Exception as e:
        return {
            "to_id": fname.replace(".md", ""),
            "project_code": "UNKNOWN",
            "title": "(parse error)",
            "assigned_to": "(unknown)",
            "issued_by": "",
            "issued_date": "",
            "status_raw": "",
            "status_class": "UNKNOWN",
            "priority": "",
            "path": path,
            "_error": str(e),
        }


def find_all_to_files() -> list[str]:
    pattern = str(WORKSPACE / "org" / "**" / "task_orders" / "*.md")
    return glob.glob(pattern, recursive=True)


def load_projects_with_prds(lookback_days: int, show_all: bool,
                             project_filter: str | None) -> tuple[list[dict], list[dict]]:
    """Return (prd_projects, malformed). prd_projects have _recent_prds injected."""
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=lookback_days)
    closed_statuses = {"complete", "completed", "closed", "cancelled", "merged",
                       "superseded", "done"}
    projects = []
    malformed = []

    for f in sorted(PROJECTS_DIR.glob("*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8", errors="replace"))
            projects.append(d)
        except Exception as e:
            malformed.append({"_path": str(f), "_error": str(e)})

    result = []
    for p in projects:
        if p.get("status", "unknown").lower() in closed_statuses:
            continue
        prds = p.get("prds") or []
        if not prds:
            continue
        code = p.get("project_code", "")
        if project_filter and code.upper() != project_filter.upper():
            continue

        recent_prds = []
        for prd in prds:
            # prds entries can be str (path only) or dict {path, label, date}
            if isinstance(prd, str):
                prd = {"path": prd, "label": prd.split("/")[-1].replace(".md", ""), "date": ""}
            date_str = prd.get("date", "")
            try:
                prd_date = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                if show_all or prd_date >= cutoff:
                    recent_prds.append(prd)
            except ValueError:
                if show_all:
                    recent_prds.append(prd)
        if not recent_prds:
            continue
        p["_recent_prds"] = recent_prds
        result.append(p)

    # Sort: newest PRD date first
    def sort_key(p):
        dates = []
        for prd in p.get("_recent_prds", []):
            try:
                dates.append(datetime.strptime(prd["date"], "%Y-%m-%d"))
            except ValueError:
                pass
        return max(dates) if dates else datetime.min

    result.sort(key=sort_key, reverse=True)
    return result, malformed


def _fmt_assignee(raw: str) -> str:
    """Shorten agent serial for display: 0.6.0_AE_PartnerETL -> AE_PartnerETL."""
    m = re.match(r"^\d+\.\d+\.\d+_(.+?)(\s|$|·)", raw.strip())
    return m.group(1) if m else raw.strip()[:40]


def _status_label(sc: str) -> str:
    return {"ACTIVE": "ACTIVE", "PENDING": "PENDING",
            "BLOCKED": "BLOCKED", "COMPLETE": "DONE",
            "UNKNOWN": "??"}.get(sc, sc)


def main():
    args = sys.argv[1:]
    show_all = "-all" in args or "--all-time" in args
    project_filter = None
    if "--project" in args:
        idx = args.index("--project")
        if idx + 1 < len(args):
            project_filter = args[idx + 1]

    prd_projects, malformed = load_projects_with_prds(LOOKBACK_DAYS, show_all, project_filter)

    # Load and index all TO files by project code
    to_files = find_all_to_files()
    tos_by_project: dict[str, list[dict]] = {}
    parse_errors = []
    for f in to_files:
        t = parse_to_file(f)
        if t["_error"]:
            parse_errors.append(t)
        tos_by_project.setdefault(t["project_code"], []).append(t)

    # Categorize projects
    has_active: list[dict] = []
    no_active: list[dict] = []
    for p in prd_projects:
        code = p.get("project_code", "")
        tos = tos_by_project.get(code, [])
        active_tos = [t for t in tos if t["status_class"] != "COMPLETE"]
        if active_tos:
            p["_active_tos"] = active_tos
            has_active.append(p)
        else:
            p["_all_tos"] = tos
            no_active.append(p)

    # Header
    now_str = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    scope_label = "all open PRDs" if show_all else f"PRDs issued <={LOOKBACK_DAYS}d"
    print(f"PRD-CHECK  {now_str}  |  {len(prd_projects)} projects ({scope_label})  "
          f"|  {len(has_active)} active TOs  |  {len(no_active)} no active TOs")
    if malformed:
        names = ", ".join(Path(m["_path"]).name for m in malformed)
        print(f"  MALFORMED-JSON ({len(malformed)}): {names}")
    if parse_errors:
        print(f"  TO-PARSE-ERROR ({len(parse_errors)}): "
              + ", ".join(Path(e["path"]).name for e in parse_errors[:5]))
    print()

    if has_active:
        print(f"== ACTIVE TOs ({len(has_active)} projects) ==")
        print()
        for i, p in enumerate(has_active, 1):
            code = p.get("project_code", "?")
            status = p.get("status", "unknown")
            prds_str = " | ".join(
                f"\"{clean(prd.get('label', '?'))}\" ({prd.get('date', '?')})"
                for prd in p.get("_recent_prds", [])
            )
            active_tos = p.get("_active_tos", [])
            print(f"#: {i}")
            print(f"Project: {code}")
            print(f"Status:  {status}")
            print(f"PRD:     {prds_str}")
            print(f"TOs ({len(active_tos)} active):")
            for t in sorted(active_tos, key=lambda x: x.get("issued_date", "")):
                label = _status_label(t["status_class"])
                assignee = clean(_fmt_assignee(t["assigned_to"]))
                raw_title = clean(t["title"])
                title_short = raw_title[:58] + ("..." if len(raw_title) > 58 else "")
                print(f"  [{label}] {t['to_id']}")
                print(f"    -> {assignee}")
                print(f"    {title_short}")
            print(SEP)

    if no_active:
        print(f"== NO ACTIVE TOs ({len(no_active)} projects) ==")
        print()
        for i, p in enumerate(no_active, 1):
            code = p.get("project_code", "?")
            status = p.get("status", "unknown")
            prds_str = " | ".join(
                f"\"{clean(prd.get('label', '?'))}\" ({prd.get('date', '?')})"
                for prd in p.get("_recent_prds", [])
            )
            all_tos = p.get("_all_tos", [])
            to_note = (f"{len(all_tos)} total (all closed)"
                       if all_tos else "none filed")
            print(f"#: {i}")
            print(f"Project: {code}")
            print(f"Status:  {status}")
            print(f"PRD:     {prds_str}")
            print(f"TOs:     {to_note}")
            print(SEP)

    # Footer
    print(f"PRD-CHECK-RESULT active_to={len(has_active)} no_to={len(no_active)} "
          f"malformed={len(malformed)} parse_errors={len(parse_errors)}")


if __name__ == "__main__":
    main()
