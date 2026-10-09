# ANDREW-DIRECT 2026-10-09 ~05:3xZ -- MDPF_SECHIST card A goes into the MDPF_DEMQUE Bloomberg queue

**Channel:** typed by Andrew at the `2.0.0_SA_COO~H1` terminal (dell1, Claude Code session), answering this seat's explanation of
card A and its two options ((a) release it as an MDPF_DEMQUE request, quoted first, paced; (b) keep it with him and site Z).
**Recorded by:** `2.0.0_SA_COO~H1`, same turn.

## VERBATIM

> "This can go into the BBG queue system that MDPF_DEMQUE is for"

## What it settles (as written)

- Card A -- the Bloomberg price-history backfill for the 1,319 `BLOOMBERG_SITE_Z` rows of
  `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~27/PRICE_NEED_FOR_SECHIST.csv` (FWD-2) -- goes into the
  MDPF_DEMQUE Bloomberg queue. It supersedes his 2026-10-08 ~17:5xZ "I will handle that with sitez"
  (`cooH1_ANDREW_DIRECT_20261008_175xZ_SECHIST_SH_T4_RELAND_YES_SITEZ_CARD_A_HIS.md` point 3) for the route.
- Open call `dell1-20261009T032427Z-deae` is answered (a).

## What it does not say

- No tier, pace, start date or field list was named. Those are the queue's (MDPF_DEMQUE ranks and paces; CTO ruling
  `CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md`). The request is filed at the tier `1.0.0_SA_CTO~DELL1`'s REC named
  (tier 2, msg 1566), quoted before any draw.
- It does not lift the production reserve or the bbg_budget ledger; the queue draws under them.

## Acts this seat takes on it

1. File the request `org/missions/D8/MDPF/MDPF_DEMQUE/requests/MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.json`.
2. Close call deae, ruled by Andrew, citing this file.
3. Tell `1.0.0_SA_CTO~DELL1` (decision), `2.0.0_SA_COO~Q1` (queue owner) and `0.0.0_AB_MSTR~DELL1`.
4. Cut `SH-t-5` (the series write of the returned rows, C-SERIES) in round 3, as told to Andrew.
