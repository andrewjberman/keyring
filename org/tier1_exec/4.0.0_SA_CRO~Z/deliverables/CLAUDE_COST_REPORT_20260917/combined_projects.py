"""Per-project cost across BOTH machines.

Site Z: each seat's measured spend split across the projects that seat committed to (the stronger
method, because site Z's per-seat spend is measured here).
Laptop: its measured total, $34,953.22, split across projects in proportion to the commits its seats
authored in the window. Weaker, and labelled so: the laptop's per-seat spend is not on this machine.
"""
import collections
import importlib.util
import json
import re
import subprocess

REPO = "C:/Users/Opal Bloomberg/Desktop/ajb_workspace"
PROJ = "C:/Users/Opal Bloomberg/.claude/projects/C--Users-Opal-Bloomberg-Desktop-ajb-workspace"
SRC = REPO + "/org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CLAUDE_COST_REPORT_20260917/measure_claude_usage.py"
SINCE, UNTIL = "2026-08-18T00:00:00Z", "2026-09-17T23:59:59Z"
LAPTOP_TOTAL = 34953.22
PAID = 1110.04

spec = importlib.util.spec_from_file_location("m", SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

records, _ = m.collect(PROJ)
serial_map = m.load_serial_map(REPO + "/org/mcp/sessions")
box_serials = set(serial_map.values())
projects = m.site_projects(REPO)

by_seat = collections.Counter()
site_total = 0.0
for rec in records:
    cost = m.price(rec)
    if cost is None:
        continue
    usd = sum(cost.values())
    site_total += usd
    by_seat[serial_map.get(rec["session"], "UNMAPPED")] += usd

CODE = re.compile(r"^[a-z0-9-]+\(([A-Z]{4}_[A-Z0-9]{4,12})")
PATH = re.compile(r"^org/missions/D[^/]+/[^/]+/([A-Z]{4}_[A-Z0-9]{4,12})/")

raw = subprocess.run(
    ["git", "-C", REPO, "log", "--all", "--no-merges", "--since=" + SINCE, "--until=" + UNTIL,
     "--format=C%x09%an%x09%s", "--name-only"],
    capture_output=True, timeout=900).stdout.decode("utf-8", errors="replace")

seat_project = collections.defaultdict(collections.Counter)
laptop_project = collections.Counter()
author = code = None
paths = []


def flush():
    global author, code, paths
    if author is None:
        return
    c = code
    if c is None:
        for p in paths:
            mm = PATH.match(p)
            if mm:
                c = mm.group(1)
                break
    if c:
        if m.box_author(author, box_serials, projects):
            seat_project[author][c] += 1
        elif "_" in author and author[0].isdigit():
            laptop_project[c] += 1
    author = code = None
    paths = []


for line in raw.splitlines():
    if line.startswith("C\t"):
        flush()
        _, an, subj = line.split("\t", 2)
        author = an
        mm = CODE.match(subj)
        code = mm.group(1) if mm else None
    elif line.strip():
        paths.append(line.strip())
flush()

site_attr = collections.Counter()
site_nocommit = 0.0
for seat, usd in by_seat.items():
    dist = seat_project.get(seat)
    if not dist:
        site_nocommit += usd
        continue
    n = sum(dist.values())
    for c, k in dist.items():
        site_attr[c] += usd * k / n

lap_total_commits = sum(laptop_project.values())
lap_attr = {c: LAPTOP_TOTAL * k / lap_total_commits for c, k in laptop_project.items()}

combined = collections.Counter()
for c, v in site_attr.items():
    combined[c] += v
for c, v in lap_attr.items():
    combined[c] += v

grand = site_total + LAPTOP_TOTAL
share = PAID / grand
print("site Z priced $%.2f | laptop $%.2f | grand $%.2f | paid share %.4f"
      % (site_total, LAPTOP_TOTAL, grand, share))
print("laptop commits with a project: %d" % lap_total_commits)
print("\n%-24s %11s %11s %11s %10s" % ("project", "site Z $", "laptop $", "total $", "cost to us"))
rows = []
for c, v in combined.most_common(14):
    print("%-24s %11.0f %11.0f %11.0f %10.0f"
          % (c, site_attr.get(c, 0.0), lap_attr.get(c, 0.0), v, v * share))
    rows.append([c, round(v), round(v * share)])
tail = sum(v for c, v in combined.items()) - sum(v for c, v in combined.most_common(14))
print("%-24s %11s %11s %11.0f %10.0f" % ("(smaller projects)", "", "", tail, tail * share))
print("%-24s %11.0f %11s %11.0f %10.0f"
      % ("no project commits", site_nocommit, "", site_nocommit, site_nocommit * share))
json.dump({"site_total": site_total, "laptop_total": LAPTOP_TOTAL, "grand": grand, "share": share,
           "site_nocommit": site_nocommit, "rows": rows},
          open("combined_projects.json", "w", encoding="utf-8"), indent=1)
print("\nwrote combined_projects.json")
