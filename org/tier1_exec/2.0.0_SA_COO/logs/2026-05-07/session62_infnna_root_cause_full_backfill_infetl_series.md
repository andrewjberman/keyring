# COO Session 62 — INFNNA Root Cause + Full Backfill + INFETL Series Dispatch

**Date:** 2026-05-07
**Agent:** 2.0.0_SA_COO
**Session focus:** Andrew's NMNC/NNA inconsistency diagnosis → full Inflection bronze backfill (local) → 13-TO series authored & dispatched → CHAININC structural finding → multiple parallel agent ships throughout afternoon

---

## Trigger

Andrew @ ~15:23Z 2026-05-07: "Assets Overview NNA: Q2 2026 firm NNA = -$1.36M while NMNC = $19.7M (incongruous). Hypothesis: 'Inflection Wealth Management' general advisor tag may be capturing what should be Patrick Scanlan / Joe Brandenburg / Peter Lee."

---

## Phase 1 — INFNNA.001 Diagnostic

**DS~A RAVC1 (root cause)**: `pull_inflection_transactions_v2.py` line 71 hardcoded `INFLECTION_REP_IDS = "3,11,12"` — Joe Brandenburg (rep_id=6) excluded from API @RepIDs param. Bronze never had Joe's transactions. Account-level rep_id PERFECTLY aligns with txn-level (no Orion tagging issue).

**DS~A RAVC2 (deeper finding)**: Inflection retroactively re-attributed accounts in Orion in last few days. Joe's accounts were rep_id=3 (IWM) historically, now rep_id=6. silver/transactions + canonical_nna carry stale IWM-aggregated attribution. NMNC/NNA mismatch is data-era mismatch — accounts_v2 reflects NEW; canonical_nna reflects OLD.

**Quantified misattribution** (canonical_nna IWM cluster, 253 accounts):
- rep_id=3 (IWM proper): 2 accts $3,517 — correct
- rep_id=6 (Joe): 17 accts $5.2M — historically misattributed
- rep_id=11 (Patrick): 48 accts $7.65M — historically misattributed
- rep_id=12 (Peter): 181 accts $63.7M — historically misattributed

---

## Phase 2 — Wave C1 Architecture Pivot Sequence (~17:00-17:30Z)

Multiple architecture rewrites in ~30 min driven by Andrew direct:

1. **AE 0.7 dispatched 8x parallel SSMs on inf-bronze-runner EC2** (Wave C1 backfill) — pivoted from prior 1x sequential.
2. **Andrew: "ditch EC2, use Lambda"** — COO dispatched architecture pivot to AE 0.7.
3. **Race condition**: AE 0.7's 8x SSMs dispatched ~52s before pivot landed. Cancel-command + watchdog stopped instance.
4. **Andrew: "8x EC2 is fine"** — rescinded Lambda pivot. AE 0.7 restarted EC2 + re-dispatched 8 SSMs.
5. **Andrew: "you can run api calls locally"** — COO took over backfill on local Andrew-machine via Python ThreadPoolExecutor (8-16 workers).
6. **EMPIRICAL** confirmed: 16 workers = 0.21 dates/sec, ~2.7h ETA matched Andrew's projection.

**Local backfill 8 parallel streams launched 17:51Z 2026-05-07:**
- Stream A: tax + perf per-date (16 workers, 2247 dates)
- Stream B: billing per-date (8 workers, 2241 dates)
- Stream C: assets_v2 batch
- Stream D: positions_daily batch
- Stream E: transactions full-history (single-shot, --start-date 03/11/2020 --end-date 05/07/2026)
- Stream F: unified_account_dim (initially failed; later fixed via UAD-CREATOR + DS~B re-pull)
- Stream G: new_portfolio_accounts (single-shot)
- Stream H: representatives (single-shot)

**Critical deliverable: Stream E2 (transactions full historical with @RepIDs="3,6,11,12") shipped 1,154,146 rows / 545.2 MB — Joe Brandenburg's complete history pulled for the first time ever.**

---

## Phase 3 — Silver Convert + accounts_v2 Filter Fix

**Transactions silver** (1.15M rows, snapshot 2026-05-07): clean.

**accounts_v2 silver** initially failed — Guard B FAIL at $476.9M (sanity bounds [$50M, $400M]). Root cause: `build_accounts_v2()` filtered by custodian only (Fidelity_Inflection + Fidelity_LH) — NO rep_id filter. Let through 2,215 accounts.

**COO-applied fix** to `convert_orion_api_to_silver.py`:
- Added `INFLECTION_REP_IDS = {3, 6, 11, 12}` constant
- Added post-merge filter: `out = out[out['rep_id'].isin(INFLECTION_REP_IDS)]`
- Result: 848 rows / **$203,203,649** (canonical for today, confirmed by Andrew)

---

## Phase 4 — TO Series Authored + Dispatched (Andrew direct: "Author everything now and issue, we are going to barrel through all of this")

**11 INFETL Phase 1 TOs authored pre-Andrew-GO** (CTO RAVC2 authorization), then dispatched in 5 consolidated agent messages:

| TO | Owner | Status |
|----|-------|--------|
| ADVI_INFETL.001 (cron + nightly fallback) | AE 0.7 | ✅ COMPLETE 7e9d30e7d (REVISED — cron is now FALLBACK 06:00 UTC, not primary) |
| ADVI_INFETL.002 (dispatch.sh sentinel) | DS~A | ✅ COMPLETE 2e0024db2 |
| ADVI_INFETL.003 (inf-portal-publisher Lambda) | DS~B | ✅ COMPLETE 9b66c9c43+ all 7 ACs PASS |
| ADVI_INFETL.004 (inf-portal-advisor-publisher) | DS~C | ✅ COMPLETE 0c6a1be6e + AE 0.7 v1.7.36 deploy |
| ADVI_INFETL.005 (S3 ObjectCreated wire) | AE 0.7 | ✅ COMPLETE 7e9d30e7d |
| ADVI_INFETL.007 (portal-route audit) | RD | ✅ COMPLETE df0b18942 — 16 gold violations + 5-tranche TO-8 plan |
| ADVI_INFETL.DAILY-AUDIT | AE 0.7 | 🔄 in queue |
| ADVI_INFETL.LAMBDA-DIMS | AE 0.7 | 🔄 gated on DAILY-AUDIT |
| ADVI_INFETL.SILVER-AGGREGATOR | AE 0.7 | 🔄 in queue |
| ADVI_INFETL.GOLD-EVENT-TRIGGER | AE 0.7 | ✅ COMPLETE c6500c313 (v1.7.34) |
| ADVI_INFETL.SHAPE-VERIFY | DS~A | 🔄 in queue |
| ADVI_INFNNA.UAD-CREATOR | DS~B | ✅ COMPLETE ec6f19c00 |
| ADVI_INFNNA.GUARDS-AUDIT | DS~A | ✅ COMPLETE 7782c716f (Guard B [$150M,$300M]) |
| ADVI_INFNNA.SILVER | DS~A | 🔄 gated on bronze completion |
| ADVI_INFNNA.GOLD | DS~A | 🔄 gated on silver |
| ADVI_INFNNA.PORTAL-VERIFY | RD | 🔄 gated on gold |

**Architecture revision** (Andrew @ ~18:30Z): "lambdas should be doing both daily incremental ingestion and silver conversion. then our gold runner ec2 needs to be event-based to trigger at the receipt of all daily silver data" + clarified: clock-driven bronze, event-driven downstream. Cron at 06:00 UTC is fallback only.

INFETL.001 revision section appended to TO file documenting the new architecture.

---

## Phase 5 — Follow-on TOs (per emerging findings)

**Authored + dispatched mid-session:**

- **ADVI_INFETL.ROUTER-DRIFT** (AE 0.7, Andrew direct: "fix that drift issue, definitely want to keep everything organized in tf"): ✅ COMPLETE 59919e763 + eb253a058 + portal-auth-v1.15.1. CloudTrail audit identified Andrew_Berman as drift actor (11 manual UpdateFunctionCode events 2026-04-06 → 2026-04-21 iterating v3→v13).

- **ADVI_INFETL.MDR** (DS~A, Andrew direct: "we need master data registry very badly"): ✅ COMPLETE 85977d68a + 31bf7e99a. 75 artifacts enumerated across bronze/silver/gold/platinum. data_semantic_class taxonomy: SINGLE_SHOT/SNAPSHOT_PER_DATE/LOOKBACK_WINDOW/EVENT_LOG. Surfaced 7 GAPs.

- **ADVI_INFLEC.CUMCHART** (DS~D, Andrew direct routing): 🔄 3 iterations (689e9bc81 + 2227a8ac1 + fc18781eb) — state-source + firm-tag + household_id-dtype fixes. Pending AE 0.7 re-QA #3 + PROD + CDN.

- **ADVI_INFETL.CHAININC** (AE 0.6.1, Andrew direct: "billing and tax definitely need to be included in chain"): 🔄 RAVC0 reframed (billing/tax ARE on chain) → RAVC1 surfaces bigger finding: 4 of 7 silver builders perpetually fail (household, performance, activity, accounts_v2). Phase 1.1 graceful-skip APPROVED, in flight.

- **owned-paths micro-TOs** (AE 0.7): ✅ 79dbf6138 (initial POD4_OR_AE lane) + bc93a1c52 (widened to `infra/aws/lambda/inf-*/**` glob).

- **IAM-CF mini-TO** (AE 0.7): ✅ 19c267f18 (v1.7.35) — `cloudfront:CreateInvalidation` for inf-gold-layer-lambda-role. Unblocked DS~B's INFETL.003 CF invalidation.

---

## Phase 6 — Discovery: 4 Silver Builders Chronically Fail

**AE 0.6.1 CHAININC RAVC1 finding** (~19:30Z):

Daily inf-silver-chain Lambda runs SILVER_BUILDERS = [household, performance, activity, billing, tax_unrealized, tax_realized, accounts_v2]. Every chain run shows `ok=3 fail=4`:

| Builder | Failure |
|---------|---------|
| household | NoSuchKey on geo_verify (orphaned producer) + unified_account_dim daily exit=3 |
| performance | NoSuchKey on performance_dim.csv (producer SKIPs on pre-onboarding 400; 0 CSVs ever written) |
| activity | NoSuchKey (same source as household — unified_account_dim) |
| accounts_v2 | NoSuchKey OR Guard B $476M > $300M (deployed silver layer may be STALE — pre-DS~A's INFLECTION_REP_IDS filter) |

This DIRECTLY MAPS to MDR GAP-1 (activity unpopulated). Same root-cause class. Months of partial production data hidden by try/except + continue.

**4-phase fix plan approved:**
1. Phase 1.1 (AE 0.6.1, ~1h, **APPROVED**): graceful-skip pattern in silver builders (mirrors v1.7.31 pattern). Chain summary becomes "ok=N skipped=M" not fake-FAILing.
2. Phase 1.2 (DS~A, ~1d): fix bronze producers per per-builder root-cause table.
3. Phase 1.3 (joint, ~0.5d): empirical 2-day chain watch, target ok=7/7.
4. Phase 1.4 (Andrew approval): Guard B bound widening for accounts_v2 if needed (verify deployed silver has DS~A's INFLECTION_REP_IDS filter first).

DS~A also dispatched (Andrew direct: "compiler-aided investigation") for parallel deeper bronze-side root cause. Coordinated with AE 0.6.1 to avoid duplication.

---

## State at session log time (~19:35Z)

### COMPLETE TOs (15)
1. INFNNA.UAD-CREATOR (DS~B ec6f19c00)
2. INFNNA.GUARDS-AUDIT (DS~A 7782c716f)
3. INFETL.002 sentinel write (DS~A 2e0024db2)
4. INFETL.007 portal-route audit (RD df0b18942)
5. INFETL.001 fallback cron (AE 0.7 7e9d30e7d)
6. INFETL.005 S3 wire (AE 0.7 7e9d30e7d)
7. INFETL.003 publisher Lambda full empirical (DS~B + AE 0.7 v1.7.34)
8. INFETL.GOLD-EVENT-TRIGGER (AE 0.7 c6500c313 v1.7.34)
9. owned-paths initial (AE 0.7 79dbf6138)
10. owned-paths widen (AE 0.7 bc93a1c52)
11. IAM-CF mini-TO (AE 0.7 19c267f18 v1.7.35)
12. ROUTER-DRIFT (AE 0.7 59919e763 portal-auth-v1.15.1)
13. INFETL.004 advisor publisher (DS~C 0c6a1be6e + AE 0.7 v1.7.36 21a00aec4)
14. ADVI_INFETL.MDR (DS~A 85977d68a + 31bf7e99a)
15. AD-HOC compiler INF support (DS~A 7ee141664) — separate Andrew direct order

### IN FLIGHT
- INFETL.DAILY-AUDIT (AE 0.7 — gates LAMBDA-DIMS)
- INFETL.LAMBDA-DIMS (AE 0.7)
- INFETL.SILVER-AGGREGATOR (AE 0.7)
- INFETL.SHAPE-VERIFY (DS~A — gated on LAMBDA-DIMS)
- INFETL.CHAININC Phase 1.1 (AE 0.6.1 — graceful-skip pattern, in flight)
- INFLEC.CUMCHART (DS~D iter3 fc18781eb shipped, AE 0.7 re-QA #3 in flight)
- 4 silver-builder root cause investigation (DS~A compiler-aided, parallel with AE 0.6.1)
- INFNNA.SILVER (DS~A, gated on bronze)
- INFNNA.GOLD (DS~A, gated on silver)
- INFNNA.PORTAL-VERIFY (RD, gated on gold)
- 8 bronze backfill streams running locally (Streams A-D — tax+perf, billing, assets, positions; ETA Stream A+B ~22:00Z, C+D overnight)

### KEY ARTIFACT STATES (post-fix)
- silver/transactions/2026-05-07.parquet: **1,154,146 rows** (Joe Brandenburg full history INCLUDED)
- silver/api_dims/accounts_v2/snapshot_date=2026-05-07/data.parquet: **848 rows / $203.2M** (INFLECTION_REP_IDS filtered, Andrew-confirmed canonical)
- silver/api_dims/representatives/snapshot_date=2026-05-07/: 18 rows
- platinum/firm/* (9 outputs from INFETL.003 publisher empirical run): all written + CF invalidated

### OPEN DECISIONS / WATCHES
- Andrew Phase 1.4 Guard B bound widening (after deployed-silver-version check)
- INF_D_00d iter3 QA result (real states + 4 advisors + $199.6M total)
- Bronze tax+perf + billing completion ETA ~22:00Z
- INFNNA.SILVER → INFNNA.GOLD → PORTAL-VERIFY cascade tonight ~22:00-23:00Z
- Pending CTO PRD per Andrew note — TOs route to 0.7.0_AE_CloudOps~B (sub-agent ~B specifically, not the primary ~A who's been shipping today)

---

## Decisions / Rulings (this session)

1. **Architecture: bronze clock-driven, downstream event-driven.** INFETL.001 cron is FALLBACK at 06:00 UTC, not primary. Primary trigger is silver-aggregator → gold-event-trigger event chain.
2. **Wave C1 backfill executed locally** on Andrew's machine (Python ThreadPoolExecutor 16 workers); inf-bronze-runner EC2 stays only for inf-api-txn daily cron.
3. **accounts_v2 silver filter** = INFLECTION_REP_IDS {3,6,11,12} applied (DS~A 7782c716f + COO patch in convert_orion_api_to_silver.py).
4. **INF_D_00d cumulative_chart fix** unfolded from INFNNA.GOLD scope; assigned standalone to DS~D (per Andrew direct routing).
5. **INFETL.LAMBDA-DIMS Lambda code lane**: DS~B (publisher pattern) + AE 0.7 (Terraform). owned-paths exception widened to `infra/aws/lambda/inf-*/**` for POD4_OR_AE.
6. **CHAININC Phase 1.1 graceful-skip APPROVED** (AE 0.6.1, mirrors v1.7.31 pattern). Phase 1.2 bronze fixes routed to DS~A.
7. **Master Data Registry now canonical**: docs/architecture/INFETL_MASTER_DATA_REGISTRY.md + inf_data_graph.yaml. comp-tools.yaml inf_pipeline block references it.
8. **CloudTrail finding from ROUTER-DRIFT**: Andrew was the actor on 11 manual UpdateFunctionCode events 2026-04-06→2026-04-21. Process reminder framed: CLAUDE.md rule 1 = Terraform-only Lambda deploy.

---

## Notable agent velocity

- **DS~A**: 6 ships today (compiler INF support 7ee141664, GUARDS-AUDIT 7782c716f, INFETL.002 sentinel 2e0024db2, MDR 85977d68a + 31bf7e99a, accounts_v2 silver filter)
- **DS~B**: 3 ships (UAD-CREATOR ec6f19c00, INFETL.003 publisher 9b66c9c43+9ba99cff6+940108659, INFETL.003 full empirical close)
- **DS~C**: 2 ships (INFETL.004 advisor publisher 0c6a1be6e, BLOCKER follow-up to widen owned-paths)
- **DS~D**: 4 ships (SL-P1c shadow gap fix 6424b29ab, INF_D_00d 3 iterations 689e9bc81 + 2227a8ac1 + fc18781eb)
- **AE 0.7**: 8 ships (INFETL.001+005 7e9d30e7d, GOLD-EVENT-TRIGGER c6500c313, OWNPTH 79dbf6138 + bc93a1c52, IAM-CF 19c267f18, ROUTER-DRIFT 59919e763 + eb253a058, INFETL.004 deploy 21a00aec4)
- **AE 0.6.1**: 3 ships (T-1 Lambda v1.7.30 fd4105bec, build_billing_dim NoSuchKey v1.7.31 f427c6aed, billing $0 AUA v1.7.32 b2e634a12) plus extensive diagnostic work (CHAININC RAVC0 + RAVC1)
- **RD**: 2 ships (INFLFE.006 final verification a184ac895, INFETL.007 audit df0b18942)
- **CTO**: PRD v0.2 ratchet in progress (autonomous)
- **COO**: 13 TOs authored + dispatched in 5 batches; running local backfill streams; CHAININC + GAP analysis routing

---

## Inbox watcher health

- COO inbox-watch.sh repeatedly exits on message delivery (by design); relaunched after each exit
- 2-min recurring loop active (cron 35f6666b) for "watcher running + sweep last 5 read messages"
- Andrew flagged DS~A inactive at one point (~18:54Z) — sub-agent inbox routing nuance; resolved when watcher caught the ACK

---

## Forward-looking (tonight)

- ~22:00Z bronze tax+perf completion → INFNNA.SILVER fires
- ~22:30Z silver done → INFNNA.GOLD canonical_nna rebuild + INF_D_08 + INF_D_00c re-run (DS~D's INF_D_00d picked up via gold cascade — needs DS~D commit + S3 upload BEFORE chain step 35)
- ~22:45Z RD INFNNA.PORTAL-VERIFY visual confirm
- Joe Brandenburg appears in portal NMNC/NNA reconciliation completes

Pending CTO PRD (Andrew flagged incoming) — TOs to route to 0.7.0_AE_CloudOps~B specifically when received.
