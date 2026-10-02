# DSGN_AMGTV1 task order -- `AV-zg-2` -- THE HEADER IS ONE LIGHT FACE, AT REST IN THE BOOK ORDER; ITS KEY FIGURES READ ONCE, FORMATTED AND DATED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zg-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~81</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from the round-14/15 served fixtures (BA, VLO, 6501).
comp-adversary: RUN by the issuer at the cut on portal dcdc89b1 (= DEV ec65c5d6 for src/pages/SecurityAnalysis) -- face.cjs 2 of 4, figures.cjs 1 of 4 (FAIL as expected; CONTROL and PLANTED arms pass by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zg-2` (round 29, decomposition v29; serves FWD-12 (the header) and FWD-27 (the header))

PRD `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` FWD-12 (~186-201), FWD-24 (~345-357, which must keep passing) and FWD-27
(~387-402); register rows SAUX-02, 03, 04, 05, 15, plus SAUX-30 ("Back to universe", "Export rich text (.md)"), 31 (the card empty
lines) and 33/34 on the header (`docs/briefs/amgt-security-analysis-ui-findings-20261002.json`). CTO fold ruling 1: LIGHT, the
/philosophy GraphicCard face (`pages/CapitalMarketAssumptions/components/PhilosophyPillars.tsx`), in the /advisor-intelligence /book L0
order.

Build (the checks grade exactly this):
1. **Hooks.**
   - New: `data-key-figures` (ONE element, the root of the key-figure row) and `data-header-action="back"`.
   - Refresh: `data-header-action="refresh"`, or keep `data-primary-action="refresh"`. Optional: `data-empty-state`.
   - Keep: `data-identity-card`, `data-identity-name` (before the ticker), `data-header-posture`, `data-header-dossier-position`,
     `data-header-reading="chatter"`, `data-axis-footnote`, a label whose own text is exactly `Breakout (price)`, and FigureTooltip's
     `[role="tooltip"][data-mnemonic]` with `data-full-value`.
2. **Ground (FWD-12, SAUX-02, 05).** All four header states (loaded, loading, error, no data) sit on `Panel variant="nested"` or another
   white surface, never `mixed`, `chart` or `dark-band`. Navy fill appears only inside GraphicCard's own panel. `text-white` or
   `palette-white`/`palette-mediumGray` ink only on a dark ground, so the `data-identity-name` div becomes navy. Buttons use
   `buttonClass(kind, 'canvas', ...)`; Refresh is secondary, or primary on the white panel.
3. **Order at rest (SAUX-15).** In `components/SecurityOverlay.tsx`:
   - The order is: identity, then `[data-key-figures]`, then `<HeaderBrief bundle={bundle} />` with NO `postureLine` prop, then
     `<TimelinePanel securityKey={bundle.security_key} />`. Cell `AV-zg-1` owns both components; it makes HeaderBrief the recent-news
     card and stops it mounting a timeline of its own.
   - After those, a closed native `<details>` with a reader-words `<summary>` holds the posture line (exactly one), the dossier line, the
     readings grid and the axis footnote. No other text is visible at rest.
   - "identity as of" prints at most once across the header and `IdentityLine` (e.g. IdentityLine keeps only its data attributes).
4. **FWD-24 stays.** Keep the breakout cell (`#rank | +pct.toFixed(2)%, up/down N places`) and the footnote as they are. The header never
   says "today", "not served", "unsupported", "ABSENT" or "REFUSED".
5. **Key figures, once (SAUX-03).** Each of PX_LAST, CUR_MKT_CAP, CURR_ENTP_VAL, NET_DEBT, EQY_BETA, VOLUME_AVG_30D and
   SI_PERCENT_EQUITY_FLOAT (or SHORT_INT_RATIO) shows exactly ONCE across the header and every `HeaderCardDetail` render, if that export
   remains. A shown figure is the element that is FigureTooltip's direct parent. Keep exporting `HeaderCardDetail`:
   `__harness__/exportCompare.harness.cjs` imports it.
6. **Tooltips (SAUX-04).** Header tooltip rows are built locally. They carry the formatted value, the as-of date, the source as
   "Bloomberg" in words, and `data-full-value` = `String(value)`. No raw number and no source id (`bloomberg-dapi`) shows on the face.
   This settles FWD-13 against SAUX-04: the full-precision value travels in `data-full-value`.
7. **Money and dates (SAUX-33, 34; issuer ruling a).** Money prints as `<figure.currency> <n>`, never with `$`, and the market-cap element
   shows its vintage date in words.
8. **No-source lines (SAUX-31).** A figure with no source prints nothing: drop the `emptyLine` text and "is not in the data yet". When no key
   figure is served, `[data-key-figures]` still renders and holds exactly ONE PanelEmpty, EmptyState or `[data-empty-state]`.
9. **Words (SAUX-30).** PrintExportAction keeps its 2 buttons, and neither says "rich text" or ".md". The back control carries
   `data-header-action="back"` and reader words, not "Back to universe".
10. **Shared exports (issuer ruling).**
   - `components/StatTile.tsx` keeps `FigureTooltip` (props), `formatStatValue(value, format, currency, unit)` returning a string, and
     `figureTooltipRows(figure)` returning `{label, value}[]`; keep its verbatim value row (round-21 `tipface.cjs` reads it). Cell
     `AV-zg-5` (Model) imports all three. The money rule may change `formatStatValue`'s output, not its signature.
   - `constants.ts` keeps `HEADER_CARD_DEFS`, `STAT_TILE_DEFS`, `IDENTITY_CURRENCY_MNEMONIC` and `StatTileFormat` by name; ModelTab imports
     them.
11. **`__harness__/shell.harness.cjs`, five clauses re-anchored (issuer grant).** Change ONLY these clauses:
   - `security_band_count` and `universe_band_count` become FWD-20 v0.9's band clause, `bandContainersTopLevel <= 1`. That clause must
     pass with the Lead Panel still dark (your tree) AND light (cell `AV-zg-3`, merged later).
   - `back_to_universe_present` becomes the back control with `data-header-action="back"` in reader words.
   - `header_cards==4` becomes ONE `[data-key-figures]` row.
   - `card_window_carries_provenance` becomes: each figure's tooltip carries its source in words and `data-full-value`.
   Each re-anchored clause must still FAIL on a planted page that breaks it; show one planted run in your report.

**Contracts:** C-PRESENTATION-ONLY. C-FRIDAY: the served currency as served. Design law: a code may sit in a data attribute, never in
visible or tooltip text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; in the harness file only the five named clauses change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/SecurityOverlay.tsx
portal/src/pages/SecurityAnalysis/components/HeaderCards.tsx
portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx
portal/src/pages/SecurityAnalysis/components/StatTile.tsx
portal/src/pages/SecurityAnalysis/components/PrintExportAction.tsx
portal/src/pages/SecurityAnalysis/constants.ts
portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~81/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zg-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/header/face.cjs"; echo "exit=$?"</invocation><expect>THE HEADER IS ONE LIGHT FACE, AT REST IN THE BOOK ORDER: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zg-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/header/figures.cjs"; echo "exit=$?"</invocation><expect>THE KEY FIGURES READ ONCE, FORMATTED, DATED, IN READER WORDS: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zg-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)"; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (0 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~81/DSGN_AMGTV1.TO-AV-zg-2.header-one-light-face-in-book-order.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W81-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, the five re-anchored clauses
with their planted-failure runs, and any row. If a battery item OWNED BY ANOTHER CELL turns red in your tree, file a surprise row and
report it as BLOCKING; do not edit that file.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Not graded by the checks (L9 PNG read): the hairline and navy look and its likeness to /philosophy; the tooltip style;
SAUX-15's 1440x900 first-viewport limb; the details control's place and words; the description and Social lines (HeaderBrief, `AV-zg-1`);
a figure inside a closed dialog not rendered through `HeaderCardDetail`; money format for a figure with no currency of its own (every
fixture carries one). In this worker's own tree HeaderBrief still mounts a timeline, so two timelines render until `AV-zg-1` merges; the
checks stub HeaderBrief.

<status>complete</status>
<round>29</round>
<slot>~81</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
