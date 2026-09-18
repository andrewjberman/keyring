"""Fabric-wide output counts for the window: commits and completed task orders, both machines.

The two fabrics share one git history, so the laptop's commits are visible here. Site Z's own commits
are identified by the same rule the cost report uses (lane serials in this box's session map, the
terminal seat, and workers of site-Z projects); everything else authored by an agent serial is the
other fabric's.
"""
import collections
import importlib.util
import subprocess

REPO = "C:/Users/Opal Bloomberg/Desktop/ajb_workspace"
SRC = REPO + "/org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/CLAUDE_COST_REPORT_20260917/measure_claude_usage.py"
SINCE, UNTIL = "2026-08-18T00:00:00Z", "2026-09-17T23:59:59Z"

spec = importlib.util.spec_from_file_location("m", SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

serials = set(m.load_serial_map(REPO + "/org/mcp/sessions").values())
projects = m.site_projects(REPO)

log = subprocess.run(
    ["git", "-C", REPO, "log", "--all", "--no-merges", "--since=" + SINCE, "--until=" + UNTIL,
     "--format=%H%x09%an%x09%ad", "--date=short"],
    capture_output=True, timeout=900).stdout.decode("utf-8", errors="replace")

site, other, human = 0, 0, 0
days = set()
other_authors = collections.Counter()
for line in log.splitlines():
    if not line.strip():
        continue
    sha, an, ad = line.split("\t", 2)
    days.add(ad)
    is_agent = ("_" in an and any(an.startswith(p) for p in ("0.", "1.", "2.", "3.", "4.")))
    if not is_agent:
        human += 1
        continue
    if m.box_author(an, serials, projects):
        site += 1
    else:
        other += 1
        other_authors[an] += 1

print("WINDOW %s..%s" % (SINCE[:10], UNTIL[:10]))
print("commits, site Z rule      : %d" % site)
print("commits, other agent seats: %d" % other)
print("commits, non-agent authors: %d" % human)
print("commits, all agents       : %d" % (site + other))
print("distinct commit days      : %d" % len(days))
print("\ntop other-fabric authors:")
for a, c in other_authors.most_common(12):
    print("   %-34s %5d" % (a, c))

# completed task orders across EVERY project, not just site Z's
out = subprocess.run(
    ["git", "-C", REPO, "log", "--all", "--no-merges", "--since=" + SINCE, "--until=" + UNTIL,
     "-G", "<status>complete</status>", "-p", "--format=COMMIT %H", "--",
     "org/missions", "org/projects"],
    capture_output=True, timeout=1800).stdout.decode("utf-8", errors="replace")
done = set()
current = None
for line in out.splitlines():
    if line.startswith("+++ b/"):
        current = line[len("+++ b/"):]
    elif line.startswith("+") and "<status>complete</status>" in line and current:
        if "/task-orders/" in current:
            done.add(current)
print("\ntask orders completed, ALL projects: %d" % len(done))
by_project = collections.Counter()
for path in done:
    parts = path.split("/")
    for i, seg in enumerate(parts):
        if seg == "task-orders" and i >= 1:
            by_project[parts[i - 1]] += 1
            break
for k, v in by_project.most_common(15):
    print("   %-24s %4d" % (k, v))
