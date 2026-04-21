# Session Log — 0.6.0_AE_PartnerETL
**Date:** 2026-04-21 (+ tail of 2026-04-20 Session 3)
**Branch:** CLOUD
**Status:** Paused — awaiting Andrew GO on chain full; backfill complete, both runners stopped

---

## Scope of this log

Picks up where 2026-04-20/session2_ec2_group_d_watchdog.md left off. Covers:

1. **Session 3 (2026-04-20 afternoon→night):** FIX wave PROD deploy, RCA closure, multiple qa-runner cycles, D_02 KeyError fix cycle, `--from <id>` feature shipped
2. **Overnight (2026-04-20 23:00Z → 2026-04-21 04:20Z):** Both scheduled nightly fires failed at B_00 `NameError: defaultdict`
3. **2026-04-21 morning:** RCA, B_00 import fix deploy, Schwab silver sync, role_aua backfill complete

Not included: ADVI_STAUDT.INV1 closeout (logged separately in `staudt_inv1_historical_nna_mechanism.md`).

---

## Timeline (UTC)

### 2026-04-20 Session 3 — Post-FIX-wave validation + multiple qa-runner cycles

| Time | Event |
|---|---|
| 16:57Z | QA dispatch `d749a6b2` — Group D FIX1+FIX2+FIX6+FIX7 first attempt. **Watchdog killed mid-D_02 at 17:06:55Z.** |
| 17:15Z | Restarted QA; forensics pull |
| 17:19Z | Widened watchdog regex `9139086d` committed + uploaded + live-patched QA |
| 17:21Z | Re-dispatch `b5ad3829` (+ GOLD_KEEP_ALIVE marker as belt-and-suspenders) |
| 17:47Z | QA Group D clean 17:47:29Z. D_04 wall 399.2s. All 7 scripts clean. Widened regex caught manual-SSM processes for 5 consecutive watchdog cycles during active run. Marker removed + verified missing. |
| 18:00Z | DT extended validation pack fires. All 4 PROD-blocking RAVC4 closed (FIX7, FIX3A, FIX6 Phase 2, FIX2) |
| 18:41Z | RCA authored (`RCA_20260420_watchdog_shutdown.md`), Q1-Q6 answered to CTO. Commit `9a700351` |
| 19:16Z | CTO appended Q3 addendum to RCA (30m→10m uptime threshold window analysis). Commit `d9a419aa` |
| 19:23Z | PROD Group D dispatch `3e06059f` — manual-SSM, killed systemd gold-layer-runner.service first. c6i.16xlarge. |
| 19:49Z | PROD Group D clean. All FIX1/FIX2/FIX6/FIX7 PASS on PROD (platinum layer evidence). Widened watchdog proven end-to-end on PROD (active protection + idle-reap). |
| 19:58Z | QA `c6i.16xlarge` → `c6a.16xlarge` revert (per session 2 plan) |
| 20:12Z | DS staged 4 scripts for tonight's nightly: D_00 4299e1c0 + D_02 035352c3 + D_04 8593ea51 + B_00 081223b5 |
| 20:22Z | Andrew GO: D_02-onward dispatch for RD 5-invariant validation |
| 20:40Z | c6a.16xlarge InsufficientInstanceCapacity in us-east-1d. Sized DOWN to `c6a.8xlarge` (mem_peak ≤14.4GB, fits in 64GB). First-ever 8xlarge gold run. |
| 20:43Z | `--from D_02` feature shipped (`d13b11d5`) — commit + push + S3 upload while waiting. First new CLI mode in gold_dispatch in weeks. |
| 20:44Z | Dispatch `ed77b4d3` — `--from D_02 --bg --no-shutdown`. **D_02 crashed at 52s with KeyError.** Bug in DS commit `035352c3`: `_acct_adv_role_books` builder at L1157-1174 missing `first_date`/`last_date` groupby. Latent — never exercised because 035352c3 was never on S3 until today. |
| 20:56Z | ~D authored fix `048af6a3`, DT uploaded to S3 by 20:58Z |
| 21:00Z | Re-dispatch `d67a844f` — `--from D_02` on 048af6a3 |
| 21:22Z | CHAIN `from:D_02` clean — 21m40s wall. D_02 fix validated end-to-end. |
| 21:22Z | DT validates (RIDE +$6.3M YTD Travis, $2.46M residual is methodology-scope) |
| 21:40-21:41Z | **Confusion window:** COO MCP'd "disable nightly" citing Andrew 21:38Z. AE DISABLED rule at 21:41Z. 90s later DT MCP'd "re-enable" citing Andrew 21:41Z. Andrew's direct chat was ambiguous; AE flagged escalation. **DT re-enabled directly** (lane crossing into AE's EventBridge ownership, self-flagged) at 21:42Z. |
| 21:57Z | QA `--group D` full dispatch `fe8d3e9b` (D_00 4299e1c0 + D_02 048af6a3 + D_04 8593ea51 + rest of D at HEAD). c6a.8xlarge. |
| 22:22Z | --group D clean 22:22:09Z. 26m07s wall. Validates scope under new sizing. |
| 22:00Z | Andrew briefed AE on RD 0.4.2's 2-command sequence: (1) `--backfill-role-aua` + (2) `--chain full`. Bundle in tonight's scheduled run. |
| 22:09Z | AE pre-flagged CTO + COO. Deploy-freshness MATCH on D_00/D_00b/D_00c/D_02/D_04. |
| 22:11Z | CTO asked 3 clarifying questions on backfill (partition range, race with nightly, phantom-outflow coverage) before signoff |
| 22:12Z | Andrew direct: "just run backfill right now" (override CTO clarifiers) |
| ~22:30Z | **SESSION CONTEXT INTERRUPTED.** Backfill never fired. Data gap. |

### 2026-04-20 23:00Z → 2026-04-21 ~04:20Z — Overnight failures

| Time | Event |
|---|---|
| 2026-04-20T23:00:14Z | `bd-gold-nightly-fallback` EventBridge fired. bd-gold-trigger Lambda cleanly started PROD i-01003b035d2988dfb. |
| 23:01:06Z | `/tmp/gold_logs/chain_full_20260420_230106.log` started |
| 23:13:54Z | **B_00 canonical_holdings crashed** with `NameError: name 'defaultdict' is not defined` at L456. Latent bug in DS commit `081223b5` (BFIX1 bd_stale predicate tightening) — `defaultdict(set)` added at L428 without `from collections import defaultdict`. Code path only reached when schwab_cache non-empty; local dryrun missed it. |
| 23:20:58Z | B_01 completed (reads positions_cube directly, doesn't need B_00 output). Chain aborted after — C-tier needs canonical_holdings.parquet which B_00 never wrote. |
| 23:21Z-ish | Runner self-shutdown via --chain full's auto-shutdown path (log writer stopped, instance stopped) |
| 2026-04-21T04:00:14Z | `bd-canonical-prices-daily` EventBridge fired. PROD started again. |
| 04:01:06Z | `chain_full_20260421_040106.log` started |
| 04:13:51Z | **Identical B_00 NameError.** Chain aborted at same point. |
| 04:20:52Z | B_01 done, chain ended |

**Net impact:** Portal data frozen since 2026-04-20 22:25Z (yesterday's QA `--group D` completion). No C-tier or D-tier ran overnight. Two identical back-to-back failures.

### 2026-04-21 morning — Recovery sequence

| Time | Event |
|---|---|
| ~12:10Z | Andrew resumed session, asked "what happened last night, why no new data" |
| 12:14Z | RCA delivered. Bug confirmed in committed source (B_00.canonical_holdings.py L428 has `defaultdict(set)` but no import). Two identical EventBridge fires, same failure. |
| 12:16Z | DS commit `1a54d46a` — 1-line import fix `from collections import defaultdict` |
| 12:18Z | AE uploaded B_00 `1a54d46a` via `git show 1a54d46a:...` pattern. S3 ETag `79e9d306e893e49cbe8d1851d1ca45de`, 51,243 B. comp-pipescript deployed B_00 MATCH. |
| 12:45Z | DT uploaded B_01 `5f5d0319` (HLOT2 Patch A + Patch B dual-patch). ETag `fd1531fec074cf7eb1225646560f2edd`. comp-pipescript deployed B_00 + B_01 both MATCH. |
| 13:37Z | Andrew GO "deploy from B_00 through full chain". AE fired `--chain full --bg --no-shutdown` on QA c6a.8xlarge. SSM `cf5bd5ad-e6d6-45dc-902d-584ccced2c09`. **Scope wider than CTO's APPROVE OPTION 1 (chain bcd)** — self-flagged to CTO + Andrew. |
| 13:40Z | Andrew: "hold on, schwab files need converting first." AE killed chain full mid silver-prep. |
| 13:41Z | `sync_schwab_onedrive_to_s3.py --upload` → 25 files uploaded to `s3://opal-data-schwab/01_raw/` + 2 RPS mirror to `bronze/rps/`. New dates: 2026-04-17 + 2026-04-20 |
| 13:42-13:44Z | 4 silver converters executed sequentially: |
| | - RPS: 2 new dates (569 total partitions) |
| | - ACC: 2 new dates (568 total) |
| | - TRN: 2 new dates (568 total) |
| | - ULN: 2 new dates (352 total, range 2024-01-12 → 2026-04-20) |
| 13:45Z | Andrew GO: "backfill first." AE fired D_02 `--backfill-role-aua` via nohup through SSM `769ba103`. D_02 PID 2318. |
| 13:49Z | Step 1b shadow write in progress — 2,297 historical partitions (2020-01-02 onward) being rewritten with corrected `n_roles_per_pair` denominator (from 6f724293) |
| 13:59:33Z | D_02 backfill complete. Wall 862.6s (14m23s). mem_peak 10.2 GB. Total AUA $1,651,446,371 (matches yesterday's FIX7 expected). |
| 14:03Z | Andrew: "stop instance." AE stop-instances. Both runners stopped. |

**Current state:** awaiting Andrew's explicit GO to fire `gold_dispatch.sh --chain full --bg --no-shutdown`.

---

## Commits this session

| SHA | Author | Description |
|---|---|---|
| `9139086d` | 0.6.0_AE_PartnerETL | fix(watchdog): widen regex to match manual-SSM gold dispatch paths |
| `9a700351` | 0.6.0_AE_PartnerETL | docs(RCA): watchdog mid-D_02 shutdown post-mortem + structural fix recommendation |
| `d9a419aa` | 0.6.0_AE_PartnerETL | docs(RCA): append Q3 PROD addendum + post-fix validation receipts |
| `d13b11d5` | 0.6.0_AE_PartnerETL | feat(gold_dispatch): add --from <id> for partial-group resumption |
| `1a54d46a` | 0.4.0_DS_ClientPlatform~A | fix(B_00): add missing `from collections import defaultdict` (081223b5 follow-up) — deployed by AE |

AE also:
- Uploaded `gold_dispatch.sh` (d13b11d5) to `s3://opal-data-bd/code/gold/` at 2026-04-20T20:16:53Z
- Uploaded `watchdog-shutdown.sh` (9139086d) to `s3://opal-data-bd/code/runner/` at 2026-04-20T17:19:35Z
- Uploaded `B_00.canonical_holdings.py` (1a54d46a) to `s3://opal-data-bd/code/gold/` at 2026-04-21T12:18:04Z
- Live-patched QA + PROD watchdog scripts (EBS root) on 2026-04-20 via SSM
- Disabled `bd-gold-nightly-fallback` EventBridge rule at 21:41Z, DT re-enabled at 21:42Z (re-enabled by DT without AE coordination — lane-crossing, self-flagged)

---

## EC2 state (end of session)

| Instance | Name | State | Type | Note |
|---|---|---|---|---|
| i-0090b823a4a0997e3 | bd-gold-qa-runner | stopped | **c6a.8xlarge** | Downsized from c6a.16xlarge on 20260420T20:40Z due to capacity block. D_04 peak 14.4 GB fits. To revert to c6a.16xlarge once capacity returns. |
| i-01003b035d2988dfb | bd-gold-layer-runner | stopped | c6i.16xlarge | PROD. Both overnight EventBridge fires aborted at B_00; self-shutdown worked. |

**EventBridge rules:**
| Rule | State | Schedule |
|---|---|---|
| bd-gold-nightly-fallback | ENABLED | `cron(0 23 ? * MON-SAT *)` — fires 23:00 UTC tonight |
| bd-canonical-prices-daily | ENABLED | `cron(0 4 * * ? *)` — fires 04:00 UTC tomorrow |
| bd-gold-layer-monthly-trigger | DISABLED | — |

If chain full is NOT fired before 23:00 UTC, tonight's nightly will pick up all fixes (B_00 1a54d46a, B_01 5f5d0319 HLOT2, D_00 4299e1c0, D_02 048af6a3, D_04 8593ea51) + corrected historical role_aua from today's backfill and run `--chain full --incremental` against PROD.

---

## S3 state on deployed scripts

| Script | Commit | S3 key | Last upload |
|---|---|---|---|
| B_00.canonical_holdings.py | 1a54d46a | code/gold/B_00.canonical_holdings.py | 2026-04-21T12:18Z (AE) |
| B_01.holdings_lots.py | 5f5d0319 | code/gold/B_01.holdings_lots.py | 2026-04-21T12:45Z (DT) |
| D_00.portal_aggregates.py | 4299e1c0 | code/gold/D_00.portal_aggregates.py | 2026-04-20 (DT) |
| D_00b.portal_timeseries.py | e0550693 | code/gold/D_00b.portal_timeseries.py | 2026-04-20 (DT) |
| D_00c.portal_leaderboard.py | c25afc6c | code/gold/D_00c.portal_leaderboard.py | 2026-04-20 (DT) |
| D_02.advisor_client_detail.py | 048af6a3 | code/gold/D_02.advisor_client_detail.py | 2026-04-20T20:58Z (DT) |
| D_04.client_portal_summary.py | 8593ea51 | code/gold/D_04.client_portal_summary.py | 2026-04-20 (DT) |
| gold_dispatch.sh | d13b11d5 | code/gold/gold_dispatch.sh | 2026-04-20T20:16Z (AE) |
| watchdog-shutdown.sh | 9139086d | code/runner/watchdog-shutdown.sh | 2026-04-20T17:19Z (AE) |

All scripts `comp-pipescript deployed` MATCH as of 2026-04-21T12:20Z check.

---

## Schwab silver state (end of session)

| Table | Partitions | Latest date |
|---|---|---|
| silver/RPS | 569 | 2026-04-20 |
| silver/ACC | 568 | 2026-04-20 |
| silver/TRN | 568 | 2026-04-20 |
| silver/ULN | 352 | 2026-04-20 (range 2024-01-12 onward) |

**Latest BD silver dates (via prior observation):** 2026-04-17 (typical T-1 from Friday close).

---

## Compiler Tools

| Phase | Tool | Run | Result |
|---|---|---|---|
| Pre-dispatch (today) | comp-pipescript | `deployed B_00 B_01 D_00 D_02 D_04` | All MATCH on 1a54d46a + 5f5d0319 + 4299e1c0 + 048af6a3 + 8593ea51 |
| Pre-dispatch (yesterday) | comp-pipescript | `deployed D_00 D_02 D_04` at 22:10Z | All MATCH (triple-checked before backfill pre-flag to CTO) |
| Pre-dispatch (yesterday) | comp-pipescript | `deployed B_00 B_01` at 12:20Z (today) | Both MATCH after deploys |
| RCA forensics | `pgrep -f "$WATCHDOG_REGEX"` | sim-test against killed dispatch | Proved regex widening from `run_gold_layer|gold_rebuild|build_gold` → `...|gold_dispatch|gold_prof|gold_layer_scripts/` catches manual-SSM path |
| PROD live-patch verification | `md5sum watchdog-shutdown.sh` | pre `3520122f…` vs post `f3a20c83…` | Confirms live-replace succeeded on PROD root EBS |
| RCA date forensics | CloudWatch metric `AWS/Events Invocations` | bd-gold-nightly-fallback + bd-canonical-prices-daily at overnight timestamps | Both rules fired exactly once; confirmed via `get-metric-statistics` |

Skipped today:
- `comp-blast` — no repo-graph touches beyond gold_dispatch.sh + watchdog + B_00 import
- `comp-iam gaps` — no iam.tf changes
- `comp-pipescript postdeps` — all dispatches were `--chain full` or group-scope, auto-sequenced

---

## Current State

- AE lane: idle, **awaiting Andrew GO on chain full**
- Both runners stopped
- All gold scripts on S3 match CLOUD HEAD
- Schwab silver fresh through 2026-04-20
- Historical role_aua backfill complete (2,297 partitions, corrected denominator)
- No blockers
- Portal data last written 2026-04-20T22:25Z (yesterday's QA `--group D` — pre-HLOT2, pre-B_00-fix)

## Next Steps

1. **[Andrew]** Explicit GO on chain full → **[0.6.0_AE]** fire `--chain full --bg --no-shutdown` on QA c6a.8xlarge. ETA ~2h wall. Bundles B_00 1a54d46a + B_01 5f5d0319 HLOT2 + all A/B/C/D fixes with fresh Schwab silver + corrected historical role_aua.
   - If not fired manually, tonight's 23:00 UTC `bd-gold-nightly-fallback` catches it on PROD with `--chain full --incremental`.
2. **[0.4.0_DT]** Run extended comparison pack on completion artifacts per CTO's HLOT2 attribution plan (DIVZ ~$78.6M Patch A, IEFA/SPYM/IDVZ/IEMG/SPHY Patch B Tier 1, ~25 accts Tier 2, BFIX1/2 cohort sizing, firm total_aua unchanged $1.649B).
3. **[1.0.0_CTO + 2.0.0_COO]** Dual RAVC4 close on HLOT2 + BFIX1+2 based on attribution-split evidence from (2).
4. **[0.4.2_RD]** Validate 5-invariant close: Firm Overview 5 new fields populated + Travis historical Lifetime Activity bars correct (backfill contribution).
5. **[0.6.0_AE]** Post-chain: revert QA c6a.8xlarge → c6a.16xlarge once capacity returns (not urgent — 8xlarge handled D_04 at 14.4 GB peak with 4x headroom).
6. **[0.6.0_AE carry-forward]** Q4 coverage test (`scripts/test_watchdog_regex_coverage.sh`) + Q6 process-tagging follow-on TO drafts — queued per CTO's prior GO.
7. **[Process gap]** Two latent-bug-on-ad-hoc-commit incidents in 48h (D_02 035352c3 KeyError + B_00 081223b5 NameError). CTO flagged pre-commit import/lint discipline gap to raise with DS separately — not blocking.

## Pending (carried from prior sessions)

- CP-DS1 Gate 1 signal — COO re-authorization of `backfill --all` + EC2 deploy of `merge-daily-incremental.py` still pending (from 2026-04-17)
- SL-AE1 email draft — on COO hold pending review (commit 00760f48)
- Schwab-bucket-access TF drift — iam.tf import deferred pending CTO review
- silver/ULN converter commit — converter exists locally, committed + running successfully today, no new commit needed (verified OK per this session's run)
- ADVI_STAUDT.OPB — held pending DS~A BD ground-truth findings (CTO HOLD 2026-04-20T17:21Z; CTO absorbed INV1 findings into FIX6 shipped yesterday)

## Incidents / Lessons

1. **Two latent-bug-on-commit failures in 24h** (D_02 035352c3, B_00 081223b5). Both bugs were in code paths that local dryruns didn't exercise. Pattern: DS commits → DT uploads → first real run surfaces. Mitigation path: pre-commit import/lint + code-path execution test in CI. CTO raising with DS lane.

2. **COO/DT cross-lane EventBridge flip at 21:40-21:42Z** — lane discipline broke briefly. DT crossed into AE's EventBridge ownership to re-enable the rule under 80-min time pressure. Self-flagged, stood down. AE accepted; worth logging for lane protocol evolution.

3. **`--from <id>` validated in production same-day as shipping.** Yesterday's dispatch used it (CHAIN_LABEL `from:D_02` emitted correctly, resolution `D_02 D_03 D_04` matched design). First new gold_dispatch.sh CLI feature in weeks.

4. **c6a.8xlarge downsize worked cleanly.** Gold workload is memory-bound (14.4 GB D_04 peak) not CPU-bound (~5% avg), so 32 vCPU was as fast as 64. Saves ~50% compute cost for single-cycle tests. c6a.16xlarge remains steady-state due to `feedback_ec2_gold_runner_sizing` but 8xlarge is proven viable fallback when capacity is constrained.

5. **Watchdog widened regex end-to-end validated on both runners.** QA `b5ad3829` (5 consecutive SKIP: gold process is running during active D_02+), PROD `3e06059f` (survived full Group D run, self-reaped at idle). Addresses the latent gap flagged in RCA Q3 (PROD would have misfired on manual-SSM after the 2026-04-09 threshold drop from 30m → 10m but for pure luck).

6. **Schwab OneDrive ingest was AE-owned recurring task per README.** Session confirmed the flow (sync → 4 converters) completes in ~2:30 for 2 new dates across 4 tables. ACC duplicate-column edge case (state x3) still patched via convert_schwab_acc_to_parquet.py (commit f41b37f5). No changes needed.

---

## Closeout state

No formal RAVC closeout this session — chain full dispatch is still pending Andrew's GO. Backfill and Schwab sync were prerequisite ops with no external RAVC counterparty (AE-owned).

Session log commit pending.
