"""
render_board_svg.py -- branded SVG project-board renderer for /registry-check.

Renders the HOT-project portfolio as a single Opal-branded SVG poster: a navy
header with the KO-white interlock logo, cluster sections, and one card per
project (status pill + WHAT line + NOW line + owner/last-commit footer).

Styling is pulled from the deck brand spec:
  deck_generation/brand_spec/brand.json  (palette: navy #163372, purple #5F3BE3,
  cool-grey #C4CBDB, charcoal #595959, etc.) + font Lato.
Logo: deck_generation/brand/.../Full Logo/KO/Opal-Capital-Logo-KO.svg (paths inlined).

  NOTE -- the per-project WHAT / NOW one-liners and the cluster grouping below are
  HAND-CURATED (the rich phrasing /registry-check's --json does not carry). This is
  a SNAPSHOT generator: to refresh the board, run `/registry-check` for the current
  status/owner/age, edit the `clusters` list, and re-run. Status/owner/age mirror
  registry-check's columns; the WHAT/NOW/cluster taxonomy is the curated layer.

Usage:
  python .claude/skills/registry-check/render_board_svg.py [OUTPUT.svg]
  (default OUTPUT: ./opal_project_board.svg)

Last curated snapshot: 2026-06-25 (22 HOT projects).
"""
from __future__ import annotations
import html
import sys

# ---- Opal brand palette (deck_generation/brand_spec/brand.json) ----
NAVY      = "#163372"   # opal_navy (primary)
MIDNIGHT  = "#0A1733"   # midnight_blue (dark accent)
COOLGREY  = "#C4CBDB"   # cool_grey (neutral / borders)
PURPLE    = "#5F3BE3"   # electric_purple (accent)
WHITE     = "#FFFFFF"
BLACK     = "#000000"
MEDBLUE   = "#174A7C"   # extended medium_blue
CHARCOAL  = "#595959"   # extended charcoal (secondary text)
TEAL      = "#63D6D4"   # extended teal_accent

FONT = "Lato, 'Helvetica Neue', Arial, sans-serif"

# KO (white) logo paths, viewBox 0 0 1301.87 575
LOGO_VIEWBOX = "0 0 1301.87 575"
LOGO_PATHS = '''<path fill="#fff" d="M296.62,145.9h-2.52v62.41c0,74.93-14.18,90.24-82.9,90.24H118.11c-12.67,0-23.44-.5-32.67-1.82-40.75-5.83-50.18-27.3-50.18-88.42v-72.08c0-72.66,14.75-88.61,82.85-88.61h93.09c59.73,0,78.46,12.28,82.13,64.24h3.86c11.51,0,21.95,.58,31.4,1.65-4.13-68.29-29.05-99.93-116.84-99.93H117.54C19.89,13.59,0,52.76,0,137.93v68.67c0,77.07,15.45,116.24,86.21,124.35,9.43,1.13,19.81,1.63,31.33,1.63h94.22c97.65,0,117.54-38.6,117.54-125.98v-58.79c-9.19-1.34-20-1.92-32.67-1.92Z"/><path fill="#fff" d="M811.55,236.15v68.69c0,87.42-19.87,126.02-117.51,126.02h-79.47c-59.6,0-85.72-14.76-96.51-47.12v150.44c0,5.11-3.4,8.51-8.51,8.51h-18.16c-5.11,0-8.51-3.4-8.51-8.51V120.35c0-5.11,3.4-8.51,8.51-8.51h18.16c5.11,0,8.51,3.4,8.51,8.51v38.6c10.79-31.8,36.91-47.12,96.51-47.12h79.47c97.64,0,117.51,39.17,117.51,124.32Zm-35.19-1.7c0-72.66-14.76-88.56-82.32-88.56h-93.1c-56.76,0-82.88,12.49-82.88,88.56v72.1c0,78.34,25.56,90.26,82.88,90.26h93.1c68.13,0,82.32-15.33,82.32-90.26v-72.1Z"/><path fill="#fff" d="M866.26,344.58c0-59.04,24.4-85.15,101.61-93.66l158.95-17.61c13.63-1.7,18.16-8.51,18.16-19.3,0-51.09-11.35-68.12-74.94-68.12h-169.73c-5.11,0-8.51-3.4-8.51-8.51v-17.03c0-5.11,3.4-8.51,8.51-8.51h170.3c81.74,0,109.56,28.95,109.56,93.66v216.86c0,5.11-3.4,8.51-8.51,8.51h-18.17c-5.11,0-8.51-3.4-8.51-8.51v-47.68c-13.05,37.46-34.62,56.2-103.88,56.2h-55.63c-76.07,0-119.21-27.82-119.21-86.29Zm183.35,52.8c72.1,0,95.37-26.11,95.37-95.37v-38.04l-172.57,19.3c-58.47,6.24-70.97,21.57-70.97,59.61,0,34.62,24.41,54.49,84.02,54.49h64.15Z"/><path fill="#fff" d="M1266.67,422.35V8.51c0-5.11,3.41-8.51,8.51-8.51h18.17c5.11,0,8.51,3.4,8.51,8.51V422.35c0,5.11-3.4,8.51-8.51,8.51h-18.17c-5.1,0-8.51-3.4-8.51-8.51Z"/><path fill="#fff" d="M682.88,556.65c-2.22,10.62-10.2,18.35-24.43,18.35-18.02,0-26.49-12.75-26.49-28.88s8.8-29.45,27.07-29.45c15.14,0,22.46,8.8,23.86,18.34h-12.26c-1.24-4.44-4.28-8.8-12.01-8.8-10.12,0-13.99,9.13-13.99,19.5,0,9.54,3.37,19.67,14.32,19.67,8.06,0,10.53-5.35,11.6-8.73h12.34Z"/><path fill="#fff" d="M749.02,561.09l-4.36,13.08h-12.09l19.26-56.68h15.38l20.16,56.68h-12.92l-4.69-13.08h-20.73Zm18.1-10.04c-4.04-12.01-6.58-19.67-7.98-24.76h-.08c-1.4,5.59-4.2,14.48-7.4,24.76h15.47Z"/><path fill="#fff" d="M843.96,517.49h23.45c12.09,0,20.24,6.74,20.24,17.52,0,12.34-9.3,18.02-20.49,18.02h-10.95v21.14h-12.26v-56.68Zm12.26,25.75h9.38c5.67,0,9.71-2.22,9.71-7.98s-4.28-8.06-9.46-8.06h-9.63v16.04Z"/><path fill="#fff" d="M958.48,517.49v56.68h-12.26v-56.68h12.26Z"/><path fill="#fff" d="M1033.51,527.53h-17.28v-10.04h46.73v10.04h-17.2v46.65h-12.26v-46.65Z"/><path fill="#fff" d="M1124.34,561.09l-4.36,13.08h-12.09l19.26-56.68h15.38l20.16,56.68h-12.92l-4.68-13.08h-20.73Zm18.1-10.04c-4.04-12.01-6.58-19.67-7.98-24.76h-.08c-1.4,5.59-4.2,14.48-7.4,24.76h15.47Z"/><path fill="#fff" d="M1219.28,517.49h12.26v46.65h28.31l-1.4,10.04h-39.16v-56.68Z"/><path fill="#fff" d="M329.28,137.93v9.87c-9.18-1.33-20-1.9-32.65-1.9h-2.53v-9.68c0-8.99-.25-17.02-.76-24.36h3.86c11.52,0,21.96,.57,31.39,1.65,.51,7.66,.7,15.82,.7,24.43Z"/><path fill="#fff" d="M410.37,182.19c-.14-.74-.31-1.49-.48-2.21-.67-3.05-1.42-5.97-2.25-8.8-4.32-14.34-10.94-26-20.72-35.07-13.07-12.06-31.81-19.53-58.31-22.6-9.45-1.08-19.88-1.65-31.4-1.65h-94.22c-48.84,0-78.2,9.79-95.4,30.22-17.17,20.44-22.14,51.5-22.14,94.08v60.57c9.23,1.32,20,1.82,32.67,1.82h2.59v-64.12c0-72.63,14.73-88.53,82.83-88.53h93.09c12.67,0,23.48,.58,32.67,1.92,5.47,.79,10.36,1.9,14.78,3.33,28.11,9.14,35.45,32.14,35.45,83.28v72.08c0,74.93-14.18,90.31-82.9,90.31h-93.09c-59.8,0-78.27-11.63-82.01-64.24h-3.98c-11.51,0-21.9-.5-31.33-1.63,4.29,69.03,29.43,99.93,116.77,99.93h94.22c97.65,0,117.51-38.62,117.51-126.07v-68.65c0-20.68-1.18-38.62-4.34-53.97Z"/>'''

# ---- status -> pill color ----
STATUS_COLOR = {
    "active":         PURPLE,
    "scoping":        MEDBLUE,
    "build-complete": TEAL,
    "superseded":     COOLGREY,
}

# ---- data ----
clusters = [
    ("GRAPH-SSOT EXPANSION", "NFRA_EXPAND macro - Andrew-direct, scoped today", [
        ("NFRA_EXPAND", "scoping", "1h", "CTO", "",
         "Graph = single source of truth for ALL Opal properties, then ONE global heat-map analytic",
         "PRD complete; 2 Andrew rulings folded (access-topology = security, single AWS Nessie)"),
        ("EXPAND_MSCLOUD", "scoping", "1h", "CTO", "Strand A",
         "Ingest SharePoint + OneDrive into the graph (Outlook + all personal comms OFF-graph)",
         "Scoped; hard scope boundary + structure-not-content guardrail set"),
        ("EXPAND_AUTHEDGE", "scoping", "1h", "CTO", "Strand B",
         "Model the CloudFront -> Lambda@Edge auth binding as a typed graph edge (F4b)",
         "Scoped; auth-edge YES, F4a prefix-grain explicitly dropped (grain explosion)"),
        ("HEATMAP_OBJECT", "scoping", "1h", "CTO", "Strand C",
         "File-hygiene heat-map -> archive/delete RECOMMENDATIONS (advisory-only, never auto-delete)",
         "Re-homed under NFRA_EXPAND; the buildable-now (repo-file) half"),
        ("HEATMAP_PROCESS", "scoping", "1h", "CTO", "DUP",
         "MCP-traffic workflow-mining schema (L0-L5) - same domain as NFRA_WRKFLW",
         "Flagged for supersede -> fold NFRA_WRKFLW in as the process strand"),
        ("NFRA_HEATMAP", "superseded", "1h", "-", "",
         "Heat-map analytics macro - absorbed into NFRA_EXPAND as Strand C today",
         "Superseded -> NFRA_EXPAND (correct consolidation)"),
    ]),
    ("ETFS - partner ETF-ownership tracking", "", [
        ("ETFS_SETUP", "active", "2h", "AE", "",
         "Infra: opal-data-etfs bucket + per-partner ETF-ownership producers",
         "~75%; Andrew 2-day decisive wrap; W2 49F producer live (bd-v2.39.0)"),
        ("ETFS_AVGCAP", "active", "0h", "DS", "",
         "Monthly AVERAGE partner ownership value (the marquis metric)",
         "Scope expanded ingestion -> presentation; date-conforming-slice fix"),
        ("ETFS_CANON", "scoping", "0h", "AE", "",
         "Canonical output: DynamoDB daily rows + monthly marquis artifact",
         "CTO design-gate GO (DynamoDB + fan-in); 0.5.0 Dynamo skeleton landed"),
    ]),
    ("CUSTODIAN DATA - BD / Schwab / Cottonwood + the platform", "", [
        ("ADVI_BDAPIMIG", "active", "0h", "AE", "",
         "Migrate 49F Black Diamond scrape -> DataMining REST API (resolves the 06-19 MFA P0)",
         "P0 RECOVERED; durable auto-auth building (proxy-secret CVO Rule-22 fix)"),
        ("ADVI_COTETL", "active", "1.3d", "DS", "",
         "Onboard Cottonwood onto the Black Diamond medallion pipeline",
         "P0 complete; TO-status reconcile (DATEMODE-A / CHAINFIX)"),
        ("DATA_PLATFORM", "active", "3h", "AE", "",
         "Proprietary custodian data platform to replace BD + Orion",
         "Phase-1 audit done; DC2 eclipse-crawl harness applied (06-26 fire)"),
        ("DATA_ANALYTICS", "active", "0h", "DS", "",
         "Schwab-raw-native gold clean-rebuild (PARALLEL R&D, NOT a cutover)",
         "fact_* builds; missing-raw-file -> SKIP-not-ERROR fix"),
    ]),
    ("COMP-TOOL / GRAPH PLATFORM", "", [
        ("NFRA_COMPRAIL", "active", "6h", "CVO", "",
         "comp-which-first search + inspection rail, hard-gated",
         "Gate-1 built + green; enforce-flip 06-26 14:00Z; TO-5 telemetry seed"),
        ("NFRA_DEBTSCAN", "active", "1h", "AE", "",
         "Graph-driven estate debt / dead-path / canon scanning",
         "TO-D3 canon-scorer 4/4 scored + AC4 CVO-verified"),
        ("NFRA_TSGRAPH", "active", "6h", "COO", "",
         "Frontend TypeScript semantic graph",
         "P1 cutover signed; P2 reroute (AE off-peak crawl-block resolved)"),
        ("NFRA_COMPAWS", "active", "22h", "COO", "",
         "comp-aws full AWS resource graph",
         "IAM-conditions charter (fix comp-iam condition-blindness)"),
        ("NFRA_COSTAWS", "active", "2h", "AE", "",
         "Cloud cost governance (standing program)",
         "Section-7 permanent recurring cost-model line authored"),
    ]),
    ("M365 / WORKFLOW", "", [
        ("NFRA_OPLMCP", "build-complete", "23h", "COO", "",
         "Per-user M365 MCP gateway for Claude (delegated Graph API)",
         "Build complete; .08 read-only Teams-read tools charter"),
        ("NFRA_WRKFLW", "active", "1.2d", "COO", "DUP",
         "Workflow-mining over OPLMCP gateway traffic",
         "Same domain as HEATMAP_PROCESS -> to fold into NFRA_EXPAND Strand C"),
    ]),
    ("OTHER", "", [
        ("SCTY", "active", "1h", "COO", "",
         "Security macro: diligence + own-attack-surface program",
         "Drive cycle-18; TO-D3 security-scanner AC4 CVO-verified"),
        ("ASTN_WSJFT", "active", "7h", "CTO", "",
         "CEO daily WSJ & FT news digest (Austin)",
         "LIVE v0.3.0 - schedules ENABLED (go-live), GATE-3 cleared"),
    ]),
]

# ---- layout constants ----
W       = 1740
M       = 48
COLS    = 3
GAP     = 28
CARD_W  = (W - 2*M - (COLS-1)*GAP) // COLS  # 535
PAD     = 18

HEADER_H = 132
SEC_HDR_H = 40
SEC_GAP_TOP = 30
ROW_GAP = 24

# crude text-wrap by estimated width
def wrap(text, font_px, max_px, weight_factor=0.50):
    avg = font_px * weight_factor
    max_chars = max(6, int(max_px / avg))
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= max_chars:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def esc(s):
    return html.escape(s, quote=True)

# pre-compute card heights
inner_w = CARD_W - 2*PAD
WHAT_FS = 14
NOW_FS  = 14
def card_lines(p):
    code, status, age, owner, tag, what, now = p
    wl = wrap(what, WHAT_FS, inner_w)
    nl = wrap(now, NOW_FS, inner_w)
    return wl, nl

def card_height(p):
    wl, nl = card_lines(p)
    h = PAD                 # top
    h += 26                 # code row
    h += 14                 # label WHAT
    h += len(wl)*19
    h += 12                 # label NOW
    h += len(nl)*19
    h += 8 + 16             # footer owner/age
    h += PAD
    return h

# ---- build svg ----
parts = []
# compute total height first (two-pass)
def layout(y_start, emit):
    y = y_start
    for title, sub, projs in clusters:
        y += SEC_GAP_TOP
        if emit:
            # section header bar
            parts.append(f'<rect x="{M}" y="{y}" width="{W-2*M}" height="{SEC_HDR_H}" rx="6" fill="{NAVY}"/>')
            parts.append(f'<rect x="{M}" y="{y}" width="6" height="{SEC_HDR_H}" rx="3" fill="{PURPLE}"/>')
            parts.append(f'<text x="{M+20}" y="{y+SEC_HDR_H/2+6}" font-family="{FONT}" font-size="19" font-weight="700" fill="{WHITE}" letter-spacing="0.5">{esc(title)}</text>')
            if sub:
                parts.append(f'<text x="{W-M-16}" y="{y+SEC_HDR_H/2+5}" text-anchor="end" font-family="{FONT}" font-size="12.5" font-weight="300" fill="{COOLGREY}">{esc(sub)}</text>')
        y += SEC_HDR_H + 18
        # rows of COLS
        i = 0
        while i < len(projs):
            row = projs[i:i+COLS]
            heights = [card_height(p) for p in row]
            rh = max(heights)
            for ci, p in enumerate(row):
                x = M + ci*(CARD_W+GAP)
                if emit:
                    emit_card(x, y, rh, p)
            y += rh + ROW_GAP
            i += COLS
        y -= ROW_GAP
    return y

def emit_card(x, y, h, p):
    code, status, age, owner, tag, what, now = p
    wl, nl = card_lines(p)
    sc = STATUS_COLOR.get(status, MEDBLUE)
    superseded = (status == "superseded")
    body_fill = "#F4F6FB" if superseded else WHITE
    accent = sc if status != "scoping" else PURPLE
    # card
    parts.append(f'<rect x="{x}" y="{y}" width="{CARD_W}" height="{h}" rx="10" fill="{body_fill}" stroke="{COOLGREY}" stroke-width="1.2"/>')
    parts.append(f'<rect x="{x}" y="{y}" width="5" height="{h}" rx="2.5" fill="{accent}"/>')
    cx = x + PAD + 6
    cy = y + PAD + 16
    # code
    code_fill = CHARCOAL if superseded else NAVY
    parts.append(f'<text x="{cx}" y="{cy}" font-family="{FONT}" font-size="18" font-weight="700" fill="{code_fill}" letter-spacing="0.3">{esc(code)}</text>')
    # status pill (top-right)
    pill_txt = status.upper()
    pill_w = 9 + len(pill_txt)*7.4
    pill_x = x + CARD_W - PAD - pill_w
    pill_y = y + PAD + 1
    pill_text_fill = NAVY if status in ("build-complete","superseded") else WHITE
    parts.append(f'<rect x="{pill_x}" y="{pill_y}" width="{pill_w}" height="20" rx="10" fill="{sc}"/>')
    parts.append(f'<text x="{pill_x+pill_w/2}" y="{pill_y+14}" text-anchor="middle" font-family="{FONT}" font-size="10.5" font-weight="700" fill="{pill_text_fill}" letter-spacing="0.4">{esc(pill_txt)}</text>')
    yy = cy + 22
    # optional tag (Strand X / DUP)
    if tag:
        tag_fill = "#C0392B" if tag == "DUP" else PURPLE
        parts.append(f'<text x="{cx}" y="{yy}" font-family="{FONT}" font-size="11.5" font-weight="700" fill="{tag_fill}" letter-spacing="0.6">{esc(tag)}</text>')
        yy += 6
    # WHAT
    parts.append(f'<text x="{cx}" y="{yy+8}" font-family="{FONT}" font-size="10" font-weight="700" fill="{PURPLE}" letter-spacing="1.2">WHAT</text>')
    ty = yy + 8 + 17
    for ln in wl:
        parts.append(f'<text x="{cx}" y="{ty}" font-family="{FONT}" font-size="{WHAT_FS}" font-weight="400" fill="{BLACK if not superseded else CHARCOAL}">{esc(ln)}</text>')
        ty += 19
    # NOW
    ty += 2
    parts.append(f'<text x="{cx}" y="{ty+8}" font-family="{FONT}" font-size="10" font-weight="700" fill="{MEDBLUE}" letter-spacing="1.2">NOW</text>')
    ty = ty + 8 + 17
    for ln in nl:
        parts.append(f'<text x="{cx}" y="{ty}" font-family="{FONT}" font-size="{NOW_FS}" font-weight="400" fill="{CHARCOAL}">{esc(ln)}</text>')
        ty += 19
    # footer: owner + age (bottom-right)
    foot = f"{owner}  -  last commit {age} ago" if owner != "-" else f"last touch {age} ago"
    parts.append(f'<text x="{x+CARD_W-PAD}" y="{y+h-PAD+2}" text-anchor="end" font-family="{FONT}" font-size="11" font-weight="600" fill="{COOLGREY if superseded else MEDBLUE}">{esc(foot)}</text>')

# pass 1: measure
total_h = layout(HEADER_H, emit=False)
total_h += 70  # footer band

# now actually emit (reset parts, header first)
parts = []
parts.append(f'<rect x="0" y="0" width="{W}" height="{total_h}" fill="{WHITE}"/>')
# header band
parts.append(f'<rect x="0" y="0" width="{W}" height="{HEADER_H}" fill="{NAVY}"/>')
parts.append(f'<rect x="0" y="{HEADER_H-5}" width="{W}" height="5" fill="{PURPLE}"/>')
# logo (KO white) top-left, height ~46
logo_h = 50
logo_w = logo_h * (1301.87/575)
parts.append(f'<svg x="{M}" y="{(HEADER_H-logo_h)/2 - 6}" width="{logo_w}" height="{logo_h}" viewBox="{LOGO_VIEWBOX}" preserveAspectRatio="xMinYMid meet">{LOGO_PATHS}</svg>')
# title block (right of logo)
tx = M + logo_w + 40
parts.append(f'<text x="{tx}" y="{HEADER_H/2 - 8}" font-family="{FONT}" font-size="30" font-weight="700" fill="{WHITE}" letter-spacing="0.5">Opal Project Board</text>')
parts.append(f'<text x="{tx}" y="{HEADER_H/2 + 20}" font-family="{FONT}" font-size="14.5" font-weight="300" fill="{COOLGREY}">22 HOT projects (worked &lt; 72h) - what each is &amp; most recent activity</text>')
# date / meta top-right
parts.append(f'<text x="{W-M}" y="{HEADER_H/2 - 8}" text-anchor="end" font-family="{FONT}" font-size="15" font-weight="600" fill="{WHITE}">2026-06-25</text>')
parts.append(f'<text x="{W-M}" y="{HEADER_H/2 + 16}" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="300" fill="{COOLGREY}">source: /registry-check + ascribed commits  |  0 malformed</text>')

# body
layout(HEADER_H, emit=True)

# footer band
fy = total_h - 70
parts.append(f'<rect x="0" y="{fy}" width="{W}" height="70" fill="{MIDNIGHT}"/>')
parts.append(f'<rect x="0" y="{fy}" width="{W}" height="4" fill="{PURPLE}"/>')
# legend
lx = M
ly = fy + 30
legend = [("active", PURPLE), ("scoping", MEDBLUE), ("build-complete", TEAL), ("superseded", COOLGREY)]
parts.append(f'<text x="{lx}" y="{ly+5}" font-family="{FONT}" font-size="12" font-weight="700" fill="{COOLGREY}" letter-spacing="0.8">STATUS</text>')
lx += 70
for name, col in legend:
    parts.append(f'<rect x="{lx}" y="{ly-9}" width="14" height="14" rx="3" fill="{col}"/>')
    parts.append(f'<text x="{lx+20}" y="{ly+3}" font-family="{FONT}" font-size="12.5" font-weight="400" fill="{WHITE}">{esc(name)}</text>')
    lx += 40 + len(name)*8
# footnote right
parts.append(f'<text x="{W-M}" y="{ly+3}" text-anchor="end" font-family="{FONT}" font-size="12" font-weight="300" fill="{COOLGREY}">DUP = HEATMAP_PROCESS &amp; NFRA_WRKFLW overlap (reconcile pending)  -  + 14 cold projects via /registry-check -all</text>')

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{total_h}" '
       f'viewBox="0 0 {W} {total_h}" font-family="{FONT}">\n' + "\n".join(parts) + "\n</svg>\n")

out = sys.argv[1] if len(sys.argv) > 1 else "opal_project_board.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", out, "  dims", W, "x", total_h)
