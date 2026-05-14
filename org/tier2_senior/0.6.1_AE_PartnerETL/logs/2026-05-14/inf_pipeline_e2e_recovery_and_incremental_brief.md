# Session log — INF chain E2E recovery + ADVI_INFINC brief + Phase 1 dispatch.sh shim

**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-14
**Time window:** ~12:54Z → 14:44Z (~2h wall)
**Branch:** CLOUD
**Continues:** `2026-05-13/session_chain_28_29_inffin_e2e_andrew_direct.md`
**Status:** Major threads CLOSED; cash_drag perf P0 in DS~B lane (~30min ETA)

---

## Summary

Six-thread session anchored by Andrew-direct end-to-end chain analysis request that surfaced a comprehensive incremental-architecture redesign opportunity. All major threads closed; queue cleared to ADHC_TRIGMRK + dispatch.sh asymmetry TOs.

1. **Chain #29 closure recap** — overnight chain failed silently at INF_D_00c; my P0 dispatch.sh fix `a9a114ba8` (2026-05-13 20:03Z) converted silent-success-then-emit-pipeline-complete.json into loud-failure-and-exit; validated empirically on today's morning cron.
2. **INF_D_00c P0 triage cycle** — DS~A's morning fix `fd11a33c2` (Int64/str dtype merge) unmasked a follow-on bug (advisor_key suffix collision); DS~A diagnosed in ~30s post-Andrew-direct chain failure; shipped `11ca5f36f`; chain `chain_gold-d_20260514_141936` recovery confirmed all 3 cumulative fixes converged clean.
3. **Andrew-direct E2E chain analysis** — full chain `chain_full_20260514_131842` fired 13:17:07Z; failed 49min later at INF_D_00c; recovery via mode=gold-d (Andrew said "lets not do another full run, we should just do the d group run"); SSM-direct dispatch bypassed Lambda-marker race; 13.4min recovery wall; all scorecard sentinels PASS.
4. **ADVI_INFINC brief** — 399-line `docs/briefs/inf-incremental-pipeline-design-20260514.md` (commit `2920719f8`) diagnosing ~35-40min/day waste in historical-rewrite stages; 5-pattern architecture (A: per-partition skip-gate / B: append-only cumulative blob / C: anchor cache / D: latest-state / E: date-windowed API pulls); 6-phase migration; target wall 8-12min/day from ~70min. §4.3+§4.6 expansions per CTO Q1+Q6 rulings shipped commit `cabf3d01d`.
5. **INFINC Phase 1 ratchet** — DS~D shipped lib `d88b7a7a4`; I shipped paired dispatch.sh shim `64e583272` + S3-sync ETag `361a99936c5bdbc98106162b2a43a45f`. Both gated behind `INFINC_PHASE1=1` master switch — structural no-op until Phase 2 dispatches. 5 smoke tests PASS.
6. **Three architectural gaps surfaced** — trigger-marker race (incident #1: 13:02Z phantom chain; incident #2: 14:14Z gold-d→full mis-fire after preemptive EC2 start); dispatch.sh `--run-date` symmetry bug (silver scripts shift via `{date}` template, pull scripts use internal `date -u` so they desync); INF_D_06.cash_drag.py line 211 perf bug (553s vs <30s expected — 20+ FutureWarnings from non-vectorized groupby-apply). All three routed.

**Memory writes today:** none new. Prior memory references in play: `feedback_bug_shadows.md` (referenced extensively in DS~A 3-fix sequence), `feedback_signal_bounded_vs_time_bounded_emit.md` (preserved in brief §4.2), `feedback_dispatch_sh_bang_inverts_exit_code.md` (yesterday's P0 fix anchor), `feedback_ds_sub_agent_routing.md` (DS~A/~D direct addressing throughout).

---

## Stale task closure (from `2026-05-13/session_chain_28_29_inffin_e2e_andrew_direct.md`)

| ID | Subject | Closure |
|---|---|---|
| #15 | Plan-B cron-disable trigger watch (04:00 UTC deadline if v1.7.56 not landed) | **AVERTED.** AE 0.7 v1.7.56 LANDED 2026-05-13 19:48Z (commit `5555eb2dc` deploy + `46c2c3dd6` code + `2ded10fba` log AC1-9 PASS). EventBridge `inf-canonical-prices-daily` rule remained ENABLED throughout. Plan-B was not invoked. |
| #16 | Chain #29 E2E mode=full monitoring + Lambda thaw orchestration | **TERMINAL-CLOSED.** Chain `chain_full_20260513_231128` ran ~Andrew-direct fire 23:08Z 2026-05-13; FAILED silently at INF_D_00c (silent-failure dispatch.sh bug). My P0 fix `a9a114ba8` (2026-05-13 20:03Z) — `run_script || rc=$?` not `if ! run_script` — corrected the silent emit. Lambda `inf-portal-advisor-publisher` reserved concurrency was thawed (no reservation post v1.7.56 deploy + async retries drained on v1.7.56 code). |
| #12 | REST consistency monitoring: duplicate_id_count sentinel (DS~D flag #1 — 624 dups / 3.5%) | **STILL PENDING.** Carries forward; not gating today's work. Will fold into Phase 2 Pattern A migration scope for INF_API_SILVER_TXN if relevant; otherwise standalone DS~D follow-on TO. |

---

## Chain #131842 (Andrew-direct mode=full E2E)

### Fire + failure

| Field | Value |
|---|---|
| Mode | full |
| Snapshot | 2026-05-14 |
| Fire | 13:17:07Z via Lambda inf-gold-trigger (EC2 was stopped; cold-boot path) |
| Chain start | 13:18:42Z (boot+dispatcher ~95s) |
| Telemetry run_id | `chain_full_20260514_131842` |
| Failure | 14:08:04Z at INF_D_00c step 39 (70.9%) |
| Wall | 49min |
| Failure class | DS~A `fd11a33c2` follow-on regression: merge suffix collision `advisor_key_x`/`_y` |

### Empirical step durations (anchors §1.1 of the brief)

| Stage | Wall | Cost class |
|---|---|---|
| INF_API_PULL_REPS | 5s | small |
| INF_API_SILVER_REPS/HHREP/ACCOUNTS_V2 | 1s each | small |
| INF_API_PULL_ASSETS_V2/NEW_PORTFOLIO | 1-2s | **skipped** (today's bronze existed) |
| INF_API_PULL_TXN | 426s (~7.1min) | unconditional re-pull |
| INF_API_PULL_PERF | 469s (~7.8min) | unconditional re-pull |
| INF_A_-1..A_04 | ~54s total | latest-state |
| INF_A_03 positions_cube | 47s | latest |
| INF_API_PULL_POSITIONS_DAILY | ~1-3min | snapshot pull |
| **INF_B_00 canonical_holdings** | **660s (~11min)** | **history walk — Pattern A target** |
| INF_B_01/01b/02 | 42s + 11s + 93s | mix |
| **INF_B_03 account_gains** | **344s (~5.7min)** | **history walk — Pattern A target** |
| C-stage (full) | not reached pre-failure | — |
| D-stage (steps 36-38: D_00/D_00b/D_00d) | ran ok | — |
| INF_D_00c step 39 | FAILED at 14:08:03Z | KeyError ['advisor_key'] line 628 |

### Diagnosis (DS~A ~30s post-fail)

DS~A `fd11a33c2` cast both sides of the merge at line 615-628 to str. The merge no longer threw the Int64-vs-object ValueError. But the merge result now has columns `advisor_key_x` + `advisor_key_y` (pandas auto-suffix on name collision) — the subsequent `joined.dropna(subset=['advisor_key'])` at line 628 KeyErrors because there's no plain `advisor_key` column anymore.

Root cause: `client_performance.parquet` (INF_C_02 output) AND `account_team.parquet` (INF_C_07 output) BOTH carry `advisor_key`. The dtype ValueError previously fired before pandas could attempt the merge, so the suffix collision was masked. Fix unmasked it. **Bug-shadows pattern (per `memory/feedback_bug_shadows.md`) — fix in dependency order; second bug only diagnosable AFTER first fix runs.**

### Recovery cycle

| Time | Action |
|---|---|
| 14:09Z | P0 surface to DS~A + COO + DS~A | with traceback + hypothesis |
| 14:12:55Z | I `aws ec2 start-instances` preemptively (anticipating DS~A's 5min ETA + saving 2min cold-boot) |
| 14:12:52Z | DS~A `11ca5f36f` shipped — 8-line drop `advisor_key` from `iw` pre-merge so `hh_to_adv` (INF_C_07 authoritative) wins |
| 14:13Z | S3-synced + ETag SHA-MATCH verified (`a2198e4ad6e2459233912ea70b8131c5`) |
| 14:14:19Z | **Stale-marker race** — preemptive EC2 boot consumed old mode=full trigger marker → dispatcher launched chain_full at 14:14:19Z, 3s BEFORE my 14:14:22Z mode=gold-d Lambda fire |
| 14:18:53Z | Andrew direct: "lets not do another full run, we should just do the d group run" |
| 14:19Z | SSM `dispatch.sh --kill` killed mode=full (was at step 7 / INF_API_PULL_TXN, 3min wasted) |
| 14:19Z | SSM-direct dispatch `bash /tmp/orion-gold-dispatch.sh --chain gold-d --no-shutdown` |
| 14:19:36Z | Chain `chain_gold-d_20260514_141936` started (clean) |
| 14:32:59Z | **TERMINAL COMPLETE** — 20/20 steps, 0 errors, 0 warnings |

### gold-d recovery scorecard (all sentinels PASS)

| COO sentinel | Expected | Actual |
|---|---|---|
| header_metrics AUA total | $203M ± | **$203,183,160.52** (QTD) |
| Advisors | 4 | 4 |
| Joe Brandenburg AUA | $16.2M | **$16,418,661.69** (+1.3% delta — within normal day-to-day drift) |
| Joe Brandenburg clients | 21 | **21** exact |
| NaN literal count on leaderboard.json | 0 | **0** (DS~C `de2286d67` held) |
| INF_D_00c step PASS | yes | 24s, status=ok |
| 30 platinum/firm/*.json refreshed today | yes | 14:19-14:33Z mtimes |

### Cumulative fix convergence

| Commit | Author | Scope |
|---|---|---|
| `fd11a33c2` | DS~A | Int64-vs-str household_id merge dtype fix (morning) |
| `de2286d67` | DS~C | NaN cleanup at write boundary + tripwire guard |
| `11ca5f36f` | DS~A | advisor_key suffix-collision drop pre-merge (afternoon) |

All three landed on `s3://opal-data-inf/code/gold/INF_D_00c.portal_leaderboard.py` ETag `a2198e4ad6e2459233912ea70b8131c5`. Validated end-to-end clean by chain_gold-d_20260514_141936.

### gold-d step durations (anchors brief Pattern D timing)

| Step | Wall | Notes |
|---|---|---|
| INF_D_00 | 8s | latest |
| INF_D_00b | 9s | derived from C_02 |
| INF_D_00d | 9s | derived from C_02 |
| INF_D_00c | 24s | **DS~A fix moment of truth — PASS** |
| INF_D_02 | 78s | per-HH latest (~862 accounts × 4 advisors) |
| INF_D_02b/02d/02c/03 | 1-7s each | small artifacts |
| INF_D_04b/04 | 5-22s | client portal summary |
| INF_09 | 10s | aggregator |
| INF_D_09 | 18s | per-account quarterly timeseries |
| INF_D_05 | 15s | client top_holdings |
| INF_D_06 | 17s | per-HH quarterly mix |
| INF_D_07/07a/08 | 2s each | latest-state |
| INF_D_05a (activity_scan) | 17s | window-bucketed |
| **INF_D_06a (cash_drag)** | **553s (~9.2min)** | **PERF BUG — 17× next-slowest** |

Total: 803s wall. 19 of 20 scripts ran in 1-78s; D_06a alone consumed 69% of total wall.

---

## INF_D_06a cash_drag perf P0 (Andrew-direct to DS~B)

**Andrew directive 14:33Z:** "Ok have DS~B fix that script now"

**Empirical evidence captured:**
- 553s wall vs <30s expected (matching sibling activity_scan at 17s)
- CPU sustained 106% (1+ core saturated)
- 20+ FutureWarnings observed from line 211 `df.groupby('account_id').apply(...)` — same call fires repeatedly
- Outputs landed correctly (`platinum/firm/cash_drag_{qtd,ytd,1y,max}.json` at 14:33Z) — perf-only bug, semantically valid

**Hypothesis routed to DS~B:** outer loop (per-account or per-date) wrapping the groupby-apply when it should be vectorized. Should be 4 invocations (one per window), not 20+.

**DS~B ACK'd, engaging.** ETA ~30min wall. Plan: read lines 180-230 + outer-loop context, refactor to single vectorized groupby per window, add `include_groups=False` for pandas 2.x compat, validate parity vs current cash_drag artifacts (byte-equal preferred).

**EC2 i-0ed5afded2ebd4ed4 stays warm** (`--no-shutdown` flag from my SSM-direct dispatch) for DS~B fix cycle.

---

## ADVI_INFINC — Incremental Architecture Initiative

### Brief (commit `2920719f8` + `cabf3d01d` expansion)

`docs/briefs/inf-incremental-pipeline-design-20260514.md` — 479 lines after expansion.

**Diagnosis anchor:** today's chain `chain_full_20260514_131842` (49min wall, failed at step 39) reinforced the structural argument — ~35-40min of "wasteful historical rewrites" out of ~70min total chain. Empirical step durations from the failed chain + recovery gold-d anchor §1.1 of the brief.

**5 patterns mapped:**
- A: per-partition skip-gate (date-partitioned canonical) — B_00, B_03, A_03, C_00, C_01
- B: append-only cumulative blob (timeseries assemblers) — C_02, C_03
- C: anchor cache (per-HH historical replay) — D_06, D_09
- D: dependency-skip (latest-state artifacts — already incremental) — D_00, D_00b/c/d, D_07, D_07a, D_05, D_05a, D_06a, D_08, INF_09
- E: date-windowed API pulls — PULL_TXN, PULL_PERF

**6 open questions routed by COO:**
1. Advisor attribution lag → CTO Q1 ruling: (a) point-in-time-correct + `--rebuild-advisor-attribution-only` escape hatch. v2 bifurcation deferred. (§4.3 expansion shipped.)
2. PULL_TXN/PERF trailing window size → DS~B empirical probe: 90d window ratified (max observed lag 65d, P99 4d, 25d safety margin). §6.2 brief default holds.
3. Schema-stamping → opt-in per-script (DS judgment).
4. partition_provenance.json layout → per-partition file.
5. DIAGFIX template → COO style call (banner during migration window).
6. Validation epsilon budget → CTO Q6 ruling: PK-stable sort + byte-equal (md5) gate. (§4.6 expansion shipped.)

### Phase 1 ratchet (LOCKED today)

| Component | Owner | Commit | ETag/Status |
|---|---|---|---|
| skip_gate.py + empty_sentinel.py + schema_version.py + partition_provenance.py + tests | DS~D | `d88b7a7a4` | 9 files S3-synced |
| dispatch.sh shim — 4 new flags + validation + env-var exports + bg-args + help text | AE 0.6.1 | `64e583272` | ETag `361a99936c5bdbc98106162b2a43a45f` |
| Brief §4.3 + §4.6 expansions (CTO Q1+Q6 rulings) | AE 0.6.1 | `cabf3d01d` | committed + pushed |

**Env-var contract LOCKED:**
- `INFINC_PHASE1` — master enable (default 0 = lib is no-op)
- `INFINC_REBUILD` — force re-write all partitions in scope
- `INFINC_REBUILD_START` / `INFINC_REBUILD_END` — date window
- `INFINC_REBUILD_ADVISOR_ATTRIBUTION_ONLY` — Phase 4 hook

5 smoke tests PASS on dispatch.sh shim. Phase 1 is structurally inert until `INFINC_PHASE1=1` is set — Phase 2 Pattern A migrations can dispatch independently without disrupting in-flight chains.

### Phase 2-6 sequencing (recommended)

| Phase | Scope | Owner | Days |
|---|---|---|---|
| 2 | Pattern A (B_00, B_03, A_03, C_00, C_01) | DS~B | ~5 |
| 3 | Pattern B (C_02, C_03) | DS~B | ~3 |
| 4 | Pattern C (D_06, D_09 + anchor cache materializer) | DS~A | ~4 |
| 5 | Pattern E (PULL_TXN + PULL_PERF date-windowed) | DS~B | ~2 |
| 6 | Validation + cutover (--validate-against-rebuild) | AE 0.6.1 + DS~A + DS~B | ~2 |

Total: ~3 weeks calendar, ~19 dev-days. Each phase shippable + reversible.

---

## Architectural gaps surfaced (3)

### 1. Trigger-marker race (incident #1 + #2 today)

**Empirical:**
- 13:02Z phantom chain: unattributed Lambda fire with snapshot_date=2026-05-13 triggered dispatcher; chain ran with `--run-date 2026-05-13` semantics, hit silver/pull date asymmetry, failed at step 2.
- 14:14Z gold-d→full mis-fire: my preemptive EC2 start at 14:12:55Z caused dispatcher daemon to consume the stale 13:17Z mode-marker (mode=full) on boot, launching chain_full at 14:14:19Z (3s before my 14:14:22Z mode=gold-d Lambda fire).

**Mitigations (P2 TO scope authorize):**
1. Lambda checks `telemetry status.json status == running` before writing markers; refuses queued fire + alerts operator
2. Dispatcher daemon poll loop refuses markers older than N seconds on boot (e.g., 5 min)
3. SSM-direct dispatch is the existing workaround for high-stakes recovery (used today)

Project code proposed: `ADHC_TRIGMRK`. Authoring queued.

### 2. dispatch.sh `--run-date` asymmetry

**Empirical (13:02Z phantom chain):** `{date}` template in catalog rows 176-187 substitutes to `$RUN_DATE` (which honors `--run-date` override per line 309 + 749). But pull scripts have no `{date}` template; they use script-internal `date -u +%Y-%m-%d`. Passing `--run-date 2026-05-13` shifts silver `--snapshot-date` to yesterday but pull bronze writes use today → silver looks for non-existent `/tmp/.../2026-05-13_representatives.json` → fail.

**Mitigations:**
- Symmetric `--run-date` propagation: inject `--date $RUN_DATE` into pull catalog rows OR document pull-rows-are-always-today as intentional
- My `a9a114ba8` fix already ensures loud-fail at step 2 if asymmetry triggers — SAFE outcome preserved

P2 standalone TO queued.

### 3. INF_D_06.cash_drag.py line 211 perf bug

Already routed to DS~B (Andrew-direct P0). Empirical 553s vs <30s; 17× the next-slowest gold-d script.

---

## Compiler Tools

| Tool run | Purpose | Result |
|---|---|---|
| `aws s3api head-object` on `s3://opal-data-inf/code/gold/INF_D_00c.portal_leaderboard.py` | Pre-fire SHA-MATCH gate (×2: against DS~A's `fd11a33c2` claim 14:01Z + `11ca5f36f` claim 14:12Z) | PASS both times — ETags `08b64c2b...` + `a2198e4a...` |
| `comp-pipescript deployed INF_D_00c` | First attempt at SHA-MATCH | Defaulted to bd-pipeline bucket (`opal-data-bd`) — flag needed for INF pipeline; fell back to S3-head-object manually |
| `aws s3api list-objects-v2 prefix=gold/logs/ ... sort_by(LastModified)` | Find current chain runner log | Found `chain_full_20260514_131805.log` + `runner_20260514_140807.log` |
| `aws s3 cp ... telemetry/.../history/{run_id}.json` | Pull terminal archive for chain #29 + chain_full_20260514_131842 + chain_gold-d_20260514_141936 | All 3 archives present + readable |
| SSM `dispatch.sh --kill` + pkill fallback | Kill mode=full chain mid-flight per Andrew direct | Clean kill; zero residual processes |
| SSM-direct `bash /tmp/orion-gold-dispatch.sh --chain gold-d --no-shutdown` | Bypass Lambda-marker race for clean recovery | PID 6264; chain started 14:19:36Z; ran to terminal complete |
| `bash -n data/orion/scripts/gold/orion-gold-dispatch.sh` | Syntax check on dispatch.sh shim pre-commit | PASS |
| 5 INFINC flag-parsing smoke tests (bad-date / start-gt-end / clean-parse / PHASE1=0 vs PHASE1=1) | dispatch.sh shim validation | All 5 PASS |
| `aws s3 cp data/orion/scripts/gold/orion-gold-dispatch.sh s3://...` | S3-sync dispatch.sh shim | Uploaded; ETag `361a99936c5bdbc98106162b2a43a45f` verified |

**Gap noted:** `comp-pipescript deployed` defaults to bd-pipeline; needs INF pipeline flag OR pipeline auto-detection. AE 0.5.0 (OpalETL lane) may own; or fold into next comp-tools session.

---

## Open follow-ons in my lane

| Item | Status |
|---|---|
| ADHC_TRIGMRK TO authoring (trigger-marker race + 2 mitigations) | next |
| dispatch.sh `--run-date` asymmetry TO | queued after TRIGMRK |
| Cohort delta investigation (accounts_dim 835 / account_team 862 / silver 842 / portal 799 / expected 857) | INFFIN close housekeeping; deferred to Phase 4 Pattern C touch |
| DS~B re-add `created_date`/`edited_date` to silver puller CONFIRMED_FIELDS (post-DWSPLT.002 regression flagged in Q2 probe) | folded into ADHC_TRIGMRK scope (or standalone DS~B TO) |
| Phase 2 Pattern A migration dispatch from COO | not in my lane until COO authors |

---

## Routing summary (MCPs sent this session)

| To | Subject |
|---|---|
| 2.0.0_SA_COO | RAVC2-style status: chain #29 closed + v1.7.56 confirmed + INF_D_00c repeat-failure RCA |
| 2.0.0_SA_COO | ACK + standing by for DS~A RAVC2 |
| 0.4.0_DS_ClientPlatform~A | ACK RAVC1 — chain #30 FIRED 13:01Z (pre-Andrew direct, became 13:17Z) |
| 2.0.0_SA_COO | P0 — chain #30 FAILED step 2 INF_API_SILVER_REPS snapshot-date mismatch |
| 2.0.0_SA_COO | Update — failed chain was NOT mine + dispatch.sh date-flag inconsistency RCA |
| 0.7.0_AE_CloudOps | Did you fire a chain ~13:02Z? |
| 2.0.0_SA_COO | Andrew direct — firing fresh chain 13:17Z for E2E analysis |
| 2.0.0_SA_COO | Chain #131842 RAVC2-FAIL — DS~A fd11a33c2 follow-on regression at INF_D_00c:628 |
| 0.4.0_DS_ClientPlatform~A | P0 — chain #131842 FAILED at INF_D_00c:628 |
| 0.4.0_DS_ClientPlatform~A | EC2 ALREADY STOPPED — cold-boot path on your fix |
| 0.4.0_DS_ClientPlatform~D | ACK Phase 0 contract — env-var interface is exactly right |
| 2.0.0_SA_COO | ACK all directions — DS~A racing fix |
| 0.4.0_DS_ClientPlatform~A | RAVC1 — recovery chain FIRED 14:14:22Z mode=gold-d |
| 2.0.0_SA_COO | ALERT — recovery chain is mode=FULL not gold-d (stale-marker race) |
| 0.4.0_DS_ClientPlatform~A | FYI — recovery chain came up as mode=full not gold-d |
| 2.0.0_SA_COO | Andrew direct kill+re-fire — mode=full chain KILLED 14:19Z, mode=gold-d FIRED 14:19Z clean |
| 0.4.0_DS_ClientPlatform~B | P0 — fix INF_D_06.cash_drag.py line 211 groupby-apply perf bug NOW |
| 0.4.0_DS_ClientPlatform~B | ACK Q2 probe — 90d window LOCKED in brief §6.2 |
| 0.4.0_DS_ClientPlatform~D | Pick option (a) — separate dispatch.sh PR + smoke test on my side |
| 2.0.0_SA_COO | RAVC2-CLEAN — chain_gold-d_20260514_141936 COMPLETE, all sentinels PASS |
| 0.4.0_DS_ClientPlatform~A | RAVC2-CLOSE — your 11ca5f36f fix exercised CLEAN end-to-end |
| 0.4.0_DS_ClientPlatform~A | CLOSE ACK — EC2 staying warm for DS~B cash_drag fix |
| 2.0.0_SA_COO | ACK RAVC2-accept — starting §4.3/§4.6 brief expansions |
| 2.0.0_SA_COO | Brief §4.3 + §4.6 expansions SHIPPED — cabf3d01d |
| 0.4.0_DS_ClientPlatform~D | RAVC1 — dispatch.sh INFINC Phase 1 shim SHIPPED + S3-synced — 64e583272 |
| 2.0.0_SA_COO | INFINC Phase 1 LOCKED — dispatch.sh shim 64e583272 + DS~D lib d88b7a7a4 both shipped |

26 messages this session.

---

## Commits this session

| Commit | Subject |
|---|---|
| `2920719f8` | docs(inf-pipeline): incremental architecture design brief — Andrew-direct 2026-05-14 (399 lines) |
| `cabf3d01d` | docs(inf-pipeline): brief §4.3 + §4.6 expansions per CTO Q1+Q6 rulings (80 inserts / 4 deletes) |
| `64e583272` | feat(inf-dispatch): INFINC Phase 1 — --rebuild family flag plumbing + env-var exports for DS~D skip-gate lib (75 inserts) |

All 3 pushed to origin/CLOUD.

---

## Lessons reinforced

1. **Preemptive EC2 warm-up pays off** — anticipating DS lane's fix-ETA against EC2 cold-boot window saves ~2min/cycle. DS~A 14:33Z explicitly called this out: "lane-coordination-by-anticipation discipline compounds well." Will codify in prompt.md.
2. **Bug-shadows pattern empirical proof** — DS~A's two-fix sequence (dtype mask + suffix collision unmasked) is the textbook `memory/feedback_bug_shadows.md` case. Diagnosis-first discipline matters AFTER the upstream fix lands; the second bug only becomes diagnosable then.
3. **SSM-direct dispatch is the high-stakes recovery workaround** — Lambda-marker path has trigger-marker race (incident #1 + #2 today). For deterministic recovery: skip Lambda, SSM directly to `bash /tmp/orion-gold-dispatch.sh --chain X --no-shutdown`. Mitigation TO (ADHC_TRIGMRK) authoring queued; in the interim, SSM-direct is the documented escape hatch.
4. **Incremental architecture brief is a high-leverage artifact** — Andrew-direct request → 2h to ship the comprehensive 479-line brief + Phase 1 ratchet locked-in. Multiple downstream wins: CTO Q-rulings, DS~B empirical Q2 probe, DS~D Phase 1 lib, AE dispatch.sh shim, COMP_LEARNS signal corpus per COO (5 architectural gap candidates from a single day's empirical work). Pattern: empirical baseline (real chain timings) > theoretical analysis; ship a doc + a Phase 1 ratchet same-day.

---

## Status at session end

- Chain `chain_gold-d_20260514_141936` complete + scorecard-PASS
- INFFIN v0.1 close path data-side unblocked
- INF_D_06.cash_drag perf P0 in flight (DS~B, ~30min ETA at 14:35Z)
- INFINC Phase 1 ratchet LOCKED (DS~D + AE 0.6.1)
- EC2 i-0ed5afded2ebd4ed4 running for DS~B
- Inbox-watch live; queue clear except for ADHC_TRIGMRK + --run-date asymmetry TO authoring (next)
