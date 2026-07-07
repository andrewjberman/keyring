# Session (cont.) — DI-1 D-stage TTM fix + DI-7 close via account_type false-premise catch + M1 reroute + dispatch guard — lane B

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, COORDINATE, VALIDATE

**Serial:** 0.4.0_DS_ClientPlatform~B
**Window:** ~0000Z -> ~0224Z 2026-07-07 (delta since prior log 5191614d4)
**Commits:** 9f0235d16 (M1 reroute), 63b0a34c8 (dispatch guard), 121d22bfd->reverted-portion, c3e8b1a93 (A_00 un-freeze revert), 6d69a7bf3 (DI-7 D_00 account_type fix)

## Summary
Continuation of the INF tax-panel work. Five threads landed, the headline being a Rule-22 grounding catch that turned an hours-old false premise into a simpler+fresher+more-accurate one-line fix.

### DI-1 D-stage capital_gains_ttm (CVO P1) — CLOSED, CVO-cert
CVO caught my DI-1 C_03 re-point left a MIXED-BASIS TTM: C_03 made unrealized native 07-06-FORWARD only; history stayed phantom-derived, so capital_gains_ttm (365d delta from account_performance) straddled the re-point cliff -> served $101,377,008 (7.6x the $13.3M unrealized). My "self-heals nightly" belt was WRONG.
- FIX (CTO-ruled, no code change): ONE-TIME full-rebuild of INF_C_03 account_performance (INFINC_REBUILD via --rebuild flag) -> recomputes unrealized_gain native per (date,account_id) from tax_unrealized across ALL history. My C_03 code already does the per-date native join.
- GROUNDED: historical tax_unrealized is GENUINE as-of (total_gain_loss varies 2025-07-03 $8.97M -> 07-06 $13.29M, 2103 daily partitions 2020-fwd), so the backfill produces meaningful native-native TTM.
- 0.6.1 ran --single INF_C_03 --rebuild (after 2 dispatch-error retries: stray code/bronze M1 copy sync-collision + INFINC_REBUILD env clobbered by dispatch:1247) then gold-d. VERIFIED: served capital_gains_ttm $101.4M -> $4,450,438 native-native; account_performance single-basis (07-02 $174M phantom -> $13.22M native, no cliff, 1.3M rows/2485 dates). CVO exercise-gate PASS.

### DI-7 tax-status — CLOSED (served-verified, closing on CVO cert) via a FALSE-PREMISE catch
My earlier DI-7 a1 (frozen silver/accounts_dim reg_type rejoin) gave 9.56% fallback (WARN_HIGH_FALLBACK), accepted as "honest frozen-source." COO queued the A_00 reg_type "un-freeze" as the durable.
- RULE-22 CATCH: grounding the un-freeze source, I found the CURRENT fresh accounts_dimension already had genuine tax_status (204/250/414, NOT collapsed) and accounts_v2.account_type LITERALLY CONTAINS the genuine reg-type vocab (IRA 304/Roth 199/TOD.../0 null/868, identical to registrationCode). The premise "account_type is not a genuine registration type" was NAME-based and FALSE. Halted the A_00 --single before it ran (0.6.1 held clean, zero fired). CTO re-grounded + REVERSED (I was right).
- REAL fix (CTO-ruled minimal): the DI-7 collapse was D_00.load_accounts_dim DROPPING reg_type from its out-frame (a column-drop/silent-default, invariant #1), NOT a bad source. FIX = one line `out['reg_type']=df['account_type']` at the drop-point. Removed the a1 _join_reg_type_from_silver + SILVER_ACCOUNTS_DIM_KEY (frozen-dep GONE). Sentinel-degrade guard + data_quality + D_04 passthrough KEPT.
- COND-2 exercise-verified on live: 0.23% fallback (2 Invalid Type), buckets 204/250/414 (count) / 27.2/64.2/8.7 (AUA). SERVED-VERIFIED both surfaces: clients_tab.json (D_00) + clients-tab-slim.json (D_04) = 27.19/64.15/8.66, fallback 0.0023, data_quality OK, capital_gains held $4.45M. The 81 post-04-29 onboards a1 mis-defaulted to taxable now correctly classified.
- A_00 un-freeze REVERTED (c3e8b1a93) -- lateral swap on the false premise, nothing run.

### Perf-pull M1 (reroute) — COMMITTED
DS base offline -> COO re-routed 0.6.1's CTO-validated M1 patch to me (live INF DS lane). Applied ADVI_INFPERF_M1_incremental_perfpull.patch via git apply --3way (base drift from 94042ebf1, merged clean, NOT --force). ds-gate clean. Commit 9f0235d16. Handed to 0.6.1 for the full-312 pre-deploy gate. Caught + unstaged a stray pre-staged org/mcp/reap_lib.py (flagged to MSTR via COO).

### Dispatch silent-rebuild-trap guard — COMMITTED + DEPLOYED
0.6.1's Error-2 root: orion-gold-dispatch.sh:1247 clobbers env-set INFINC_REBUILD to $REBUILD (0 without --rebuild) -> a rebuild-intent silently ran as append. My POD4 lane. FIX (Option B, WARN-loud not fail-closed): loud WARN before the clobber when INFINC_REBUILD env-truthy AND --rebuild omitted; keeps the flag canonical + stale-env protection, no re-exec/nightly break risk. Commit 63b0a34c8; 0.6.1 deployed to code/gold (sha 4ffe58d9, single-homed, EC2-idle, MATCH).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-blast | account_performance / accounts_dimension / build_firm_tax_block | PASS | DI-1-Dstage C_00-undisturbed (C_00 not an account_performance consumer); A_00 77-consumer value-only |
| comp-pipescript io | INF_A_00, INF_D_00 | PASS | D_00 reads accounts_v2 directly; A_00 write->17 consumers |
| ds-commit-gate | all touched .py | PASS | clean all |
| bash -n | orion-gold-dispatch.sh | PASS | dispatch guard syntax |
| (read-only diagnostics) | tax_unrealized as-of / account_type values / vocab-match | PASS | Rule-22 grounding: genuine-as-of history + account_type genuine + 0.23% exercise |

**What worked:** comp-blast confirmed both the C_00-undisturbed (DI-1-Dstage) and the A_00 value-only (77-consumer) safety. Read-only diagnostics were the decisive Rule-22 grounding tool throughout (caught the false premise + proved every fix pre-deploy).
**What failed:** subprocess `aws` on Windows (verifiers run inline via bash aws|python instead). comp-pipescript deployed still no inf-tree coverage.
**Gap found:** the account_type false premise held multiple agents + CTO for hours BECAUSE nobody value-grounded the field (reasoned from the name). Banked: value-ground a source before accepting a source-quality premise, even a CTO's.

## Deployment Sequence + Verification
- DI-1-Dstage: 0.6.1 --single INF_C_03 --rebuild @01:36Z + gold-d -> capital_gains_ttm $4.45M verified.
- DI-7: A_00 revert (c3e8b1a93) + D_00 fix (6d69a7bf3) deployed code/gold ETag-MATCH -> gold-d @02:18Z -> clients_tab + slim verified (27.19/64.15/8.66, 0.23%, OK).
- M1 (9f0235d16): committed, deploy = 0.6.1's pre-deploy gate.
- dispatch guard (63b0a34c8): 0.6.1 deployed code/gold.

## Blockers
None (mine). Awaiting CVO's DI-7 exercise-gate cert (peer, not a block) + 0.6.1 D-stage chain-complete confirm.

## Current State
- DI-1 (PIT) + DI-1-Dstage (TTM) + DI-7 (tax-status): all served-correct + verified. DI-7 closes on CVO cert.
- DI-7 served: clients_tab.json + clients-tab-slim.json = taxable 27.19% / deferred 64.15% / free 8.66%, fallback 0.23%, data_quality OK, capital_gains_ttm $4,450,438. accounts_dimension genuine (account_type-sourced, A_00 restored via revert).
- Frozen silver/accounts_dim dependency REMOVED from the INF tax lineage (a1 retired). tax_unrealized is the unrealized-gain source (C_05/C_03); account_type is the tax-status source (A_00/D_00).
- M1 committed (9f0235d16), with 0.6.1. Dispatch guard live (63b0a34c8).

## Next Steps
1. **[3.0.0_SA_CVO]** DI-7 account_type exercise-gate cert (served 27.19/64.15/8.66, 0.23%, OK) -> DI-7 tax-axis fully closed.
2. **[0.6.1_AE_PartnerETL]** D-stage chain-complete confirm (EC2 auto-stop, no FATAL); M1 full-312 pre-deploy gate + nightly cutover.
3. **[0.4.0_DS_ClientPlatform~A]** REPOINT-COMPLETE household repoint (parallel; A_00 reg_type axis is CLOSED via account_type, no longer needs the un-freeze).
4. **[0.4.0_DS_ClientPlatform~B]** (self, durable, non-gating) D_00/D_02 pre-2020 honest-null guard for TTM windows below tax_unrealized coverage (CTO-agreed defer).
