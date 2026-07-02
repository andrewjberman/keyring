# ADVI_ETLFIX WS-1 CLASS-B -- inf converter-guard + legacy-dim audit (findings)

**Author:** 0.4.0_DS_ClientPlatform~B | **Date:** 2026-07-02 | **Type:** AUDIT-ONLY findings (feeds DS~A's uniform DEFER-guard set + CTO arch-gate)
**Scope:** inf-only (opal-data-inf). Grounded per Rule 22 -- mechanism=source (file:line), state=live S3 (comp-freshness + aws s3 ls), 2026-07-02.
**Split (confirmed w/ DS~A 202054Z):** ~A IMPLEMENTS the shared `defer_guard_read_bronze` helper (`_orion_api_silver_lib.py`) + wires each converter; ~B (this) AUDITS -> the prioritized fix-shaped list below. I do NOT write guard code.

## The chain (grounded)

`data/inf/scripts/gold/orion-gold-dispatch.sh`: `CHAIN_FULL` (line 337) = `CHAIN_PULL` (20 steps, line 334) + `CHAIN_COMPUTE` (43 steps, line 335) = **63 steps**. ALL silver converters live in the PULL stage (steps 3-20); step catalog + flags = lines 235-303. PULL steps are `timeout`-bounded + TOLERATED (585-594) -> a tolerated pull-miss leaves bronze ABSENT, which is exactly why the downstream silver converter must DEFER (carry-forward) instead of hard-abort or silent-stale. Eclipse silver is post-sentinel best-effort, NOT one of the 63.

## Guard census result

**GUARDED = 2** (the arch-gate-PASSED 3-limb pattern: NoSuchKey->None DEFER + `Inflection/GoldChain` CW metric + N-staleness-ceiling):
- convert_transactions_to_silver.py (INF_API_SILVER_TXN, step 10) -- confirmed (b7dc964db).
- convert_performance_to_silver.py (INF_API_SILVER_PERF, step 12, TWR `silver/performance/`) -- confirmed (c6332e5dd).

**UNGUARDED IN-CHAIN = 8 silver-write paths across 4 scripts** (each: unguarded read -> raise -> `sys.exit(1)` -> hard-aborts the chain; OR a tolerated .jsonl.gz that silently reads the stale prior on miss). Prioritized below.

## PRIORITIZED fix-shaped findings (the deliverable)

### P0 -- highest stakes (guard first)
1. **assets_v2** -- `convert_assets_v2_to_silver.py` reads `bronze/assets/{date}.jsonl.gz`, unguarded `get_object` **:87** -> missing raises -> `sys.exit(1)`. It is the EARLIEST silver step (step 6): a tolerated-pull miss HARD-ABORTS the whole 63-step chain BEFORE B_00->D (the served-AUA producers) ever run. Same P0 class the txn guard fixed. **FIX: the full 3-limb DEFER-guard (carry-forward + CW metric + ceiling).** Needs its OWN guard (direct .jsonl.gz reader, not the shared CSV read).
2. **positions_mv** -- `convert_orion_api_to_silver.py --dim positions_mv` reads `bronze/positions/{date}.jsonl.gz`, unguarded `get_object` **:799** (empty->RuntimeError:805->exit). Step 14, feeds the served-AUA lineage (positions/holdings->B_00 canonical_holdings). On pull-miss it silently reads the STALE prior .jsonl.gz = silent stale served-AUA (worse than a loud abort). **FIX: DEFER-with-HONEST-VINTAGE, N=1** (CTO-sharpened, tighter than txn/perf N=2 -- per DS~A). Also trace: is `reconvert_bronze_to_jsonl(_parallel)` chain-wired daily or backfill-only? (determines whether positions also needs a pull-reliability fix -- see net-new #5; agent found reconvert is a one-time LEG-3 bronze reformatter, NOT chain-wired -> positions .jsonl.gz freshness rides the daily pull, so the guard is the right lever, no reconvert dependency).

### P1 -- shared choke point (one guard covers 6 steps)
3. **The 6 CSV-dims** -- reps (step 3), household_rep_mapping (4), accounts_v2 (8), tax (16), billing (18), **perf_dim (20 -- the FLAGGED one, `silver/api_dims/performance/`, distinct from step-12 TWR perf)** ALL read via the SHARED `_orion_api_silver_lib.py::read_bronze_csv` (**353-379**), which raises NoSuchKey/FileNotFoundError with NO DEFER. **FIX: put the DEFER-guard in `read_bronze_csv` ONCE (DS~A's `defer_guard_read_bronze`) -> covers all 6 chain steps in one change.** This is the highest-leverage guard. (build_tax_dim.py:210-214 + build_billing_dim.py:170-174 are the tax/billing entrypoints over the same shared read.)

### P1 -- legacy-dim latent hazard (NOT benign orphan)
4. **aum_snapshot degrades the dispatch freshness gate to ALWAYS-PROCEED.** `silver/aum_snapshot/` is EMPTY (0 objects live). `orion-gold-dispatch.sh::check_freshness()` **:373** reads it -> empty -> `silver_latest=""` -> **:378 "could not determine silver latest -- proceeding"** = the freshness gate silently degrades OPEN. **FIX (dispatch, not a converter): remove aum_snapshot from check_freshness (or repoint to a live surface); also the readers INF_A_04:54 / INF_D_00:65 / INF_D_04:82 (household_name reads) need repoint.** This is a silent-gate-hole, higher priority than the other 3 dims.

### P2 -- cleanup + optional
5. **accounts_dim residual readers** -- DEAD producer (legacy `convert_orion_to_silver.py::build_accounts_dim:657`, de-wired), last write 04-29 (comp-freshness FAIL). Critical consumers already repointed to `gold/dimensions/accounts_dimension_latest.parquet` (ADVI_INFREF P1 LEG-1). RESIDUAL live readers = stale-input hazard: INF_D_02/D_04/D_05/D_06/D_07/D_07a + `lib/tax_status.py`. **FIX: repoint the residual readers to the fresh gold dim (finish the LEG-1 migration), then decommission `silver/accounts_dim/`.**
6. **household / gap_manifest** -- both DEAD (household superseded by the active `household_rep_mapping`; gap_manifest a static 234B frozen 04-29, INF_09 no longer reads it). No live gold consumer of either. **FIX: remove the stale entries from `gold_freshness_config.yaml` (lines 24/126/187-194) -> stops the comp-freshness WARN noise; no producer to fix.**
7. **eclipse** (convert_eclipse_portfolios_to_silver.py:146, unguarded) -- NOT in the 63; dispatch-tolerated (best-effort, never rc!=0, non-gating per Andrew 2026-05-15). Optional defense-in-depth guard; lowest priority.

## Legacy-dim disposition summary (Task 2)

| Dim | Disposition | Live evidence | Action |
|---|---|---|---|
| accounts_dim | DEAD producer + RESIDUAL live readers | silver/accounts_dim/latest.parquet 2026-04-29, comp-freshness FAIL | repoint residual readers -> gold dim, then decommission (P2 #5) |
| aum_snapshot | DEAD + EMPTY -> degrades dispatch freshness gate OPEN | silver/aum_snapshot/ = 0 objects | remove from check_freshness + repoint readers (P1 #4 -- LATENT HAZARD) |
| household | DEAD, superseded by household_rep_mapping | silver/api_dims/household/ 2026-05-11 (snapshot 04-28), WARN | remove stale freshness-registry entry (P2 #6) |
| gap_manifest | DEAD, orphaned (INF_09 no longer reads) | silver/meta/gap_manifest.json 2026-04-29, 234B, WARN | remove stale freshness-registry entry (P2 #6) |

**None is SLOW-CADENCE or SILENT-FAIL** -- all 4 are DEAD/RETIRED producers (`convert_orion_to_silver.py` de-wired from the chain). The hazard is not the staleness itself (non-AUA, gold-fresh) but the RESIDUAL WIRING (accounts_dim readers + the aum_snapshot freshness-gate hole).

## Net-new beyond the candidate list

1. `convert_orion_to_silver.py` -- the legacy master CSV converter; DEAD producer of accounts_dim + aum_snapshot + gap_manifest; off-chain, unguarded. Root of Task 2.
2. `build_assets_dim.py` -- retired off-chain converter (`silver/api_dims/assets/`, last 05-06, WARN); superseded by convert_assets_v2. A 5th dead silver surface.
3. `_orion_api_silver_lib.py::read_bronze_csv` (353-379) -- the shared unguarded read = the single choke covering 6 chain steps (P1 #3).
4. eclipse converter (P2 #7).
5. `reconvert_bronze_to_jsonl(_parallel)` = one-time LEG-3 bronze->bronze reformatter, NOT chain-wired -> positions_mv freshness rides the daily pull (no reconvert dependency for the guard).

## Handoff

- **[0.4.0_DS_ClientPlatform~A]** consume for the uniform-guard set. Sequence rec: (1) the shared `read_bronze_csv` guard = 6 steps at once; (2) assets_v2 :87 (chain-abort); (3) positions_mv :799 (served-AUA, N=1 honest-vintage). Metric: `ChainStepStalenessDays` keyed by Step (your genericize nit) so all guards report uniformly.
- **[1.0.0_SA_CTO]** arch-gate: the N-per-step (txn/perf N=2, positions_mv N=1) + the aum_snapshot freshness-gate-hole (P1 #4 -- a dispatch-level silent-open, may warrant its own fast-fix independent of the guard set).
- **[2.0.0_SA_COO]** the legacy-dim decommission (accounts_dim residual-reader repoint + household/gap_manifest registry cleanup) = a separate small DS work item if you want it scoped.
