#!/usr/bin/env python3
"""render_activity_dashboard.py -- the HTML companion to /activity-check.

The visual companion to the text `/activity-check` lens: each active agent's 5 most
recent commits as a card, PLUS a summary section of three top-4+Other pie charts --
which MACROS get the most project-directed activity, which PROJECTS the most commits,
and which AGENTS commit the most.

DATA-DRIVEN + HARDENED: it consumes the STABLE `activity-check.py --json` public
contract (NOT the engine's internal functions), so an engine refactor cannot silently
break this generator -- only a --json schema change, the intended public contract, would.

Usage:
  python .claude/skills/activity-check/render_activity_dashboard.py            # 7d -> Desktop/Opal_Activity_Dashboard.html
  python .claude/skills/activity-check/render_activity_dashboard.py --days 3    # tighter window
  python .claude/skills/activity-check/render_activity_dashboard.py --out PATH.html
  python .claude/skills/activity-check/render_activity_dashboard.py --print

Read-only: writes only the one HTML file. Owned by 0.0.0_AB_MSTR (Andrew-direct 2026-07-06).
"""
from __future__ import annotations

import argparse
import html
import json
import subprocess
import sys
from pathlib import Path


def find_workspace() -> Path:
    for start in (Path.cwd(), Path(__file__).resolve()):
        p = start
        for _ in range(8):
            if (p / "org" / "projects" / "REGISTRY.md").exists():
                return p
            if p.parent == p:
                break
            p = p.parent
    return Path(__file__).resolve().parents[3]


MACRO_COLORS = {
    "NFRA": "#0a4b78", "ADVI": "#0891b2", "DATA": "#7c3aed", "SCTY": "#b91c1c",
    "ADHC": "#b45309", "ETFS": "#15803d", "PFMG": "#0d9488", "FIND": "#ca8a04",
    "ASTN": "#db2777", "COMP": "#0a4b78", "MDPF": "#0369a1", "YALP": "#9333ea",
    "HEATMAP": "#64748b", "EXPAND": "#0a4b78", "TRSB": "#0f766e", "SXPL": "#7c3aed",
}


def macro_color(mc: str) -> str:
    return MACRO_COLORS.get((mc or "").upper(), "#94a3b8")


def get_data(ws: Path, days: int) -> dict:
    """Fetch via the STABLE `activity-check.py --json` contract (no internal coupling)."""
    eng = ws / ".tools" / "activity-check.py"
    r = subprocess.run(
        [sys.executable, str(eng), "--json", "--days", str(days)],
        capture_output=True, text=True, cwd=str(ws),
    )
    if r.returncode != 0 or not r.stdout.strip():
        sys.stderr.write("ERROR: `activity-check.py --json` failed:\n" + (r.stderr or "")[:1000] + "\n")
        sys.exit(1)
    return json.loads(r.stdout)


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Opal &mdash; Activity Dashboard</title>
<style>
 :root{--bg:#f8fafc;--ink:#0f172a;--sub:#475569;--mut:#94a3b8;--line:#e2e8f0;--card:#fff;--navy:#0a4b78}
 *{box-sizing:border-box}
 body{margin:0;background:var(--bg);color:var(--ink);font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
 .wrap{max-width:1280px;margin:0 auto;padding:28px 32px 60px}
 header.top{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;border-bottom:2px solid #cbd5e1;padding-bottom:18px}
 h1{font-size:28px;font-weight:700;margin:0;letter-spacing:-.2px}
 .subt{font-size:15px;color:var(--sub);margin-top:6px}
 .asof{font-size:12.5px;color:var(--mut);text-align:right;white-space:nowrap}
 .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:22px 0 8px}
 .stat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;box-shadow:0 2px 4px rgba(15,23,42,.05)}
 .stat .n{font-size:24px;font-weight:700;color:var(--navy);line-height:1}
 .stat .l{font-size:11px;color:var(--sub);margin-top:6px;letter-spacing:.3px;text-transform:uppercase}
 .sectlbl{font-size:12.5px;font-weight:700;color:#64748b;letter-spacing:1px;text-transform:uppercase;margin:28px 2px 12px}
 .charts{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
 .chart{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;box-shadow:0 2px 5px rgba(15,23,42,.06)}
 .chart h3{font-size:13.5px;margin:0 0 3px;color:var(--ink)}
 .chart .cap{font-size:11px;color:var(--mut);margin-bottom:12px;line-height:1.3}
 .chartrow{display:flex;align-items:center;gap:16px}
 .chartrow svg{flex:none}
 .lgs{display:flex;flex-direction:column;gap:6px;flex:1;min-width:0}
 .lg{display:flex;align-items:center;gap:8px;font-size:11.5px}
 .lg i{width:11px;height:11px;border-radius:3px;flex:none}
 .lgl{color:#334155;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1;min-width:0}
 .lgv{color:var(--sub);font-weight:700;white-space:nowrap}
 .lgv small{font-weight:400;color:var(--mut)}
 .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
 .card{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--navy);border-radius:12px;padding:14px 18px 13px;box-shadow:0 2px 5px rgba(15,23,42,.06)}
 .crow{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:9px}
 .agent{font-size:15.5px;font-weight:700;letter-spacing:.2px}
 .rolebadge{font-size:9.5px;font-weight:700;color:#64748b;border:1px solid #cbd5e1;border-radius:8px;padding:1px 6px;margin-left:7px;vertical-align:middle}
 .cnum{font-size:12px;color:var(--sub);font-weight:600}
 .cmts{display:flex;flex-direction:column;gap:6px}
 .cmt{display:flex;align-items:baseline;gap:8px;font-size:11.5px;line-height:1.3}
 .mtag{font-size:9px;font-weight:700;color:#fff;padding:1px 6px;border-radius:7px;white-space:nowrap;flex:none;min-width:64px;text-align:center}
 .cage{color:var(--mut);font-size:10.5px;white-space:nowrap;flex:none;width:34px;text-align:right}
 .csub{color:#334155;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;flex:1;min-width:0}
 footer{margin-top:32px;font-size:11.5px;color:var(--mut);border-top:1px solid var(--line);padding-top:14px;line-height:1.5}
 @media(max-width:900px){.charts{grid-template-columns:1fr}.grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}}
</style></head><body><div class="wrap">
 <header class="top"><div><h1>Opal &mdash; Activity Dashboard</h1>
   <div class="subt">Each active agent's <b>5 most recent commits</b>, and where recent activity is directed.</div></div>
   <div class="asof">as of __ASOF__<br/>source: git (__DAYS__d) + org/projects</div></header>
 <div class="stats" id="stats"></div>
 <div class="sectlbl">Where recent activity is directed  &middot;  top 4 + Other</div>
 <div class="charts" id="charts"></div>
 <div class="sectlbl">Active agents  &middot;  5 most recent commits each  &middot;  busiest first</div>
 <div class="grid" id="grid"></div>
 <footer><b>Active agent</b> = a fabric serial that committed in the last __DAYS__ days (pod numbers
   collapsed to the role-agent, e.g. the three AE_PartnerETL pods count as one). <b>Macros / Projects</b>
   charts count PROJECT-DIRECTED commits only (a "drive cycle" / "/govern" / "log" commit references no
   project, so it is excluded from those two but still counts for <b>Agents</b>, which is ALL commits =
   raw volume). Each commit's project is resolved by matching its message against the known
   <code>org/projects/*.json</code> codes. Read-only snapshot &mdash; authoritative record is git +
   the TO / project files. Generated by <code>.claude/skills/activity-check/render_activity_dashboard.py</code>.</footer>
</div>
<script>
const STATS=__STATS__, CHARTS=__CHARTS__, AGENTS=__AGENTS__, DAYS=__DAYS__;
const CATEG=["#0a4b78","#0891b2","#7c3aed","#b45309","#94a3b8"];
document.getElementById("stats").innerHTML=STATS.map(s=>
  `<div class="stat"><div class="n">${s[0]}</div><div class="l">${s[1]}</div></div>`).join("");

function pie(slices,size){
  const total=slices.reduce((a,x)=>a+x.value,0)||1, r=size/2, cx=r, cy=r;
  if(slices.length<=1){ return `<svg width="${size}" height="${size}"><circle cx="${cx}" cy="${cy}" r="${r}" fill="${CATEG[0]}"/></svg>`; }
  let a0=-Math.PI/2, out="";
  slices.forEach((s,i)=>{
    const frac=s.value/total, a1=a0+frac*2*Math.PI, col=CATEG[Math.min(i,CATEG.length-1)];
    if(frac>=0.9999){ out+=`<circle cx="${cx}" cy="${cy}" r="${r}" fill="${col}"/>`; a0=a1; return; }
    const x0=(cx+r*Math.cos(a0)).toFixed(2), y0=(cy+r*Math.sin(a0)).toFixed(2);
    const x1=(cx+r*Math.cos(a1)).toFixed(2), y1=(cy+r*Math.sin(a1)).toFixed(2);
    const large=frac>0.5?1:0;
    out+=`<path d="M${cx},${cy} L${x0},${y0} A${r},${r} 0 ${large} 1 ${x1},${y1} Z" fill="${col}"/>`;
    a0=a1;
  });
  return `<svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">${out}</svg>`;
}
function legend(slices){
  const total=slices.reduce((a,x)=>a+x.value,0)||1;
  return slices.map((s,i)=>`<div class="lg"><i style="background:${CATEG[Math.min(i,4)]}"></i>
    <span class="lgl">${s.label}</span><span class="lgv">${s.value} <small>${(s.value/total*100).toFixed(0)}%</small></span></div>`).join("");
}
document.getElementById("charts").innerHTML=CHARTS.map(c=>
  `<div class="chart"><h3>${c.title}</h3><div class="cap">${c.cap}</div>
    <div class="chartrow">${pie(c.slices,118)}<div class="lgs">${legend(c.slices)}</div></div></div>`).join("");

document.getElementById("grid").innerHTML=AGENTS.map(a=>{
  const rows=a.recent.map(c=>`<div class="cmt">
     <span class="cage">${c.age}</span>
     <span class="mtag" style="background:${c.color}">${c.code}</span>
     <span class="csub">${c.subj}</span></div>`).join("");
  return `<div class="card"><div class="crow"><div><span class="agent">${a.agent}</span>
     <span class="rolebadge">${a.role}</span></div>
     <span class="cnum">${a.n} commits &middot; ${DAYS}d</span></div>
    <div class="cmts">${rows}</div></div>`;
}).join("");
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--out", default=None)
    ap.add_argument("--print", dest="to_stdout", action="store_true")
    args = ap.parse_args()

    ws = find_workspace()
    d = get_data(ws, args.days)

    stats = [
        [d["n_active_agents"], "active agents"],
        [f"{d['n_commits']:,}", f"commits &middot; {d['days']}d"],
        [f"{d['n_directed']:,}", "project-directed"],
        [d["pie_agent"][0]["label"] if d["pie_agent"] else "-", "busiest agent"],
    ]
    charts = [
        {"title": "Macros", "cap": "most project-directed activity", "slices": d["pie_macro"]},
        {"title": "Projects", "cap": "most commits (directed)", "slices": d["pie_project"]},
        {"title": "Agents", "cap": "most commits (all, raw volume)", "slices": d["pie_agent"]},
    ]
    agents = [{
        "agent": html.escape(a["agent"]),
        "role": html.escape(a["role"]),
        "n": a["n_window"],
        "recent": [{
            "code": html.escape(c["code"]),
            "color": macro_color(c["macro"]),
            "age": html.escape(c["age"]),
            "subj": html.escape(c["subj"][:110]),
        } for c in a["recent"]],
    } for a in d["agents"]]

    out_html = (TEMPLATE
                .replace("__ASOF__", d["as_of"])
                .replace("__STATS__", json.dumps(stats, ensure_ascii=True))
                .replace("__CHARTS__", json.dumps(charts, ensure_ascii=True))
                .replace("__AGENTS__", json.dumps(agents, ensure_ascii=True))
                .replace("__DAYS__", str(d["days"])))

    if args.to_stdout:
        sys.stdout.write(out_html)
        return
    out = Path(args.out) if args.out else (ws.parent / "Opal_Activity_Dashboard.html")
    out.write_text(out_html, encoding="utf-8")
    print(f"ACTIVITY-DASHBOARD written -> {out}")
    print(f"  {d['n_active_agents']} active agents | {d['n_commits']:,} commits/{d['days']}d "
          f"| busiest={d['pie_agent'][0]['label'] if d['pie_agent'] else '-'}")


if __name__ == "__main__":
    main()
