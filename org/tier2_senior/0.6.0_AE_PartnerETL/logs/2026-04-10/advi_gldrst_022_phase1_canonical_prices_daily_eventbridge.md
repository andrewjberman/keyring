# 0.6.0_AE Log: ADVI_GLDRST.022 Phases 1 + 2 -- bd-canonical-prices-daily EventBridge rule + runner IAM sanity check
**Date:** 2026-04-10
**Agent:** 0.6.0_AE_PartnerETL
**Tag:** bd-v2.22.0
**Related:** docs/briefs/ae-brief-v2-prestep-integration.md (Phases 1 + 2 of 5)
**Predecessor:** ADVI_GLDRST.022 DS integration shipped earlier today (commit 8c801923 on CLOUD; v2 + ticker_overrides.py in s3://opal-data-bd/code/gold/)

## Context

DS completed ADVI_GLDRST.022 integration: `build_canonical_prices_v2.py` is now registered as `S_00` in `gold_dispatch.sh` CATALOG and runs as a silver-prep pre-step before the freshness gate on every `--chain full` / `--chain rebuild` invocation. Code + S3 artifacts are in place. AE owns the downstream infra work.

Phase 1 of the AE brief: add a new daily EventBridge cron rule that fires `bd-gold-trigger` every day (including weekends and US market holidays), so v2 can T3-interpolate or T4-carry-forward the weekend/holiday gap dates into `silver/prices/canonical_prices.parquet`. Pre-Phase 1 coverage was Mon-Fri only via `bd-allocation-pipeline-trigger` + `bd-gold-nightly-fallback`, leaving weekends/holidays with no canonical_prices refresh.

## Work Done

### Terraform -- new resources

Added to `infra/aws/terraform/bd-pipeline/eventbridge.tf` section 7:

- `aws_cloudwatch_event_rule.bd_canonical_prices_daily` -- `cron(0 22 * * ? *)`, ENABLED, every day
- `aws_cloudwatch_event_target.bd_canonical_prices_daily_target` -- targets `module.gold_trigger.function_arn`, input `{"mode":"incremental"}`
- `aws_lambda_permission.eventbridge_canonical_prices_daily` -- `statement_id = "allow-canonical-prices-daily-trigger"`

Cron pattern rationale: `cron(0 22 * * ? *)` not `cron(0 22 ? * * *)` -- EventBridge requires exactly one of day-of-month or day-of-week to be `?`. Matches the pattern already used by `historical-prices-daily`.

Mode rationale: `incremental` delegates to `gold_dispatch.sh --chain full --incremental` on the runner. On weekdays that runs silver-prep (S_00) first, then the freshness gate passes (new allocations landed), then the full A/B/C/D chain executes. On weekends/holidays silver-prep runs, the gate trips, A/B/C/D skips, and the instance shuts down via watchdog -- canonical_prices is still updated for that weekend/holiday date.

### Drift handling

Initial `terraform plan` showed 3 adds (my changes) plus 2 unexpected drift items:

| Resource | Live state | TF-defined | Decision |
|---|---|---|---|
| bd-gold-layer-monthly-trigger | DISABLED | ENABLED | Keep live (DISABLED) -- codified into tf |
| bd-gold-nightly-fallback | cron(0 23 ? * MON-SAT *) | cron(0 23 ? * MON-FRI *) | Keep live (MON-SAT) -- codified into tf |

Flagged both to Andrew, who confirmed both live-state changes are intentional. Chose the targeted-apply path to ship Phase 1 cleanly without sweeping the drift:

1. Applied the 3 new resources via `terraform apply -target=...` (3 added, 0 changed, 0 destroyed)
2. Edited `eventbridge.tf` to match live state: `bd_gold_monthly.state = "DISABLED"` and `bd_gold_nightly_fallback.schedule_expression = "cron(0 23 ? * MON-SAT *)"` + updated description
3. Follow-up `terraform apply` picked up only a description text change on `bd_gold_nightly_fallback` (0 added, 1 changed)
4. Final `terraform plan` returned `No changes. Your infrastructure matches the configuration.`

`-target` is flagged as non-routine by Terraform, but this was the right call here: the drift was load-bearing intent from someone else and bundling it into the Phase 1 apply would have silently reverted their changes.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Read AE brief + DS session log | Phase 1 scope confirmed |
| 2 | comp-blast bd-gold-trigger | No down connections (known compiler gap: lambda->EC2 edges not indexed) |
| 3 | Read eventbridge.tf | Confirmed section 6 (historical-prices-daily) as append point |
| 4 | Edit eventbridge.tf -- add section 7 (canonical_prices_daily) | 3 new resources |
| 5 | terraform plan | 3 add + 2 drift changes -- flagged to Andrew |
| 6 | Andrew confirmed drift is intentional | Targeted apply approved |
| 7 | terraform apply -target=... (3 resources) | 3 added, 0 changed, 0 destroyed |
| 8 | Verify rule in live AWS | `bd-canonical-prices-daily` ENABLED, cron(0 22 * * ? *), target=bd-gold-trigger, input={"mode":"incremental"} |
| 9 | Verify Lambda policy | `allow-canonical-prices-daily-trigger` statement present |
| 10 | Edit eventbridge.tf -- codify live state (monthly DISABLED, nightly MON-SAT) | Matches live |
| 11 | terraform apply (full, no -target) | 0 added, 1 changed, 0 destroyed (nightly description text) |
| 12 | terraform plan | No changes. Infrastructure matches configuration. |
| 13 | Update pipeline_inventory.xml (current_tag, add 2 rules, DISABLED monthly) | Core doc in sync |
| 14 | git commit (infra + core doc) | (filled by commit) |
| 15 | record-terraform-deploy.sh + tag + push | bd-v2.22.0 |

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| BD | bd-v2.22.0 | (filled by commit) |

## Verification

```
$ aws events describe-rule --name bd-canonical-prices-daily --query '[Name,State,ScheduleExpression]' --output text
bd-canonical-prices-daily   ENABLED   cron(0 22 * * ? *)

$ aws events list-targets-by-rule --rule bd-canonical-prices-daily --query 'Targets[0].[Id,Arn,Input]' --output text
1   arn:aws:lambda:us-east-1:313476888478:function:bd-gold-trigger   {"mode":"incremental"}

$ aws lambda get-policy --function-name bd-gold-trigger (Sids)
allow-monthly-trigger
S3PricesTrigger
allow-nightly-fallback-trigger
allow-canonical-prices-daily-trigger

$ terraform plan (final)
No changes. Your infrastructure matches the configuration.
```

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| 1 (before writing) | comp-blast | `comp-blast bd-gold-trigger` | "No downstream consumers" -- known compiler gap: graph doesn't index lambda->EC2 invocation edges or EventBridge->lambda reverse targets. Graph built 659 nodes / 285 edges in 1.4s. |
| 1 (before writing) | comp-trace | `comp-trace bd-gold-trigger --direction down` | "No down connections found" -- same graph gap |
| 2 (before commit) | terraform validate (implicit via plan) | `terraform plan` | Plan succeeded, resources resolvable, no syntax errors |
| 2 (before commit) | terraform plan (post-edit) | `terraform plan` | 0-diff confirmed |
| 3 (after commit) | aws events describe-rule + list-targets-by-rule + get-policy | see Verification | Rule + target + lambda permission live |

**Compiler gaps logged** (also flagged by DS earlier today in `advi_gldrst_022_v2_prestep_gold_runner_integration.md`):

1. Graph builder does not follow Lambda-to-Lambda `lam.invoke(FunctionName=...)` edges
2. Graph builder does not follow Lambda-to-EC2 SSM send_command / start_instances edges
3. Graph builder does not index EventBridge->Lambda target edges (reverse direction)

Combined, these gaps meant neither comp-blast nor comp-trace could surface anything meaningful for this change. Verification fell back to direct AWS CLI describe-rule / get-policy and terraform plan 0-diff. Appending to `org/compiler-tools-log.md`.

## Phase 2 -- IAM Sanity Check (post-Phase-1, noninvasive)

Non-destructive: no EC2 boot, no test-file write. Purely static IAM inspection + read-target existence verification.

### Runner identity

| Field | Value |
|---|---|
| Instance | i-01003b035d2988dfb (bd-gold-layer-runner) |
| Instance profile | arn:aws:iam::313476888478:instance-profile/bd-exporter-profile |
| Role | bd-exporter-ec2-role |

### Read targets exist (verified via my local creds, not runner creds)

```
$ aws s3 ls s3://opal-data-bd/silver/transactions/ | head
2026-02-23 11:22:48  48161 2020-03-06.parquet
2026-02-23 11:22:48  48228 2020-04-21.parquet
[...parquets back to 2020...]

$ aws s3 ls s3://opal-data-bd/silver/historical_prices.parquet
2026-04-10 10:08:42  36812112 historical_prices.parquet

$ aws s3 ls s3://opal-data-bd/silver/prices/canonical_prices.parquet
2026-04-10 09:55:23  89352581 canonical_prices.parquet
```

All three v2 read targets exist. `historical_prices.parquet` refreshed today at 10:08 UTC (by `historical-prices-daily` 14:00 UTC = 10:00 ET -- actually the object lists 10:08 UTC so this may be a timezone quirk in my local display; whatever, it's current). `canonical_prices.parquet` refreshed today at 09:55 UTC -- this is the pre-v2 version; v2 will overwrite it tonight at 22:00 UTC.

### Runner role policy (s3-access inline policy)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BDDataBucket",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:ListBucket",
        "s3:HeadObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::opal-data-bd",
        "arn:aws:s3:::opal-data-bd/*"
      ]
    }
  ]
}
```

Bucket-wide coverage (not prefix-scoped). Every S3 prefix in `opal-data-bd` inherits read+write+list+delete automatically.

### v2 requirements vs. role capability

| v2 needs | Action | Resource | Covered? |
|---|---|---|---|
| Read `silver/transactions/*` | `s3:GetObject` | `opal-data-bd/*` | yes |
| Read `silver/historical_prices.parquet` | `s3:GetObject` | `opal-data-bd/*` | yes |
| Read `silver/prices/canonical_prices.parquet` (emergency rebuild path) | `s3:GetObject` | `opal-data-bd/*` | yes |
| `list_objects_v2` on bucket | `s3:ListBucket` | `opal-data-bd` | yes |
| Write `silver/prices/canonical_prices.parquet` | `s3:PutObject` | `opal-data-bd/*` | yes |
| Pending-marker delete (pre-existing runner behavior, bd-v2.21.7) | `s3:DeleteObject` | `opal-data-bd/*` | yes |

### Phase 2 verdict

PASS. No terraform edit needed. The runner's bucket-wide inline policy already covers every action v2 requires. Phase 2 closed with no changes to IAM.

Note: the three attached policies not inspected in detail (`AdditionalPermissions`, `gold-layer-trigger`, `pipeline-chain`, `schwab-bucket-access`, `bd-securities-access`) are out of scope for v2's read/write surface -- v2 only touches `opal-data-bd` and the inline `s3-access` policy covers that bucket fully.

## Current State

| Component | State |
|---|---|
| `bd-canonical-prices-daily` EventBridge rule | ENABLED, cron(0 22 * * ? *), target=bd-gold-trigger, input={"mode":"incremental"} |
| `bd-gold-nightly-fallback` rule | ENABLED, cron(0 23 ? * MON-SAT *) (live + tf in sync) |
| `bd-gold-layer-monthly-trigger` rule | DISABLED (live + tf in sync) |
| `bd-price-update` Lambda Job 1 | STILL ENABLED -- Phase 3 parallel-run diff must complete before Phase 4 disables it |
| Runner IAM (Phase 2) | PASS, no changes needed |
| pipeline_inventory.xml | updated to bd-v2.22.0, new rules documented |
| Production gold runner (i-01003b035d2988dfb) | Stopped. First fire of new rule at 22:00 UTC tonight (6 PM EDT). |

## Next Steps

- **[0.6.0_AE_PartnerETL]** Tonight at 22:00 UTC (6 PM EDT, ~3h from now): monitor the first fire of `bd-canonical-prices-daily`. Watch `bd-gold-trigger` CloudWatch logs and the runner's systemd logs at `s3://opal-data-bd/logs/gold-layer/`. Today is Friday, so `bd-allocation-pipeline-trigger` also fires at 22:00 UTC -- the pending-marker mechanism should absorb the double-fire into a single runner boot.
- **[0.6.0_AE_PartnerETL] DONE 2026-04-10** Phase 2 IAM sanity check: PASS. Runner's `bd-exporter-ec2-role.s3-access` inline policy already grants `Get/Put/List/Head/Delete` on `opal-data-bd/*` bucket-wide. No terraform change. See Phase 2 section above.
- **[0.6.0_AE_PartnerETL] MONDAY 2026-04-13** Phase 3 kickoff -- parallel-run diff protocol. Full runbook in the "Phase 3 Monday Runbook" section below. TL;DR: snapshot canonical_prices.parquet after bd-price-update Job 1 finishes and again after v2 silver-prep finishes, diff on (date, asset_name), record price deltas + source-tag agreement, repeat daily through 2026-04-17 (5 business days).
- **[0.6.0_AE_PartnerETL]** Phase 4 (after clean parallel week): wrap `bd-price-update` Job 1 in `ENABLE_JOB_1` env var guard defaulting to false. Do NOT touch Job 2 (interpolated_prices.parquet writer -- v2 still reads it for the emergency-rebuild path).
- **[0.6.0_AE_PartnerETL]** Phase 5 rollback plan accessible for 2 weeks post-shipping: env var flip -> gold_dispatch revert -> EventBridge rule disable.
- **[Andrew]** First production run of v2 via this rule fires tonight at 22:00 UTC. If anything misbehaves, Phase 5 rollback options are in the brief.
- **[1.0.0_SA_CTO / 2.0.0_SA_COO]** Org dirt from DS session (task orders .021 / .021b, earlier session log, diagram generator, cross-DS audit docs) is still uncommitted in the working tree. Outside AE's lane -- deferred to whoever picks up the next org-tidy routing.
- **[follow-up, not assigned]** Two EventBridge rule entries in `pipeline_inventory.xml` had stale schedules predating the 2026-04-06 BD schedule shift (transaction shown as 21:40 UTC, should be 21:53; allocation shown as 21:48 UTC, should be 22:00). Not touched in this commit to avoid scope creep. Worth a small cleanup pass.
- **[follow-up, not assigned]** Compiler graph gaps (lambda-to-lambda, lambda-to-EC2, eventbridge-to-lambda reverse direction) make comp-blast / comp-trace near-useless for pipeline infra changes. Logged above + in DS's log earlier today. Small PR to `org/modules/graph/` would help.

---

## Phase 3 Monday Runbook -- 2026-04-13 through 2026-04-17

**Goal:** prove v2 canonical_prices matches bd-price-update canonical_prices on overlapping (date, asset_name) rows for 5 consecutive business days before disabling bd-price-update Job 1 in Phase 4.

**Why this matters:** bd-price-update Job 1 and v2 both write `s3://opal-data-bd/silver/prices/canonical_prices.parquet`. On weekdays they both run -- v2 runs last, so v2's output is authoritative. If v2 disagrees with Job 1 on any overlapping row, we ship bad data the moment Job 1 gets disabled. The diff protocol is the only catch-net.

### Daily schedule (each day Mon-Fri)

UTC times -- Eastern time in parens for human sanity.

| Time (UTC) | Event |
|---|---|
| 21:40 (5:40 PM ET) | `bd-transaction-pipeline-trigger` fires -> transactions EC2 boots |
| 22:00 (6:00 PM ET) | **BOTH** `bd-allocation-pipeline-trigger` AND `bd-canonical-prices-daily` fire simultaneously |
| ~22:00-22:05 | bd-allocation-trigger -> allocation EC2 boots -> allocation download -> silver/allocations/<date>.xlsx lands |
| ~22:05-22:15 | bd-allocation-processor Lambda fires on S3 event -> processes allocation xlsx -> writes `silver/prices/<date>.parquet` |
| ~22:15 | S3 trigger on `silver/prices/*.parquet` fires `bd-gold-trigger` |
| ~22:15 | AND `bd-canonical-prices-daily` already fired `bd-gold-trigger` directly at 22:00 |
| ~22:15-22:18 | Runner boots (first trigger wins, second writes pending marker) |
| Runner boot | **bd-price-update** Lambda also runs at 22:00-ish via the allocation chain. Writes `canonical_prices.parquet` via Job 1, then `interpolated_prices.parquet` via Job 2. |
| Runner boot | gold_dispatch.sh runs silver-prep = v2. v2 OVERWRITES `canonical_prices.parquet`. |
| Runner boot | Freshness gate passes, A/B/C/D chain runs. |
| ~23:00-23:45 | Gold run completes, watchdog shuts down runner |

**Snapshot window:** the critical window is between bd-price-update Job 1 completing and v2 silver-prep completing. Based on the daily timing, that's roughly 22:05 - 22:20 UTC.

### Snapshot capture strategy

**Option A (preferred) -- S3 object versioning:** check whether `opal-data-bd` has versioning enabled on `silver/prices/`. If yes, each write creates a new version and we can retrieve both (Job 1 version + v2 version) after the fact. Low-risk, no live interception needed.

**Option B (fallback) -- live SSM snapshot:** if versioning is off, monitor CloudWatch logs for `bd-price-update` Lambda completion ("Job 1 complete" marker), then immediately `aws s3 cp s3://opal-data-bd/silver/prices/canonical_prices.parquet /tmp/canonical_prices_job1_<date>.parquet` before v2 overwrites. Then snapshot again after v2 completes (gold runner systemd log confirms silver-prep done): `aws s3 cp ... /tmp/canonical_prices_v2_<date>.parquet`.

Monday AM first task: check bucket versioning.

```bash
aws s3api get-bucket-versioning --bucket opal-data-bd
```

If versioning is disabled, write a small capture script that tails `bd-price-update` CloudWatch logs, detects Job 1 completion, and pulls the object immediately. Store snapshots at `data/analysis/phase3_diff_snapshots/<YYYY-MM-DD>_job1.parquet` and `..._v2.parquet` locally.

### Diff script

Write at `data/analysis/phase3_v2_vs_job1_diff.py`. Pseudocode:

```python
import pandas as pd
import sys
from datetime import date

def diff_day(d):
    job1 = pd.read_parquet(f"data/analysis/phase3_diff_snapshots/{d}_job1.parquet")
    v2   = pd.read_parquet(f"data/analysis/phase3_diff_snapshots/{d}_v2.parquet")

    # Outer join on (date, asset_name)
    key = ['date', 'asset_name']
    merged = job1.merge(v2, on=key, how='outer', suffixes=('_job1', '_v2'), indicator=True)

    # Bucket 1: rows only in Job 1 (red flag)
    only_job1 = merged[merged._merge == 'left_only']

    # Bucket 2: rows only in v2 (expected -- v2 has gap-date fills)
    only_v2 = merged[merged._merge == 'right_only']

    # Bucket 3: rows in both -- this is the validation set
    both = merged[merged._merge == 'both'].copy()
    both['price_delta'] = (both.price_v2 - both.price_job1).abs()
    both['source_agrees'] = both.source_job1 == both.source_v2

    # Stop-ship signals
    price_violations = both[both.price_delta > 0.001]
    source_violations = both[~both.source_agrees]

    print(f"=== Diff report {d} ===")
    print(f"Rows Job1:           {len(job1)}")
    print(f"Rows v2:             {len(v2)}")
    print(f"Rows only in Job1:   {len(only_job1)}   <-- should be 0 (STOP-SHIP if > 0)")
    print(f"Rows only in v2:     {len(only_v2)}    (expected: gap dates, weekends, holidays)")
    print(f"Rows in both:        {len(both)}")
    print(f"Price violations:    {len(price_violations)}  <-- should be 0")
    print(f"Source violations:   {len(source_violations)}  <-- should be 0")
    if len(price_violations):
        print("\nSample price violations:")
        print(price_violations[['date','asset_name','price_job1','price_v2','price_delta','source_job1','source_v2']].head(20))
    if len(source_violations):
        print("\nSample source violations (sans linear_interpolation rows which are v2-only and valid):")
        realviolations = source_violations[source_violations.source_v2 != 'linear_interpolation']
        print(realviolations[['date','asset_name','price_job1','price_v2','source_job1','source_v2']].head(20))

if __name__ == "__main__":
    diff_day(sys.argv[1])
```

Run each morning: `python data/analysis/phase3_v2_vs_job1_diff.py 2026-04-13` (etc.)

### Stop-ship signals (from the brief)

Any ONE of these on any day during the parallel-run week is a stop-ship -- do NOT proceed to Phase 4, instead open a new TO to investigate divergence:

1. Any `(date, asset_name)` row present in Job 1 but missing from v2 -- **v2 is losing data**
2. Any `price_delta > $0.001` on an overlapping row -- **tier resolution divergence**
3. Any row where `source_job1 != source_v2` AND `source_v2 != 'linear_interpolation'` -- **tier source disagreement** (linear_interpolation is a v2-only source on gap dates and is expected to not match)

Expected signals (NOT stop-ship):

- v2 has MORE rows than Job 1 (v2 fills gap dates, Job 1 only writes target_date) -- healthy
- `source = linear_interpolation` rows appear only in v2 -- healthy
- Overlapping rows match exactly on price and source (except linear_interpolation) -- healthy

### Diff tracking table (to be filled in each day)

| Date | Job 1 rows | v2 rows | Only Job 1 | Only v2 | Both | Price viol. | Source viol. | Decision |
|---|---|---|---|---|---|---|---|---|
| 2026-04-13 | | | | | | | | |
| 2026-04-14 | | | | | | | | |
| 2026-04-15 | | | | | | | | |
| 2026-04-16 | | | | | | | | |
| 2026-04-17 | | | | | | | | |

After 5 clean days, message COO/CTO for GO on Phase 4.

### Monday first-task checklist

1. Read yesterday's first-fire results: `aws s3 ls s3://opal-data-bd/logs/gold-layer/ | grep 2026-04-10` and skim the runner's systemd log from tonight's 22:00 UTC fire. Confirm v2 ran, no crash, canonical_prices.parquet was overwritten, watchdog cleanly shut down the instance.
2. Check bucket versioning: `aws s3api get-bucket-versioning --bucket opal-data-bd`. Pick Option A (versioning) or Option B (live capture).
3. If Option B: write `data/analysis/phase3_capture_snapshots.sh` -- tails CloudWatch log for bd-price-update, detects "Job 1 complete", pulls snapshot, then waits for gold runner systemd silver-prep done marker, pulls second snapshot.
4. Write `data/analysis/phase3_v2_vs_job1_diff.py` per pseudocode above.
5. At ~22:05 UTC Monday: run the capture script. (Or trust versioning and retrieve after the fact.)
6. Tuesday AM: run diff script on Monday's snapshots, record results in the tracking table, commit the diff report under `org/tier2_senior/0.6.0_AE_PartnerETL/logs/2026-04-14/phase3_day1_diff.md`.
7. Repeat Tue-Fri.
8. Friday EOD or Monday 2026-04-20: if all 5 days clean, proceed to Phase 4. If any stop-ship signal: do NOT proceed, open investigation TO.

### What NOT to do during the diff week

- Do NOT disable bd-price-update Job 1 before the diff is clean. v2's output will silently become the only source and we lose the comparison.
- Do NOT edit v2 source during the diff week. Any v2 change invalidates prior diff results.
- Do NOT edit `gold_dispatch.sh` or `run_gold_layer.sh` during the diff week. Same reason.
- Do NOT manually run v2 off-schedule during the diff week (except for debugging a stop-ship signal). Off-schedule runs confuse the snapshot timing.
