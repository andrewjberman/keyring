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
    "—": "--", "–": "-", "…": "...", "\u2192": "->",
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
                  "superseded", "withdrawn", "done", "merged", "decommissioned", "dropped",
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


# ---------------------------------------------------------------------------------------------
# FIX C -- STATUS READ OFF WORKER-FACE PROSE. `_extract_tag` takes the FIRST `<status>` in the
# file and runs non-greedily to the NEXT `</status>`. A spine-v3 worker face INSTRUCTS the worker
# to "flip this file's `<status>` to `complete`" -- an UNPAIRED inline mention, usually inside
# backticks -- so that mention OPENS the match and the record element's own closing tag CLOSES
# it. The captured value is then the prose BETWEEN them, and `_classify_status` grades prose: its
# first token is a backtick, which matches no word set, so it falls through to ACTIVE.
#
# Measured 2026-09-12 on AMGT_RESAPP round 7 (rows AMGT_RESAPP-Z-S36 and -Z-S42): six orders
# reported ACTIVE against six literal `<status>complete</status>` record faces and zero open
# orders. The same count reaches the DIRECTIVES REGISTER, because directives-check.py:83
# `open_tos()` shells out to this tool and reprints its per-project line -- so D5 stated six open
# orders against a measured zero. Cause located by 3.0.0_SA_CVO~Z in REMEDIATION_v7 @00e0813b9d.
#
# THE DISCRIMINATOR IS THE BACKTICK, AND IT WAS FOUND BY MEASUREMENT, NOT BY REASONING. Every
# spurious `<status>` token in this corpus is an INLINE CODE SPAN -- prose ABOUT the tag, written
# between backticks. The two failing shapes are mirror images and no rule on the bare token tells
# them apart:
#   AMGT_RESAPP rf-*  a backticked mention BEFORE the element ("flip this file's `<status>` to
#                     `complete`"), which the old first-open search takes as the opener.
#   ETFS_POSITIONING  an element whose own CONTENT holds a backticked mention ("**`<status>` TAG
#     TO-6, TO-3       ADDED 2026-08-28 ...") -- so a nearest-opener rule skips the REAL opener.
# Masking inline code spans before locating the tag fixes both, and leaves a SET file
# (D7_NOTIFY.TO-SET.md, six orders in one file, first status a SPRING-CLEAN prose closure) reading
# exactly as it always has.
#
# WARN: TWO WRONG FIXES WERE WRITTEN BEFORE THIS ONE AND BOTH WERE CAUGHT THE SAME WAY -- by running
# the patched tool against HEAD's copy over the whole estate at the same instant, and asking which
# projects moved. A "single bare token" test reopened six closed projects; a non-nesting-pair test
# turned 130 active TOs into 144 by capturing prose in the mirror shape. NEITHER would have been
# caught by testing the case that motivated the fix. The prediction to hold the fix to: EXACTLY
# ONE project moves, and the project SET is unchanged.
#
# SCOPED TO STATUS ONLY: `_extract_tag` itself is unchanged and every other tag reads as before.
# ---------------------------------------------------------------------------------------------
_CODE_SPAN_RE = re.compile(r"`[^`\n]*`")


def _extract_status_tag(text: str) -> str | None:
    """The status ELEMENT, located with inline code spans masked so prose about the tag is inert.

    The mask is used ONLY to find the span; the value is sliced out of the ORIGINAL text, so a
    status whose value legitimately contains backticks is returned intact.
    """
    masked = _CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), text)
    m = re.search(r"<status>(.*?)</status>", masked, re.DOTALL | re.IGNORECASE)
    if not m:
        return _extract_tag(text, "status")
    return _strip_xml_comments(text[m.start(1):m.end(1)]).strip()


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


SERIAL_RE = re.compile(r"\d\.\d\.\d_[A-Za-z]+_[A-Za-z0-9]+(?:~[A-Z])?")

# ---------------------------------------------------------------------------------------------
# FIX A -- SCHEMA BLINDNESS. _extract_tag reads CHILD ELEMENTS only, so on an attribute-form TO
# (<task_order id="..." project="...">) BOTH to_id and project returned None and resolution fell
# through to the FILENAME. Measured on the live corpus: 106 attribute-form / 655 child-form /
# 1,316 neither, of 2,077 TO files (one grain, sums to the corpus).
# ---------------------------------------------------------------------------------------------
def _extract_attr(text: str, attr: str) -> str | None:
    """Read `attr="value"` off the <task_order ...> open tag. Child element wins; this is the
    fallback, so a TO carrying both forms keeps its historical answer."""
    m = re.search(r"<task_order\b[^>]*>", text, re.IGNORECASE)
    if not m:
        return None
    a = re.search(rf'\b{re.escape(attr)}\s*=\s*"([^"]*)"', m.group(0), re.IGNORECASE)
    return a.group(1).strip() if a and a.group(1).strip() else None


# ---------------------------------------------------------------------------------------------
# FIX C -- ROLE RESOLUTION. THE TOOL'S DEFECT WAS NEVER "IT READS THE WRONG FIELD"; IT IS THAT A
# SERIAL APPEARING IN A TO IS NOT AN ASSIGNMENT. One live <status> block carries three serials in
# three roles (assigner / assignee / assignee), and corpus-wide the ACTOR notation outnumbers the
# unambiguous TARGET notation 50 to 4 (occurrence counts, across 78 serial-bearing <status> blocks
# -- TWO GRAINS, stated separately on purpose).
#
# SO THIS READER IS DELIBERATELY NARROW: an assignment is recognised ONLY in an unambiguous target
# position; everything else is NOT-AN-ASSIGNMENT rather than assumed-one, and the residue is
# COUNTED AND PRINTED. A narrow reader that declares its narrowness beats a broad one that cannot
# defend its inclusions -- a token sweep would have passed the known exercise while misattributing
# at fifty-file scale.
# ---------------------------------------------------------------------------------------------
_ACTOR_RE = re.compile(r"\b(?:by|per|from|via)\s+$", re.IGNORECASE)
_TARGET_RE = re.compile(r"(?:->|=>|\u2192|=|\bto\b|:)\s*$", re.IGNORECASE)
# LEAD POSITION: a serial that OPENS the field is its subject -- "<serial> (build; site-Z).
# Laptop apply leg = ... via <other> ferry" names the assignee first and then annotates.
# MEASURED: 6 of this seat's 7 live TOs use exactly that shape, and a LATER serial in the
# same field is the ferry/actor, not a second assignee.
_LEAD_RE = re.compile(r"^[\s*_`\"'(\[]*$")
# GLOSS: "NAME (<serial>) = role" -- the serial is a parenthetical gloss and the assignment
# marker follows the closing paren. Discriminating, MEASURED in one live field: the ferry
# serial in that same field also sits inside parens but is not followed by ") =", so it
# stays out. Keyed on the marker AFTER the paren, never on being inside one.
_GLOSS_RE = re.compile(r"^\s*\)\s*(?:=(?!=)|->|:)")


def _assignees_from_field(raw: str) -> tuple[list[str], int]:
    """-> (assignee serials, unclassified serial occurrences) for ONE field's text.

    Two shapes, and only two are trusted:
      BARE     the field is essentially just serial(s) -- <issued_to>0.5.0_AE_OpalETL~Z</issued_to>
               -- every serial is an assignee by construction. This is the common case and it is
               what keeps the historical answers stable.
      TARGETED prose, and the serial sits immediately after an explicit target marker (-> => to:).
    Anything else is UNCLASSIFIED and counted, never assumed. An ACTOR marker (by/per/from/via)
    is an explicit non-assignment and is not counted as residue.
    """
    if not raw:
        return [], 0
    text = _strip_xml_comments(raw)
    serials = list(SERIAL_RE.finditer(text))
    if not serials:
        return [], 0
    # BARE: an assignee LIST may carry per-serial role annotations in parens/brackets --
    # "0.4.0_DS~B (DS-items) + 0.5.0_AE_OpalETL (store-writer)" is a TWO-ASSIGNEE FIELD, not
    # prose. MEASURED: rejecting that shape dropped 20 live TOs from their own assignees.
    # Annotations are stripped BEFORE the test, and this does NOT re-admit the assigner case:
    # "site Z, seats assigned by X (note)" still leaves "site Z, seats assigned by" as residue
    # and falls through to the per-serial role rules below, where "by" is an explicit no.
    annot = re.sub(r"\([^)]*\)|\[[^\]]*\]", " ", text)
    residue = SERIAL_RE.sub("", annot)
    if not re.sub(r"[\s,;/&+|-]|\band\b|\bor\b", "", residue, flags=re.IGNORECASE):
        return [m.group(0) for m in serials], 0
    out, unclassified = [], 0
    for m in serials:
        before = text[max(0, m.start() - 24):m.start()]
        if _LEAD_RE.match(text[:m.start()]):
            out.append(m.group(0))       # the field opens with it: it is the subject
            continue
        after = text[m.end():m.end() + 10]
        if _GLOSS_RE.match(after):
            out.append(m.group(0))       # "NAME (<serial>) = role" -- a glossed assignee
            continue
        if _ACTOR_RE.search(before):
            continue                      # explicit non-assignment: not residue, a known no
        if _TARGET_RE.search(before):
            out.append(m.group(0))
        else:
            unclassified += 1
    return out, unclassified


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
    # WAS `return to_id.upper()`. That NEVER returned empty for a non-empty to_id, so every
    # caller's "if not project_code -> consult the DECLARED field" branch was UNREACHABLE and
    # the TO's own <project> / project="..." statement was dead code. Returning "" is what
    # makes the declared field REACHABLE. It deliberately does not make it DOMINANT: to_id
    # stays primary, so historical classification does not move under a tooling fix.
    return ""


def parse_to_file(path: str) -> dict:
    """Parse a TO file. Handles XML (new + old schema) and Markdown formats.
    Never drops -- surfaces parse errors in _error field."""
    fname = Path(path).name
    try:
        text = Path(path).read_text(encoding="utf-8", errors="replace")

        # XML fields -- new schema with old-schema fallbacks
        to_id = _extract_tag_multi(text, "to_id") or ""
        if not to_id:
            candidate = _extract_tag_multi(text, "id") or _extract_attr(text, "id") or ""
            if re.match(r"^[A-Z][A-Z0-9_]{2,}", candidate.upper()):
                to_id = candidate

        # FIX A: attribute form is a FALLBACK, never an override -- a TO carrying both keeps its
        # historical answer, so this widens coverage without moving anything already resolved.
        project_field = (_extract_tag_multi(text, "project", "project_code")
                         or _extract_attr(text, "project") or "")
        title = _extract_tag_multi(text, "title") or ""
        assigned_to = _extract_tag_multi(text, "assigned_to", "issued_to") or ""
        issued_by = _extract_tag_multi(text, "issued_by") or ""
        issued_date = _extract_tag_multi(text, "issued_date", "date", "issued") or ""
        status_raw = _extract_status_tag(text) or ""   # FIX C: the record element, never the prose
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

        # Project code resolution.
        # FIX B -- PRECEDENCE, NOT EXTRACTION. _extract_project_code_from_to_id returns
        # to_id.upper() when its regex does not match, so it NEVER returns empty for a non-empty
        # to_id -- which made the `if not project_code` branch below UNREACHABLE and the DECLARED
        # <project>/project="..." field dead code on every TO that had a to_id. The declared field
        # is the TO's own statement of its project and now wins; the to_id-derived code remains the
        # fallback, and the filename remains the last resort.
        project_code = _extract_project_code_from_to_id(to_id)
        # THE DECLARED CODE IS AN ADDITIONAL WAY TO REACH THIS TO, NOT A COMPETITOR TO THE
        # to_id-derived one. Making it WIN reclassified D7 wholesale (D7_TICKETING -> 0);
        # leaving it as a fallback left it provably dead (no to_id in the corpus fails the
        # code-shape test). Both codes are kept: to_id-derived for DISPLAY and grouping so
        # nothing historical moves, and the union for FILTERING so a TO is findable under the
        # project it DECLARES as well. The registration mismatch is then VISIBLE instead of
        # silently adjudicated by a tool that has no standing to pick.
        m_decl = re.match(r"^([A-Z][A-Z0-9_]{2,})", project_field.upper())
        declared_code = m_decl.group(1) if m_decl else ""
        if not project_code:
            project_code = declared_code
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

        # FIX C: resolve ROLE across BOTH recording sites. <issued_to> is prose that carries the
        # assigner AND the assignee ("seats assigned by X ... -> Y"), so the same role rules apply
        # to it -- reading only <status> would have left the live FALSE POSITIVE untouched.
        a_field, u_field = _assignees_from_field(assigned_to)
        a_status, u_status = _assignees_from_field(status_raw)
        assignee_serials = list(dict.fromkeys(a_field + a_status))
        unresolved_serials = u_field + u_status

        return {
            "to_id": to_id or fname.replace(".md", ""),
            "project_code": project_code,
            "project_codes": [c for c in dict.fromkeys([project_code, declared_code]) if c],
            "title": title,
            "assigned_to": assigned_to or "(unassigned)",
            "assignee_serials": assignee_serials,
            "unresolved_serials": unresolved_serials,
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
            "project_codes": ["UNKNOWN"],
            "title": "(parse error)",
            "assigned_to": "(unknown)",
            "assignee_serials": [],
            "unresolved_serials": 0,
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
    # TWO ROOTS (project-tree spec s.7, CVO residual R-ii): seat task_orders/ AND the tree's
    # org/missions/D*/<MACRO>/<PROJECT>/task-orders/ (contract task_orders_glob).
    flat = glob.glob(str(WORKSPACE / "org" / "**" / "task_orders" / "*.md"), recursive=True)
    tree = glob.glob(str(WORKSPACE / "org" / "missions" / "D*" / "*" / "*" / "task-orders" / "*.md"))
    return flat + tree


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


def third_population(tos: list[dict]) -> list[dict]:
    """THE THIRD PRINTED POPULATION (tool-owner disposition 1.0.0_SA_CTO~X 80520, CVO-accepted;
    landed by 1.0.0_SA_CTO~Y under the D11 split 80816 (c)).

    Faces that carry a <status> tag (or a markdown Status field) and NO recognised assignment
    field at all -- no <assigned_to>/<issued_to>, none of the markdown fields Owner / Assigned to /
    Assignee. Such a face never reaches _assignees_from_field, so it contributes NOTHING to
    `unresolved_serials`: it is invisible in the one direction that has no disclosure. Measured
    2026-08-29 (@12a2031f2c): three freshly-cut wave-2 faces addressed as `**to:** <serial>` rendered
    (unassigned) and the seating census read 0 open TOs for all three. The contract does NOT widen
    (`**to:**` is not admitted); the silence becomes a number, printed on every run beside the
    residue with the denominator.
    """
    return [t for t in tos
            if not t.get("_error")
            and (t.get("status_raw") or "").strip()
            and t.get("assigned_to") in ("(unassigned)", "", None)]


def third_population_selftest() -> int:
    """Both control arms, exercised on fixtures written to a temp dir and parsed by the SAME
    parse_to_file the live run uses. POSITIVE: a face carrying only `**to:** <serial>` MUST land
    in the population. NEGATIVE: a face with <assigned_to> MUST NOT. THIRD: a face with no
    <status> tag at all MUST NOT (it is not a face with a status tag). Exit 0 only if all fire."""
    import tempfile
    fixtures = {
        "pos_to_only.md": ("# TASK ORDER -- fixture\n<status>pending</status>\n<project>NFRA_SELFTEST</project>\n"
                           "**to:** `1.0.0_SA_CTO~Y` -- **issuer:** `2.0.0_SA_COO~X`\n"),
        "neg_assigned_to.md": ("# TASK ORDER -- fixture\n<status>pending</status>\n<assigned_to>1.0.0_SA_CTO~Y</assigned_to>\n"
                               "<project>NFRA_SELFTEST</project>\n"),
        "neg_no_status.md": ("# TASK ORDER -- fixture\n<project>NFRA_SELFTEST</project>\n**to:** `1.0.0_SA_CTO~Y`\n"),
    }
    expect = {"pos_to_only.md": True, "neg_assigned_to.md": False, "neg_no_status.md": False}
    ok = True
    with tempfile.TemporaryDirectory() as d:
        parsed = []
        for name, body in fixtures.items():
            p = Path(d) / name
            p.write_text(body, encoding="utf-8")
            parsed.append(parse_to_file(str(p)))
        pop = {Path(t["path"]).name for t in third_population(parsed)}
        for name, want in expect.items():
            got = name in pop
            arm = "PASS" if got == want else "FAIL"
            ok &= (got == want)
            print(f"  third-population selftest {arm}: {name} in_population={got} expected={want}")
    print(f"third-population selftest: {'PASS 3/3' if ok else 'FAIL'} (denominator 3 arms)")
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if "--proof-board" in args:
        sys.exit(proof_board())
    if "--third-population-selftest" in args:
        sys.exit(third_population_selftest())
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

    # THE THIRD POPULATION is taken over the WHOLE parsed corpus, HERE, before any scope filter and
    # before the BY-AGENT rollup below rebinds the name `tos` to one agent's list (a shadow that
    # made this line print 0 of 2181 against a raw-text census of 84 on its first run, 2026-08-29).
    _third_all = third_population(tos)

    # Filter: exclude COMPLETE unless --all with explicit intent
    active_tos = [t for t in tos if t["status_class"] != "COMPLETE"]

    # Scope filter
    if project_filter:
        # match ANY code the TO is reachable by -- to_id-derived OR declared
        active_tos = [t for t in active_tos
                      if project_filter in t.get("project_codes", [t["project_code"]])]
    elif hot_codes is not None:
        active_tos = [t for t in active_tos if t["project_code"] in hot_codes]

    # Assignee filter
    if assignee_filter:
        # ROLE, NOT SUBSTRING. The old form matched any occurrence in <issued_to> prose, so a TO
        # reading "seats assigned BY <serial>" was returned as that serial's assignment -- a live
        # false positive, in the same query and the same file as the known undercount.
        active_tos = [t for t in active_tos
                      if any(assignee_filter in s.lower() for s in t.get("assignee_serials", []))]

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

    # THE DENOMINATOR. `scanned` is the corpus this answer is over; `unresolved_serials` is
    # the NARROW role reader's residue. Printing both is the whole difference from a tool that
    # answered "1" and meant nothing of the kind.
    _unres = sum(t.get("unresolved_serials", 0) for t in active_tos)
    print(f"\nTO-CHECK-RESULT total={len(active_tos)} projects={len(by_project)} "
          f"blocked={sum(1 for t in active_tos if t['status_class']=='BLOCKED')} "
          f"parse_errors={len(parse_errors)} scanned={len(to_files)} "
          f"unresolved_serials={_unres}")
    if _unres:
        print("  NOTE: " + str(_unres) + " serial-shaped token(s) in these TOs sit in NO "
              "recognised assignment notation. They are UNCLASSIFIED, not counted as "
              "non-assignments -- a real assignee written in an unusual notation lands here. "
              "Widen the notation set; do not read this residue as zero.")

    # THE THIRD POPULATION -- printed on EVERY run, over the whole scanned corpus, never over the
    # scope filter: faces with a <status> tag and NO recognised assignment field. These reach
    # neither `assignee_serials` nor `unresolved_serials`; without this line their silence reads
    # as a clean zero on the seating census. Denominator = scanned; "open" = not COMPLETE.
    _third = _third_all
    _third_open = [t for t in _third if t["status_class"] != "COMPLETE"]
    _to_marker = re.compile(r"\*\*to:\*\*")
    _third_to = [t for t in _third
                 if _to_marker.search(Path(t["path"]).read_text(encoding="utf-8", errors="replace"))]
    print(f"  THIRD-POPULATION: {len(_third)} of {len(to_files)} faces carry a <status> tag and NO "
          f"recognised assignment field ({len(_third_open)} open; {len(_third_to)} of them address a "
          f"seat as `**to:**`, the unrecognised notation). They are outside BOTH counts above; the "
          f"contract does not widen -- fix the face's field, then re-run.")
    _root = WORKSPACE.resolve()
    for t in sorted(_third, key=lambda t: t["path"]):
        flag = "OPEN" if t["status_class"] != "COMPLETE" else "complete"
        mark = " **to:**" if t in _third_to else ""
        p = Path(t["path"]).resolve()
        try:
            shown = p.relative_to(_root).as_posix()
        except ValueError:
            shown = p.as_posix()
        print(f"    [{flag}]{mark} {shown}")


if __name__ == "__main__":
    main()
