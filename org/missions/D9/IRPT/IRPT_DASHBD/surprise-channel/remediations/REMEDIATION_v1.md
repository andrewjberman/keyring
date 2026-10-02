# IRPT_DASHBD -- round 1 (workstream B) remediations

<sweep_watermark>2026-10-02T02:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02. Graduated at ADJUDICATION_v1.md: 5 rows. Closed here on this seat's reads: S3, S4, S5. OPEN: S6 (limb (e) only) and S8 are in no round-2 cell and come back to 1.0.0_SA_CTO as an addendum to the round-2 analysis (round 2 cuts DB-b-5 and DB-b-6; E2 is row S12). Round label v2 (round 2).

```json
[
  {
    "id": "IRPT_DASHBD-S3",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The adapter valued in-kind legs at a whole position's market value times the quantity (F01, 3,277.8x in aggregate) and never excluded WD withholding from income (F06); the round-1 thresholds measured over that output were artifacts and were quarantined.",
    "evidence": [
      "investigation row IRPT_DASHBD-S3; repairs at 35e325eedc",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py and sources.json at CLOUD HEAD (this seat, 2026-10-02 ~04:5xZ): sources.json declares price_column closing_price (basis measured) and withholding_code_column sb_cd (basis measured); the producer raises SystemExit on an undeclared price column rather than substituting another quantity",
      "served gold read by this seat 2026-10-02 ~04:5xZ, s3://opal-data-49financial/irpt/49financial/gold/: dim_return_method/method_version=1 (1 row, LastModified 2026-10-01 15:12:57Z): flow_convention END, fee_basis GROSS_ONLY, tolerance 0.001244, large_flow_share 0.002535, band [-0.5, 0.5], comparability_max_excluded_weight 0.002488, tieout_tolerance_proposed 0.037, no tieout_tolerance column; account_return_daily 559 of 559 partitions, 1,105 rows, 6 accounts: return_basis TWR 1,071 / NOT_MEASURABLE 34 (no HOLDINGS_INCOME_FALLBACK), guard_state GRADED_AGREED 700 / NOT_GRADED_OUTSIDE_DOMAIN 377 / GUARD_NOT_REACHED 20 / GRADED_DISAGREED 8, emitted total_return_daily 1,071 all inside the band (min -0.0735, max 0.0484), 0 NOT_MEASURABLE rows with a number",
      "the quarantined tolerance was 1.0677%; the served re-measured tolerance is 0.001244 (amendment 5 (h): re-measured after (c)-(g))"
    ],
    "remedy": "Done: both defects repaired in the producer, the thresholds re-measured after the method amendments and served in dim_return_method.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S4",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Three defects in the order's own text: (a) a cross-account cash leg was INTERNAL at account grain; (b) advisory fees stayed inside a series labelled gross; (c) the served method row could name a convention the returns were not computed under.",
    "evidence": [
      "investigation row IRPT_DASHBD-S4; issuer amendment 5 @f4f57b6fe4 clauses (c) account boundary and (d) fee basis",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py and sources.json at CLOUD HEAD (this seat, 2026-10-02 ~04:5xZ): legs resolved INTERNAL by pair-match enter F_t at account grain (comment at :475, census key resolved_pair-match :509-510); FEE-MANAGEMENT, -VERIFIED and -INFERRED map to one class entering F_t (:195-197, :568); emit_method_row's winner argument is passed by neither call site (:1802, :1856), so flow_convention is always END",
      "served gold read by this seat 2026-10-02 ~04:5xZ, s3://opal-data-49financial/irpt/49financial/gold/: dim_return_method/method_version=1 (1 row, LastModified 2026-10-01 15:12:57Z): flow_convention END, fee_basis GROSS_ONLY, tolerance 0.001244, large_flow_share 0.002535, band [-0.5, 0.5], comparability_max_excluded_weight 0.002488, tieout_tolerance_proposed 0.037, no tieout_tolerance column; account_return_daily 559 of 559 partitions, 1,105 rows, 6 accounts: return_basis TWR 1,071 / NOT_MEASURABLE 34 (no HOLDINGS_INCOME_FALLBACK), guard_state GRADED_AGREED 700 / NOT_GRADED_OUTSIDE_DOMAIN 377 / GUARD_NOT_REACHED 20 / GRADED_DISAGREED 8, emitted total_return_daily 1,071 all inside the band (min -0.0735, max 0.0484), 0 NOT_MEASURABLE rows with a number; fee_amount_reason FEE_RAIL_UNUSED on 1,105 of 1,105 rows",
      "PRD v0.6 ruling 24: 'The served flow_convention stays END'"
    ],
    "remedy": "Done: (a) and (b) by amendment 5 (c) and (d) in the producer; (c) removed by ruling 24 and by the producer never passing a winner. Not re-derived: the per-account census of legs entering F_t by each route (amendment 5 (c)).",
    "owner": "2.0.0_SA_COO~P",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S5",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "The guard substituted a holdings return over a different population (priced long basket) for the whole-account return, and the plausibility band checked a raw value that was then discarded.",
    "evidence": [
      "investigation row IRPT_DASHBD-S5; PRD v0.4 rulings 17-19 (prd/IRPT_DASHBD_PRD.md:372-392)",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py and sources.json at CLOUD HEAD (this seat, 2026-10-02 ~04:5xZ): 'PRD v0.4 RULING 19: THE ONE GATE, run AFTER selection, on the value that is EMITTED' (:936), band read from the method row (:961-962); 'HOLDINGS_INCOME_FALLBACK is never emitted' (:1686)",
      "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json 0.2.0: return_basis enum ['TWR', 'NOT_MEASURABLE']; supersedes/changes: 'return_basis LOSES the member HOLDINGS_INCOME_FALLBACK'",
      "served gold read by this seat 2026-10-02 ~04:5xZ, s3://opal-data-49financial/irpt/49financial/gold/: dim_return_method/method_version=1 (1 row, LastModified 2026-10-01 15:12:57Z): flow_convention END, fee_basis GROSS_ONLY, tolerance 0.001244, large_flow_share 0.002535, band [-0.5, 0.5], comparability_max_excluded_weight 0.002488, tieout_tolerance_proposed 0.037, no tieout_tolerance column; account_return_daily 559 of 559 partitions, 1,105 rows, 6 accounts: return_basis TWR 1,071 / NOT_MEASURABLE 34 (no HOLDINGS_INCOME_FALLBACK), guard_state GRADED_AGREED 700 / NOT_GRADED_OUTSIDE_DOMAIN 377 / GUARD_NOT_REACHED 20 / GRADED_DISAGREED 8, emitted total_return_daily 1,071 all inside the band (min -0.0735, max 0.0484), 0 NOT_MEASURABLE rows with a number; the 8 GRADED_DISAGREED rows: 8 of 8 FLOW_UNRECONCILED with a null total_return_daily",
      "the issuer's rewritten check org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_1_ac2_guard_seam.py (last change ea2e7145ee) run live by this seat: 40 of 559 partitions sampled, 65 rows, DB-1-AC2 PASS"
    ],
    "remedy": "Done by rulings 17-19 in the producer, the contract and the served gold.",
    "owner": "2.0.0_SA_COO~P",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~P",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S6",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "mechanism": "Of five findings, four are remedied (unknown cash, run-window inception, valuation intervals, the four checks). Limb (e) stands: the SHARED code table classes foreign tax with the WD marker (FTP/FC/WD, FTR/FC/WD) as EXTERNAL capital, and the served 49F engine executes that table; only this adapter overrides it.",
    "evidence": [
      "investigation row IRPT_DASHBD-S6; issuer amendment 5 clauses (e), (f), (g), (i)",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py and sources.json at CLOUD HEAD (this seat, 2026-10-02 ~04:5xZ): unknown cash propagated as a state (:676, :686), SOURCE_LAG for an absent partition (:120, :302), first_data_dates over the account's whole history (:773-776), intervening valuations chained (:1211-1215); sources.json withholding_is_neither_flow_nor_income true (override 'held', amendment 5 (g))",
      "the issuer's rewritten check org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/checks/r1/p1_1_ac2_guard_seam.py (last change ea2e7145ee) run live by this seat: 40 of 559 partitions sampled, 65 rows, DB-1-AC2 PASS",
      "org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json at HEAD (last change 5bb3b2626d, 2026-08-11), 187 rows: FTP/FC/WD partition EXTERNAL (rule wd-generic, 2,449 rows, 36,759.84 USD abs); FTR/FC/WD EXTERNAL (4 rows, 233.66 USD); the FC/FC rows of both codes read INTERNAL (rule foreign-tax)",
      "comp-find 'SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811' over data/ and infra/: the served engine's reader data/assets/scripts/gold/runners_49f/a05_ref_txn_classification.py:4,42,44 and this adapter's sources.json; comp-find over org/missions and org/surprise_channel for the FTP/FC/WD class: 2 hits, both this row (no other carrier)",
      "limb (c) was not replayed on served data: the January example in S6 is a review fixture, not a served account-day"
    ],
    "remedy": "Limb (e) only, IN NO ROUND-2 CELL (the round-2 analysis lists E1 to E3; issuance 97eaff05ff cuts DB-b-5 (E1) and DB-b-6 (E3), E2 is row S12): the table's owner (4.0.0_SA_CRO's file) and the served 49F engine's lane decide whether FTP/FC/WD and FTR/FC/WD are EXTERNAL, with ruling 6.5 ('foreign-tax withholding is not a withdrawal') as the spec. INERT by the row's own magnitude (about 15 USD per row, under a basis point on a six-figure account). Placement is 1.0.0_SA_CTO's by addendum.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": true
  },
  {
    "id": "IRPT_DASHBD-S8",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "fact_trn carries no usable per-event identifier (none of 17 identifier-shaped columns is unique per row), so the review's duplicate-input remedy has no key to dedup on and no verified invariant; 1,099 of 3,209,771 rows (0.034%) share the ten columns the producer reads, an upper bound and not a duplicate count.",
    "evidence": [
      "investigation row IRPT_DASHBD-S8 (all 561 partitions read)",
      "data/assets/scripts/gold/irpt_reporting/account_return_daily.py and sources.json at CLOUD HEAD (this seat, 2026-10-02 ~04:5xZ): account_values() now REFUSES a balance partition carrying more than one row for an account before it sums (:755-770), citing S8: the dim_balance invariant is enforced, not only observed",
      "comp-find for a per-event key carrier over org/missions/D9 and org/surprise_channel: 3 hits, all this row or DB-b-1's own proof (no other carrier)"
    ],
    "remedy": "IN NO ROUND-2 CELL: an upstream silver change (a stable per-event key on fact_trn) in the Schwab ingest lane, first asking whether the raw CRS record carries a key silver drops. Until then the producer keeps no dedup on fact_trn and the 0.034% stands as a disclosed upper bound. Placement is 1.0.0_SA_CTO's by addendum.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "closed": false
  }
]
```
