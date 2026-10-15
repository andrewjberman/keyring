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
  }
]
```
