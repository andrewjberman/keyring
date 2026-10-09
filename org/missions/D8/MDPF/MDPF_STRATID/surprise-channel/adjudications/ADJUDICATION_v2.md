# MDPF_STRATID -- round 1 L9 grade on the SERVED fire (dell1)

<sweep_watermark>2026-10-09T13:39Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T13:39:00Z. FWD-1's figures hold on the 13:30Z scheduled fire; the pair's check-A STOP is the producer's daily restatement (negative control); the page read of the Global view is still owed.

```json
[
  {
    "id": "MDPF_STRATID-C-S4",
    "project": "MDPF_STRATID",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T13:39:00Z",
    "one_line": "FWD-1 on the 2026-10-09 13:30Z SCHEDULED fire (log stream 2026/10/09 a20f67ef, run date 2026-10-08 written 13:31:40Z): the ACCEPT figures hold on the served artifacts -- Global SMA > ETF Strategies > PFDE = 410,420.98 = Cottonwood's served PFDE; Global's total rose by exactly that (opal_aggregate_aua 2,147,378,054.74 = base 2,118,155,241.25 + tax 28,812,392.51 + sma_additive 410,420.98); overlap measured (withheld []); PFDE under Client 0 times. The pair's check A printed STOP (per-firm figures for 2026-10-07 differ between the 10-08 and 10-09 runs), but the NEGATIVE CONTROL shows the same STOP between two PRE-D2 runs (10-07 vs 10-08 writes of 2026-10-06): the producer restates the prior day every run -- Inflection account counts up, 49financial model values by tens to hundreds of dollars, Cottonwood counts to 'absent', tax_coverage.business_active_accounts to None. Every class moved after the fire also moves with no fold, so check A as written cannot tell a fold move from the daily restatement; no moved figure is a PFDE or sleeve figure. Verdict: the fold is right and did not widen; the pair's STOP condition is mis-specified (rollback is the CTO/COO's call, my recommendation is no rollback). FWD-1's DONE WHEN also names a person opening the Global VIEW: that page read is still owed (Andrew or someone for him); this row grades the served data, not the page.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9: FWD-1 is graded on the scheduled run's served output by a seat that did none of the work; NEVER_WIDEN_PAIR_R1_GLOBAL_PFDE_FOLD.md: a per-firm figure that moves is a STOP.",
    "world_is": "FWD-1 on the 2026-10-09 13:30Z SCHEDULED fire (log stream 2026/10/09 a20f67ef, run date 2026-10-08 written 13:31:40Z): the ACCEPT figures hold on the served artifacts -- Global SMA > ETF Strategies > PFDE = 410,420.98 = Cottonwood's served PFDE; Global's total rose by exactly that (opal_aggregate_aua 2,147,378,054.74 = base 2,118,155,241.25 + tax 28,812,392.51 + sma_additive 410,420.98); overlap measured (withheld []); PFDE under Client 0 times. The pair's check A printed STOP (per-firm figures for 2026-10-07 differ between the 10-08 and 10-09 runs), but the NEGATIVE CONTROL shows the same STOP between two PRE-D2 runs (10-07 vs 10-08 writes of 2026-10-06): the producer restates the prior day every run -- Inflection account counts up, 49financial model values by tens to hundreds of dollars, Cottonwood counts to 'absent', tax_coverage.business_active_accounts to None. Every class moved after the fire also moves with no fold, so check A as written cannot tell a fold move from the daily restatement; no moved figure is a PFDE or sleeve figure. Verdict: the fold is right and did not widen; the pair's STOP condition is mis-specified (rollback is the CTO/COO's call, my recommendation is no rollback). FWD-1's DONE WHEN also names a person opening the Global VIEW: that page read is still owed (Andrew or someone for him); this row grades the served data, not the page.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "3.0.0_SA_CVO fetched the 12 pre objects by the PREFIRE_SNAPSHOT version ids and the 12 run-date 2026-10-08 objects (opal-data-assets portal/gold/mdpf/<scope>/<view>/), ran python org/missions/D8/MDPF/MDPF_STRATID/deliverables/2.0.0_SA_COO~S1/l4_read.py pre post at 13:4xZ: C OVERLAP-MEASURED OK, D1 OK (delta 410420.98), D2 OK, A STOP x3, B OK x3, L4-VERDICT FAIL",
        "negative control, same script: pre = 2026-10-06.json, post = 2026-10-07.json (both pre-D2 code): A STOP x3 with the same classes (inflection account_count 548->577, 49financial model_value small deltas, cottonwood count_basis measured->absent, tax_coverage business_active_accounts -> None)",
        "aws logs describe-log-streams /aws/lambda/mdpf-gold-lambda: newest stream 2026/10/09 [$LATEST]a20f67ef; s3 key portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-08.json LastModified 2026-10-09T13:31:40Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "An L9 grade record, not a hazard."
  }
]
```
