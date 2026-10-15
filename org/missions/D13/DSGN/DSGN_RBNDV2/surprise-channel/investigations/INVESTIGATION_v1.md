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
    }
]
```
