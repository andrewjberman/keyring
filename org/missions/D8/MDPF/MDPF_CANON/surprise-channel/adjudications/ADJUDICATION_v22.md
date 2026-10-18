# MDPF_CANON -- FWD-10 ADVI leg L9 grade (dell1)

<sweep_watermark>2026-10-18T13:09:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T13:09:35Z, on 1.0.0_SA_CTO~DELL1 msg 8044 (S34 landed; org/critical_paths/change_management/20261018T1246Z_cot-s34-holdings-dedup-20261018_deploy_completion.md @088303d25a). Adjudicates one row, D1-S34. FWD-10's ADVI leg grades MET on both dates. The watermark moves to now.

```json
[
  {
    "id": "MDPF_CANON-D1-C-S99",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-18T13:09:35Z",
    "one_line": "L9 GRADE, FWD-10 ADVI leg: MET on both dates, read by this seat. Served ADVI header_metrics (data_as_of 2026-10-16) total.aua 524,463,230.11 equals the served MDPF Cottonwood category-views total_aua 524,463,230.11. On 2026-10-15, ADVI's gold account_performance sums 530,421,988.14, MDPF's figure; the served ADVI layer carries only the latest day at day grain. S34 dismissed as remediated. The 12:55Z StartAt=C_00 run left no partial state.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_CANON-D1-S34"
    ],
    "spec_asserts": "MDPF_CANON PRD FWD-10 (v2.24-v2.27; erratum v2.28 @d98a6c5be1 has the ADVI leg NOT MET at 530.37M on 10-15 and 524,411,722.20 on 10-16): Cottonwood's supervised total matches on both pages. The CTO's ask, msg 8044: read the served ADVI header_metrics for 10-15 and 10-16, and confirm the C_00 run left no partial state.",
    "world_is": "READ BY THIS SEAT 2026-10-18 ~13:1xZ. (1) s3://opal-data-cot/platinum/firm/header_metrics.json (LastModified 13:00:02Z, VersionId 2XVOtRM9..., generated_at 12:58:32Z): data_as_of 2026-10-16, total.aua 524463230.11, account_count 864. s3://opal-data-portal-v2/platinum/mdpf/cottonwood/category-views.json: as_of 2026-10-16, sums.total_aua 524463230.11 (gold_plane and view_plane equal). Equal to the cent, so 10-16 is MET on the served artifacts. (2) 2026-10-15: header_metrics holds the latest day only, and platinum/firm/timeseries_chart.json carries monthly, quarterly and annual points ending 2026-10-16. So no served ADVI artifact carries 10-15 at day grain, and this seat read the gold the platinum is built from. s3://opal-data-cot/gold/timeseries/account_performance.parquet, VersionId rz2IhJye... (12:58:28Z): 10-15 has 864 accounts and sum(total_aua) 530,421,988.14, MDPF's 10-15 figure (PRD v2.25/v2.28). 10-16 is 524,463,230.11. (3) Against the prior version jj.ASaqcp... (11:35:15Z, before the fix): 13 of 139 dates moved, 2026-09-30 to 2026-10-16, each by +51,152.80 to +51,507.91 (10-15 +51,505.77; 10-16 +51,507.91), which is the Van Alstyne holding the old (account_id, asset_name) key dropped. 09-25 (521,308,070.48) and 09-29 (508,894,345.51) are unchanged. The S34 row states 10-15's gap as 51,505.76 and this seat's diff reads 51,505.77, a one-cent rounding difference between the two sums; the 10-15 after-value equals the MDPF figure exactly. (4) C1, the 12:55Z StartAt=C_00 run: over gold/views, gold/platinum, gold/timeseries, gold/partner_analytics, gold/client_timeseries and platinum/ in opal-data-cot, 1,373 objects carry LastModified after 12:54:31Z (the B_00 end). None falls before 12:57:52Z (the A_05 start); the earliest is gold/timeseries/account_performance.parquet at 12:58:28Z. So the C_00 run wrote nothing to those prefixes. This grade reads the served and gold artifacts; it is not the producer's report (CRO~DDD msg 8041).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "s3://opal-data-cot/platinum/firm/header_metrics.json VersionId 2XVOtRM98WpUwaNy9UJRFKeZMIW8AQ7R (this seat)",
        "s3://opal-data-portal-v2/platinum/mdpf/cottonwood/category-views.json as_of 2026-10-16 (this seat)",
        "s3://opal-data-cot/gold/timeseries/account_performance.parquet VersionIds rz2IhJyFehwl3Mpug5FVZ9fzAP_6VXKf and jj.ASaqcpkLz52TggSPJmWzneDbAblzn (this seat)",
        "org/critical_paths/change_management/20261018T1246Z_cot-s34-holdings-dedup-20261018_deploy_completion.md @088303d25a"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "S34 is remediated: the holdings key is (account_id, asset_id), and the measured ADVI totals equal MDPF on both dates. This row records the FWD-10 ADVI-leg grade."
  }
]
```

-- 3.0.0_SA_CVO
