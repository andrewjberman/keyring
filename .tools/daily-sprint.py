#!/usr/bin/env python3
"""daily-sprint.py -- the GROUNDING PACKET for Andrew's daily sprint text (/daily-sprint).

Compiles, read-only, everything the rewrite must be grounded on, for a given day (default: today
UTC), and scaffolds the day's file from yesterday's if it does not exist yet. The PROSE is the
seat's act (template: org/ref/DAILY_SPRINT_TEMPLATE.md); this script is the machine half.

Usage:
  daily-sprint.py                  packet for today (UTC) + scaffold org/sprints/DAILY_SPRINT_<today>.md
  daily-sprint.py --date 2026-08-20
  daily-sprint.py --packet-only    print the packet, write nothing
  daily-sprint.py --json           packet as JSON

Packet sections (each with its denominator):
  1. comp-state self-test + drift rows (BEHIND / POST-CLOSE)
  2. git census since 00:00Z of the day, all refs (both fabrics): commits, authors, top subjects
  3. directives-check --json (live rows w/ device/projects/TOs/flags; retired rows)
  4. to-check totals (open TOs / projects)
  5. Andrew-direct records committed that day (file names, both fabrics)
  6. projects whose org/projects JSON closed that day
  7. ledger entries created that day
  8. yesterday's sprint file (the base to rewrite from), if present
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import subprocess
import sys

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or os.getcwd()
SPRINTS = os.path.join(ROOT, "org", "sprints")
TOOLS = os.path.join(ROOT, ".tools")


def run(cmd, timeout=300):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, timeout=timeout, shell=isinstance(cmd, str))
        return (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        return f"<run failed: {e}>"


def packet(day):
    since = f"{day}T00:00:00Z"
    until = f"{day}T23:59:59Z"
    p = {"day": day}
    cs = run("comp-state --self-test 2>&1 | tail -1")
    p["comp_state_selftest"] = cs.strip()
    p["comp_state_trusted"] = "PASS" in cs
    drift = run("comp-state 2>&1")
    p["comp_state_rows"] = [ln for ln in drift.splitlines() if ln.startswith("[BEHIND]") or ln.startswith("[POST-CLOSE]")]
    log = run(["git", "log", "--all", f"--since={since}", f"--until={until}", "--format=%an\t%h\t%s"])
    rows = [ln.split("\t", 2) for ln in log.splitlines() if ln.strip()]
    p["commits"] = len(rows)
    authors = {}
    for a, _, _ in rows:
        authors[a] = authors.get(a, 0) + 1
    p["authors"] = dict(sorted(authors.items(), key=lambda kv: -kv[1]))
    kinds = {}
    for _, _, s in rows:
        k = re.split(r"[(:]", s, 1)[0].strip().lower()[:24]
        kinds[k] = kinds.get(k, 0) + 1
    p["subject_kinds_top"] = dict(sorted(kinds.items(), key=lambda kv: -kv[1])[:20])
    try:
        p["directives"] = json.loads(run([sys.executable, os.path.join(TOOLS, "directives-check.py"), "--json", "--all"]))
    except Exception as e:
        p["directives"] = {"error": str(e)}
    tc = run([sys.executable, os.path.join(TOOLS, "to-check.py"), "--all"])
    m = re.search(r"TO-CHECK-RESULT (.+)", tc)
    p["to_check"] = m.group(1) if m else "<unavailable>"
    names = run(["git", "log", "--all", f"--since={since}", f"--until={until}", "--name-only", "--format="])
    day_compact = day.replace("-", "")
    p["andrew_direct_records"] = sorted({os.path.basename(n) for n in names.splitlines()
                                         if re.search(rf"ANDREW_(DIRECT|RULED|RULING)_{day_compact}", n)})
    closed = []
    for f in glob.glob(os.path.join(ROOT, "org", "projects", "*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        st = str(d.get("status", "")).lower()
        when = str(d.get("closed") or d.get("completed") or "")
        if st in ("closed", "complete", "completed") and when == day:
            closed.append(os.path.basename(f)[:-5])
    p["projects_closed"] = sorted(closed)
    p["ledger_today"] = sorted({os.path.basename(n)[:-3] for n in names.splitlines()
                                if re.match(r"org/tier0/ledger/LD-\d+\.md$", n)})
    prev = sorted(glob.glob(os.path.join(SPRINTS, "DAILY_SPRINT_*.md")))
    prev = [x for x in prev if os.path.basename(x) < f"DAILY_SPRINT_{day}.md"]
    p["yesterday_file"] = prev[-1] if prev else None
    return p


def print_packet(p):
    _wd = datetime.date.fromisoformat(p['day']).strftime("%A")  # DATE LAW (Andrew-direct 2026-08-30): the weekday is DERIVED here so the writer never types it
    print(f"DAILY-SPRINT PACKET for {p['day']} ({_wd}, UTC)  |  generated {datetime.datetime.now(datetime.UTC):%Y-%m-%d %H:%MZ}")
    print(f"  comp-state: {p['comp_state_selftest']}   -> packet trusted: {p['comp_state_trusted']}")
    print(f"  drift rows: {len(p['comp_state_rows'])}")
    for ln in p["comp_state_rows"][:25]:
        print(f"    {ln}")
    print(f"  git census: {p['commits']} commits, {len(p['authors'])} authors (all refs = both fabrics)")
    for a, n in list(p["authors"].items())[:25]:
        print(f"    {n:>4}  {a}")
    print(f"  subject kinds (top): {p['subject_kinds_top']}")
    d = p.get("directives") or {}
    if "live" in d:
        print(f"  directives: live={len(d['live'])} retired={len(d['retired'])} malformed={len(d.get('malformed', []))}")
        for r in d["live"]:
            print(f"    {r['code']} {r['device']:<7} TOs={r['open_tos']:<3} projects={r['projects']} flags={r['flags']}  last={r['last']}")
        for r in d["retired"]:
            print(f"    RETIRED {r['code']} at {r['at']} by {r['by']}")
    print(f"  to-check: {p['to_check']}")
    print(f"  Andrew-direct records today ({len(p['andrew_direct_records'])}):")
    for n in p["andrew_direct_records"]:
        print(f"    {n}")
    print(f"  projects closed today: {p['projects_closed'] or '-'}")
    print(f"  ledger today: {p['ledger_today'] or '-'}")
    print(f"  yesterday's sprint file: {p['yesterday_file'] or '(none -- first day)'}")
    print("DAILY-SPRINT-PACKET-RESULT "
          f"commits={p['commits']} authors={len(p['authors'])} andrew_direct={len(p['andrew_direct_records'])} "
          f"closed={len(p['projects_closed'])} trusted={p['comp_state_trusted']}")


def scaffold(day, p):
    os.makedirs(SPRINTS, exist_ok=True)
    out = os.path.join(SPRINTS, f"DAILY_SPRINT_{day}.md")
    if os.path.exists(out):
        print(f"  today's file exists: {out} (not overwritten -- rewrite it in place)")
        return out
    base = p.get("yesterday_file")
    text = open(base, encoding="utf-8").read() if base else open(os.path.join(ROOT, "org", "ref", "DAILY_SPRINT_TEMPLATE.md"), encoding="utf-8").read()
    open(out, "w", encoding="utf-8").write(text)
    print(f"  SCAFFOLDED {out} from {os.path.basename(base) if base else 'the template'} -- REWRITE every line against the packet")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d"))
    ap.add_argument("--packet-only", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    p = packet(a.date)
    if a.json:
        print(json.dumps(p, indent=2, default=str))
        return
    print_packet(p)
    if not a.packet_only:
        scaffold(a.date, p)


if __name__ == "__main__":
    main()
