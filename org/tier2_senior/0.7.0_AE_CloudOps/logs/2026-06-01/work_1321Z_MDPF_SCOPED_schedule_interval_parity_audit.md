# MDPF_SCOPED P1 — AE leg: Schedule / Interval-Parity Audit (Model Portfolios: GLOBAL / 49 / INFLECTION)

**Agent:** 0.7.0_AE_CloudOps · **Cycle:** /work tick 2026-06-01 ~1321Z · **Project:** MDPF_SCOPED Phase 1 maturation
**Dispatch:** 2.0.0_SA_COO [DRIVE] (Andrew-direct FIRST priority) + [SYNC] (DE-flagged orphan-artifact fold-in)
**Verification posture:** AWS ground-truth (EventBridge / S3 / runner telemetry + logs), not repo-read alone.

---

## TL;DR (verdict)

- **Cron / schedule level: NO interval mismatch.** All three segments are served by ONE unified daily job — EventBridge rule `mdpf-daily-refresh-trigger`, `cron(0 15 ? * MON-FRI *)` (15:00 UTC, weekdays), **ENABLED**. The deployed aggregator is current (`v0_9_1`, inflection-aware). The scheduled chain demonstrably produces all-3-segment output with `reconciliation=PASS`.
- **Effective-freshness level: SEVERE mismatch in the CURRENT serving state.** The INFLECTION segment is **null on the latest date (2026-05-29) and on 4 of the last 5 daily dates**, while 49 Financial is populated every date. Root cause is **NOT scheduling** — an **out-of-band rebuild with stale `v0_8_ruling2` code (~19:26 UTC on 2026-05-29) overwrote the chain's correct multi-partner output**, stripping inflection out of the latest partitions + both timeseries.
- **Fix is therefore NOT a schedule change.** It is: (1) re-emit the affected dates with the current chain to restore inflection to latest serving state; (2) find + eliminate the rogue out-of-band stale-code rebuild; (3) add a methodology-version monotonic write-guard so an older artifact can never overwrite a newer one.
- **Orphan artifacts:** the 2 DE-flagged `json/mdpf/...` keys are NOT dead — they are written daily by the chain's ROLLUP dual-write. One of them (`json/mdpf/global/aggregate-aua-timeseries.json`) is a **perfectly-named GLOBAL segment feed that the FE reportedly does not read** — itself a likely unwired-Global FE↔BE gap to reconcile with DE/RD.

---

## 1. SCHEDULE MATRIX (per segment)

| Segment | Refresh job | Cadence | Last SCHEDULED run | Next run | Effective freshness in CURRENT serving artifacts |
|---|---|---|---|---|---|
| **GLOBAL** (aggregate 1a+1b+1c+2a) | `mdpf-daily-refresh-trigger` → `mdpf-daily-trigger` Lambda → EC2 `mdpf-daily-runner` → 5-stage chain (WS-A aggregate) | `cron(0 15 ? * MON-FRI *)` = 15:00 UTC weekdays | 2026-05-29 15:04 UTC (CHAIN complete, partners=2, **PASS**) | 2026-06-01 15:00 UTC (today, ~1.5h out) | **CLOBBERED** — latest partition (5/29) reflects 49F-only after the 19:26 UTC out-of-band rewrite |
| **49 FINANCIAL** | Same unified chain (WS-B SmartX model + WS-E non-model residual) | Same (15:00 UTC weekdays) | Same run | Same | **OK / daily** — 49F is the only partner surviving in the latest serving state |
| **INFLECTION** | Same unified chain (WS-C Eclipse/Orion feeder; WS-A includes it on/after onboard 2026-05-18) | Same (15:00 UTC weekdays) | Same run — WS-C ran clean 5/29 (model_aua $96.6M, 405 rows; WS-A partners=2 PASS) | Same | **STALE** — null on 5/29 (latest) and on 5/22/25/26/27; last surviving value 2026-05-28 |

**Upstream feeders (all settle BEFORE the 15:00 UTC chain — no upstream interval gap):**
- SmartX REST JWT refresh `cron(0 9 * * ? *)` (09:00 ET) + REST pull `cron(15 9 * * ? *)` (09:15 ET) — feeds 49F.
- Inflection bronze `cron(43 12 * * ? *)` (12:43 UTC) + gold fallback `cron(0 14 * * ? *)` (14:00 UTC) — feeds inflection.

---

## 2. EVIDENCE TRAIL

1. **EventBridge rule** `mdpf-daily-refresh-trigger`: `ScheduleExpression cron(0 15 ? * MON-FRI *)`, `State ENABLED`, target Lambda `mdpf-daily-trigger`, DLQ wired. **Only ONE** mdpf EventBridge rule exists (confirmed `aws events list-rules`).
2. **Runner telemetry** `s3://opal-data-mdpf/telemetry/mdpf-daily-runner/status.json`: last run `mdpf_daily_20260529_150030`, status `complete`, 0 errors, weekend gap (5/30–5/31) expected for MON-FRI cron.
3. **Deployed aggregator** `s3://opal-data-mdpf/code/scripts/gold/mdpf_aggregate_aua.py` (deployed 2026-05-26 17:57): `METHODOLOGY_VERSION = "v0_9_1"`, `expected_partners = {"49financial","inflection"}`, `INFLECTION_PARTNER_ONBOARD_DATE = "2026-05-18"`. **NOT stale.**
4. **Scheduled-chain log** `logs/mdpf_daily_20260529_150030.log`:
   - WS-C inflection feeder OK (model_aua_positions/inflection/2026-05-29.parquet, 405 rows).
   - WS-A line 3022: `opal_aggregate_aua=1,783,772,321.21 ... partners=2 reconciliation=PASS`; line 3025 wrote `platinum/mdpf/aggregate_aua/2026-05-29.json`. Chain complete 15:04:02 UTC.
5. **Current latest partition** `platinum/mdpf/aggregate_aua/2026-05-29.json`: `generated_at 2026-05-29T19:26:04Z` (4h22m AFTER the chain), `methodology_version v0_8_ruling2`, partners `[49financial]` ONLY, `reconciliation NOT_APPLICABLE_HISTORICAL`, `opal_aggregate_aua 1,847,968,516.41`.
6. **Cross-partition pattern** (partners present): 5/21 `[49financial, inflection]` v0_9 PASS · 5/22 `[49financial]` v0_8_ruling2 · 5/28 `[49financial, inflection]` v0_9_1 PASS · 5/29 `[49financial]` v0_8_ruling2. The two inflection-bearing dates (5/21, 5/28) were written ~11:03 ET and ESCAPED the rewrite; the v0_8_ruling2 dates were rewritten in the 5/29 19:26 UTC bulk pass.
7. **Timeseries** `platinum/mdpf/aggregate_aua_timeseries.json` + `json/mdpf/inflection/aggregate-aua-timeseries.json`: `as_of_last 2026-05-29` (fresh file timestamp) but inflection `model_aua` tail = `[None, None, None, None, 96211989.78, None]` over dates `[5/22,5/25,5/26,5/27,5/28,5/29]` — **fresh file, stale content**. Inflection FE view would show a null latest day.

**`v0_8_ruling2` is not a version string in the current `v0_9_1` code** → the clobbering writer ran an OLD code checkout. Not the EventBridge chain (only one rule; deployed code is v0_9_1; chain produced PASS partners=2).

---

## 3. ROOT CAUSE

An **out-of-band, non-scheduled rebuild** ran ~2026-05-29 19:26 UTC using a **stale `v0_8_ruling2` aggregator checkout** and rewrote a large set of `platinum/mdpf/aggregate_aua/{date}.json` partitions plus both the platinum and `json/mdpf/` timeseries — overwriting the scheduled chain's correct `v0_9_1` multi-partner (PASS) output and stripping inflection from the latest serving state. Source is most likely a manual SSM/local run by a session with an old checkout, or a stray task on a non-runner host (no second EventBridge rule). Requires CloudTrail `PutObject` attribution on the affected keys to pin the principal — AE-domain forensic.

---

## 4. ORPHAN-ARTIFACT DISPOSITION (DE-flagged)

`json/mdpf/` prefix, all rewritten 2026-05-29 15:38 by the chain ROLLUP (`build_aggregate_aua_timeseries.py` dual-write, commits `44afa1dd2` + `6b21c8cf4`):
- `json/mdpf/49financial/aggregate-aua-timeseries.json` (live 49F segment feed)
- `json/mdpf/inflection/aggregate-aua-timeseries.json` (live inflection segment feed — but stale content per §2.7)
- `json/mdpf/global/aggregate-aua-timeseries.json` ← **DE-flagged not-referenced**
- `json/mdpf/aggregate-aua-timeseries.json` (unscoped combined) ← **DE-flagged not-referenced**

**Disposition:** Both flagged keys ARE refreshed daily — they are NOT dead orphans, so "wasting compute" is real but trivial (rollup ~50s; negligible cost). The more important read: `json/mdpf/global/` is a *correctly named GLOBAL segment feed that the FE reportedly does not consume*. That is a candidate **unwired-Global FE↔BE linkage gap**, not merely a decommission target. Recommendation:
1. Reconcile against DE's FE-read matrix: does ModelPortfolios.tsx serve "Global" from `json/mdpf/global/`, from the unscoped combined, from platinum, or compute it client-side from 49F+inflection? If Global is meant to read `json/mdpf/global/` and doesn't → **wire it** (RD/DE).
2. Only if Global is confirmed sourced elsewhere → deprecate-then-remove the dual-write of the 2 unreferenced keys from `build_aggregate_aua_timeseries.py` (DS-owned code change). Do NOT delete S3 objects pre-confirmation.
Priority: LOW relative to the inflection clobber.

---

## 5. REMEDIATION RECOMMENDATION (owner-routed)

1. **RESTORE (immediate, content):** re-run the current `v0_9_1` chain (or WS-A + ROLLUP) for the clobbered dates to regenerate multi-partner partitions + timeseries and restore inflection to the latest serving state. Owner: DS/DE run the script; AE can dispatch via `mdpf-daily-runner` SSM. *(Today's 15:00 UTC scheduled run will itself re-emit 6/1 correctly — but historical 5/22/25/26/27/29 stay clobbered until a backfill.)*
2. **PREVENT (root cause):** CloudTrail-attribute the 19:26 UTC 5/29 `PutObject`s on `platinum/mdpf/aggregate_aua/*` to identify + eliminate the rogue stale-code rebuild path. Owner: AE (CloudOps forensic) + flag the offending session.
3. **GUARD (structural):** add a **methodology-version monotonic write-guard** to the aggregate/rollup write path — refuse to overwrite an artifact whose existing `methodology_version` is newer than the writer's. And/or restrict `s3:PutObject` on `platinum/mdpf/aggregate_aua/*` to the runner instance role only (comp-iam). Owner: DS (write-guard in script) + AE (IAM). This is the durable fix for the *class* (out-of-band stale-code clobber), independent of schedule.

**Net for Andrew's question** ("are all three scheduled on comparable intervals?"): YES at the schedule level (one unified daily chain, all three, current code, reconciliation PASS) — but the latest *visible* data is wrong for inflection/global because a stale-code out-of-band rebuild clobbered it. The corrective is data re-emit + a write-guard, not a new/changed schedule.

---

## 5b. FORENSIC ADDENDUM (work-cycle 0002, ~1343Z) — attribution of the 19:26Z clobber

Pre-authorized read-only forensic on the §3 out-of-band rebuild, to determine if retroactive principal-attribution is possible:

1. **Runner telemetry history** `s3://opal-data-mdpf/telemetry/mdpf-daily-runner/history/`: the ONLY 5/29 record is `mdpf_daily_20260529_150030.json` (the scheduled 15:00 run). **No out-of-band run is recorded** → the 19:26Z clobber did NOT execute via `mdpf-daily-runner`. It was a **manual/external run** (workstation/agent session running an old `v0_8_ruling2` checkout directly against S3).
2. **CloudTrail** `lookup-events EventName=PutObject` for the 19:00–20:00Z 5/29 window: **empty**. S3 object-level PutObject is a *data event*, not captured by the default management-event trail.
3. **S3 server access logging** on `opal-data-portal-v2` (`get-bucket-logging`): **not configured** — empty.

**Attribution verdict: the clobber is NOT retroactively attributable** — neither CloudTrail data events nor S3 access logging is enabled on the bucket. Therefore the remediation MUST be **preventive/structural, not investigative**:
- The §5.3 **IAM write-lock** (restrict `s3:PutObject` on `platinum/mdpf/aggregate_aua/*` to the `mdpf_runner` instance role only — `infra/aws/terraform/mdpf-pipeline/ec2.tf:34` `aws_iam_instance_profile.mdpf_runner`) would have **structurally blocked this manual clobber**. This is now the highest-leverage fix.
- The §5.3 **methodology-monotonic write-guard** is the second layer (defends even a runner-role write that regresses methodology).
- **Going-forward attribution:** enable S3 server access logging (or a CloudTrail S3 data-event selector) on `opal-data-portal-v2 platinum/mdpf/*` so the next anomaly IS attributable. Low cost, AE-domain.

All three are infra changes → Terraform (Rule 1) + safe-apply (Rule 18); pending COO leg-ownership confirmation before authoring.

## 5c. ROOT-CAUSE CONFIRMED + RESTORE-INCOMPLETE CATCH (work-cycle 0003, ~1333Z, post RAVC2-ACCEPT)

**Authoritative root-cause (code-inspection — CloudTrail dark):** the rogue clobberer is `data/mdpf/scripts/backfill/build_mdpf_process_backfill.py`:
- L118 `METHODOLOGY_VERSION = "v0_8_ruling2"`; L120 `PARTNER = "49financial"` (hardcoded, 49F-only); L80 `PLATINUM_PREFIX = "platinum/mdpf/aggregate_aua"`; L524 reconciliation `"NOT_APPLICABLE_HISTORICAL"` — **exact signature match** to the 5/29 19:26Z clobbered partitions.
- L618 self-documented rule "NEVER write a date >= INFLECTION_PARTNER_ONBOARD_DATE" was **comment-only, not code-enforced** → it clobbered post-onboard dates (5/18–5/29). Reconciles AE's "stale v0_8_ruling2 code" + DS~B's "49F-only backfiller" = the same script. DS~B shipped a narrow onboard-date enforcement (`a9352506f`).

**Restore status (verified):** DS~B re-emitted the daily PARTITIONS via canonical `v0_9_1` local `--upload` — 8 dates (5/18,19,20,22,25,26,27,29) now both-partners, gen `2026-06-01T13:22Z`, confirmed. 5/21 + 5/28 were never clobbered (own-date 15:03Z originals).

**INCOMPLETE-RESTORE CATCH (verify-channel):** partition re-emit ≠ serving-artifact fix. The ROLLUP was NOT re-run — `platinum/mdpf/aggregate_aua_timeseries.json` + `json/mdpf/{inflection,global,49financial}/aggregate-aua-timeseries.json` all still `meta.generated_at=2026-05-29T19:38:07Z` (built from the clobbered partitions); inflection `model_aua` tail still `[None,None,None,None,96211989.78,None]` over `[5/22,25,26,27,28,29]`. The FE inflection/global TREND feed remains stale until the ROLLUP (`build_aggregate_aua_timeseries.py`) re-runs against the restored partitions. Coordinated to DS~B (their Rule-13 script-run); today's 15:00 UTC scheduled chain self-heals it otherwise, but Andrew-priority → re-run now.

**GUARD SPLIT (final, no overlap):** (i) DS~B keeps `a9352506f` onboard-date guard (path-scoped; catches new post-onboard dates with no prior partition to compare); (ii) version-monotonic write-guard in the shared emit helper = DS~B script-side leg; (iii) `s3:PutObject` restriction to the `mdpf_runner` role on `platinum/mdpf/aggregate_aua/*` = AE IAM/Terraform leg (closes the local `--upload` path the clobber + the restore both used).

## 6. SPLIT NOTE

0.5.0_AE not yet registered LIVE at audit time → completed solo. When it comes up, suggested split: 0.5.0_AE takes remediation-impl legs (CloudTrail attribution §5.2 + IAM write-restriction §5.3); 0.7.0_AE_CloudOps retains this audit + the write-guard coordination. All infra changes via Terraform (Rule 1) + safe-apply (Rule 18).
