# Review: IRPT_ANLREQ PRD v0.25 @b83ce81b5b, brief half (4.0.0_SA_CRO~TCKT, 2026-10-20 ~16:2xZ)

Brief: `docs/briefs/irpt-anlreq-report-engine-core-then-parity-brief-20261020.md` @e197f63e58 (this seat's).
Read: PRD ENDPOINT lines 105-140 (FWD-9 to FWD-12) and ADDENDUM v0.25 lines 676-708, at b83ce81b5b, against the brief's
PART I (lines 47-94).

## Outcome by outcome (brief -> ENDPOINT)

| Brief | ENDPOINT | Content carried | Verdict |
|---|---|---|---|
| O1 Andrew judges the Opal Overview on a sample run | FWD-9 (105-112) | Overview with no comparables, the PDF opened from the ticket, read beside the 2026-09-16 YCharts sample, his verdict; anything named becomes Overview work; it is not a gate on FWD-10 (the brief said "gate on the generator's base, not a build"; the PRD makes it not hold FWD-10, a sequencing call within L2's remit) | CARRIED |
| O2 Core | FWD-10 (114-123) | Cumulative return chart over one common window; periodic returns; standard deviation, Sharpe, Sortino, drawdown, alpha, beta against a stated reference; allocation side by side; Opal computes every figure. ADDS the stated window rule and the 2024-04-30 model floor (C-MODEL-SOURCE). The ACCEPT line keeps the brief's "without opening YCharts" bar | CARRIED (narrowed by contract, sound) |
| O3 Parity | FWD-11 (125-133) | Region and country, style and market cap, sector, bond sector, credit and maturity, fundamentals, scatter, standardized returns, holdings tables; starts as soon as FWD-10 is met. The brief's fundamentals field list (yield, expense, PE, ...) is summarized as "fundamentals"; the maps (`comparison_map.json`, `multi_map.json`) remain the field authority | CARRIED |
| O4 Words, not blanks | FWD-12 (135-140) | "not available for <comparable>: <reason>"; no construction cards in the PDF | CARRIED |
| Part II boundary | ADDENDUM 698-702 | ~G2 owns FWD-10, FWD-11 and C-MODEL-SOURCE; ~Y2 owns the swap leg, C-AUDIT-RECORD and FWD-9's filing; the IRPT_DASHBD TWR engine is relied on, not owned | CARRIED |
| Part V preconditions (model data source; audit record home) | C-MODEL-SOURCE, C-AUDIT-RECORD (CTO rulings @665110f9c2) | The firm-neutral return series and current weights; a schema'd analysis-report family | CARRIED |

## Proof gaps named (no refusal)

1. FWD-9 grades on a live Overview filing. Run 7b has not shown the four attachments yet (read 16:2xZ). FWD-9 cannot
   be graded before FWD-1's package lands; that is an order, not a defect.
2. The front-end note (ADDENDUM 694-696) lists rows 500c, 4664 and 37f6. Since then 5779 (PROD set @602ca19e) and 3067
   (DEV @381a835a) supersede 4664 and 37f6 for the stale-test fix (COO msg 11421). This is status, not ratified text.

Verdict: SIGN.
