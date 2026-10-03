# DSGN_AMGTV1 task order -- `AV-zg-3` -- THE LEAD PANEL IS ONE LIGHT CARD; THE PRICE FACE SHOWS THE TOP MOVERS AND NAMES ITS WINDOW

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_AMGTV1/decompositions/DSGN_AMGTV1_DECOMP.md</decomp_doc>
<owned_cells>AV-zg-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_DSGN_AMGTV1~82</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the checks render page sources statically from a served capture (Opal's own scoped API, read by the issuer's agent) and planted fixtures.
comp-adversary: RUN by the issuer at the cut on portal dcdc89b1 (= DEV ec65c5d6 for src/pages/SecurityAnalysis) -- pricemovers.cjs 1 of 4, leadface.cjs 1 of 3 (FAIL as expected; PLANTED arms pass by design).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `AV-zg-3` (round 29, decomposition v29; serves FWD-12 (the Lead Panel), FWD-22, FWD-26's price caption, FWD-27)

PRD `org/missions/D13/DSGN/DSGN_AMGTV1/prd/DSGN_AMGTV1_PRD.md` FWD-12 (~186-201), FWD-22 (~317-329), FWD-26 (~375-385, the caption
only) and FWD-27 (~387-402); register rows SAUX-01, 20, 21, 36 and SAUX-30's page subtitle
(`docs/briefs/amgt-security-analysis-ui-findings-20261002.json`). CTO fold rulings 1 (LIGHT) and 3 (10 gainers + 10 losers at rest, the
full list in the same panel). The 30/90/365 presets are NOT this round: the month cursor stays. The served price capture is
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/fixtures/leadprice/rankings.trending.price.live.json` (94 rows,
`window_days` 30, as_of 2026-10-01).

Build (the checks grade exactly this):
1. **`components/LeadPanel.tsx`**, rendered on both faces:
   - **Root:** a white bordered panel, `Panel variant="nested"` or the GraphicCard root. The header stays the GraphicCard.
   - **No band anywhere in the render:** no `dark-band` class and no `--bg-band/header/medium/card` or `contentPanel` background. That
     rules out Panel `chart`/`mixed`, PanelHeader, PanelFooter, SmartPanelFooter, DarkCard, NestedCard and SectionCard.
   - **Light ink only inside the GraphicPanel (navy top):** `text-white*`, `--palette-white`, `--palette-mediumGray`, `#E8ECF5`, `#A8B0C0`,
     `text-<colour>-50..300` and `bg-white/N`, including their `hover:`/`focus:`/`placeholder:` forms. No white fill sits inside the
     GraphicPanel. The bar labels and values, the unserved line, the footer wrapper and the ResolutionNote line take navy ink.
   - **Chatter face:** still passes ChatterBubbles a `month` and an `onMonthChange` function, so the month cursor stays.
2. **`components/GenerationCaption.tsx`, the Details disclosure (SAUX-36).** Keep exactly one `data-source-caption="detail"` element. It
   contains the as_of_date in words (`dateWords.longDate`, e.g. "October 1st, 2026") and the word "Bloomberg". It contains NO
   generation id; none of the words "generation", "row(s)", "vintage" or "pointer"; no "state X" or status code (COMPLETE, SERVED,
   SHORT_READ and the rest), on a served payload or a SHORT_READ one; and none of the vendor client strings (bloomberg-dapi, boxside,
   blp_client, 127.0.0.1). `data-generation-id` may stay as a data attribute.
3. **`SecurityAnalysis.tsx` (SAUX-30).** The `PageHeaderCleanBadge` `description` is at least three words. It contains no "universe",
   "discovery", "server-side" or "per-name", no " / " list, and no code-shaped token.
4. **`components/PriceBars.tsx`** and the Price face (SAUX-20, 21):
   - **Bars:** every bar keeps `data-price-bar="<security_key|ticker>"` and its own `title` with the served name and the ticker.
   - **At rest:** the 10 largest gainers (largest first) and the 10 largest losers (most negative first); a side with fewer than 10
     shows all it has. Bars not shown are not rendered, or sit inside a closed native `<details>`, never hidden by CSS.
   - **Expand control:** one native `<button type="button" data-price-expand aria-expanded={open}>` with visible words, or a
     `<summary>`; not an estate Button or Segmented, whose stubs drop attributes. Its state lives in `useState`/`useReducer`. A click
     shows every served bar in the same panel, each side longest first; a second click returns to the 20.
   - **Window caption:** one `data-price-window` element reading "Change over the last {window_days} days to {longDate(as_of_date)}",
     from the served fields. When `window_days` is not served, it names no day count. No other day count appears on the face: the
     hard-coded "over 30 days" in the hover (`PriceBars.tsx:71`) and the "30-day" unserved sentence go.
   - **One form:** 0 line charts, 0 rank-chart markers, 0 List/Chart toggles.
5. **Two battery harness files whose clauses pin the old dark panel (issuer grant).** Change ONLY the named clauses and nothing else:
   - `__harness__/leadPanelPattern.harness.cjs`: `band_is_lead_panel`, `empty_state_designed_in_band` and `caption_facts_unchanged` are
     re-anchored to this order's rules. The panel is a white card with no band, the empty state is designed inside it, and the caption
     facts are named in words per item 2.
   - `__harness__/tabs.harness.cjs`: ONLY two clauses.
     - `generation_captions_present`: re-anchored so the caption is present in reader words (the generation id may stay only as a data
       attribute).
     - `header_posture_line_matches_payload`: re-anchored to read the posture line from the overlay's own `[data-header-posture]`, not
       from HeaderBrief's posture slot. Cell `AV-zg-1` removes that slot, and cell `AV-zg-2` keeps exactly one `[data-header-posture]`
       inside its details control. The clause must pass on your tree AND after both land. The Model cell `AV-zg-5` relies on this file's `data-model-cell` and
     `data-model-fiscal-cells` clauses: leave them untouched.
   Each re-anchored clause must still FAIL on a planted page that breaks it; show one planted run per file in your report.
   `__harness__/shell.harness.cjs` is NOT yours. Cell `AV-zg-2` owns it and re-anchors its `universe_band_count` to
   `bandContainersTopLevel <= 1`. Your light panel turns that clause red in YOUR tree, so your battery skips `shell` (AC3). The issuer
   runs the full battery, with no skip, on the merged candidate.

**Contracts:** C-PRESENTATION-ONLY (the page computes no window and no return; it sorts and slices the served list). C-FRIDAY (the served
unit as served). Design law: a code may sit in a data attribute, never in visible text.

## 2. BOUNDS

1. No server, no fetch, no network, no install, no push, no deploy. REFUSE, do not rescue.
2. Only the files in `<paths>` change; in the three harness files only the named clauses change.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
4. Write code with the Edit/Write tools ONLY -- never a shell heredoc, `python -c` or a script that rewrites a file.

## 3. SURFACES

<paths>
portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx
portal/src/pages/SecurityAnalysis/components/PriceBars.tsx
portal/src/pages/SecurityAnalysis/components/GenerationCaption.tsx
portal/src/pages/SecurityAnalysis/SecurityAnalysis.tsx
portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs
portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs
org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~82/
org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; in particular the issuer's checks and fixtures under
`org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/` (never edit them).

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AV-zg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/leadprice/pricemovers.cjs"; echo "exit=$?"</invocation><expect>THE PRICE FACE SHOWS THE TOP MOVERS, OPENS ON DEMAND AND NAMES ITS WINDOW: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AV-zg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; node "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/leadprice/leadface.cjs"; echo "exit=$?"</invocation><expect>THE LEAD PANEL IS ONE LIGHT CARD AND SPEAKS READER WORDS: 3 of 3 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AV-zg-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/battery29.sh" "$(git rev-parse --show-toplevel)" --skip shell; echo "exit=$?"</invocation><expect>BATTERY29: ALL PASS (1 skipped) -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~82/DSGN_AMGTV1.TO-AV-zg-3.lead-panel-light-and-price-top-movers.proof_of_spec.json`.
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the `task-orders/` face is lane ANY).
A row id on this project carries the site-z infix: `DSGN_AMGTV1-Z-W82-S<k>`, with a real UTC `surfaced_at` (YYYY-MM-DDTHH:MMZ).
Report once: what changed and where, the output line of every criterion, the portal and outer commit hashes, the re-anchored harness
clauses with their planted-failure runs, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- **Not graded by the checks** (L9 PNG read): the card look, navy tone and spacing; bar length and colour; stacked versus side-by-side
  gainers and losers; visual clipping (the title is required instead); the expand control's wording and placement; an eyebrow repeating
  the page title; subtitle quality beyond the banned words; the Chatter face's own ink (cell `AV-zg-4`).
- **Superseded:** the round-15 `pricebars.cjs` (it expects all bars) is not in the battery.
- **Fixture:** the portal's `uiContractFixtures.json` holds a 32-row round-7 price set, so the live 94-row capture is the issuer's
  fixture.

<status>complete</status>
<round>29</round>
<slot>~82</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<direct_act>false</direct_act>
<worker_class>worker</worker_class>
