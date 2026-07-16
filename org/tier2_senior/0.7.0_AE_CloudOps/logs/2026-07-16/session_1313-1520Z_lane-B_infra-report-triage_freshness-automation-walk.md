# 0.7.0_AE_CloudOps~B -- Andrew-direct infra-report triage: severity INVERSION named, 6 instrument defects grounded, AI-triage layer falsified 3/3

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, TRACE, VALIDATE, SCRIBE
**serial:** 0.7.0_AE_CloudOps~B (lane ~B; base folder) | **date:** 2026-07-16 | **window:** ~13:13Z (session start + Andrew-direct commission) -> ~15:20Z (ONGOING -- live session with Andrew)

## Summary

1. **ANDREW-DIRECT COMMISSION (recorded VERBATIM + broadcast same turn, per XXX.md).** Line-by-line triage
   of the daily OPAL INFRASTRUCTURE REPORT -- "noise vs real" -- because it is "just blaring red alert every
   day". Deliverable = BOTH the reporting-system FIX and the foundation for a NEW **SCTY** project "patching
   the holes". Method Andrew-set: line by line, in-session. Brief opened + committed `04a1dca43`
   (`docs/briefs/infra-report-noise-vs-real-triage-20260716.md`); broadcast to CTO+COO+MSTR.
2. **THESIS (proven, not asserted): the report's severity is INVERTED** -- loud on the safe, quiet on the
   broken. It RENDERS RED on known/deliberate/already-fixed state while rating actual dead controls WATCH.
   Root mechanism found in prior art: `docs/briefs/infra-report-revamp-proposal-20260616.md` (CVO) LARGELY
   SHIPPED its **ADD** half (freshness/drift/graph/contracts/cost-depth/re-homed-AI) and **NOT its TRIAGE
   half** ("new-vs-chronic", "suppress the chronic-accepted baseline", "a RED-only interrupt ... alert on
   state-changes"). The report therefore went from counts-of-everything to ALARMS-for-everything. **That
   omission IS the alert-fatigue mechanism.**
3. **D-2, the load-bearing defect: THE FRESHNESS MANIFEST HAS NO INVOKER.** `.tools/freshness_manifest_gen.py`
   is a hand-run repo tool. DESIRED: commit `1591d9ef8` = 2026-06-17 14:45Z (its build day). APPLIED:
   `s3://opal-data-portal-v2/infrastructure/freshness_manifest.json` LastModified **2026-06-17 10:48:12**,
   `generated_at 2026-06-17T14:47:36Z`, 77 served_artifacts (denominator matches the report's 32+31+8+1+3+1+1
   exactly -> the whole section renders off this frozen set). `comp-grep` denominator: **20 refs repo-wide,
   ZERO crons/CI/TF/scheduler**. Architecture: the generator emits the artifact SET+cadence+thresholds; the
   Lambda head-objects at runtime -> **AGES ARE LIVE, SET+THRESHOLDS FROZEN 29 DAYS.** Rated WATCH *under an
   OVERALL: RED* -- the instrument rated its own blindness BELOW the readings taken while blind.
4. **FRESHNESS WALK COMPLETE (18 flagged lines): 4 CONFIRMED FALSE, 3 REAL, 2 real-and-known, 2 correct,
   7 resolved-to-noise.** The INF RED block is retired-path noise with a dated paper trail (below). The cot
   "missing/unreadable" x3 is an **IAM boundary rendered as missing data**. `model-portfolios 0/3` is REAL.
5. **THE AI TRIAGE LAYER FALSIFIED 3/3 -- it is the report's single largest noise source, and it ANTI-triages.**
   It restored the FORM of actionability without the SUBSTANCE: confident, specific, well-formatted root
   causes that are wrong. Worse than the bare counts it replaced -- bare counts don't help but don't lie about
   causation; a confident wrong root cause dispatches someone to fix the wrong thing.
6. **SCTY SEED IDENTIFIED:** the report's quietest lines are its realest holes -- 5 INERT never-widen tripwires
   naming 0 live IAM role (CANNOT FIRE; a NEVER-rule surface), 2 UNCONTRACTED SEV1 surfaces, a NO-OP
   comp-surface-check rendered `[OK]`, 33% of TF unassessable, and 10 SNS topics paging NOBODY.

## Grounded findings (each source- or live-confirmed; INFERRED marked)

| # | Finding | Verdict | Grounding |
|---|---|---|---|
| D-1 | Header stamps "13:03 ET"; true 13:13Z = 09:13 ET | INSTRUMENT | live `aws scheduler get-schedule infrastructure-monitor-daily` -> `cron(0 13 ? * MON-FRI *)`, **no `ScheduleExpressionTimezone`** = UTC. Emits UTC labeled ET; violates CLAUDE.md quick-ref (times to Andrew = ET, never UTC) |
| D-2 | Freshness manifest has NO invoker; frozen 29d | INSTRUMENT | desired (commit 1591d9ef8 2026-06-17) + applied (S3 LastModified 2026-06-17 10:48:12) + comp-grep denominator 20 refs / 0 callers |
| D-3 | ~25 `[standing]` vs exactly **1** `[NEW]` drift finding, rolled up identically | INSTRUMENT | the discriminator EXISTS in the data; the rollup ignores it. Today's only [NEW] = `shared-infra aws_s3_bucket_lifecycle_configuration.global_graph` |
| D-4 | Self-contradiction x2 in ONE document | INSTRUMENT | SMARTX served "Overall OK 1.5h" vs AI "investor-facing data is stale"; SECURITY "TREND vs 07-15: HIGH +2" vs AI briefing "No prior baseline available" |
| D-5 | AI names `schwab_runtime.py` for the **SmartX** pull | INSTRUMENT | `schwab_runtime.py:227` is REAL for opal-assets-silver-schwab -> correct there, **misattributed** to smartx-assets-daily-pull |
| F-1 | `inf_silver_accounts_dim` RED (1866.1h) | **NOISE - RETIRED** | SOURCE-CONFIRMED: `INF_D_00.portal_aggregates.py:57` + `INF_C_09.fee_status_audit.py:164` -- "**ADVI_INFREF P1 LEG-1 repoint (2026-06-30): silver/accounts_dim/ froze 04-29**". Consumers repointed 06-30. Manifest (06-17) predates the fix by 13d. COO drive_log_20260702T2332Z already called it "**dead accounts_dim**" |
| F-2 | `inf_orion_api_assets` WATCH (1702.6h) | **NOISE - SUPERSEDED** | watches `silver/api_dims/assets/` (frozen 2026-05-05); live successor `silver/assets_v2/2026-07-16.parquet` written **today 09:35:45** |
| F-3 | INF silver "stale" overall | **NOISE - INF IS HEALTHY** | live: `_silver_complete/2026-07-16/`, `transactions/2026-07-16.parquet`, `performance/2026-07-16.parquet`, `assets_v2/2026-07-16.parquet` ALL current |
| F-4 | cot `header_metrics` + `timeseries_chart` "missing/unreadable" | **FALSE** | both EXIST + FRESH (2026-07-15 22:06:28; 733B / 287,693B). **The monitor is IAM-DENIED on cot** -- 3-arm battery per Rule 22a: target `s3:GetObject` on `opal-data-cot/platinum/firm/header_metrics.json` = **implicitDeny**; 2 ISOLATED positive controls (`opal-data-portal-v2/...`, `opal-data-inf/...`) = **allowed**. Denial is by DESIGN (firm separation, CLAUDE.md #13). **The instrument renders "I am forbidden to look" as "the artifact is missing."** |
| F-5 | cot `employee_leaderboard` "missing" | **FALSE - WRONG KEY** | key absent; real file = `leaderboard.json` (fresh 07-15 22:06) |
| F-6 | `model-portfolios 0/3 fresh` | **REAL** | `benchmark_returns.json` + `model_portfolio_benchmarks.json` last written **2026-07-12 14:10:42** (Sunday). Calendar-resolved: `trading_days_behind(2026-07-10)=4`, `expected_last_trading_day=2026-07-16`. All 4 files in the prefix wrote at the same instant and stopped = **producer freeze 07-12**. CONVERGES with `model_portfolios.headline` = an UNCONTRACTED SEV1 surface (two sections, one story, never joined) |
| F-7 | `inf_silver_aum_snapshot` "missing" | **REAL** | prefix EMPTY; positive control proves the monitor CAN read `inf` -> "missing" is TRUE here |
| F-8 | `bd_silver_unrealized` 63.4h | **INSTRUMENT (INFERRED mechanism)** | 63.4h == the mtime of a **2026-07-09 partition BACKFILLED 07-13 21:40Z**; newest DATA = 2026-07-10. Prefix appears aged by newest-object-mtime -> **a backfill of an OLD partition resets the freshness clock with no new data = it can FALSE-CLEAN.** Aging code NOT yet read -> mechanism INFERRED per Rule 22 |
| A-1 | `access-anomaly-scanner` rated **LOW** / "metric misclassification" | **REAL + MIS-RATED (the SCTY headline)** | It is the **CloudTrail access-anomaly detector** ("Loaded 197 IAM roles, 6 IAM users / Fetched 3206 CloudTrail events (2h window) / No access anomalies"), `cron(0 * * * ? *)` **hourly ENABLED**. Errors 18/8/15 last 3d. Duration **Max = 60000.0ms pegged at the 60s timeout**, avg **38.0s -> 48.5s RISING**; successful runs ~28.8s. A timeout leaves NO traceback -> the AI saw only INFO and called it a misclassification. **Failure mode = silence; success mode = "No access anomalies" = also silence. Broken and clean are byte-identical** (verification law #5 instantiated). Cause (INFERRED): CloudTrail fetch scales with event volume -> scaling into its own timeout |
| A-2 | `opal-assets-silver-schwab` 37/65 "misconfigured trigger" | **FABRICATED + ALREADY FIXED** | The AI's claimed root cause (`refusing to silently no-op`) occurred **0 times** in the report's 24h window (it fired **twice, on 07-14** -- 2 days earlier, OUTSIDE the window). Real in-window errors = **7 timeouts at 600000ms**. The "misconfigured trigger" theory is false: `opal-assets-silver-schwab-sweep-daily` sends `Input: {"mode":"sweep"}` CORRECTLY. Errors/day: 07-14=**31**, 07-15=**68**, 07-16=**0**. Redeployed **2026-07-15 18:40:47Z** (was 10240MB using 2201MB -> now 3008MB). **Error-free ~18h at report time.** The report has no concept of "already fixed" |
| A-3 | `smartx-assets-daily-pull` CRITICAL | **KNOWN + fix landed pre-report** | the Scheduler default RetryPolicy (185 attempts/24h) was fixed by 0.7.0 base **05-06Z the same morning** (explicit retry_policy 2/3600s, smartx-pipeline-v1.6.0). AI recommends the fix 7h AFTER it landed. Also contradicted by the report's own SMARTX freshness "Overall OK 1.5h" |
| S-5 | `bd_silver_allocations` + its alarm | **REAL -> REFERRED (Andrew-routed)** | `bd-allocation-pipeline-trigger` cron(0 22 ? * MON-FRI) **ENABLED**, last output 07-12, Mon/Tue/Wed landed NOTHING (4 trading days behind). `bd-allocation-file-check-daily` cron(30 22) ENABLED -> `bd-allocation-file-checker` **alive, 1 invocation/day 07-13/14/15**. SNS `bd-allocation-file-missing` subscriptions = **`[]` EMPTY**. The estate built the exact right control for the exact failure occurring, and the last hop pages NOBODY. **checker->topic link NOT source-confirmed = INFERRED** |

**AI-TRIAGE LAYER: 3/3 FALSIFIED (A-1 A-2 A-3).** Shared mechanism: **no window discipline and no state model** --
it reads a log, finds *an* error, and explains it, without checking whether it is *the* error, *in* the window,
or *already fixed*. Verification law #3 verbatim: "a false premise gets answered ON and returns as corroboration."
**It reached OPPOSITE conclusions from IDENTICAL evidence in one document**: `bd-silver-merge` ("logs truncated,
no error -> **consistent with a timeout**" -> HIGH, CORRECT) vs `access-anomaly-scanner` ("no actual error ->
**metric misclassification**" -> LOW, WRONG). Same signature, opposite verdicts -> **its severity ratings carry
no information.**

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "where is the source for opal-infrastructure-monitor" | PARTIAL | **near-tie 1.50 x3** (comp-aws / comp-iam / pipescript) -- none answers "where is the source"; it correctly declined to guess and routed to `comp-grep`. GAP: no router cell for a plain source-location question |
| comp-grep | x5 (`opal-infrastructure-monitor`, `freshness_manifest_gen`, `accounts_dim`, `silver/accounts_dim`, `data/inf/scripts`) | PASS | the load-bearing tool this session. Surfaced the CVO prior-art brief, the 20-ref/0-caller denominator (D-2), and the ADVI_INFREF 06-30 repoint (F-1). Raw `grep -rn` over the repo **TIMED OUT at 120s**; comp-grep answered the same question in seconds -- Rule 21 earned its keep |
| lib/trading_calendar.py | `expected_last_trading_day` / `trading_days_behind` | PASS | NEVER#1 discharged BEFORE any staleness call. Frontier = 2026-07-16; Apr-29 artifacts = **53 trading days** behind (no calendar rescues them); model-portfolios 07-12 = **4** (REAL) |
| aws iam simulate-principal-policy | 3-arm battery on `opal-portal-lambda-role` | PASS (discriminating) | Rule 22a honored: **ONE `--resource-arns` per call**, both positive controls run as **SEPARATE isolated invocations**. target cot=implicitDeny, portal-v2=allowed, inf=allowed |
| aws primitives (live) | scheduler get-schedule; lambda get-function-configuration x5; get-policy; list-event-source-mappings; events describe-rule/list-targets/list-rules; s3 ls x12; sns list-topics/list-subscriptions-by-topic; cloudwatch get-metric-statistics x4; logs filter-log-events x5 | PASS | APPLIED truth for every claim (Rule 22a) -- never a config-read for a behavioral claim |
| safe-commit.sh | brief @ 04a1dca43 | PASS | surface-check OK (1 file, no critical surface); risk-reflex REFLEX CLEAN, denominator 1 file vs 1239 danger nodes (danger map itself **55.2h STALE** -- noted, not load-bearing here) |

**What worked:** grounding EVERY report claim on the live primitive instead of arguing with the document --
each of the 4 "FALSE" verdicts came from one `aws s3 ls` the report's author never ran. The 3-arm IAM battery
(isolated positives) turned "missing/unreadable" from an ambiguity into a proven IAM boundary. Resolving the
trading calendar FIRST (NEVER#1) kept me off the reverse error and made `model-portfolios` REAL rather than
hand-waved.

**What failed (mine, caught in-flight):** my first CloudWatch query used `--filter-pattern '[ERROR]'` --
CloudWatch parses `[...]` as a **bracket pattern**, not a literal, so it matched `START`/`END`/`REPORT` lines
and would have inflated the count. Caught because the returned lines did not look like errors; re-run with a
quoted literal. **Same class as the `grep -c` trap in CLAUDE.md Git section: put the control on the RETRIEVAL,
not the pattern.** Also: my "bd producers have no scheduler" hypothesis was **WRONG** -- `bd-allocation-pipeline-trigger`
is ENABLED; the live check killed the hypothesis and made the finding REAL rather than excusable.

**Gaps found:** (1) `comp-which` has no cell for "where is the source of X" (near-tie -> fallback; the fallback
worked). (2) **The freshness manifest generator has no invoker** -- a producer nothing runs (D-2); the fix is a
scheduler/CI leg, and it is MY lane's own artifact (`freshness_manifest_gen.py:5` names `0.7.0_AE_CloudOps~B` as
the renderer; the base authored 1591d9ef8). (3) The monitor's `opal-portal-lambda-role` cannot read `opal-data-cot`
by design, and the report has no vocabulary to say so.

## MCP traffic

~4 in / ~4 out. **Out:** Andrew-direct record+broadcast to CTO + COO + MSTR (verbatim, scope surfaced-not-
adjudicated); REFERRAL to `0.7.0_AE_CloudOps` base of the bd-allocations chain (Andrew-routed passive-care under
the 49 refactor). **In:** COO ACK (folded; **elevated the AMEND-62 kill-switch-alarm finding to CTO's supervision
stand-down condition**; noted the SNS FIX stays **Andrew-gated per his 07-01 SNS rule** -> rides SCTY as patch
candidate #1); MSTR ACK; base ACK (allocations chain banked to the 49 refactor).

## Deployment Sequence + Verification (AE)

**NONE -- zero deploys, zero TF, zero mutations this window.** This is a read-only diagnostic session by
Andrew's design ("go through it line by line ... assess"). Every AWS call was an inspection or an IAM
*simulation*; no `safe-apply`, no artifact upload, no schedule/subscription change. The one write is a repo
doc commit (`04a1dca43`). **The SNS egress fix is Andrew-gated (COO, 07-01 rule) and was deliberately NOT
touched.**

## Blockers

**None.** Nothing stranded, no deploy open, no ledger entry outstanding (no deploy was begun).

## Current State (handoff surface -- zero-prior-context)

- **Commission:** Andrew-direct, line-by-line triage of the daily infra report; deliverable = the reporting-system
  FIX + the **SCTY** project foundation. Live in-session with Andrew; method is his (step by step).
- **Deliverable:** `docs/briefs/infra-report-noise-vs-real-triage-20260716.md` @ `04a1dca43` (CLOUD). Carries the
  verbatim commission, the INVERSION thesis, D-1..D-6, S-1..S-5, and a triage ledger. **The brief predates the
  freshness+automation walk results in this log -- it needs an update pass to fold F-1..F-8 / A-1..A-3.**
- **Generator:** `infra/aws/lambda/infrastructure_monitor/lambda_function.py` -> Lambda `opal-infrastructure-monitor`
  (python3.12, 512MB, 300s, role `opal-portal-lambda-role`, LastModified 2026-07-08), fired by EventBridge rule
  `infrastructure-monitor-daily` = `cron(0 13 ? * MON-FRI *)` **UTC** (= 09:00 ET). Emits SES to
  andrew@opalinvest.com + archives JSON to `s3://opal-data-portal-v2/infrastructure/reports/`.
- **Manifest:** `s3://opal-data-portal-v2/infrastructure/freshness_manifest.json` (53,166B, LastModified
  **2026-06-17 10:48:12**, `generated_at 2026-06-17T14:47:36Z`, `source_commit 1591d9ef821b`, 77 served_artifacts,
  7 pipelines). Generator = `.tools/freshness_manifest_gen.py` (hand-run, **no invoker**). Local copy pulled to
  the session scratchpad.
- **Prior art:** `docs/briefs/infra-report-revamp-proposal-20260616.md` (CVO) -- ADD half shipped, TRIAGE half did not.
- **WALKED + CLOSED:** the whole DATA FRESHNESS section (18 flagged lines, verdicts in the table above) and 3 of
  the 7 erroring functions (`access-anomaly-scanner`, `opal-assets-silver-schwab`, `smartx-assets-daily-pull`).
- **NOT YET ASSESSED (explicitly open -- do NOT read absence as clean):** the **122-HIGH composition** (NEXT, per
  Andrew); `trade-parquet-batch-export` (AI claims a concrete `dynamodb:Query` deny on the `by-date` GSI -- looks
  actionable, UNVERIFIED); `bd-silver-merge` (49/bd class -> passive-care/base); `opal-assets-silver-orion` (2/72),
  `opal-assets-silver-etf` (2/7); the COST section + the EC2 right-size axis (suspect: 14d-avg CPU is the WRONG
  AXIS for a batch box -- `inf-gold-layer-runner` c6a.4xlarge at 0.9% runs ~80min/night by design); the
  `(untagged) $255.24 = 70% of MTD` coverage denominator; DEPLOY-DRIFT; the SNS section (findings stand; FIX is
  Andrew-gated).
- **Live peers:** `0.7.0_AE_CloudOps` BASE is LIVE (PID 25356) on today's timed reads (13:22Z AoR / 13:30Z box boot
  / 14:15Z C2 mirror walk) -- different work, no collision; it holds the referred bd/49 allocations chain.

## Next Steps

- **[NOW, Andrew-directed] the 122-HIGH composition** -- decompose by rule / AWS-managed-vs-inline / chronic-vs-new.
  Working hypothesis: heavily inflated by AWS-managed-policy false positives (3 of today's NEW HIGHs are the SAME
  `AmazonSSMManagedInstanceCore` on `consolidation-gold-runner-role`, split by action-group; `Resource:*` on
  `ssmmessages`/`ec2messages` is **how AWS ships it** and is not grantable per-resource).
- **[this session] fold F-1..F-8 / A-1..A-3 into the brief**; then draw the FIX shape (the missing triage layer:
  new-vs-chronic + accepted/known suppression + state-change detection + a "monitor is blind" severity that
  OUTRANKS its blind readings) + the SCTY decomposition candidates.
- **[0.7.0_AE_CloudOps base]** the referred bd/49 allocations chain (passive-care, folds under the 49 refactor);
  incl. `bd_gold_ticker_resolution` (04-07) + `bd_silver_bd_assets_dim` (04-14, ENABLED trigger) same class.
- **[unowned -> route at COO]** `model-portfolios` producer freeze 2026-07-12 (REAL, 4 trading days, SEV1-adjacent
  + UNCONTRACTED). Possible adjacency: `yang-pipeline infra drift -- aws_sfn_state_machine.yang_pipeline [update]`
  in the same report. **Not yet dispatched.**
- **[me, mine to fix]** `freshness_manifest_gen.py` needs an invoker (D-2) -- my lane's own artifact. The fix is
  the manifest's refresh leg, and it should land WITH the SCTY reporting fix, not before it (a fresh manifest over
  an un-triaged report just re-points the noise).
- **[open question for the walk]** read the monitor's prefix-aging code to confirm/kill the newest-mtime
  FALSE-CLEAN mechanism (F-8, currently INFERRED).
