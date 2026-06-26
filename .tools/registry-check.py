#!/usr/bin/env python3
"""registry-check.py -- clean What/Where/Why view of active (not-closed) projects.

Companion to fabric-projects.py, but optimized for HUMAN reading: numbered title
rows (code / status / last-commit / owner) with the long phase/description blocks
PARSED OUT into three one-line fields:

  What:  what the project IS              (JSON name -> REGISTRY name -> code)
  Where: where it is at right now         (JSON phase | current_phase -> REGISTRY narrative -> latest commit)
  Why:   why we are / were doing it       (JSON description rationale -> REGISTRY narrative)

Ordered by most recent ASCRIBED commit (a commit whose message references the
project code), newest first. Read-only -- pure filesystem + git, no MCP, no writes.

Usage:
  registry-check.py            HOT only (worked <72h, not closed)
  registry-check.py -all       HOT + COLD (cold = >72h since work, still not closed)
  registry-check.py --json     machine-readable rows (respects -all)

Schema-tolerant: handles both the rich JSON schema (name/description/phase) and
the thin schema (status/current_phase/macro). MALFORMED JSONs are SURFACED, not
silently dropped (the failure mode that hid two completed projects 2026-06-08).
"""
from __future__ import annotations

import datetime
import glob
import json
import os
import re
import subprocess
import sys

# Canonical closed tokens + tolerant synonyms ("completed" is a known drift of "complete").
CLOSED = {"complete", "completed", "closed", "cancelled", "canceled",
          "merged", "superseded", "done", "inactive-closed"}
HOT_HOURS = 72
PROJ_DIR = "org/projects"
REGISTRY = "org/projects/REGISTRY.md"


# ASCII-fold common unicode so the Windows console charmap codec never mangles
# output to U+FFFD or truncates a log line (CLAUDE.md Code Quality -- ASCII only).
_ASCII = {
    "—": "--", "–": "-", "…": "...", "→": "->",
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "✓": "OK", "✗": "x", "×": "x", " ": " ", "•": "*",
}


def to_ascii(t: str) -> str:
    for u, a in _ASCII.items():
        t = t.replace(u, a)
    return t.encode("ascii", "replace").decode("ascii")


def clean(t: str) -> str:
    t = to_ascii(str(t or ""))
    t = re.sub(r"\s+", " ", t).strip()
    t = t.replace("**", "")            # drop markdown bold
    return t


def first_sentence(t: str, maxlen: int) -> str:
    t = clean(t)
    if not t:
        return ""
    m = re.search(r"(?<=[.!?])\s", t)
    s = t[: m.start() + 1] if m else t
    if len(s) > maxlen:
        s = s[: maxlen - 3].rstrip() + "..."
    return s


def load_registry() -> dict:
    """code -> (name_col, narrative_col) from the REGISTRY.md tables."""
    reg = {}
    try:
        lines = open(REGISTRY, encoding="utf-8").read().splitlines()
    except OSError:
        return reg
    for ln in lines:
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        code = cells[0].strip("` ")
        if not re.match(r"^[A-Z][A-Z0-9_]+$", code):
            continue
        name = cells[2] if len(cells) > 2 else ""
        narr = cells[3] if len(cells) > 3 else ""
        reg.setdefault(code, (name, narr))   # first (Active table) wins
    return reg


def git_latest(code: str):
    """Most recent commit referencing the code -> (iso_date, author, subject)."""
    out = subprocess.run(
        ["git", "log", "--all", "-1", "--grep", code,
         "--pretty=format:%cI\t%an\t%s"],
        capture_output=True, text=True, errors="replace",
    ).stdout.strip()
    if not out:
        return (None, "?", "")
    p = out.split("\t", 2)
    return (p[0], p[1] if len(p) > 1 else "?", p[2] if len(p) > 2 else "")


def build_rows():
    reg = load_registry()
    now = datetime.datetime.now(datetime.timezone.utc)
    rows, malformed = [], []
    for f in sorted(glob.glob(os.path.join(PROJ_DIR, "*.json"))):
        code = os.path.basename(f)[:-5]
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            malformed.append({"code": code, "err": f"{type(e).__name__}: {e}"})
            continue
        code = d.get("project_code") or code
        st = str(d.get("status", "")).lower().strip()
        if st in CLOSED:
            continue
        dt, owner, subj = git_latest(code)
        rname, rnarr = reg.get(code, ("", ""))
        what = d.get("name") or rname or code
        where = d.get("phase") or d.get("current_phase") or rnarr or subj or ""
        why = d.get("description") or rnarr or ""
        age_h = None
        if dt:
            age_h = (now - datetime.datetime.fromisoformat(dt)).total_seconds() / 3600
        rows.append({
            "code": code, "status": st or "unknown", "dt": dt, "owner": owner,
            "age_h": age_h,
            "macro": bool(d.get("macro")),
            "macro_code": str(d.get("macro_code") or "").strip(),
            "children": d.get("children") or [],
            "what": first_sentence(what, 100),
            "where": first_sentence(where, 150),
            "why": first_sentence(why, 150),
        })
    rows.sort(key=lambda r: r["dt"] or "", reverse=True)
    hot = [r for r in rows if r["age_h"] is not None and r["age_h"] < HOT_HOURS]
    cold = [r for r in rows if r["age_h"] is None or r["age_h"] >= HOT_HOURS]
    return hot, cold, malformed, now


def short_owner(owner):
    """Serial -> role token: 3.0.0_SA_CVO -> CVO, 0.6.0_AE_PartnerETL -> AE."""
    if not owner or owner == "?":
        return owner or "?"
    parts = owner.split("_")
    if len(parts) >= 3 and parts[1] == "SA":
        return parts[2]            # SA_CTO -> CTO
    if len(parts) >= 2:
        return parts[1]            # 0.6.0_AE_PartnerETL -> AE
    return owner[:12]


def fmt_commit(dt, now):
    """Short last-commit: today -> 'HH:MM (Xh)', older -> 'M/DD (X.Xd)'. ASCII."""
    if not dt:
        return "no ascribed commit"
    d = datetime.datetime.fromisoformat(dt)
    ah = (now - d).total_seconds() / 3600
    if ah < 24:
        return f"{d.strftime('%H:%M')} ({ah:.0f}h)"
    return f"{d.month}/{d.day:02d} ({ah / 24:.1f}d)"


SEP = "-" * 56


def _print_record(i, r, now, indent="", macro_of="", macro_tag=False):
    # Vertical field-per-line record (Andrew-direct 2026-06-08): each field on its
    # own labeled line, What/Where/Why never run together, ASCII-only separators.
    def p(s):
        print(f"{indent}{s}")
    tag = f"  ({macro_of} child)" if macro_of else ("  [MACRO]" if macro_tag else "")
    p(f"#: {i}")
    p(f"Project: {r['code']}{tag}")
    p(f"Status: {r['status']}")
    p(f"Last commit: {fmt_commit(r['dt'], now)} - {short_owner(r['owner'])}")
    p(f"What:  {r['what'] or '-'}")
    p(f"Where: {r['where'] or '-'}")
    p(f"Why:   {r['why'] or '-'}")


def _print_macro_header(m, kid_count, now):
    # A macro is a CONTAINER, not a workstream -- render it as a program header,
    # NOT a numbered What/Where/Why project row (fix: macro masquerading as a row).
    print(f"[MACRO] {m['code']} -- {m['what'] or m['code']}")
    print(f"  Status: {m['status']}  (program container; {kid_count} child project(s) below)")
    print(f"  Why:   {m['why'] or '-'}")
    print(f"  Last:  {fmt_commit(m['dt'], now)} - {short_owner(m['owner'])} (macro charter/PRD)")


def emit(title, rs, now, macros_by_code, start=1):
    # Macro-aware grouping: a macro renders as a header with its child projects
    # nested beneath it (fix: macros + children no longer flat peer rows). A child
    # whose macro lives in a different tier renders solo with a "(<MACRO> child)" tag.
    bar = f"Registry -- {title} ({len(rs)})"
    print(f"\n{bar}\n{'=' * len(bar)}")

    macro_rows = [r for r in rs if r["macro"]]
    macro_codes_here = {m["code"] for m in macro_rows}
    children_by_macro, standalone = {}, []
    for r in rs:
        if r["macro"]:
            continue
        mc = r["macro_code"]
        if mc and mc in macros_by_code and mc != r["code"]:
            children_by_macro.setdefault(mc, []).append(r)
        else:
            standalone.append(r)

    # Display units ordered by recency. A macro unit's recency = newest of (macro, kids).
    # Only macros WITH child projects present get the container-header treatment;
    # a macro:true with no children is an ordinary workstream carrying a family tag
    # (e.g. NFRA_MSGRAPH/ASTN_WSJFT) -> render as a normal row, just [MACRO]-tagged.
    units = []  # (recency_iso, kind, row, kids)
    for m in macro_rows:
        kids = children_by_macro.get(m["code"], [])
        if kids:
            recency = max([m["dt"] or ""] + [k["dt"] or "" for k in kids])
            units.append((recency, "macro", m, kids))
        else:
            units.append((m["dt"] or "", "solo-macro", m, None))
    for r in standalone:
        units.append((r["dt"] or "", "solo", r, None))
    # Orphan children (their macro is in the OTHER tier) -> solo, tagged.
    for mc, kids in children_by_macro.items():
        if mc not in macro_codes_here:
            for k in kids:
                units.append((k["dt"] or "", "orphan", k, None))
    units.sort(key=lambda u: u[0], reverse=True)

    i = start
    first = True
    for recency, kind, row, kids in units:
        if not first:
            print(f"\n{SEP}")
        first = False
        print()
        if kind == "macro":
            _print_macro_header(row, len(kids), now)
            for k in sorted(kids, key=lambda x: x["dt"] or "", reverse=True):
                print()
                _print_record(i, k, now, indent="  ", macro_of=row["code"])
                i += 1
        elif kind == "orphan":
            _print_record(i, row, now, macro_of=row["macro_code"])
            i += 1
        elif kind == "solo-macro":
            _print_record(i, row, now, macro_tag=True)
            i += 1
        else:
            _print_record(i, row, now)
            i += 1
    return i


def main():
    args = [a.lower() for a in sys.argv[1:]]
    allmode = any(a in ("-all", "--all", "all") for a in args)
    jsonmode = "--json" in args
    hot, cold, malformed, now = build_rows()

    if jsonmode:
        out = {"hot": hot, "cold": cold if allmode else [], "malformed": malformed}
        print(json.dumps(out, indent=2, default=str))
        return

    # Macros (macro==true) across BOTH tiers, so a child can resolve its parent
    # even when the two land in different tiers (hot child / cold macro).
    macros_by_code = {r["code"]: r for r in (hot + cold) if r["macro"]}

    cold_hint = "showing HOT + COLD below" if allmode else f"run /registry-check -all for the {len(cold)} cold"
    print(f"REGISTRY  {now.strftime('%Y-%m-%dT%H:%MZ')}  |  {len(malformed)} malformed  |  {cold_hint}")
    n = emit("HOT  (worked <72h, not closed)", hot, now, macros_by_code)
    if allmode:
        emit("COLD  (>72h since work, still not closed)", cold, now, macros_by_code, n)
    if malformed:
        print(f"\nWARN: MALFORMED JSON ({len(malformed)}) -- unparseable, fix these:")
        for m in malformed:
            print(f"   {m['code']}.json -> {m['err']}")
    tail = f"\nSUMMARY: {len(hot)} hot | {len(cold)} cold"
    if malformed:
        tail += f" | {len(malformed)} MALFORMED"
    print(tail)
    print(f"REGISTRY-CHECK-RESULT hot={len(hot)} cold={len(cold)} malformed={len(malformed)}")


if __name__ == "__main__":
    main()
