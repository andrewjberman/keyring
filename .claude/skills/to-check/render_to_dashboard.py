#!/usr/bin/env python3
"""render_to_dashboard.py -- the HTML card+bar DASHBOARD renderer for /to-check.

The visual companion to the text `/to-check` lens (the TO variant of
registry-check's render_dashboard.py). Emits a single self-contained, Opal-branded
HTML dashboard of ACTIVE task orders:

  1. TO LOAD BY AGENT  -- a leaderboard: one bar per agent, length = # active TOs
     it carries, segmented by status (active / pending / blocked). The "who is
     carrying how much" view -- the throughput/bottleneck read.
  2. BY PROJECT        -- one card per project, a status-segmented TO-count bar +
     the compact TO list (id -> agent, status). Macro-colored.

DATA-DRIVEN: loads the canonical engine (.tools/to-check.py) and reuses its TO
parser + classifier + agent-tokenizer, so the TO schema logic stays in ONE place.
Same scope flags as the text lens (default = hot PRD projects <=14d).

Usage:
  python .claude/skills/to-check/render_to_dashboard.py            # hot PRD projects
  python .claude/skills/to-check/render_to_dashboard.py --all      # all workspace TOs
  python .claude/skills/to-check/render_to_dashboard.py --project CODE
  python .claude/skills/to-check/render_to_dashboard.py --assignee SERIAL
  python .claude/skills/to-check/render_to_dashboard.py --out PATH.html

Read-only: pure filesystem, no MCP, no writes except the one HTML file.
"""
from __future__ import annotations

import argparse
import html
import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path


MACRO_COLORS = {
    "NFRA": "#0a4b78", "ADVI": "#0891b2", "DATA": "#7c3aed", "SCTY": "#b91c1c",
    "ADHC": "#b45309", "ETFS": "#15803d", "PFMG": "#0d9488", "FIND": "#ca8a04",
    "ASTN": "#db2777", "COMP": "#0a4b78", "HEATMAP": "#64748b", "SCHWAB": "#0369a1",
}
FALLBACK = ["#475569", "#0369a1", "#7c3aed", "#0891b2", "#b45309", "#be123c", "#15803d"]
# TO status -> (segment color, pill bg, pill fg)
ST = {
    "ACTIVE": ("#15803d", "#dcfce7", "#15803d"),
    "PENDING": ("#b45309", "#fef3c7", "#92400e"),
    "BLOCKED": ("#b91c1c", "#fee2e2", "#b91c1c"),
    "UNKNOWN": ("#94a3b8", "#f1f5f9", "#64748b"),
}


def macro_of(code: str) -> str:
    return (code or "").split("_", 1)[0].upper()


def macro_color(code: str) -> str:
    mc = macro_of(code)
    if mc in MACRO_COLORS:
        return MACRO_COLORS[mc]
    if not mc:
        return "#475569"
    return FALLBACK[sum(ord(c) for c in mc) % len(FALLBACK)]


def find_workspace() -> Path:
    for start in (Path.cwd(), Path(__file__).resolve()):
        p = start
        for _ in range(8):
            if (p / ".tools" / "to-check.py").exists():
                return p
            if p.parent == p:
                break
            p = p.parent
    return Path(__file__).resolve().parents[3]


def load_engine(ws: Path):
    spec = importlib.util.spec_from_file_location("to_check_engine", ws / ".tools" / "to-check.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def esc(t) -> str:
    return html.escape(str(t or ""))


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Opal &mdash; Task Order Dashboard</title>
<style>
 :root{--bg:#f8fafc;--ink:#0f172a;--sub:#475569;--mut:#94a3b8;--line:#e2e8f0;--card:#fff;--navy:#0a4b78}
 *{box-sizing:border-box}
 body{margin:0;background:var(--bg);color:var(--ink);font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
 .wrap{max-width:1280px;margin:0 auto;padding:28px 32px 60px}
 header.top{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;border-bottom:2px solid #cbd5e1;padding-bottom:18px}
 h1{font-size:28px;font-weight:700;margin:0;letter-spacing:-.2px}
 .subt{font-size:15px;color:var(--sub);margin-top:6px}
 .asof{font-size:12.5px;color:var(--mut);text-align:right;white-space:nowrap}
 .stats{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin:22px 0 8px}
 .stat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;box-shadow:0 2px 4px rgba(15,23,42,.05)}
 .stat .n{font-size:24px;font-weight:700;color:var(--navy);line-height:1}
 .stat .l{font-size:11px;color:var(--sub);margin-top:6px;letter-spacing:.3px;text-transform:uppercase}
 .legend{display:flex;flex-wrap:wrap;gap:16px;margin:14px 2px 4px;font-size:12px;color:var(--sub)}
 .legend span{display:inline-flex;align-items:center;gap:6px}
 .dot{width:11px;height:11px;border-radius:3px;display:inline-block}
 .sectlbl{font-size:12.5px;font-weight:700;color:#64748b;letter-spacing:1px;text-transform:uppercase;margin:26px 2px 12px}
 /* agent leaderboard */
 .lb{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:8px 18px;box-shadow:0 2px 5px rgba(15,23,42,.06)}
 .lrow{display:flex;align-items:center;gap:12px;padding:8px 0;border-bottom:1px solid #f1f5f9}
 .lrow:last-child{border-bottom:none}
 .lname{width:200px;font-size:13px;font-weight:600;color:#334155;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
 .ltrack{flex:1;height:16px;background:#f8fafc;border-radius:5px;display:flex;overflow:hidden;border:1px solid #f1f5f9}
 .seg{height:100%}
 .lnum{width:52px;text-align:right;font-size:13px;font-weight:700;color:#334155}
 /* project cards */
 .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
 .card{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--navy);border-radius:12px;padding:15px 18px 14px;box-shadow:0 2px 5px rgba(15,23,42,.06);display:flex;flex-direction:column;gap:9px}
 .row1{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
 .code{font-size:16px;font-weight:700}
 .macrotag{font-size:10px;font-weight:700;color:#fff;padding:2px 7px;border-radius:9px;letter-spacing:.4px}
 .cnt{font-size:12px;color:var(--sub);font-weight:600}
 .segbar{height:12px;background:#f1f5f9;border-radius:6px;display:flex;overflow:hidden}
 .tolist{display:flex;flex-direction:column;gap:5px;margin-top:2px}
 .to{display:flex;align-items:center;gap:8px;font-size:11.5px}
 .tstat{font-size:9px;font-weight:700;padding:1px 6px;border-radius:7px;white-space:nowrap;min-width:58px;text-align:center}
 .tid{color:#0f172a;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1}
 .tagent{color:var(--sub);white-space:nowrap}
 footer{margin-top:32px;font-size:11.5px;color:var(--mut);border-top:1px solid var(--line);padding-top:14px;line-height:1.5}
 @media(max-width:820px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}.lname{width:130px}}
</style></head><body><div class="wrap">
 <header class="top"><div><h1>Opal &mdash; Task Order Dashboard</h1>
   <div class="subt">Active task orders by <b>agent load</b> and <b>project</b>. Bars sized by TO count, segmented by status.</div></div>
   <div class="asof">as of __ASOF__<br/>scope: __SCOPE__</div></header>
 <div class="stats" id="stats"></div>
 <div class="legend">
   <span><i class="dot" style="background:#15803d"></i>ACTIVE</span>
   <span><i class="dot" style="background:#b45309"></i>PENDING</span>
   <span><i class="dot" style="background:#b91c1c"></i>BLOCKED</span>
   <span><i class="dot" style="background:#94a3b8"></i>UNKNOWN</span></div>
 <div class="sectlbl">TO load by agent  &middot;  who is carrying how much</div>
 <div class="lb" id="lb"></div>
 <div class="sectlbl">By project</div>
 <div class="grid" id="grid"></div>
 <footer><b>Agent bar</b> = the number of active TOs assigned to that agent (primary assignee), segmented by status &mdash;
   the throughput/bottleneck read. <b>Project bar</b> = TO count, same status segments. A long ACTIVE bar = heavy live
   work; a long PENDING/BLOCKED bar = a queue to clear. Read-only snapshot &mdash; authoritative record is the TO files
   under <code>org/**/task_orders/</code>.</footer>
</div>
<script>
const AGENTS=__AGENTS__, PROJECTS=__PROJECTS__, MAXA=__MAXA__, MAXP=__MAXP__, STCOL=__STCOL__;
document.getElementById("stats").innerHTML=__STATS__.map(s=>
  `<div class="stat"><div class="n">${s[0]}</div><div class="l">${s[1]}</div></div>`).join("");
// agent leaderboard
document.getElementById("lb").innerHTML=AGENTS.map(a=>{
  const wpx=Math.max(2,Math.round(a.total/(MAXA||1)*100));
  const segs=["ACTIVE","PENDING","BLOCKED","UNKNOWN"].filter(k=>a.by[k]).map(k=>
    `<div class="seg" style="width:${a.by[k]/a.total*100}%;background:${STCOL[k]}"></div>`).join("");
  return `<div class="lrow"><div class="lname">${a.name}</div>
    <div class="ltrack" style="max-width:${wpx}%">${segs}</div><div class="lnum">${a.total}</div></div>`;
}).join("");
// project cards
const pill=k=>STCOL[k];
document.getElementById("grid").innerHTML=PROJECTS.map(p=>{
  const segs=["ACTIVE","PENDING","BLOCKED","UNKNOWN"].filter(k=>p.by[k]).map(k=>
    `<div class="seg" style="width:${p.by[k]/p.total*100}%;background:${STCOL[k]}"></div>`).join("");
  const rows=p.tos.map(t=>`<div class="to">
     <span class="tstat" style="background:${STCOL[t.s]}22;color:${STCOL[t.s]}">${t.s}</span>
     <span class="tid">${t.id}</span><span class="tagent">${t.agent}</span></div>`).join("");
  return `<div class="card" style="border-left-color:${p.color}">
    <div class="row1"><div><span class="code">${p.code}</span>
      <span class="macrotag" style="background:${p.color}">${p.macro}</span></div>
      <span class="cnt">${p.total} TO${p.total>1?"s":""}</span></div>
    <div class="segbar">${segs}</div><div class="tolist">${rows}</div></div>`;
}).join("");
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--project", default=None)
    ap.add_argument("--assignee", default=None)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    ws = find_workspace()
    mod = load_engine(ws)

    # ---- reuse the engine to gather + classify TOs (same as its main()) ----
    hot_codes = None
    if not args.all and not args.project:
        hot_codes = mod.get_hot_prd_project_codes(mod.LOOKBACK_DAYS)

    tos = [mod.parse_to_file(f) for f in mod.find_all_to_files()]
    active = [t for t in tos if t["status_class"] not in ("COMPLETE", "NOT_MET")]
    if args.project:
        active = [t for t in active if t["project_code"] == args.project.upper()]
    elif hot_codes is not None:
        active = [t for t in active if t["project_code"] in hot_codes]
    if args.assignee:
        active = [t for t in active if args.assignee.lower() in t["assigned_to"].lower()]

    STCOL = {k: v[0] for k, v in ST.items()}

    # ---- by agent (primary assignee) ----
    by_agent = {}
    for t in active:
        primary = mod._agent_token(t["assigned_to"]).split(" ")[0]
        by_agent.setdefault(primary, []).append(t)
    agents = []
    for name, ts in by_agent.items():
        by = {}
        for t in ts:
            by[t["status_class"]] = by.get(t["status_class"], 0) + 1
        agents.append({"name": esc(name), "total": len(ts), "by": by})
    agents.sort(key=lambda a: (-a["total"], a["name"]))
    maxa = max([a["total"] for a in agents], default=1) or 1

    # ---- by project ----
    by_proj = {}
    for t in active:
        by_proj.setdefault(t["project_code"], []).append(t)
    projects = []
    for code, ts in by_proj.items():
        by = {}
        for t in ts:
            by[t["status_class"]] = by.get(t["status_class"], 0) + 1
        # order TOs blocked -> pending -> active -> unknown for the list
        order = {"BLOCKED": 0, "PENDING": 1, "ACTIVE": 2, "UNKNOWN": 3}
        ts_sorted = sorted(ts, key=lambda t: order.get(t["status_class"], 9))
        projects.append({
            "code": code, "macro": macro_of(code), "color": macro_color(code),
            "total": len(ts), "by": by,
            "tos": [{"id": esc(t["to_id"]), "agent": esc(mod._agent_token(t["assigned_to"])),
                     "s": t["status_class"]} for t in ts_sorted],
        })
    projects.sort(key=lambda p: (-p["total"], p["code"]))
    maxp = max([p["total"] for p in projects], default=1) or 1

    now = datetime.now(tz=timezone.utc)
    n_blocked = sum(1 for t in active if t["status_class"] == "BLOCKED")
    n_pending = sum(1 for t in active if t["status_class"] == "PENDING")
    scope = (f"project {args.project.upper()}" if args.project
             else "all workspace TOs" if args.all
             else f"hot PRD projects (<={mod.LOOKBACK_DAYS}d)")
    if args.assignee:
        scope += f" · assignee~={args.assignee}"
    stats = [
        [len(active), "active TOs"],
        [len(by_proj), "projects"],
        [len(by_agent), "agents"],
        [n_pending, "pending"],
        [n_blocked, "blocked"],
    ]

    htmlout = (TEMPLATE
               .replace("__ASOF__", now.strftime("%Y-%m-%d %H:%MZ"))
               .replace("__SCOPE__", esc(scope))
               .replace("__AGENTS__", json.dumps(agents))
               .replace("__PROJECTS__", json.dumps(projects))
               .replace("__MAXA__", str(maxa))
               .replace("__MAXP__", str(maxp))
               .replace("__STCOL__", json.dumps(STCOL))
               .replace("__STATS__", json.dumps(stats)))

    out = Path(args.out) if args.out else (ws.parent / "Opal_TaskOrder_Dashboard.html")
    out.write_text(htmlout, encoding="utf-8")
    print(f"TO-DASHBOARD written -> {out}")
    print(f"  {len(active)} active TOs | {len(by_proj)} projects | {len(by_agent)} agents "
          f"| {n_blocked} blocked | scope: {scope}")


if __name__ == "__main__":
    main()
