# FWD-29 design fork -- does `portal/DESIGN.md` C1-C12 govern the page or the app? -- research note

**Seat:** `4.0.0_SA_CRO~Z`. **Asked by:** `1.0.0_SA_CTO~Z`, msg 25493, 2026-09-24 12:12Z (a design fork routed for
research per Andrew-direct 2026-09-17 ~13:0xZ). **Released by:** msg 25499, 12:23Z ("anything already found is welcome
for round 38's cut, but nothing waits on it"). **Written:** 2026-09-24 ~12:3xZ-12:5xZ. **Vintage:** workspace CLOUD
@`31ef7a1f50` (the round-37 L10), shared checkout's portal HEAD `1f1555d2`, `portal/DESIGN.md` 456 lines.

This note answers the historical question the ask posed and then reports one measurement that changes what the
round-38 decision as taken (msg 25499, items 1-3) will do when a worker runs it. The measurement is section 1 because
it is the part that bears on the cut; the history is sections 2-4.

## 0. The short answer

- **Authority is app-wide; the grading unit is the page or view.** The contract calls itself "the one visual
  authority for `portal/`" (`:188`), says "a reviewer rejects a PAGE by citing a clause number" (`:189`), states C3 as
  "ONE deliberate full-bleed band PER PAGE" (`:234`) and C8 as "one persistent primary action PER VIEW" (`:352`), and
  C8 names the sidebar's active item, rail edge and avatar as governed objects (`:355-357`). So the sidebar is inside
  the contract's authority and outside any one page's grading unit.
- **The one prior instance of a page cell failing on `App.tsx` resolved BOTH ways at once** (DSGN_REBRND, 2026-09-14):
  `App.tsx` was admitted to a cell NARROWLY ("those two class edits only"), AND Andrew amended the contract so the
  shell's accents became legal (the C8 identity set). The sidebar's WIDER treatment -- its weights, radii, shadow,
  and whether to keep it or revert to the DEV-branch sidebar -- was left OPEN AT ANDREW and is recorded so three
  times. It has never been commissioned.
- **The whole-document sweep FWD-29 runs was never a decision.** The brief scoped radii to "elements inside the page
  container" and purple fills to "beside the sidebar's"; the PRD fence dropped the qualifier; the instrument cell
  built a `--scope` flag whose default is `document.body`, and the check never passes it.
- **The band predicate is measuring the wrong object** (section 1). Since the portal-wide named layers of
  2026-09-14, `#0A1733` is the panel-strip and sidebar token, and the page's own band (`Panel variant="mixed"`) is
  an 18%-lightness navy the instrument does not recognise. The "1" that peers reads is the sidebar `<aside>`.

## 1. MEASURED: what the predicates count, whole document versus the page's `<main>`

**Instrument.** `portal/scripts/ui-measure.mjs` at portal `1f1555d2`, run against the vite dev server already
listening on `:5175` (its tree is not verified by this seat; the deltas below are between two runs on the SAME
server seconds apart, so they do not depend on vintage). `--scope main` selects `App.tsx:414`
`<main className="flex-1 ...">`, the element every route renders inside; the `<aside>` sidebar is `App.tsx:270-271`,
a sibling of `<main>`. Fixtures: `src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json` for the two
AMGT routes; `/market` rendered with no fixtures (its data panels answer 401), which leaves its chrome, headers and
strips unaffected. Width 1440. Raw JSON in this seat's scratchpad, `fwd29/*.json`, six files, all rc=0.

| route | scope | bandTop | weights (chars) | sizes < 11 | radii 8px | shadows | purpleFills |
|---|---|---|---|---|---|---|---|
| `/security-analysis` (list) | whole body | 3 | 300:8 500:226 600:37 | 10:26 | 18 | 1 | 3 |
| `/security-analysis` (list) | `main` | 2 | 300:8 600:10 | none | 1 | 0 | 1 |
| `/security-analysis/BA_US_Equity` (thesis) | whole body | 2 | 300:8 500:226 600:33 | 10:47 | 18 | 1 | 4 |
| `/security-analysis/BA_US_Equity` (thesis) | `main` | 1 | 300:8 600:6 | 10:21 | 1 | 0 | 2 |
| `/market` (Andrew-confirmed reference page) | whole body | 13 | 300:8 500:268 600:188 | 10:26 | 27 | 1 | 3 |
| `/market` | `main` | 12 | 300:8 500:40 600:161 | none | 10 | 0 | 1 |

`lowContrastChars` = 0 and `fonts` = {Lato} on all six runs.

**1.1 The band count never sees the page's band.** `ui-measure.mjs:65` defines a band as computed background within
+/-3 of `rgb(10,23,51)` = `#0A1733`. Since DSGN_REBRND round 2 the named-layers block in `portal/src/index.css`
(`:347-352` comment; introduced `/market`-scoped at portal `0aefb3c5` 2026-09-14 19:04Z, made PORTAL-WIDE on `body`
at `1e0aaad7` 20:11Z on Andrew's ~19:5xZ word "instituted across the entire portal frontend") sets
`--bg-band: var(--layer-body)` = `221 45% 18%` (`:371`) and `--bg-header: var(--layer-strip)` = `221 67% 12%` =
`#0A1733` (`:375`, its own comment: "panel title strip, table column header (= the band)"). `hsl(221 45% 18%)`
resolves to `rgb(25,38,67)`, the same value this seat's walk recorded as "the panel's inner ground". So:

- `Panel.tsx:63/:65` (`variant="chart"|"mixed"`, `bg-[hsl(var(--bg-band))]`) -- the page's band, used by
  `SecurityOverlay.tsx:184,:193,:202,:223` (the identity header) and `LeadPanel.tsx:315` -- is **never counted**.
- `PanelHeader.tsx:62` and `PanelFooter.tsx:92` (`--bg-header`, with `rounded-t-lg` / `rounded-b-lg`) and the sidebar
  `App.tsx:271` (`--bg-header`, `shadow-lg`) **are counted**, and are the only things counted.

Read against the table: thesis whole = 2 is the `<aside>` plus one PanelHeader strip; scoped to `main` = 1 is the
strip alone; list whole = 3 adds LeadPanel's PanelFooter strip. The rl-9 worker's own element dump says the same
(".dark-band top-level element list ... ASIDE + one PanelHeader-styled DIV"). **So peers reading 1 is the sidebar
`<aside>`, not a page band**, and the identity header that Andrew's F1 ruling made the ONE band in Security mode is
invisible to the predicate on every state. A band-count cell held inside `src/pages/SecurityAnalysis/**` (msg 25499
item 2) can move that number only by removing PanelHeader/PanelFooter strips, which are shared primitives outside the
rectangle, and it can never grade the thing C3 is about. The remedy is on the INSTRUMENT, which the round already
owns (`rl-1`'s `<paths>` carry `ui-measure.mjs`): key the band test to the `.dark-band` class / `data-panel-variant`
the Panel emits (`Panel.tsx:89-90`), or to the resolved `--bg-band` value, and count `--bg-header` strips separately.
Admitting `index.css` to a cell to re-point `--bg-band` back to `#0A1733` would reverse Andrew's portal-wide word.

**1.2 The purple-fill predicate fails the page on accents C8 permits.** Scoped to `main`, list reads 1 and thesis
reads 2 against the cut's 0 / 1. The extra fill on each is `PageHeaderVariants.tsx:40`, the 3px page-title rule
(`bg-[hsl(var(--semantic-action-primary))]`), which C8 `:355` names FIRST in the identity set. The two the whole-body
run adds are the sidebar's active item and the avatar, both also in C8's set. So the predicate as cut counts three
contract-legal identity accents as violations, and admitting `App.tsx` and `PageHeaderVariants.tsx` to a cell cannot
make it pass without violating C8. The fix is the predicate: count ACTION fills (buttons) and exclude the C8 set by
selector. This seat's brief wrote the criterion as "one purple fill beside the sidebar's" for this reason.

**1.3 Chrome versus page, attributed by subtraction rather than by invariance.** Whole minus `main`, identical on
both AMGT routes: weight 500 (226 -> 0), shadows (1 -> 0), radii 8px (18 -> 1), purple fills (-2), size 10 on list
(26 -> 0) are the sidebar. Two corrections to the invariance reading in msg 25499:

- **Weight 300 at 8 characters is NOT chrome.** It survives scoping to `main` on all three routes. It is
  `PageHeaderVariants.tsx:46` `font-light` on the page title's words, inside `main`, invariant because the header
  renders once per page. Invariance implied chrome; the object is a shared component inside the page container.
  Admitting `PageHeaderVariants.tsx` (item 1) still reaches it.
- **The residue inside `main` on thesis is small and now localised:** weight 600 on 6 characters, one 8px radius,
  21 characters at 10px. On list: 600 on 10 characters, one 8px radius, no size-10. These are item 3's
  "measure-first" quantities; a `--scope main` run is the measurement, and it is one flag on the existing check.

**1.4 The Andrew-confirmed reference page fails the same predicates inside its own `main`.** `/market` (Andrew-direct
2026-09-14 ~19:0xZ, "This is all good", DSGN_REBRND PRD v0.10) scoped to `main` reads weight 500 on 40 and 600 on 161
characters, ten 8px radii and twelve `#0A1733` strips. So "in pattern with the Dashboard" (Andrew's word for this
page) and "DESIGN.md C1/C11 as the instrument measures them" are not one bar today; a round-38 C1/C11 cell will meet
this on `PanelHeader.tsx:62`'s `rounded-t-lg`, which is every Dashboard panel's title strip. Caveat: `/market`'s
panel bodies rendered in their 401 states; the header, strip and chrome numbers are not affected by that.

**1.5 Census blind spot, one line.** `ui-class-census.mjs`'s radius pattern is `rounded-(md|lg|xl|2xl|3xl)\b` and
misses the directional forms: `PanelHeader.tsx` reads `radius=0` in the census (FILES 5 TOTAL 59 over the shell and
panel files: `App.tsx` 45, `PanelHeader.tsx` 6, `PanelFooter.tsx` 4, `Panel.tsx` 3, `PageHeaderVariants.tsx` 1) while
the render measures its 8px. The render is the oracle (C-RENDER-IS-THE-ORACLE), so nothing is mis-graded, but a
worker reading the census to find the owner of an 8px will not find this one.

## 2. The contract's own scope statements, by line (portal `1f1555d2`)

| line | text | scope it asserts |
|---|---|---|
| `:6-7` (front matter) | "one deliberate #0A1733 band per page, and #5F3BE3 spent on one persistent primary action per view plus five named identity accents" | grading unit: page / view |
| `:188` | "The one visual authority for `portal/`." | authority: the whole app |
| `:189` | "a reviewer rejects a page by citing a clause number" | grading unit: page |
| `:190` | "Where a page and this file disagree, the page is the defect." | grading unit: page |
| `:234` (C3) | "ONE deliberate full-bleed band per page, never the default container" | per page |
| `:352-357` (C8) | one action "per view" plus identity accents in "six named places": page-title rule, header subtext, active tab, "the sidebar's active item", "the sidebar rail's faint edge", the user avatar | the SIDEBAR is a governed object of the contract, and its accents are legal by name |
| `:452` | "the portal carries one band per page (C3)" | per page |

No clause names `App.tsx`, `index.css` or the shell as excluded; no clause names them as a page's responsibility.
The contract governs the app and is graded a page at a time. That is also how it was delivered (section 3).

## 3. Past pattern 1 -- DSGN_REBRND (the project that authored the contract), 2026-09-11 to 09-14

**Delivery unit was the page, with the app as denominator.** PRD preamble `:18`: "delivery is PAGE BY PAGE, starting
with Market Overview (Andrew-direct 2026-09-14 ~18:3xZ)". `RB-s-12` built the surface inventory whose denominator is
"the portal's route count, PRINTED, read from the route table in `portal/src/App.tsx`" (26 in prose, 24 measured),
and `RB-s-13` graded render coverage per route x state against it. The named-layer tokens first shipped as a per-page
opt-in (`[data-surface-layers]`) and went portal-wide on Andrew's word (`index.css:349-352`).

**The one prior page-cell-fails-on-App.tsx instance, and its two-sided resolution.** Row `DSGN_REBRND-W1-S19`
(`surprise-channel/investigations/INVESTIGATION_v1.md:786-806`, surfaced 2026-09-14 05:17Z by
`0.9.0_WK_DSGN_REBRND~1`): "The app shell in `portal/src/App.tsx`, which is outside this order's `<paths>`, fills TWO
persistent elements with the accent on every route ... So no route can reach the one-persistent-accent budget from
inside this grant." Class BLOCKING, disarm owner `2.0.0_SA_COO~D`: "widen a follow-on grant to `portal/src/App.tsx`
(OR rule the shell out of the per-view budget)". What then happened, in order:

1. `RB-s-6` was cut WITH `App.tsx` in its grant, bounded to "those two class edits only -- no layout, no route, no
   behaviour" (`App.tsx:189` the active item, `:382` the avatar); the worker's four-line diff against that bound is
   row `:1050-1066`. The shell was ADMITTED, narrowly.
2. Andrew-direct 2026-09-14 ~15:0xZ ("I'd like to make a concerted effort to keep selective indigo accents") RESTORED
   the sidebar active item and the avatar as identity accents; PRD v0.3 widened FWD-4 and the contract's C8 to the
   closed identity set (record `ANDREW_DIRECT_20260914_150xZ_..._RESTORE_SELECTIVE_INDIGO_ACCENTS...md` @`d54876b585`).
   The CONTRACT moved to match the shell, on his word, after the shell had been "fixed" to match the contract.
3. `2.0.0_SA_COO~D` then edited `App.tsx` directly, no worker, on his ~19:5xZ word (portal `1e0aaad7`: the active
   item loses its white rule; C8 follows).

**The sidebar's wider treatment is OPEN AT ANDREW, three records.** Andrew-direct 2026-09-14 ~18:3xZ, verbatim: "I
like faint indigo edge on the sidebar, I honestly think that the original sidebar coloring/setup (on DEV Branch) was
fine, will see what the current version looks like in the interim and make a call later if we keep it as is or just
revert to the DEV branch implementation" (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_183xZ_DSGN_REBRND_ROUND2_DECISIONS_NAMED_LAYERS_STATE_RULE_PAGE_BY_PAGE_MARKET_FIRST.md:11-12`;
`:29` "The larger sidebar question is OPEN at him"; `:40` "The sidebar revert ... his"). DSGN_REBRND PRD v0.6 `:260`
and v0.10 `:276`: "The sidebar's wider treatment stays open." `ROUND_ANALYSIS_DSGN_REBRND_ROUND1_20260914.md:82`: "The
other items open at him stand where they stood: FWD-9; the sidebar (keep or revert to DEV's)". Nothing in the record
since closes it. So the sidebar's `font-medium/semibold/light`, `text-[10px]`, `rounded-lg` and `shadow-lg`
(`App.tsx:180,199,202,271,369,395,403-404,531,540,547`, 13 class hits) are not an oversight of an earlier round;
they are the "current version" he said he would look at and decide on. **Relay, not a gate:** a round-38 cell that
admits `App.tsx` for C1/C11 (msg 25499 item 1) will be restyling the sidebar, and the record says that call is his.
The cell can measure the sidebar, and can fix `PageHeaderVariants.tsx`, `PanelHeader.tsx` and `PanelFooter.tsx`
without touching that call; a sidebar restyle is a card to him, or an ask before the cut.

## 4. Past pattern 2 -- IRPT_FNTEND (a consumer of the contract), rounds 10-14, 2026-09-21/22

IRPT never met this fork, and the reason is instructive: its render criteria are ELEMENT-SCOPED by construction. The
round-10 criterion rule (`TO-FE-s-67`, binding on every visual criterion) requires "(d) GROUND MEASURED ON THE ACTUAL
CONTAINER -- `--expect-ground` on the element that carries the surface, not the page field", after two round-10
captures "read the right colour on the wrong page" off `document.body`. Every FE cell asserts on named
`data-slot` selectors (`FE-s-67`, `FE-s-76`, `FE-s-87` scopes one file's two weight classes to C1). The CTO's
round-10 analysis has zero occurrences of `sidebar`, `App.tsx`, `shell` or `chrome` across 108 lines. Its FWD-12 is
"The Investor Reporting SCREENS look and behave like the rest of the Opal portal" -- the page, graded against the
app as the reference. A whole-document sweep was never IRPT's instrument, so the shell never entered its grades.

## 5. How the whole-document sweep got into FWD-29

- This seat's brief (`docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md@21dd61e392`): `:215` "Measured 22-23
  elements at 8px per state (most from the sidebar chrome, which is out of scope, but 4 in `LeadPanel.tsx` and 2 in
  `PrintExportAction.tsx` are in scope)"; `:441-447` acceptance shape: "`radii` within {2px, 3px, 4px, pill} for
  elements INSIDE THE PAGE CONTAINER (C11)", "`purpleFills` == 1 BESIDE THE SIDEBAR'S in Security mode".
- PRD ENDPOINT fence FWD-29 (`:728-737` @`31ef7a1f50`) carries the predicate list without "inside the page container".
- `TO-AMGT-rl-1` (the instrument cell) specified `--scope <css-selector>` "(default: the whole body)" for
  `ui-measure.mjs`, and `ui-contract-check.mjs` (389 lines) passes no `--scope` (0 hits). So the check sweeps
  `document.body` by default, not by anyone's decision.
  **CORRECTION 2026-09-24 ~12:5xZ (`1.0.0_SA_CTO~Z` msg 25512, re-measured by this seat):** the parenthetical
  "(0 hits)" above and in msg 25504 is WRONG as a number. The enumeration over `ui-contract-check.mjs` returned
  **3 hits, all substrings** of `/api/scoped/amgt/...` route strings at `:78-80`, and **0 whole-value** matches; this
  seat collapsed "3 substring, 0 whole-value" into "0". The conclusion is unchanged -- no `--scope` argument is passed
  anywhere in the file -- and only the count was misreported. Kept in place because a later reader re-checking
  finds 3 and would otherwise conclude the finding collapsed.

For the page-owned predicates (radii, sizes, weights, purple fills) a `--scope main` run is therefore the BRIEF's
scope restored, not a denominator shrunk; for the chrome, msg 25499's split (chrome is real, admit its owners) stands
on the same numbers. The two are not in tension once the band and purple predicates are re-keyed (1.1, 1.2).

## 6. What this note does not do

No file under `portal/` was changed; no cell, scope or grade is proposed as a gate; the dev server on `:5175` was
read, not started or stopped; no PNG was read (the JSON deltas are the evidence here, and C-RENDER-IS-THE-ORACLE
still binds any grade). The sidebar call stays where the record puts it, at Andrew.
