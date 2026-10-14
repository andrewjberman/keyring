# MDPF_DEMQUE -- round 9 L9, one judgment criterion ahead of the date-gated compile (dell1)

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T11:25:00Z. Asked by 2.0.0_SA_COO~Q1 msg 5454 (acked). Scope: `DQ9-t35-AC2` ONLY. The rest of
round 9's L8 (packet after the 2026-10-17 fire), the sweep watermark and the held W35-S3 disarm
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_DEMQUE_W35_S3_DISARM_HELD_20261013.md`) are NOT in this file; they land at the round-9 compile.

**L9 -- DQ9-t35-AC2 (judgment, MDPF_DEMQUE.TO-DQ-t35): MET.** The chain is the right one, and each of the 15 `read_by_a_page`
verdicts is supported by its cited evidence. The conclusion that matters is supported independently of the worker: no Cottonwood page
values these names from the Yahoo price file. Two limits are stated in row C-S28. The finding about the second consumer is filed on
ADVI_COTBKF's channel as `ADVI_COTBKF-D1-S1`.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-C-S28",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-14T11:25:00Z",
    "one_line": "JUDGMENT DQ9-t35-AC2 (MDPF_DEMQUE.TO-DQ-t35) MET: the price-file-to-page chain is the right one and all 15 read_by_a_page=false verdicts are supported; no Cottonwood page values FTHSX, PFORX or RPIFX from the Yahoo store; two limits stated.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "TO-DQ-t35 line 62: DQ9-t35-AC2 (judgment, graded by the CVO at L9, never self-graded) -- the chain from the price file to the client page is the right one and each read_by_a_page verdict is supported by the cited evidence.",
    "world_is": "DQ9-t35-AC2 MET. Graded on (a) the de-identified trace @3fc6879679 (blob 5e75a1c5de, verified) and (b) the worker's full VALUATION_TRACE.json read from git blob 411f47490d, whose sha256 370e9b0b...51e1 and 29,938 bytes equal MOVED_ACCOUNT_DATA.md. Account numbers were masked at read and none is reproduced here. THE CHAIN, re-read by this seat. Hop 1: the per-CUSIP Yahoo store. Hops 2 and 3: the builder's Yahoo input resolves through infra/logic/registry/legacy_addresses.json row cottonwood-silver-historical-prices to opal-data-cot/silver/historical_prices.parquet; HeadObject returns 404 live at 11:12Z, and config/ticker_lookup.json also returns 404. Positive control: silver/prices/canonical_prices.parquet in the same bucket returns 200 (LastModified 2026-10-09T13:41Z). So the Yahoo store has no input route into canonical prices. Hop 5: B_00.canonical_holdings.py L163-173 prices a snapshot row as market_value / units with source 'bd_snapshot', and ssm.tf L375-404 runs B_00 then A_05, C_01..C_06 and D_00..D_04, with no B_01/B_02/B_03. Hop 6: D_03.composition_artifacts.py builds composition from gold/canonical/holdings (L175-203). Hop 7: route from source. The production binding (opal-data-cot, FIRM_ID cottonwood) is as stated. THE 15 VERDICTS: each false carries its crosswalk status (13 NO_CURRENT_ACCOUNT_HOLDS_POSITIONS, 2 AWAITING_PERSON at 0.765), account_links ABSENT, and no applied household. That is the order's own test ('true only when you read the hop that puts that position's value on a page'). LIMIT 1 (how to read the count): '0 of 15 read by a page' means no APPLIED link. It does not mean these shares appear on no page. Three FTHSX rows carry 'exact units on 2026-10-09 yes' at a candidate current account whose household composition is served. Those shares are very likely valued on that page at the BD mark (57.67), inside a non-top-9 bucket that a top-9 read cannot see. What the count supports is: no page values them from the Yahoo file. LIMIT 2 (a consumer not cited): ADVI_COTBKF reads the same Yahoo store and fetched FTHSX and PFORX closes into the Cottonwood return history (deliverables/0.9.0_WK_ADVI_COTBKF~130/FETCH_HELD_27.csv: 1,579 rows each, 2020-06-29..2026-10-09). It reaches no page today: COTBKF PRD C-SCOPE-OUT says 'nothing on a page', and v0.6 says 'No reader of the Cottonwood return history is released'. That is filed as ADVI_COTBKF-D1-S1. Not read by this seat: the deployed portal edge version; canonical_prices rows (taken from the worker's read; not load-bearing once hop 2 is 404); the four candidate households' composition (taken from the worker).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO git rev-parse 3fc6879679:<de-identified trace> = 5e75a1c5de64b3f8e56e2f2f705377d27fc3ded4 (equals msg 5454)",
        "3.0.0_SA_CVO git cat-file -p 411f47490d | sha256sum = 370e9b0beb6459b0844fd08c940cd9b32fc163091080abc3ceb698ecbe8c51e1, 29938 B (equals deliverables/0.9.0_WK_MDPF_DEMQUE~27/MOVED_ACCOUNT_DATA.md)",
        "3.0.0_SA_CVO aws s3api head-object opal-data-cot silver/historical_prices.parquet -> 404; config/ticker_lookup.json -> 404; silver/prices/canonical_prices.parquet -> 200, 97443387 B, 2026-10-09T13:41:04Z (2026-10-14 ~11:12Z)",
        "data/cot/scripts/gold/build_canonical_prices_v2.py:158-171 + infra/logic/registry/legacy_addresses.json row cottonwood-silver-historical-prices (bucket opal-data-cot, template silver/historical_prices.parquet)",
        "data/cot/scripts/gold/B_00.canonical_holdings.py:163-173 (price = mv / units, source bd_snapshot); infra/aws/terraform/cot-pipeline/ssm.tf:375-404 (production step list)",
        "data/cot/scripts/gold/D_03.composition_artifacts.py:175-203 (composition built from gold/canonical/holdings)",
        "org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md:121 (C-SCOPE-OUT) and :278-288 (v0.6: no released reader); deliverables/0.9.0_WK_ADVI_COTBKF~130/FETCH_HELD_27.csv (FTHSX, PFORX returned)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 judgment record, not a hazard: DQ9-t35-AC2 graded MET by 3.0.0_SA_CVO, which did none of the work; the forward hazard on the second consumer is carried by ADVI_COTBKF-D1-S1."
  }
]
```
