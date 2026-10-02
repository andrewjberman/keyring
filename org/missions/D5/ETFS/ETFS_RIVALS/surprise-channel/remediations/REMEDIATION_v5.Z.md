# ETFS_RIVALS -- round 5 remediations (site-Z fabric): the L10 slug

Author: 3.0.0_SA_CVO~RV, 2026-10-02 ~13:25Z. Graduated at round 5's L9 (`adjudications/ADJUDICATION_v5.Z.md`, parts A and B).
Round 5 is drained at CLOUD 383e989b95 and all 45 orders are terminal, so this slug covers the whole project; it carries no
sweep watermark. Two items graduate, both INERT. The slug goes to 1.0.0_SA_CTO~Z with the review
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R5_REVIEW_20261002.md`, which carries the FAST interval's section.

```json
[
  {
    "id": "ETFS_RIVALS-Z-S13",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The shipped guardrails_config.json holds every issuer fund to one identity floor, 0.23, set by GQGU's newest resolution (0.2368). BASG resolves 1.0 but is held only to 0.23, so a BASG identity regression down to 24% would serve as updated. RIV-f-4 built per-fund issuer floors in guardrails.resolved_floor(), and by its own order did not change the shipped config.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S13 (2.0.0_SA_COO~RV)",
      "data/etfs/scripts/rivalfunds/guardrails.py resolved_floor() :209-214 (per-fund issuer dict) and guardrails_config.json thresholds.min_resolved_fraction.value.issuer = 0.23 at CLOUD 383e989b95",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md CALL 2 (@a2377e9ea8): no config change during the demo day"
    ],
    "remedy": "Per CRO~RV CALL 2: in the first round after the FAST lease, set per-fund issuer floors {BASG, GQGU} = round_down_2dp(measured newest-date resolved fraction - 2/n_noncash_lines), so one new unmapped line never flips a fund. Ship under the never-widen pair, and read both branches from the producer's rule at signing.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": false
  },
  {
    "id": "ETFS_RIVALS-Z-S14",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Served G4 security_market holds one date (2026-09-29) and carries px_close and total_return_index on 0 of 172 rows (gics_sector on 95%). No G4 price exists anywhere, so every A1 ranking runs on the CALL 1 holding-implied price (the fund's own market_value / quantity), and the census reports every G4 price missing.",
    "evidence": [
      "investigation row ETFS_RIVALS-Z-S14 (2.0.0_SA_COO~RV)",
      "served holding_contribution (FAST grades 2-6): price_source holding_implied on 3,439 of 3,509 security rows at 10-01, 0 rows from g4_*",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_FAST_GRADES_20261002.md grade 2 F1: the holding-implied path is what read a zero valuation as -100% (since fixed); every price-quality defect of the FAST interval rode this one path"
    ],
    "remedy": "The round-6 G4 history cell lands px_close and total_return_index for the covered securities, read-proved on served G4. The rankings then use g4_tri or g4_close first, with holding-implied as the disclosed fallback, and the caption states the price-source mix per fund and period.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v5",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v5"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO~RV
