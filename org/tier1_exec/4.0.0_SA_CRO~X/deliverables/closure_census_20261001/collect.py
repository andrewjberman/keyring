"""Closure census collector: per open laptop project, read its state from artifacts. Read-only.

    python collect.py <scratch dir>

Reads the directives register output (directives.json in the scratch dir), then per project: the project row
(org/projects/<CODE>.json or the missions tree project.json), to-check, prd-delta, sequence-check, and git history.
Writes census_raw.json. Prints the denominator.
"""
import glob
import json
import os
import re
import subprocess
import sys

S = sys.argv[1]
LAPTOP = ["D0", "D2", "D3", "D7", "D8", "D9", "D10", "D11", "D13", "D14"]
EXCLUDE = {"IRPT_BCKEND", "IRPT_DASHBD", "DSGN_IRPTV1"}
CLOSED = re.compile(r"^(closed|complete)", re.I)


def run(*a, timeout=240):
    try:
        p = subprocess.run(list(a), capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT"


d = json.load(open(os.path.join(S, "directives.json")))
members = []
for x in d["live"]:
    if x["code"] in LAPTOP:
        for code, st in x["projects"].items():
            members.append((x["code"], code, st))
open_all = [(dc, c, st) for dc, c, st in members if not CLOSED.match(str(st))]
scope = [(dc, c, st) for dc, c, st in open_all if c not in EXCLUDE]
print("members of the ten laptop directives: %d | closed or complete: %d | open: %d | excluded by the ask: %d | in "
      "scope: %d" % (len(members), len(members) - len(open_all), len(open_all), len(open_all) - len(scope), len(scope)))

out = []
for dc, code, st in scope:
    rec = {"directive": dc, "code": code, "register_status": st}
    rows = [p.replace("\\", "/") for p in glob.glob("org/projects/%s.json" % code)]
    rows += [p.replace("\\", "/") for p in glob.glob("org/missions/D*/*/%s/project.json" % code)]
    rec["project_rows"] = rows
    info = {}
    for p in rows:
        try:
            j = json.load(open(p, encoding="utf-8"))
        except Exception as e:  # a malformed row is a finding, not a skip
            info[p] = {"UNREADABLE": str(e)[:120]}
            continue
        keep = {}
        for k in ("status", "phase", "blocking", "blocked_on", "hold", "holds", "device", "fabric", "closer_contract",
                  "endpoint_outcomes", "updated", "last_updated", "owner", "coo", "priority", "description", "title",
                  "name", "next", "next_steps", "round", "limb", "stance", "prd", "prd_path", "directive"):
            if k in j:
                v = j[k]
                keep[k] = v if not isinstance(v, str) else v[:900]
        keep["_keys"] = sorted(j.keys())
        info[p] = keep
    rec["rows"] = info
    rc, o, e = run(sys.executable, ".tools/to-check.py", "--all", "--project", code)
    m = re.search(r"TO-CHECK-RESULT total=(\d+) projects=(\d+) blocked=(\d+)", o)
    rec["to_check"] = {"rc": rc, "active": int(m.group(1)) if m else None, "blocked": int(m.group(3)) if m else None}
    lines = [ln for ln in o.split("\n") if code in ln and "THIRD-POPULATION" not in ln]
    rec["to_check"]["lines"] = [ln.strip()[:230] for ln in lines[:14]]
    # every task-order file naming the code, by status tag
    tos = [p.replace("\\", "/") for p in glob.glob("org/**/task_orders/%s.*.md" % code, recursive=True)]
    tos += [p.replace("\\", "/") for p in glob.glob("org/missions/D*/*/%s/task-orders/*.md" % code)]
    counts = {}
    for p in tos:
        try:
            t = open(p, encoding="utf-8", errors="replace").read(6000)
        except OSError:
            continue
        s = re.search(r"<status>\s*([A-Za-z_-]+)", t)
        k = s.group(1).lower() if s else "no-status-tag"
        counts[k] = counts.get(k, 0) + 1
    rec["task_orders"] = {"files": len(tos), "by_status": counts}
    rc, o, e = run(sys.executable, ".tools/prd-delta.py", "--project", code)
    rec["prd_delta"] = {"rc": rc, "out": [ln.rstrip()[:230] for ln in o.split("\n") if ln.strip()][:40],
                        "err": e.strip()[:200]}
    rc, o, e = run(sys.executable, ".tools/sequence-check.py", "--project", code)
    rec["sequence"] = {"rc": rc, "out": [ln.rstrip()[:200] for ln in o.split("\n") if ln.strip()][:8]}
    rc, o, e = run("git", "log", "-4", "--format=%h|%cI|%an|%s", "--grep", code)
    rec["commits_last4"] = [ln[:230] for ln in o.strip().split("\n") if ln]
    rc, o, e = run("git", "rev-list", "--count", "--since=2026-09-17", "--grep", code, "HEAD")
    rec["commits_since_0917"] = o.strip()
    rc, o, e = run("git", "rev-list", "--count", "--grep", code, "HEAD")
    rec["commits_total"] = o.strip()
    out.append(rec)
    print("%-22s %-4s rows=%d tos=%d active=%s commits14d=%s total=%s" % (
        code, dc, len(rows), len(tos), rec["to_check"]["active"], rec["commits_since_0917"], rec["commits_total"]))
json.dump(out, open(os.path.join(S, "census_raw.json"), "w"), indent=1)
print("projects collected:", len(out))
