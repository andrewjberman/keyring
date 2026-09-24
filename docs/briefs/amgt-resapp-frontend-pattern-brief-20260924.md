# BRIEF: the Security Analysis frontend, walked surface by surface, and the spec that brings it into pattern

**Author** `4.0.0_SA_CRO~Z` -- **Date** 2026-09-24 (rendered and measured 04:31Z-04:50Z, device OPAL_BLOOMBERG) --
**Mode** MIDSTREAM (AMGT_RESAPP is in flight) -- **Consumer** `1.0.0_SA_CTO~Z`, who cuts the L4 addendum for a fresh
canonical round from this; `2.0.0_SA_COO~Z` builds.

**Andrew-direct 2026-09-24 ~04:3xZ at the `1.0.0_SA_CTO~Z` terminal, verbatim (relayed as msg 25249):** *"I need
you to get an addendum for a fresh round by having 4.0.0_SA_CRO~Z do a comprehensive walk over the surfaces and spec
out how to completely upgrade the frontend to be in pattern and good design, because currently it is a nightmare
zone of walls of text and overlapping chaos, the brief they make will be the basis for the addendum."*

**Andrew-direct at this terminal, ~04:4xZ, verbatim:** *"Yes I recommend checking the earnings reports from The
asset management team in their "Research" sharepoint folder for a very loose reference, but also use opal brand
guidelines from deck_generation folder, use the existing "Positioning" and "Model Portfolios" pages, "Advisor
Intelligence" page "Benchmark" tab in Model Portfolios page as well, fixtures from "Philosophy" page particularly
those cards at the top of that page. There is a lot of prior art on teh Dashboard that we should absolutely reuse
for consistency, with charts being in opal brand guidelines colors and so on."*

**The standard is the ratified contract, not taste:** `portal/DESIGN.md` clauses C1-C12, enforced by
`portal/CLAUDE.md`. Every rejection below cites a clause number and points at a rendered screenshot in
`org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_FRONTEND_WALK_20260924/` (files `01`-`08`, `R1`-`R5`), with
the DOM measurements in `MEASUREMENTS.json` beside them.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

Honoured: no AMGT_RESAPP task order was opened for this brief, and the project's `phase` / `blocking` fields were
not read for it. The inputs were the served reality (the page rendered from the DEV working tree with captured
payloads), the PRD's page-design record (`AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md`, the "one header, five tabs"
drawing), the design contract, the reference pages, the deck brand bible, and one Research-folder earnings report.

Where it bent: earlier tonight this seat read the AMGT gap register (`GAPS.csv`) and the CTO's slate for the two
`/closer` trace briefs, so the open-work set is in this seat's context. Nothing below ratifies an open order: every
finding is a rendered property with a clause number, and the order of work is by user-visible gain, not by what is
open. The one place the leak could enter is Part I O2 (the identity header), which overlaps the Lead Panel closer's
step 3; it is stated as a render outcome, not as that step.

---

## PART I -- THE OUTCOME TERRITORY

The person is the portfolio manager or analyst who opens Security Analysis to decide whether a name deserves a
position. Read alongside the asset management team's own earnings updates (Part IV.9), which is what that person
writes and reads today.

### O1 -- The candidate thread: a PM opens Boeing and reads the Thesis on one screen, under one dark band

Sign in, open `/security-analysis/BA_US_Equity`, read the identity strip and the Thesis tab. What renders is one
`#0A1733` band (the identity header), white hairline panels beneath it, navy Lato at the contract's body size, and
the Thesis as a short recommendation line, a summary paragraph and headed sections whose sentences fit on one
screen with their evidence folded. Today the same journey is four stacked dark bands and 6,548 px of 12-px text
(Part IV.2, screenshot `02`). Coarse grain: one name, one tab, the default window, no export.

### O2 -- A PM reads the name's headline figures as formatted tiles, not a mnemonic list

Price, market cap, net debt, enterprise value, beta and short interest read as labelled tiles with units and
tabular numerals ("$161.9bn", "26,965m"), the Bloomberg mnemonic and full-precision value one hover away. Today
the overlay prints fourteen rows of `161867780096.00003 ABSOLUTE (full currency units) CUR_MKT_CAP` (screenshot
`03`). The person can dispute a tile by hovering it, and never has to parse a float.

### O3 -- Every sentence keeps its evidence, and the evidence stays out of the way until asked for

A drafted sentence shows its PASS face and a "cites 2 passages" affordance; opening it reveals the filing passage
and accession line. The verbatim-gate guarantee (every sentence over its cited passage, no `title=` tooltip
carrier, AMGT-rj-2) is preserved: the passages are in the document, rendered collapsed, never in a native tooltip.
A reviewer can still audit any sentence; a reader is no longer made to scroll 48 blockquotes to reach the Risks.

### O4 -- A PM reads the Model sheet as a table, and a refusal as one line per row

The fiscal table renders as a white heatmap panel with tabular numerals, one status icon and one navy sentence per
refused row ("DPS: not measured -- unit and sign convention not yet built"), and absent lines folded into a single
footnote. Today the DPS row repeats a 60-character refusal in ten red-bordered chips (screenshot `05`).

### O5 -- A PM reads the comparable set as the five columns that exist, and can open the twelve that do not

The CSC table shows the present columns; a disclosure "12 columns absent from the scanner registry" opens the
reasons. The ranker's basis reads as a status chip with the test statement one hover away. Today the table is 17
columns of which 12 print "ABSENT" in every cell, above a 696-character paragraph and a 15-line reasons list
(screenshot `04`).

### O6 -- A PM reads the Posture verdict as a headline and its six reasons as cards, with unresolved cites marked by an icon

HOLD reads as a stat tile with the comparable beside it; each reason is a numbered card with its cites folded; an
unresolved cite is a `status.warning` icon beside navy text, never amber text (screenshot `06`).

### O7 -- The Lead Panel's controls read as the Dashboard's controls do

Movement and Subject are segmented controls whose active state is weight and rule, the list/chart switch is the
same, the generation and resolution lines sit in a "Source:" footer as on the Dashboard panels, and the one purple
action in Security mode is Refresh. Today the view switch is a filled purple chip and the two caption lines sit as
10-px text above the rows (screenshot `01`).

### O8 -- Every panel on the page renders one of the four designed states when it has nothing to show

"Select a name from the Lead Panel" renders as the EMPTY state in a white panel with navy ink, LOADING as a
skeleton, ERROR as the danger icon beside navy text with a retry, exactly as `/market`'s tab panel already does
(screenshot `R1`). Today the empty Thesis is a centered sentence inside a full-width dark band.

### O9 -- The page passes the contract's render check, and the check can fail

A headless render of each of the six states plus its DOM measurement reads: one top-level band, Lato at 400 and
700 only, radii in {2,3,4,pill}, no box-shadow but the focus ring, zero text below 4.5:1 on its ground, one purple
fill beside the sidebar's, and the four states present. The same instrument reads today's page as failing each of
those (Part IV), which is what makes it a control rather than a checklist.

Outcomes that complete together are one: O2 and O7 both live in the Lead Panel; O3 and O1 both live in Thesis.
They are split because a build seat lands them separately and a CVO grades them separately.

---

## PART II -- WHERE THE BOUNDARY SITS

**This work owns:** `portal/src/pages/SecurityAnalysis/**` (the page shell, the five tabs, the twelve components,
the two hooks' render contracts), and only the presentation of the payloads the four routes already serve.

**This work relies on and does not change:** the four routes and their payload shapes (`lib/research/api/
scoped_amgt.py`, the served DTOs in `types.ts`); the shared chrome (`PageHeaderCleanBadge`, `TabNavigation`, the
sidebar); the panel system (`src/ui/components/panels/`), the designed states (`src/ui/components/states/`), `Stat`,
`MetricsRow`, `DataTooltip`, `HelperTip`, `BenchmarkHeatmap`; the brand tokens (`portal/design/brands/opal-capital.json`)
and the contract itself. Any field a tile or tooltip needs that the payload does not carry is a Served Runtime ask
to `2.0.0_SA_COO~Z`, not a page-side computation (C-SERVER-SIDE-RANKING and the "value must carry its claim" law
both bind).

**Architecture, and the tension named by the CTO:** Andrew's 02:47Z word, *"i wouldnt change AMGT_RESAPP page
layout architecturally"*, and his ~04:3xZ word, *"completely upgrade the frontend to be in pattern and good
design"*, are both honoured by the NARROW reading: one header, five tabs in the ratified order, the Lead Panel as
the discovery surface, the overlay as the identity header. Nothing in Part I moves a tab, adds a route or
re-splits the page. ONE FORK is named for Andrew rather than taken silently (Part VII, F1): whether the Security-
mode header becomes the page's one band, with the ranked list hidden as today, or the page stays band-less in
Security mode with the band spent on the Lead Panel only. The recommendation is the first.

**Sibling projects named:** `AMGT_RESAPP` (this page), `DSGN_REBRND` (the contract's author; its rows W1-S9, W2-S5,
W2-S7 are the known divergences this spec works within), `AMGT_CORPUS` and `AMGT_HARVST` (the water; nothing here
depends on them), and the two `/closer` lanes now running on Peers and the Lead Panel.

---

## PART III -- THE QUALITATIVE BAR

- **A reader can dispute the density.** After the change, a PM reading the Thesis tab on a 1440x900 screen sees
  the recommendation, the summary and the first section's sentences without scrolling, and reaches Risks in fewer
  screens than a printed earnings update takes pages. Today Risks begins at roughly the sixth screen.
- **A reviewer can dispute the pattern.** Every panel on the page is either the one band or a white hairline panel,
  and a reviewer who puts the page beside `/positioning` or `/market` cannot tell which was built first.
- **An auditor can dispute the evidence.** Any sentence's passage is still one click away and still in the DOM; the
  drafting harness (`__harness__/drafting.harness.cjs`) still passes its three properties.
- **A grader can dispute conformance by clause.** Each of C1, C2, C3, C8, C9, C10, C11 and C12 has a rendered read
  that reads FAIL today and PASS after, on the same instrument.

No number is set here. Tile counts, fold heights and evidence-collapse defaults are step 4 and 5 calls.

---

## PART IV -- THE SUBSTRATE: what exists, measured

### IV.1 The surface inventory, from the tree

One page, `portal/src/pages/SecurityAnalysis/` (5,909 lines across 31 files at portal `10141b6d0b`). Shell
`SecurityAnalysis.tsx` (93 lines): `PageHeaderCleanBadge` with the print action, a `sticky top-0 z-40` wrapper
around `LeadPanel`, `TabNavigation` over `SECURITY_ANALYSIS_TABS` (Thesis, Exec Management, Peers, Model, Posture),
one tab mounted at a time. Five tabs: `ThesisTab` 223 lines, `ExecManagementTab` 247, `PeersTab` 178, `ModelTab`
210, `PostureTab` 393. Twelve components: `LeadPanel` 402, `RankedList` 263, `RankedChart` 279, `StarredList` 176,
`SecurityOverlay` 162, `HeaderBrief` 134, `ThesisDriverChart` 160, `PrintExportAction` 107, `IdentityLine` 74,
`CheckFaceBadge` 63, `ProvenanceLine` 62, `GenerationCaption` 59. Two hooks: `useLeadPanelApi` (all four data
queries) and `useSecurityAnalysisState` (selection only). `types.ts` is 1,023 lines of served DTOs.

What each renders today, from the six captures (fixtures: the Boeing payloads captured 2026-09-15 plus tonight's
live rankings; 38 drafted sentences with 48 evidence rows, 165 fiscal figures, 12 officers, 12 peers, 14 header
figures):

| state | screenshot | page height | top-level bands | text chars | chars at <=12px | at 500/600 weight |
|---|---|---|---|---|---|---|
| Lead Panel list, no selection | `01` | 900 | 2 | 960 | 635 | 278 |
| Security mode + Thesis | `02`, `07` | 6,548 | 4 | 47,393 | 41,109 | 675 |
| Exec Management | `03` | 1,731 | 3 | 4,479 | 3,834 | 457 |
| Peers | `04`, `08` | 2,390 | 3 | 7,367 | 6,706 | 489 |
| Model | `05` | 2,122 | 3 | 5,148 | 4,472 | 534 |
| Posture | `06` | 2,519 | 3 | 7,304 | 5,641 | 493 |

Instrument: `scripts/ui-smoke.mjs` (headless Edge, auth stub) for the PNG; a sibling DOM pass for the numbers
(`MEASUREMENTS.json`, per text node: ground, contrast, font, size, weight; per element: radius, shadow, opacity).

### IV.2 Clause violations per surface, cited by number

**C3 (one band per page, panels white with a hairline).** Every tab body and the Lead Panel are
`Panel variant="mixed"` (20 uses) or `"chart"` (1), which resolve to the band (`Panel.tsx:62-67`). Measured: 2
top-level band containers with no selection, 3 on every tab, 4 on Thesis (the Big Thing chart panel is a fourth).
Contract allows one. The page has no white panel at all. Evidence: every screenshot; `bandContainersTopLevel` in
the JSON.

**C1 (Lato 400 and 700 only).** Lato is the only family (100% of characters), but weights 500 and 600 carry
278-675 characters per state (`font-medium`, `font-semibold` on labels, section heads and badges), and 8 characters
sit at 300. Contract forbids 300, 500 and 600.

**C2 and the type ladder (numerals tabular; body 16px, numeral 14px, label 13px, footnote 11px).** On Thesis,
34,480 of 47,393 characters render at 12px and 6,331 at 10px; 9px carries the "machine" badges. Across the five
tabs, between 87% and 90% of characters sit at or below 12px, which is below the contract's footnote size. The
overlay's figures print at full float precision without grouping (`161867780096.00003`) and left-aligned.

**C8 (one purple action per view; a segmented control never gets a filled purple chip).** The list/chart switch in
the Lead Panel is a filled `#5F3BE3` chip (screenshot `01`); Security mode adds the Refresh button beside it, so a
view carries two purple fills plus the sidebar's identity accent. The "machine" badge is purple text at 9px.

**C9 (4.5:1 on the resolved ground).** 280 characters on Thesis and 14-21 on the other tabs fail: every "machine"
badge is `#5F3BE3` on the panel's inner ground `rgb(25,38,67)` at 2.3:1. The contract's own table says the band
carries no purple (2.72:1). Everything else on the bands clears, because the white idiom is legal there; the
failures will multiply the moment a panel goes white unless each idiom is inverted by C5.

**C10 (density: generous inside, disciplined between).** The tab panels use `space-y-6` (24px) between the header,
the Lead Panel, the tab strip and the content; inside the panels the text ladder is compressed to 10-12px with
`space-y-2`. That is the inverse of the rule: tight inside, loose between.

**C11 (radii 2/3/4/pill, no shadow).** `rounded-lg` (8px) on the Lead Panel's four controls and the print action;
one `box-shadow` on the print action (`shadow-`). Measured 22-23 elements at 8px per state (most from the sidebar
chrome, which is out of scope, but 4 in `LeadPanel.tsx` and 2 in `PrintExportAction.tsx` are in scope).

**C12 (four designed states).** The empty Thesis renders as a centered sentence inside a full-width band, not the
EMPTY state (`PanelEmpty`, navy on white, with the one action). The Lead Panel's "no committed ranking" and the
overlay's ABSENT lines are 10-px captions, not states. `/market`'s error panel (screenshot `R1`) is the reference
that already exists.

**C6 (status and data disjoint; warning never text on a light ground).** Posture's "cite not resolved" lines are
amber text (`text-amber-300/80` class family) carrying meaning by hue; the Peers "DERIVED" basis is a green-tinted
chip. Both must become icon-plus-navy-text when the panel goes white.

### IV.3 The "walls of text", measured rather than felt

- Thesis renders 38 sentences, each as a 14-px line with a 9-px purple "MACHINE" prefix and a PASS chip, followed
  IN THE DOCUMENT by every cited passage as a 12-px blockquote (48 of them) and a 10-px uppercase accession line.
  Sentence, passage, accession, repeat: 6,548 px, six and a half screens at 900 px, 47,393 characters. The design
  intent (verbatim gate: the passage is in the DOM under its sentence) is right; the presentation (every passage
  open, every line under 12px, no headings above 12px bold) is the wall.
- Model renders 165 figures in a 10-column table at 12px inside a band; the DPS row prints the same 60-character
  refusal in ten red-outlined chips (screenshot `05`); six "ABSENT -- not on the model block" lines and five
  footnotes follow.
- Peers renders 17 columns, 12 of them "ABSENT" in every one of 18 rows, under a 696-character test statement
  (the longest single block on the page) and above a 15-line reasons list at 10px.
- Posture renders six reasons, each followed by two to four cite blocks in a sunken box, two of them 718 and 360
  characters long.
- The overlay renders 14 header figures as `value UNIT-DESCRIPTION MNEMONIC` rows, plus two axis captions and a
  peers caption.

### IV.4 The "overlapping chaos", measured

- Sibling text overlaps: 10-14 pairs per state, every one of them the collapsed sidebar's hidden labels against
  page content (an instrument artifact of the fixed sidebar, listed in `overlapSamples`). No content-on-content
  overlap was measured.
- The sticky wrapper: `sticky top-0 z-40` around a Lead Panel that is 907 px tall in Security mode. Measured at
  900 and 1080 px viewports after scrolling to the tab panel: 0 px of the tab content is covered, because the
  wrapper never engages as rendered. It is a latent hazard, not a live one: if a layout change made it engage, a
  907-px sticky band would cover the whole viewport. Recommended removal (Part V).
- What Andrew is most likely naming: in Security mode the eye meets four stacked dark surfaces (identity overlay,
  tab strip, Big Thing band, Thesis band) with 24-px gaps, so the tab content reads as a continuation of the header
  rather than as content beneath it. That is C3 and C10, not a z-order defect.

### IV.5 Prior art on the estate, rendered tonight (`R1`-`R5`)

- **Dashboard (`/market`, `R1`):** `PanelHeader` with title, help icon, a period segmented control whose active
  state is weight and underline, and a "Source: Bloomberg." footer. Two-up cards with a coloured left rule and an
  "Expand" affordance (Bullish/Bearish, Top/Bottom). A four-up KPI row (Daily Cloud, Global RSI, U.S. Regime, Fear
  and Greed). The tab panel below renders the C12 ERROR state correctly: danger icon, navy text, "Try again". The
  bands are still several per page (the W1-S9 divergence), so it is the pattern to copy for chrome and states, not
  for band count.
- **Positioning (`R2`):** a summary panel with a swatch legend, the five-model chip row in ladder order (C4), an
  "Expand details" secondary button, and the model selector as text tabs in the panel header.
- **Model Portfolios (`R3`, `R3b`):** partner selector in the page header, three text tabs (AUA, Benchmark, Peers),
  the Benchmark panel with Index/ETF and Gross/Net toggles and `BenchmarkHeatmap`. Its toggles are filled purple
  chips, the same C8 divergence as Advisor Intelligence; the spec follows the contract, not the divergence.
- **Philosophy (`R4`):** the five pillar cards: a navy graphic header with a 4-px indigo top rule, faint grid, big
  numeral and icon, over a white body with an eyebrow label, a title, one tagline and a "Read more" link. This is
  the one estate component that already puts a small dark moment over a white body, and is the shape for Posture's
  reason cards and for the Thesis section heads.
- **Advisor Intelligence (`R5`):** Mode/Interval/Window segmented controls in the panel header, a "Data Source"
  footer panel with a connection status line, and the AUM chart band. Filled purple chips there too.

### IV.6 Reusable components that already exist

`Panel` (`nested` and `heatmap` are the white variants), `PanelHeader` (title, subtitle, timestamp, source,
actions), `PanelFooter` / `SmartPanelFooter`, `PanelEmpty` / `PanelLoading` / `PanelError` / `PanelNoPermission`
(`src/ui/components/states/`), `Stat` (title, value, change), `MetricsRow`, `Card` with `CardHeader` (category,
title), `DataTooltip`, `HelperTip`, `DataAsOf`, `StatusBadge`, `ChartLegend`, `BenchmarkHeatmap`, `TabNavigation`,
and the catalyst `table`, `badge`, `description-list` and `dialog`. Nothing in Part V needs a new primitive.

### IV.7 The brand bible (deck_generation/DESIGN_BIBLE.md), where it adds to the contract

The same palette (navy, midnight, medium-blue, muted, cool-grey, electric-purple, white, charcoal); 60-30-10
weighting with purple the 10; Lato only; dark-to-light ramps for multi-segment fills; purple never inside a ramp;
no underlines beneath titles (separate title from body by weight and whitespace); large text never wraps; body
copy left-aligned. Charts keep their colour from the token `data` block (contract C6); the duration ladder is
locked (C4) and does not appear on this page.

### IV.8 The one earnings report read as the loose content reference

`Asset Management/Research/Alphabet GOOGL US/GOOGL earnings update 2Q26.pdf` (five pages, local OneDrive sync of
the SharePoint library; the folder holds 93 company folders). Its shape: company and ticker, period, one
recommendation line ("Maintain positions in PFOE and DIVZ"), a one-paragraph summary with the headline figures,
then fixed headed sections with short bullets: Headline results (Positives / Negatives), Geographic highlights,
Segment highlights, Headwinds and risks. Figures are formatted ("$119.8bn, +24% YoY, +23% cc"). That ladder --
recommendation, summary, headed sections, formatted figures, short bullets -- is the content pattern the Thesis
tab should read as, with the verbatim-gate evidence folded beneath each bullet. "Opal Earnings Brief Sept 2026.pdf"
in the team site's "End of Day Updates" folder was located but not read (Graph refused the PDF rendition and the
folder is not synced locally).

### IV.9 What is right and must be kept

The verbatim gate (every sentence over its passage in the DOM, no tooltip carrier); the one identity block
(`IdentityLine`); the PASS/REFUSE face (`CheckFaceBadge`); the three-state reads (SERVED / ABSENT / READ_FAILED)
and the generation caption's facts; the crossed-controls model of the Lead Panel; the Peers/Posture symmetry; the
"machine, never an instruction" marking. The spec changes how these are shown, never whether.

---

## PART V -- WHAT MUST BE TRUE, without sequencing it: the target pattern per surface

**Page-wide.**
- ONE band: in Universe mode the Lead Panel; in Security mode the identity header (F1 in Part VII). Every other
  container is `Panel variant="nested"` or `"heatmap"` with navy ink, inverted by C5 with output opacity 1.0.
- The type ladder from the contract: body 16px/400 for prose, numeral 14px/400 tabular for figures, label 13px/700
  for eyebrows and column heads, footnote 11px/400 for provenance and accession lines; nothing below 11px; weights
  400 and 700 only. Figures right-aligned in columns with a sign on every change value.
- Radii 4px on panels, 3px on buttons and inputs, 2px on chips, pill on status dots; no `box-shadow` but the focus
  ring; `rounded-lg` and `shadow-*` removed from the page.
- One purple fill per view (Refresh in Security mode; none in Universe mode), the active tab's label and underline
  and the sidebar carrying the identity accent. Segmented controls are weight and rule.
- Every panel renders `PanelEmpty` / `PanelLoading` / `PanelError` / `PanelNoPermission` from the shared states.
- Status colours appear as an icon beside navy text, never as text on a light ground (C6, C12); the "machine"
  marker becomes a navy outline chip reading "machine" at label size, with the sentence "a machine's view for a
  person to accept or reject" in the panel's subtitle once, not on every line.
- The `sticky top-0 z-40` wrapper is removed.

**Lead Panel (Universe mode) -- the band.** `PanelHeader` with title, the crossed controls as two segmented
controls (weight and rule), Starred as a toggle, list/chart as an icon segmented control, search at the right, and
the generation caption and resolution line in the panel's "Source:" footer (Dashboard pattern). Rows as today, with
rank, ticker, name and the score on one line at numeral size; headline placeholder removed until the feed carries
one.

**Identity header (Security mode) -- the band, replacing the overlay's list.** Left: display ticker, name, sector,
country, the crosswalk vintage as a footnote; right: "Back to universe" as a secondary button and Refresh as the
one primary. Below: a row of `Stat` tiles (price, market cap, enterprise value, net debt, beta, short interest,
average volume) with formatted values and units, each tile's `DataTooltip` carrying the full `ProvenanceLine`
(value, unit, mnemonic, definition, vintage, source) verbatim. Then the description sentence with its machine chip,
the posture line, and the feed as a three-item list with "Expand" (Dashboard's Bullish/Bearish shape). The two
axis captions become a single "On today's rankings: ..." footnote.

**Thesis.** One white panel. Header: title, the drafting source and vintage as subtitle, the held-uncited basis in
the footer. Body in the earnings-update ladder: the recommendation section first as a highlighted line, the
company description as the summary paragraph, then Investment thesis, Risks, Recommendation (and CEO bio when it
carries text) as sections with a 13-px bold eyebrow and a 4-px indigo top rule in the pillar-card manner. Each
sentence at body size with the PASS face and a "cites N passages" disclosure; the passages render beneath, in the
DOM, collapsed by default, quoted at body size with the accession line at footnote size. The Big Thing chart sits
in a 40/60 split beside the recommendation and summary (summary 40, chart 60), or as its own white panel when the
series is ABSENT, with the ABSENT reason as the C12 EMPTY state.

**Exec Management.** One white panel with the catalyst table: officer, role, role start, tenure (numeral,
right-aligned), profile (a secondary button or a navy link, "ABSENT" as an icon-plus-text cell), confirmed (a
status dot with label). The averages line as the footer. Already the closest surface to pattern.

**Peers.** One white panel. Basis as a `StatusBadge` ("derived" / "analyst-entered") with the test statement in
a `HelperTip`; comparable count, universe vintage and as-of as the subtitle. `BenchmarkHeatmap`-style table over
the PRESENT columns only, subject row bold, summary rows on a sunken `#E8EBF0` fill; an "Absent columns (12)"
disclosure below the table listing each with its registry reason at footnote size. Present-not-carried cells as an
em-dash with the reason in the column head's tooltip.

**Model.** One white `heatmap` panel with the fiscal table at numeral size, years as column heads, negative values
signed; a REFUSED row renders one danger icon and one navy sentence spanning the row, not a chip per cell; ABSENT
rows fold into one footnote naming them; the three scores as `Stat` tiles above the table with "not read" as
their EMPTY state.

**Posture.** One white panel. The verdict as a large `Stat` (HOLD / BETTER / WORSE / STEER CLEAR) beside the
comparable's display ticker as a navy link and the as-of; the machine chip once in the header. Reasons as numbered
cards in the pillar-card shape (navy numeral header, white body), each with a "cites N" disclosure; a resolved cite
quotes the passage at body size; an unresolved cite is a `status.warning` icon beside navy text. The evidence-
coverage sentence becomes a footer line.

**Dependencies named, not sequenced.** The four payloads carry every field the tiles need except a formatted
display string (the page formats; the payload stays raw). The C5 inversion of the 246 light-on-dark idioms across
the 18 files (per-file counts in `MEASUREMENTS.json`) is the bulk of the work and is mechanical. The drafting
harness and the tabs harness must keep passing; the render check (`__rendercheck__/renderCheck.tsx`) needs its
band assertions inverted. `DSGN_REBRND` rows W1-S9 (band-valued variants) and W2-S7 (secondary ink on the page
field) bound what a white panel may use for secondary text (`#6B7280` on a panel only). The dev-server render is
the instrument; E0 on the served stack is Andrew's act.

---

## PART VI -- STATUS, NOT OUTCOME-BEARING

Measured 2026-09-24 04:31Z-04:50Z on the local vite dev server (portal `10141b6d0b`, DEV) with the auth stub and
the captured fixtures; not the served PROD bundle:

- Canvas reads `rgb(244, 246, 250)` on every route; the page's containers read the band on every surface.
- Six Security Analysis states and six reference pages rendered; DOM measurements in `MEASUREMENTS.json`.
- Zero page errors on every capture. The Lead Panel list state shows tonight's true data: two rows at score 0.
- The idiom census: 246 light-on-dark or translucent idioms across 18 files in the page directory, the largest in
  `PostureTab.tsx` (29), `LeadPanel.tsx` (26), `ExecManagementTab.tsx` (26), `PeersTab.tsx` (24), `SecurityOverlay.tsx` (22).
- The sticky wrapper measured inert (0 px covered) at 900 and 1080 px.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM, and the fork

- **F1, the fork for Andrew (not taken silently):** in Security mode, is the identity header the page's one band
  (recommended: the discovery band is hidden then, so the count stays one), or does the page go band-less in
  Security mode with the band reserved for the Universe-mode Lead Panel? Both keep the architecture; they differ in
  what the eye meets first. The CTO's narrow reading is honoured either way.
- No signed-in walk was made; the auth-stubbed harness is the instrument here, and E0 remains Andrew's act.
- The served PROD bundle was not rendered for this walk (the DEV tree at `10141b6d0b` was); the Peers trace brief
  established that the PROD chunk carries this page.
- The Lead Panel's chart view, the starred-only view, the print action and mobile widths were not captured.
- Contrast was measured per text node against the nearest opaque ancestor; a gradient or image ground would read
  as its nearest solid colour. None were found on this page.
- The overlap count is a sibling bounding-box test and, as stated, its hits are the collapsed sidebar; it does not
  see visual crowding, which is why the density numbers carry the "chaos" finding instead.
- "Opal Earnings Brief Sept 2026.pdf" was located and not read.
- No component was changed, no deploy, no vendor call.

---

## Recommended order of work, highest user-visible gain first

1. **Thesis density and evidence disclosure** (O1, O3): the ladder, collapsed passages, section heads. This is the
   surface Andrew named and the largest measured wall.
2. **Identity header with Stat tiles** (O2): replaces the fourteen raw rows the eye meets on every tab.
3. **Band discipline page-wide** (O1, O9): tab panels to `nested`, one band, the C5 inversion sweep of the 246
   idioms, the type ladder and weights, radii and the shadow, the sticky wrapper removed.
4. **Model refusal and absence rendering** (O4).
5. **Peers present-columns table with the absent disclosure** (O5).
6. **Posture verdict tile and reason cards** (O6).
7. **Lead Panel controls and footer** (O7): segmented controls by weight and rule, captions to the footer.
8. **Designed states everywhere** (O8), then the render check re-asserted (O9) and the six captures re-taken and
   READ, per clause.

Each step is one pinned candidate, rendered by `scripts/ui-smoke.mjs` and measured by the same DOM pass, graded by
the CVO on the PNG and the JSON against the clause it names.

## Acceptance shape, per clause

For each of the six states (list; Thesis; Exec Management; Peers; Model; Posture), a rendered PNG at 1440 and the
measurement JSON, with: `bandContainersTopLevel == 1` (C3); `weights` keys within {400, 700} and `fonts` == {Lato}
(C1); no `sizes` key below 11 (ladder); `radii` within {2px, 3px, 4px, pill} for elements inside the page container
(C11); `shadows == 0` outside the focus ring (C11); `lowContrastChars == 0` (C9); `purpleFills` == 1 beside the
sidebar's in Security mode and 0 in Universe mode (C8); each panel's EMPTY, LOADING and ERROR states captured once
(C12); the drafting, tabs and posture harnesses green; and the six PNGs read by a person against the contract, the
rejection citing the clause. A pass on the JSON without the PNG read is care, not a control.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md
  PROJECT           AMGT_RESAPP (the L4 addendum's home; canonical flow resumes with this round)
  EXISTING PRD      org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md; page design
                    org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md
  CONTRACT          portal/DESIGN.md C1-C12; portal/CLAUDE.md; design/process/UI_VERIFICATION.md;
                    deck_generation/DESIGN_BIBLE.md sections A-C
  EVIDENCE          org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_FRONTEND_WALK_20260924/
                    (01-08 Security Analysis captures, R1-R5 reference pages, MEASUREMENTS.json)
  INSTRUMENT        portal/scripts/ui-smoke.mjs + the DOM measurement pass (to be checked in beside it)
  PRIOR ART         /market, /positioning, /portfolios (Benchmark), /philosophy pillar cards, /advisor-intelligence;
                    src/ui/components/{panels,states,Stat,Card}, src/components/{MetricsRow,DataTooltip,HelperTip,BenchmarkHeatmap}
  CONTENT REFERENCE Asset Management/Research/<company>/ earnings updates (93 folders, local OneDrive sync)
  SIBLING PROJECTS  DSGN_REBRND (W1-S9, W2-S5, W2-S7), AMGT_CORPUS, AMGT_HARVST; the Peers and Lead Panel closers
  MEASURED AT       2026-09-24 04:31Z-04:50Z, portal 10141b6d0b, workspace 3ed1c5e1f1
  RECORDS           msg 25249 (commission); Andrew ~04:4xZ at this terminal (reference set); 02:47Z layout word
```
