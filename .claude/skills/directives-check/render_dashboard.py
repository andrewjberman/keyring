#!/usr/bin/env python3
"""render_dashboard.py -- the HTML DASHBOARD for /directives-check (Andrew's internal directives view).

Andrew-direct 2026-08-20 (verbatim): "/directives-check which is for me internally and shows the
current state of directives + creates a render for visible analysis. Then there should also be
/daily-sprint which essentially is just a formatted text version i can copy/paste ... for the Opal
teams channel." So the RENDER lives here; /daily-sprint stays text-only.

One DEVICE-colored card per LIVE directive (LAPTOP / SITEZ / UNRULED per the LD-0428 boundary):
activity bar (commits mentioning the code in N days -- A MENTION COUNT, NOT A WORK MEASURE), member
projects as status pills, open-TO load, the compacted stance, the row's own per-row freshness, and
flags WITH THEIR BASIS beside them; then the RETIRED partition from the machine-cut view with each
cut's authority; malformed rows surfaced. Design input: CTO's withdrawn draft (taken whole).

DATA-DRIVEN: consumes ONLY the stable `directives-check.py --all --json` public contract, never
the engine's internals (the /registry-check renderer's deliberate decoupling).

Usage:
  python .claude/skills/directives-check/render_dashboard.py            # -> Desktop/Opal_Directives_Dashboard.html
  python .claude/skills/directives-check/render_dashboard.py --days 14 --out PATH.html
Read-only except the one HTML file. Desktop = the workspace's parent dir (same as /registry-check).
"""
from __future__ import annotations

import argparse
import datetime
import html
import json
import re
import subprocess
import sys
from pathlib import Path

DEVICE_COLORS = {"LAPTOP": "#0a4b78", "SITEZ": "#7c3aed", "UNRULED": "#b45309"}


def find_workspace() -> Path:
    for start in (Path.cwd(), Path(__file__).resolve()):
        p = start
        for _ in range(8):
            if (p / "org" / "missions" / "DIRECTIVES.yaml").exists():
                return p
            if p.parent == p:
                break
            p = p.parent
    return Path(__file__).resolve().parents[3]


def get_rows(ws: Path):
    r = subprocess.run([sys.executable, str(ws / ".tools" / "directives-check.py"), "--all", "--json"],
                       capture_output=True, text=True, cwd=str(ws))
    if r.returncode != 0 or not r.stdout.strip():
        sys.stderr.write("ERROR: directives-check.py --all --json failed:\n" + (r.stderr or "")[:1000] + "\n")
        sys.exit(1)
    d = json.loads(r.stdout)
    return d.get("live", []), d.get("retired", []), d.get("malformed", []), d.get("ever_minted")


def git_activity(ws: Path, codes, days: int) -> dict:
    try:
        log = subprocess.run(["git", "log", "--all", f"--since={days} days ago", "--pretty=format:%s%n%b"],
                             capture_output=True, text=True, errors="replace", cwd=str(ws)).stdout
    except Exception:
        return {c: 0 for c in codes}
    return {c: len(re.findall(rf"\b{re.escape(c)}\b", log)) for c in codes}


def esc(s) -> str:
    return html.escape(str(s if s is not None else ""))


def project_pills(projects: dict) -> str:
    if not projects:
        return '<span class="pill none">no member projects</span>'
    out = []
    for code, status in sorted(projects.items()):
        s = (status or "").lower()
        cls = ("closed" if "closed" in s or "complete" in s else "nojson" if "no-json" in s or "malformed" in s else "active")
        out.append(f'<span class="pill {cls}">{esc(code)}<em>{esc(status)}</em></span>')
    return "".join(out)


def flag_pills(flags) -> str:
    out = []
    for f in (flags or []):
        cls = "hint" if ("MEMBERS-ALL-CLOSED" in f or "MEMBERS-STALE" in f) else "warn"
        out.append('<span class="flag ' + cls + '">' + esc(f) + "</span>")
    return "".join(out)


CSS = """
:root{--ink:#0f172a;--mut:#64748b;--line:#e2e8f0;--bg:#f8fafc;--card:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
header{background:#0f172a;color:#fff;padding:22px 28px}
header h1{margin:0;font-size:20px;letter-spacing:.3px}
header .sub{color:#94a3b8;font-size:12.5px;margin-top:6px}
.wrap{max-width:1180px;margin:0 auto;padding:22px 28px 56px}
h2.sec{font-size:12px;text-transform:uppercase;letter-spacing:1.2px;color:var(--mut);margin:26px 0 12px;border-bottom:1px solid var(--line);padding-bottom:7px}
.card{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--dev);border-radius:9px;padding:15px 17px;margin-bottom:12px;box-shadow:0 1px 2px rgba(15,23,42,.05)}
.chead{display:flex;align-items:baseline;gap:11px;flex-wrap:wrap}
.code{font-weight:700;font-size:15px;color:var(--dev)}
.title{font-weight:600;flex:1;min-width:230px}
.dev{font-size:10.5px;font-weight:700;letter-spacing:.6px;color:#fff;background:var(--dev);padding:2px 8px;border-radius:20px}
.meta{color:var(--mut);font-size:12px;margin-top:7px;display:flex;gap:16px;flex-wrap:wrap}
.bar{height:5px;background:#e2e8f0;border-radius:3px;margin:11px 0 9px;overflow:hidden}
.bar i{display:block;height:100%;background:var(--dev);border-radius:3px}
.pill{display:inline-block;font-size:11px;border-radius:5px;padding:2px 7px;margin:3px 5px 0 0;background:#eef2f7;color:#334155;border:1px solid var(--line)}
.pill em{font-style:normal;color:var(--mut);margin-left:6px;font-size:10px}
.pill.active{background:#ecfdf5;border-color:#a7f3d0;color:#065f46}
.pill.closed{background:#f1f5f9;color:#64748b}
.pill.nojson{background:#fef2f2;border-color:#fecaca;color:#991b1b}
.pill.none{background:#fff7ed;border-color:#fed7aa;color:#9a3412}
.flag{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.4px;border-radius:5px;padding:2px 8px;margin-left:7px}
.flag.hint{background:#fef9c3;color:#854d0e;border:1px solid #fde68a}
.flag.warn{background:#fee2e2;color:#991b1b;border:1px solid #fecaca}
.stance{margin-top:9px;padding:9px 11px;background:#f8fafc;border-left:3px solid var(--line);border-radius:0 6px 6px 0;color:#334155;font-size:12.5px}
.tos{font-weight:700}
.retired .card{border-left-color:#94a3b8;opacity:.86}
.retired .code{color:#475569}
footer{color:var(--mut);font-size:11.5px;margin-top:26px;border-top:1px solid var(--line);padding-top:12px;line-height:1.7}
"""


def render(ws: Path, days: int, out: Path) -> None:
    live, retired, malformed, ever = get_rows(ws)
    acts = git_activity(ws, [r.get("code", "") for r in live], days)
    peak = max([acts.get(r.get("code", ""), 0) for r in live] or [0]) or 1
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%MZ")

    def card(r, is_retired=False):
        code = r.get("code", "?")
        dev = (r.get("device") or "UNRULED").upper()
        col = "#94a3b8" if is_retired else DEVICE_COLORS.get(dev, "#475569")
        n = acts.get(code, 0)
        pct = 0 if is_retired else int(100 * n / peak)
        prd_note = "" if r.get("prd_exists", True) else ' <span class="flag warn">PRD MISSING</span>'
        bar = "" if is_retired else (f'<div class="bar"><i style="width:{pct}%"></i></div>'
                                     f'<div class="meta"><span>{n} commit(s) mentioning <b>{esc(code)}</b> in {days}d (mention count, not a work measure)</span></div>')
        auth_html = (f'<div class="stance"><b>Retired {esc(r.get("at",""))} by {esc(r.get("by",""))} &mdash; authority:</b> {esc(r.get("authority",""))}</div>'
                     if is_retired else "")
        subs = ", ".join(r.get("subgroups") or []) or "-"
        return f"""
<div class="card" style="--dev:{col}">
  <div class="chead"><span class="code">{esc(code)}</span><span class="title">{esc(r.get('title',''))}{prd_note}</span><span class="dev">{esc(dev)}</span>{flag_pills(r.get('flags'))}</div>
  <div class="meta"><span>PRD: {esc(r.get('directive','-'))}</span><span class="tos">{esc(r.get('open_tos',0))} open TO(s)</span><span>last: {esc(r.get('last','-'))}</span></div>
  {bar}
  <div>{project_pills(r.get('projects') or {})}</div>
  <div class="meta"><span>subgroups: {esc(subs)}</span></div>
  <div class="stance">{esc(r.get('stance',''))}</div>
  {auth_html}
</div>"""

    live_html = "".join(card(r) for r in live)
    ret_html = "".join(card(r, True) for r in retired)
    mal = (f'<h2 class="sec">Malformed ({len(malformed)}) -- surfaced, never dropped</h2>'
           + "".join(f'<div class="card" style="--dev:#b91c1c">{esc(m)}</div>' for m in malformed)) if malformed else ""
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Opal &mdash; Directives Register</title><style>{CSS}</style></head>
<body>
<header><h1>Opal &mdash; Directives Register</h1>
<div class="sub">live {len(live)} &middot; retired {len(retired)} &middot; ever minted {esc(ever)} &middot; malformed {len(malformed)} &middot; activity window {days}d &middot; rendered {now}</div></header>
<div class="wrap">
  <h2 class="sec">Live directives ({len(live)})</h2>
  {live_html}
  <div class="retired"><h2 class="sec">Retired ({len(retired)}) &mdash; machine-cut, byte-frozen (LD-0433)</h2>{ret_html}</div>
  {mal}
  <footer>
   Rendered from the <code>directives-check.py --all --json</code> public contract; the activity bar is a MENTION count, not a work measure.<br/>
   <b>MEMBERS-ALL-CLOSED</b> = every recorded member project closed with zero open TOs &mdash; MEMBERSHIP CURRENCY, not work completion (a directive
   whose scope outgrew its recorded members reads this way while its work is alive); <b>MEMBERS-STALE?</b> = the stance moved after the member set
   last did. Hints for the register owner; retirement is the FACT + MOVE + CHECK chain on Andrew's word. Read-only lens.
  </footer>
</div></body></html>"""
    out.write_text(doc, encoding="utf-8")
    print(f"wrote {out}")
    print(f"DIRECTIVES-DASHBOARD-RESULT live={len(live)} retired={len(retired)} ever_minted={ever} malformed={len(malformed)} window={days}d")


def main() -> int:
    ap = argparse.ArgumentParser(description="/directives-check HTML dashboard")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    ws = find_workspace()
    out = Path(a.out) if a.out else (ws.parent / "Opal_Directives_Dashboard.html")
    render(ws, a.days, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
