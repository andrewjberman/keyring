#!/usr/bin/env python3
"""render_prd_delta_dashboard.py -- the HTML card+bar DASHBOARD renderer for /prd-delta.

The visual companion to the /prd-delta text lens: one card per assessed project,
sorted worst-completeness first, with a horizontal COMPLETION bar (colored red/
amber/green by percentage) and a bullet list of what's still missing in natural
language -- the two things Andrew asked this dashboard to show explicitly.

DATA-DRIVEN, not a snapshot: reads the SAME persisted JSON the text lens
(`prd-delta-report.py`) reads (default org/mcp/prd_delta_results/latest.json,
written by the /prd-delta Workflow fan-out). This script does zero assessment
itself -- pure presentation, same split as its /registry-check sibling
(render_dashboard.py), whose CSS/layout this borrows for visual consistency
across the dashboard family.

Usage:
  python .claude/skills/prd-delta/render_prd_delta_dashboard.py
      -> writes Opal_PRDDelta_Dashboard.html to the Desktop
  python .claude/skills/prd-delta/render_prd_delta_dashboard.py --path PATH.json
  python .claude/skills/prd-delta/render_prd_delta_dashboard.py --out PATH.html
"""
from __future__ import annotations

import argparse
import datetime
import html
import json
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


def bar_color(pct) -> str:
    if pct is None:
        return "#94a3b8"          # gray -- N/A (no PRD)
    if pct >= 90:
        return "#15803d"          # green
    if pct >= 50:
        return "#ca8a04"          # amber
    return "#b91c1c"              # red


def pill(label: str):
    m = {
        "NO-PRD": ("p-inactive", "NO PRD"),
        "NOT-STARTED": ("p-held", "NOT STARTED"),
        "EARLY": ("p-held", "EARLY"),
        "IN-PROGRESS": ("p-decomp", "IN PROGRESS"),
        "MOSTLY-COMPLETE": ("p-decomp", "MOSTLY COMPLETE"),
        "COMPLETE": ("p-active", "COMPLETE"),
        "ASSESS-FAILED": ("p-held", "ASSESS FAILED"),
    }
    return m.get(label, ("p-inactive", label or "?"))


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Opal &mdash; PRD Delta Dashboard</title>
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
 .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:18px}
 .card{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--navy);border-radius:12px;padding:16px 18px 15px;box-shadow:0 2px 5px rgba(15,23,42,.06);display:flex;flex-direction:column;gap:9px}
 .row1{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
 .code{font-size:16.5px;font-weight:700;letter-spacing:.2px}
 .pill{font-size:10px;font-weight:700;padding:2px 8px;border-radius:9px;letter-spacing:.3px}
 .p-active{background:#dcfce7;color:#15803d}.p-decomp{background:#dbeafe;color:#0a4b78}
 .p-held{background:#fef3c7;color:#92400e}.p-inactive{background:#f1f5f9;color:#64748b}
 .bar-wrap{display:flex;align-items:center;gap:10px;margin-top:2px}
 .bar-track{flex:1;height:13px;background:#f1f5f9;border-radius:7px;overflow:hidden}
 .bar-fill{height:100%;border-radius:7px}
 .bar-num{font-size:13px;font-weight:700;color:#334155;min-width:44px;text-align:right}
 .mism{font-size:11.5px;color:#b91c1c;background:#fee2e2;border-radius:6px;padding:5px 9px;line-height:1.35}
 .missing{font-size:12px;color:var(--ink);line-height:1.5;margin:2px 0 0}
 .missing ul{margin:2px 0 0;padding-left:18px}
 .missing li{margin-bottom:2px}
 .missing .lbl{font-size:10.5px;font-weight:700;color:#64748b;text-transform:uppercase;letter-spacing:.3px}
 .undoc{font-size:11px;color:#7c3aed;background:#f3e8ff;border-radius:6px;padding:5px 9px;line-height:1.4;margin-top:2px}
 .undoc ul{margin:2px 0 0;padding-left:16px}
 footer{margin-top:32px;font-size:11.5px;color:var(--mut);border-top:1px solid var(--line);padding-top:14px;line-height:1.5}
 @media(max-width:820px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}}
</style></head><body><div class="wrap">
 <header class="top"><div><h1>Opal &mdash; PRD Delta Dashboard</h1>
   <div class="subt">Per-project completeness: PRD promises vs. what TOs + commits actually show landed. Cards ordered worst &rarr; best.</div></div>
   <div class="asof">as of __ASOF__<br/>source: /prd-delta (agent-assessed, not a keyword count)</div></header>
 <div class="stats" id="stats"></div>
 <div class="grid" id="grid"></div>
 <footer><b>Completion bar</b> = the assessing agent's measured completeness (PRD deliverables with
   real landed TO+commit evidence / total deliverables) &mdash; gray means no PRD exists for that
   project at all. <b>Missing</b> = natural-language bullets of unmet PRD items, most useful field
   on this dashboard. <b>Registry mismatch</b> (red banner) flags when org/projects/*.json's claimed
   status disagrees with the measured evidence. This is an LLM judgment pass over the same TOs/commits
   /to-check and /activity-check show mechanically &mdash; treat it as a strong signal, not a certified audit.
   Read-only. Re-run <code>/prd-delta</code> to refresh.</footer>
</div>
<script>
const DATA=__DATA__;
document.getElementById("stats").innerHTML=__STATS__.map(s=>
  `<div class="stat"><div class="n">${s[0]}</div><div class="l">${s[1]}</div></div>`).join("");
document.getElementById("grid").innerHTML=DATA.map(d=>{
  const pctTxt = d.pct===null ? "N/A" : `${d.pct}%`;
  const width = d.pct===null ? 100 : Math.max(3,d.pct);
  const mism = d.mismatch ? `<div class="mism"><b>REGISTRY MISMATCH:</b> ${d.mismatch}</div>` : "";
  const missItems = d.missing.length
    ? `<ul>${d.missing.map(m=>`<li>${m}</li>`).join("")}</ul>`
    : `<div style="color:#15803d">Nothing outstanding.</div>`;
  const undoc = d.undoc.length
    ? `<div class="undoc"><span class="lbl">Undocumented activity</span><ul>${d.undoc.map(u=>`<li>${u}</li>`).join("")}</ul></div>`
    : "";
  return `<div class="card" style="border-left-color:${d.color}">
   <div class="row1"><span class="code">${d.code}</span>
     <span class="pill ${d.pillCls}">${d.pillTxt}</span></div>
   <div class="bar-wrap"><div class="bar-track"><div class="bar-fill" style="width:${width}%;background:${d.color}"></div></div>
     <div class="bar-num">${pctTxt}</div></div>
   ${mism}
   <div class="missing"><span class="lbl">Missing</span>${missItems}</div>
   ${undoc}
  </div>`;
}).join("");
</script></body></html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=None, help="results JSON path (default org/mcp/prd_delta_results/latest.json)")
    ap.add_argument("--out", default=None, help="output HTML path")
    args = ap.parse_args()

    ws = find_workspace()
    results_path = Path(args.path) if args.path else (ws / "org" / "mcp" / "prd_delta_results" / "latest.json")
    if not results_path.exists():
        sys.stderr.write(f"ERROR: no results file at {results_path} -- run /prd-delta first.\n")
        sys.exit(1)
    d = json.loads(results_path.read_text(encoding="utf-8-sig", errors="replace"))
    results = d.get("results", [])

    cards = []
    for r in sorted(results, key=lambda r: (r.get("completeness_pct") is not None, r.get("completeness_pct") or 0)):
        pct = r.get("completeness_pct")
        cls, txt = pill(r.get("completeness_label", ""))
        cards.append({
            "code": r.get("code", "?"),
            "pct": pct,
            "color": bar_color(pct),
            "pillCls": cls, "pillTxt": txt,
            "mismatch": html.escape(str(r.get("registry_mismatch"))) if r.get("registry_mismatch") else "",
            "missing": [html.escape(str(m)) for m in (r.get("missing") or [])],
            "undoc": [html.escape(str(u)) for u in (r.get("undocumented_activity") or [])],
        })

    now = datetime.datetime.now(datetime.timezone.utc)
    pcts = [c["pct"] for c in cards if c["pct"] is not None]
    avg = round(sum(pcts) / len(pcts)) if pcts else 0
    stats = [
        [len(cards), "projects assessed"],
        [f"{avg}%", "avg completeness"],
        [sum(1 for c in cards if c["pct"] is None), "no PRD"],
        [sum(1 for c in cards if c["mismatch"]), "registry mismatches"],
    ]

    htmlout = (TEMPLATE
               .replace("__ASOF__", now.strftime("%Y-%m-%d %H:%MZ"))
               .replace("__DATA__", json.dumps(cards))
               .replace("__STATS__", json.dumps(stats)))

    out = Path(args.out) if args.out else (ws.parent / "Opal_PRDDelta_Dashboard.html")
    out.write_text(htmlout, encoding="utf-8")
    print(f"PRD-DELTA DASHBOARD written -> {out}")
    print(f"  {len(cards)} projects | avg completeness {avg}% | "
          f"{sum(1 for c in cards if c['pct'] is None)} no-PRD | "
          f"{sum(1 for c in cards if c['mismatch'])} mismatches")


if __name__ == "__main__":
    main()
