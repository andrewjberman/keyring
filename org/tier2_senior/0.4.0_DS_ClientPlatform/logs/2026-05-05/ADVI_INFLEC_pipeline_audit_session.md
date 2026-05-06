# Session Log — Inflection Pipeline Full Audit

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-05-05
**Scope:** Full audit of Inflection pipeline — scripts, S3 backfill/freshness, AWS resources, scheduled triggers, active data-quality items

---

## Summary

On-demand full audit of the Inflection pipeline executed in response to Andrew directive. Covered 47 gold scripts, 4 EC2 runners, 12 Lambda functions, 7 EventBridge rules, S3 artifact freshness across bronze/silver/gold/platinum, and all deployed-code currency in code/gold/.

**Key findings:**
- Infrastructure is fully deployed, Terraform-managed, and correctly structured
- Scheduled triggers (EventBridge crons) are all ENABLED and in correct format
- **Silver chain not propagating**: bronze has 2026-05-01 and 2026-05-05 data but silver stale at 2026-04-28/29 — automation gap
- **Bronze missing days**: May 2–4 absent (May 2–3 may be weekends; May 4 Monday gap warrants investigation)
- **D3 in-flight**: gold/holdings stale at 2026-04-28 expected — D3 chain-full `--from INF_B_00` fired ~20:35Z (ETA complete ~21:20-21:35Z)
- **joe_brandenbrug top_holdings.json now present** (2026-05-05 16:22:38Z) — v10 PENDING marker on this cell may flip
- All platinum artifacts timestamped 2026-05-05 from today's chain run

---

## Audit Scope & Method

- **S3 reads**: `platinum/firm/`, `platinum/advisors/`, `gold/holdings/`, `silver/api_dims/`, `bronze/orion-api-v2/`, `gold/artifacts/`, `code/gold/`
- **Manifest reads**: `infra/aws/ec2/EC2_MANIFEST.json`
- **AWS API**: `aws events list-rules` (all EventBridge rules enumerated)
- **Explore agent**: scanned 47 INF_* scripts, Terraform inf-pipeline workspace, lambda-source-map.json, task orders

---

## Section 1 — EC2 Runners

4 dedicated Inflection instances in EC2_MANIFEST.json (`inf-pipeline` Terraform workspace):

| Instance | ID | Type | Purpose |
|---|---|---|---|
| `inf-gold-layer-runner` | i-0ed5afded2ebd4ed4 | c6a.4xlarge (16 vCPU/32 GB) | PROD gold generation |
| `inf-gold-qa-runner` | i-04373615f03fbf9a9 | c6a.2xlarge | QA runs (manual SSM only) |
| `inf-exporter` | i-081ae6aafb394fb1a | t3.medium | Playwright JWT renewal |
| `inf-bronze-runner` | i-083ad9ae297f88e9f | t3.small | Daily Orion API bronze pulls |

Gold PROD: dispatch-on-demand only (no automated daily gold cron — by design).
Gold QA: manual SSM only per ADVI_INFSHIP.B3 spec.

---

## Section 2 — EventBridge Scheduled Rules

All 7 Inflection rules ENABLED, all in correct cron format.

| Rule | Schedule | Target | Status |
|---|---|---|---|
| `opal-inf-jwt-fetch` | cron(13 12 * * ? *) = 12:13 UTC | inf-jwt-trigger Lambda | ENABLED OK |
| `opal-inf-bronze-runner-cron` | cron(43 12 * * ? *) = 12:43 UTC | inf-bronze-trigger Lambda | ENABLED OK |
| `inf-api-assets-v2-daily` | cron(45 12 * * ? *) = 12:45 UTC | inf-api-assets-v2 Lambda | ENABLED OK |
| `opal-inf-export-schedule` | cron(0 21 * * ? *) = 21:00 UTC | inf-jwt-trigger Lambda (evening) | ENABLED OK |
| `inf-silver-chain-bronze-complete` | S3 ObjectCreated `_BRONZE_COMPLETE.json` | inf-silver-chain Lambda | ENABLED — **NOT PROPAGATING** |
| `inf-otp-state-change` | S3 ObjectCreated `otp/state.json` | inf-otp-relay Lambda | ENABLED OK |
| `opal-inf-ec2-state-change-monitor` | EC2 StateChange events | monitoring Lambda | ENABLED OK |

30-min stagger between JWT (12:13) and bronze (12:43) is correct.
No gold-trigger EventBridge cron — all PROD gold runs are manual dispatch. Consistent with design.

---

## Section 3 — Bronze Backfill

**`bronze/orion-api-v2/` — continuous daily backfill confirmed:**

- 2026-04-01 through 2026-04-30: PRESENT (full daily series)
- 2026-05-01 (Friday): PRESENT
- 2026-05-02 (Saturday): MISSING — likely Orion API unavailable (weekend)
- 2026-05-03 (Sunday): MISSING — likely Orion API unavailable (weekend)
- 2026-05-04 (Monday): **MISSING — warrants investigation** (weekday, cron should have fired)
- 2026-05-05 (Tuesday): PRESENT

Action item: Check CloudWatch logs for `opal-inf-bronze-runner-cron` 2026-05-04 execution. If runner failed: re-trigger manually; if Orion API was down: document and no action.

---

## Section 4 — Silver Layer Freshness

| Dimension | Latest Partition | Expected | Gap |
|---|---|---|---|
| `silver/api_dims/accounts_v2/` | snapshot_date=2026-04-29 | 2026-05-05 | **6 days stale** |
| `silver/api_dims/assets_v2/` | snapshot_date=2026-04-29 | 2026-05-05 | **6 days stale** |
| `silver/api_dims/performance/` | snapshot_date=2026-04-28 | 2026-05-05 | **7 days stale** |

**Root cause (suspected):** `inf-silver-chain-bronze-complete` EventBridge rule fires `inf-silver-chain` Lambda on `_BRONZE_COMPLETE.json` ObjectCreated. If bronze runner is writing data but NOT writing `_BRONZE_COMPLETE.json` sentinel, the Lambda is never triggered.

Bronze has May 1 and May 5 data but silver has none from those dates — the sentinel is not firing or the Lambda is failing silently.

**This is the primary automation gap.** If silver doesn't rebuild, gold chain cannot produce fresh platinum artifacts.

---

## Section 5 — Gold Layer Freshness

**`gold/holdings/`:**
- Max partition date: 2026-04-28
- D3 chain-full `--from INF_B_00` fired ~20:35Z — IN FLIGHT
- ETA complete: ~21:20-21:35Z
- Post-D3 expected: holdings partitions through latest available silver dates

**`gold/artifacts/`:**
- `employee_leaderboard.json`: 2026-05-05 16:23:06Z
- `cumulative_chart.json`: 2026-05-05 16:17:39Z (post-IAM fix)
- `client_mix_timeseries.json`: 2026-05-05 16:17:14Z
- `clients_tab.json`: 2026-04-29 (stale — not regenerated today; last from pre-AUDIT sprint)

---

## Section 6 — Platinum Artifacts (Current State)

All platinum artifacts are from today (2026-05-05). Key values:

| Artifact | generated_at | Key Values | Status |
|---|---|---|---|
| `dashboard.json` | 20:23:35Z | total_aua=$182.55M, advisor_count=3 | STALE (D3 pending) |
| `leaderboard.json` | 20:23:05Z | QTD total_aua=$199.65M, 4 advisors, lifecycle_aua=0 | PARTIAL (Bug A+C pending) |
| `header_metrics.json` | 16:23:37Z | 28KB | OK |
| `mix_summary.json` | 16:22:42Z | 8KB | OK |
| `clients_tab.json` | 16:17:25Z | 55KB | OK |
| `cumulative_chart.json` | 16:17:39Z | geo_drill len=1 | OK |
| `activity_scan.json` | 16:23:58Z | 307 rows | OK |
| `cash_drag.json` | 16:24:08Z | 295 rows | OK |
| `concentration_risk.json` | 16:24:09Z | 295 rows | OK |

**Per-advisor artifacts — all 4 advisors × 4 artifacts = 16/16 present:**
`inflection_wealth_management`, `joe_brandenbrug`, `patrick_scanlan`, `peter_lee` — all have `top_holdings.json`, `composition.json`, `book.json`, `summary.json` (all timestamped 16:22-16:23Z today).

`joe_brandenbrug/top_holdings.json` is new today (16:22:38Z) — previously identified as RED-MISSING in v9 matrix. This cell may flip in v10.

---

## Section 7 — Deployed Gold Scripts (code/gold/)

47 INF_* scripts deployed. All present. Recent updates (2026-05-05):

| Script | Deployed | Change |
|---|---|---|
| `INF_I_D03.composition_artifacts.py` | 16:27 | Most recent |
| `INF_D_08.nmec_nmnc_nna.py` | 16:07 | New script (NNA decomp publisher) |
| `INF_D_00c.portal_leaderboard.py` | 16:07 | AUDIT-003a fix + ADVI_LDRBRD.001 |
| `_orion_api_silver_lib.py` | 15:30 | AE 0.7 silver lib fix (FE gate) |
| `INF_D_04.client_portal_summary.py` | 13:17 | S7SUMFIX |
| `INF_B_00.canonical_holdings.py` | 14:08 | B-chain canonical holdings fix |
| `INF_I_D00c.cumulative_chart.py` | 11:12 | AUDIT-006 geo_drill |

Baseline mass-deploy: 2026-04-27 to 2026-04-29 (full A/B/C/D/I chain).

---

## Section 8 — Active Data Quality Items

| Item | Artifact | Root Cause | ETA Fix |
|---|---|---|---|
| `total_aua = $182.55M` (should be ~$199M) | `dashboard.json` | gold/holdings stale; D3 in-flight | ~21:20-21:35Z (D3 complete) |
| `lifecycle_aua = 0 all advisors` | `leaderboard.json` | ADVI_LDRBRD.001 Bug C — wiring in INF_D_00c | ~22:00Z (D4 post Bug C fix) |
| `period_start_aua MAX null` | `leaderboard.json` | ADVI_LDRBRD.001 Bug A — MAX window fallback | ~22:00Z (D4 post Bug A fix) |
| `active_since null all advisors` | `platinum/advisors/*/summary.json` | INF_D_04 publisher emits null; consumer disabled for Inflection | GRAY-by-design (non-blocking) |
| Silver chain not propagating | `silver/api_dims/*` | `_BRONZE_COMPLETE.json` sentinel not triggering inf-silver-chain Lambda | Needs investigation |
| May 4 bronze missing | `bronze/orion-api-v2/2026-05-04/` | Cron fired but runner failed, or Orion API down | Needs CloudWatch log check |

---

## Open Items / Next Actions

1. **D3 RAVC5''** — Await AE/COO message (~21:20-21:35Z): dashboard.json advisor_count=4, total_aua ~$199M
2. **ADVI_LDRBRD.001 ship** — DS~D (~21:35-21:50Z): Bug A MAX fallback + Bug C lifecycle wiring
3. **D4 dispatch + RAVC** — (~21:50-22:00Z): leaderboard.json period_start_aua + lifecycle_aua populated
4. **v10 routing window** (~22:15-22:30Z): fill all TODO markers with D3/D4 empirical, route diff to CTO + DT in same turn
5. **Silver chain investigation** — Post v10 close: check `inf-silver-chain` Lambda CloudWatch logs for May 1 + May 5 executions; check if `_BRONZE_COMPLETE.json` is being written by bronze runner
6. **May 4 bronze gap** — Check `opal-inf-bronze-runner-cron` CloudWatch logs for 2026-05-04

---

## Compiler Tools Log

| Date | Agent | Tool | Command | Result |
|---|---|---|---|---|
| 2026-05-05 | DS~A | aws s3 ls | `s3://opal-data-inf/platinum/firm/` | All 16 firm artifacts present; timestamps 2026-05-05 |
| 2026-05-05 | DS~A | aws s3 ls | `s3://opal-data-inf/platinum/advisors/` | 4×4 advisor artifacts present; joe_brandenbrug/top_holdings.json NOW PRESENT |
| 2026-05-05 | DS~A | aws s3 cp | `dashboard.json` | total_aua=$182.55M, advisor_count=3, generated_at 20:23:35Z (D3 pending) |
| 2026-05-05 | DS~A | aws s3 cp | `leaderboard.json` | QTD total_aua=$199.65M, lifecycle_aua=0, period_start_aua MAX null |
| 2026-05-05 | DS~A | aws s3 ls | `gold/holdings/` | Max date 2026-04-28; D3 in-flight |
| 2026-05-05 | DS~A | aws s3 ls | `silver/api_dims/performance/` | Max snapshot_date=2026-04-28 (stale) |
| 2026-05-05 | DS~A | aws s3 ls | `bronze/orion-api-v2/` | Missing 2026-05-02/03/04; present 2026-05-01 + 2026-05-05 |
| 2026-05-05 | DS~A | aws s3 ls | `code/gold/` | 47 INF_* scripts present; most recent INF_I_D03 16:27 |
| 2026-05-05 | DS~A | aws events list-rules | all prefixes | 7 Inflection rules enumerated; all ENABLED |
| 2026-05-05 | DS~A | EC2_MANIFEST.json | read | 4 inf-* instances confirmed |
