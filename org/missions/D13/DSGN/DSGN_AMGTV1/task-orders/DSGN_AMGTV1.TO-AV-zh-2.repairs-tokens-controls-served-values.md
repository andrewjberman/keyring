# DSGN_AMGTV1 task order -- `AV-zh-2` -- REPAIRS: THE PAGE WEARS THE ESTATE'S OWN TOKENS AND CONTROLS; A SERVED VALUE PRINTS AS SERVED; THE TABS START IN THE FIRST VIEWPORT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zh-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~87</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from captured and planted fixtures.
comp-adversary: RUN by the issuer at the cut on portal e370eb7c (the CTO-approved round-29 candidate) -- chrome.cjs 1 of 4, served.cjs 1 of 3 (FAIL as expected; PLANTED arms pass by design). The issuer's amended round-29 face.cjs and dayopen.cjs read 4 of 4 at that base.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zh-2` (round 30, decomposition v30; serves FWD-12, FWD-23, FWD-27 and FWD-5's chrome)

A batched repair cell. Its sources:
- the CTO's round-29 review (msg 28820, FWD-23);
- rows `DSGN_AMGTV1-Z-W81-S1` and `Z-W81-S3`;
- 2.0.0_SA_COO~Z's msg 28802 (RESAPP row Z-W212-S2);
- the CTO's msg 28833 (from CVO~Z v33).

No new `data-*` hooks. The checks read existing ones: `data-header-action="refresh"|"back"`, `data-bubble`, `data-tone-legend`,
`data-feed-item`, `data-what-changed-row`, `data-what-changed-cell="before"|"after"`.

Build:
1. **The no-tone fill becomes a token (FWD-23: "0 hard-coded hex in the panel's chart files").**
   - **`portal/src/lib/chartColors.ts`:** add exactly ONE new top-level export holding the no-tone fill string, e.g.
     `export const CHATTER_NO_TONE_FILL = '#cbd5e1'`. All 44 existing exports stay value-identical. Do not add a key to `PALETTE`. Every
     page reads this file, so the change is additive only.
   - **`components/ChatterBubbles.tsx`:** import the token on an `import { ... } from '../../../lib/chartColors'` line. The bubble fill
     and the legend swatch both use it. No hex, `rgb()` or `hsl()` with numeric channels in any string, template or JSX text (comments
     are not graded). Keep the `getSentimentColor` import line unchanged and add no bare-package import.
2. **Refresh wears the canonical primary class (row Z-W81-S1).** In `components/SecurityOverlay.tsx`:
   - Refresh is `buttonClass('primary', 'canvas', 'sm')`. A 4th argument may carry only non-paint tokens (no `text-`, `bg-`, `border-`,
     `fill-` or `stroke-`).
   - Keep `data-header-action="refresh"` and `data-primary-action="refresh"`.
   - No line of the file, comments included, contains `hsl(0 0% 100%)` in any separator, or `text-[#fff|#ffffff|white|rgb(255 255 255)]`.
   - The issuer's round-29 `face.cjs` is amended: white ink on a primary button's OWN fill is legal, and white ink on a white ground in any
     spelling is caught. So the workaround is no longer needed.
3. **The render check reads the back control by its hook (row Z-W81-S3).** In `__rendercheck__/renderCheck.tsx`:
   - Keep `readRoute(path, html)` a top-level function using only top-level string or regex constants.
   - `persistentPanelPresent = html.includes('Lead Panel') || html.includes('data-header-action="back"')`.
   - No string literal reads "Back to universe".
4. **A feed item links only where a url is served (RESAPP Z-W212-S2).** After RESAPP's next redeploy the overlay feed serves `url: null`. In
   `components/HeaderBrief.tsx`:
   - A non-empty `item.url` keeps `<a href={item.url} target="_blank" rel="noreferrer">` around the title.
   - Otherwise the title prints as plain text with no `<a>`. Each row keeps `data-feed-item` and its title.
   - Keep everything the issuer's amended round-29 `dayopen.cjs` reads: one `[data-header-feed]`, the description in a closed `<details>`
     with a words summary, no timeline of its own, `postureLine` ignored.
5. **What changed prints at display precision (FWD-27).** Served compare values print unrounded today ("2.9039 -> 3.036"). In
   `components/model/WhatChangedPanel.tsx`:
   - Header-map figures stay on `formatStatValue`.
   - Any other numeric value prints `formatSheetValue(type, n)`. `type` is the `FINANCIAL_SUMMARY_ROWS` / `MARGIN_HISTORY_ROWS` row's type
     for the mnemonic, or for the row whose label `FORECAST_MNEMONICS` maps to it; otherwise undefined (2 places, grouped).
   - Examples: SHORT_INT_RATIO "2.90" -> "3.04"; IS_EPS "3.46"; PE_RATIO "23.5x"; EBITDA_MARGIN "12.3%"; EBITDA "1,234,568".
   - The full values stay in the closed "Full figures" details.
   - The round-29 `whatchanged.cjs` must keep passing; its pct rule reads the precision shown.
6. **The first tab panel starts inside the first viewport (SAUX-15).** At 1440x900 on BA, the first tab panel must start above y=900;
   today it starts at about y=989. Cut at least 90 px of the stack above the tabs, and more for a name with several news items: each extra
   open news item adds about 45 px, and the Expand line about 21 px.
   - Measured at base (walk shot 005):
     - title band: 140 px (page shell, not yours);
     - identity block: 41 + 109 px (SecurityOverlay);
     - key figures: 75 px (HeaderCards, not yours);
     - "About the company" + news card + padding: 24 + 91 + 24 px (HeaderBrief);
     - timeline: about 283 px (`TimelinePanel.tsx`, yours this round);
     - posture details summary: 26 px;
     - gaps and padding: 64 + 16 px (SecurityOverlay);
     - tab bar: 99 px (page shell).
   - Options inside your files: a tighter identity card and gaps; at most 2 open news items at rest, with the rest on demand (the
     existing Expand); and the chart down toward FWD-5's 200 px floor. The round-29 `chart.cjs` requires >= 200 px.
   - Graded at the issuer's close walk by the tab bar's measured y; there is no check for it here.

**Contracts:** C-PRESENTATION-ONLY. A served value is formatted, never changed: rounding is display precision. Served drafted prose
("$2.9 billion") stays as served, by CTO ruling (b), msg 28836.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; in `chartColors.ts` only the one new export is added.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file. The base worktree's
   files may be CRLF; keep each file's existing line endings.

## 3. SURFACES

<paths>
portal/src/lib/chartColors.ts
portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/__rendercheck__/renderCheck.tsx
portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx
portal/src/pages/SecurityAnalysis/components/model/WhatChangedPanel.tsx
portal/src/pages/SecurityAnalysis/components/TimelinePanel.tsx
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~87/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round30/` and `round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round30/checks/repairs/chrome.cjs"; echo "exit=$?"</invocation><expect>THE PAGE WEARS THE ESTATE'S OWN TOKENS AND CONTROLS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round30/checks/repairs/served.cjs"; echo "exit=$?"</invocation><expect>A SERVED VALUE PRINTS AS SERVED: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zh-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 and AC2 also run the round-29 checks that read your files (tone, collage, face, figures, dayopen, whatchanged, etwords) and need
each to exit 0.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~87/DSGN_AMGTV1.TO-AV-zh-2.repairs-tokens-controls-served-values.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W87-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, the height you removed above
the tabs (block by block), and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Not graded** (L9 PNG read): how a null-url title looks (it must not look like a link); the Change column's precision; how the
  compaction looks, and the tab-bar y itself (measured at the close walk); the no-tone colour's appearance.
- **Check limits:** the renderCheck repair is lexical; `runRenderCheck` has no consumer. The FWD-26 presets cell will later touch
  ChatterBubbles.tsx and is sequenced after this one.
- **Issuer amendments landed with this issuance:** round29/checks/header/face.cjs (primary ink judged by its own fill; white caught in
  every spelling) and round29/checks/timeline/dayopen.cjs (an href only where a url is served).

<status>pending</status>
<round>30</round>
<slot>~87</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
