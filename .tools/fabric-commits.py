#!/usr/bin/env python3
"""
fabric-commits.py -- commit scraper: maps git commits to project codes + authors.

Deterministic enrichment source for the fabric suite:
  - fabric-projects.py uses it to compute each project's last-activity (hot/cold) +
    "what was done" (recent commit subjects per project).
  - fabric-check.py uses it to map each agent to the project(s) it has been committing to.

Read-only (git log). Project codes are the org/projects/*.json basenames; commit
subjects reference them as feat(CODE)/proj(CODE)/close(CODE) prefixes or inline
(e.g. "MDLP I1+I2", "INF_D_04"). Codes can be prefixes of each other
(ADHC_COMPIL vs ADHC_COMPIL_V4) -> matched longest-first with consume so the
specific code wins.

Usage:
  python .tools/fabric-commits.py                 # per-project commit summary, last 30d
  python .tools/fabric-commits.py --days 7        # window override
  python .tools/fabric-commits.py --project NFRA  # one project's commits
  python .tools/fabric-commits.py --by-author     # group by committing agent
  python .tools/fabric-commits.py --json          # structured (for the other scripts)
"""
from __future__ import annotations
import glob
import json
import os
import subprocess
import sys
import time

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
PROJECTS_DIR = os.path.join(ROOT, "org", "projects")

DEFAULT_DAYS = 30
US = "\x1f"  # unit separator for git pretty-format field split


def project_codes() -> list[str]:
    """All project codes (org/projects/*.json basenames), longest-first for match precedence."""
    codes = set()
    try:
        for p in glob.glob(os.path.join(PROJECTS_DIR, "*.json")):
            codes.add(os.path.splitext(os.path.basename(p))[0])
    except OSError:
        pass
    return sorted(codes, key=len, reverse=True)


def scrape(days: int = DEFAULT_DAYS) -> list[dict]:
    """Raw commit list (sha, author, ts_unix, subject) since `days` ago."""
    fmt = US.join(["%H", "%an", "%at", "%s"])
    try:
        out = subprocess.run(
            ["git", "log", f"--since={days} days ago", "--no-merges",
             f"--pretty=format:{fmt}"],
            cwd=ROOT, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=90,
        )
        lines = out.stdout.splitlines()
    except (OSError, subprocess.SubprocessError):
        lines = []
    commits = []
    for ln in lines:
        parts = ln.split(US)
        if len(parts) >= 4:
            try:
                ts = int(parts[2])
            except ValueError:
                continue
            commits.append({"sha": parts[0][:9], "author": parts[1],
                            "ts": ts, "subject": parts[3]})
    return commits


def match_codes(text: str, codes: list[str]) -> list[str]:
    """Codes referenced in text, longest-first with consume (specific code wins over its prefix)."""
    found = []
    t = text
    for c in codes:
        if c in t:
            found.append(c)
            t = t.replace(c, " ")  # consume so a shorter prefix doesn't re-match this span
    return found


def by_project(days: int = DEFAULT_DAYS, codes: list[str] | None = None) -> dict:
    """{code: [commits...]} newest-first. A commit can map to multiple codes (real: close(A + B))."""
    if codes is None:
        codes = project_codes()
    commits = scrape(days)
    out: dict[str, list[dict]] = {}
    for c in commits:
        for code in match_codes(c["subject"], codes):
            out.setdefault(code, []).append(c)
    for code in out:
        out[code].sort(key=lambda x: x["ts"], reverse=True)
    return out


def by_author(days: int = DEFAULT_DAYS) -> dict:
    """{author: [commits...]} newest-first."""
    out: dict[str, list[dict]] = {}
    for c in scrape(days):
        out.setdefault(c["author"], []).append(c)
    for a in out:
        out[a].sort(key=lambda x: x["ts"], reverse=True)
    return out


def _age(sec: float) -> str:
    if sec < 0:
        return "?"
    if sec < 5400:
        return f"{int(sec/60)}m"
    if sec < 172800:
        return f"{int(sec/3600)}h"
    return f"{int(sec/86400)}d"


def main():
    args = sys.argv[1:]
    days = DEFAULT_DAYS
    if "--days" in args:
        try:
            days = int(args[args.index("--days") + 1])
        except (ValueError, IndexError):
            pass
    proj = None
    if "--project" in args:
        try:
            proj = args[args.index("--project") + 1]
        except IndexError:
            pass
    now = time.time()

    if "--json" in args:
        print(json.dumps({"days": days, "ts": now,
                          "by_project": by_project(days),
                          "by_author": by_author(days)}, indent=2))
        return

    if "--by-author" in args:
        ba = by_author(days)
        print(f"COMMITS BY AGENT (last {days}d): {sum(len(v) for v in ba.values())} commits, {len(ba)} agents")
        for a in sorted(ba, key=lambda x: -len(ba[x])):
            cs = ba[a]
            print(f"  {a:<32} {len(cs):>3} commits | latest {_age(now-cs[0]['ts'])} ago: {cs[0]['subject'][:80]}")
        return

    bp = by_project(days)
    if proj:
        cs = bp.get(proj, [])
        print(f"COMMITS for {proj} (last {days}d): {len(cs)}")
        for c in cs:
            print(f"  {c['sha']} {_age(now-c['ts']):>5} ago {c['author']:<28} {c['subject'][:90]}")
        return

    print(f"COMMITS BY PROJECT (last {days}d): {len(bp)} projects touched")
    for code in sorted(bp, key=lambda x: -bp[x][0]['ts']):
        cs = bp[code]
        print(f"  {code:<26} {len(cs):>3} commits | last {_age(now-cs[0]['ts']):>5} ago by {cs[0]['author']}: {cs[0]['subject'][:70]}")


if __name__ == "__main__":
    main()
