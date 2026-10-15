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
  }
]
```
