#!/usr/bin/env python3
"""render_dashboard.py -- the HTML card+bar DASHBOARD renderer for /registry-check.

The visual companion to the text `/registry-check` lens: instead of the vertical
What/Where/Why text records, this emits a single self-contained, Opal-branded HTML
dashboard -- one card per not-closed project, macro-colored, sized by a real
ACTIVITY BAR (commits referencing the project in the last N days), sorted busiest
-> quietest, with status pills + owner + last-touch.

DATA-DRIVEN (not a snapshot): it loads the canonical engine (.tools/registry-check.py)
and reuses its build_rows() -- so What/Where/Why/status/owner/age stay in ONE place
(the engine), and this script only adds the activity bar + the presentation. The
git-activity count is the one thing the text lens does not compute.

Usage:
  python .claude/skills/registry-check/render_dashboard.py
      -> writes Opal_Project_Dashboard.html to the Desktop (workspace parent), HOT only
  python .claude/skills/registry-check/render_dashboard.py --all
      -> include COLD (>72h) projects too
  python .claude/skills/registry-check/render_dashboard.py --days 14
      -> activity window (default 7 days)
  python .claude/skills/registry-check/render_dashboard.py --out PATH.html
      -> explicit output path

Read-only: pure filesystem + git, no MCP, no writes except the one HTML file.
"""
from __future__ import annotations

import argparse
import datetime
import html
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path


# ---- macro palette (extend freely; unknown macros get a stable hashed color) ----
MACRO_COLORS = {
    "NFRA": "#0a4b78", "ADVI": "#0891b2", "DATA": "#7c3aed", "SCTY": "#b91c1c",
    "ADHC": "#b45309", "ETFS": "#15803d", "PFMG": "#0d9488", "FIND": "#ca8a04",
    "ASTN": "#db2777", "COMP": "#0a4b78", "HEATMAP": "#64748b", "DATA_": "#7c3aed",
}
FALLBACK_PALETTE = ["#475569", "#0369a1", "#7c3aed", "#0891b2", "#b45309", "#be123c", "#15803d"]


def macro_color(macro_code: str) -> str:
    mc = (macro_code or "").upper().strip()
    if mc in MACRO_COLORS:
        return MACRO_COLORS[mc]
    if not mc:
        return "#475569"
    return FALLBACK_PALETTE[sum(ord(c) for c in mc) % len(FALLBACK_PALETTE)]


def find_workspace() -> Path:
    """Walk up from cwd + this file to the dir holding org/projects/REGISTRY.md."""
    for start in (Path.cwd(), Path(__file__).resolve()):
        p = start
        for _ in range(8):
            if (p / "org" / "projects" / "REGISTRY.md").exists():
                return p
            if p.parent == p:
                break
            p = p.parent
    # last resort: assume this script sits under <ws>/.claude/skills/registry-check/
    return Path(__file__).resolve().parents[3]


def load_engine(ws: Path):
    """Load the hyphenated .tools/registry-check.py as a module (reuse its logic)."""
    eng = ws / ".tools" / "registry-check.py"
    spec = importlib.util.spec_from_file_location("registry_check_engine", eng)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git_activity(codes, days: int) -> dict:
    """code -> count of commits (last `days`) whose message references the code."""
    try:
        log = subprocess.run(
            ["git", "log", f"--since={days} days ago", "--pretty=format:%s%n%b"],
            capture_output=True, text=True, errors="replace",
        ).stdout
    except Exception:
        return {c: 0 for c in codes}
    counts = {}
    for c in codes:
        counts[c] = len(re.findall(rf"\b{re.escape(c)}\b", log))
    return counts


def status_pill(status: str, where: str):
    """(css_class, label) -- derive a display pill from status + phase text."""
    s = (status or "").lower()
    w = (where or "").lower()
    if "held" in w or "parked" in w or "on hold" in w:
        return ("held", "HELD")
    if s.startswith("decompos"):
        return ("decomp", "DECOMPOSING")
    if "deprioritiz" in w or s in ("inactive", "paused", "on-hold", "hold"):
        return ("inactive", "PAUSED")
    if s in ("active", "dispatched", "dispatch", "staged", "go", "in_progress", "build-complete"):
        return ("active", "ACTIVE")
    return ("inactive", (status or "unknown").upper()[:14])


def fmt_age(age_h) -> str:
    if age_h is None:
        return "no commit"
    if age_h < 1:
        m = max(1, int(age_h * 60))
        return f"{m}m"
    if age_h < 24:
        return f"{age_h:.0f}h"
    return f"{age_h / 24:.1f}d"


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Opal &mdash; Project Dashboard</title>
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
 .legend{display:flex;flex-wrap:wrap;gap:14px;margin:16px 2px 6px;font-size:12px;color:var(--sub)}
 .legend span{display:inline-flex;align-items:center;gap:6px}
 .dot{width:11px;height:11px;border-radius:3px;display:inline-block}
 .sectlbl{font-size:12.5px;font-weight:700;color:#64748b;letter-spacing:1px;text-transform:uppercase;margin:26px 2px 12px}
 .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
 .card{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--navy);border-radius:12px;padding:16px 18px 15px;box-shadow:0 2px 5px rgba(15,23,42,.06);display:flex;flex-direction:column;gap:9px}
 .row1{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
 .code{font-size:16.5px;font-weight:700;letter-spacing:.2px}
 .macrotag{font-size:10px;font-weight:700;color:#fff;padding:2px 7px;border-radius:9px;letter-spacing:.4px}
 .mbadge{font-size:9.5px;font-weight:700;color:#64748b;border:1px solid #cbd5e1;border-radius:8px;padding:1px 6px;margin-left:6px;vertical-align:middle}
 .name{font-size:13px;color:var(--ink);line-height:1.3}
 .where{font-size:11.5px;color:var(--sub);line-height:1.35;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
 .meta{display:flex;gap:14px;font-size:11px;color:var(--sub);flex-wrap:wrap;align-items:center}
 .pill{font-size:10px;font-weight:700;padding:2px 8px;border-radius:9px;letter-spacing:.3px}
 .p-active{background:#dcfce7;color:#15803d}.p-decomp{background:#dbeafe;color:#0a4b78}
 .p-held{background:#fee2e2;color:#b91c1c}.p-inactive{background:#f1f5f9;color:#64748b}
 .owner{font-weight:600;color:#334155}
 .bar-wrap{display:flex;align-items:center;gap:10px;margin-top:2px}
 .bar-track{flex:1;height:11px;background:#f1f5f9;border-radius:6px;overflow:hidden}
 .bar-fill{height:100%;border-radius:6px}
 .bar-num{font-size:12px;font-weight:700;color:#334155;min-width:74px;text-align:right}
 .bar-num small{font-weight:400;color:var(--mut);font-size:10.5px}
 footer{margin-top:32px;font-size:11.5px;color:var(--mut);border-top:1px solid var(--line);padding-top:14px;line-height:1.5}
 @media(max-width:820px){.grid{grid-template-columns:1fr}.stats{grid-template-columns:repeat(2,1fr)}}
</style></head><body><div class="wrap">
 <header class="top"><div><h1>Opal &mdash; Project Dashboard</h1>
   <div class="subt">Every not-closed project, sized by <b>__DAYS__-day commit activity</b>. Cards ordered busiest &rarr; quietest.</div></div>
   <div class="asof">as of __ASOF__<br/>source: /registry-check + git (__DAYS__d)</div></header>
 <div class="stats" id="stats"></div>
 <div class="legend" id="legend"></div>
 <div class="sectlbl" id="sectlbl"></div>
 <div class="grid" id="grid"></div>
 <footer><b>Activity bar</b> = commits in the last __DAYS__ days whose message references the project code
   (full bar = the busiest project). A high bar means heavy in-flight work; a low bar on a fresh PRD means it was
   just chartered, not stalled. <b>Owner</b> = the role that last touched it. <b>Phase</b> is the one-line current
   state from the registry. Activity is a keyword count (relative heat, not an exact ledger).
   Read-only snapshot &mdash; authoritative record is <code>org/projects/REGISTRY.md</code> + each <code>*.json</code>.</footer>
</div>
<script>
const DATA=__DATA__, MACROS=__MACROS__, MAXACT=__MAXACT__;
document.getElementById("stats").innerHTML=__STATS__.map(s=>
  `<div class="stat"><div class="n">${s[0]}</div><div class="l">${s[1]}</div></div>`).join("");
document.getElementById("legend").innerHTML=Object.keys(MACROS).map(k=>
  `<span><i class="dot" style="background:${MACROS[k]}"></i>${k}</span>`).join("");
document.getElementById("sectlbl").textContent=__SECTLBL__;
const pc={active:"p-active",decomp:"p-decomp",held:"p-held",inactive:"p-inactive"};
document.getElementById("grid").innerHTML=DATA.map(d=>{
  const col=d.color, pct=Math.max(3,Math.round(d.act/(MAXACT||1)*100));
  const badge=d.macroFlag?`<span class="mbadge">${d.macroFlag}</span>`:"";
  return `<div class="card" style="border-left-color:${col}">
   <div class="row1"><div><span class="code">${d.code}</span>${badge}
     <span class="macrotag" style="background:${col}">${d.macro||"-"}</span></div>
     <span class="pill ${pc[d.pillCls]}">${d.pillTxt}</span></div>
   <div class="name">${d.name}</div><div class="where">${d.where}</div>
   <div class="bar-wrap"><div class="bar-track"><div class="bar-fill" style="width:${pct}%;background:${col}"></div></div>
     <div class="bar-num">${d.act} <small>commits</small></div></div>
   <div class="meta"><span class="owner">${d.owner}</span><span>touched ${d.age} ago</span></div></div>`;
}).join("");
</script></body></html>
"""


def build(rows, activity, section_label):
    """rows(list of engine dicts) + activity dict -> list of card dicts (sorted)."""
    cards = []
    macros_seen = {}
    for r in rows:
        code = r["code"]
        mc = r.get("macro_code") or ""
        col = macro_color(mc)
        if mc:
            macros_seen[mc] = col
        pill_cls, pill_txt = status_pill(r.get("status", ""), r.get("where", ""))
        cards.append({
            "code": code,
            "macro": mc,
            "macroFlag": "MACRO" if r.get("macro") else "",
            "color": col,
            "name": html.escape(r.get("what") or code),
            "where": html.escape(r.get("where") or "-"),
            "owner": html.escape(_short_owner(r.get("owner"))),
            "age": fmt_age(r.get("age_h")),
            "act": int(activity.get(code, 0)),
            "pillCls": pill_cls, "pillTxt": pill_txt,
        })
    cards.sort(key=lambda c: (-c["act"], c["code"]))
    return cards, macros_seen


_ENGINE = {"short_owner": None}


def _short_owner(owner):
    fn = _ENGINE["short_owner"]
    return fn(owner) if fn else (owner or "?")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="include COLD (>72h) projects")
    ap.add_argument("--days", type=int, default=7, help="activity window in days (default 7)")
    ap.add_argument("--out", default=None, help="output HTML path")
    args = ap.parse_args()

    ws = find_workspace()
    os.chdir(ws)                       # engine uses cwd-relative paths + git
    mod = load_engine(ws)
    _ENGINE["short_owner"] = getattr(mod, "short_owner", None)

    # Working-time engine (registry-check.py 2026-07-06, patch 6938340ce): build_rows now
    # TAKES (now, holidays) and returns a 3-tuple. Compute both from the engine so this
    # generator stays lockstep with /registry-check's holiday-aware classification.
    now, _pin = mod.resolve_asof([])
    holidays = mod.load_holidays()
    hot, cold, malformed = mod.build_rows(now, holidays)
    rows = hot + (cold if args.all else [])
    codes = [r["code"] for r in rows]
    activity = git_activity(codes, args.days)

    section = ("All not-closed projects (hot + cold)" if args.all
               else "Hot projects  ·  worked in the last 72h")
    cards, macros_seen = build(rows, activity, section)

    total = len(cards)
    total_commits = sum(activity.values())
    n_macros = len({r["macro_code"] for r in rows if r.get("macro_code")})
    busiest = cards[0]["code"] if cards else "-"
    maxact = max([c["act"] for c in cards], default=1) or 1
    held = sum(1 for c in cards if c["pillCls"] == "held")
    stats = [
        [total, "projects"],
        [f"{total_commits:,}", f"commits &middot; {args.days}d"],
        [n_macros, "active macros"],
        [busiest, "busiest"],
        [held, "held/parked"],
    ]

    htmlout = (TEMPLATE
               .replace("__DAYS__", str(args.days))
               .replace("__ASOF__", now.strftime("%Y-%m-%d %H:%MZ"))
               .replace("__DATA__", json.dumps(cards))
               .replace("__MACROS__", json.dumps(macros_seen))
               .replace("__MAXACT__", str(maxact))
               .replace("__STATS__", json.dumps(stats))
               .replace("__SECTLBL__", json.dumps(section))
               .replace("__MALF__", str(len(malformed))))

    out = Path(args.out) if args.out else (ws.parent / "Opal_Project_Dashboard.html")
    out.write_text(htmlout, encoding="utf-8")
    print(f"DASHBOARD written -> {out}")
    print(f"  {total} projects | {total_commits:,} commits/{args.days}d | busiest={busiest} | {len(malformed)} malformed")


if __name__ == "__main__":
    main()
