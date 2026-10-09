# DSGN_AMGTV1 -- ROUND 58, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~06:2xZ)

**Inputs:**
- the round-58 drain-end (`2.0.0_SA_COO~D1` msg 1825), with its candidate review in rulings batch @6c538a0bfd section G;
- DEV landed `c0c6f570` (re-cut on `c34ff9c0`, the same 2 files, +8 -3; `0.0.0_AB_MSTR~DELL1` msg 1862);
- Andrew's walk register `docs/briefs/dsgn-amgtv1-security-analysis-walk-findings-20261009.json` @5786933a9c (SAW-01..23, record
  @1725deb826);
- the cut plan `deliverables/2.0.0_SA_COO~D1/round59/ROUND59_CUT_PLAN.md` @f37fb3dc95, read whole.

## 1. Graded

- **AV-zzj-1 (RESAPP round-80 R4): MET on DEV.** The signed-in walk at 05:40Z: beside AMD's drawn segment table, the filing box reads
  "The filing text for these segments is not stored for this name yet." It no longer contradicts the table.
- **FWD-1:** the redesign is on PROD (`bf780f94`, portal-v2.1.205). Andrew's own PROD walk is still owed.
- **Andrew's verdict on the page** (~05:0xZ): it is ugly, the news is "the worst part", and the disclaimers are redundant. Measured on
  DEV `2d42e9b7`:
  - a headline drawn three times;
  - the Thesis absence said seven ways;
  - "roster did not resolve" four times, plus 25 "not stated" rows;
  - tabs starting ~2,000 px down.

  That is the round-59 scope. It is FWD-27 (plain words) and the layout outcomes, not a new endpoint.

## 2. Rulings

- **R1, the cut plan is adopted as written:** six cells A-F with disjoint write sets, the footers (SAW-13) after A-F land, and no cell
  editing `reasonWords.ts`. Each cell moves where a sentence sits, not its words.
- **R2, IdentityLine (the asked ruling): YES.** The page says the security's identity ONCE, in its header. The tabs drop their own
  "AMD US" lines. Cell C removes the mount from all five tabs: it owns the decision, and the mount lines are one-line edits. Cells D-F do
  not touch those lines. This answers Andrew's "redundant" directly.
- **R3, absences:** each absence is said once, where the reader needs it.
  - A page-composed sentence that repeats another is removed, not reworded.
  - A served reason (the five dossier notes, the Exec `source_item`) is shown ONCE, folded under one "What is not on file" line per
    tab.
  - Rewording served text is not asked this round. Folding answers "said seven ways"; it waits on RESAPP only if the folded words
    still read badly.
- **R4, the spine (SAW-01..04):** the page marks the top days from served `breakout_ratio` / `z_score`, labels the served events, and
  drops the searched/partly/not legend (Andrew: irrelevant under backfill). No price line until the route serves one.
- **R5, news (SAW-05..09):** one news surface, each headline once, sorted by the served `mentions` the "In the news" items already
  carry. The feed's relevance ranking and a why-line wait on a served field. The word cloud shows its top terms only.
- **R6, RESAPP asks, routed to `2.0.0_SA_COO~R1` for its next round:**
  1. a per-day price series on the timeline route;
  2. a relevance/mention field on feed items;
  3. the print PDF's "date not stored with this figure" said once, not per line (`render_pack.py:486`).

  The fourth ask (shorter served reasons) is NOT made, per R3.

## 3. ENRICHMENT LIST (round 59, ONE issuance by `2.0.0_SA_COO~D1`, up to 6 workers)

Cells A-F as in the cut plan, with R2-R5 applied. The footer cell (SAW-13) is cut after A-F merge. Each build cell carries at most three
mechanical criteria, and the round closes on a signed-in walk read against the register (23 of 23 findings dispositioned).

## 4. ACTS ONLY ANDREW CAN DO (cited)

- FWD-1's walk of the redesigned page on PROD (hand-over, "Acts only Andrew can do").

-- 1.0.0_SA_CTO~DELL1
