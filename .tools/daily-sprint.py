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
  9. the other repos' commits for the day: portal (the nested checkout) and opal_ai (OPAL_AI_REPO, or a
     sibling checkout); a repo with no checkout is read from a temporary clone through `gh`, and one that
     cannot be read is reported as not read
 10. Andrew's notes for the day (daily_reports/notes/<day>.md) -- read FIRST when present
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile

ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip() or os.getcwd()
SPRINTS = os.path.join(ROOT, "org", "sprints")
TOOLS = os.path.join(ROOT, ".tools")
OTHER_REPOS = {"portal": os.path.join(ROOT, "portal"),
               "opal_ai": os.environ.get("OPAL_AI_REPO") or os.path.join(os.path.dirname(ROOT), "opal_ai")}


NO_PROMPT = dict(os.environ, GIT_TERMINAL_PROMPT="0", GCM_INTERACTIVE="never")


def _force_rmtree(path):
    """git leaves pack files read-only; clear the bit and retry so a temp clone is really removed."""
    def _retry(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)
    shutil.rmtree(path, onerror=_retry)


def run(cmd, timeout=300, env=None):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT, timeout=timeout, shell=isinstance(cmd, str),
                           env=env)
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
    # 9. The other repos (Andrew-direct 2026-09-24: "all daily sprint stuff checks both ajb_workspace and portal
    # commits, and it should also check opal_ai"). A repo is read only from a real checkout: `git -C` on a
    # directory that is not one walks UP to ajb_workspace and would report its commits under the wrong name.
    p["other_repos"] = {}
    for name, d in OTHER_REPOS.items():
        tmp = None
        if os.path.exists(os.path.join(d, ".git")):
            run(["git", "-C", d, "fetch", "--quiet", "origin"], timeout=120)
        else:
            # No checkout here: a fresh blobless, checkout-free clone (the Lambda's form), credential from `gh`,
            # prompts OFF -- the Git Credential Manager otherwise waits on an interactive login and hangs the run.
            tmp = tempfile.mkdtemp(prefix=f"sprint_{name}_")
            d = os.path.join(tmp, name)
            since3 = (datetime.date.fromisoformat(day) - datetime.timedelta(days=3)).isoformat()
            run(["git", "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential", "clone",
                 "--filter=blob:none", "--no-checkout", "--no-single-branch", "--no-tags", "--quiet",
                 f"--shallow-since={since3}", f"https://github.com/Opal-Capital/{name}.git", d],
                timeout=180, env=NO_PROMPT)
        if os.path.exists(os.path.join(d, ".git")):
            lg = run(["git", "-C", d, "log", "--all", "--no-merges", f"--since={since}", f"--until={until}",
                      "--format=%an\t%h\t%s"])
            rr = [ln.split("\t", 2) for ln in lg.splitlines() if ln.count("\t") >= 2]
            p["other_repos"][name] = {"status": f"{len(rr)} commits", "subjects": [f"{a}|{s}" for a, _, s in rr]}
        else:
            p["other_repos"][name] = {"status": "not read: no checkout, and a clone through gh failed"}
        if tmp:
            _force_rmtree(tmp)
    # 10. Andrew's own notes for the day (daily_reports/notes/<day>.md), read FIRST by the writer when present.
    note = os.path.join(ROOT, "daily_reports", "notes", f"{day}.md")
    p["andrew_notes"] = open(note, encoding="utf-8").read().strip() if os.path.exists(note) else None
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
    for name, r in p["other_repos"].items():
        print(f"  {name}: {r['status']}")
        for s in r.get("subjects", [])[:40]:
            print(f"    {s[:160]}")
    if p["andrew_notes"]:
        print("  ANDREW'S NOTES FOR THE DAY (read these FIRST: his named wins are sprint items, his headline is the headline):")
        for ln in p["andrew_notes"].splitlines():
            print(f"    {ln}")
    else:
        print("  Andrew's notes: none for this day (default run)")
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
