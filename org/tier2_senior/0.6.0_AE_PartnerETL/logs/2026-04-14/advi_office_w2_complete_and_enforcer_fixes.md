# 0.6.0_AE Log: ADVI_OFFICE W2 Complete + Enforcer Fixes + Phase 3 Day 1
**Date:** 2026-04-14
**Agent:** 0.6.0_AE_PartnerETL
**Tags:** security-scanner-v1.0.1, security-scanner-v1.0.2
**Related:** ADVI_OFFICE.W2, ADVI_GLDRST.022 Phase 3, ec2-auto-shutdown-enforcer

---

## Session Summary

Full session covering: Phase 3 Day 1 diff (missed last night), two enforcer fixes (one wrong, one correcting it), ADVI_OFFICE W2 gold run (blocked on QA capacity, resolved by running D_03+D_04 locally), and an architectural correction from Andrew on the PROD trigger pattern.

---

## 1. Phase 3 Day 1 Diff

Phase 3 diff script (phase3_v2_vs_job1_diff.py) was not run last night as planned. Fixed subprocess issue on Windows (boto3 replaces aws_cli), then ran.

**Results (2026-04-13):**

| Metric | Value | Status |
|---|---|---|
| Overlap rows | 10,668,634 | - |
| Price violations | 0 | PASS |
| Source violations | 0 | PASS |
| Only in Job 1 | 10,100 | Design gap (see below) |
| Only in v2 | 30 | Expected (linear_interpolation) |

Root cause of 10,100 only-in-Job1 rows: all from 2026-04-12 (Sunday). v2 spine ends at `transactions['trade_date'].max()` (Friday). Fixed in build_canonical_prices_v2.py (commit ecbdee3b): `global_end_date = max(tx_max, today)` so spine extends to today and ffill covers weekends. Uploaded to S3 — tonight's 22:00 UTC run will validate the fix (expect 0 only-in-Job1 rows for Day 2).

Also confirmed: S_00 hotfix (2a6136e4) effective — canonical_prices.parquet got 3 new versions at 22:02-22:04 UTC on 2026-04-13 (first successful S_00 prod run).

---

## 2. bd-fees First Prod Run Confirmation

fees-download-2026-04-13.log confirmed:
- Downloaded: Fees_OpalCapital_Daily_2026-04-10_to_2026-04-10.xlsx (179 KB)
- Silver: silver/fees/2026-04-10.parquet (1,079 rows, 89,539 bytes)
- Silver conversion started: 2026-04-13T22:17:32Z (on schedule)
- Exit code: 0

bd-fees pipeline healthy.

---

## 3. ec2-auto-shutdown-enforcer: Two Fixes (One Wrong)

### Background
Andrew got an email "idle for 1 hour was shut down." The stop_reason string printed `running_minutes` (total uptime) rather than idle duration, so "idle 60m" meant the instance had been running 60 min total — not that it was idle for 60 min. The actual behavior was correct: instance ran gold scripts for ~45 min, went idle, enforcer caught it ~15 min later. Only the message was confusing.

### Fix 1 (WRONG) — security-scanner-v1.0.1
Misdiagnosed the cause as CloudWatch data delay. Widened lookback to 45 min with Period=300, assessed last 3 datapoints. This broke the enforcer: on a c6a.16xlarge (64 vCPUs), one Python process = ~1.5% instance CPU, which is below the 5% idle threshold even mid-run. The wider lookback delivered CW data faster, and the enforcer killed the QA runner mid-run during the D_02→D_03 transition.

**Mistake:** Misread the "1 hour" message as a CW delay symptom. It was a message formatting issue, not a timing issue.

### Fix 2 (CORRECT) — security-scanner-v1.0.2
Reverted CW lookback to original 15-min single-period window. Only kept the message string fix: reason now says "idle CPU for last 15m (avg X% < 5%), running Ym total" so idle window and total uptime are clearly separate.

**Also added:** `AutoShutdown=disabled` tag to QA runner (i-0090b823a4a0997e3) so enforcer never stops it regardless.

### Deployment Sequence

| Step | Commit | Tag | Result |
|---|---|---|---|
| Wrong fix | 2685a689 | security-scanner-v1.0.1 | Applied, killed QA runner mid-run |
| Revert to correct | e93d5d86 | security-scanner-v1.0.2 | Applied, 0-diff, live |

---

## 4. ADVI_OFFICE W2 — Gold Run

### Pre-checks
- D_00b ETag: b1255ef7bf58c105199a926f83dead05 — matches DS fix #3 (5b4439e1, float→int normalization for relationship_id in _build_rel_office_dim_d00b)
- dim_advisor_office.csv: already on S3 from prior session
- AutoShutdown=disabled tag set on QA runner

### QA Run Attempt
Dispatched `--group D` to QA runner (i-0090b823a4a0997e3) at 12:59:45Z.

| Script | Result | Time |
|---|---|---|
| D_00 | DONE | ~25s |
| D_00b | DONE — no crash, OFC keys confirmed | 197s |
| D_00c | DONE | 56s |
| D_01 | DONE | 222s |
| D_02 | DONE | ~6 min |
| D_03, D_04 | NOT RUN — enforcer (v1.0.1 wrong fix) killed instance at 13:16 UTC |

### Capacity Block
After stopping, c6a.16xlarge showed InsufficientInstanceCapacity in us-east-1d. Instance is AZ-pinned, cannot move.

### Resolution — D_03 + D_04 run locally
COO authorized running D_03+D_04 locally (same production S3 bucket, credentials work).

- D_03.composition_artifacts.py --upload: 52 advisor files, 2,786 relationship files, firm composition, mix views. Completed 13:59:21 UTC. No OOM.
- D_04.client_portal_summary.py --upload: 20,476 platinum files (firm dashboard, advisor summaries, client summaries/timeseries, account summaries, partner analytics, leaderboard, pass-throughs). Completed 14:09:13 UTC.

### Platinum Spot-check
```
platinum/firm/partner_analytics_quarterly.json:
  views keys: ['aua', 'nna', 'geo', 'adv', 'ofc', 'cla']
  views.ofc present: True
  ofc period keys: ['current', 'q1', 'q2', 'q3']
  office segments: 10 (Austin, Dallas, Los Angeles, Jacksonville, Arkansas, Atlanta, Minnesota, Kansas City, ...)
platinum/firm/timeseries_chart.json: ofc + nna_ofc top-level keys present
```

All W2 acceptance criteria met.

### PROD Runner Error (corrected)
Mistakenly triggered bd-gold-trigger Lambda following the W2 task order's "Promote: trigger PROD gold run" step. Andrew corrected: this step is architecturally wrong and must never appear in a task order again. QA runner and PROD runner share the same production S3 bucket — QA run artifacts ARE production. PROD runner is nightly EventBridge only, never manually triggered.

PROD runner stopped mid-run (was running incremental chain for ~5 min before stopped). No damage — nightly run at 22:00 UTC will re-run clean.

**W2 task order corrected:** removed step 3 ("Promote: trigger PROD gold run"). Added NOTE comment explaining the rule. COO notified to audit all pending TOs for this pattern.

### DE + COO Signaled
MCP messages sent:
- 0.4.0_DE_ClientPlatform: W2 complete, OFC live in platinum, proceed with W3
- 2.0.0_SA_COO: W2 complete, platinum OFC confirmed, DE signaled, architectural correction noted

---

## Architectural Correction — Permanent Rule

**No PROD gold trigger after QA runs.** QA runner writes directly to production S3. Artifacts are live the moment QA run completes. bd-gold-layer-runner is nightly EventBridge only. This rule is now in MEMORY.md (feedback_no_prod_gold_trigger.md) and CLAUDE.md.

---

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | Register + check inbox | PID 28608, inbox empty |
| 2 | Phase 3 Day 1 diff (boto3 fix) | 0 violations, 10,100 Sunday gap |
| 3 | v2 spine fix (ecbdee3b) | extend to today, S3 upload, pushed |
| 4 | Enforcer wrong fix (2685a689) | security-scanner-v1.0.1 — killed QA runner |
| 5 | Enforcer correct fix (e93d5d86) | security-scanner-v1.0.2 — 0-diff, live |
| 6 | AutoShutdown=disabled tag on QA runner | Set on i-0090b823a4a0997e3 |
| 7 | W2 QA run dispatch | D_00-D_02 passed; D_03-D_04 blocked on capacity |
| 8 | D_03 local run --upload | 52 advisors, 2786 relationships, mix views |
| 9 | D_04 local run --upload | 20,476 platinum files |
| 10 | Platinum OFC spot-check | views.ofc present, 10 segments |
| 11 | Mistakenly triggered PROD runner | Stopped; no damage |
| 12 | W2 task order corrected | Removed PROD trigger step |
| 13 | MCP: DE + COO | W2 complete, W3 GO |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| Phase 3 diff | boto3 list_object_versions + download | phase3_v2_vs_job1_diff.py --fetch 2026-04-13 | 3 versions captured, 0 violations |
| Pre-W2 | S3 code check | aws s3 ls ... grep D_00b | ETag b1255ef7 confirmed (DS fix #3) |
| Pre-W2 | S3 code check | aws s3 ls ... grep D_01 | Confirmed ready |
| Post-D_04 | Platinum spot-check | aws s3 cp platinum/firm/partner_analytics_quarterly.json | views.ofc: 10 segments |
| Post-D_04 | Platinum spot-check | aws s3 cp platinum/firm/timeseries_chart.json | ofc + nna_ofc keys present |

comp-blast/comp-pipescript not applicable this session (no gold script edits, read-only analysis + local execution).

---

## Current State

| Component | State |
|---|---|
| ADVI_OFFICE.W2 | COMPLETE — platinum OFC live |
| ADVI_OFFICE.W3 | DE signaled, in progress |
| Phase 3 Day 1 | DONE — 0 violations, Sunday gap (design, fixed in v2) |
| Phase 3 Days 2-5 | Run after each 22:00 UTC gold run |
| build_canonical_prices_v2.py | Spine-to-today fix live on S3 |
| ec2-auto-shutdown-enforcer | security-scanner-v1.0.2 live — correct 15-min window |
| QA runner (i-0090b823a4a0997e3) | Stopped, AutoShutdown=disabled tag set |
| PROD runner (i-01003b035d2988dfb) | Stopped (manually stopped after erroneous trigger) |

---

## Next Steps

- **[0.6.0_AE_PartnerETL] Tonight after 22:00 UTC gold run:** Run Phase 3 Day 2 diff: `python data/analysis/phase3_v2_vs_job1_diff.py --fetch 2026-04-14` — expect 0 only-in-Job1 rows (spine-to-today fix should close the Sunday gap)
- **[0.6.0_AE_PartnerETL] Days 3-5 (Apr 15-17):** Repeat Phase 3 diff each morning
- **[2.0.0_SA_COO]** Audit all pending/staged TOs for "trigger PROD runner" step and remove
- **[DS, follow-up]** PROFAU.003 QA check: verify platinum/advisors/{id}/summary.json contains tax_exposure.capital_gains_ttm + cost_basis_by_year (D_02 ran on QA this morning)
