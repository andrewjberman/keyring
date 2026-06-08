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
            "what": first_sentence(what, 100),
            "where": first_sentence(where, 150),
            "why": first_sentence(why, 150),
        })
    rows.sort(key=lambda r: r["dt"] or "", reverse=True)
    hot = [r for r in rows if r["age_h"] is not None and r["age_h"] < HOT_HOURS]
    cold = [r for r in rows if r["age_h"] is None or r["age_h"] >= HOT_HOURS]
    return hot, cold, malformed, now


def fmt_dt(dt, now):
    if not dt:
        return "no ascribed commit"
    d = datetime.datetime.fromisoformat(dt)
    ah = (now - d).total_seconds() / 3600
    ago = f"{ah/24:.1f}d ago" if ah >= 24 else f"{ah:.0f}h ago"
    return d.strftime("%Y-%m-%d %H:%M") + f"  ({ago})"


def emit(title, rs, now, start=1):
    bar = f"{title} ({len(rs)})"
    print(f"\n{bar}\n{'=' * len(bar)}")
    for i, r in enumerate(rs, start):
        print(f"\n{i}. {r['code']}  [{r['status']}]  {fmt_dt(r['dt'], now)}  by {r['owner']}")
        print(f"   What:  {r['what'] or '-'}")
        print(f"   Where: {r['where'] or '-'}")
        print(f"   Why:   {r['why'] or '-'}")
    return start + len(rs)


def main():
    args = [a.lower() for a in sys.argv[1:]]
    allmode = any(a in ("-all", "--all", "all") for a in args)
    jsonmode = "--json" in args
    hot, cold, malformed, now = build_rows()

    if jsonmode:
        out = {"hot": hot, "cold": cold if allmode else [], "malformed": malformed}
        print(json.dumps(out, indent=2, default=str))
        return

    scope = "HOT + COLD" if allmode else "HOT only  (run with -all to include cold)"
    print(f"REGISTRY CHECK  ({now.strftime('%Y-%m-%dT%H:%MZ')})  --  {scope}")
    n = emit("HOT  (worked <72h, not closed)", hot, now)
    if allmode:
        emit("COLD  (>72h since work, still not closed)", cold, now, n)
    if malformed:
        print(f"\n⚠ MALFORMED JSON ({len(malformed)}) -- unparseable, fix these:")
        for m in malformed:
            print(f"   {m['code']}.json -> {m['err']}")
    tail = f"\nSUMMARY: {len(hot)} hot | {len(cold)} cold"
    if malformed:
        tail += f" | {len(malformed)} MALFORMED"
    print(tail)
    print(f"REGISTRY-CHECK-RESULT hot={len(hot)} cold={len(cold)} malformed={len(malformed)}")


if __name__ == "__main__":
    main()
