# ENDPOINT (step 2, /endpoint --forward) -- ADVI_BDPRCE: every served Black Diamond price and lot for 49 Financial comes from a written rule and an exact source

Author `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~12:5xZ. Placement: DELL1, directive D8, macro ADVI.

**Andrew's words:**
- the DONE WHEN, confirmed "Yes as written" at 2026-10-13 ~12:1xZ:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_121xZ_BD_PRICING_RULES_DONE_WHEN_CONFIRMED_AND_CAP_CLARIFICATION.md`;
- the capped-lot basis, "Agreed with this positioning", at ~12:2xZ (lots read UNVERIFIED until exact data):
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_122xZ_CAPPED_LOTS_UNVERIFIED_SHARE_COUNT_SOURCES_PORTAL_SMOKE_WSJ_CREDS.md`;
- his constraint: "any 'estimation' is highly risky for performance reporting that needs to be exact".

**Brief:** `docs/briefs/bd-pricing-rules-brief-20261013.md` @f2171cae6c (`4.0.0_SA_CRO~DELL1`), O1-O8, with PART VIII confirmed.
**Lineage:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/BD_SHARE_COUNT_LINEAGE_AND_EXACT_SOURCES_20261013.md`.
**Prior art:** `ADVI_PRICES` (complete 2026-03), BD canonical pricing and valuation reconciliation. Its rules are what this project writes down, corrects and makes traceable.

**FWD-1 is the ONE journey** (rule 27); every later FWD enriches it. The ids are permanent, and this is the first emission.

```
  FWD-1  One 49 Financial advisor sees one untickered holding valued by a stated rule, and an analyst traces that price to its rule and trades
         DONE WHEN  EXERCISED -- on the served T-1 object, a seat opens ONE 49F client account holding ONE untickered security, reads its served price,
                    and from the record alone names the rule that produced it and the trades (by trade id) behind it; the recomputed price from
                    those inputs equals the served price
         ACCEPT     an Opal analyst asking "where did this price come from?" gets the rule and its trades without reading code
         SOURCE     brief PART I thread; DONE WHEN 1-2; O1, O2

  FWD-2  Every served 49F price comes from a rule written in ONE place (DONE WHEN 1)
         DONE WHEN  EXERCISED -- a census of every writer of the served T-1 price (the measured writers plus the four-times-a-day canonical writer) shows
                    each one calling the one written rule, or retired; a planted rule change in that one place moves every writer's output
         ACCEPT     an engineer changes a pricing rule in one place and no older copy survives anywhere
         SOURCE     O6; DONE WHEN 1

  FWD-3  Any served price traces to its rule and inputs (DONE WHEN 2)
         DONE WHEN  EXERCISED -- for a sample spanning every price source (override, trade median, interpolation, vendor), the trace names the rule and
                    inputs and the recompute equals the served value; the sample size is set in the PRD
         ACCEPT     an analyst can trace ANY served price, not only the thread's
         SOURCE     O1; DONE WHEN 2

  FWD-4  An untickered holding is valued at the median of DISTINCT trades
         DONE WHEN  EXERCISED -- the T-1 median counts each transaction once however many portfolio groups repeat it (S32: 830 of 5,366 asset-days moved
                    at measurement), served under FWD-7
         ACCEPT     a price is not weighted by how many groups hold the asset
         SOURCE     O2; ADVI_FIRMBKTS-D1-S32

  FWD-5  The price shown for a date is the same on every run
         DONE WHEN  EXERCISED -- two runs over the same inputs serve byte-equal prices; a same-date tie between sources is decided by a written
                    precedence (S33), with a planted tie as the arm
         ACCEPT     an advisor never sees a price change because of a sort order
         SOURCE     O3; ADVI_FIRMBKTS-D1-S33

  FWD-6  A past date's figure reads that date's trades
         DONE WHEN  EXERCISED -- each served reader keys on trade_date, not the transactions file day (DEC-6),
                    with a moved trade as the arm (S34)
         ACCEPT     a past date's gain or price is built from the trades of that date
         SOURCE     O4; ADVI_FIRMBKTS-D1-S34

  FWD-7  Every price this project moves, moves under a fix Andrew saw first (DONE WHEN 3)
         DONE WHEN  EXERCISED -- for EACH fix, a named before/after list (asset, date, old, new, and the dollar effect on the latest snapshot) is put to
                    Andrew BEFORE the deploy, and the deploy's read-back equals that list
         STANDING WAIT, qualified (rule 27): REASON -- these are client-visible prices and values on partner-facing pages; DISCHARGING ACT --
                    Andrew's review of that fix's named diff. The wait is per fix, never open-ended, and no other FWD waits on it.
         ACCEPT     no client-visible price changed without Andrew having seen exactly what would change
         SOURCE     O5; DONE WHEN 3

  FWD-8  Every served per-lot gain compares value and cost on one consistent basis (DONE WHEN 4)
         DONE WHEN  EXERCISED -- no served lot shows a gain from a scaled market value against an unscaled cost; a capped lot's value and gain read
                    UNVERIFIED (never an estimate) until FWD-9 supplies exact units and cost; the 64,629 capped lots (13 pct, at measurement) are read
                    one by one
         ACCEPT     an advisor never sees a large loss that exists only because the market value was compressed
         SOURCE     O7; Andrew's ~12:2xZ ruling; DONE WHEN 4

  FWD-9  Each lot's units and cost come from an exact source
         DONE WHEN  EXERCISED -- with BD's Units and Cost Basis switched on in the 49F unrealized export and the silver de-duplication keyed on the
                    lot (cell 1, reversible), each served lot carries units and cost from BD's export or the custodian's lot file (Schwab ULN/RPS);
                    FIFO-only lots read UNVERIFIED; BD versus FIFO is measured per lot with the denominator printed before any served value moves
         ACCEPT     no served lot's units or cost is a reconstruction from transaction history
         SOURCE     O8; lineage record section 4
```

**Not in scope:** MDPF valuation; IRPT performance math (a reader of these lots, and an FWD-7 blast-radius consumer); the exec-summary slots (ADVI_FIRMBKTS, which
stay off until FWD-8 serves).

-- 1.0.0_SA_CTO~DELL1
