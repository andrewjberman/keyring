# IRPT_ANLREQ PRD v0.9 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~16:0xZ. **Delivery:** msg 7734 (and 7736). **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @c642900a88 (half_hash 06bd2303d500). **Compared against:** v0.7 @f9fea7f81b,
which this seat signed (4490e36e3e).
**Authority read:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261014_155xZ_SINGLE_YCHARTS_DATA_CALL_FOR_PRICING_OK.md`
@14360692df, line 15: "I am ok with a single data call to YCharts for pricing data." ADDENDUM v0.9 quotes it exactly.

**Verdict: SIGN.**

## What moved in the half (v0.7 to v0.9)

v0.8 changed only BRIEF COVERAGE row 5, which is outside this half. v0.9 changed FWD-7 and C-PRICES. FWD-1 to FWD-6 and every other
CONTRACTS row are byte-equal to v0.7.

- **FWD-7** now carries both of his limits:
  - "single": AT MOST ONE YCharts data call for the whole request;
  - "for pricing data": prices only, with no YCharts report, figure or PDF and no signed-in browser session.

  ACCEPT checks both in the trace (zero or one call, prices only), and each price carries its source. SOURCE keeps his 10-09 word and
  names the 10-14 relaxation. No annotation or seat name is inside DONE WHEN or ACCEPT.
- **C-PRICES** agrees with FWD-7:
  - SECHIST first, then the one batched YCharts call, then yfinance (labelled UNVERIFIED), then Bloomberg through its queue;
  - every price carries its source as a claim field.
- **C-SWAP is unchanged and consistent.** Its yfinance checker decides KEEP for an unknown holding, and its prices land in SECHIST,
  which C-PRICES reads first.

## One point for the record (not a reason to refuse)

ADDENDUM item 2 calls placing the YCharts call BEFORE yfinance the narrow reading. On the axis of how often YCharts is called, it is
not:
- Within the one-call cap, the YCharts-first order calls YCharts for any security SECHIST lacks.
- A yfinance-first order would call it only when yfinance also lacks a price.

The order is a quality choice: a paid price outranks an UNVERIFIED one, per CTO ruling 7546. His word allows either order, and the cap
binds both. It belongs on Andrew's list as a one-word question ("YCharts before yfinance, or only after?"). It does not gate this half.

-- 3.0.0_SA_CVO~DELL2
