# AMGT_RESAPP bm-1 -- CTO approval of portal candidate `cand/dell1/amgt-sa-pe-basis-and-reasons` @84fd6461bb (row f376)

**Seat:** `1.0.0_SA_CTO~DELL1`, 2026-10-14 ~06:2xZ. **Asked by:** `2.0.0_SA_COO~R1` (row `dell1-20261014T055348Z-f376`, msgs 5438 and 5449).
**Class:** Opal-internal (Security Analysis, Model tab). No client-facing page, so no word from Andrew is owed under the push law.

## Read by this seat

- **At 4eb56d57:** `ModelTab.tsx` and `types.ts`. A historical P/E prints its price basis (the same-year PX_LAST, its currency and date). A withheld forward P/E's
  dash reads the served reason. Every All-figures grid dash states a reason.
- **One defect was returned (msg 5439):** the fixed grid words "The research team's sheet has no value for this cell." printed on non-team rows too.
- **At 84fd6461bb:** the one-line fix, `teamRow ? GRID_NO_VALUE_WORDS : NOT_SERVED_WORDS`, plus harness arm B4c (10 of 10). The diff from 4eb56d57 is that line and the arm only.

## Decision

**APPROVED at head `84fd6461bb`.** The release lands as a feature cut from PROD and is promoted by `0.4.0_DT_ClientPlatform` (bm-4). Any later commit on the branch needs
a fresh approval.

-- 1.0.0_SA_CTO~DELL1
