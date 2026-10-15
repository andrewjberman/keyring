# IRPT_DASHBD: CVO adjudication, round 132 (workstream B-49F, ~D2): the value-level read of the landed Cottonwood days

<sweep_watermark>2026-10-15T17:40Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T17:40Z, on msg 8480 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND130_132_131_B49F_DRAIN_END_20261015.md` @27847c126a, blob 1e264c2eb8; rounds 130 and 131 are ADJUDICATION_v96 and v97). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md`, against the CTO's round-128 analysis @cbd0289ecd ('ONE landed day (07-10) at the VALUE level ... every return value equal within 1e-12', and a load by the downstream reader). Round 132 is the issuer's direct LOCAL act (record RD_COT_VALUE_READ_R132.json @9d24eac8b6; no task order; `round-close-check --round 132` reads 0 orders, MAY-CLOSE). Re-run here: DB132-1-AC1 and DB132-1-AC2, 2 of 2 PASS (rc 0). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S35",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T17:40:00Z",
  "one_line": "Round 132 B-49F: the value-level read of the landed Cottonwood days. 2 of 2 PASS re-run (fresh re-derivation under pyarrow 25.0.1, load under the private 3.12.10 / pyarrow 14.0.2 interpreter). THE 07-10 READ IS VACUOUS ON RETURNS. In the landed 2026-07-10 file (20 columns, created_by parquet-cpp-arrow 14.0.2, 867 rows, every row day_quality NOT_MEASURABLE: the floor day has no base), total_return_daily, holdings_price_return, income_return, income_received and fee_amount are NULL on all 867 rows. The '1,734 float values over 7 columns' are market_value_eod and external_flow only (867 x 2). So 'every return value equal within 1e-12' compared ZERO return values; the CTO's bar is met in letter, not in substance. THIS SEAT CLOSED THE GAP by running the issuer's own fresh derivation (p132_value.fresh) on two days that carry returns. 2026-07-13: 861 rows, key set equal, 2,558 float values compared, including 836 measured total_return_daily, max abs diff 0.0, 0 non-float mismatches, loads under 14.0.2 (861 rows). 2026-10-14: 864 rows, key set equal, 2,555 float values compared, including 827 measured returns, max abs diff 0.0, 0 mismatches, loads under 14.0.2. So the served 14.0.2 returns equal the 25.0.1 reference exactly on the first and last Act 3 days; the other 62 days are not value-compared. 2026-07-10 itself is unchanged since Act 2 (ETag 0f65e010..., 21,655 bytes, 15:32:54Z) and reads 867 rows under both 14.0.2 and 25.0.1. THE CONSUMER LOAD: the CTO's analysis named holdings_performance. This seat confirms the issuer's correction: infra/aws/lambda/investor-reporting/holdings-performance/ holds 0 occurrences of account_return_daily, and the CTO's ADDENDUM 1 erratum agrees. The real consumer is the round-131 report-build function, which does not exist in AWS (v97). So 'loads under 14.0.2' is a load by a private interpreter that matches the layer's pyarrow version, not a consumer's load; the consumer's proof is its first build after the enable, as ADDENDUM 1 rules.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S92"
  ],
  "disposition": "UNDER_INVESTIGATION",
  "notes": "D2-S92 (ARMED, owner ~D2: the Commonwealth/Black Diamond era splice in one prefix) is named to HOLD it, not to dismiss it, so this row carries UNDER_INVESTIGATION; it bears on every consumer of these partitions.",
  "spec_asserts": "CLAUDE.md rule 24 (i): a check's population must be the claim's (a return comparison must compare returns); the CTO's round-128 binding: value equality within 1e-12 on returns and a consumer's load of the 14.0.2 file.",
  "world_is": "The landed 14.0.2 returns equal the reference exactly on 2026-07-13 and 2026-10-14 (1,663 measured returns between them). 2026-07-10 has no returns by construction. No consumer has yet loaded these files in AWS. The schedule stays DISABLED (v96).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T17:2xZ: DB132-1-AC1, DB132-1-AC2 PASS rc 0",
    "aws s3api get-object date=2026-07-10/data.parquet: ETag 0f65e010cf21932623cf6a81bcc848e4; 867 rows, 20 columns; null counts: total_return_daily, holdings_price_return, income_return, income_received, fee_amount all 867; day_quality NOT_MEASURABLE 867",
    "scratchpad valread_days.py (calls p132_value.fresh): 2026-07-13 values_compared 2558, max_abs_diff 0.0, rows 861 / 861, loader 14.0.2 861; 2026-10-14 values_compared 2555, max_abs_diff 0.0, rows 864 / 864, loader 14.0.2 864",
    "day_quality counts: 2026-07-13 MEASURED 836 / NOT_MEASURABLE 25; 2026-10-14 MEASURED 827 / NOT_MEASURABLE 37",
    "Grep account_return_daily in infra/aws/lambda/investor-reporting/holdings-performance/: 0; CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_128_20261015.md ADDENDUM 1 erratum",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/RD_COT_VALUE_READ_R132.json @9d24eac8b6"
   ]
  }
 }
]
```
