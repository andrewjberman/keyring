#!/usr/bin/env python3
"""Render the day's DAILY SPRINT markdown as a Teams-ready operating-report IMAGE page.

    python .claude/skills/daily-sprint/render_sprint.py [--date YYYY-MM-DD] [--out PATH]

WHY THIS EXISTS (Andrew-direct 2026-08-26 ~23:0xZ): the sprint was a Teams TEXT post, and
Teams' renderer forced a growing pile of formatting workarounds (spacer bullets carrying a
non-breaking space, no-heading rules, collapse hacks) that a reader could "tidy" and silently
break. His call: *"there is no reason this should be text and f***ing around with illegible
teams formatting."* An image renders identically everywhere and takes the renderer out of the
loop entirely -- so the LAYOUT LAW lives here, in code, instead of in prose nobody can enforce.

Pattern follows the estate's existing generative layer (`/to-check`, `/registry-check`):
a render script in the skill dir emits ONE self-contained HTML file to the Desktop, surfaced
inline. Self-contained is load-bearing: no external CSS/fonts/images, so the page screenshots
identically on any box and at any time.

The markdown is the CONTENT and this file is the PRESENTATION. Parsing is deliberately
tolerant of both the plain-uppercase Teams shape (TODAY SPRINT / PROJECTS / PROCESS / BLOCKED)
and the older bolded-header form, because a render that drops a section is worse than one that
renders it plainly.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path


def workspace_root() -> Path:
    return Path(__file__).resolve().parents[3]


# --- parsing -----------------------------------------------------------------

SECTIONS = ("TODAY SPRINT", "PROJECTS", "PROCESS", "BLOCKED", "BLOCKS")


def _clean(line: str) -> str:
    """Strip list markers and the Teams spacer artefacts from a content line."""
    s = line.rstrip()
    s = re.sub(r"^\s*[-*•]\s+", "", s)
    s = s.replace(" ", " ")            # the retired spacer NBSP
    s = re.sub(r"^\s*&nbsp;\s*$", "", s)
    return s.strip()


def _is_spacer(line: str) -> bool:
    body = line.strip().lstrip("-*•").replace(" ", "").replace("&nbsp;", "")
    return line.strip() != "" and body.strip() == ""


def split_sections(text: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    cur = None
    for raw in text.split("\n"):
        probe = raw.strip().strip("*# ").upper().rstrip(":")
        if probe in SECTIONS:
            cur = "BLOCKED" if probe == "BLOCKS" else probe
            out.setdefault(cur, [])
            continue
        if cur:
            out[cur].append(raw)
    return out


ITEM_RE = re.compile(r"^\s*[-*•]?\s*\**\s*Item\s+(\d+)\s*[—–-]\s*(.+?)\**\s*$")


def parse_items(lines: list[str]) -> list[dict]:
    """Item title lines + whatever is indented beneath them."""
    items: list[dict] = []
    for raw in lines:
        if _is_spacer(raw):
            continue
        m = ITEM_RE.match(raw)
        if m:
            items.append({"n": m.group(1), "name": m.group(2).strip(), "body": []})
        elif items and raw.strip():
            items[-1]["body"].append(_clean(raw))
    return items


def parse_bullets(lines: list[str]) -> list[str]:
    out: list[str] = []
    for raw in lines:
        if _is_spacer(raw) or not raw.strip():
            continue
        c = _clean(raw)
        if c:
            out.append(c)
    return out



TABLE_ROW = re.compile(r"^\s*\|\s*(\d+)\s*[—–-]\s*(.+?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*$")


def parse_process_table(lines: list[str]) -> list[dict]:
    """Fallback for the RETIRED `| Item | Timing | Status |` table form.

    A section that silently renders EMPTY is the worst outcome here -- the reader
    cannot tell a missing section from an absent one. Measured on the first render:
    PROCESS vanished because the day's file still carried the table.
    """
    items = []
    for raw in lines:
        m = TABLE_ROW.match(raw)
        if not m or set(raw.replace("|", "").strip()) <= set("-: "):
            continue
        items.append({"n": m.group(1), "name": m.group(2).strip(),
                      "body": [f"Timeline: {m.group(3)}", f"Status: {m.group(4)}"]})
    return items


TIMELINE_RE = re.compile(r"\**\s*Timeline\s*:\s*(.+?)\**\s*$", re.I)
STATUS_RE = re.compile(r"\**\s*Status\s*:\s*\**\s*(.+?)\s*$", re.I)


def split_process(body: list[str]) -> tuple[str, str]:
    timeline, status, rest = "", "", []
    for ln in body:
        m = TIMELINE_RE.match(ln)
        if m:
            timeline = m.group(1).strip().rstrip(".")
            continue
        m = STATUS_RE.match(ln)
        if m:
            status = m.group(1).strip()
            continue
        rest.append(ln)
    if not status and rest:
        status = " ".join(rest)
    return timeline, status


# --- presentation ------------------------------------------------------------

def md_inline(s: str) -> str:
    """Escape, then honour **bold** and "quotes" -- content may carry deliberate emphasis."""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s


def status_class(status: str) -> str:
    """Classify a PROCESS status into a pill.

    WORD-BOUNDARY MATCHING IS MANDATORY, and the order is specific-before-general.
    Measured on the first render: a substring classifier read "rest" inside
    "restore" and "complete" inside "completed" -- putting IDLE on a shipping item
    and ON TRACK on one that is idle by design. The pill is the first thing a
    partner's eye lands on, so a wrong pill is worse than no pill; this is the
    estate's common-noun-token trap in a renderer.
    """
    t = status.lower()
    WORDS = set(re.findall("[a-z]+", t))

    def has(*words: str) -> bool:
        return bool(WORDS.intersection(words))

    if has("hold", "held", "waiting", "blocked", "gating", "gates") or "on hold" in t:
        return "hold"
    if has("idle", "resting", "dormant") or "no movement" in t:
        return "idle"
    if has("unblocked", "complete", "completed", "certified", "delivered", "done",
           "resolved", "cleared", "restored", "driving", "underway", "progressing"):
        return "ok"
    return "neut"


PILL_LABEL = {"ok": "on track", "hold": "held", "idle": "idle", "neut": "active"}


CSS = """
*{box-sizing:border-box}
body{margin:0;background:#eef2f6;font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
 -webkit-font-smoothing:antialiased;color:#0f172a}
.page{width:1180px;margin:0 auto;background:#fff;padding:34px 40px 30px}
.hdr{display:flex;justify-content:space-between;align-items:flex-end;
 border-bottom:3px solid #0a4b78;padding-bottom:14px}
.brand{font-size:23px;font-weight:700;letter-spacing:.3px;color:#0a4b78}
.brand span{color:#0f172a;font-weight:600}
.tag{font-size:12.5px;color:#64748b;margin-top:5px;letter-spacing:.2px}
.date{font-size:13px;color:#334155;text-align:right;font-weight:600}
.date small{display:block;font-weight:400;color:#94a3b8;font-size:11.5px;margin-top:3px}
.sect{font-size:12px;font-weight:700;color:#0a4b78;letter-spacing:1.6px;
 margin:26px 0 12px;padding-bottom:6px;border-bottom:1px solid #dbe3ea}
.lead{background:#f7fafc;border:1px solid #dbe3ea;border-left:5px solid #0a4b78;
 border-radius:10px;padding:16px 20px 14px}
.lead ul{margin:0;padding-left:20px}
.lead li{font-size:14.2px;line-height:1.62;color:#1e293b;margin:0 0 9px}
.lead li:last-child{margin-bottom:0}
.lead li.scale{margin-top:13px;padding-top:12px;border-top:1px solid #e2e8f0;
 color:#0a4b78;font-size:13.4px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:13px;align-items:start}
.card{background:#fff;border:1px solid #dbe3ea;border-left:4px solid #0a4b78;border-radius:9px;
 padding:13px 15px 12px;box-shadow:0 1px 3px rgba(15,23,42,.05)}
.card.quiet{border-left-color:#cbd5e1;background:#fbfcfd}
.card .t{font-size:13.2px;font-weight:700;color:#0f172a;line-height:1.3;
 display:flex;gap:8px;align-items:baseline}
.num{display:inline-flex;align-items:center;justify-content:center;min-width:22px;height:19px;
 background:#0a4b78;color:#fff;border-radius:5px;font-size:11px;font-weight:700;flex:none;
 padding:0 5px}
.card.quiet .num{background:#94a3b8}
.card .b{font-size:12.4px;line-height:1.55;color:#475569;margin-top:8px}
.prow{display:grid;grid-template-columns:250px 190px 1fr;gap:14px;align-items:baseline;
 padding:9px 4px;border-bottom:1px solid #eef2f6}
.prow:last-child{border-bottom:none}
.prow .pn{font-size:12.6px;font-weight:600;color:#0f172a;display:flex;gap:7px;align-items:baseline}
.prow .tl{font-size:11.8px;font-weight:600;color:#0a4b78}
.prow .st{font-size:12.1px;color:#475569;line-height:1.45}
.pill{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:.4px;
 padding:2px 7px;border-radius:9px;margin-right:7px;vertical-align:1px;text-transform:uppercase}
.ok{background:#dcfce7;color:#15803d}.hold{background:#fef3c7;color:#a16207}
.idle{background:#f1f5f9;color:#64748b}.neut{background:#dbeafe;color:#0a4b78}
.blk{background:#fffbeb;border:1px solid #fde68a;border-left:5px solid #f59e0b;
 border-radius:10px;padding:14px 18px}
.blk .bt{font-size:13.2px;font-weight:700;color:#92400e}
.blk .bb{font-size:12.5px;color:#78350f;line-height:1.55;margin-top:6px}
.blk .item+.item{margin-top:12px;padding-top:12px;border-top:1px solid #fde68a}
footer{margin-top:26px;padding-top:12px;border-top:1px solid #dbe3ea;
 font-size:11px;color:#94a3b8;display:flex;justify-content:space-between}
"""


def render(day: str, sections: dict[str, list[str]], src: Path) -> str:
    sprint = parse_bullets(sections.get("TODAY SPRINT", []))
    projects = parse_items(sections.get("PROJECTS", []))
    process = parse_items(sections.get("PROCESS", []))
    blocked = sections.get("BLOCKED", [])

    # TODAY SPRINT -- the volume/scale line renders distinctly when present.
    lis = []
    for b in sprint:
        cls = ' class="scale"' if re.search(r"\bcommits?\b.*\bagents?\b", b, re.I) else ""
        lis.append(f"<li{cls}>{md_inline(b)}</li>")
    lead = f'<div class="lead"><ul>{"".join(lis)}</ul></div>' if lis else ""

    cards = []
    for it in projects:
        body = " ".join(it["body"]).strip()
        quiet = " quiet" if re.search(r"no movement|idle", body, re.I) else ""
        cards.append(
            f'<div class="card{quiet}"><div class="t"><span class="num">{html.escape(it["n"])}</span>'
            f'<span>{md_inline(it["name"])}</span></div>'
            f'<div class="b">{md_inline(body)}</div></div>'
        )
    proj = f'<div class="grid">{"".join(cards)}</div>' if cards else ""

    if not process:
        process = parse_process_table(sections.get("PROCESS", []))
    rows = []
    for it in process:
        tl, st = split_process(it["body"])
        rows.append(
            f'<div class="prow"><div class="pn"><span class="num">{html.escape(it["n"])}</span>'
            f'<span>{md_inline(it["name"])}</span></div>'
            f'<div class="tl">{md_inline(tl)}</div>'
            f'<div class="st"><span class="pill {status_class(st)}">'
            f'{PILL_LABEL[status_class(st)]}</span>'
            f'{md_inline(st)}</div></div>'
        )
    proc = "".join(rows)

    bitems, cur = [], None
    for raw in blocked:
        if _is_spacer(raw) or not raw.strip():
            continue
        c = _clean(raw)
        if re.match(r"^\s*[-*•]", raw) or cur is None:
            if cur:
                bitems.append(cur)
            cur = {"t": c, "b": []}
        else:
            cur["b"].append(c)
    if cur:
        bitems.append(cur)
    blk = "".join(
        f'<div class="item"><div class="bt">{md_inline(b["t"])}</div>'
        f'<div class="bb">{md_inline(" ".join(b["b"]))}</div></div>'
        for b in bitems
    )
    blocked_html = f'<div class="blk">{blk}</div>' if blk else ""

    pretty = dt.datetime.strptime(day, "%Y-%m-%d").strftime("%A, %B %-d, %Y") \
        if sys.platform != "win32" else dt.datetime.strptime(day, "%Y-%m-%d").strftime("%A, %B %d, %Y")
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%MZ")

    def sect(label: str, body: str) -> str:
        return f'<div class="sect">{label}</div>{body}' if body else ""

    return f"""<!doctype html><html><head><meta charset="utf-8">
<title>Opal Daily Operating Report - {day}</title><style>{CSS}</style></head><body>
<div class="page">
  <div class="hdr">
    <div><div class="brand">OPAL CAPITAL <span>/ Daily Operating Report</span></div>
    <div class="tag">Technology &amp; Platform Operations</div></div>
    <div class="date">{pretty}<small>rendered {stamp}</small></div>
  </div>
  {sect("TODAY SPRINT", lead)}
  {sect("PROJECTS", proj)}
  {sect("PROCESS", proc)}
  {sect("BLOCKED", blocked_html)}
  <footer><span>Source: {html.escape(src.name)}</span><span>Opal Capital - internal</span></footer>
</div></body></html>"""


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--date", default=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"))
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--src", type=Path, default=None)
    a = ap.parse_args(sys.argv[1:] if argv is None else argv)

    root = workspace_root()
    src = a.src or root / "org" / "sprints" / f"DAILY_SPRINT_{a.date}.md"
    if not src.is_file():
        print(f"render-sprint: no sprint file at {src}", file=sys.stderr)
        return 2

    out = a.out or root.parent / "Opal_Daily_Sprint.html"
    sections = split_sections(src.read_text(encoding="utf-8"))
    if not sections:
        print("render-sprint: no recognised sections (TODAY SPRINT/PROJECTS/PROCESS/BLOCKED)",
              file=sys.stderr)
        return 2
    out.write_text(render(a.date, sections, src), encoding="utf-8")
    counts = {k: len(v) for k, v in sections.items()}
    print(f"render-sprint: wrote {out}")
    print(f"  sections parsed: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
