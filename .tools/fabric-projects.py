#!/usr/bin/env python3
"""
fabric-projects.py -- HOT / COLD active-project status, deterministic + structured.

Reads org/projects/*.json (the registered projects), keeps only the NOT-closed ones
(status not in complete/closed/cancelled/merged), and partitions them by recency of work:

  HOT  = last activity within 72h   (actively in flight; needs a live owner + monitoring)
  COLD = last activity older than 72h, still not closed (closure-debt or stalled; review)

"Last activity" = max(project-JSON mtime, latest commit referencing the code) -- enriched
via fabric-commits.py (the commit scraper). Each project gets a <=2-sentence status derived
deterministically from current_phase + blocking + the latest commit subject.

Read-only. Usage:
  python .tools/fabric-projects.py            # HOT then COLD
  python .tools/fabric-projects.py --hot      # hot only
  python .tools/fabric-projects.py --cold     # cold only
  python .tools/fabric-projects.py --json     # structured
"""
from __future__ import annotations
import glob
import json
import os
import subprocess
import sys
import time
from collections import Counter

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
PROJECTS_DIR = os.path.join(ROOT, "org", "projects")
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))

HOT_S = 72 * 3600                 # 72h
COMMIT_WINDOW_DAYS = 30           # how far back the scraper looks for last-activity
CLOSED = {"complete", "closed", "cancelled", "canceled", "merged", "superseded", "done"}


def commit_map(days: int) -> dict:
    """{code: [commits]} from fabric-commits.py --json (decoupled subprocess)."""
    try:
        out = subprocess.run(
            [sys.executable, os.path.join(TOOLS_DIR, "fabric-commits.py"),
             "--json", "--days", str(days)],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120,
        )
        return json.loads(out.stdout).get("by_project", {})
    except (OSError, ValueError, subprocess.SubprocessError):
        return {}


def load_projects() -> list[dict]:
    rows = []
    for path in glob.glob(os.path.join(PROJECTS_DIR, "*.json")):
        code = os.path.splitext(os.path.basename(path))[0]
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                d = json.load(f)
        except (OSError, ValueError):
            d = {}
        try:
            mtime = os.path.getmtime(path)
        except OSError:
            mtime = 0.0
        rows.append({
            "code": code,
            "status": str(d.get("status", "unknown")).lower(),
            "phase": d.get("current_phase") or d.get("phase") or "",
            "owner": d.get("owner") or d.get("owners") or "",
            "blocking": d.get("blocking") or d.get("blocker") or "",
            "mtime": mtime,
        })
    return rows


def first_sentences(text: str, n: int = 2, cap: int = 260) -> str:
    """First n sentences (deterministic), capped. ASCII-clean for Windows-safe output."""
    if not text:
        return ""
    t = " ".join(str(text).split())
    # map common unicode to ascii, drop the rest
    for u, a in (("—", "-"), ("–", "-"), ("’", "'"), ("“", '"'),
                 ("”", '"'), ("…", "..."), ("‘", "'")):
        t = t.replace(u, a)
    t = t.encode("ascii", "ignore").decode("ascii")
    out, count = [], 0
    buf = ""
    for ch in t:
        buf += ch
        if ch == ".":
            out.append(buf)
            count += 1
            buf = ""
            if count >= n:
                break
    s = ("".join(out) or buf).strip()
    if len(s) > cap:
        s = s[:cap - 3].rstrip() + "..."
    return s


def age(sec: float) -> str:
    if sec < 0 or sec > 1e11:
        return "?"
    if sec < 5400:
        return f"{int(sec/60)}m"
    if sec < 172800:
        return f"{int(sec/3600)}h"
    return f"{int(sec/86400)}d"


def gather() -> dict:
    now = time.time()
    cmap = commit_map(COMMIT_WINDOW_DAYS)
    hot, cold = [], []
    for p in load_projects():
        if p["status"] in CLOSED:
            continue
        commits = cmap.get(p["code"], [])
        latest_commit_ts = commits[0]["ts"] if commits else 0
        last_activity = max(p["mtime"], latest_commit_ts)
        age_s = now - last_activity if last_activity else 1e12

        # owner: JSON field if present, else the dominant recent committer (de-facto worker)
        owner = str(p["owner"]).strip()
        if not owner and commits:
            owner = Counter(c["author"] for c in commits).most_common(1)[0][0] + " (top committer)"

        status2 = first_sentences(p["phase"], 2)
        blk = str(p["blocking"]).strip()
        if blk and blk.lower() not in ("none", "", "null", "none.", "n/a"):
            status2 = (status2 + f" BLOCKING: {first_sentences(blk, 1, 120)}").strip()
        if not status2 and commits:
            status2 = first_sentences(commits[0]["subject"], 2)

        row = {
            "code": p["code"],
            "status": p["status"],
            "owner": owner,
            "last_activity_s": None if age_s > 1e11 else round(age_s),
            "commit_count": len(commits),
            "latest_commit": (commits[0]["subject"][:100] if commits else ""),
            "latest_commit_by": (commits[0]["author"] if commits else ""),
            "status_2sent": status2,
        }
        (hot if age_s <= HOT_S else cold).append(row)
    hot.sort(key=lambda r: (r["last_activity_s"] is None, r["last_activity_s"] or 0))
    cold.sort(key=lambda r: (r["last_activity_s"] is None, r["last_activity_s"] or 0))
    return {"hot": hot, "cold": cold, "ts": now}


def render_section(title: str, rows: list[dict], hint: str) -> list[str]:
    out = [f"{title} ({len(rows)})   {hint}"]
    if not rows:
        out.append("  (none)")
    for r in rows:
        a = age(r["last_activity_s"] if r["last_activity_s"] is not None else 1e12)
        owner = (r["owner"] or "?")[:24]
        out.append(f"  {r['code']:<26} [{r['status']:<8}] last {a:>4} | owner {owner} | "
                   f"{r['commit_count']} commits/30d")
        if r["status_2sent"]:
            out.append(f"      {r['status_2sent']}")
        if r["latest_commit"]:
            out.append(f"      latest: ({r['latest_commit_by']}) {r['latest_commit']}")
    return out


def main():
    args = sys.argv[1:]
    g = gather()
    if "--json" in args:
        print(json.dumps(g, indent=2))
        return
    out = []
    out.append(f"FABRIC PROJECTS  ({time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(g['ts']))})")
    out.append("not-closed registered projects, partitioned by 72h last-activity (commit + JSON mtime)")
    out.append("")
    want_hot = "--cold" not in args
    want_cold = "--hot" not in args
    if want_hot:
        out += render_section("HOT (worked <72h, not closed)", g["hot"],
                              "<-- in flight; ensure live owner + monitoring")
        out.append("")
    if want_cold:
        out += render_section("COLD (>72h since work, still not closed)", g["cold"],
                              "<-- closure-debt or stalled; close it or re-activate")
        out.append("")
    out.append(f"SUMMARY: {len(g['hot'])} hot | {len(g['cold'])} cold | "
               f"{len(g['hot']) + len(g['cold'])} not-closed total")
    print("\n".join(out))


if __name__ == "__main__":
    main()
