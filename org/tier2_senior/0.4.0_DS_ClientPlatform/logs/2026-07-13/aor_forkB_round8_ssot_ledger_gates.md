# AoR go-live: fork-B resolution -> rounds 6-8.1 -> SSOT ledger architecture, gate-2 CLOSED

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform | **Window:** 2026-07-12 ~20:29Z (post design-CLEAN log) -> 2026-07-13 ~04:05Z
**Commits this window:** 8 (denominator: `git log --author --since=2026-07-12T20:00Z | wc -l` = 8)

## What happened (the arc)

1. **Round-6 verdict (CTO~B):** the round-5 count-based daily-guard model hit a STRUCTURAL ceiling --
   fold correctness is per-account; count guards cannot see a per-account swap netting ~164. Not a
   patch round; CTO~B surfaced the architecture fork to Andrew. I held (no patch), staged fork prep.
2. **Andrew resolved the fork = B, reframed detect-and-ALERT** (relayed COO 2026-07-12T22:48Z,
   converged with CTO~B dispatch): the fold serves the correct attribution nightly; the risk is
   SILENT drift -> make it visible via a spot-check that alerts a human, never blocks.
3. **Fork-B build** (`d082f2eef`, `1a107c20b`, `bdc0c3f60`, `d18a25298`): per-account joined
   comparison + drift detector + fold surgery (count-RAISEs dropped, S1-systemic -> alert) + INF_D_11
   dispatch step + AE's SNS channel (opal-partner-etl-ops-alerts) + [GO-LIVE-EXERCISE] rehearsal label
   + isolated-prefix override. AE EXERCISED the delivery on the runner under inf-gold-layer-ec2-role:
   publish OK, SQS RECEIVED; Andrew's SMS failed = SNS SMS-SANDBOX (AE's lane; affects ALL INF SMS
   alarms -- his finding, routed to Andrew).
4. **Round-7** (`9c3b4513b`): CTO~B gate-1 found the detector FALSE-GREENED on missing/stale/blank
   data ("OK no drift" on a check that never ran). Fixed finding-grade (COMPARISON-STALE/
   -INCOMPLETE/CANNOT-EVALUATE; never a WARN). CVO~B verified... then gate-1 on round-7 found the
   fix itself REINTRODUCED the class: the as-of-keyed fixed-path comparison partition COLLAPSES two
   nights under a frozen INF_AOR_ASOF.
5. **Round-8 (Andrew-direct LOCKED contract):** ONE resolution at the front + APPEND event ledger +
   zero per-view AoR logic + detector = ledger-diff changes-only (freshness axis belongs to the
   existing freshness layer -- cited: freshguard watchdog TF, jwt_freshness x9 feeders,
   inf-gold-freshness-guard, mdpf gate, comp-freshness).
   - `345c85daa` (c1): INF_A_0.aor_resolver + lib/aor_resolution.py (canonical
     gold/dimensions/aor_resolution.parquet + ledger aor_ledger/events/{run-ts}.parquet -- NEW key
     per run = structurally uncollapsible; events baseline|new|change|relabel; EDGE-3 value->value
     only) + detector rewrite + A_01 comparison-emit retired + dispatch wiring.
   - `5581c0de1` (c2): 14-site migration -- fold census 10->1, household 4->1 (C_07 stamps
     household_headline_advisor_key; consumers inherit via household_headline_map). TWO inherit
     modes (load-bearing): FULL attach for the current-snapshot base (A_00/A_01); MOVERS-ONLY
     (apply_resolution_fold) for vintage frames -- a full attach there would rewrite historical
     attribution under OFF. DELTA-0 grounded LIVE: 0/873 basis mismatches (rep_name-slug vs
     rep_id-primary), 0/873 FLAG-2 catchall subset (probe in scratchpad delta0_basis_probe.py).
     Census gate: test_census_single_resolution_point (greps the estate; new per-view call fails).
6. **Round-8.1** (`68be1809d`): CVO~B gate-2 EXERCISED the real ON path -> the three ACTIVE
   firebreaks lived only in the RETIRED lazy loader; build_ returns ({},{}) silently ->
   run_resolver now RAISES under ACTIVE on raw-missing / representative_name-missing / all-null /
   populated-but-zero-movers (fail-closed, serve-stale); OFF positive-control preserved. False
   docstring fixed. **CVO~B re-verified: all 4 arms flip on the real path; gate-2 round-8+8.1
   CLOSED (35/35 battery re-pinned).**

## Verification (my runs, final state)

- test_aor_resolution.py 15/15 (uncollapsibility: frozen-as-of swap = distinct keyed rows; census;
  EDGE-3; R8-F1 arms + OFF control; state rebuild last-wins)
- test_aor_attribution_audit.py 12/12 (change fires w/ legit-vs-bug signal; baseline/new/quiet
  green; CANNOT-EVALUATE on list-fail + unparseable key; SNS gated/best-effort/rehearsal)
- test_aor_fold_derivation.py 22/22 | commit-gate clean every commit | safe-deploy PASS every push
- IAM: simulate-principal-policy on gold/audit/ + gold/dimensions/ with positive control
  (gold/dimensions/advisor_assignments.parquet=allowed) AND negative control
  (s3:DeleteBucket=implicitDeny) -- Rule 22a satisfied; ruling took the covered prefix anyway.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-pipescript io | INF_A_01 | PASS | terminal write, minimal blast -- grounded the emit placement |
| comp-pipescript io | INF_C_07, INF_C_01 | PASS/PARTIAL | C_07 reads grounded; C_01/C_07 WRITES under-detected (io manifest gap; code comments used) |
| comp-blast | apply_advisor_of_record_fold, derive_advisor_key | FAIL | NOT-FOUND on a STALE graph (8 stale nodes; lib-function nodes unindexed). Fallback: HEAD-source grep census, accepted by CTO~B/COO |
| comp-surface-check | (auto in safe-commit) | OK x8 | no critical surface touched any commit |

**What worked:** comp-pipescript io for placement/blast grounding. **What failed:** comp-blast on
lib functions (stale graph + no lib-function nodes) -- census had to be ground-truthed at HEAD
source. **Gap found:** graph does not index lib-level function call-sites; comp-build was stale vs
same-session commits (rebuild takes 35s mid-P0 -- deferred, worth an auto-refresh-on-HEAD hook like
comp-kuzu's).

## Briefs Written (DS)

None this window -- design flowed through the CTO~B LOCKED contract (broker) + commit messages;
the DS-lane state banked in memory: project_aor_round8_ssot_ledger_state.md.

## MCP traffic

~30 messages handled (all same-turn). Significant: CTO~B round-6 DESIGN-PASS verdict + round-8 P0 +
LOCKED contract + FLAG-1/FLAG-2 rulings + r8.1 confirm; Andrew fork=B resolution + two emphatic
sharpenings (one-front-resolution, zero per-view); COO co-sign path (5 steps) + D_02b staging +
CHANGE-3 checklist ACK; CVO~B gate-2 VERIFIED (r7) -> RE-OPENED (r8) -> CLOSED (r8+8.1); AE channel
grounding + runner exercise (SQS received; SMS-sandbox finding) + cleanup both-confirm-gated;
0.8.0_AE_CloudComp OPAL_ASSETS P0-A schema (3 notes adopted as binding).

## Blockers

NONE I own. All waits are evidence-cited external gates: gate-1 (CTO~B xhigh /code-review, running,
workflow wjlqray4r->fresh on 345c85daa^..5581c0de1 + 68be1809d delta); then CHANGE-2 -> SMS-channel
decision (Andrew; AE's sandbox finding) -> COO never-widen co-sign -> Andrew GO.

## Current State (zero-context handoff)

- **Everything AoR is SERVE-HELD + INF_AOR_FOLD_ACTIVE=0 (OFF). Nothing served. Estate runs
  yesterday's deployed code untouched.**
- Commits (origin/CLOUD): d082f2eef, 1a107c20b, bdc0c3f60, d18a25298 (fork-B build);
  9c3b4513b (round-7); 345c85daa + 5581c0de1 (round-8); 68be1809d (r8.1 firebreaks).
- Architecture: INF_A_0.aor_resolver.py (front of CHAIN_COMPUTE, switch-gated pre-GO ONLY) resolves
  ONCE -> gold/dimensions/aor_resolution.parquet (canonical, every view inherits) +
  gold/dimensions/aor_ledger/events/{run-ts}.parquet (append, uncollapsible) + aor_ledger_state.parquet
  (cache, rebuildable). Detector INF_D_11 -> lib/aor_attribution_audit.py (changes-only, exit-0,
  AOR-DRIFT-ALERT token + SNS INF_AOR_DRIFT_SNS_ARN + INF_AOR_DRIFT_EXERCISE rehearsal label).
  Consumers: A_00/A_01 FULL attach; B_00/C_01/INF_09/D_00c/D_00d/D_00f/D_02b movers-only
  apply_resolution_fold; C_02/D_02c/D_00d/D_04 household_headline_map off C_07's stamp.
- **GO release (single commit, COO-coordinated, order is FAIL-CLOSED):** (1) CHANGE-3 silver
  (convert_orion_api_to_silver.py, 63dd76201) deploys FIRST; (2) lift ALL AoR sentinels; (3) make
  INF_A_0's chain entry UNCONDITIONAL in orion-gold-dispatch.sh; (4) INF_AOR_FOLD_ACTIVE=1; AE wires
  INF_AOR_DRIFT_SNS_ARN + deploys the dispatch .sh to code/gold. Post-GO rollback = switch-flip ONLY.
- Staged tasks (my list): #19 D_02b reversed rep_id map grounding (post-gates, COO acceptance
  criteria banked); #15 SNS delivery re-run if CTO~B wants it on round-8 code; #16 _aor_exercise/
  S3 cleanup (human-confirm-gated both DS+AE); #13 leaderboard comp-validate config drift
  (post-AoR); #20 OPAL_ASSETS P0-B (wait for CTO~B-locked schema; opal-data-etfs/daily single-source
  rule banked).
- Memory: project_aor_round8_ssot_ledger_state.md (+ MEMORY.md CVO-bullet updated, MEMORY_FULL
  pointer added).

## Next Steps

1. [1.0.0_SA_CTO~B] gate-1 verdict lands -> if clean, ping [2.0.0_SA_COO] to advance the co-sign
   chain; if findings, ground-fix-reprove (same discipline as rounds 7/8.1).
2. [3.0.0_SA_CVO~B] on AE channel decision: re-stage INF_D_11+lib to isolated paths for (3a)/(3b);
   on CHANGE-2 re-entry: send ae737009f grounding pointers.
3. [2.0.0_SA_COO] owns cadence: CHANGE-2 -> SMS decision -> co-sign -> Andrew GO -> release.
4. Me, post-gates: task #19 D_02b grounding (Rule-22, (a)-vs-(b), file:line@commit, route to CTO~B).
