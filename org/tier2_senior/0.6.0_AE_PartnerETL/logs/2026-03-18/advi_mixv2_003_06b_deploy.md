# ADVI_MIXV2.003 — 06b Deploy + Gold Run — 0.6.0_AE_PartnerETL

**Date:** 2026-03-18
**Start Time:** 13:45 UTC
**End Time:** 15:50 UTC

## Objective

Deploy the updated `06b_build_client_mix_timeseries.py` (DS commits ADVI_MIXV2.001 + ADVI_MIXV2.002)
to bd-gold-layer-runner, run the insurance AP gate diagnostic to populate `insurance_accounts.json`,
and execute a full rebuild to produce `firm_mix_views.json` and per-advisor `mix.json` artifacts.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Verify DS dependencies on CLOUD | `a7617a08` (AP gate), `a885f625` + `2384a9f6` (firm/advisor views) confirmed |
| 2 | Read devops-brief-mixv2-001.md + 002.md | Insurance diagnostic required before full rebuild |
| 3 | Run `.tmp_insurance_ap_gate.py` locally | 539 partitions scanned; 109 accounts identified as gated |
| 4 | Populate `insurance_accounts.json` | 109 account_ids, 180-day override — `8d054663` |
| 5 | `safe-ec2-deploy.sh bd-gold-layer-runner` | All gold scripts synced to `s3://opal-data-bd/code/gold/` — `be7ac233` |
| 6 | Start EC2 instance (i-01003b035d2988dfb) | Instance running, SSM online |
| 7 | SSM: incremental smoke test | Loaded 109-account insurance config, 20 advisors — SUCCESS |
| 8 | SSM: full rebuild attempt | Instance auto-stopped mid-run (boot incremental finished, self-shutdown fired) |
| 9 | Diagnose: 06b position in run_gold_layer.sh | 06b was running BEFORE 08b — could not read rel_architect_lookup |
| 10 | Fix: move 06b after 08b in both modes | `b427502d` — committed and pushed |
| 11 | Upload fixed run_gold_layer.sh to S3 | `s3://opal-data-bd/code/gold/run_gold_layer.sh` updated |

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Run diagnostic locally, not on EC2 | `s3://opal-data-bd` accessible with local creds; faster turnaround than SSM roundtrip |
| 109 accounts selected (not all 118) | Only accounts with `snap_dates_excluded > 0` are actually gated out; remaining 9 have no excluded dates |
| Move 06b to after 08b in both incremental and full modes | 06b reads `rel_architect_lookup.parquet` written by 08b; running before 08b means it uses a stale or missing mapping |
| Did not trigger run_gold_layer.sh full this session | Full run takes 2+ hrs; sequence fix committed; next daily incremental and monthly full will use correct order |

---

## Diagnostic Findings

Insurance AP gate scope was larger than DS estimated ($60M) — actual impact was $24B cumulative over 18-month window:

```
Accounts examined:        118
Total MV when INCLUDED:   $2,363,683,767
Total MV when EXCLUDED:   $24,182,394,244
Oscillation source:       $24.2B disappears when 45-day AP gate fires
```

Root cause: 109 accounts (insurance/annuity products — SHIELD, BUFFER, Cap 20%, etc.) have
`account_performance.last_seen` in 2023 (quarterly statement cycle). The 45-day gate
excludes them from every snapshot date in the 18-month window.

`insurance_accounts.json` committed at `8d054663` with all 109 account_ids and `ap_gate_days_override: 180`.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/insurance_accounts.json` | Populated with 109 gated account_ids | Yes — `8d054663` |
| `data/black_diamond/scripts/gold/run_gold_layer.sh` | Moved 06b after 08b in both incremental and full modes | Yes — `b427502d` |
| `org/tier2_senior/0.6.0_AE_PartnerETL/task_orders/ADVI_MIXV2.003.ec2-06b-deploy.md` | Status -> in_progress | Yes — `8eda0ed9` |
| `infra/aws/ec2/EC2_MANIFEST.json` | Deploy recorded at commit `8d054663` | Yes — `be7ac233` |

---

## Current State

**Status:** IN PROGRESS

Active deployment: `b427502d` is the current HEAD on CLOUD. `run_gold_layer.sh` is
updated on S3 (`s3://opal-data-bd/code/gold/run_gold_layer.sh`). The current boot
incremental (started 15:30 UTC) is running on i-01003b035d2988dfb with the old script
order (06b before 08b) — but 06b found no new partitions so no data was written either way.

`firm_mix_views.json` and `gold/advisors/*/mix.json` do NOT yet exist in S3. They will be
written by the next run that (a) uses the corrected script order and (b) processes at least
one new partition date.

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Trigger `run_gold_layer.sh full`** after current incremental
   shuts down — required to satisfy acceptance criterion of >=4 quarterly periods in
   `firm_mix_views.json`. Full run will process all 2,086 historical partitions with 06b
   running after 08b (rel_architect_lookup current).

2. **[0.6.0_AE_PartnerETL] Verify S3 outputs** after full run:
   - `aws s3 ls s3://opal-data-bd/gold/firm_mix_views.json`
   - `aws s3 ls s3://opal-data-bd/gold/advisors/ --recursive | grep mix.json | wc -l` (expect 19+)
   - Spot-check pct sums using verification script in devops-brief-mixv2-002.md

3. **[0.6.0_AE_PartnerETL] Mark task order complete** once S3 verification passes.

4. **[0.4.0_DT_ClientPlatform] Fix CHANGELOG.json for partners-api** — ADVI_MIXV2.004
   Lambda deploy (partners-api-v1.3.0) was deployed correctly but `record-terraform-deploy.sh`
   was not run. CHANGELOG.json still shows v1.1.0 as last entry.

**Files to touch next:**
- Trigger: `bash /tmp/gold_layer_scripts/run_gold_layer.sh full` via SSM on i-01003b035d2988dfb
- Verify: `s3://opal-data-bd/gold/firm_mix_views.json`

**Do NOT:**
- Run `python3 06b_build_client_mix_timeseries.py --upload --incremental` as the full rebuild — incremental with no new partitions produces no output
- Start the instance and assume the boot script will run full mode — boot always runs incremental
