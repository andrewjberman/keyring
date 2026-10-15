# Andrew-direct 2026-10-14 ~20:4xZ (dell1, `4.0.0_SA_CRO~DELL1` terminal) -- /open-calls answers: Global Trend Variant 1; satellite returns = models + the commodity ticker at its weight

## VERBATIM

> "Let's just focus on MDPF for now. Call 3, only opal staff see global, that is correct. therefore your assessment is
> correct with rec a, that is the easiest stitch. Call 4, check the actual satellite holdings, there is obviously some
> commodity ticker being included and im merely asking for the pro-rated performance of whatever that ticker is to be
> included with the actual weighted average performance of the constituent models. e.g., if a Satellite is 48% INT and
> 48% ST and 4% PHYS (or GLD, or whatever it is, seemingly is GLD but confirm), then we take the actual performance
> from the various windows for the two opal models and the gold ticker and average weight them to get the period
> performances."

The calls answered are cards 3 and 4 of this seat's /open-calls at ~20:3xZ.

## What it decides (verbatim scope; nothing wider)

1. **Call 3, the MDPF_CANON Global AUA Trend: Variant 1 (REC (a)).**
   - Per-model lines from 2024-11-01, as in `MDPF_CANON_GLOBAL_AUA_TREND_FULL_HISTORY_SPEC_20261014.md` @8025c4d7f1.
   - Andrew's stated fact: "only opal staff see global". The single-firm lines (49 Financial before 2026-05-15, and
     Inflection's Custom from 2026-05-15 to 07-19) are therefore shown on the Global view. The X2 / fe9b fold (A)
     concern does not hold the Trend's history.
2. **Call 4, satellite trailing returns:** each window = the constituent Opal models' actual window returns, weighted by
   their sleeve, plus the satellite's commodity ticker's window return at its actual weight. This is the J359 addendum-2
   rule, confirmed: R = (1 - g) x sleeve-weighted model returns + g x commodity-ticker return, with Andrew's example 48%
   INT, 48% ST, 4% gold.

## Measured, as Andrew asked ("check the actual satellite holdings ... confirm"), 2026-10-14 ~20:4xZ

- Served `s3://opal-data-cot/platinum/satellites/holdings.json` (as_of 2026-10-14), tickers outside each satellite's
  constituent model holdings (from `positioning_data.json` `current_holdings`):

  | Satellite | GLD (SPDR Gold Shares, commodities / Metals) | other non-model |
  |---|---|---|
  | 15 | 8.03% | CASH 0.37% |
  | 30 | 6.98% | CASH 0.40% |
  | 40 | 5.93% | CASH 0.42% |
  | 50 | 4.88% | CASH 0.45% |
  | 60 | 3.83% | CASH 0.47% |
  | 70 | 2.94% | CASH 0.72% |
  | 80 | 2.04% | CASH 0.97% |
  | 90 | **none** | CASH 1.06% |
  | 98 | **none** | CASH 1.06% |

  **The commodity ticker is GLD**, the only commodity row in any satellite.
- **Satellites 90 and 98 hold no commodity.** Confirmed at the source: Black Diamond's rebalancer definitions
  (`opal-data-assets/blackdiamond/cottonwood/bronze/rebalancer_model_detail/2026-10-14/df70eaaa-ecb0-4076-a586-545b80ad2dc6.json`
  "Opal Satellite 90" and `366d64d6-f53f-4b10-bd43-a0b2075495f4.json` "Opal Satellite 98") hold one sleeve, "Opal
  Long-Term Aggressive", whose tickers are CASH, CLIP, DIVZ, IDVZ, IEFA, IEMG, IJH, PCHI, PFDE, PFOE, QQQ, SPHY, SPYM,
  VEA, VUG and VXX. There is no GLD or other gold ticker, and no "gold", "commodit" or "metal" string. Under the rule they
  read as pure ULT (g = 0). If they should carry gold, that is a change to Cottonwood's model in Black Diamond, not to
  the producer.
- CASH sits inside the model sleeve in Black Diamond's hierarchy ("CASH - CASH" under the sleeve), so it is part of
  (1 - g), not a separate leg.

## Acts it starts

- `2.0.0_SA_COO~J1`: the addendum-2 producer change proceeds as specified, with the formula confirmed and no change to
  the oracle. It stays under its own never-widen pair (`1.0.0_SA_CTO~DELL1` msg 5809).
- `1.0.0_SA_CTO~DELL1`: route the Global Trend Variant 1 to MDPF_CANON (PRD addendum; producer plus portal per the spec's
  "Where it lands"). Approval row 19ae's successor is cut on Variant 1.

-- 4.0.0_SA_CRO~DELL1
