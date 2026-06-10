#!/usr/bin/env python3
"""
to-check.py -- show active task orders, optionally filtered.

Default: non-complete TOs for projects with PRDs issued <=14d (hot PRD projects).
Use --all to see all non-complete TOs across the workspace.

Usage:
  python .tools/to-check.py                   # hot PRD projects (<=14d), active TOs
  python .tools/to-check.py --all             # all non-complete TOs workspace-wide
  python .tools/to-check.py --project CODE    # TOs for one project (any age)
  python .tools/to-check.py --assignee SERIAL # TOs assigned to agent (partial match ok)
"""
from __future__ import annotations

import json
import re
import sys
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
    "'": "'", "'": "'", """: '"', """: '"',
    "✓": "OK", "✗": "x", "×": "x", " ": " ", "•": "*",
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

STATUS_LABELS = {
    "ACTIVE": "ACTIVE",
    "PENDING": "PENDING",
    "BLOCKED": "BLOCKED !!",
    "COMPLETE": "DONE",
    "UNKNOWN": "??",
}


def _strip_xml_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def _extract_tag(text: str, tag: str) -> str | None:
    m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL | re.IGNORECASE)
    if not m:
        return None
    return _strip_xml_comments(m.group(1)).strip()


def _extract_tag_multi(text: str, *tags: str) -> str | None:
    for tag in tags:
        v = _extract_tag(text, tag)
        if v:
            return v
    return None


def _extract_md_field(text: str, *labels: str) -> str | None:
    for label in labels:
        m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*`?([^`\n]+?)`?\s*$",
                      text, re.MULTILINE | re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return None


def _classify_status(raw: str) -> str:
    cleaned = _strip_xml_comments(raw).strip().lower()
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
    return "ACTIVE"


def _extract_project_code_from_to_id(to_id: str) -> str:
    if not to_id:
        return ""
    parts = to_id.split(".", 1)
    code = parts[0].strip().upper()
    if re.match(r"^[A-Z][A-Z0-9_]{2,}$", code):
        return code
    return to_id.upper()


def parse_to_file(path: str) -> dict:
    """Parse a TO file. Handles XML (new + old schema) and Markdown formats.
    Never drops -- surfaces parse errors in _error field."""
    fname = Path(path).name
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")

        # XML fields -- new schema with old-schema fallbacks
        to_id = _extract_tag_multi(text, "to_id") or ""
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

        # Markdown fallbacks
        if not assigned_to:
            assigned_to = _extract_md_field(text, "Owner", "Assigned to", "Assignee") or ""
        if not issued_by:
            issued_by = _extract_md_field(text, "From", "Issued by") or ""
        if not status_raw:
            status_raw = _extract_md_field(text, "Status") or ""
        if not issued_date:
            issued_date = _extract_md_field(text, "Date", "Issued") or ""

        # Title fallback: first markdown H1
        if not title:
            m = re.match(r"^#\s+(.+)", text.lstrip(), re.MULTILINE)
            if m:
                header = _strip_xml_comments(m.group(1)).strip()
                title_m = re.match(r"^[A-Z][A-Z0-9_.\-]+\s*[\-–—:]\s+(.+)", header)
                title = title_m.group(1).strip() if title_m else header
        if not title:
            title = "(no title)"

        # Project code resolution
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

        status_display = " ".join(_strip_xml_comments(status_raw).split())[:100]

        return {
            "to_id": to_id or fname.replace(".md", ""),
            "project_code": project_code,
            "title": title,
            "assigned_to": assigned_to or "(unassigned)",
            "issued_by": issued_by,
            "issued_date": issued_date,
            "status_raw": status_raw,
            "status_display": status_display,
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
            "status_display": "",
            "status_class": "UNKNOWN",
            "priority": "",
            "path": path,
            "_error": str(e),
        }


def find_all_to_files() -> list[str]:
    pattern = str(WORKSPACE / "org" / "**" / "task_orders" / "*.md")
    return glob.glob(pattern, recursive=True)


def get_hot_prd_project_codes(lookback_days: int) -> set[str]:
    """Project codes that have a PRD issued <=lookback_days ago and are not closed."""
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=lookback_days)
    closed = {"complete", "completed", "closed", "cancelled", "merged",
              "superseded", "done"}
    codes: set[str] = set()
    for f in PROJECTS_DIR.glob("*.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8", errors="replace"))
            if d.get("status", "").lower() in closed:
                continue
            for prd in d.get("prds") or []:
                if isinstance(prd, str):
                    prd = {"path": prd, "date": ""}
                date_str = prd.get("date", "")
                try:
                    prd_date = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                    if prd_date >= cutoff:
                        code = d.get("project_code", "")
                        if code:
                            codes.add(code)
                        break
                except ValueError:
                    pass
        except Exception:
            pass
    return codes


def _fmt_assignee_full(raw: str) -> str:
    """Return the full assignee string, cleaned of leading/trailing whitespace."""
    return raw.strip()


def _fmt_issued_by(raw: str) -> str:
    """Shorten issued_by for display."""
    # Extract the serial if present
    m = re.match(r"^\d+\.\d+\.\d+_\S+", raw.strip())
    if m:
        return m.group(0)
    return raw.strip()[:40]


def _age(date_str: str, now: datetime) -> str:
    """Return human age string like '7d' or '?' if unparseable."""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        delta = now - d
        days = delta.days
        if days == 0:
            return "today"
        if days == 1:
            return "1d"
        return f"{days}d"
    except ValueError:
        return "?"


def main():
    args = sys.argv[1:]
    show_all = "--all" in args
    project_filter: str | None = None
    assignee_filter: str | None = None

    if "--project" in args:
        idx = args.index("--project")
        if idx + 1 < len(args):
            project_filter = args[idx + 1].upper()
    if "--assignee" in args:
        idx = args.index("--assignee")
        if idx + 1 < len(args):
            assignee_filter = args[idx + 1].lower()

    # Determine scope
    hot_codes: set[str] | None = None
    if not show_all and not project_filter:
        hot_codes = get_hot_prd_project_codes(LOOKBACK_DAYS)

    # Load and filter TOs
    to_files = find_all_to_files()
    tos: list[dict] = []
    parse_errors: list[dict] = []
    for f in to_files:
        t = parse_to_file(f)
        if t["_error"]:
            parse_errors.append(t)
            tos.append(t)  # still include -- surface, don't drop
        else:
            tos.append(t)

    # Filter: exclude COMPLETE unless --all with explicit intent
    active_tos = [t for t in tos if t["status_class"] != "COMPLETE"]

    # Scope filter
    if project_filter:
        active_tos = [t for t in active_tos if t["project_code"] == project_filter]
    elif hot_codes is not None:
        active_tos = [t for t in active_tos if t["project_code"] in hot_codes]

    # Assignee filter
    if assignee_filter:
        active_tos = [t for t in active_tos
                      if assignee_filter in t["assigned_to"].lower()]

    # Sort: by project_code then issued_date (newest first within project)
    def sort_key(t: dict):
        try:
            ts = datetime.strptime(t["issued_date"], "%Y-%m-%d").timestamp()
        except ValueError:
            ts = 0.0
        return (t["project_code"], -ts)

    active_tos.sort(key=sort_key)

    # Group by project
    by_project: dict[str, list[dict]] = {}
    for t in active_tos:
        by_project.setdefault(t["project_code"], []).append(t)

    now = datetime.now(tz=timezone.utc)
    now_str = now.strftime("%Y-%m-%dT%H:%MZ")

    # Scope description
    if project_filter:
        scope_desc = f"project {project_filter}"
    elif show_all:
        scope_desc = "all projects (workspace-wide)"
    else:
        scope_desc = f"hot PRD projects (<={LOOKBACK_DAYS}d)"
    if assignee_filter:
        scope_desc += f" assignee~={assignee_filter}"

    print(f"TO-CHECK  {now_str}  |  {len(active_tos)} active TOs  "
          f"|  {len(by_project)} projects  |  scope: {scope_desc}")
    if parse_errors:
        print(f"  PARSE-ERROR ({len(parse_errors)}): "
              + ", ".join(Path(e["path"]).name for e in parse_errors[:5]))
    print()

    to_num = 0
    for code, project_tos in by_project.items():
        blocked = [t for t in project_tos if t["status_class"] == "BLOCKED"]
        pending = [t for t in project_tos if t["status_class"] == "PENDING"]
        active = [t for t in project_tos if t["status_class"] == "ACTIVE"]
        unknown = [t for t in project_tos if t["status_class"] == "UNKNOWN"]
        summary_parts = []
        if active:
            summary_parts.append(f"{len(active)} ACTIVE")
        if pending:
            summary_parts.append(f"{len(pending)} PENDING")
        if blocked:
            summary_parts.append(f"{len(blocked)} BLOCKED")
        if unknown:
            summary_parts.append(f"{len(unknown)} UNKNOWN")
        print(f"Project: {code}  ({', '.join(summary_parts)})")
        for t in project_tos:
            to_num += 1
            label = STATUS_LABELS.get(t["status_class"], t["status_class"])
            age_str = _age(t["issued_date"], now)
            raw_title = clean(t["title"])
            title_short = raw_title[:64] + ("..." if len(raw_title) > 64 else "")
            assignee = clean(_fmt_assignee_full(t["assigned_to"]))
            issued_by = clean(_fmt_issued_by(t["issued_by"]))

            print(f"  #{to_num}  [{label}]  {t['to_id']}  ({age_str})")
            print(f"       Title:  {title_short}")
            print(f"       To:     {assignee}")
            if issued_by:
                print(f"       By:     {issued_by}")
            if t["issued_date"]:
                print(f"       Issued: {t['issued_date']}")
            if t["status_display"]:
                status_short = clean(t["status_display"])[:80]
                print(f"       Status: {status_short}")
            if t["_error"]:
                print(f"       PARSE-ERROR: {t['_error']}")
        print(SEP)

    if not active_tos:
        print("(no active TOs in scope)")

    print(f"\nTO-CHECK-RESULT total={len(active_tos)} projects={len(by_project)} "
          f"blocked={sum(1 for t in active_tos if t['status_class']=='BLOCKED')} "
          f"parse_errors={len(parse_errors)}")


if __name__ == "__main__":
    main()
