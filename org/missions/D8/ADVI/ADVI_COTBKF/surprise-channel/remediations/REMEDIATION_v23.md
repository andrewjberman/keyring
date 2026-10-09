# ADVI_COTBKF: remediations, round 32

<sweep_watermark>2026-10-09T09:53Z</sweep_watermark>

Graduated at round 32's L9 (ADJUDICATION_v25.md), round label v33: W59-S1, OPEN (a methodology ruling).

```json
[
 {
  "id": "ADVI_COTBKF-D2-W59-S1",
  "project": "ADVI_COTBKF",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "CB-af-1: the chain's SCHB and SCHZ close is the cottonwood silver canonical_prices row (field price, ticker key, source label yahoo_finance, same-day row); it sits at a CONSTANT ratio to today's Yahoo Adj Close (SCHB 1.0054, SCHZ 1.0216 on every sampled day) but 0.9214..1.0000 / 0.8777..1.0000 to Close. By the pre-written rule the class is other_source:yahoo_finance for both (adj_close_base needs 0.5%: SCHB misses by 0.04 pt, SCHZ by 1.7 pt).",
  "evidence": [
   "investigation row ADVI_COTBKF-D2-W59-S1",
   "org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~59/base_close_trace.md"
  ],
  "remedy": "Rule the price basis (as-traded close with dividends as cash, or a total-return adjusted close with no dividend cash), then measure the store across every held dividend payer: the share of rows that are dividend-adjusted, and the effect on day returns at ex/pay dates. Re-grade, and re-mint FWD-3's served tables under a pair if values or grades move.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v33",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v33"
  },
  "closed": true
 }
]
```
