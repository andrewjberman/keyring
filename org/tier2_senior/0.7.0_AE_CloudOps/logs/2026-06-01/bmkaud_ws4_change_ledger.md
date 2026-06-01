# BMKAUD WS-4 — Benchmark/Peers Change Forensics + Deploy-Ops Ledger

**Audit:** `docs/briefs/benchmark-yang-truth-audit-20260601.md` (Andrew-direct) · **Lane:** 0.7.0_AE_CloudOps (WS-0 + WS-4) · **Owner:** 1.0.0_SA_CTO · **Verify:** 3.0.0_SA_CVO (WS-5)
**Method:** git forensics (repo) + LIVE AWS verification (not repo-read alone). All times ET unless marked UTC/Z.

---

## BOTTOM LINE
1. **SmartX injection into the Benchmark producer is FULLY REVERTED** (commit `80224d674`). LIVE deployed code proven pure-yang (CodeSha256 identity + deployed-bytes grep). No other SmartX swap remains in the benchmark producer.
2. **`smartx-model-monthly-pull` is a TRUE ORPHAN (Finding #1)** — producer lambda + daily 09:35 ET schedule + script + source-map entry all still present; the 2 sidecars it writes have ZERO consumers post-revert. Schedule now DISABLED (WS-0 freeze). **Recommend full retirement.**
3. **`opal-data-portal-v2` bucket policy is UNMANAGED by Terraform** — a rigid-deploy-ops gap (Finding #2). The anti-clobber Deny (MDPF IAM-A) folds into the WS-4 managed-import pass.
4. **ONE deploy of the revert today** (yang-v2.4.9); the apparent "two deploys" was an ET-vs-UTC artifact.
5. **Peers UST-1M gap is NOT in SmartX scope** — `yang-generate-peer-performance` is 100% Excel-sourced, never touched by the SmartX work; `PERIODS` includes `1M` (reads Excel). Source-Excel data gap → WS-2/WS-3.

---

## A. CHANGE LEDGER (to-the-minute)

### A.1 yang-model-portfolio-benchmarks/lambda_function.py
| time (ET) | hash | author | delta |
|---|---|---|---|
| 2026-04-13 10:25 | bc6f4ccb6 | DS-CP | SI-annualization REMOVE (SI→absolute cumulative) |
| 2026-04-13 14:43 | 62985fcf0 | DS-CP | SI-annualization RESTORE + LATEST.json fix |
| 2026-05-04 11:09 | e2f0a8077 | 0.5.0_AE | MDLP_RVVALT.003: emit model_portfolio_timeseries.json |
| 2026-05-04 13:17 | 2c18f0c06 | 0.5.0_AE | MDLP_RVVALT.004: duration-matched RFR (UST/ST=1Y,INT=5Y,LTC/LTA=10Y) |
| 2026-05-04 14:08 | 1c80f15e7 | 0.5.0_AE | drop weekend rows (sqrt(252) fix) |
| 2026-05-04 14:55 | cdc2271c4 | 0.5.0_AE | drop holiday rows (clean 252 td/yr) |
| **2026-05-21 14:17** | **84128c245** | 0.7.0_AE~A | **[B1/B2] DUAL-INPUT (yang+smartx); per-period model_source label** |
| **2026-05-22 11:05** | **9f6357634** | 0.7.0_AE | **[B3/B4] SmartX-realized end-to-end; adds timeseries_realized key** |
| **2026-06-01 09:41** | **80224d674** | 0.7.0_AE (code: DS-CP) | **[REVERT] pure-yang; drops all SmartX load/override + timeseries_realized (+36/-224)** |

### A.2 yang-generate-peer-performance/lambda_function.py
Last touched **2026-04-06** (629a2fef8, DT-CP: filename regex + cache-control). **Never part of SmartX work.** Excel-driven; `PERIODS` (line 55) includes `1M`.

### A.3 smartx producer — pull_smartx_model_monthly_performance.py
| time (ET) | hash | author | delta |
|---|---|---|---|
| 2026-05-21 14:06 | 1d2e312c4 | 0.7.0_AE~A | [B1/B2] ADD — emits `_smartx_model_monthly.json` |
| 2026-05-22 10:56 | aa9f285bc | 0.7.0_AE | [B3/B4] add `_smartx_model_daily.json` sidecar |

### A.4 Terraform
| time (ET) | hash | file | delta |
|---|---|---|---|
| 2026-05-21 14:09 | 48c651f1d | smartx-pipeline/model-perf-pull.tf | NEW lambda + IAM + `aws_scheduler_schedule` cron(35 9 ET). **Only commit to ever touch this file** until the freeze. |
| 2026-06-01 ~14:44 | f38353b0f | smartx-pipeline/model-perf-pull.tf | **[WS-0 FREEZE] state=DISABLED** (this audit) |
yang-pipeline `lambdas.tf` NOT modified by B1–B4 (benchmark+peer module blocks predate the SmartX work).

### A.5 lambda-source-map.json
| time (ET) | hash | delta |
|---|---|---|
| 2026-05-21 14:09 | 48c651f1d | added smartx-model-monthly-pull entry |
| 2026-06-01 09:47 | 3d3de4565 | revert artifact upload (sha IYrvZ0zN) |
| 2026-06-01 09:50 | fbdf5f687 | record-deploy bump |
(Minor deploy-ops note: the source-map `yang-model-portfolio-benchmarks` entry did not surface `artifact_sha256`/`last_deployed_commit` on direct key-read — field-naming/structure differs from expectation; sha provenance is nonetheless PROVEN via live CodeSha256 below. Flag for source-map schema-consistency follow-up.)

### A.6 CHANGELOG deploy records
- yang-pipeline: yang-v2.4.7 (05-21 B1/B2) → 05-22 B3/B4 → **yang-v2.4.9 (06-01 09:50 ET / 13:50 UTC, deployed_commit pin 447e1bbb, functions:[yang-model-portfolio-benchmarks], commits incl 80224d674)**.
- smartx-pipeline: v1.1.0 (05-21) → 05-22 daily-sidecar. **No deploy after 05-22 → orphan producer never un-deployed** (until WS-0 disable).

---

## B. REVERT COMPLETENESS — PROVEN COMPLETE (live)
- **LIVE `CodeSha256` of yang-model-portfolio-benchmarks = `IYrvZ0zN+9+30dPON9sSxicvZbRJ6c/7mrH31a1hiw0=`** == artifact sha built from revert `80224d674` (== yang-v2.4.9). Hash identity ⇒ deployed zip IS the revert source. LastModified 2026-06-01T13:48:15Z.
- **Downloaded the live deployed zip (7385 B) + grepped:** `smartx|sidecar|timeseries_realized|realized` → 5 hits, **ALL comments** (lines 53-54, 223-225, 335-336, documenting removal). `model_source='yang_design'` hardcoded (line 230). **Zero live SmartX code in deployed bytes.**
- `timeseries` (yang, MDLP_RVVALT Sharpe/drawdown consumer) unchanged by revert ⇒ zero regression there.

## C. FINDING #1 — `smartx-model-monthly-pull` TRUE ORPHAN (retire-candidate)
| component | state | 
|---|---|
| Schedule `smartx-model-monthly-pull-daily` | was ENABLED `cron(35 9 ET)` → **DISABLED** (f38353b0f, live-verified) |
| Lambda `smartx-model-monthly-pull` | deployed, last 2026-05-22, never un-deployed |
| Script `data/smartx/scripts/pull_smartx_model_monthly_performance.py` | exists; writes `json/benchmarks/_smartx_model_{monthly,daily}.json` |
| source-map entry | present (unchanged) |
| **Consumers** | **NONE** — repo-wide grep for `_smartx_model_monthly`/`_smartx_model_daily` finds only docs/logs/TO/source-map/producer; no live code reads them post-revert |
**Recommendation (per COO ruling):** FULL RETIREMENT post-CVO sign-off — remove `model-perf-pull.tf` (lambda+role+schedule), the script, and the source-map entry; optionally delete the 2 stale sidecars. The disable is the interim freeze; retirement closes the residual SmartX-era writer.

## D. TWO-DEPLOY RECONCILE — ONE DEPLOY
`09:50:46 ET == 13:50:46 UTC`. The "yang@447e1bbb 09:50 (ET)" baseline entry and "yang-v2.4.9 13:50 (UTC)" are the SAME deploy event. Revert code authored by DS-CP, landed/deployed via AE-CloudOps lane. `447e1bbb` = HEAD-pin COO drive commit at apply (not a yang source commit); code delta = `80224d674`. Deploy footprint: 3d3de4565 (upload) → apply → fbdf5f687 (record). Latest deployed = pure-yang. **No earlier/second yang-benchmark deploy today.**

## C-bis. FINDING #3 — EC2 dual-writer of `benchmark_returns.json` (DORMANT, latent clobber)
`infra/aws/ec2/smartx-exporter/smartx-workspace/scripts/generate_benchmark_performance.py` (smartx-exporter instance) writes the SAME serving key `json/benchmarks/benchmark_returns.json` (line 49) — Yang-sourced but with its OWN period math (`calculate_period_return` 30/90/365-day windows, distinct from the lambda's yang trailing-calendar). **DORMANCY CONFIRMED:** repo-wide grep finds NO cron / systemd / autostart / run-all-portfolios.sh reference invoking it → no automated execution path. **Latent (manual-run-only) clobber vector**, not active. If ever run manually it would overwrite the lambda's pure-yang `benchmark_returns.json` with divergent-period-math values + desync legacy-vs-comprehensive. **Disposition (DS-CP item B):** confirmed dormant; recommend REMOVE/quarantine the script (repo + smartx-exporter instance via safe-ec2-deploy) in the WS-4 managed-cleanup batch so the lambda is the SOLE `benchmark_returns.json` writer. Low urgency (dormant); fold into the post-ratify cleanup with the smartx retirement.

## E. NON-TF / MANUAL CHANGES
1. **Finding #2 — `opal-data-portal-v2` bucket policy UNMANAGED by Terraform.** No `aws_s3_bucket`/`aws_s3_bucket_policy` resource anywhere; live policy = 2 OAC `s3:GetObject` statements (AllowCloudFrontOAI + AllowCloudFrontOACPublicData). The anti-clobber Deny (MDPF IAM-A) must `terraform import` + merge here (CTO import ruling pending) — folds into the WS-4 managed pass.
2. **Orphan dangling infra** (Finding #1) — TF-managed but revert-left-behind; retire or explicitly accept.
3. **No undocumented/console deploys found** — every artifact upload + apply on these surfaces has a matching source-map upload commit + CHANGELOG record; no `aws lambda update-function-code` evidence.
4. **Out-of-scope (not a revert defect):** Peers UST-1M gap = `yang-generate-peer-performance` Excel source-data, not SmartX/code (last code change 2026-04-06; PERIODS includes 1M). Triage in WS-2/WS-3.
