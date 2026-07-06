#!/usr/bin/env python3
"""activity-check.py -- REAL-TIME "who's active right now" view, by recency.

The point of this tool is TEMPORAL, not a rolling-period summary: it answers "what is
happening right now, today" -- so agents are ordered by RECENCY (most recently active
FIRST), NOT by who has the most commits over the window (Andrew-direct 2026-07-06). Each
agent's card leads with "last commit Xm ago" and lists their 5 MOST RECENT commits.

ACTIVE AGENT = a git author whose name is a fabric serial (N.N.N_ROLE_*) with >=1 commit
in the last --days (default 7 -- this is only how far BACK to look; ordering is by recency,
so a busy-but-idle-for-days agent sinks to the bottom and whoever just committed floats up).

--summary appends the (opt-in) 7d AGGREGATE (top macros / projects / agents by count) --
NOT shown by default, since the default view is intentionally real-time, not a period roll-up.
Directed vs all: a project/macro aggregate only counts commits whose message references a
known project code; an exec "drive cycle N" / "log" commit is directed at no project.

Usage:
  python .tools/activity-check.py                 # REAL-TIME view: agents by recency, newest first
  python .tools/activity-check.py --days 2         # tighter look-back
  python .tools/activity-check.py --summary        # + the opt-in 7d aggregate roll-up
  python .tools/activity-check.py --json           # machine-readable (the dashboard consumes this)

Read-only: pure git + filesystem, no MCP. The HTML dashboard companion is
.claude/skills/activity-check/render_activity_dashboard.py.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

WS = Path(__file__).resolve().parent.parent
PROJ_DIR = WS / "org" / "projects"
FS = chr(1)  # git pretty field separator (subjects can contain anything but \x01)
AGENT_RE = re.compile(r"^\d+\.\d+\.\d+_")

_ASCII = {"—": "--", "–": "-", "…": "...", "→": "->",
          "‘": "'", "’": "'", "“": '"', "”": '"',
          "•": "*", "·": "-", "✓": "OK"}


def to_ascii(t: str) -> str:
    for u, a in _ASCII.items():
        t = t.replace(u, a)
    return t.encode("ascii", "replace").decode("ascii")


def known_codes() -> dict:
    """UPPER project code -> macro group. From every org/projects/*.json (open + closed)."""
    codes = {}
    for f in PROJ_DIR.glob("*.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8", errors="replace"))
        except Exception:
            continue
        c = (d.get("project_code") or f.stem).upper()
        mc = d.get("macro_code")
        if not mc or not isinstance(mc, str):
            mc = c.split("_")[0]
        codes[c] = mc
    return codes


def resolve_code(subject: str, codes: dict):
    """The known project code a commit subject references (most-specific token match)."""
    up = subject.upper()
    hits = [c for c in codes
            if re.search(r"(?<![A-Z0-9_])" + re.escape(c) + r"(?![A-Z0-9_])", up)]
    if not hits:
        return None, None
    c = max(hits, key=len)  # SCTY_MCPGUARD beats SCTY
    return c, codes[c]


def agent_name(serial: str) -> str:
    """Serial -> role-name identity, pod-number stripped (house convention, matches
    to-check): 0.6.1_AE_PartnerETL -> AE_PartnerETL, 2.0.0_SA_COO~B -> SA_COO~B. The
    three AE_PartnerETL pods (0.6.0/0.6.1/0.6.2) collapse to one role-agent."""
    m = re.match(r"^\d+\.\d+\.\d+_(.*)$", serial)
    return m.group(1) if m else serial


def role_from_name(name: str) -> str:
    """Short role token from an agent-name: SA_COO -> COO, SA_COO~B -> COO,
    AE_PartnerETL -> AE, DS_ClientPlatform~A -> DS."""
    parts = name.split("_")
    if parts[0] == "SA" and len(parts) >= 2:
        return parts[1].split("~")[0]
    return parts[0].split("~")[0]


def fmt_age(dt: datetime, now: datetime) -> str:
    h = (now - dt).total_seconds() / 3600
    if h < 1:
        return f"{max(1, int(h * 60))}m"
    if h < 24:
        return f"{h:.0f}h"
    return f"{h / 24:.1f}d"


def window_commits(days: int):
    r = subprocess.run(
        ["git", "log", f"--since={days} days ago", f"--pretty=%H{FS}%an{FS}%aI{FS}%s"],
        capture_output=True, text=True, cwd=str(WS), errors="replace",
    )
    out = []
    for ln in r.stdout.splitlines():
        parts = ln.split(FS)
        if len(parts) != 4:
            continue
        sha, an, aiso, subj = parts
        if not AGENT_RE.match(an):  # fabric-agent serials only
            continue
        out.append({"sha": sha[:9], "author": an, "iso": aiso, "subj": subj})
    return out


def top4_other(counter: Counter):
    items = counter.most_common()
    res = [{"label": k, "value": v} for k, v in items[:4]]
    other = sum(v for _, v in items[4:])
    if other > 0:
        res.append({"label": "Other", "value": other})
    return res


def build(days: int) -> dict:
    now = datetime.now(timezone.utc)
    codes = known_codes()
    commits = window_commits(days)
    macro_ct, proj_ct, agent_ct = Counter(), Counter(), Counter()
    by_agent = defaultdict(list)
    for c in commits:
        code, macro = resolve_code(c["subj"], codes)
        c["code"], c["macro"] = code, macro
        name = agent_name(c["author"])
        agent_ct[name] += 1                              # ALL commits (by role-agent)
        if code:
            proj_ct[code] += 1                           # directed only
            macro_ct[macro] += 1
        by_agent[name].append(c)

    agents = []
    for name, cs in by_agent.items():
        cs.sort(key=lambda x: x["iso"], reverse=True)
        recent, last_dt = [], None
        for c in cs[:5]:
            try:
                dt = datetime.fromisoformat(c["iso"]).astimezone(timezone.utc)
                age = fmt_age(dt, now)
                if last_dt is None:
                    last_dt = dt                          # most-recent commit (cs sorted desc)
            except ValueError:
                age = "?"
            recent.append({"sha": c["sha"], "age": age, "subj": c["subj"],
                           "code": c["code"] or "(none)", "macro": c["macro"] or "(none)"})
        agents.append({"agent": name, "role": role_from_name(name),
                       "n_window": len(cs), "recent": recent,
                       "last_age": recent[0]["age"] if recent else "?",
                       "last_iso": last_dt.isoformat() if last_dt else ""})
    # REAL-TIME focus (Andrew-direct 2026-07-06): order by RECENCY -- the most recently
    # active agent first -- NOT by 7d commit count. The --days window is only how far back
    # to look for each agent's recent commits; who floats to the top is "who committed last".
    agents.sort(key=lambda a: a["last_iso"], reverse=True)

    return {
        "as_of": now.strftime("%Y-%m-%d %H:%MZ"),
        "days": days,
        "n_active_agents": len(agents),
        "n_commits": len(commits),
        "n_directed": sum(proj_ct.values()),
        "agents": agents,
        "pie_macro": top4_other(macro_ct),
        "pie_project": top4_other(proj_ct),
        "pie_agent": top4_other(agent_ct),
    }


def main():
    args = sys.argv[1:]
    days = 7
    if "--days" in args:
        i = args.index("--days")
        if i + 1 < len(args):
            try:
                days = int(args[i + 1])
            except ValueError:
                pass
    data = build(days)

    if "--json" in args:
        print(json.dumps(data, indent=2, ensure_ascii=True))
        return

    p = lambda s: print(to_ascii(s))
    p(f"ACTIVITY-CHECK  {data['as_of']}  |  {data['n_active_agents']} agents, MOST-RECENTLY-ACTIVE FIRST  "
      f"|  looked back {days}d  ({data['n_commits']} commits)")
    p("  (real-time view: agents ordered by their LATEST commit; lead line = time since it)")
    p("")
    for a in data["agents"]:
        p(f"{a['agent']}  --  last commit {a['last_age']} ago   (role {a['role']}, {a['n_window']} commits/{days}d)")
        for c in a["recent"]:
            tag = c["code"] if c["code"] != "(none)" else "(no project)"
            p(f"    {c['age']:>4}  [{tag}]  {c['subj'][:74]}")
        p("")
    if "--summary" in args:  # the 7d AGGREGATE, opt-in only (default view is real-time)
        p(f"-- {days}d aggregate summary --")
        p("TOP MACROS (directed):    " + ", ".join(f"{s['label']} {s['value']}" for s in data["pie_macro"]))
        p("TOP PROJECTS (directed):  " + ", ".join(f"{s['label']} {s['value']}" for s in data["pie_project"]))
        p("TOP AGENTS (all commits): " + ", ".join(f"{s['label']} {s['value']}" for s in data["pie_agent"]))


if __name__ == "__main__":
    main()
