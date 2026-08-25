# ANDREW-DIRECT 2026-08-25 ~16:46Z -- AGG SHOULD NOT EXIST ANYMORE

**Received at:** the `0.2.0_DT_PortfolioAnalytics~Z` terminal (site Z), 2026-08-25 ~16:46Z
**Recorded by:** 0.2.0_DT_PortfolioAnalytics~Z
**Channel:** direct to this seat, mid-turn, while I was investigating the AGG question dispatched by
0.0.0_AB_MSTR~Z (msg 9076)

## VERBATIM

> "Yeah agg should not exist anymore, we were in the process of puling that off the frontend"

Quoted exactly as received, including the typo. NOT paraphrased -- the phrasing is the ruling.

## WHY THIS ARRIVED

0.0.0_AB_MSTR~Z dispatched me (msg 9076) to classify a flag I had raised during the v2.1.167 promote:
1.0.0_SA_CTO~Z's brief listed SIX models books including AGG; only FIVE tabs render
(UST/ST/INT/LT/ULT). The assignment was to classify it as one of three, investigate-only:

- (a) AGG does not exist in the served artifact -- a doc correction, no defect
- (b) AGG exists and renders NOWHERE -- a real client-facing defect, priority above the cash row
- (c) AGG exists and is DELIBERATELY excluded -- not a defect, but the exclusion must be findable

**Andrew's word settles it as (c), at the sovereign level, before I finished.** It is deliberate and
it is in progress.

## WHAT I HAD MEASURED WHEN HIS WORD ARRIVED -- it corroborates (c) exactly

Served models artifact `/api/general/positioning/positioning_data.json` (8,059 B compressed,
generated_at 2026-08-25T11:06:11Z, data_as_of 2026-08-24), read with a minted RS256 bearer.
Note: the code docstring at `portal-proxy.ts:1083` claims "PUBLIC DATA (DEMO): No auth required" --
**it returns 401 without a bearer.** Stale docstring, recorded in passing, not chased.

**The two structures disagree, and that is the whole finding:**

| structure | keys | AGG present? |
|---|---|---|
| `portfolios` | 5 -- UST, ST, INT, LT, ULT | **NO** |
| `current_holdings` | 6 -- UST, ST, INT, LT, ULT, **AGG** | **YES** |

`current_holdings.AGG` carries **30 holdings, weight_sum 1.0000**, and every holding carries a
`model_breakdown` mapping its weight across the OTHER books (ST/INT/LT/ULT). That shape is an
AGGREGATE ROLL-UP across the models, not a sixth portfolio -- which is why it has no `portfolios`
entry with its own allocation/characteristics.

**The Positioning page renders 5 tabs because it reads `portfolios`, which has 5 books. That is
correct by construction, not a dropped tab.** So this was never the same defect class as the
PFDE/PFOE dropped holdings row, despite looking like it one layer up.

**The deliberate removal is findable in source, and it is dated ONE DAY before his word:**

- `src/pages/FactorTilts/FactorTilts.tsx:93`
  `transformed.summary = transformed.summary.filter((row) => (row.model as string) !== 'AGG')`
- `src/pages/FactorTilts/panels/FactorTiltOverviewPanel.tsx:265` -- "applied only to the **removed AGG
  view** (2026-08-24)"
- `src/pages/FactorTilts/panels/SummaryMetricsTable.tsx:73,195` -- "The 'AGG' scope..." / "applied only
  to the **removed AGG row**"

## THE RESIDUAL -- what his "in the process of" leaves open

The pull-off is **FRONTEND-ONLY SO FAR. The data plane still emits AGG**, and the type union still
admits it:

- `current_holdings.AGG` is still served, 30 holdings, in today's artifact
- `src/api/portal-proxy.ts:1399` -- `export type FactorTiltPortfolioId = 'UST' | 'ST' | 'INT' | 'LT' | 'ULT' | 'AGG'`
- `portal-proxy.ts:1040` "Model breakdown (only for AGG portfolio)", `:1069` "For AGG portfolio",
  `:1076` "Current holdings including AGG"

**NOT filed as a defect and NOT actioned.** He said it is in progress; a producer still emitting a
field the frontend has stopped rendering is the expected mid-state of exactly that process, not a
finding against it. Recorded so whoever finishes the pull-off knows the data plane and the type are
still to do, and so nobody re-derives the census.

⛔ **NOT AN AUTHORIZATION TO REMOVE ANYTHING.** He stated a direction and said it is already underway
at another seat. Moving served output is NEVER#3, and this seat is mid-promote on an unrelated change.

## CROSS-FABRIC RELEVANCE -- why this was broadcast immediately

At the moment his word arrived, 0.0.0_AB_MSTR~Z was holding portal `eaa094e6` off `origin/DEV`
(msg 9080) arbitrating a cross-fabric collision, and reported that **the LAPTOP fabric's change had
widened ~16:4xZ "from a nav entry to a FULL PAGE REMOVAL."** That is very likely this AGG pull-off.
If so, the two fabrics are working the same surface from opposite ends, and the arbitration MSTR~Z is
running needs this ruling in hand rather than after the fact.

## Disposition

Answer to MSTR~Z's dispatch: **(c) -- deliberately excluded, exclusion findable at
`FactorTilts.tsx:93` plus the three dated comments, and now ratified sovereign-level.** No defect
filed. Investigation closed by Andrew's word.
