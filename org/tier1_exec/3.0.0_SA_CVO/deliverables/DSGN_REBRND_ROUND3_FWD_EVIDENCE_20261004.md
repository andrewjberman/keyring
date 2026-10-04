# DSGN_REBRND round 3 -- per-FWD evidence (3.0.0_SA_CVO, assembled by a read-only delegate, 2026-10-04 ~18:5xZ)

# DSGN_REBRND round 3 -- FWD evidence for the L9 outcome grade (DRAFT for 3.0.0_SA_CVO)

Assembled READ-ONLY on 2026-10-04 at about 18:5xZ by a delegate of `3.0.0_SA_CVO`. This is evidence and a PROPOSED verdict per
outcome. It is not the grade. Nothing was committed, edited, rendered or messaged.

Asked by: `1.0.0_SA_CTO` RULINGS batch 238 item 1 (@77645a2835): "Round 3 closes at L10 on `3.0.0_SA_CVO`'s outcome grade:
every FWD, read at portal DEV and PROD heads."

## Planes read

| plane | value | how read |
|---|---|---|
| portal origin/PROD | `dbd29c63` (merge DEV->PROD of DEV `dddaf3a1`, 2026-10-03 21:47Z, authored for 0.0.0_AB_MSTR on Andrew's "Yes, promote all") | `git -C portal fetch origin` at 18:47Z, then `ls-remote` (they agree) |
| portal origin/DEV | `c67c242f` (2026-10-04 02:53Z, 2.0.0_SA_COO~D, a DSGN_IRPTV1 item) | same |
| workspace origin/CLOUD | `791909f744` (ls-remote); local HEAD `8daaf100b2` | STATUS.md last changed at `a1460a5842`, batch 238 `77645a2835`, E5 `207728cced`, E6 skill `91c6cbb6d2`: all are ancestors of origin/CLOUD (rc 0) |
| PRD | `org/missions/D13/DSGN/DSGN_REBRND/prd/DSGN_REBRND_PRD.md`, `prd_version` v0.10, RATIFIED, ENDPOINT FWD-1..FWD-13 | read at HEAD. The v0.11 correction of FWD-3's PROOF line (batch 80 item 11) has NOT been cut |

Method:
- Source census over the git blobs of both refs, using Python over `git cat-file`, with no working-tree reads. The script is
  `scratchpad/rebrnd_r3/census.py`. Counts are over non-test `src/` files unless stated otherwise. PROD has 1,090 src files
  (621 non-test); DEV has 1,103 (621 non-test).
- Ancestry by `merge-base --is-ancestor`.
- A content control on the 10 DEV-only pins: the share of each pin's added lines found in PROD's bytes is 0 of 4-21 for 9 pins
  and 1 of 13 for a403f466. Positive controls: 8526dacb 18/18, d7141e5a 17/17, 6cb31b54 15/15.
- No browser, no render, no tests, no CI or CDN read. Whether PROD's served bundle matches the ref is taken from this seat's own
  pin-grade records ("Deploy succeeded" for 6169edd9, 98a98e70 and dbd29c63).

Context the grade should hold:
- **The close conditions on record disagree.** Batch 238 says "the project closes only when every FWD grades REALIZED". Andrew's
  word of 2026-09-14 ~19:3xZ
  (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_193xZ_DSGN_REBRND_PAGE_BY_PAGE_NO_TOS_MANUAL_CLOSE_MARKET_APPROVED_PORTFOLIOS_NEXT.md`)
  "authorize[s] a manual close when I'm happy". That record reads the mechanical proofs as evidence, not the gate. This draft
  grades the FWDs as batch 238 asks.
- **The named layers went portal-wide by Andrew's word on 2026-09-14 ~19:5xZ** (record `..._194xZ_DSGN_REBRND_PORTAL_WIDE_...`).
  On PROD the `--layer-*` rungs sit on `body` in `src/index.css`, and `[data-surface-layers]` is a no-op. The PRD's page-level
  surface scope is therefore retired by his word, not by the last page opting in.
- **The PRD's SURFACE MANIFEST and preamble still say "no cell writes to DEV or CLOUD"**, under the feature-branch confinement.
  Round 3 landed on DEV under the FAST lease (batch 165) and reached PROD through three promotes. The text and the world
  disagree. This is an observation, not a grade.

## Round-3 pins: this seat's grade and PROD ancestry

Source: `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_FAST_PIN_GRADES_20260928.md` (the sections from 22:xZ 2026-10-02
through 02:4xZ 2026-10-04). "First PROD" is the first promote that carries the pin.

| pin | item | this seat's grade | on PROD | first PROD | FWD |
|---|---|---|---|---|---|
| fb5d6116 | E4: the Summary's translucent fills move onto opaque rungs | NOT_EVALUATED (re-graded NOT_EVALUATED; no colour assertion) | yes | 6169edd9 | 12 |
| fe461611 | E4: the Breakdown's subtotal and total rows move to the tile and selected rungs | NOT_EVALUATED; on re-grade, the inks PASS by arithmetic and the rung choice is unpinned (row S5) | yes | 6169edd9 | 12, 13 |
| 661e49b3 | E4 FWD-13: the AGG chip ink and the name hover | NOT_EVALUATED by test; the ink PASS by arithmetic | yes | 6169edd9 | 13 |
| 44d6a215 | E4 FWD-13: a highlighted name on a band ground; the OKLab ramp | PASS on the walk's computed styles; NOT_EVALUATED by test | yes | 6169edd9 | 13 |
| b23917f7 | row S5's remedy, a white/70 dash | PASS on a test run (iv-e-152); arithmetic, not pixels | yes | 6169edd9 | 13 |
| c9d303db | E2: DESIGN.md C10 gains the PAGE END | NOT_EVALUATED (no test reaches it) | yes | 98a98e70 | 10, 6 |
| 8526dacb | E2: /positioning ends on its PAGE END | PASS on a test run + PASS by render | yes | 98a98e70 | 10 |
| 201bfe69 | E6: the canvas comments stop saying "silver" (28 files) | NOT_EVALUATED (no logic change) | yes | 98a98e70 | 6 (FWD-1 constraint) |
| d7141e5a | E3 W3-S1: the route NO-PERMISSION panel | PASS on a test run; broke F49-AC4 (row S13) | yes | 98a98e70 | 11 |
| d8d236a0 | row S10: class-label inks at 5.89 and 5.65 | PASS on a test run | yes | 98a98e70 | 13 |
| 71a946e3 | 4b: the band's secondary ink | PASS on a test run | yes | 98a98e70 | 13 |
| 46aeea17 | 4c: the Satellites footer date format | PASS on a test run (the formatter); the footer render NOT_EVALUATED | yes | 98a98e70 | -- |
| fb5534f8 | compact percentage labels | PASS | yes | 98a98e70 | -- (layout) |
| cbfbb77a | the footer hour asks New York | PASS | yes | 98a98e70 | -- |
| 55560835 | /market RSI and Fear & Greed show ERROR | PASS on the claim (a gauge `: 50` mutant survives) | yes | 98a98e70 | 11 |
| a7b16628 | Daily Cloud, Trending and Performers show ERROR | PASS (the page wiring is unpinned) | yes | 98a98e70 | 11 |
| 564a8f95 | the RSI hook does not invent 50 | PASS by probe; unpinned | yes | 98a98e70 | 11 |
| b0b3c524 | /positioning Models load ERROR | PASS | yes | 98a98e70 | 11 |
| 94c055e8 | /attribution ERROR and LOADING | PASS | yes | 98a98e70 | 11 |
| c3e1d7b9 | /portfolio-management | PASS; pin gap (wiring) | yes | 98a98e70 | 11 |
| 3d8cce99 | /ticket-center | PASS by probe | yes | 98a98e70 | 11 |
| 30f7fca1 | /data-refresh History and Rollback | PASS by probe | yes | 98a98e70 | 11 |
| 075d33fa | the Advisors tab | PASS by probe | yes | 98a98e70 | 11 |
| 10fca02d | "Connected" | PASS by probe | yes | 98a98e70 | 11 |
| 1754d9c1 | RSI period change | PASS by probe | yes | 98a98e70 | 11 |
| 4a40a0ff | the RSI modal | PASS by probe | yes | 98a98e70 | 11 |
| 6e31c220 | /positioning notices | PASS by probe (2 of 6 notices) | yes | 98a98e70 | 11 |
| 1b8fccfd | Assets Overview | PASS by probe | yes | 98a98e70 | 11 |
| e2563c17 | F49-AC4 counts the NO-PERMISSION panel | PASS; answers row S13 | yes | 98a98e70 | 11 |
| 2da1eaaf | F47-AC6 | PASS | yes | 98a98e70 | -- (test) |
| 3a842221 | the regime says no reading, never 50 | PASS | yes | dbd29c63 | 11 |
| a6a77e31 | wiring tests | PASS | yes | dbd29c63 | 11 |
| 6cb31b54 | the auth pages' error state | PASS | yes | dbd29c63 | 11 |
| cc1d7cc6 | /factor-tilts says it once | PASS | yes | dbd29c63 | 11 |
| 7b265fc4 | merge | PASS (clean re-merge) | yes | dbd29c63 | -- |
| fb73cb1c | /philosophy Views states | PASS | **no** | -- | 11 |
| 3e526a44 | the Cause line drops the raw JSON | PASS | **no** | -- | 11 |
| 8071b59b | the IR request list and preview states | PASS | **no** | -- | 11 |
| e2f89bd9 | /valuations states | PASS | **no** | -- | 11 |
| 7a12098c | the Valuation Range with no range | PASS | **no** | -- | 11 |
| c35c66db | /correlations states | PASS | **no** | -- | 11 |
| a403f466 | /data-refresh ERROR with a retry | PASS | **no** | -- | 11 |
| a9b7427e | /security-scanner LOADING | PASS | **no** | -- | 11 |
| d8b81b65 | /advisor-intelligence PanelLoading | PASS; the census reaches part of the tree | **no** | -- | 11 |
| 504e5379 | the sign-in check is PanelLoading | PASS; "on a panel" is unpinned | **no** | -- | 11 |

Totals:
- 34 REBRND commits plus 1 merge are on PROD. 10 are on DEV only (the merge 822ce891 is also DEV-only).
- Workspace E5 (`207728cced`, the two checkers) and E6's skill half (`91c6cbb6d2`) are on origin/CLOUD. This seat has NOT graded
  either: no row in the pin-grade file.
- Rows this seat graded: S6 supports the W2-S8 disarm for /positioning (text only). S7: latent confirmed for `html.dark-mode`,
  with a second, OS-driven path (row S9).

---

## FWD-1 -- A prospect moving from the website into the portal does not experience a change of firm

- **DONE WHEN:** "EXERCISED -- one person who has never seen the portal is walked from opalinvest.com into a portal route and
  asked what changed"
- **ACCEPT:** "the person names capability differences (it does more, it shows my data) and no visual ones; typeface, canvas
  colour, corner radius, focus visibility and the role of navy read as one system across the boundary"
- **Round 2:** not graded (a person act; round 1 graded it NOT EVALUATED: the walk was not performed and RB14-AC4 FAILED because
  several IV.3 differences are not bands). RULING W (CTO round-1 analysis) made the site half the existing
  `design/brand/opalinvest.com.json` and made the walk a human act whose timing is Andrew's.
- **Round-3 evidence:**
  - No pin serves it directly.
  - 201bfe69 (on PROD, NOT_EVALUATED) removes the "silver" canvas comments: the FWD-1 CONSTRAINT's "rewritten in place".
  - E6's skill half (CLOUD `91c6cbb6d2`, not graded) does the same.
  - PROD census: `shadow-lg` 36 in 24 files, unchanged from round 2 (row W1-S36: shadows were the brief's one agreement).
    `dark:` 304 uses in 27 files with no `@custom-variant dark` (row S9: modals restyle under the OS's dark preference).
  - ~D's STATUS: "FWD-9 ... and FWD-1 (a walk by a person new to the portal) are person acts, unchanged."
- **Missing for REALIZED:** the walk itself, which is the DONE WHEN. Also the IV.3 parity re-measured on three PROD routes
  (round 1 failed it; nothing since).
- **Proposed: NOT REALIZED.** The EXERCISED act (one new person's walk) has never happened.

## FWD-2 -- An advisor reads a figure without the typeface telling them it came out of a terminal

- **DONE WHEN:** "APPLIED -- every numeral in the product renders in the firm's typeface with tabular alignment"
- **ACCEPT:** "an advisor reading a return, a value or a date cannot tell from its letterforms whether it came from the product
  or a developer's console, and columns of figures still line up"
- **Round 2:** REALIZED, with one gap (row W1-S8: weight 700 is served by the SemiBold face). The before/after pixel alignment was
  not re-measured.
- **Round-3 evidence:**
  - No round-3 pin.
  - Re-read at PROD `dbd29c63`, identical at DEV: `font-mono` 1 in 1 file (`src/lib/designTokens.ts`, the unreferenced
    `dataValue` token round 2 named); `tabular-nums` 134.
  - `public/fonts/` = `lato-regular-400.woff2`, `lato-semibold-600.woff2`, `OFL.txt`, `README.md`.
  - 0 Google-font or Inter imports in `src/index.css`. No regression since round 2.
- **Missing:** the PROOF's before/after pixel comparison of figure columns (never measured in any round); row W1-S8 (a true
  Lato Bold is Andrew's word).
- **Proposed: REALIZED (carried from round 2, PROD re-read shows no regression)**, with the two named gaps restated.

## FWD-3 -- An advisor reads the ORDER of an ordered scale off its colour, without a legend

- **DONE WHEN:** "APPLIED -- every ordered quantity in the product is one hue ramped light to dark"
- **ACCEPT:** "shown a duration ladder, a performance band or an over/under-weight scale with the legend covered, an advisor puts
  the steps in the right order"
- **Round 2:** NOT REALIZED. Global RSI is off-ramp (row S3), and no census of ordered scales with a printed denominator exists.
- **Round-3 evidence:**
  - E1 CLOSED: `1.0.0_SA_CTO` batch 215 RULED NO. The RSI bars keep their original gradient, by analogy to Andrew's 2026-09-14
    Fear & Greed word. Row S3 is "superseded", and the patch is archived at `deliverables/2.0.0_SA_COO~D/e1/`, never applied.
  - E5 (`207728cced`, CLOUD, not graded): `rb4-ramp-check.py` grades the portal-wide SENTIMENT tokens only and prints the
    /market block as EXCEPTED.
  - PROD: `getRSIColor` 8 references in `RSIModal.tsx`; 10 `--ramp-N` declarations in `index.css`.
- **Missing for REALIZED:**
  - (a) The PROOF's census of EVERY ordered scale in `portal/src/` with a denominator. It was absent in round 2 and in round 3,
    since E5's checker covers sentiment tokens only.
  - (b) The ENDPOINT CONSTRAINT names exactly two exceptions "by Andrew's word". The RSI bars are a third, resting on a CTO
    ruling by analogy that the ratified text does not carry.
  - (c) The PROOF line still calls the canon five-hue control "the named positive case" (v0.11 is owed and is an ENDPOINT
    change).
- **Proposed: NOT REALIZED.** No ordered-scale census exists. The RSI exception also stands outside the ratified text until
  v0.11 carries it.

## FWD-4 -- An advisor can tell at a glance which single thing on a screen is the action to take

- **DONE WHEN (short):** "APPLIED -- each view spends the accent on AT MOST ONE PERSISTENT primary action ... plus a CLOSED SET
  OF IDENTITY accents ...; the [focus] ring ..., the highlight on selected text and every tooltip share the accent as TRANSIENT
  feedback and are budgeted separately"
- **ACCEPT (short):** "on any screen that has an action an advisor points at the one thing that is clearly the action, and a
  screen without one carries no accent posing as an action; ... segmented controls and toggles mark their active state by
  weight and rule, never by a filled accent chip per option ..."
- **Round 2:** PARTLY EVALUATED, no defect found. Not measured: the accent pixel share per route and the three-route
  counterexample walk.
- **Round-3 evidence:**
  - No enrichment item and no pin targeted FWD-4.
  - 661e49b3's AGG chip ink moves to indigo400. That is a book's data colour (`AGG_PORTFOLIO.color`), not the accent; it is
    noted only so it is not mistaken for one.
- **Open:**
  - Row C-S11: the Fear & Greed "Neutral" label is painted in the accent. Its remediation row is OPEN; round 2 did not read it.
  - Row W1-S20: the ruling half is in the text; the /portfolio-management half was not read.
- **Missing:** the PROOF's measurements (accent pixel share per route, persistent carriers enumerated, the counterexample walk)
  were never taken in round 2 or 3.
- **Proposed: NOT REALIZED** (not evaluated). The PROOF has never been measured, and C-S11 is open.

## FWD-5 -- An advisor working by keyboard can see where they are

- **DONE WHEN:** "APPLIED -- focus is visible on every interactive element, with the ring the website ships"
- **ACCEPT:** "tabbing through any route, the advisor always sees which element is focused"
- **Round 2:** REALIZED on three routes, with one gap: row W3-S6 (the drop zones on /data-refresh and /trade-submission carry no
  `tabIndex`).
- **Round-3 evidence:**
  - No pin.
  - PROD: `outline: none !important` 0.
  - `src/pages/DataRefresh/components/FileDropZone.tsx` and `src/pages/TradeSubmission/components/FileUploadZone.tsx` each carry
    `onDrop` with 0 `tabIndex` and 0 `onKeyDown`, on both PROD and DEV, so W3-S6 is unchanged.
  - The new ERROR panels' "Try again" buttons were not keyboard-walked; the ring is a global `:focus-visible` rule.
- **Missing:** W3-S6. A strict reading of "every interactive element" counts an unfocusable drop zone against the DONE WHEN; the
  ACCEPT ("always sees which element is focused") is met as written. This is the grader's call.
- **Proposed: REALIZED (carried)**, with W3-S6 restated. If the grader reads W3-S6 as inside the DONE WHEN, it is NOT REALIZED
  on one named defect.

## FWD-6 -- A builder derives every visual decision from one written contract, and a reviewer can FAIL a page by citing its clause

- **DONE WHEN:** "EXERCISED -- one new page has been built from the contract alone by someone who has not seen the portal, and one
  page has been rejected by clause"
- **ACCEPT:** "the contract resolves typeface, colour role, spacing, shape, elevation, focus and layout split; it is the file the
  estate's design tooling reads; a rejected page's author agrees the clause was violated without further argument"
- **Round 2:** not graded. Round 1 graded it NOT REALIZED: RB7-AC4 PASS (the build from the contract), RB7-AC5 FAIL (0 of 5
  author agreements), and C-S12.
- **Round-3 evidence:**
  - c9d303db (on PROD; NOT_EVALUATED) adds C10's PAGE END.
  - E5 makes `rb7-contract-check.py` grade both arms (CLOUD; not graded).
  - E6 rewrites the old law in the frontend-dev skill (CLOUD; not graded) and in 201bfe69 (on PROD; NOT_EVALUATED). Row
    W2-S15's three named carriers (`panels/README.md`, `TicketCenter.tsx`, `designTokens.ts`) read 0 "silver" on PROD; 35
    "silver" mentions in 17 non-test files remain, left by reading each per STATUS.
  - PROD `DESIGN.md` (512 lines): 0 `class:` keys, 0 "derived", 0 "preserved", so row C-S12 is unchanged.
  - 0 matches for "layer", "strip" and "inset", so no named-layer role table (FWD-12) is in the contract.
  - No "ink follows the current ground" state clause (FWD-13) is found by those words.
- **Missing:**
  - The rejection-by-clause with the author's agreement on record. It was never done after round 1.
  - Every token value classed (C-S12).
  - The layer and state clauses the CONTRACTS table requires the contract to carry.
  - Rows W1-S3, W2-S9 and W1-S25 (byte-equality of the contract and the tokens) are open.
- **Proposed: NOT REALIZED.** The EXERCISED rejection-by-clause is absent, and the contract still lacks class labels and the
  layer and state clauses.

## FWD-7 -- A chart series is never painted in the colour the product reserves for "something is wrong"

- **DONE WHEN:** "APPLIED -- status colour and data colour are two separate token systems with no aliasing"
- **ACCEPT:** "no series on any chart shares a colour with an error, warning or success state; a reviewer can show the two
  systems and where they are kept apart"
- **Round 2:** REALIZED, with one gap: `--sentiment-extreme-greed: var(--success)`, inside the Fear & Greed exception.
- **Round-3 evidence:**
  - No pin targeted it.
  - PROD `src/index.css`: 7 `--chart-*` declarations, 0 aliased to a status variable. The one alias remains:
    `--sentiment-extreme-greed: var(--success)`.
  - PROD `design/brands/opal-capital.json`: `status` 4 distinct hex, `data` 21 distinct hex, intersection empty. DEV is identical.
  - d8d236a0 adds class-colour TEXT inks (blue400, pink400) through `chartColors.getAssetClassInkOnDark`, which are data-family
    inks; it creates no status alias.
- **Missing:** the gap (one sentiment token aliased to `--success`, which FWD-7's text does not except). Rows W1-S4 (two
  model-colour systems disagree) and W2-S11 (the /positioning asset-class legend is swapped against the token file) are open and
  unread.
- **Proposed: REALIZED (carried)**, with the alias gap restated.

## FWD-8 -- Two charts on the same screen share their axis, tick, tooltip and legend treatment

- **DONE WHEN:** "APPLIED -- a screen's charts come from one rendering system"
- **ACCEPT:** "an advisor looking at two charts on one screen sees one product, not two libraries"
- **Round 2:** REALIZED on the census. Two charts on a populated screen were not compared by eye.
- **Round-3 evidence:** no pin. PROD import census (import lines / files), identical on DEV:

  | library | import lines / files |
  |---|---|
  | recharts | 40 / 40 |
  | apexcharts | 0 |
  | @nivo | 0 |
  | @visx | 2 / 1 (`TopicCloud.tsx`, the named exception) |
  | lucide-react | 125 / 122 |
  | phosphor | 0 |
  | framer-motion | 0 |
  | motion | 3 / 3 |

  `package.json` carries exactly recharts, @visx/text, @visx/wordcloud, lucide-react and motion.
- **Missing:** only the by-eye comparison of two charts on a populated screen (an ACCEPT limb never exercised).
- **Proposed: REALIZED (carried)** on the census, with that gap restated.

## FWD-9 -- Andrew puts the portal beside an institutional competitor and the difference is not that ours looks generated

- **DONE WHEN:** "EXERCISED -- Andrew has made that comparison and said so"
- **ACCEPT:** "the comparison turns on capability rather than on finish"
- **Round 2:** not graded (his act). Round 1: "his". RB15-AC5 PASS graded the pack's form only.
- **Round-3 evidence:**
  - None.
  - A search of `org/` for DSGN_REBRND with FWD-9 or "side-by-side" finds no word from him after 2026-09-14.
  - ~D's STATUS lists it under "Open at Andrew".
- **Missing:** his word, on record.
- **Proposed: NOT REALIZED** (his to grade; never self-graded).

## FWD-10 -- An advisor's screen is filled by the work, not by the space around it

- **DONE WHEN:** "APPLIED -- on every route the density gradient runs generous inside a data container and disciplined between
  sections, and a page that has run out of content ends on purpose"
- **ACCEPT:** "on the representative populated routes an advisor sees the work fill the screen, with less space between sections
  than inside a container; a page whose content is genuinely short ends with a designed statement that it has ended -- never a
  stretched row, never filler, never a trail of empty canvas"
- **Round 2:** NOT REALIZED on the end-of-page limb (no terminator clause, row W1-S29). Density NOT_EVALUATED (no populated
  fixture).
- **Round-3 evidence:**
  - E2: c9d303db, the C10 PAGE END clause (`DESIGN.md:387-401`), on PROD, NOT_EVALUATED.
  - E2: 8526dacb, /positioning adopts it, on PROD, PASS on a test run + by render.
  - ~D's signed-in walk `20261003T013711Z` reads "End of Positioning. Data as of October 1st, 2026, 5:00p ET." This is a
    self-report.
  - PROD census: `<PageEnd` is used in exactly 1 file (`src/pages/Positioning/Positioning.tsx`). App.tsx has 28 `<Route path>`
    entries, 25 excluding the `*`, `/` and `/*` redirect and wildcard entries. So the PAGE END is on 1 of 25 routes.
  - STATUS: "Other routes adopt it in their own cells."
- **Missing:**
  - The terminator on every other route.
  - The density limb: no populated-fixture render, no before/after share of the viewport below the last content, and no
    measured inside-container versus between-section spacing.
  - The sparse-populated negative control.
- **Proposed: NOT REALIZED.** The terminator is on 1 of 25 routes, and density has never been measured on populated fixtures.

## FWD-11 -- An advisor meeting a panel with no data still sees a designed surface

- **DONE WHEN:** "APPLIED -- empty, loading, error and no-permission are four designed states and every panel uses one of them"
- **ACCEPT:** "a panel with nothing to show still looks like part of the product, says in plain words which of the four things
  happened, never repeats its own message, and never paints an error on the bare page"
- **Round 2:** NOT REALIZED. The census was not at zero (W3-S5), NO-PERMISSION was unwired (W3-S1), and error-versus-empty
  (W3-S4) was not exercised.
- **Round-3 evidence:** E3 is the bulk of round 3.
  - **W3-S1** is disarmed by row S11. d7141e5a is on PROD, PASS on a test run; its F49-AC4 break was answered by e2563c17, on
    PROD, PASS. Parked by design: a partner firm outside its allowlist still redirects to its landing ("un-parks on a CTO
    ruling").
  - **W3-S4** is disarmed by row S14 on every named route. Pins 55560835 through 1b8fccfd plus 3a842221 and a6a77e31 are all on
    PROD, PASS by test or probe. This seat: "W3-S4 holds on every route this range touched." Not swept: routes the row did not
    name. Effect-driven branches were checked by a 401 render alone.
  - **W3-S5** is partly landed:
    - On PROD: 6e31c220, 6cb31b54, cc1d7cc6.
    - **DEV only: 10 pins**: fb73cb1c, 3e526a44, 8071b59b, e2f89bd9, 7a12098c, c35c66db, a403f466, a9b7427e, d8b81b65 and
      504e5379. All PASS; the content control confirms they are absent from PROD.
  - STATUS: "W3-S5 ON THIS SEAT'S SURFACE: DONE", with three items parked with owners. Batch 238 item 1 rules that these "do not
    hold the grade": /portfolios under MDPF_TAXSMA; ClientsTab and AdvisorBookView under MDPF_SECCLASS (~M).
  - **The StatusPanel reason code is UN-PARKED by batch 238 item 2 and is OWED by ~D.** DEV `src/pages/InvestorReporting/tabs/
    StatusPanel.tsx:81-89` still prints `envelope.publicReasonCode` as visible text (0 "Technical details").
  - This seat's last section names two more bare spinners: `App.tsx:440-445` (the Suspense page-loading fallback,
    `<LoadingSpinner size="lg" />`, on PROD and DEV) and `AdvisorPublicProfile.tsx:844`. Neither is in a parked set.
  - The census, replicating `rb10-state-census.py` over blobs: RAW-REMAIN 2 across 2 files on both PROD (417 .tsx) and DEV
    (430 .tsx). Both hits are messages inside `<PanelEmpty>`, so they are checker false positives. The project checker still
    cannot read MIGRATED.
  - A crude spinner-idiom count (lines with `animate-spin`, `<LoadingSpinner`, `<Loader2` or `<LoadingInline`, non-test, not
    classified, so it includes button busy-indicators and the component's own definition): PROD 65 in 41 files, DEV 50 in 32.
    The DEV-only pins account for the drop.
  - Row W3-S3 is open: `rb13-coverage-check.py` checks that a PNG exists, not what it shows.
- **Missing for REALIZED:**
  - (a) The 10 DEV-only pins promoted to PROD.
  - (b) The StatusPanel item built (batch 238 item 2).
  - (c) The App.tsx fallback and AdvisorPublicProfile spinners, which are unowned by any parked set.
  - (d) A census at a printed zero on PROD, or one that enumerates every remaining rendering and its state.
- **Proposed: NOT REALIZED.** The ACCEPT is not met on what PROD serves: 10 state fixes are DEV-only, one is owed, and two bare
  spinners have no owner.

## FWD-12 -- An advisor reads a panel's structure from its surfaces, in both worlds

- **DONE WHEN:** "APPLIED -- every surface resolves to a role in one named-layer table (page, section strip, panel body, tile,
  inset, hover, selected, tooltip); each role has an opaque rung in the band world and in the light world, and neighbouring roles
  are separated by the same ratio in both worlds, under one opacity"
- **ACCEPT:** "on any delivered page an advisor sees a title strip distinct from its body and a tile inset from its panel, on the
  band and on a light panel alike; no two neighbouring roles resolve to one value, and no surface relies on a translucent overlay
  for its separation"
- **Round 2:** REALIZED for one page's first pass (/market); NOT REALIZED for the product. 32 overlays remained on /market.
- **Round-3 evidence:**
  - E4's surface half on /positioning: fb5d6116 and fe461611, on PROD. This seat graded fb5d6116 NOT_EVALUATED and fe461611's
    inks PASS by arithmetic with the rung choice unpinned.
  - PROD /positioning: `bg-white/N` 1 in 1 file. It is the 1px centre rule `PositioningSummary.tsx:1104` `bg-white/20`,
    enumerated in fb5d6116's message as a hairline.
  - Other `white/N` uses on /positioning are hairlines and inks: `border-white/10` 9 in Summary and 51 in HoldingsTab; text inks
    `text-white/50..90`.
  - The rungs: PROD `src/index.css` `body { --layer-strip 12%, --layer-body 18%, --layer-tile 24%, --layer-hover 30%,
    --layer-selected 35%, --layer-tooltip 9% }` (hue 221; band world; portal-wide by Andrew's word).
  - The words "layer" and "strip" appear 0 times in PROD `DESIGN.md`, in the token writer `design/brands/opal-capital.json` and in
    the generated `design/themes/opal-capital.css`. `design/brand/portal-layer-map.json` (CLOUD) is the round-2 before/after
    investigation map, not a role table.
  - Product-wide: `bg-white/N` 605 in 130 non-test files on PROD, by this draft's regex (round 2 printed 512 in 133 with a
    different scope). /market and MarketPerformance: 55 in 8 files.
- **Missing for REALIZED:**
  - The role table with BOTH worlds' rungs and each neighbouring pair's separation ratio. Not found in the contract, the token
    writer or the theme, and only band-world rungs are declared, in `index.css` rather than the one writer.
  - The pass on the remaining routes (batch 80's E4 "then the remaining routes by use"; round 3 did /positioning only).
  - The overlay census re-run per delivered page with each overlay mapped or enumerated.
  - A measured before/after render by the grader. The two E4 surface pins are NOT_EVALUATED or unpinned.
- **Proposed: NOT REALIZED.** Two pages (/market and /positioning) have passes. The two-world role table is not on record, and
  the rungs live outside the one token writer and the contract.

## FWD-13 -- An advisor can read every element in every state

- **DONE WHEN:** "APPLIED -- ink follows the ground of the element's CURRENT state, never its resting ground: every interactive
  role carries a state table of (ground, ink) pairs for rest, hover, selected, focus and disabled, delivered as per-role state
  tokens, and everything inside a highlighted element -- icon, badge, delta, chart label -- takes that state's ink"
- **ACCEPT:** "on a band, a highlight that paints a light ground turns its text dark; on a light panel, a highlight that paints a
  dark or indigo ground turns its text white; no text, icon or delta in any state falls below the contrast bar against the
  ground it actually sits on"
- **Round 2:** NOT_EVALUATED. Two contrast rulings that bound it (W2-S8, W1-S11) were open.
- **Round-3 evidence:**
  - ~D's walker `--contrast-table` on /positioning (self-run):
    - walk `20261003T000242Z`: 316 interactive pairs, 0 under;
    - after 4b, `20261003T094015Z`: 105 pairs, 0 under (the limb widened to text at rest);
    - 4c, `20261003T095441Z`: ETFs 86 and Satellites 112, 0 under.
  - This seat: 44d6a215 PASS on the walk's computed styles; b23917f7, d8d236a0 and 71a946e3 PASS on a test run; 661e49b3
    NOT_EVALUATED by test. All are on PROD.
  - The two rulings were made by ~D under batch 80 item 10:
    - S6 disarms W2-S8 for /positioning. This seat called it "supports the disarm for /positioning; the walk covers text
      controls only".
    - S7 rules W1-S11 latent. This seat confirmed that for `html.dark-mode`, and filed **S9: OPEN**, a second dark path driven
      by the OS.
  - PROD: 0 `@custom-variant dark`; `dark:` 304 uses in 27 non-test files.
  - PROD `index.css` state carriers: `--layer-hover`, `--layer-selected`, `--bg-hover(-light)`, `--delta-*-hover` and
    `[data-state-ink]`. There is no per-role (ground, ink) table across rest, hover, selected, focus and disabled, and DESIGN.md
    has no state clause by those words.
- **Missing for REALIZED:**
  - The per-role state tables, with every pair's ratio and the denominator of roles x states x worlds printed.
  - The state clause in the contract.
  - Every other delivered page walked: /market's highlights were not re-walked in round 3, and the rest were never walked.
  - The light-panel half of the ACCEPT.
  - R16's checker failing a planted pair, which is not on record.
  - Row S9.
- **Proposed: NOT REALIZED.** One route (/positioning) is walked clean on the band. There are no per-role state tables, and S9
  is open on PROD.

---

## Summary

| FWD | round 2 | proposed round 3 | one-line reason |
|---|---|---|---|
| FWD-1 | not graded (round 1: NOT EVALUATED) | NOT REALIZED | The new-person walk (the EXERCISED bar) has never happened |
| FWD-2 | REALIZED | REALIZED (carried) | PROD census unchanged (font-mono 1, Lato self-hosted); gaps W1-S8 and the never-measured alignment limb |
| FWD-3 | NOT REALIZED | NOT REALIZED | No ordered-scale census; the RSI exception rests on a CTO ruling outside the ratified text (v0.11 owed) |
| FWD-4 | PARTLY EVALUATED | NOT REALIZED | Accent pixel share and the counterexample walk were never measured; C-S11 open |
| FWD-5 | REALIZED | REALIZED (carried) | outline:none 0 on PROD; W3-S6 drop zones still unfocusable (the grader's call) |
| FWD-6 | not graded (round 1: NOT REALIZED) | NOT REALIZED | No rejection-by-clause with the author's agreement; DESIGN.md has no class labels or layer and state clauses |
| FWD-7 | REALIZED | REALIZED (carried) | 0 chart aliases, the status and data token sets are disjoint on PROD; the extreme-greed alias gap remains |
| FWD-8 | REALIZED | REALIZED (carried) | Import census on PROD: one chart library plus the word cloud, one icon set, one animation library |
| FWD-9 | his | NOT REALIZED | Andrew's word is not on record |
| FWD-10 | NOT REALIZED | NOT REALIZED | PAGE END on 1 of 25 routes; density never measured on populated fixtures |
| FWD-11 | NOT REALIZED | NOT REALIZED | 10 state pins are DEV-only; the StatusPanel item is owed; 2 unowned bare spinners |
| FWD-12 | REALIZED for 1 page, NOT for the product | NOT REALIZED | Only /market and /positioning have passes; no two-world role table; rungs outside the one writer |
| FWD-13 | NOT_EVALUATED | NOT REALIZED | /positioning walked clean on the band only; no per-role state tables; S9 open on PROD |

Proposed: **4 of 13 REALIZED** (FWD-2, FWD-5, FWD-7, FWD-8, all carried from round 2), the same four as round 2. Round 3's
work moved FWD-10, FWD-11, FWD-12 and FWD-13 forward but closed none of them.

## Open rows by FWD

Channel: `org/missions/D13/DSGN/DSGN_REBRND/surprise-channel/`. It holds 78 investigation rows, 14 adjudication rows (round 1)
and 37 remediation rows.
- `REMEDIATION_v1.md` was last written 2026-10-01 06:27 -0400 (before round 3). It still reads 5 REMEDIATED and 32 OPEN.
- Round 3's dispositions (rows S6, S7, S8, S11, S12, S14, S15 and batch 215 on S3) are NOT yet compiled into it. That compile is
  this seat's at L8.

| FWD | row | state at this read |
|---|---|---|
| 1 | W1-S34 (no site half) | remediation OPEN, owner CTO; RULING W answered it in text |
| 1 | W1-S36 (painting shadows) | OPEN; PROD `shadow-lg` 36 in 24 files, unchanged |
| 1, 13 | S9 (OS-driven `dark:` restyles four modals) | OPEN, INERT; PROD 0 `@custom-variant`, 304 `dark:` in 27 files |
| 1, 12 | C-S4 group: S2, W1-S9, W1-S10, W2-S5, W2-S6, W2-S7, W1-S27, W1-S33 (DECOMP_INVALIDATING: the page inversion) | no remediation row by design; served by round-2 cells R15-R17 and the portal-wide layers; NO closing row on record |
| 2 | W1-S8 (700 is the SemiBold face) | OPEN, Andrew's word |
| 3 | S3 (Global RSI bands) | superseded by batch 215 (RULED NO); remediation row still OPEN |
| 3 | W1-S14 (ladder hexes are literals in 3 writers) | OPEN |
| 3 | W1-S16 (`aum.ts` keys on old model names) | OPEN |
| 4 | C-S11 (accent "Neutral" label) | OPEN, unread since round 1 |
| 4 | W1-S20 (/portfolio-management half) | OPEN; ruling half in the text |
| 5 | W3-S6 (drop zones not focusable) | OPEN; 0 `tabIndex` in both files on PROD and DEV |
| 6 | C-S12 (DESIGN.md has no class labels) | OPEN; 0 `class:` on PROD |
| 6 | W1-S3, W2-S9, W1-S25 (the contract and tokens are not byte-equal) | OPEN, unread |
| 6 | C-S14 (the schema refuses an amended criterion id) | OPEN, owner CTO |
| 6 | W2-S15, W1-S24 (the silver law in auto-read carriers) | remediation OPEN; the named carriers read 0 "silver" on PROD (201bfe69). A candidate to close at the compile |
| 6 | Issuer rows W1-S6, W1-S12, W1-S17, W1-S18, W1-S35, W1-S21, W1-S23 | OPEN; they bind the next issuance; round 3 was FAST with no task orders |
| 7 | W1-S4 (two model-colour systems), W2-S11 (the /positioning asset-class legend is swapped) | OPEN, unread |
| 10 | W1-S29 (no terminator clause) | remediation OPEN; the clause was written by c9d303db (on PROD, NOT_EVALUATED). A candidate to close at the compile |
| 11 | W3-S5 (stray state treatments) | partly remedied: 10 pins DEV-only, StatusPanel owed (batch 238 item 2), App.tsx:443 and AdvisorPublicProfile.tsx:844 unowned, 3 items parked with owners |
| 11 | W3-S3 (the coverage checker reads PNG existence) | OPEN |
| 11 | W3-S1 | disarmed by S11 (d7141e5a on PROD); remediation row still OPEN; the partner-allowlist redirect parked pending a CTO ruling |
| 11 | W3-S4 | disarmed by S14 (pins on PROD); remediation row still OPEN; unnamed routes not swept |
| 13 | W2-S8 | disarmed for /positioning by S6 (this seat: supports, text only); light grounds rest on C4 per page; remediation OPEN |
| 13 | W1-S11 | ruled latent by S7; S9 contests the census scope |
| -- | S5 -> S8, S10 -> S12, S13 -> S15 | round-3 rows each remedied by a later row, with this seat's PASS on b23917f7, d8d236a0 and e2563c17 |

## Not verified by this draft

- Any render or browser walk. ~D's walks are self-reports.
- The served PROD bundle through the CDN.
- The CI conclusions (taken from this seat's records).
- The unit suites.
- The light-world rungs anywhere outside the three files searched by word.
- Whether the 35 remaining "silver" mentions are all legitimate (data tier, the Silver commodity, palette.silver).
- Rows W1-S3, W2-S9, W1-S25, W1-S4, W2-S11 and C-S11 on their merits.
