# DSGN_RBNDV2 -- surprise channel, INVESTIGATION v1 (laptop fabric). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "DSGN_RBNDV2-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~RB",
    "surfaced_at": "2026-10-15T03:59:17Z",
    "one_line": "Turning every panel variant white (C-PANEL) makes light-on-dark text idioms inside panel bodies near-invisible: 140 page files under portal/src/pages carry text-white, and the portal's own law says chart/mixed panels stay dark BECAUSE those idioms depend on it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- disarmed when round 1's token cell lands the scoped ink-inversion rule and /market renders readable in the COO's close run; the walk (FWD-5, round 3) re-measures the rest.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/CLAUDE.md 'Known divergence': Panel variant chart/mixed resolve to the band and --bg-header/--bg-medium/--bg-card alias it because 4,887 light-on-dark idioms in src/pages/ depend on a dark container (rows DSGN_REBRND-W1-S9, W2-S5)",
        "portal/src/ui/components/panels/Panel.tsx:60-78 variant map: heatmap and nested are already white with dark text, chart and mixed are band-valued",
        "native Grep at the laptop portal checkout @97c66c93 (origin DEV is ad7c100b, not yet fetched): files under src/pages matching text-white 140, bg-white/ 96, border-white/ 92, of 397 page .tsx files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-PANEL: the panel primitives render a white surface with a 1px #C4CBDB border and 'no page file is edited for FWD-3's panel half'; FWD-3 ACCEPT: panels are white; FWD-5 expects only a FAINT red/green/signal colour on the new ground.",
    "world_is": "Page bodies inside chart/mixed panels were written for a dark ground and use text-white idioms; on a white panel those read invisible (white on white), a worse class than the 'faint' colour FWD-5 anticipates, and a page-file edit is not permitted for the panel half. No action taken beyond cutting round 1 so the token cell carries one scoped rule (inside the light panel, text-white/N reads navy ink) at the token seam; the walk re-measures.",
    "notes": "Ruled inside the COO's own decomposition (/canonical-drive obligation 7): no ENDPOINT change, no page edit. The counts are the laptop checkout's vintage; the first-issuance fetch to DEV's tip re-measures them. Not blocking the decomposition draft."
  },
  {
    "id": "DSGN_RBNDV2-W1-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~1",
    "surfaced_at": "2026-10-15T05:02:13Z",
    "one_line": "The theme header names a regeneration that does not reproduce the committed design/themes/opal-capital.css: the repo generator at ad7c100b writes a different file, so the canvas was set from its rendering, not by a full regeneration.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- reconcile the generator with the committed theme (or retire the header's claim) before any design build rewrites design/themes/opal-capital.css.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/design/themes/opal-capital.css@ad7c100b header: 'Generated from design/brands/opal-capital.json by that directory's own resolveBrandTheme(brand, 'light') + generateCSSVariables, then pasted here'; the same file's header names 'npm run design:build'",
        "portal/package.json@ad7c100b has no design:build script (grep for 'design' in package.json returned no line); the generator is design/tokens/generate-themes.ts, run by hand",
        "scratch run of generate-themes.ts (processBrand) on a copy of portal/design at the new JSON: writes opal-capital.dark.css, opal-capital.light.css, opal-capital.tailwind.ts and rewrites the combined opal-capital.css; the committed file differs in structure (no comment blocks, integer HSL, no 30-token light semantic block at the same names, status and data blocks absent) and the generated canvas reads 240 44.83% 94.31%"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-t-1 (a): edit the brand JSON, regenerate the theme with the repo's own generator, do not hand-edit the generated file alone, so --palette-canvas resolves to rgb(234,234,247).",
    "world_is": "The generator cannot regenerate the committed theme file: a full run would rewrite it and create three files outside the cell's grant. The cell therefore set the four canvas-carrying lines (--palette-canvas, --semantic-background-default, -mediumAlt, -hoverLight) to the generator's rendering of the new canvas (240 44.83% 94.31%) and left every other line as committed.",
    "notes": "No token other than the canvas changed. The two-decimal canvas HSL is deliberate: integer HSL would render the canvas at a channel one step off 234. Whoever owns the theme decides whether the generator or the committed file is the source of truth."
  },
  {
    "id": "DSGN_RBNDV2-W1-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~1",
    "surfaced_at": "2026-10-15T05:02:13Z",
    "one_line": "The one legibility rule keys on the panel scope and the class text alone, so a text-white element with a solid coloured fill inside a light panel also takes navy-black ink, unmeasured.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- the FWD-5 walk (round 3) measures every text-white on a solid fill inside a light panel and repairs it at the page cell that owns it.",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "portal/src/index.css (RB-t-1 block after the .dark-band state rules): [data-panel-surface=\"light\"] .text-white and [data-panel-surface=\"light\"] [class*=\"text-white/\"] set color to var(--rb-ink) with no fill test",
        "by construction, not rendered: no page was screenshotted in this cell (the cell's bounds allow none)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-t-1 (c): inside the light-panel scope, text-white and text-white/N resolve to var(--rb-ink); bg-white/N resolves to no fill; nothing outside the scope changes.",
    "world_is": "A light-on-dark idiom that sits on a solid fill (for example white text on an indigo or navy control inside a panel body) is recoloured to navy-black ink on that fill; the scope cannot tell it from a light-on-dark idiom on the white panel. Its contrast on the fill is not measured here.",
    "notes": "The rule is correct for the case the cell names; the solid-fill case is what the walk must measure. Raised so the walk is not surprised by it."
  },
  {
    "id": "DSGN_RBNDV2-W1-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~1",
    "surfaced_at": "2026-10-15T05:02:13Z",
    "one_line": "Comments that name the canvas as #F4F6FA and quote contrast ratios measured on it still stand in index.css and the theme header after the canvas moved to #EAEAF7; the ratios were not re-measured.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/index.css@ad7c100b lines 152 and 154 (ramp 2.17:1 and 1.49:1 on the canvas and the band), 162 and 166 (3.29:1 and 11.71:1 on the canvas), 396 and 397 (1.20 and 1.11 from white/canvas, 1.39 and 1.28), read by Grep",
        "portal/design/themes/opal-capital.css@ad7c100b line 10, the RB-s-1 header, still names canvas #F4F6FA as a corrected value"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-t-1 (a): update only the index.css comments that sit inside a block this cell edits and that call the canvas #F4F6FA.",
    "world_is": "The hex mentions inside the edited :root block now say #EAEAF7. The contrast figures beside them, and the theme header's historical RB-s-1 line, were left as written because they describe a different canvas and this cell does not re-measure.",
    "notes": "Stale figures inside a comment read as current. A re-measure at the walk, or a comment rewrite by the owner of those ramp tokens, retires this row."
  },
  {
    "id": "DSGN_RBNDV2-W1-S4",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~1",
    "surfaced_at": "2026-10-15T05:02:13Z",
    "one_line": "The task order names the portal worktree as based on branch feature/dsgn-rbndv2-light; the live portal checkout is on wk-DSGN_RBNDV2-1-portal at the same commit ad7c100b.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal rev-parse --abbrev-ref HEAD returned wk-DSGN_RBNDV2-1-portal; git -C portal rev-parse --short HEAD returned ad7c100b",
        "the order's Environment line names feature/dsgn-rbndv2-light at ad7c100b5c"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Environment: the portal worktree is based on the feature branch feature/dsgn-rbndv2-light at ad7c100b5c.",
    "world_is": "The commit matches (ad7c100b, the same object). The branch name differs. The work was committed on wk-DSGN_RBNDV2-1-portal, the worker's own branch, as the bounds require.",
    "notes": "Recorded so the merge owner maps the worker branch onto the feature branch by commit, not by name."
  },
  {
    "id": "DSGN_RBNDV2-W2-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~2",
    "surfaced_at": "2026-10-15T05:11:26Z",
    "one_line": "The RB1S-AC2 difference control cannot report four of four: the base App.tsx declares SidebarLink as a function and has no const form, so the control reports three of four markers present.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show ad7c100b5c:src/App.tsx line 165 reads 'function SidebarLink({' and no line of the base declares 'const SidebarLink' (native Grep over the base text)",
        "portal/src/ui/components/sidebar/__tests__/dsgn-rbndv2/rb-1-s.app-seam.test.ts@14b719cc base-control output: {\"NAV_SECTIONS\":true,\"function SidebarLink\":true,\"const SidebarLink\":false,\"<aside\":true}"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB1S-AC2 (task order DSGN_RBNDV2.TO-RV-s-1): the same text checks run against git show ad7c100b5c:src/App.tsx report all four present, proving the test can fail.",
    "world_is": "The base carries NAV_SECTIONS, function SidebarLink and <aside, and no const SidebarLink. The test keeps the four absence arms on the current App.tsx (all hold) and asserts the three base markers present; the const marker is recorded as absent in the base output, not forced to present. The verdict was not weakened to pass.",
    "notes": "Raised for the COO's ruling on whether the control should name the function form."
  },
  {
    "id": "DSGN_RBNDV2-W2-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~2",
    "surfaced_at": "2026-10-15T05:11:26Z",
    "one_line": "The collapsed-rail logo in the base is opal-icon-white.svg, which is invisible on the light sidebar ground; RV-s-1 renders opal-icon-black.svg for the collapsed icon.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show ad7c100b5c:src/App.tsx line 315 reads src=\"/logos/opal-icon-white.svg\" for the collapsed toggle icon",
        "portal/public/logos/ at ad7c100b5c ships opal-icon-black.svg, opal-logo-black.svg, opal-icon-color.svg and opal-logo-color.svg beside the white pair"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order RV-s-1: the COLLAPSED 48px icon rail keeps the current icons and its behaviour, on the same ground and border.",
    "world_is": "The current collapsed logo is white, so on the lavender ground it does not render. RV-s-1 switches only that asset to the existing black icon; the expanded wordmark is text per the A-light fixture. Whether navy ink or black is the right ink for the icon is a judgment for Andrew's read at the drain (RB1S-AC3).",
    "notes": "No new asset was added; the change is the src string of one image."
  },
  {
    "id": "DSGN_RBNDV2-W2-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~2",
    "surfaced_at": "2026-10-15T05:11:26Z",
    "one_line": "The account-menu popup in App.tsx keeps its dark styling (bg-header, white/10 border, text-white/80) beside the light sidebar, because the order names the App.tsx edit as the extraction only.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- disarm when the account-menu popup is restyled to the light ground (in round 1's ink pass or a follow-on cell) and reads at the drain.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/App.tsx@14b719cc user-menu popup div: className bg-[hsl(var(--bg-header))] border border-white/10 rounded-[4px], and its two buttons use text-white/80 hover:bg-white/10 hover:text-white",
        "portal/src/App.tsx@14b719cc still computes the popup width from 14rem (w-56) and left 3.5rem/0.75rem, unchanged from the base"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Order RV-s-1: 'This is the only edit to App.tsx' (the extraction); the foot is restyled to the light board; the popup is not named.",
    "world_is": "The popup opens from the restyled light foot and renders dark with white/80 text. If the token cell repoints --bg-header light, its text becomes near-invisible, the same class of defect as DSGN_RBNDV2-S1. The popup's width calc still refers to the old w-56 sidebar width (14rem minus padding); it is not moved by this cell.",
    "notes": "Left in place deliberately: restyling it would be a second App.tsx edit the order does not grant."
  },
  {
    "id": "DSGN_RBNDV2-W3-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~3",
    "surfaced_at": "2026-10-15T04:59:14Z",
    "one_line": "The A-light panel header has a number slot ('01' in --rb-quiet, before the eyebrow title) that no caller can fill: PanelHeader's exported prop API is frozen by C-PANEL, and no prop carries a number.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/ui/components/panels/PanelHeader.tsx@ad7c100b5c lines 17-44: PanelHeaderProps = title, subtitle, timestamp, source, frequency, helpText, leftActions, actions, className; no number prop",
        "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-p-1.panel-primitives.md: 'change NO prop: every exported prop interface ... stays exactly as it is'",
        "org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/A_LIGHT_FIXTURE.md:21 and :39 (number '01' in quiet; section.pnl > .pnl-h (h2.pnl-t > span.num + span.eyebrow))"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-p-1 and decomposition row RV-p-1 (DSGN_RBNDV2_DECOMP.md @b475e9badc) say PanelHeader renders 'an optional number in --rb-quiet' before the title, and that the prop API of every primitive is UNCHANGED. Criterion RB1P-AC1 renders PanelHeader 'with a title, a number and one action'.",
    "world_is": "No PanelHeader prop can carry a number, so the number slot is unreachable. The primitive is built without it, and RB1P-AC1's test renders a title and an action only; no arm asserts a number. Adding an optional prop would change the exported interface, which the order forbids. A ruling is needed: an additive optional prop, or the number dropped from the fixture.",
    "notes": "Not resolved by the worker. Raised for the COO's ruling; RB1P-AC1 otherwise holds (its arms do not name a number)."
  },
  {
    "id": "DSGN_RBNDV2-W3-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~3",
    "surfaced_at": "2026-10-15T04:59:14Z",
    "one_line": "PanelFooter's ground prop still defaults to 'band', the name of the navy footer strip that C-PANEL removes; 'band' and 'light' now paint the same A-light caption, so the default's name describes a band that no longer exists.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/ui/components/panels/PanelFooter.tsx@ad7c100b5c line 44 (ground?: 'band' | 'light') and line 93 (ground = 'band' default) before the edit that removed the navy strip",
        "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-p-1.panel-primitives.md: 'every default ... stays exactly as it is' and 'no navy footer strip'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-p-1 requires every default to stay exactly as it is (the ground default is 'band') and requires PanelFooter to render no navy footer strip.",
    "world_is": "The ground default stays 'band' and the prop stays accepted, but the value no longer changes the paint: both ground values render the A-light caption (the navy strip is gone). The worker kept the value and dropped the destructuring; the prop's name is stale.",
    "notes": "Not resolved by the worker. Raised for the COO's ruling on whether the value is renamed in a later round (which would move call sites) or kept as a documented no-op."
  },
  {
    "id": "DSGN_RBNDV2-W3-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~3",
    "surfaced_at": "2026-10-15T04:59:14Z",
    "one_line": "SectionCard's accent edge is written as a border-left colour on a zero-width div, so at the base it paints nothing; it predates this cell and the cell did not change it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/ui/components/panels/SectionCard.tsx@ad7c100b5c lines 28-34 (ACCENT_MAP uses border-l-[hsl(var(--...))]) and lines 51-57 (accent div: absolute left-0 top-0 bottom-0 w-1 with no border-l width class)",
        "read from the class list only; not rendered in a browser"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-p-1 names SectionCard among the primitives to render the A-light surface and hairline; it does not name the accent.",
    "world_is": "The accent div sets a border colour with no border width, so it has no visible paint at the base; the cell removed only the rounded-l-lg class from that div and left the accent logic as it was.",
    "notes": "Observed while editing. Not fixed: changing the accent mechanism is outside the cell's stated change. Raised for the COO."
  },
  {
    "id": "DSGN_RBNDV2-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~RB",
    "surfaced_at": "2026-10-15T05:57:00Z",
    "one_line": "On /market, inside the now-white panels, the period chips (1D, WTD, 90D, 1Y) read near-invisible: the shared Segmented control's band ground paints the active chip in --palette-white and the idle chips in --palette-mediumGray, tokens the legibility rule (class-text based) does not reach.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- disarmed when the scoped token remap (addendum cell RV-r-1) lands and the chips read in the COO's close run on /market.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/ui/components/Controls.tsx on feature/dsgn-rbndv2-light @d2a3c2fe: SEG_ACTIVE.band = text-[hsl(var(--palette-white))] border-[hsl(var(--palette-white))]; SEG_IDLE.band = text-[hsl(var(--palette-mediumGray))]; BUTTON_KIND.band secondary and ghost the same",
        "portal/design/themes/opal-capital.css:22 and :28: --palette-white 222 38% 93% (near white), --palette-mediumGray 220 18% 71% (#A8B0C0)",
        "headless render of /market at 1440x900 on the merged branch (tokens, sidebar, panels; no heat cell yet), read by the COO at 05:5xZ: the WTD and 90D active chips and the idle chips of the Period controls are pale on the white panel header"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD FWD-3 ACCEPT and C-PANEL: panels are white and nothing inside a panel is left unreadable by the primitives alone; FWD-1 ACCEPT: the page shows real figures and Andrew can say whether it reads as Opal's work.",
    "world_is": "Controls written with ground=band (the panel header used to be navy) spell their ink as palette tokens; inside a white panel they read as light grey on white, on the thread page itself.",
    "notes": "Ruled inside the COO's own decomposition (obligation 7): an addendum DIRECT-ACT cell, scoped token remap inside [data-panel-surface=\"light\"], no page file edited. Other token-spelled light inks inside panels are the round-3 walk's population."
  },
  {
    "id": "DSGN_RBNDV2-W4-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~4",
    "surfaced_at": "2026-10-15T05:46:24Z",
    "one_line": "None of the eight F10 heat files coloured a heat cell blue at the base ad7c100b5c; the 'blue scale' premise of RV-h-1 has no target in this list.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/BenchmarkHeatmap.tsx@ad7c100b lines 258-263 (return text success/danger), 266-270 (spread text white), 276-280 (spread overlays bg-emerald-500/50, bg-red-500/50, bg-yellow-500/50), 282-286 (navy row backgrounds): no blue",
        "portal/src/components/PerformanceHeatMap.tsx@ad7c100b line 3 (getReturnColorClass from performanceUtils.ts lines 70-75: delta tokens) and line 227 (indigo tooltip ground, a comment): no blue heat cell",
        "portal/src/pages/Macroeconomics/utils/percentileColor.ts@ad7c100b lines 20-49 (rgba green-500 / lime-500 / yellow-500 / orange-500 / red-500), 52-65 (text-green-300..text-red-300): no blue",
        "portal/src/pages/Valuation/panels/ValuationSummaryPanel.tsx@ad7c100b lines 32-43 (rgba red / orange / yellow / gray / green / emerald): no blue",
        "portal/src/pages/Correlation/constants.ts@ad7c100b lines 25-33 (CORRELATION_COLORS: pink rgba(236,72,153,..) positive, green rgba(34,197,94,..) negative): no blue; Blue-token census over the base text of the 8 files returns 0 for 7 files and 2 for Correlation.tsx line 82 (focus:border-cyan-500/50, focus:ring-cyan-500/30 on a select, not a heat cell)",
        "worktree check: git -C portal show ad7c100b5c:src/... read by rb-1-h.readers.test.ts base arm (run output: baseBlueCounts 0 x7, 2 x1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-h-1 cell and C-HEAT: 'Point each heat map at it, replacing its own blue colour logic'; 'The blue scale is gone from every heat map'. RB1H-AC2: the test lists per file 'the blue literals or blue class names that the base file coloured heat cells with' and the same absence check on base text must FAIL for every file.",
    "world_is": "The eight files at ad7c100b5c colour heat cells with emerald/red/yellow overlays, rgba green-lime-yellow-orange-red traffic bins, pink/green diverging rgba, and text delta tokens; ReturnsHeatmap has no shading. No file holds a blue heat colour, so there is no blue logic to replace and the base difference control cannot fail for seven of eight files.",
    "notes": "AC1 (the scale itself) is built and passes: portal/src/lib/heatScale.ts, silver #889399. The per-file repoint is not made; see the sibling rows for the decisions it needs. Routed to 2.0.0_SA_COO~RB to re-state the per-file target for round 1."
  },
  {
    "id": "DSGN_RBNDV2-W4-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~4",
    "surfaced_at": "2026-10-15T05:46:24Z",
    "one_line": "Two heat maps shade diverging (positive vs negative) cells, and one white-to-silver scale cannot keep their sign semantics without a second hue, which the cell forbids.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/Correlation/constants.ts@ad7c100b lines 26-33: positive correlations pink rgba(236,72,153,0.08..0.7), negative green rgba(34,197,94,0.25..0.45)",
        "portal/src/pages/Correlation/components/CorrelationMatrix.tsx@ad7c100b lines 6-8 (header: pink-to-white positive, green negative) and the legend lines 178-205",
        "portal/src/components/BenchmarkHeatmap.tsx@ad7c100b lines 276-280: spread overlays emerald (positive), red (negative), yellow (zero) at /50"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-h-1: 'Where a file colours a heat cell as diverging (positive vs negative), keep the sign semantics of the data and shade magnitude by the scale; do not invent a new hue.' C-HEAT: ONE white-to-silver scale that every heat map reads.",
    "world_is": "A single-hue white-to-silver ramp carries magnitude only. Sign would then rest on no colour cue, since cell text stays navy ink. Keeping sign needs a second hue, which the cell forbids, or a non-colour cue (a glyph or a sign label), which the cell does not name.",
    "notes": "Not repointed. Needs a ruling: (a) sign carried by a non-colour cue on the white-silver ramp; (b) the diverging cells keep their own hues as a named exception to C-HEAT; or (c) another rule. The worker does not choose."
  },
  {
    "id": "DSGN_RBNDV2-W4-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~4",
    "surfaced_at": "2026-10-15T05:46:24Z",
    "one_line": "ReturnsHeatmap.tsx has no heat shading to replace; pointing it at heatScale would invent a shading the fixture does not carry.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/reporting/ReturnsHeatmap.tsx@ad7c100b lines 116-160: data cells carry text classes only (text-[hsl(var(--palette-navy))], tabular-nums); the spread row carries bg-[hsl(var(--hairline))]/20 (a row tint, not a value scale)",
        "A_LIGHT_FIXTURE.md (Heat maps paragraph): the board has none; C-HEAT says white to silver"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-h-1: 'replacing its own blue colour logic and keeping its data logic'; the fixture: 'invent nothing'.",
    "world_is": "The file has no colour logic of its own to replace; it is a plain numeric table. Whether it should gain a shading is a design call the fixture does not make.",
    "notes": "Left unchanged pending the ruling on S1."
  },
  {
    "id": "DSGN_RBNDV2-W4-S4",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~4",
    "surfaced_at": "2026-10-15T05:46:24Z",
    "one_line": "RB1H-AC2 cannot pass as written: its presence arm needs all eight files repointed, its difference control cannot fail for seven files, and its absence arm trips on a non-heat cyan focus class in Correlation.tsx.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rb-1-h.readers.test.ts run at the worktree portal (bun 1.3.9): presence false for 8 of 8, absence false for Correlation.tsx only, baseControl false for 7 of 8 (baseBlueCounts 0), VERDICT not printed",
        "portal/src/pages/Correlation/Correlation.tsx@ad7c100b line 82: focus:border-cyan-500/50 focus:ring-cyan-500/30 on the ticker select (not a heat cell)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB1H-AC2 difference control: 'the same absence check run against the base text must FAIL for every file, proving it can fail'; 'Refusal clause: do not weaken the test to pass'.",
    "world_is": "The check is written from the criterion's text and runs honestly; it fails in three arms for the reasons in S1 to S3 and the non-heat cyan focus class. Nothing was weakened.",
    "notes": "Criterion-level defect for the issuer: re-state the base-control arm against the real base colour logic (or drop it), and scope the absence arm to heat-cell classes. The worker does not re-scope it."
  },
  {
    "id": "DSGN_RBNDV2-W4-S5",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~4",
    "surfaced_at": "2026-10-15T05:46:24Z",
    "one_line": "A blue percentile legend sits in a file outside this cell's grant: Valuation/tabs/ValuationTimeSeriesTab.tsx names blue as a band in its percentile colour mapping.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/Valuation/tabs/ValuationTimeSeriesTab.tsx@ad7c100b line 69: comment 'Map percentile to legend color: green(cheap) -> blue -> gray -> orange -> red(expensive)', with getPercentileColor mapping to PERCENTILE_COLORS (lines 70-76)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-h-1: 'if a heat map elsewhere in src/ also uses a blue scale, name its file in a surprise row and leave it (it is a wall: not in your <paths>).'",
    "world_is": "This file is a valuation time-series chart with a percentile line colour, not a heat-cell map; its blue band is named in the comment. Left untouched (outside the grant). Named for the issuer to rule whether it is a heat map.",
    "notes": "Not in <paths>; no edit made."
  },
  {
    "id": "DSGN_RBNDV2-W5-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~5",
    "surfaced_at": "2026-10-15T06:08:36Z",
    "one_line": "The criterion's difference-control invocation git show d2a3c2fe:portal/src/index.css does not resolve from the workspace root (rc=128): the base commit lives in the portal's own git repository, so the test reads git show d2a3c2fe:src/index.css from the portal root, which returns the same base bytes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C C:/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-5/portal cat-file -t d2a3c2fe printed commit; git rev-parse --show-toplevel from the portal printed C:/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-5/portal (a separate repository)",
        "git show d2a3c2fe:portal/src/index.css run at C:/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-5 printed 'fatal: invalid object name d2a3c2fe' and rc=128; git cat-file -t d2a3c2fe at the workspace root printed the same fatal line",
        "bun test src/__tests__/dsgn-rbndv2/rb-1-r.remap.test.ts before the CSS edit: 0 pass, 1 fail, 'exact-scope rules outside @layer: 0'; after the edit: VERDICT: PALETTE-REMAP-OK, 1 pass"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB1R-AC1 (TO RV-r-1): the difference control runs the same text checks against git show d2a3c2fe:portal/src/index.css and reports the rule absent, proving the test can fail.",
    "world_is": "The portal is its own git repository, so the base path form in the criterion resolves only from inside the portal. The test reads the base as git show d2a3c2fe:src/index.css with cwd at the portal root; it asserts the base text carries the existing [data-panel-surface=light] .text-white rule (positive control) and that the exact-scope rule is absent there, so the control can fail.",
    "notes": "The criterion's literal invocation was not run as written; the bytes it names are the same. No file outside the grant was touched."
  },
  {
    "id": "DSGN_RBNDV2-W5-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~5",
    "surfaced_at": "2026-10-15T06:08:36Z",
    "one_line": "The scoped palette remap reaches every palette-white and palette-mediumGray consumer inside a light panel, not only the Segmented and Button band variants: 161 occurrences in 31 portal/src files, and 5 of them paint a status dot fill rather than ink, so an idle grey dot inside a light panel turns navy.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- at the FWD-5 walk (round 3), decide whether the status dots keep the quiet ink or take a fill token; the remap cell edits no page file and does not touch them.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "native Grep over C:/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-5/portal/src for palette-white or palette-mediumGray (base d2a3c2fe plus the RV-r-1 edit): 161 occurrences across 31 files",
        "bg-[hsl(var(--palette-mediumGray))] status dot at portal/src/pages/AdvisorIntelligence/_partners/inflection/index.tsx:323, demo/index.tsx:263, cottonwood/index.tsx:206, 49financial/index.tsx:303, and portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx:93",
        "whether each dot sits inside a light panel was not measured; the native Grep found no bg- or fill use of palette-white"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-r-1 cell: a custom property set on the panel root is inherited by every control inside it, so nothing else needs to move; the cell edits only portal/src/index.css and its test.",
    "world_is": "The remap is scoped to [data-panel-surface=light], so every element inside a light panel that spells palette-mediumGray now resolves to the navy ink, including the four partner-page status dots and the ExecManagementTab dot that paint a fill. An idle grey dot inside a light panel reads as navy, a change of meaning the cell did not name.",
    "notes": "Filed, not fixed: the cell grants only index.css and its test, and the page files are outside it."
  },
  {
    "id": "DSGN_RBNDV2-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~RB",
    "surfaced_at": "2026-10-15T06:50:00Z",
    "one_line": "On /market with live data inside the white panels, the heat tables and tiles keep dark navy grounds (the old --bg-header, --bg-medium, --bg-card and --semantic-background-contentPanel tokens) while the light-panel ink rule turned their white text to navy: names read navy on navy, 141 text elements under 3:1.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- disarmed when the scoped surface-token remap (addendum cell RV-r-2) lands and /market reads in the COO's close run.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ui-walk of /market on the merged feature branch via dev:live on 5174, signed in as the walker, 2026-10-15 06:33Z: finding design:contrast 141 text element(s) under 3:1; first sample text 'Trump Announces $80B Taiwan LNG Deal' ratio 1.44, color rgb(10, 23, 51) on background rgb(37, 52, 86) (walk folder tmp/ui-walk/20261015T063315Z, gitignored)",
        "portal/src/components/PerformanceHeatMap.tsx lines 114, 161, 173, 245, 296 and BenchmarkHeatmap.tsx lines 284-286: grounds spelled bg-[hsl(var(--semantic-background-contentPanel))], --bg-header, --bg-medium, --semantic-background-hover; ExecutiveSummary.tsx lines 673, 776, 794, 959, 992, 1110: --bg-medium, --bg-card, --bg-header",
        "portal/src/index.css: --bg-header, --bg-medium, --bg-card, --bg-dark, --bg-medium-alt all alias --bg-band (the dark field)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD FWD-4 ACCEPT: heat maps shade white to silver, none left in the old blue scale; FWD-3 ACCEPT: no stacked dark strips, panels read white; FWD-1: the page shows real figures and reads as Opal's work.",
    "world_is": "The 'blue scale' is the navy ground of the heat tables (PerformanceHeatMap, BenchmarkHeatmap) and the dark tiles, not a hue ramp in the eight F10 files, which is why the RV-h-1 worker found no blue literal. The ink rule (RV-t-1 c) flips their white text to navy while their ground stays navy.",
    "notes": "Ruled inside the COO's own decomposition (obligation 7): addendum 2, DIRECT-ACT cell RV-r-2, scoped token remap of the old dark surface tokens inside [data-panel-surface=\"light\"] to white and silver, no page file edited. Heat cell premise finding goes to the CTO in the drain-end message."
  },
  {
    "id": "DSGN_RBNDV2-W6-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~6",
    "surfaced_at": "2026-10-15T06:58:10Z",
    "one_line": "The acceptance invocation for RB1R2-AC1 names the literal placeholder <WS> in its cd path, which no shell resolves as written; the worker ran it with <WS> replaced by its worktree path.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-r-2.inner-surface-token-remap.md worker face, ACCEPTANCE: invocation of RB1R2-AC1 begins 'cd <WS>/portal'; header declares <placeholders>WS</placeholders>",
        "worktree /c/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-6 at portal HEAD f96f2d60 (branch wk-DSGN_RBNDV2-6-portal, equal to feature/dsgn-rbndv2-light)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB1R2-AC1 invocation: 'cd <WS>/portal && ... bun test src/__tests__/dsgn-rbndv2/rb-1-r2.surfaces.test.ts' runs as written and prints VERDICT: INNER-SURFACES-OK.",
    "world_is": "The invocation is not runnable verbatim because <WS> is an undeclared-expansion placeholder. The worker ran it with <WS> replaced by /c/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-6, the worktree the order names; bun test then printed VERDICT: INNER-SURFACES-OK with rc=0 (1 pass, 0 fail, 7 expect() calls).",
    "notes": "No criterion was weakened. The substitution changes only the path prefix, not the command or the expectation."
  },
  {
    "id": "DSGN_RBNDV2-W6-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~6",
    "surfaced_at": "2026-10-15T06:58:10Z",
    "one_line": "The task order file in the worker's worktree carries the RECORD FACE header and its preflight block below the WORKER FACE, although the worker face is the worker's whole context and the record face never travels.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- the issuer cuts the worker's copy of the order without the RECORD FACE, or rules where the record face is placed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-r-2.inner-surface-token-remap.md after the REPORT line: a '---' separator, then '## RECORD FACE' and a '<preflight>' block (read at worktree HEAD f96f2d60 by a sed of lines 1-80)",
        "the worker rules this face is built on: the WORKER FACE is the worker's whole context; the RECORD FACE never travels (L7)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "L7: the WORKER FACE is the worker's whole context and the RECORD FACE never travels to the worker.",
    "world_is": "The order file at the worker's worktree path contains the RECORD FACE header and its preflight block. The worker read them in passing while locating the criteria and took no action from them; the criteria, invocations and expectations used are the WORKER FACE's.",
    "notes": "Observed only; the worker did not open the rest of the RECORD FACE section."
  },
  {
    "id": "DSGN_RBNDV2-W7-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~7",
    "surfaced_at": "2026-10-15T07:58:58Z",
    "one_line": "The test file RB1R3-AC1 names, rb-1-r3.token-format.test.ts, is absent from the worktree at HEAD adc70061; the worker authored it at that path to the criterion's arms.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- confirm at the drain that the authored file is the test the order meant, and that no other cell writes the same path.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/ui/components/sidebar/__tests__/dsgn-rbndv2/ listing at adc70061 (worktree /c/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-7/portal): rb-1-s.app-seam.test.ts and rb-1-s.sidebar.test.tsx only",
        "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-r-3.sidebar-token-format.md ACCEPTANCE: the invocation names src/ui/components/sidebar/__tests__/dsgn-rbndv2/rb-1-r3.token-format.test.ts"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-r-3 RB1R3-AC1: the criterion's invocation runs src/ui/components/sidebar/__tests__/dsgn-rbndv2/rb-1-r3.token-format.test.ts and expects VERDICT: SIDEBAR-TOKEN-FORMAT-OK.",
    "world_is": "The named file did not exist, so the invocation could not produce its verdict. The worker wrote the file at the named path, inside the granted folder, with the arms the criterion lists and the adc70061 difference control, and did not weaken any assertion."
  },
  {
    "id": "DSGN_RBNDV2-W7-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~7",
    "surfaced_at": "2026-10-15T07:58:58Z",
    "one_line": "The criterion says the --rb names used by the sidebar are five names defined in index.css :root; the :root block defines seven.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/index.css lines 135-141 (:root block, RB-t-1 tokens): --rb-rule, --rb-row-rule, --rb-ink, --rb-ink-2, --rb-ink-3, --rb-quiet, --rb-accent",
        "the sidebar files at the cell's HEAD use exactly accent, ink, ink-2, ink-3, rule (AppSidebar.tsx, SidebarLink.tsx)"
      ]
    },
    "spec_asserts": "TO RV-r-3 RB1R3-AC1: every --rb- name used in the two files is one of the five names defined in src/index.css :root.",
    "world_is": "The defined set is seven names. The test reads the defined set from the CSS text and checks that every used name is in it; the used set is the five named in the criterion, so the verdict is the same under either reading."
  },
  {
    "id": "DSGN_RBNDV2-W9-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~9",
    "surfaced_at": "2026-10-15T08:35:21Z",
    "one_line": "The RV-i-1 section contract turns the round-1 test RB1P-AC1 arm (f) red: that arm requires NestedCard to render the box surface and hairline it now removes.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- rule whether RB1P-AC1 arm (f) is amended to the section contract (a round-2 criterion amendment) or the round-1 test is kept; until then the portal panels test run on this branch stays red at that arm. The worker did not edit the round-1 test.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/ui/components/panels/__tests__/dsgn-rbndv2/rb-1-p.panel.test.tsx lines 122-135 (arm f: NestedCard root must carry bg-[hsl(var(--bg-surface))] and border-[hsl(var(--hairline))]) at branch HEAD febd743a plus the RV-i-1 commit",
        "bun test run of rb-1-p.panel.test.tsx after the RV-i-1 change: 0 pass, 1 fail; Expected to contain bg-[hsl(var(--bg-surface))]; Received [ py-4, px-4 ]",
        "portal/src/ui/components/panels/NestedCard.tsx at the RV-i-1 commit: cn('py-4 px-4', className), no bg- class, no border class, no absolute bar",
        "bun test run of rb-2-i1.sections.test.tsx: VERDICT: SECTIONS-OK, 27 expect() calls, 1 pass"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-i-1 RB2I1-AC1: NestedCard renders a section with no border box, no bg- fill, no radius and no absolutely positioned bar, and PanelGrid draws the hairlines. Round-1 TO RV-p-1 RB1P-AC1 arm (f): NestedCard, like SectionCard and DarkCard, renders the white surface and the hairline border.",
    "world_is": "Both assertions cannot hold on the same NestedCard. RV-i-1 was executed as written, so the round-1 arm (f) now fails by design. The worker left the round-1 test unchanged and did not weaken the RV-i-1 criterion."
  },
  {
    "id": "DSGN_RBNDV2-W8-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T08:32:09Z",
    "one_line": "The pre-commit checks passed a portal .tsx commit with 0 of 3 files checked: the risk reflex scanned 0 of 3 with a STALE danger map, and commit-gate reads only .py/.sh/.tf/org/projects JSON.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- route to the commit-gate and risk-reflex owner; no worker can disarm it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "safe-commit output of commit 1b157a12 in the portal worktree (branch wk-DSGN_RBNDV2-8-portal): comp-pulse WARN, the portal toplevel carries no .tools/comp-pulse, so the baked path C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/comp-pulse ran; danger map 194.9h old, ANSWER STATE PARTIAL_OR_BLIND, scanned 0 of 3",
        "safe-commit output of commit 1b157a12: [commit-gate] WARN checked 0 of 3 file(s); the gate reads only .py / .sh / .tf / org/projects/*.json",
        "the worker ran the checks itself before the commit: bun test on rb-2-m1.frame.test.tsx (1 pass) and bun x tsc --noEmit -p tsconfig.app.json (rc=0, 0 error TS lines) in the portal worktree"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Rule 14 of CLAUDE.md: every .py edit passes .tools/commit-gate.sh; rule 14a: commit via .tools/safe-commit.sh. The TO RV-m-1 names no frontend pre-commit check.",
    "world_is": "safe-commit ran for a portal .tsx-only commit, and the commit-gate and risk reflex both checked none of its three files and printed that as WARN, not as a failure. Every frontend commit on the portal worktree passes this path unchecked by the pre-commit gates."
  },
  {
    "id": "DSGN_RBNDV2-W8-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T08:32:09Z",
    "one_line": "The order says the portal feature branch is at adc70061; the worktree HEAD is febd743a, three commits later, carrying the RV-r-3 merge and its token-format fix (919f5cc3).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal rev-parse --short HEAD at the worktree start: febd743a (wk-DSGN_RBNDV2-8-portal); git merge-base --is-ancestor adc70061 HEAD: ancestor",
        "git -C portal log --oneline adc70061..HEAD before the RV-m-1 commit: 919f5cc3 fix(DSGN_RBNDV2 RV-r-3) and febd743a drain(DSGN_RBNDV2.TO-RV-r-3)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-1 Environment: the portal worktree is branched from feature/dsgn-rbndv2-light at adc70061 (the difference-control base).",
    "world_is": "adc70061 is an ancestor of the worktree HEAD febd743a, which adds the round-1 RV-r-3 sidebar token fix and its drain. The round-1 state the order describes is present; the base named in the order is not the HEAD. The RV-m-1 commit 1b157a12 sits on febd743a."
  },
  {
    "id": "DSGN_RBNDV2-W8-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T08:55:14Z",
    "one_line": "RB2M2-AC2 cannot pass as written by a correct adoption: each of the four TradeSubmission modals loses three onClick tokens (5 at adc70061, 2 now) because the overlay, the card stopPropagation and the header X handlers are the chrome ModalFrame replaces.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal show adc70061:src/pages/TradeSubmission/components/RejectModal.tsx: onClick count 5; the working tree (commit 1b157a12 plus the adoption edits): onClick count 2; useState 3 and 3",
        "rb-2-m2.bound.test.ts run in the portal worktree: RB2M2-AC2 TradeDetailsModal.tsx onClick base 5 now 2, expect(after).toBeGreaterThanOrEqual(before) received 2, expected >= 5; test not weakened"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-2 RB2M2-AC2: for each ADOPTED file, the file still contains every useState, useEffect, onClick and onSubmit token count it had at the base (a count may not fall); insertions plus deletions at most 160 lines.",
    "world_is": "The line bound holds (73, 82, 84, 96 changed lines against 160). useState, useEffect and onSubmit hold at base. onClick falls by three in each file, the three chrome handlers that ModalFrame now owns (scrim click, surface, Close control); the behaviour they carried is reproduced by the frame's onClose. The count bound cannot be met by an adoption that removes the chrome. The arm is not weakened; AC2 is recorded FAIL and the order stays open pending the issuer's ruling on the proxy."
  },
  {
    "id": "DSGN_RBNDV2-W8-S4",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T08:55:14Z",
    "one_line": "The order's base form git show adc70061:portal/<file> run from the workspace root fails: adc70061 is not an object in the workspace repository; it is a commit of the portal repository.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git cat-file -t adc70061 run in /c/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-8 returns fatal: Not a valid object name adc70061",
        "git -C portal cat-file -t adc70061 returns commit; cd portal && git show adc70061:src/pages/TradeSubmission/components/RejectModal.tsx prints the base file"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-2 RB2M2-AC1 invocation text: the base text is read with git show adc70061:portal/<file> from /c/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-8.",
    "world_is": "The form from the workspace root produces no base text. The tests read the same commit from the portal root with git show adc70061:src/... (the same bytes, the portal prefix dropped). No criterion was weakened by the path change."
  },
  {
    "id": "DSGN_RBNDV2-W8-S5",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T08:55:14Z",
    "one_line": "ModalFrame has no disabled state for its Close control, so the three action modals guard onClose while a submission is in flight; a backdrop click during submission no longer closes, where it did at base.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RejectModal.tsx, ExecuteModal.tsx and ApproveModal.tsx at adc70061: the header X button carries disabled={isSubmitting}; the overlay onClick called onClose with no guard",
        "portal/src/ui/components/modal/ModalFrame.tsx at 1b157a12: the Close button has no disabled prop; the scrim calls onClose when closeOnBackdrop is not false; Escape calls onClose"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-2 worker face: ALL state, effects, handlers, props and behaviour of the modal stay exactly as they are.",
    "world_is": "requestClose wraps onClose in the three action modals and does nothing while isSubmitting, so the X and Escape cannot close an in-flight submission, as the disabled X did. A backdrop click during submission is now also ignored, which differs from base. Escape and focus return are new to these modals because the frame provides them; the frame's API has no prop to disable the Close control."
  },
  {
    "id": "DSGN_RBNDV2-W8-S6",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T09:27:19Z",
    "one_line": "ModalFrame's focus-on-open effect runs after React's autoFocus, so the autoFocus search and weight inputs of SecurityLookupModal and BulkEditModal likely lose focus to the dialog surface on open.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- ModalFrame's focus effect should skip the focus call when focus is already inside the surface; route to the owner of the RV-m-1 frame.",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "portal/src/ui/components/modal/ModalFrame.tsx at 1b157a12: the focus effect is a useEffect that calls surfaceRef.current.focus() on open",
        "portal/src/pages/PortfolioManagement/components/SecurityLookupModal.tsx and BulkEditModal.tsx at 8c65d1c9 (the adoption commit, portal branch wk-DSGN_RBNDV2-8-portal): the input carries autoFocus; React applies autoFocus during commit, before passive effects; not walked in a browser (no server, per the order)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-3 worker face: ALL state, effects, handlers, props and behaviour of each adopted modal stay exactly as they are.",
    "world_is": "The adopted modals keep their autoFocus attributes unchanged. By the order of React's commit and effect phases, the frame's focus effect moves focus from the input to the surface on open, so the autofocus behaviour of the two inputs is likely lost. Not walked in a live DOM; the fix is in the frame, outside this order's grant, and the adopted files were not changed to work around it."
  },
  {
    "id": "DSGN_RBNDV2-W8-S7",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T09:27:19Z",
    "one_line": "ModalFrame adds a Close control and Escape-to-close to modals that had neither: UploadConfirmationModal and the ExportModal success view got a new close control, and Escape now closes ExportModal while a submission is in flight (its X and backdrop could already do so).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show adc70061:portal/src/pages/PortfolioManagement/components/UploadConfirmationModal.tsx: no close button in the header; the backdrop calls onClose",
        "git show adc70061:portal/src/pages/PortfolioManagement/components/ExportModal.tsx: the success header has no close button; the form X and backdrop are unguarded (no disabled); Cancel is disabled while submitting"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-3 worker face: ALL state, effects, handlers, props and behaviour of each adopted modal stay exactly as they are.",
    "world_is": "These two gains come from the frame's shared chrome, not from the adopted files. UploadPortfolioModal's header X was disabled while uploading; the frame's Close control cannot be disabled, so the handler guard (handleClose) carries that rule, as recorded in DSGN_RBNDV2-W8-S5."
  },
  {
    "id": "DSGN_RBNDV2-W8-S8",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T09:47:29Z",
    "one_line": "portal/src/components/market-performance/ExecutiveSummary.tsx carries its own modal overlay in DrilldownModal (function at line 731, fixed inset-0 overlay at line 772); the file is not on the RV-m-4 list, so it is not adopted.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/market-performance/ExecutiveSummary.tsx at the portal commit dc5cf484: line 731 function DrilldownModal, line 772 className fixed inset-0 z-[100] flex items-center justify-center bg-black/60 backdrop-blur-sm",
        "the sweep of portal/src/components/market-performance (native Grep for fixed inset-0, role=dialog, aria-modal, aria-labelledby, catalyst/dialog) returns this line as the only overlay outside the five listed modals"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-4 worker face: the market-performance modals on the list adopt ModalFrame; ExecutiveSummary.tsx is NOT on the list; look in the directory for any other overlay and name it in a surprise row (a wall, not to be edited).",
    "world_is": "DrilldownModal in ExecutiveSummary.tsx still draws its own overlay and card. It is a modal the directory holds and the list does not name, so it remains the un-adopted modal of the directory until the issuer decides its cell."
  },
  {
    "id": "DSGN_RBNDV2-W8-S9",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T09:47:29Z",
    "one_line": "RSIModal and FearGreedModal keep a literal dark content ground (bg-[hsl(221,28%,25%)]), which the frame's token remap does not reach; inside data-panel-surface the text-white idioms resolve to navy ink, so the labels on that ground are likely navy on dark navy.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- the content ground of these two modals needs a token or a light ground; the issuer decides which, since the order keeps chart colours (C6) and changes only chrome.",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "portal/src/components/market-performance/RSIModal.tsx line 1003 and FearGreedModal.tsx line 696 at dc5cf484: <div className=\"flex-1 overflow-y-auto bg-[hsl(221,28%,25%)]\"> (a literal, not a --bg token)",
        "portal/src/index.css lines 546-555 (round-1 scoped rule): [data-panel-surface=\"light\"] .text-white and [class*=\"text-white/\"] set color to var(--rb-ink) #0A1733; the ground's text classes (text-white/70 and similar) fall under that rule"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-4 worker face: the frame's data-panel-surface turns the old dark grounds white and silver by token; a modal body written for a dark ground reads on the white surface; C6 keeps chart colours.",
    "world_is": "The literal navy ground is not a token, so the frame does not turn it white. The scoped rule turns the labels' text-white idioms to navy ink, so the labels on that ground are likely navy on dark navy. Not walked in a browser (no server, per the order); the judgment criterion RB2M4-AC3 is the check and it is the COO's."
  },
  {
    "id": "DSGN_RBNDV2-W8-S10",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T10:07:55Z",
    "one_line": "ModelPortfolioModal's navy HeroDialog (the 2026-09-14 design) is replaced by the A-light ModalFrame in this file only; HeroDialog still serves SatelliteModal, EtfModal and the page modals, so the modal family now carries two designs.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show adc70061:portal/src/components/ModelPortfolioModal.tsx: the render returns HeroDialog with eyebrow, icon, title, subtitle, meta and footer (the navy hero) and the file header states the 2026-09-14 design",
        "portal/src/components/ModelPortfolioModal.tsx at ec15d42a: the render returns ModalFrame (title Model Portfolio, the target and code in the first body row, footer DialogStamp); the HeroDialog import is removed",
        "native Grep for HeroDialog over portal/src lists 27 files, including components/SatelliteModal.tsx and components/EtfModal.tsx"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-5 worker face: each listed modal adopts ModalFrame and keeps its state, effects, handlers, props and behaviour; the cell's FWD-3 intent is one shared modal frame.",
    "world_is": "The adoption replaces the hero of this one modal. Its content (target, code, the ruled six fields, Key Notes, the data-as-of stamp) is kept; the eyebrow icon and the navy hero band are no longer drawn. The other HeroDialog modals are untouched, so the family differs. The issuer decides whether the hero is kept for this modal."
  },
  {
    "id": "DSGN_RBNDV2-W8-S11",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T10:07:55Z",
    "one_line": "SessionTimeoutWarning hides the frame's Close control with an arbitrary-variant class on the surface; the rule is checked as class text only (not walked), and if the variant does not emit, a dead X would show on a dialog that has no X by design.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- confirm in the live walk that the session warning shows no X; if it does, the frame needs a showClose option (the API is frozen by RV-m-1, so the issuer decides).",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "portal/src/components/SessionTimeoutWarning.tsx at ec15d42a: className=\"[&_button[aria-label=Close]]:hidden\" on ModalFrame (the className goes to the surface)",
        "portal/package.json: tailwindcss ^4.2.1 (arbitrary variants are supported); the emitted CSS was not inspected and the page was not walked (no server, per the order)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-5 worker face: SessionTimeoutWarning keeps its behaviour (static backdrop, no X: the user must actively choose to continue).",
    "world_is": "The Close control is hidden by a selector on the surface, which keeps the no-X behaviour if the variant emits as written. Onclose is a no-op, so even a visible Close control would not end the session. The walk decides."
  },
  {
    "id": "DSGN_RBNDV2-W8-S12",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T10:07:55Z",
    "one_line": "SmallAccountsByRoleModal keeps its own window keydown Escape effect, and the frame adds a document Escape handler, so one Escape press calls onClose twice.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show adc70061:portal/src/pages/AdvisorIntelligence/_shared/SmallAccountsByRoleModal.tsx lines 21-27: useEffect adds a window keydown listener that calls onClose on Escape",
        "portal/src/ui/components/modal/ModalFrame.tsx: the Escape effect adds a document keydown listener that calls onClose on Escape"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-5 worker face: every effect of the adopted modal stays exactly as it is.",
    "world_is": "The effect is kept as written. The frame's Escape adds a second onClose call per press. The onClose handler of the page is idempotent in practice (it closes a modal), so the double call is inert; the issuer may remove one listener."
  },
  {
    "id": "DSGN_RBNDV2-W8-S13",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T10:07:55Z",
    "one_line": "Other overlays in the files' directories, not on the list and not adopted: components/SatelliteModal.tsx and components/EtfModal.tsx (HeroDialog modals) and components/LoadingSpinner.tsx line 57 (a full-page fixed inset-0 loader, not a modal).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "native Grep of portal/src/components for HeroDialog lists SatelliteModal.tsx and EtfModal.tsx",
        "native Grep of portal/src/components for fixed inset-0 at portal/src/components/LoadingSpinner.tsx line 57: className fixed inset-0 bg-[hsl(var(--bg-page))] with Z_INDEX.overlay (a loader, with no dialog role)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-5 worker face: look in the files' own directories for any other overlay and name it in a surprise row, a wall you may not edit.",
    "world_is": "SatelliteModal.tsx and EtfModal.tsx are modals on HeroDialog and are not on the RV-m-5 list; LoadingSpinner.tsx draws a full-page loader, which is not a modal. None is edited."
  },
  {
    "id": "DSGN_RBNDV2-W8-S14",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T10:23:36Z",
    "one_line": "The App.tsx account-menu popup items keep hover:bg-white/10, and the round-1 light-scope remap excludes hover-variant classes, so on the white popup surface the hover tint is white on white and shows nothing.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "portal/src/App.tsx at ec15d42a: the popup buttons carry hover:bg-white/10 and hover:text-white",
        "portal/src/index.css lines 546-555 (round-1 scoped rule): the bg-white/ remap excludes classes containing :bg-white/ (a hover variant), so the hover fill is not remapped to a visible tint"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-6 worker face: App.tsx is changed only for the account-menu popup surface, which takes the A-light look; the popup's own classes are not changed.",
    "world_is": "The surface is the A-light panel and the item text reads navy. The item hover fill (white at 10 percent) does not show on the white surface. Not walked in a browser (no server, per the order); the issuer decides whether the hover needs a light tint token."
  },
  {
    "id": "DSGN_RBNDV2-W8-S15",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~8",
    "surfaced_at": "2026-10-15T10:23:36Z",
    "one_line": "ExportModal and SatelliteModal pass a width class (sm:max-w-[75rem]! and max-w-[56rem]) that must win over the frame's size class through the class merge; the merge is checked by reading the class string only, not by a rendered width.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "portal/src/pages/InvestorReporting/export/ExportModal.tsx: EXPORT_MODAL_PANEL_CLASS = 'sm:max-w-[75rem]!' passed as className to ModalFrame (size xl)",
        "portal/src/components/SatelliteModal.tsx at ec15d42a: className max-w-[56rem] when there is no sheet, over the size xl max-w-[64rem]"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-m-6 worker face: each adopted modal keeps its width (the export panel 75rem; the satellite sheet without a factsheet 56rem).",
    "world_is": "The frame's cn() merge keeps the className's important sm:max-w and the later max-w, so the intended widths should hold. Not walked: no server, no browser, no rendered width measured."
  },
  {
    "id": "DSGN_RBNDV2-W10-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~10",
    "surfaced_at": "2026-10-15T11:23:59Z",
    "one_line": "IndexPerformanceModal.tsx holds the same literal white chart props as the two named modals (grid, axis and tick rgba(255,255,255,...) at lines 456, 460, 461, 472, 473 and 479); it is outside RV-c-1's grant, so it is left untouched.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- the owner of the round-3 chart-chrome follow-on decides whether IndexPerformanceModal takes the same token mapping as RV-c-1 (grid var(--rb-rule), axis var(--rb-quiet), tick var(--rb-ink-3)); the drain's live read of the modals is the place it shows.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/market-performance/IndexPerformanceModal.tsx at portal HEAD 826551e2 lines 456 (CartesianGrid stroke rgba(255,255,255,0.1)), 460 and 472 (axis stroke rgba(255,255,255,0.4)), 461 and 473 (tick fill rgba(255,255,255,0.6)), 479 (fill rgba(255,255,255,0.5)); read by native Grep and sed at workspace HEAD 795eaa2bf3",
        "native Grep of portal/src/components/market-performance for rgba(255,255,255 returned 0 hits in KeywordSentimentModal.tsx, so that modal holds none of these props"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-c-1 Part 1 and the cell's Out-of-this-cell clause: the other three market modals (RSIModal, IndexPerformanceModal, KeywordSentimentModal) that hold the same literal white chart props are named by file and line numbers in a surprise row and left as they are.",
    "world_is": "IndexPerformanceModal.tsx carries the same white-on-dark chart chrome as FearGreedModal and MarketRegimeModal before this cell, at six lines. The file is not in the grant, so the chrome stays white on the white A-light surface; the axes stay unreadable there, the same class of defect the CVO graded NOT MET under RB2M4-AC3.",
    "notes": "Filed, not fixed. The cell's bounds name this file as a wall. KeywordSentimentModal holds none of the literals."
  },
  {
    "id": "DSGN_RBNDV2-W10-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~10",
    "surfaced_at": "2026-10-15T11:23:59Z",
    "one_line": "RSIModal.tsx holds the same literal white chart props as the two named modals (grid, axis and tick rgba(255,255,255,...) at lines 229, 334, 351, 370, 375 and 376); it is outside RV-c-1's grant, so it is left untouched.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- the owner of the round-3 chart-chrome follow-on decides whether RSIModal takes the same token mapping as RV-c-1 (grid var(--rb-rule), axis var(--rb-quiet), tick var(--rb-ink-3)); the drain's live read of the modals is the place it shows.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/market-performance/RSIModal.tsx at portal HEAD 826551e2: line 229 (axis stroke rgba(255,255,255,0.3)), 334 (CartesianGrid stroke rgba(255,255,255,0.05)), 351 and 375 (tick fill rgba(255,255,255,0.5)), 370 and 376 (axis stroke rgba(255,255,255,0.1)); read by native Grep and sed at workspace HEAD 795eaa2bf3",
        "RSIModal's literal set is wider than RV-c-1's arm: it also uses rgba(255,255,255,0.3), 0.5 and 0.05 (lines 229, 351, 375 and 334), which the RV-c-1 literal arm does not name, so a fix that only swapped the three named alphas would pass that arm on this file while leaving these"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-c-1 Part 1 and the cell's Out-of-this-cell clause: the other three market modals that hold the same literal white chart props are named by file and line numbers in a surprise row and left as they are.",
    "world_is": "RSIModal.tsx carries white-on-dark chart chrome at six lines on the white A-light surface, so its axis and tick text stays unreadable there. The file is not in the grant and was not edited.",
    "notes": "Filed, not fixed. The cell's bounds name this file as a wall. A follow-on that maps this file must cover all four of its alpha values, not the three RV-c-1 names."
  },
  {
    "id": "DSGN_RBNDV2-W11-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~11",
    "surfaced_at": "2026-10-15T11:51:17Z",
    "one_line": "RSIModal.tsx line 229 (the custom dot circle stroke, alpha 0.3) falls in the gap between the RV-c-2 alpha bands (at or below 0.15 to rule, 0.4 to quiet, 0.5 or more to ink-3) and was mapped to var(--rb-quiet) as the nearest band.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/market-performance/RSIModal.tsx@6396217d line 229: stroke=\"rgba(255,255,255,0.3)\" on the dot circle of the RSI chart (read by sed at base 6396217d)",
        "portal/src/components/market-performance/RSIModal.tsx@c1035901 line 229: stroke=\"var(--rb-quiet)\"; RB3C2-AC1 test rb-3-c2.chart-chrome.test.ts prints VERDICT CHART-CHROME-2-OK (bun test rc=0)",
        "portal/src/components/market-performance/RSIModal.tsx@c1035901 lines 370 and 376: XAxis and YAxis stroke props at alpha 0.1 mapped to var(--rb-quiet) by the explicit axis-stroke rule; the alpha band would have given var(--rb-rule)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-c-2 cell text: every other white-alpha chart literal is mapped by its alpha (at or below 0.15 to var(--rb-rule), 0.4 to var(--rb-quiet), 0.5 or more to var(--rb-ink-3)), and each such line is named in the report.",
    "world_is": "RSIModal.tsx line 229 carries alpha 0.3, which is not at or below 0.15, not 0.4, and not 0.5 or more, so the band rule has no member for it. The explicit axis-stroke rule (quiet) and the alpha band (rule at 0.1) also disagree for lines 370 and 376; the explicit rule was applied there.",
    "notes": "Line 229 is mapped to var(--rb-quiet): distance 0.1 to the 0.4 band against 0.15 to the 0.15 band. The alternative is var(--rb-rule). The issuer may overrule either choice; the code change is one token on one line. Chart-chrome test arm (a) and AC1 pass on the mapping as written."
  },
  {
    "id": "DSGN_RBNDV2-W11-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~11",
    "surfaced_at": "2026-10-15T11:51:17Z",
    "one_line": "The worktree sparse checkout omits org/surprise_channel/schemas/ from disk although git tracks investigation_item.schema.json at HEAD, so the row contract the order names was read with git show HEAD and not from the working tree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "rbndv2-11 worktree (branch wk-DSGN_RBNDV2-11): git config core.sparseCheckout reports true; ls org/surprise_channel/schemas/ returns No such file or directory",
        "git ls-files --error-unmatch org/surprise_channel/schemas/investigation_item.schema.json lists the path; git show HEAD:org/surprise_channel/schemas/investigation_item.schema.json returns 10462 bytes; git status reports 0 deleted entries"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order names org/surprise_channel/schemas/investigation_item.schema.json as the row contract a worker reads per the surprise-channel rule, expected readable at the worktree path.",
    "world_is": "That path is absent from disk in this sparse worktree while git tracks it at HEAD. Nothing was restored or checked out; the schema was read from HEAD with git show.",
    "notes": "Filed, not fixed. The row was validated by field against the HEAD copy of the schema. The worktree was not changed."
  },
  {
    "id": "DSGN_RBNDV2-W12-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~12",
    "surfaced_at": "2026-10-15T13:04:14Z",
    "one_line": "The proof-of-spec artifacts_produced kind enum has no member for a stylesheet, so the CSS artifact portal/src/index.css is recorded as frontend_component, the nearest member, and the checker's first run on the instance was INVALID.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/standards/PROOF_OF_SPEC.schema.json@d0f2cf28c9 artifacts_produced kind enum: script, s3_object, terraform, config_data, schedule, iam, test, doc, frontend_component, ddb_rows, aws_resource (no stylesheet member)",
        "python .tools/proof-of-spec-check.py on the instance (portal artifact pinned at 2426d31b) printed VIOLATION: schema: artifacts_produced/0/kind: 'stylesheet' is not one of [...] and INVALID (rc=1); the same instance with kind frontend_component is re-checked before the flip"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The proof instance carries each produced artifact with a kind the schema admits, so a worker's CSS artifact is expressible without a kind substitution.",
    "world_is": "No kind in the enum names a stylesheet; the worker recorded the one CSS file (portal/src/index.css) as frontend_component to get a schema-valid instance. The kind is a label only, and the instance otherwise carries the pinned commit and the deploy evidence.",
    "notes": "Filed, not fixed. The enum is the schema owner's to extend. The substitution is declared here so a consumer does not read the kind as a claim that the file is a component."
  },
  {
    "id": "DSGN_RBNDV2-W18-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~18",
    "surfaced_at": "2026-10-15T15:09:43Z",
    "one_line": "RV-x-6 keeps the popup's source chips as they are, but its test arm bans the text backdrop-blur in ExecutiveSummary.tsx, and the chip carries backdrop-blur-sm, so the arm cannot pass unless that one class goes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/market-performance/ExecutiveSummary.tsx@7f8731df: the DrilldownModal source chip class list carries 'bg-black/50 text-white/80 backdrop-blur-sm border border-white/10'; the only other backdrop-blur occurrence in the file is the overlay root",
        "portal worktree wk-DSGN_RBNDV2-18-portal: backdrop-blur-sm removed from that chip only; bg-black/50, text-white/80 and border classes unchanged; rb-5-x6.trending-modal.test.ts run under bun prints DRILLDOWN-OWN-OVERLAY-BEFORE 1 DRILLDOWN-OWN-OVERLAY-AFTER 0 and VERDICT: TRENDING-MODAL-OK"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-x-6: the source chips 'bg-black/50 text-white/...' stay as they are, and the overlay's backdrop-blur is removed. RB5X6-AC1: ExecutiveSummary.tsx holds no 'backdrop-blur' text.",
    "world_is": "The chip's backdrop-blur-sm is a blur on a chip, not on the overlay, and the file-wide text arm counts it. The worker removed backdrop-blur-sm from the chip to satisfy the arm, leaving the chip's background and text classes as the cell names them. The chip now renders without the blur over the lead image.",
    "notes": "Filed, not fixed. The removal is the smallest change that meets the file-wide arm without weakening it. The order's author decides whether the chip blur should return with a frame-level exemption. The hero marker sits on the w-[40%] hero container, which holds the gradient block, the arrow svg and the source chips."
  },
  {
    "id": "DSGN_RBNDV2-W13-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~13",
    "surfaced_at": "2026-10-15T15:12:42Z",
    "one_line": "The order says the Trending Topics tile carries the marker data-ink=\"on-fill\" (added by another cell), but no file under portal/src carries the marker at the base 7f8731df, so the tile-arrow context of the RV-x-1 rule matches nothing in this worktree until that cell lands.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git grep -l data-ink 7f8731df -- src (portal repo, branch wk-DSGN_RBNDV2-13-portal) prints no path: zero matches at the difference-control base",
        "portal commit 3be788d9 adds the marker only as a selector context in portal/src/index.css (58 rules, 116 selectors) and in portal/src/__tests__/dsgn-rbndv2/rb-5-x1.on-fill.test.ts; no element in this worktree carries it",
        "portal/src/components/DataTooltip.tsx@7f8731df:26 carries bg-[hsl(var(--palette-indigo))] and its text classes sit on child spans (lines 27, 34, 37, 60), so the descendant context reaches the tooltip text"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-x-1 world premise: the Trending Topics tile carries the marker attribute data-ink=\"on-fill\", added by another cell, so the second context of the on-fill rule reaches the tile's text-white arrow on a green or red gradient tile.",
    "world_is": "At 7f8731df the marker is absent everywhere under portal/src, so the tile arrow is not reached by any RV-x-1 selector in this worktree. The tile is outside this order's <paths>, so this order cannot add the marker; the arrow stays navy in the live build until the marker-carrying cell lands on the tile.",
    "notes": "Filed, not fixed: the marker belongs to the other cell and the tile file is outside this order's grant. The indigo context reaches the text of DataTooltip and of the Daily Cloud tooltip, whose text-white classes sit on child spans. The generic Tooltip is the exception and has its own row, DSGN_RBNDV2-W13-S2. The COO's drain-end live read (RB5X1-AC3) is where the tile shows."
  },
  {
    "id": "DSGN_RBNDV2-W13-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~13",
    "surfaced_at": "2026-10-15T15:12:42Z",
    "one_line": "The generic Tooltip puts text-white on the indigo box itself (portal/src/components/Tooltip.tsx:195), and the RV-x-1 indigo context is a descendant selector, so that text stays navy under the light-panel rule.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB -- disarm by a rule that also reaches the element carrying the indigo fill (a compound selector such as [data-panel-surface=\"light\"] .bg-\\[hsl\\(var\\(--palette-indigo\\)\\)\\].text-white), or by moving the text class to a child, in a cell whose paths name Tooltip.tsx.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/components/Tooltip.tsx@7f8731df:195 className 'fixed ... px-3 py-2 text-sm text-white bg-[hsl(var(--palette-indigo))] rounded-[3px] ...': text-white and the indigo fill are on one element",
        "portal/src/components/HelperTip.tsx@7f8731df:20 passes !text-white on the same element as !bg-[hsl(var(--palette-indigo))]; the !-prefixed token is not the class text-white, so neither the legibility rule nor the RV-x-1 rule matches it",
        "portal commit 3be788d9: the RV-x-1 indigo context is [data-panel-surface=\"light\"] .bg-\\[hsl\\(var\\(--palette-indigo\\)\\)\\] .text-white, a descendant selector"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-x-1 spec: every text-white inside a solid indigo box keeps white ink in a light panel, reached by the descendant context of the indigo box.",
    "world_is": "A text-white class on the indigo box itself is not a descendant of it, so the specified context does not reach it and the legibility rule turns that text navy on indigo. Whether a light panel renders this Tooltip was not measured in this worktree; the reach is unverified.",
    "notes": "Filed, not fixed: Tooltip.tsx is outside this order's <paths>, and the order names the three tooltips that are descendant-shaped. The fix belongs to the owner of the tooltip surface."
  },
  {
    "id": "DSGN_RBNDV2-W15-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~15",
    "surfaced_at": "2026-10-15T15:35:26Z",
    "one_line": "safe-commit's commit-gate checked 0 of 3 .tsx files on the RV-x-3 portal commit cbb6b041 and printed NOTHING WAS CHECKED; the frontend change was graded by bun test only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal commit cbb6b041 on branch wk-DSGN_RBNDV2-15-portal, made via bash ../.tools/safe-commit.sh: commit-gate output 'checked 0 of 3 file(s) -- NOTHING WAS CHECKED' and 'not graded: 2 .tsx' (the third file was the test .ts)",
        "the gate banner states it reads only .py / .sh / .tf / org/projects/*.json and says to use the language-appropriate instrument (tsc -b, eslint, a read render) for a frontend artifact"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A commit of frontend files is gated by safe-commit's commit-gate, so a passing gate line is evidence the staged files were checked.",
    "world_is": "On cbb6b041 commit-gate checked none of the three staged files (RSIBars.tsx, RSIModal.tsx, rb-5-x3.rsi-ink.test.ts). The only instrument run on the .tsx changes is bun test src/__tests__/dsgn-rbndv2 (8 pass, 0 fail); no typecheck was run by the worker.",
    "notes": "Filed, not fixed: commit-gate and the commit tooling are outside this order's <paths>. The RV-x-3 criteria are graded by the order's own test (RB5X3-AC1, RB5X3-AC2), which is the instrument the order names."
  },
  {
    "id": "DSGN_RBNDV2-W15-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~15",
    "surfaced_at": "2026-10-15T15:35:26Z",
    "one_line": "The row contract the worker face names, org/surprise_channel/schemas/investigation_item.schema.json, is absent from this worktree, so the row was shaped from the sibling rows of this file.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "worktree /c/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-15 (branch wk-DSGN_RBNDV2-15): no org/surprise_channel/ directory exists (ls of the schemas folder fails)",
        "INVESTIGATION_v1.md in this worktree carries 48 rows whose field set and enum values (class OBSERVATION or BLOCKING, hazard_standing INERT or ARMED, disposition UNDER_INVESTIGATION) were read from the file itself"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Each new investigation row is validated against org/surprise_channel/schemas/investigation_item.schema.json before it is appended.",
    "world_is": "That schema file is not present in the worktree the order runs in, so the row's fields could not be checked against it; the row follows the field set of the existing rows and the .tools/surprise-row-gate.py check at commit is the remaining validator.",
    "notes": "Filed, not fixed: the schema location belongs to the surprise-channel owner. The row here is appended without modifying any existing row."
  },
  {
    "id": "DSGN_RBNDV2-W16-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~16",
    "surfaced_at": "2026-10-15T15:36:39Z",
    "one_line": "RV-x-4 says the portal worktree is branched from feature/dsgn-rbndv2-light at 7f8731df, but the worktree HEAD is 9027a72d, a descendant of 7f8731df that carries the RV-x-1 merge; 7f8731df is an ancestor of HEAD, not its tip.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree wk-DSGN_RBNDV2-16-portal: git rev-parse HEAD = 9027a72d at the start of the order; git merge-base --is-ancestor 7f8731df HEAD printed ANCESTOR-YES",
        "git -C portal log -1 9027a72d: 'drain(DSGN_RBNDV2.TO-RV-x-1): merge worker 0.9.0_WK_DSGN_RBNDV2~13 ... into feature/dsgn-rbndv2-light'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-x-4 environment block: the portal worktree is branched from feature/dsgn-rbndv2-light at 7f8731df, the difference-control base.",
    "world_is": "7f8731df is an ancestor of the worktree HEAD 9027a72d, which carries the RV-x-1 merge. The difference-control arms read the base by git show 7f8731df and are unaffected. The worker's commit 140f474f touches only the three RV-x-4 paths, so the descendant commits were not edited by this cell.",
    "notes": "Filed, not fixed. The order's branch premise is stale relative to the live branch; the cut point is the drain's merge commit, not the base named in the order. Whether the RV-x-1 merge changes the light-panel render of the Fear and Greed panel was not measured here; the arms are text arms."
  },
  {
    "id": "DSGN_RBNDV2-W17-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~17",
    "surfaced_at": "2026-10-15T15:50:18Z",
    "one_line": "RV-x-5 says the portal worktree is branched from feature/dsgn-rbndv2-light at 7f8731df, but the worktree HEAD was 5269d02c, 8 commits past 7f8731df, with 7f8731df an ancestor of it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree wk-DSGN_RBNDV2-17-portal: git -C portal rev-parse HEAD = 5269d02c before the RV-x-5 commit; git rev-list --count 7f8731df..5269d02c = 8 and 5269d02c..7f8731df = 0",
        "git merge-base --is-ancestor 7f8731df 5269d02c printed ANCESTOR-YES; git log -1 --oneline 5269d02c: 'drain(DSGN_RBNDV2.TO-RV-x-4): merge worker 0.9.0_WK_DSGN_RBNDV2~16 ... into feature/dsgn-rbndv2-light'; git log -1 feature/dsgn-rbndv2-light printed the same 5269d02c"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RV-x-5 environment block: the portal worktree is branched from feature/dsgn-rbndv2-light at 7f8731df, the difference-control base.",
    "world_is": "7f8731df is an ancestor of the feature tip 5269d02c, which the worktree was branched from. The difference-control arms read the base by git show 7f8731df and are unaffected. The RV-x-5 commit e72e5dbe touches only the three RV-x-5 paths.",
    "notes": "Filed, not fixed. The cut point is the feature tip 5269d02c, not the base named in the order. Same shape as DSGN_RBNDV2-W16-S1."
  },
  {
    "id": "DSGN_RBNDV2-W14-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~14",
    "surfaced_at": "2026-10-15T15:51:43Z",
    "one_line": "The commit gate checked 0 of 3 files on the portal commit that changes two .tsx files: it printed NOTHING WAS CHECKED, so the frontend change is graded by bun test only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal commit 5c317082 (LOCAL, branch wk-DSGN_RBNDV2-14-portal): safe-commit printed '[commit-gate] WARN: commit-gate checked 0 of 3 file(s) -- NOTHING WAS CHECKED' with 'not graded: 2 .tsx'",
        "the same warning was filed for the sibling portal commit cbb6b041 as DSGN_RBNDV2-W15-S1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order commits the portal change through .tools/safe-commit.sh; CLAUDE.md rule 14 says a .py edit passes .tools/commit-gate.sh, and the order graded this cell's change by bun test.",
    "world_is": "commit-gate reads only .py, .sh, .tf and org/projects/*.json; a frontend .tsx commit is not graded and the gate reports NOT CHECKED. No tsc or eslint run was made because the order names none.",
    "notes": "Filed, not fixed. The gate's own text says a frontend artifact needs tsc -b, eslint or a read render. Whether a frontend instrument belongs on the commit path is not decided here."
  },
  {
    "id": "DSGN_RBNDV2-W14-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~14",
    "surfaced_at": "2026-10-15T15:51:43Z",
    "one_line": "The RV-p-1 panel test header (lines 13-14 of rb-1-p.panel.test.tsx) still describes the footer caption as 11px uppercase; after RV-x-2 that is no longer the footer shape.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal commit 5c317082 changes src/ui/components/panels/__tests__/dsgn-rbndv2/rb-1-p.panel.test.tsx at lines 163-164 only",
        "the same file at 5c317082 lines 13-14 still reads 'the footer caption is 11px uppercase'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The RV-x-2 order says to change nothing else in an existing test; only the footer arms that assert uppercase are updated.",
    "world_is": "The header doc comment describes a footer shape the test no longer asserts; the assertion itself (lines 163-164) now expects no uppercase and tracking-normal.",
    "notes": "Filed, not fixed. A comment-only edit to this test is outside the order's bounds and is left to its owner."
  },
  {
    "id": "DSGN_RBNDV2-W14-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~14",
    "surfaced_at": "2026-10-15T15:51:43Z",
    "one_line": "The portal worktree HEAD at the start of the order was 5269d02c, a descendant of the difference-control base 7f8731df that carries the RV-x-3 and RV-x-4 merges; the order said the branch was cut at 7f8731df.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal rev-parse --short HEAD at the start of the order = 5269d02c",
        "git -C portal merge-base --is-ancestor 7f8731df HEAD printed ANCESTOR-YES; git -C portal log -1 5269d02c: 'drain(DSGN_RBNDV2.TO-RV-x-4): merge worker 0.9.0_WK_DSGN_RBNDV2~16'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Environment block: the portal worktree is branched from feature/dsgn-rbndv2-light at 7f8731df, the difference-control base.",
    "world_is": "7f8731df is an ancestor of HEAD 5269d02c, not its tip. The base read by git show 7f8731df is unaffected; commit 5c317082 changes only the three footer paths relative to 5269d02c.",
    "notes": "Filed, not fixed. Same shape as DSGN_RBNDV2-W16-S1; the difference control is unaffected because it reads the base by commit."
  },
  {
    "id": "DSGN_RBNDV2-W19-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~19",
    "surfaced_at": "2026-10-15T16:37:28Z",
    "one_line": "The RV-y-1 order sizes the border-white sweep at about 70 lines in 6 files; the measured base denominator is 63 border-white/N classes on 60 lines in the 6 in-scope files (62 lines in 7 files with SentimentGauge.tsx).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal d0cb67d0 (worktree HEAD d0cb67d0, no edits yet): git grep -n -E \"border-white/[0-9]+\" -- src/components/market-performance src/pages/MarketPerformance returns 60 lines and 63 occurrences across the 6 in-scope files",
        "the same grep also matches src/components/market-performance/SentimentGauge.tsx (2 lines, excluded by the order): 62 lines in 7 files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-1 face: a measured denominator at the base, about 70 lines in 6 files.",
    "world_is": "The base denominator is 60 lines (63 border-white/N classes) in the 6 in-scope files. BORDER_SWEEP_LIST.md carries 63 rows, one per class occurrence, and the test counts the measured set.",
    "notes": "Filed, not fixed. The order figure is soft (about); the sweep covers the measured set and the list records the measured count."
  },
  {
    "id": "DSGN_RBNDV2-W19-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~19",
    "surfaced_at": "2026-10-15T16:41:51Z",
    "one_line": "portal/CONTRIBUTING-BOXES.md says a portal feature is built on a cand/<box>/<slug> branch cut from the last PROD release and registered with open-calls.py; this order works on the worktree branch wk-DSGN_RBNDV2-19-portal, cut from feature/dsgn-rbndv2-light at d0cb67d0, and the order says commit to that branch and never push.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/CONTRIBUTING-BOXES.md (read at the portal worktree, 2387 bytes): steps 1-4 name cand/<box>/<slug> cut from the PROD release and open-calls.py add --kind approval",
        "git -C portal rev-parse --abbrev-ref HEAD = wk-DSGN_RBNDV2-19-portal; git -C portal log -1 = d0cb67d0 (feature/dsgn-rbndv2-light base named in the order)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-1 face: commit to the worktree branch only; never push, merge or rebase; the portal rule CONTRIBUTING-BOXES.md says a portal change is made on a cand/<box>/<slug> branch and registered for approval.",
    "world_is": "The two rules name different branches. This worker committed (locally) to the worktree branch and did not register an approval row, push, or merge to DEV. The branch naming and the approval registration are the issuer decision.",
    "notes": "Filed, not fixed. Nothing was pushed, merged to DEV or registered with open-calls.py by this worker."
  },
  {
    "id": "DSGN_RBNDV2-W19-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~19",
    "surfaced_at": "2026-10-15T16:41:51Z",
    "one_line": "tsc -p tsconfig.app.json --noEmit (portal root) reports one error TS2769 at src/__tests__/dsgn-rbndv2/rb-5-x5.hover-resolve.test.ts line 30 col 81: maxBuffer is passed to execSync, which the TypeScript overload set rejects; the same line is at base d0cb67d0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node_modules/.bin/tsc -p tsconfig.app.json --noEmit at the portal worktree: rc=2, error lines 1 (TS2769 at rb-5-x5.hover-resolve.test.ts(30,81)); no error line names rb-6-y1.border-sweep.test.ts",
        "git show d0cb67d0:src/__tests__/dsgn-rbndv2/rb-5-x5.hover-resolve.test.ts lines 28-31 carry the same readBase line with maxBuffer; the file last changed at e72e5dbe (RV-x-5)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-1 face: a test file must typecheck (execSync, join, a cast on process.env reads); the bar is the test this order writes.",
    "world_is": "The new test rb-6-y1.border-sweep.test.ts adds no tsc error. The one error sits in a neighbouring cell test (RV-x-5) that this order does not own, so it is recorded here and not edited.",
    "notes": "Filed, not fixed. The fix belongs to the owner of RV-x-5; this worker did not touch that file."
  },
  {
    "id": "DSGN_RBNDV2-W21-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~21",
    "surfaced_at": "2026-10-15T17:06:48Z",
    "one_line": "RV-y-3 names git show d0cb67d0:src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts as the difference-control base; that file does not exist at d0cb67d0, so the git show would fail.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal 86db3d1b (worktree wk-DSGN_RBNDV2-21-portal): git cat-file -e d0cb67d0:src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts = fatal, path not in d0cb67d0; the folder listing at d0cb67d0 has 11 test files and no rb-6-y1",
        "git log --diff-filter=A -- src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts = e6319c40 (RV-y-1); e6319c40^ = d0cb67d0; e6319c40 holds the same y1 text as HEAD (git diff e6319c40 HEAD on that file = 0 lines)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-3 difference control: the standalone arms run on git show d0cb67d0:<y1 test path> and on git show d0cb67d0:<x5 test path>, and must report at least one failing arm.",
    "world_is": "The y1 test first exists at e6319c40, the RV-y-1 commit whose parent is d0cb67d0. The x5 base at d0cb67d0 exists and names maxBuffer. This worker reads the y1 pre-fix text at e6319c40 and the x5 pre-fix text at d0cb67d0; the arms and the discrimination are unchanged.",
    "notes": "Filed, not fixed. Substitution made in rb-6-y3.standalone.test.ts only: the y1 control reads e6319c40 because d0cb67d0 does not carry the file. The issuer decides whether the order text is corrected."
  },
  {
    "id": "DSGN_RBNDV2-W21-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~21",
    "surfaced_at": "2026-10-15T17:06:48Z",
    "one_line": "RV-y-3 says the y1 test names org/missions literally; at its pre-fix text the path is split into quoted tokens, so a literal-string arm does not see it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal show e6319c40:src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts | grep -c 'org/missions' = 0; the LIST_PATH constant (lines 28-38 at e6319c40) builds the path from the tokens 'org', 'missions', 'deliverables', '0.9.0_WK_DSGN_RBNDV2~19', one token per line",
        "the literal arm alone on the y1 pre-fix text passes; the split-token arm (SPLIT_A, SPLIT_B in rb-6-y3.standalone.test.ts) fails it"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-3 standalone arm: no test file contains the string org/missions or deliverables/0.9.0, and the difference control fails on the y1 base for that reason.",
    "world_is": "The literal arm cannot discriminate the y1 pre-fix text. The standalone test also detects the same two segments written as separate quoted tokens, so the y1 control fails on that arm. No test in the folder names a workspace path after RV-y-3.",
    "notes": "Filed, not fixed in any other file. The split-token detector is a stronger form of the order's literal arm, not a weaker one; the literal check is still performed."
  },
  {
    "id": "DSGN_RBNDV2-W20-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~20",
    "surfaced_at": "2026-10-15T17:09:08Z",
    "one_line": "portal/src/components/market-performance/ExecutiveSummary.tsx line 268 builds the Trending Topics footer as a template literal from formatSourcesForFootnote, which passes each data source name through unchanged, so a lower-case name in the data prints lower-case in the footer.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/lib/sourceRanking.ts:103-119 formatSourcesForFootnote joins getTopSources output with no case normalisation (portal@86db3d1b)",
        "portal/src/components/market-performance/ExecutiveSummary.tsx:245-268 builds the footer; line 268 is the template literal (portal@86db3d1b)",
        "the top_sources feed values are not read in this worktree, so whether a live name is lower-case is not measured here"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-2 order: fix the class, not the strings; read how a template literal builds its names; if formatSourcesForFootnote can output a lower-case source name, write a surprise row naming the line and do not edit it.",
    "world_is": "The function can output a lower-case source name whenever the data carries one. Not edited: sourceRanking.ts is read-only for this cell.",
    "notes": "Filed, not fixed. The owner of sourceRanking.ts decides whether names are normalised at the source or at the footer."
  },
  {
    "id": "DSGN_RBNDV2-W20-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~20",
    "surfaced_at": "2026-10-15T17:09:08Z",
    "one_line": "Six string literals and two JSX texts beginning Source: open with lower-case prose, not a source name (for example 'Source: the report is not named in this security's data' and 'Source: a vendor's report.'); the capitalization rule has no reading for a sentence.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx:68 'Source: a vendor's report.' (portal@86db3d1b)",
        "portal/src/pages/SecurityAnalysis/components/DossierSections.tsx:56, portal/src/pages/SecurityAnalysis/tabs/ExecManagementTab.tsx:430, portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx:176 'Source: the report is not named in this security's data' (portal@86db3d1b)",
        "portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx:255 'Source: machine draft from a filing' and its template twin (portal@86db3d1b); JSX texts at ThesisCards.tsx:153 and portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx:499",
        "portal/src/__tests__/dsgn-rbndv2/rb-6-y2.footer-source-case.test.ts header: a segment that opens in lower case is prose and is not checked"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-2 order: every footer source string reads with every word of the source name capitalized, small words excepted.",
    "world_is": "These lines are sentences or prose clauses, not source names; title-casing them would change copy the order does not name. Left as written and counted as prose. NativeSections.tsx:68 is also compared by an existing test (rb iv-e-122, line 100), so changing it would edit a file outside the grant.",
    "notes": "Filed, not fixed. Whether a prose fallback is a footer string is a ruling for the CVO."
  },
  {
    "id": "DSGN_RBNDV2-W20-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~20",
    "surfaced_at": "2026-10-15T17:09:08Z",
    "one_line": "Three footer strings carry a lower-case qualifier after a comma ('Source: Black Diamond, holdings as of ...' at PositioningSummary.tsx:1606 and HoldingsTab.tsx:310; 'Source: ${provider}, as of ${asOf}.' at MethodAndSources.tsx:72); the rule was applied to the source name only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/Positioning/panels/PositioningSummary.tsx:1606 and portal/src/pages/Positioning/tabs/HoldingsTab.tsx:310 (portal@86db3d1b)",
        "portal/src/pages/InvestorReporting/tabs/reporting/MethodAndSources.tsx:72 (portal@86db3d1b)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-2 order: in the source name after Source:, every word starts with a capital letter, small words excepted.",
    "world_is": "The source-name segments (Black Diamond, Bloomberg, provider) obey the rule. The qualifier 'holdings as of' and ', as of' are not source names; a strict reading would print 'Holdings As of'. Not edited.",
    "notes": "Filed, not fixed. The qualifier reading is a ruling for the CVO."
  },
  {
    "id": "DSGN_RBNDV2-W20-S4",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~20",
    "surfaced_at": "2026-10-15T17:09:08Z",
    "one_line": "The order's premise says the portal worktree is branched from feature/dsgn-rbndv2-light at d0cb67d0; the worktree HEAD is 86db3d1b, one RV-y-1 drain above d0cb67d0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C portal/ rev-parse --short HEAD = 86db3d1b on branch wk-DSGN_RBNDV2-20-portal; git show -s --format=%s 86db3d1b = drain(DSGN_RBNDV2.TO-RV-y-1) merge of worker ~19",
        "d0cb67d0 is the difference-control base and is an ancestor of 86db3d1b (the before counts read git show d0cb67d0:<file>)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-y-2 order environment: the portal worktree branched from the feature branch at d0cb67d0, the difference-control base.",
    "world_is": "HEAD is one drain past d0cb67d0. The cell's edits sit on 86db3d1b; the difference against d0cb67d0 is the control only and does not change the verdict.",
    "notes": "No action taken; recorded so the drain reads the base correctly."
  },
  {
    "id": "DSGN_RBNDV2-W22-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~22",
    "surfaced_at": "2026-10-15T17:58:48Z",
    "one_line": "The order states the feature branch holds about 45 non-merge commits over ad7c100b; the measured count is 39 non-merge (59 total).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C ajb_wk/rbndv2-22/portal rev-list --count --no-merges ad7c100b..feature/dsgn-rbndv2-light = 39; rev-list --count ad7c100b..feature/dsgn-rbndv2-light = 59; feature tip 3509eae8",
        "git diff --name-only ad7c100b feature/dsgn-rbndv2-light = 89 files and git diff --name-only origin/PROD ad7c100b = 22 files, both as the order states"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell RV-z-1 facts measured at the cut: the feature branch holds about 45 non-merge commits (git rev-list --reverse --no-merges ad7c100b..feature/dsgn-rbndv2-light).",
    "world_is": "39 non-merge commits. All 39 replayed in order onto origin/PROD @33ad65ee with zero conflicts and zero empty picks; the candidate is 39 commits over PROD. The 89-file and 22-file figures match; the about-45 figure does not.",
    "notes": "Filed, not fixed. REHEARSAL_RECORD.md states the measured 39."
  },
  {
    "id": "DSGN_RBNDV2-W22-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~22",
    "surfaced_at": "2026-10-15T17:58:48Z",
    "one_line": "git worktree add of the PROD scratch worktree left a full bun install as a directory in node_modules, so the order's step-2 link was never in place.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls -ld ajb_wk/rbndv2-22/prod-baseline/node_modules showed a directory (drwx, 13:48) holding .bin and .tmp stamped 13:46 with 313 entries; ln -s to the shared install created no node_modules/node_modules link",
        "ajb_wk/rbndv2-22/portal/node_modules is a junction to ajb_workspace/portal/node_modules (cmd dir /AL)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell RV-z-1 step 2: link the scratch worktree node_modules the way the portal worktree has it (a junction to the shared one).",
    "world_is": "The worktree add left a real install. The install was renamed to node_modules.scratch-install (a move, no delete) and a junction to the shared install was made with mklink /J. The shared install was checked intact after the baseline run and after the junction was removed. The baseline typecheck ran against the shared install.",
    "notes": "Filed, not fixed. Cause not measured: whether a portal hook runs bun install on worktree add is unverified."
  },
  {
    "id": "DSGN_RBNDV2-W22-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~22",
    "surfaced_at": "2026-10-15T17:58:48Z",
    "one_line": "git worktree remove --force on the PROD scratch worktree failed with Filename too long after unregistering it; the directory stays untracked at ajb_wk/rbndv2-22/prod-baseline.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git -C ajb_wk/rbndv2-22/portal worktree remove --force ../prod-baseline returned: error: failed to delete .../prod-baseline: Filename too long; git worktree list then shows no baseline entry",
        "ls ajb_wk/rbndv2-22/prod-baseline shows the PROD source tree plus node_modules.scratch-install (286 top-level entries)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Cell RV-z-1 step 2: remove that scratch worktree (git worktree remove --force) after the baseline typecheck.",
    "world_is": "The residue is an untracked copy of PROD at 33ad65ee plus a bun install, and no git worktree tracks it. Deleting it is a recursive delete, which the autonomy rule holds for Andrew's word, so this worker did not delete it.",
    "notes": "Disposition for Andrew or the drain: remove the directory. Not blocking the rehearsal; no criterion reads it."
  },
  {
    "id": "DSGN_RBNDV2-W23-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~23",
    "surfaced_at": "2026-10-15T19:19:30Z",
    "one_line": "RV-b-1 as specified makes two existing dsgn-rbndv2 tests fail (RB1R-AC1 exact-scope rule count; RB1R2-AC1 bare-triple check on the five grounds); RB8B1-AC3 cannot read 0 fail without editing them, and the cell forbids that.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@e5588a8e src/index.css: an unlayered [data-panel-surface=\"light\"] background-color rule is added beside the palette block, so the exact-scope selector now sits outside every @layer twice; the :root [data-panel-surface=\"light\"] grounds now read var(--bg-panel)",
        "bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal: 39 pass, 2 fail, 41 tests; rb-1-r.remap.test.ts:140 'exact-scope rules outside @layer: 2'; rb-1-r2.surfaces.test.ts:162 '--semantic-background-contentPanel is not a bare H S% L% triple: var(--bg-panel)'",
        "a base-commit run of those two files was not measured in this worktree; the failure reasons name the two CSS blocks this cell changes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO RB8B1-AC3: every test under src/__tests__/dsgn-rbndv2/, src/ui/components/panels/ and src/ui/components/modal/ passes (summary 0 fail). Worker face: change nothing else in an existing test; the cell requires the unlayered scoped rule and the var(--bg-panel) grounds.",
    "world_is": "The two tests pin the pre-cell form of the two CSS blocks RV-b-1 changes, so their exact-count and bare-triple arms are false under the cell's own rule form. The paths grant covers the folder, but the face forbids editing those arms, so the worker left them untouched and did not weaken them.",
    "notes": "Not edited, not weakened. Disposition for the COO: amend RB1R-AC1 and RB1R2-AC1 to the RV-b-1 form, or re-scope RB8B1-AC3. Commit e5588a8e is LOCAL on wk-DSGN_RBNDV2-23-portal (not pushed)."
  },
  {
    "id": "DSGN_RBNDV2-W23-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~23",
    "surfaced_at": "2026-10-15T19:19:30Z",
    "one_line": "The worktree carries no org/surprise_channel/ tree, so the investigation item schema named in CLAUDE.md is not reachable from the worktree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls org/surprise_channel under C:/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-23 returned 'No such file or directory'; the worktree root HEAD is 3509eae8",
        "the workspace root C:/Users/AndrewBerman/Desktop/ajb_workspace/org/surprise_channel/schemas holds investigation_item.schema.json and remediation_row.schema.json (read only, not copied)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md section 2 and the worker face: a surprise row is appended per org/surprise_channel/schemas/investigation_item.schema.json.",
    "world_is": "The schema is present at the workspace root and absent from this worktree. The row was written by the schema's required-field list read from the workspace root, not from a worktree copy.",
    "notes": "Filed, not fixed. Cause not measured: whether the worktree was cut before org/surprise_channel landed is unverified."
  },
  {
    "id": "DSGN_RBNDV2-W23-S3",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~23",
    "surfaced_at": "2026-10-15T19:35:09Z",
    "one_line": "The issuer ruling on W23-S1 names two arms, but the same RB1R2-AC1 test also has control arm (c), checkOldRule, which counts exact-scope rules outside @layer as 1 and now reads 2; the ruling says change nothing else, so AC3 stays 1 fail.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@590307cd rb-1-r2.surfaces.test.ts: checkNewRule (the ruled arm) passes; checkOldRule (arm (c), line ~150) returns 'exact [data-panel-surface] rules outside @layer: 2'",
        "bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal: 40 pass, 1 fail, 719 expect() calls, 41 tests across 28 files; the one fail is INNER-SURFACES-OK (RB1R2-AC1) at rb-1-r2.surfaces.test.ts:173",
        "bun test rb-1-r.remap.test.ts (RB1R-AC1 with the ruled count 2): passes"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Issuer ruling on DSGN_RBNDV2-W23-S1 (order amend commit 3a3a890c9e): edit RB1R2-AC1 for the five grounds, change nothing else in either test. TO RB8B1-AC3: 0 fail across dsgn-rbndv2, panels and modal.",
    "world_is": "Arm (c) of RB1R2-AC1 pins the pre-cell count of exact-scope unlayered rules (1). The palette rule is still exactly one of the two such rules, so the control's intent holds, but its count arm reads the new rule. Under the ruling wording it is not in the authorized edit, so it was left untouched.",
    "notes": "Not edited. The minimal form the issuer may wish to rule on: checkOldRule selects the rule whose declarations include --palette-white (count 1 among those) instead of counting all exact-scope rules. Commit 590307cd is LOCAL on wk-DSGN_RBNDV2-23-portal."
  },
  {
    "id": "DSGN_RBNDV2-W24-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~24",
    "surfaced_at": "2026-10-15T20:03:52Z",
    "one_line": "RV-g-1 cannot meet RB8G1-AC3 as written: the body-prefixed selector the cell mandates fails the pinned rb-1-t.tokens.test.ts TOKENS-OK arm, which requires every selector of a block whose prelude contains the scope attribute to start with that scope or equal :root scope; that test is outside the order's paths, so the order stays open on AC3.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree wk-DSGN_RBNDV2-24-portal, src/index.css: git diff --stat reports 14 insertions in one file; the only added rule is body [data-panel-surface=\"light\"] with --success 145 70% 26% and --danger 352 75% 42%",
        "portal/src/__tests__/dsgn-rbndv2/rb-1-t.tokens.test.ts lines 98-103: blocks.filter(b => b.prelude.includes(SCOPE)), then each selector must startWith(SCOPE) or equal ':root ' + SCOPE; the body-prefixed selector fails that expect (bun test, TOKENS-OK, 1 fail)",
        "bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal: 41 pass, 1 fail, 42 tests across 29 files; the fail is RB1T-AC1 TOKENS-OK; RB8G1 SIGNAL-PAIR-OK passes; bun x tsc -p tsconfig.app.json --noEmit rc=0"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RV-g-1 cell: the selector is body [data-panel-surface=\"light\"], deliberately not :root [data-panel-surface=\"light\"] or the bare scope, because rb-1-r2.surfaces.test.ts and rb-1-r.remap.test.ts pin the count of those exact selectors. RB8G1-AC3: bun test over dsgn-rbndv2, panels and modal reads 0 fail. Refusal clause: do not weaken a test to pass.",
    "world_is": "rb-1-t.tokens.test.ts also pins the scope-prefix form for every block whose prelude contains the scope attribute, and that pin is not in the cell's list of pinned tests, so no body-prefixed selector can pass it. The RV-g-1 edit is committed exactly as the cell writes it; the test was not edited (outside the order's paths) and no selector was substituted (the cell fixes it).",
    "notes": "For the issuer to rule on. The cell's own pin list (rb-1-r2, rb-1-r.remap) does not name rb-1-t.tokens.test.ts. Commit of the RV-g-1 change is LOCAL on wk-DSGN_RBNDV2-24-portal; the order's status stays pending."
  },
  {
    "id": "DSGN_RBNDV2-W25-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~25",
    "surfaced_at": "2026-10-15T20:39:22Z",
    "one_line": "RB8N1-AC3 cannot pass as written: the mandated nested-ground selector has commas inside :is(), and the pinned rb-1-t.tokens.test.ts TOKENS-OK arm (c) splits every scoped prelude on commas, so the :is() pieces fail its scope-prefix pin; that test is outside the order's two named tests, so AC3 stays red and the order stays open.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@5211a15d src/index.css: the second-layer rule sits unlayered after the :root [data-panel-surface=\"light\"] inner-surface block; its selector is the scope attribute, then :is(four item-ground classes), then :is(the same four), exactly as the cell mandates",
        "portal/src/__tests__/dsgn-rbndv2/rb-1-t.tokens.test.ts lines 98-104 (unchanged at ca146d09): scoped = blocks whose prelude includes the scope; selectorsOf(prelude) = prelude.split(',') and every piece must start with the scope or equal ':root' + scope; the failing expect is line 103",
        "bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal (portal@5211a15d, run 3): 42 pass, 1 fail, 644 expect() calls, 43 tests across 30 files; the fail is RB1T-AC1 TOKENS-OK at rb-1-t.tokens.test.ts:103, expect(received).toBe(expected), Expected true, Received false",
        "precedent: DSGN_RBNDV2-W24-S1 records the same rb-1-t arm blocking RV-g-1; the issuer ruling there re-authored that selector"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB8N1-AC3: every test under src/__tests__/dsgn-rbndv2/, src/ui/components/panels/ and src/ui/components/modal/ passes: the summary line reads 0 fail. Refusal clause: if a criterion cannot be met as written, stop and write a surprise row; do not weaken the test to pass. The order names edits only to rb-1-r2 (the RB1R2-AC1 grounds) and rb-8-b1 (its arm 4).",
    "world_is": "The mandated selector begins with the scope attribute, but its inner commas (inside :is()) are read by the rb-1-t naive comma split as separate selectors without the scope prefix, so arm (c) of TOKENS-OK fails at line 103 on the first scoped block. rb-1-t was left untouched (the order does not name it); no selector was substituted (the order fixes it).",
    "notes": "For the issuer to rule on. Two forms the issuer may weigh: the arm splits on top-level commas only (the form the rb-1-r2 checkOldRule ruling took), or the selector is written as comma-free per-pair selectors that each begin with the scope attribute. Commit 5211a15d is LOCAL on wk-DSGN_RBNDV2-25-portal; the order's status stays open."
  },
  {
    "id": "DSGN_RBNDV2-W25-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~25",
    "surfaced_at": "2026-10-15T20:39:22Z",
    "one_line": "RB6Y1-AC1 failed once in the AC3 suite run: a test reported 5016.00 ms and failed on a git show read; the same test passes alone and passed in the next full run, so the suite is not deterministic under load.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal, second run (portal@5211a15d): 41 pass, 2 fail, 43 tests across 30 files; RB6Y1-AC1 arm (a), the Trending Topics row in ExecutiveSummary.tsx holds no border-white, failed at 5016.00 ms with a git show of d0cb67d0:src/pages/MarketPerformance/tabs/types.ts reported as the failing command",
        "bun test src/__tests__/dsgn-rbndv2/rb-6-y1.border-sweep.test.ts run alone twice (portal@5211a15d): 7 pass, 0 fail on both runs",
        "full suite runs 3 and 4 (portal@5211a15d): RB6Y1 passed in both; the only fail in each was RB1T-AC1 (DSGN_RBNDV2-W25-S1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB8N1-AC3: bun test over src/__tests__/dsgn-rbndv2, src/ui/components/panels and src/ui/components/modal reads 0 fail, as a re-runnable invocation with a deterministic verdict.",
    "world_is": "One of four full suite runs failed RB6Y1-AC1 on a timed test that shells out to git show; the RB6Y1 file passed alone twice and in the other full runs. The cause of the one timeout was not measured. The invocation's verdict therefore varied between runs.",
    "notes": "Not edited. The RB6Y1 test file and its git show reads are outside this cell's changed files and were not touched. Observed on the worktree wk-DSGN_RBNDV2-25-portal."
  },
  {
    "id": "DSGN_RBNDV2-W26-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~26",
    "surfaced_at": "2026-10-15T21:09:13Z",
    "one_line": "The RV-g-2 criterion RB8G2-AC2 names the scratch path /tmp/rb8g2-tsc.txt, while the worker face fixes scratch to <worktree>/.scratch/ only; the criterion's invocation was run as written, into /tmp, and the order is unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-g-2.delta-pair.md (worker face, ACCEPTANCE, RB8G2-AC2): the invocation writes its output to /tmp/rb8g2-tsc.txt",
        "same order, worker face, Scratch clause: scratch is <your worktree>/.scratch/ only, and sibling workers overwrite each other under the shared scratchpad",
        "run at portal@5fcb37f5: the criterion invocation as written exits TSC-RC=0 with 0 diagnostic lines; a first run into the worktree scratch file also exited 0 and was not kept as the recorded invocation"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Scratch: <worktree>/.scratch/ only (worker face). RB8G2-AC2: the typecheck invocation writes to /tmp/rb8g2-tsc.txt.",
    "world_is": "The two instructions name different scratch locations. The criterion's invocation is the verdict's instrument and was run unchanged into /tmp; the worktree scratch rule was not applied to this one file. The verdict (TSC-RC=0, 0 diagnostic lines) is unaffected by the path.",
    "notes": "For the issuer to rule on whether the criterion should name the worktree scratch path. Not edited; the order stays as issued."
  },
  {
    "id": "DSGN_RBNDV2-W27-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~27",
    "surfaced_at": "2026-10-15T21:42:05Z",
    "one_line": "The RV-o-1 criterion RB9O1-AC2 names the scratch path /tmp/rb9o1-tsc.txt, while the worker face fixes scratch to <worktree>/.scratch/ only; the criterion's invocation was run as written, into /tmp, and the order is unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-o-1.outlines.md (worker face, ACCEPTANCE, RB9O1-AC2): the invocation writes its output to /tmp/rb9o1-tsc.txt",
        "same order, worker face, Scratch clause: scratch is <your worktree>/.scratch/ only, and sibling workers overwrite each other under the shared scratchpad",
        "same conflict already filed for the RV-g-2 order as DSGN_RBNDV2-W26-S1 (this file, 2026-10-15T21:09:13Z); run at portal@d52fc657: the criterion invocation as written exits TSC-RC=0 with 0 diagnostic lines"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Scratch: <worktree>/.scratch/ only (worker face). RB9O1-AC2: the typecheck invocation writes to /tmp/rb9o1-tsc.txt.",
    "world_is": "The two instructions name different scratch locations. The criterion's invocation is the verdict's instrument and was run unchanged into /tmp; the worktree scratch rule was not applied to this one file. The verdict (TSC-RC=0, 0 diagnostic lines) is unaffected by the path.",
    "notes": "For the issuer to rule on whether the criterion should name the worktree scratch path. Not edited; the order stays as issued. Filed on the same pattern as DSGN_RBNDV2-W26-S1."
  },
  {
    "id": "DSGN_RBNDV2-W27-S2",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~27",
    "surfaced_at": "2026-10-15T21:42:05Z",
    "one_line": "NestedCard.tsx's header says a section has no border, no fill, no radius and no left accent bar, and that data-accent sets no visual; after RV-o-1 a light-scope rule on [data-accent] paints an outline and an accent bar, so that header is stale.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@e88ffb03 src/ui/components/panels/NestedCard.tsx header lines 4 and 6: 'no border, no fill, no radius, no left accent bar' and 'accentColor ... sets the data-accent attribute and no visual'",
        "portal@d52fc657 src/index.css: the unlayered block after the second-layer silver rule, [data-panel-surface=\"light\"] [data-accent] { border: 1px solid hsl(var(--hairline)); border-radius: 3px } and four border-left accent selectors",
        "the cell bounds NestedCard.tsx out of this order's write surface, so the header was not edited"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "NestedCard.tsx header (e88ffb03, lines 4 and 6): a section has no border, no fill, no radius and no left accent bar; data-accent sets no visual. RV-o-1: the outline and the bars are CSS on data-accent, and NestedCard is not edited.",
    "world_is": "The CSS on data-accent now supplies the outline and the bars on a light panel, so the component's header describes a state the light panel no longer shows. Nothing in the test suite reads that header; rb-2-i1 pins only that NestedCard carries no visual class.",
    "notes": "Not edited (outside this order's paths). For the issuer to rule whether the header is corrected in a later cell. A future reader relying on the header to conclude that data-accent is visually inert would be misled; no present behaviour is wrong."
  },
  {
    "id": "DSGN_RBNDV2-W28-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~28",
    "surfaced_at": "2026-10-15T23:04:55Z",
    "one_line": "The order says to commit the portal files inside portal but gives no commit path for them: the portal repo carries no .tools/, so the commit ran through the workspace safe-commit.sh with the portal as the working directory, and the pre-commit gate graded 0 of 2 files.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree wk-DSGN_RBNDV2-28-portal: no .tools/ directory at its root; the workspace worktree rbndv2-28/.tools/safe-commit.sh was invoked from the portal cwd with -- paths relative to the portal",
        "the portal commit cc368d50 on wk-DSGN_RBNDV2-28-portal (LOCAL) carries PanelHeader.tsx and rb-10-q1.helpicon.test.ts; the pre-commit output printed 'commit-gate checked 0 of 2 file(s)' and a risk-reflex WARN that the baked comp-pulse path was used",
        "the order's BOUNDS paragraph: 'commit workspace files through .tools/safe-commit.sh; commit the portal files inside portal on your worktree branch'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "BOUNDS: commit workspace files through .tools/safe-commit.sh; commit the portal files inside /c/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-28/portal on the worktree branch. Environment: the portal worktree is a separate repo.",
    "world_is": "The portal repo has no .tools/ of its own, so the only safe-commit available is the workspace copy, run with the portal as cwd. It worked (commit cc368d50, author set, message verified MATCH), but the commit-gate reports NOTHING CHECKED for a .tsx file, so the gate adds no evidence to a portal commit and the tsc criterion carries the typecheck instead.",
    "notes": "Not worked around beyond the single invocation. For the issuer to rule which safe-commit a portal commit should use. The order did not name the instrument for portal files; the one used is recorded here, not assumed to be the intended one."
  },
  {
    "id": "DSGN_RBNDV2-W29-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~29",
    "surfaced_at": "2026-10-15T23:05:53Z",
    "one_line": "The order names no commit tool for the portal repo; the portal worktree is its own git repo with no .tools directory, so I committed the portal files with the root worktree's ../.tools/safe-commit.sh run from the portal directory, and its risk-reflex and naming-gate fell back to workspace-root copies.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal worktree git rev-parse --show-toplevel = C:/Users/AndrewBerman/Desktop/ajb_wk/rbndv2-29/portal, a separate repo on branch wk-DSGN_RBNDV2-29-portal; ls of portal/.tools returned no such directory; ../.tools/safe-commit.sh exists in the root worktree",
        "safe-commit output at portal commit c2e0802f: 'risk-reflex WARN: comp-pulse: the caller toplevel ... carries no .tools/comp-pulse -- EXECUTING THE BAKED PATH C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/comp-pulse'; commit-gate 'checked 0 of 2 file(s) -- NOTHING WAS CHECKED' for the .tsx and .ts files",
        "the commit's test and typecheck evidence was taken separately: bun test rb-10-r1 (VERDICT: SPOTLIGHT-OUTLINES-OK), tsc -p tsconfig.app.json rc=0, and the panels, modal and market-performance run with 0 fail"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Bounds of RV-r-1: commit workspace files through .tools/safe-commit.sh; commit the portal files inside the portal worktree on the worktree branch. The order names no safe-commit path for the portal repo.",
    "world_is": "The portal repo carries no .tools of its own. The only safe-commit is the root worktree's ../.tools/safe-commit.sh, which I ran from inside the portal directory. The commit-gate graded 0 of 2 files because it reads only .py, .sh, .tf and org/projects/*.json, and the risk-reflex used the baked workspace-root comp-pulse path.",
    "notes": "Not changed: the commit landed on the portal worktree branch as c2e0802f. For the issuer to say which tool and gate a portal-repo commit is to name. No gate hazard is present on this commit; the test and typecheck instruments ran on the committed bytes."
  },
  {
    "id": "DSGN_RBNDV2-W31-S1",
    "project": "DSGN_RBNDV2",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_DSGN_RBNDV2~31",
    "surfaced_at": "2026-10-16T00:07:40Z",
    "one_line": "The RV-t-1 change to RankedRow's root class turns the round-10 test rb-10-r1 red: its arm (d) pins RankedRow to its text at 4299f28a, so RB11T1-AC3 (every dsgn-rbndv2 test 0 fail) cannot hold as written.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~RB",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal@728aa979 (branch wk-DSGN_RBNDV2-31-portal): RankedRow root class gains border border-[hsl(var(--hairline))]; the RV-t-1 cell is the only change to that function",
        "portal/src/__tests__/dsgn-rbndv2/rb-10-r1.spotlight.test.ts at portal@728aa979, arm (d): RankedRow text must equal its text at git show 4299f28a; the test body is unchanged by this cell",
        "bun test src/__tests__/dsgn-rbndv2/rb-10-r1.spotlight.test.ts after the edit: '(d) RankedRow differs from its text at the base ref' and 1 fail; the same file passed before the edit",
        "bun test src/__tests__/dsgn-rbndv2 src/ui/components/panels src/ui/components/modal src/components/market-performance: 57 pass, 1 fail, rc=1; the failing test is RB10R1-AC1 spotlight outlines and canonical labels",
        "git diff --stat 4299f28a HEAD -- src/components/market-performance/RSIModal.tsx shows changes since 4299f28a, yet the RankedRow arm passed at the feature tip before this edit, so RankedRow was unchanged until RV-t-1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RB11T1-AC3: bun test over src/__tests__/dsgn-rbndv2, src/ui/components/panels, src/ui/components/modal and src/components/market-performance reads 0 fail. RB10R1-AC1 arm (d): RankedRow text equals its text at 4299f28a.",
    "world_is": "The two criteria cannot both hold on this branch. RV-t-1 requires the RankedRow class change, which is the exact text rb-10-r1 pins. The change is in place as ordered; rb-10-r1 is red on the worktree branch and so the dsgn-rbndv2 folder is red on it until the pin is moved or the cell is re-ruled.",
    "notes": "Not edited: rb-10-r1 is a prior round's test, outside this cell's change. Re-pinning its arm (d) to the new RankedRow text, or dropping the arm, is a decision for the issuer and not a weakening I would make on my own. RB11T1-AC3 is recorded FAIL; the order stays open. The RV-t-1 commit is 728aa979 on wk-DSGN_RBNDV2-31-portal."
  }
]
```
