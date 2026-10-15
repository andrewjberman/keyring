# IRPT_DASHBD: CVO adjudication, round 124 (workstream B-49F, ~D2): the hop-1 apply

<sweep_watermark>2026-10-15T16:18Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T16:18Z, on msg 8437 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND124_128_B49F_APPLIES_DRAIN_END_20261015.md` @e289d60e6e, blob 36b84f46f5; one packet covers rounds 124 and 128, and round 128 is ADJUDICATION_v94). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-b-253 (WORLD; applier 0.7.0_AE_CloudOps~DB2; merged @b43e769ff0), under the signed hop-1 pair `NEVER_WIDEN_PACKET_HOP1_FILLED_REPORT_VALUES_STAGE.md` (sha256 2f25b84dc85c, recomputed). No judgment criterion. Re-run here at 16:00Z, including each criterion's fresh live reads: DBB123-1-AC1, DBB123-2-AC1 and DBB123-3-AC1, 3 of 3 PASS (rc 0). The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row. **Applied, not proven:** the hop-1 behaviour is unproven until its first scheduled fire.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S30",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T16:18:00Z",
  "one_line": "Round 124 B-49F: the hop-1 apply of irpt-49f-reporting-gold-lambda. 3 of 3 PASS re-run with fresh live reads. (1) LIVE vs TERRAFORM, read by this seat at 16:02:17Z. The function reads python3.12, handler.lambda_handler, MemorySize 8192, Timeout 900, one layer irpt-performance-native-layer:1, no environment, State Active / LastUpdateStatus Successful, LastModified 2026-10-15T11:49:38Z, CodeSha256 jz6fRzL5..., equal to reporting-gold/lambda.tf:54-62. The inline policy holds 11 sids: the earlier 7 plus ReadTheServedModelSeriesObjectOnly, ListExactlyTheHouseholdCrosswalkPrefix, ReadTheHouseholdCrosswalkOnly and InvokeOwnFunctionOnly, and one PutObject statement of six prefixes, still named WriteTheFiveGoldPrefixesOnly (D2-S80 (4)). The schedule irpt-49f-reporting-gold-daily reads ENABLED, cron(41 7 ? * MON-FRI *) America/New_York, LastModificationDate 2026-10-02 (unchanged by the apply), default retry (185 attempts / 86,400 s). SAFE-APPLY: the applier worktree's runtime gate log shows APPLY-ENFORCE NAMING-GATE PASS at 11:49:03Z and PLAN-ENFORCE NAMING-PLAN PASS 7 graded at 11:49:06Z, 32 s before the function's LastModified. Those lines are the safe-apply gate's footprint. No safe-deploy bypass line for this function appears in org/safe-deploy-bypass-audit.log (80 lines dated 2026-10-15 read). The apply commit a6e2e44e43 records ONE safe-apply 0/2/0. (2) NOTHING RAN AFTER THE APPLY: CloudWatch Invocations for the function, 11:30Z to 16:15Z, is one, in the 11:30-11:45Z bucket: that is the 11:41Z scheduled fire, read by the applier before the apply under the packet's one-hour rule (ledger L4). The filled_report_values prefix of opal-data-49financial holds 0 objects (16:16:27Z). (3) WRITE SET: none; the apply changed the function and its policy only. ROLLBACK per key, from packet section 6: the function code and memory by a safe-apply of the reverted files. The previous artifact version (2026-10-13T12:36:19Z, UcKN2ttQ...) is present in the versioned artifact bucket beside the current one (2026-10-15T11:09:14Z, My0rI3fw...). The policy goes back to 7 by the same revert. Any filled_report_values partition the stage later writes is removed only by a listed-key delete with Andrew's word. (4) LEDGER irpt-dashbd-hop1-filled-report-values-20261015 is OPEN: L1-L5 closed (11:05Z to 11:51Z) and L6 (the first scheduled fire, read by ~D2) open. Its open marker is present in 6 of the 33 live worktrees read, including box/dell2. Its 30-hour window ends 2026-10-16T17:03Z, after the next fire. (5) NEXT FIRE, from the live schedule: Friday 2026-10-16 07:41 America/New_York = 2026-10-16T11:41Z (a trading day by lib/trading_calendar). That fire is the proof (Max Memory Used, duration, new partition rows, no FILLED_SKIPPED). Rows: D2-S80 (INERT; wrong artifact key in the order, pins written before the build, fmt alignment, the sid name) is accepted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S80"
  ],
  "spec_asserts": "CLAUDE.md never-widen and NEVER-2: a confirmed deploy is finished or rolled back, with its ledger entry opened at start and closed at completion; the sign-off names the rollback per key; Terraform only through safe-apply; a producer's self-report is verified against live state.",
  "world_is": "Hop 1 is applied: code, memory 8192, the four new grants and the self-invoke grant are live. No invocation has run on the new code and no filled_report_values object exists. The ledger stays open at L6 until the 2026-10-16T11:41Z fire is read. FWD-2 and FWD-21 are not met until that fire lands a partition.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T16:00Z: DBB123-1-AC1, DBB123-2-AC1, DBB123-3-AC1 PASS rc 0 (fresh live reads); DB118-3-AC3 FAIL rc 1",
    "aws lambda get-function irpt-49f-reporting-gold-lambda at 16:02:17Z; infra/aws/terraform/investor-reporting/reporting-gold/lambda.tf:44, 54-62",
    "aws scheduler get-schedule irpt-49f-reporting-gold-daily: ENABLED, cron(41 7 ? * MON-FRI *), America/New_York, modified 2026-10-02",
    "C:/dev/wk-irpt-dashbd-db2-b253/org/mcp/naming-gate-verdicts.log 2026-10-15T11:49:03Z and 11:49:06Z; org/safe-deploy-bypass-audit.log (no line for this function)",
    "aws cloudwatch Invocations irpt-49f-reporting-gold-lambda 11:30Z-16:15Z: 1 in the 11:30-11:45Z bucket; aws s3api list-objects-v2 opal-data-49financial irpt/49financial/gold/filled_report_values/: 0",
    "aws s3api list-object-versions opal-313476888478-lambda-artifacts investor-reporting/irpt-reporting-gold-lambda.zip: current 2026-10-15T11:09:14Z, previous 2026-10-13T12:36:19Z",
    "org/critical_paths/change_management/20261015T1103Z_irpt-dashbd-hop1-filled-report-values-20261015_deploy_completion.md (Status OPEN, L1-L5 closed); .open_deploys marker in 6 of 33 worktrees",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND124_128_B49F_APPLIES_DRAIN_END_20261015.md blob 36b84f46f5 (msg 8437)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The applier's observations are inert. The apply is verified live against Terraform and its pair, with nothing written and nothing invoked since. The ledger correctly stays open for the first fire."
 }
]
```
