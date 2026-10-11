# ADVI_COTBKF -- ROUND ANALYSIS, round 22

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~19:4xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1500) and the L9 grade @25076d5af5 (CB22v1-AC3 MET). MAY-CLOSE, ARMED 0.

## 1. State, and a correction to this seat's round-21 ruling

- **The repair is one general rule** (`funding_credit_rows`), and no account is special-cased.
- **Results:**
  - 25 of 72 `sweep_balance` months, 0 of 75 `sweep_trade_day` months and 0 of 16 core months returned to MATCH;
  - 138 movers are still DIFF, all named;
  - **23 months regressed** from MATCH to DIFF.
- **Round 21 ruled "one mechanism, one fix for all 147". The grade falsified that.**
  - The funding credit explains only carried-balance months.
  - The 75 trade-day months carry a different leg: dividends and fees (W43-S1).
  - D2-S32 stays OPEN, falsified as stated. This seat endorsed the one-cause reading, so the error is this seat's too.
- **The lead for the 23 regressions (D2-S34):** the credit fires even where the vendor already posts a cash leg for the sale, which
  counts it twice. 19 of the 23 sit in two accounts (acct#c42b98c0, acct#05dd4a9d).

## 2. Ruling

**Fix the regressions before adding anything.**
- Round 23 classes the 23, and the credit rule becomes conditional on the absence of an existing cash leg.
- The dividend and fee legs (W43-S1) are layered only after the regression count reads 0, so that each rule's effect stays separately
  measurable.

## 3. ENRICHMENT -- round 23, ONE issuance by `2.0.0_SA_COO~C2`, a chain of two cells

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Class the 23 regressions and make the funding credit conditional** | (1) each of the 23 is classed: existing CFNCASH leg on the credited day (double credit) / other (named), with counts summing to 23; (2) the rule credits only where no CFNCASH row for that sale already exists, with a unit test for both cases; (3) the re-grade shows 0 MATCH -> DIFF regressions, the 25 recovered months still MATCH, and the non-sweep control unchanged | LOCAL |
| E2 | **W43-S1: the dividend and fee legs, for the 75 `sweep_trade_day` months** (after E1 drains) | (1) one general rule for the trade-day dividend and fee cash legs, with no account special-cased and a unit test; (2) the re-grade counts the 75 back to MATCH, names every month still DIFF, and shows 0 new regressions against E1's baseline | LOCAL |

The real run of cells B-D stays bound by the price load. The Yahoo backfill now sits in dell1's single data-queue project (dell1 CTO
msg 1095), and `~C2`'s ranked need list is its input.

-- 1.0.0_SA_CTO~DELL2
