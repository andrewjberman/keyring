# /security-analysis walk -- findings for the next DSGN_AMGTV1 rounds (2026-10-09)

**Why:** Andrew-direct ~05:0xZ-05:1xZ (record `org/tier1_exec/2.0.0_SA_COO~D1/deliverables/ANDREW_DIRECT_20261009_051xZ_SECURITY_ANALYSIS_UI_WALK_SPINE_NEWS_DISCLAIMERS.md`):
the page is ugly; the news spine "makes no sense"; the news is "the worst part ... a shit ton of information laying around everywhere
haphazardly"; and there are "useless disclaimers and varying amounts of verbose and redundant disclaimers all over the place".
**Evidence:** signed-in walks of portal DEV `2d42e9b7` (deep, 121 shots) and `a6b75e25` (tabs, 36 shots), with every screenshot looked at.
The names walked are AMD US, Lenovo 992 HK, and ASML typed (the not-found path). The register is
`docs/briefs/dsgn-amgtv1-security-analysis-walk-findings-20261009.json` (23 findings, schema 1.0). Screenshots stay local.
**Status:** compiled by `2.0.0_SA_COO~D1` as input. The L1 brief is `4.0.0_SA_CRO`'s, and the cut is the CTO's round analysis.

## The shape of the problem

The page draws every served field and every absence, open, above the tabs. The result is a long scroll of plumbing (who collected what,
when, which input "Worked") wrapped around a little signal. Three moves fix most of it:
1. **One fact once.** Absence and provenance collapse to a single line, or to a single folded "About this data".
2. **Lead with the decision.** The identity band and tabs sit in the first screen; news and the spine become a designed view.
3. **Curate the dumps.** Model, Exec and Peers open on what a PM reads, with the full grids behind a fold.

## O1 -- the news spine

| id | what is wrong | done when |
|---|---|---|
| SAW-01 | The legend and bar colour show collection state (searched / partly / not), which is irrelevant under backfill. | No collection-state legend; colour means one thing about the company. |
| SAW-02 | Nine months of uniform 1-2-article bars; no price line, no labelled events (none on AMD; unlabelled circles on Lenovo). | Price/move overlay plus labelled top-move and top-news days. |
| SAW-03 | Hard to operate: a 2px click target, no hover summary, no range, no jump to key days. | Hover summary, range or top-N jump; empty days are not click targets. |
| SAW-04 | "Earnings dates are not on file ... so no earnings marker is drawn." on every name. | Nothing on the face when there is no earnings date. |

## O2 -- the news

| id | what is wrong | done when |
|---|---|---|
| SAW-05 | The same headline is drawn three times (Recent News, the "In the news" card, the spine). | One news surface; each headline appears once. |
| SAW-06 | 22 headlines date-ordered, mostly generic round-ups (AMD), or off-topic (Lenovo: "Treasury Yields Resume Their Rise"). | Ranked by relevance; round-ups grouped or folded; company stories first. |
| SAW-07 | Bare headline + source + timestamp; no why-it-matters, no themes, no link to the spine; the stated range does not match the items. | One-line why or theme tag; links to the spine day; the range matches. |
| SAW-08 | A word cloud of ~45 noisy tokens ("amzn", "calls", "plans", "strong"). | Removed, or at most 5 named themes with counts. |
| SAW-09 | A separate "In the news" card with "Mentioned 2 times" and "no social source is admitted yet". | Folded into the one news surface; no admission note. |

## O3 -- disclaimers and redundancy

| id | what is wrong | done when |
|---|---|---|
| SAW-10 | The Thesis says "the research pack is absent" seven ways. | Said once. |
| SAW-11 | The posture absence is a paragraph, repeated in the overlay fold and on the tab. | "No call on this name yet", once, on the tab. |
| SAW-12 | The "Where this page's data comes from" panel (five inputs, timestamps, "Worked") sits above the tabs. | One folded "About this data" at the page end. |
| SAW-13 | A date+source footer on nearly every block; three different as-of days on one page. | One page as-of; a source only where it differs. |
| SAW-14 | The chatter strip prints "Readings of ... (4 trading days behind ...). chatter: 43 of 95 covered names collected ...". | The two readings only. |
| SAW-15 | Exec: "roster did not resolve" four times; 25 rows of "not stated" / "per Bloomberg, not the filing"; three empty columns. | Only columns with values; the source named once. |
| SAW-16 | Peers: "currency not stated" twice, "5 of 17 columns ..." paragraph, an "Absent columns (12)" fold, n= on every cell. | The table and summary rows; one folded absence line at most. |
| SAW-17 | Lenovo tiles hold sentences ("Not shown: Bloomberg does not confirm this figure's currency"). | A dash; the reason on hover/focus. |
| SAW-18 | Four note lines under the segment tables; "Period 2..5" headings; the filing box (round 58 AV-zzj-1). | One unit line; periods labelled by end date or folded. |
| SAW-19 | Print preview titled `AMD_US_EQUITY`, "Printed 2026-10-09", and "date not stored with this figure" on every line. | Name + ticker title; long date; the clause at most once. |
| SAW-23 | Walker hits already ruled (money in quoted headlines, the HeroDialog contrast, an empty tspan, "Earlier month", the ASML not-found). | No action; recorded for coverage. |

## O4 -- page structure

| id | what is wrong | done when |
|---|---|---|
| SAW-20 | Everything is open above the tabs; the tabs start ~2,000 px down on AMD; the description is printed twice. | Tabs within the first 1440x900 screen; the description once; news and the spine in their own tab or one fold. |
| SAW-21 | "AMD US" and "a machine's view for a person to accept or reject" repeat at the top of every tab. | The subject is named once, in the identity band. |

## O5 -- the tabs

| id | what is wrong | done when |
|---|---|---|
| SAW-22 | Model: full-precision change figures with a paragraph per row, a ~70-row raw Bloomberg grid, and "no Base/Upside/Downside case" three times. | A curated 8-12-line summary; the full grid behind a fold; absent cases said once. |

## Ownership notes for the cut

- Every item is DSGN_AMGTV1 presentation (C-PRESENTATION-ONLY). Where a sentence is SERVED text (much of SAW-10, -11, -15, -16, -18),
  the page decides whether and where to show it but never rewrites it. Folding, de-duplicating and choosing one placement are page acts.
  Rewording a served sentence is an ask to AMGT_RESAPP.
- Ranking news (SAW-06) uses served fields only (e.g. `mention_count`). If relevance is not served, ranking is a RESAPP ask.
- The spine's price overlay (SAW-02) reads a served price series. If none is served for the timeline, it is a RESAPP ask.
