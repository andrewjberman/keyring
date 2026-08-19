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
  python .tools/to-check.py --proof-board     # DERIVED per-firm x per-phase board from
                                              # PROOF_OF_SPEC instances (TIGHTENING J1
                                              # @1dceb7d61d; read-only, run-and-read)
"""
from __future__ import annotations

import json
import re
import subprocess
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
        # Capture the value to END-OF-LINE. The old `([^`\n]+?)` stopped at the
        # FIRST inline-code backtick, so a markdown status CONTAINING backticks
        # (e.g. **Status:** complete -- ... `MAINT_MARK refs=8` ...) captured
        # nothing -> the TO mis-rendered [??] despite leading with "complete".
        # Capture to EOL, then strip any wrapping backticks. (NFRA registry
        # hygiene 2026-06-29, MSTR-adopted status-format finding.)
        m = re.search(rf"\*\*{re.escape(label)}:\*\*\s*([^\n]+?)\s*$",
                      text, re.MULTILINE | re.IGNORECASE)
        if m:
            return m.group(1).strip().strip("`").strip()
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
        issued_date = _extract_tag_multi(text, "issued_date", "date", "issued") or ""
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

        # Validate issued_date format.
        # ACCEPT ISO-8601 WITH TIME as well as a bare date: TOs authored with
        # <issued>2026-08-19T20:05Z</issued> are as dated as ones carrying
        # <date>2026-07-07</date>, and blanking them made 156 of 359 open TOs
        # read as age-UNKNOWN -- which reads as "no dormancy signal" rather than
        # "the parser could not see the date". Truncate to the date part, then
        # validate exactly as before.
        if issued_date and len(issued_date) >= 10:
            issued_date = issued_date[:10]
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


def _agent_token(raw: str) -> str:
    """Short meaningful agent tag for headline display.
    '0.7.0_AE_CloudOps (+3.0.0_SA_CVO)' -> 'AE_CloudOps +CVO'
    '0.4.0_DS_ClientPlatform~B' -> 'DS_ClientPlatform~B'
    no serial -> first 24 chars or (unassigned)."""
    raw = (raw or "").strip()
    if not raw or raw == "(unassigned)":
        return "(unassigned)"
    serials = re.findall(r"\d+\.\d+\.\d+_([A-Za-z]+_?[A-Za-z]*(?:~[A-Z])?)", raw)
    if serials:
        primary = serials[0]
        extras = ""
        if len(serials) > 1:
            # secondary agents shown by role prefix only (e.g. +CVO)
            extras = " " + " ".join("+" + s.split("_")[0] for s in serials[1:])
        return primary + extras
    return raw[:24]


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


# ---- --proof-board: DERIVED per-firm x per-phase board (TIGHTENING J1 @1dceb7d61d) ---------
# The board is an INSTRUMENT for the attestation owner; the framework's CURRENT STATE prose
# remains the attested RECORD (a derivation, not a second home). Read-only; no S3, no writes.

FIRM_SET = ("49F", "INF", "COT", "MDPF")   # the ratified firm token set (criterion-id grammar)
BOARD_PHASES = ("P1-SCRIPTS", "P2-TIMING", "P3-REPOINTS", "P4-PUBLISHERS", "P5-DECOMMISSION",
                "INVESTIGATION", "NON-BUILD-OTHER")   # the schema's own phase enum, verbatim
_SCHEMA_REQUIRED = ("schema_version", "to_id", "phase", "spec_ref", "assignee",
                    "artifacts_produced", "acceptance", "controls", "declared_exclusions",
                    "surprises", "session_log", "compiler_tools")


def _board_last_touch_map() -> dict[str, int]:
    """ONE streaming git-history walk -> {repo-rel path: last-commit-ts}. The
    state_scan.py build_last_touch_map pattern (4.1s total vs 277ms/call per file).
    encoding= is load-bearing (TIGHTENING J2, landed same session): text=True alone
    decodes with the locale codec and a stray commit byte kills the whole read."""
    r = subprocess.run(["git", "log", "--format=%x01%ct", "--name-only"],
                       cwd=str(WORKSPACE), capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    raw = r.stdout if r.returncode == 0 else ""
    last: dict[str, int] = {}
    ts = 0
    for ln in raw.splitlines():
        if ln.startswith("\x01"):
            try:
                ts = int(ln[1:])
            except ValueError:
                ts = 0
        elif ln and ts and ln not in last:   # log is newest-first: first seen = last touch
            last[ln] = ts
    return last


def _derive_firm(inst: dict) -> str:
    """DECLARED derivation, printed in the board header: the instance's own optional
    `firm` field wins (schema-ratified, additive); else the leading to_id token
    (split on the first -, _ or .) matched against FIRM_SET; else UNPARSED --
    rendered as its own row, never guessed (J1.4 contract row 1)."""
    f = inst.get("firm")
    if isinstance(f, str) and f.upper() in FIRM_SET:
        return f.upper()
    lead = re.split(r"[-_.]", str(inst.get("to_id", "")), maxsplit=1)[0].upper()
    return lead if lead in FIRM_SET else "UNPARSED"


def proof_board() -> int:
    now = datetime.now(tz=timezone.utc)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(WORKSPACE),
                          capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout.strip()[:12]
    # SUBSTRING glob, deliberately wider than the spec's PROOF_OF_SPEC_* prefix: the newest
    # instances name themselves {TO_ID}_PROOF_OF_SPEC[~lane].json (e.g. the 49F P1-CLOSE
    # attestation instance) and a prefix glob silently drops them -- measured 20 dropped of
    # 65 on 2026-08-18, the exact never-dropped defect J1 exists to close.
    matched = sorted(glob.glob(str(WORKSPACE / "org" / "**" / "*PROOF_OF_SPEC*.json"),
                               recursive=True))
    schema_files = [f for f in matched if f.endswith(".schema.json")]
    inst_files = [f for f in matched if not f.endswith(".schema.json")]

    malformed: list[tuple[str, str]] = []   # (relpath, why) -- LISTED, never dropped
    parsed: list[dict] = []
    for f in inst_files:
        rel = str(Path(f).relative_to(WORKSPACE)).replace("\\", "/")
        try:
            d = json.loads(Path(f).read_text(encoding="utf-8", errors="replace"))
        except (OSError, json.JSONDecodeError) as e:
            malformed.append((rel, f"unreadable/unparseable: {e}"))
            continue
        missing = [k for k in _SCHEMA_REQUIRED if k not in d]
        if missing:
            malformed.append((rel, f"missing required key(s): {', '.join(missing)}"))
            continue
        if d.get("phase") not in BOARD_PHASES:
            malformed.append((rel, f"phase not in schema enum: {d.get('phase')!r}"))
            continue
        acc = d.get("acceptance") or []
        mix = {"P": 0, "F": 0, "U": 0}
        for row in acc:
            s = str(row.get("status", "")) if isinstance(row, dict) else ""
            if s == "PASS":
                mix["P"] += 1
            elif s == "FAIL":
                mix["F"] += 1
            else:
                mix["U"] += 1   # the UNCOMPUTABLE/UNVERIFIABLE/N-A family + legacy
        parsed.append({"rel": rel, "firm": _derive_firm(d), "phase": d["phase"],
                       "to_id": str(d.get("to_id", "?")), "mix": mix,
                       "vintage": str(((d.get("spec_ref") or {}).get("vintage_commit")
                                       or "?"))[:9]})

    touch = _board_last_touch_map()
    for p in parsed:
        p["touch"] = touch.get(p["rel"], 0)   # 0 = untracked/uncommitted (shown as such)

    # ---- render -------------------------------------------------------------------------
    print(f"PROOF-BOARD  {now.strftime('%Y-%m-%dT%H:%MZ')}  |  HEAD {head}  |  plane: "
          f"working tree (untracked instances included; last-touch from git history)")
    print("  derivation: firm = instance 'firm' field if declared, else leading to_id token "
          f"in {{{','.join(FIRM_SET)}}}, else UNPARSED (own row, never guessed)")
    print(f"  denominators: {len(parsed)} instances parsed of {len(matched)} files matched "
          f"({len(schema_files)} schema excluded); {len(malformed)} MALFORMED (listed below)"
          if malformed else
          f"  denominators: {len(parsed)} instances parsed of {len(matched)} files matched "
          f"({len(schema_files)} schema excluded); 0 MALFORMED")
    print("  cell = instances | acceptance-row mix P(ASS)/F(AIL)/U(NCOMPUTABLE-family). "
          "UNKNOWN(0) = no instance -- never 'not started', never blank.")
    print()

    firms = list(FIRM_SET) + ["UNPARSED"]
    cells: dict[tuple[str, str], list[dict]] = {}
    for p in parsed:
        cells.setdefault((p["firm"], p["phase"]), []).append(p)

    colw = 15
    print("  " + "phase \\ firm".ljust(18) + "".join(f.ljust(colw) for f in firms))
    for ph in BOARD_PHASES:
        row = ["  " + ph.ljust(18)]
        for fm in firms:
            grp = cells.get((fm, ph))
            if not grp:
                row.append("UNKNOWN(0)".ljust(colw))
            else:
                m = {"P": 0, "F": 0, "U": 0}
                for g in grp:
                    for k in m:
                        m[k] += g["mix"][k]
                row.append(f"{len(grp)} P{m['P']}/F{m['F']}/U{m['U']}".ljust(colw))
        print("".join(row))

    print()
    for ph in BOARD_PHASES:
        for fm in firms:
            grp = cells.get((fm, ph))
            if not grp:
                continue
            newest = max(grp, key=lambda g: g["touch"])
            when = (datetime.fromtimestamp(newest["touch"], tz=timezone.utc)
                    .strftime("%m-%d %H:%M") + "Z" if newest["touch"]
                    else "UNTRACKED/uncommitted")
            print(f"  {fm} x {ph}: {len(grp)} instance(s) | newest touch {when} "
                  f"{Path(newest['rel']).name} | its spec vintage @{newest['vintage']}")
    if any(p["firm"] == "UNPARSED" for p in parsed):
        print("\n  UNPARSED rows (no firm field, no firm token leading to_id -- re-key or "
              "declare `firm` to place them):")
        for p in parsed:
            if p["firm"] == "UNPARSED":
                print(f"    {p['to_id'][:60]:60s} {Path(p['rel']).name}")
    if malformed:
        print("\n  MALFORMED (counted in denominator, excluded from cells):")
        for rel, why in malformed:
            print(f"    MALFORMED: {rel} -- {clean(why)[:100]}")
    print(f"\nPROOF-BOARD-RESULT files={len(matched)} instances={len(parsed)} "
          f"malformed={len(malformed)} schema_excluded={len(schema_files)}")
    return 0


def main():
    args = sys.argv[1:]
    if "--proof-board" in args:
        sys.exit(proof_board())
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

            agent_tag = to_ascii(_agent_token(t["assigned_to"]))
            print(f"  #{to_num}  [{label}]  {t['to_id']}  ->  {agent_tag}  ({age_str})")
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

    # BY AGENT rollup -- the TO->agent roster view (one line per TO under each agent).
    # Grouped by PRIMARY agent only so joint-assignee TOs don't split an agent's count.
    if active_tos:
        by_agent: dict[str, list[dict]] = {}
        for t in active_tos:
            primary = _agent_token(t["assigned_to"]).split(" ")[0]
            by_agent.setdefault(primary, []).append(t)
        print("\n== BY AGENT ==")
        for agent in sorted(by_agent, key=lambda a: (-len(by_agent[a]), a)):
            tos = by_agent[agent]
            # recover the full primary serial for precision
            m = re.search(r"\d+\.\d+\.\d+_\S+", (tos[0]["assigned_to"] or ""))
            serial = f" ({m.group(0).rstrip(',)')})" if m else ""
            print(f"{to_ascii(agent)}{serial} -- {len(tos)} TO(s):")
            for t in tos:
                label = STATUS_LABELS.get(t["status_class"], t["status_class"])
                title_short = clean(t["title"])[:48]
                print(f"    [{label}] {t['to_id']} -- {title_short}")

    print(f"\nTO-CHECK-RESULT total={len(active_tos)} projects={len(by_project)} "
          f"blocked={sum(1 for t in active_tos if t['status_class']=='BLOCKED')} "
          f"parse_errors={len(parse_errors)}")


if __name__ == "__main__":
    main()
