"""Attribute site Z's measured Claude spend to projects.

Method, stated so it can be argued with:
  1. Price every response on this machine and total it per SEAT (session -> serial map).
  2. For each seat, count the commits it authored in the window, per PROJECT (project code taken
     from the commit subject's `type(CODE, ...)` prefix, else from an org/missions/.../CODE path).
  3. Split each seat's spend across its own projects in proportion to those commit counts.
  4. Real cost = attributed cost x (what we paid / total standard price).
A seat with spend but no commits lands in NO PROJECT COMMITS rather than being spread.
"""
import collections
import importlib.util
import json
import re
import subprocess
import sys

REPO = "C:/Users/Opal Bloomberg/Desktop/ajb_workspace"
PROJ = "C:/Users/Opal Bloomberg/.claude/projects/C--Users-Opal-Bloomberg-Desktop-ajb-workspace"
SRC = REPO + "/org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CLAUDE_COST_REPORT_20260917/measure_claude_usage.py"
SINCE, UNTIL = "2026-08-18T00:00:00Z", "2026-09-17T23:59:59Z"
PAID = float(sys.argv[1]) if len(sys.argv) > 1 else 1110.04
COMBINED = float(sys.argv[2]) if len(sys.argv) > 2 else 43282.97

spec = importlib.util.spec_from_file_location("m", SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

records, _counts = m.collect(PROJ)
serials = m.load_serial_map(REPO + "/org/mcp/sessions")

by_serial = collections.Counter()
total = 0.0
for rec in records:
    cost = m.price(rec)
    if cost is None:
        continue
    usd = sum(cost.values())
    total += usd
    by_serial[serials.get(rec["session"], "UNMAPPED")] += usd

CODE = re.compile(r"^[a-z0-9-]+\(([A-Z]{4}_[A-Z0-9]{4,12})")
PATH = re.compile(r"^org/missions/D[^/]+/[^/]+/([A-Z]{4}_[A-Z0-9]{4,12})/")

raw = subprocess.run(
    ["git", "-C", REPO, "log", "--all", "--no-merges", "--since=" + SINCE, "--until=" + UNTIL,
     "--format=C%x09%H%x09%an%x09%s", "--name-only"],
    capture_output=True, timeout=900).stdout.decode("utf-8", errors="replace")

seat_project = collections.defaultdict(collections.Counter)
cur_author = None
cur_code = None
pending_paths = []


def flush():
    global cur_author, cur_code, pending_paths
    if cur_author is None:
        return
    code = cur_code
    if code is None:
        for p in pending_paths:
            mm = PATH.match(p)
            if mm:
                code = mm.group(1)
                break
    if code:
        seat_project[cur_author][code] += 1
    cur_author, cur_code, pending_paths = None, None, []


for line in raw.splitlines():
    if line.startswith("C\t"):
        flush()
        _, _sha, an, subj = line.split("\t", 3)
        cur_author = an
        mm = CODE.match(subj)
        cur_code = mm.group(1) if mm else None
        pending_paths = []
    elif line.strip():
        pending_paths.append(line.strip())
flush()

attributed = collections.Counter()
no_commits = 0.0
for serial, usd in by_serial.items():
    dist = seat_project.get(serial)
    if not dist:
        no_commits += usd
        continue
    n = sum(dist.values())
    for code, c in dist.items():
        attributed[code] += usd * c / n

share = PAID / COMBINED
rows = []
for code, usd in attributed.most_common():
    rows.append((code, usd, usd / total, usd * share))

print("site Z priced total: $%.2f   paid share used: %.4f (paid $%.2f / combined $%.2f)"
      % (total, share, PAID, COMBINED))
print("%-24s %12s %8s %12s" % ("project", "standard $", "share", "real cost $"))
for code, usd, sh, real in rows:
    print("%-24s %12.2f %7.1f%% %12.2f" % (code, usd, 100 * sh, real))
print("%-24s %12.2f %7.1f%% %12.2f" % ("NO PROJECT COMMITS", no_commits, 100 * no_commits / total,
                                       no_commits * share))
json.dump({"total": total, "no_project": no_commits,
           "projects": {c: {"standard": u, "real": u * share} for c, u, _s, _r in
                        [(c, u, s, r) for c, u, s, r in rows]}},
          open("per_project_cost.json", "w", encoding="utf-8"), indent=1)
print("\nwrote per_project_cost.json")
