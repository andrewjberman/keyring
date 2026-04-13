# 0.6.0_AE Log: ADVI_OFFICE W2 QA Run (in progress) + EC2 Idle Enforcer Deploy
**Date:** 2026-04-13
**Agent:** 0.6.0_AE_PartnerETL
**Tag:** No new bd-pipeline tag. ec2-auto-shutdown-enforcer updated (no version tag convention for that module).
**Related:** ADVI_OFFICE.W2, ADVI_GLDRST.022 Phase 3

---

## Session Context

Continuation of earlier session (see advi_gldrst_022_phase3_kickoff_and_s00_hotfix.md).
GO signal received from both COO and DS (ADVI_OFFICE W1 complete, commit 27471bed).
Proceeded with W2 but D_00b crashed twice with two distinct bugs. Blocked on DS fix.

---

## W2 Execution Log

### Phase 1 checks (pre-run)
```
aws s3 ls s3://opal-data-bd/code/gold/ | grep -E "D_00b|D_01"
2026-04-13 16:20:47  D_00b.portal_timeseries.py   (e20fcf0a -- DS crash fix)
2026-04-13 16:20:45  D_01.partner_analytics.py    (27471bed -- W1 code)

aws s3 ls s3://opal-data-bd/gold/dimensions/dim_advisor_office.csv
2026-04-13 16:42:11  dim_advisor_office.csv        (uploaded this session -- OK)
```

### Dim file upload
```
aws s3 cp data/black_diamond/config/office_mapping/advisor_registry_lusha_office_bridge_clean.csv \
    s3://opal-data-bd/gold/dimensions/dim_advisor_office.csv
```
Upload: OK. Acceptance criterion 1 (dim file exists) -- PASS.

### QA runner state
- Instance: i-0090b823a4a0997e3 (c6a.16xlarge)
- Was already running when W2 started (34 min uptime, no gold processes)
- Started group D run directly

### Run 1 (PID 1547, log: group_D_20260413_204729.log) -- CRASHED
**D_00:** completed OK
**D_00b (e20fcf0a):** crash at `_build_office_view` line 255
```
KeyError: 'account_id'
joined['office'] = joined['account_id'].astype(str).map(account_office_dim).fillna('Other')
```
Root cause: `client_performance` is relationship-grained, no `account_id` column.
DS fixed (commit e20fcf0a on S3 -- bridge via account_team -> relationship_id).

### Run 2 (PID 2659, log: group_D_20260413_211932.log) -- CRASHED
**D_00:** completed OK (25s)
**D_00b (e20fcf0a):** crash at `build_timeseries_chart` line 746
```
UnboundLocalError: local variable '_nna_drill_data' referenced before assignment
```
Root cause: new OFC call on line 746 references `_nna_drill_data` before its `def`
in function body. Python treats as local from moment of any assignment in scope.

Secondary observation: `ofc: 2290 days, 1 offices` -- OFC dim loaded 178 advisors
but aggregation collapsed to 1 office. Likely dim join or modal office logic bug in
`_build_rel_office_dim_d00b()`. Not the crash cause but will produce wrong output.

Briefing written for Andrew to pass to DS.

### Instance management
- Run 1: instance was already running, dispatched group D
- Between runs: Andrew asked to stop all instances -- PROD runner was already stopped,
  QA runner stopped manually
- Run 2: started QA runner, dispatched group D
- End of session: QA runner stopped manually (Andrew's request)

---

## EC2 Idle Enforcer Deploy

Separate work item triggered by the QA runner being left up after crashes.

**Finding:** existing `ec2-auto-shutdown-enforcer` Lambda only had a hard runtime cap
(4h). No idle detection -- instances that crash before their shutdown block stay up.

**Changes to `infra/aws/lambda/ec2-auto-shutdown-enforcer/`:**

| File | Change |
|---|---|
| `lambda_function.py` | Added CloudWatch CPU idle check; removed emojis (ASCII only); added c6i/c6a pricing |
| `main.tf` | Added `cloudwatch:GetMetricStatistics` to IAM; added 4 idle env vars; schedule 15min -> 5min |

**New behavior:** stop any instance with avg CPU <5% for 15 min (after 15 min uptime).
Hard cap of 4h unchanged.

**Deployment:**
```
commit d17a2c21 feat(ec2-auto-shutdown-enforcer): add idle CPU detection + 5min schedule
terraform apply -- 1 added, 3 changed, 0 destroyed
0-diff confirmed
git push origin CLOUD
```

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Check inbox -- GO signal from COO + DS | DS W1 commit 27471bed confirmed |
| 2 | Flip W2 task order staged -> pending | Done |
| 3 | Verify D_00b + D_01 on S3 | Both confirmed (16:20 UTC upload) |
| 4 | Check QA runner state | Running (c6a.16xlarge), no gold processes |
| 5 | Upload dim file to S3 | s3://opal-data-bd/gold/dimensions/dim_advisor_office.csv -- OK |
| 6 | Dispatch group D (Run 1, PID 1547) | D_00 OK; D_00b crash #1 KeyError: account_id |
| 7 | DS fix (e20fcf0a) uploaded to S3 | Confirmed 16:20 UTC |
| 8 | Stop + restart QA runner (Andrew request) | Instance stopped then restarted |
| 9 | Dispatch group D (Run 2, PID 2659) | D_00 OK; D_00b crash #2 UnboundLocalError |
| 10 | Briefing written for Andrew | See crash notes above |
| 11 | Deploy ec2-auto-shutdown-enforcer updates | d17a2c21, applied, 0-diff |
| 12 | Stop QA runner (Andrew request) | i-0090b823a4a0997e3 stopping |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (before W2) | S3 code check | `aws s3 ls s3://opal-data-bd/code/gold/ | grep D_00b\|D_01` | Both confirmed on S3 |
| 1 (before W2) | QA runner probe | SSM `pgrep -af gold_dispatch` | NO_GOLD_RUNNING -- safe to dispatch |
| 3 (post run 1) | SSM status | `gold_dispatch.sh --status` | Crash confirmed, full traceback retrieved |
| 3 (post run 2) | SSM log read | `cat /tmp/gold_logs/group_D_20260413_211932.log` | Full crash traceback + ofc anomaly found |

---

## Current State

| Component | State |
|---|---|
| dim_advisor_office.csv | Uploaded: s3://opal-data-bd/gold/dimensions/dim_advisor_office.csv |
| D_01 on S3 | Ready (27471bed) |
| D_00b on S3 | Broken -- 2 bugs remaining (UnboundLocalError + 1-office aggregation anomaly) |
| ADVI_OFFICE.W2 | Pending -- blocked on DS D_00b fix #3 |
| QA runner (i-0090b823a4a0997e3) | Stopping |
| PROD runner (i-01003b035d2988dfb) | Stopped |
| ec2-auto-shutdown-enforcer | Updated -- idle CPU detection live (d17a2c21) |
| ADVI_GLDRST.022 Phase 3 | Tonight at 22:00 UTC: first clean S_00 run. Fetch snapshots after ~23:45 UTC. |

---

## Next Steps

- **[Andrew -> DS]** Forward D_00b crash briefing:
  1. `UnboundLocalError: _nna_drill_data` -- move `def _nna_drill_data` above line 746 call
  2. `ofc: 2290 days, 1 offices` -- check `_build_rel_office_dim_d00b()` modal office logic /
     merge key; 178 advisors loaded but all collapsing to 1 bucket
  DS needs to fix both in one pass, re-upload D_00b to S3, and MCP-message AE.

- **[0.6.0_AE_PartnerETL]** On DS MCP GO: start QA runner, dispatch `--group D`, monitor run.

- **[0.6.0_AE_PartnerETL] Tonight ~23:45 UTC:**
  `python data/analysis/phase3_v2_vs_job1_diff.py --fetch 2026-04-13`
  then diff. Record Day 1 result in ADVI_GLDRST.022 Phase 3 tracking table.

- **[0.6.0_AE_PartnerETL] Tonight ~22:15 UTC:** Monitor bd-fees first prod run.
  Check `s3://opal-data-bd/logs/fees-download-2026-04-13.log` after run completes.
