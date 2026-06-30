# SEAMS: Inflection pipeline — (1) ingestion→bronze, (2) bronze→silver, (3) silver→gold

**archetype:** VALIDATE | **Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-30 ~16:15Z | Andrew-direct
**Macro target:** inflection orion-api pipeline, decomposed into 3 sequential seams. Weakest-seam-binds. Grounded vs LIVE S3 / deployed (current-day 06-30 = the sharp test).

---

## SEAM 1: Orion/Eclipse endpoints → BRONZE (scale: MESO)

**Def.** A = the pull layer (9 cron λ + the gold-EC2 inline re-pulls + the Eclipse EC2). B = bronze S3. Boundary = the HTTP pull → S3 write. Contract = raw native, all-fields, datestamped (DATA_PLATFORM catalog / INFLEC_API_ENDPOINTS_CATALOG).

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL | **PASS (today)** | bronze/orion-api/2026-06-30/ landed all dims by ~12:08Z (billing, performance_dim, tax_*, transactions, unified_account_dim, new_portfolio_accounts; reps/hhrep in -v2/); _BRONZE_COMPLETE 06-30 08:46. Eclipse bronze datestamped JSON (06-29). | — (standing fragility: the auth/JWT+OTP refresh + the Eclipse-roster dep are the latent mechanical risks — not failing today) |
| DECLARATIVE | **FAIL (layout drift)** | 3 layouts: orion-api/{date}/*.csv\|json, bronze/orion-api-v2/ (split), bronze/positions/ + bronze/assets/ (own-prefix parquet, NOT raw — bronze does a JSON→parquet conversion). Two pull layers (cron λ + inline) + duplicate pull scripts (`_v2/_dim` ↔ `_rest`). | believed "one raw datestamped bronze"; actually 3 layouts + positions/assets parquet-at-bronze + 2 redundant pull layers (the refactor SPEC-1 target) |
| SEMANTIC | **PASS** | positions_mv ties Orion to the cent; pulls land raw full-field. | — |

**Seam 1 verdict: BROKEN@DECLARATIVE** (layout/variance drift — the known refactor scope; data itself is fresh+correct today).

---

## SEAM 2: BRONZE → SILVER (scale: MESO)

**Def.** A = bronze raw. B = silver/api_dims/* (+ flat copies). Boundary = the converters. Contract = dedup+dtype only, full fidelity (Rule 17).

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL | **PASS (today)** | silver/api_dims/positions_mv/snapshot_date=2026-06-30 EXISTS — the bronze→silver conversion carried 06-30. | — |
| DECLARATIVE | **FAIL (converter drift)** | duplicate converters (transactions/performance: unified `--dim` AND standalone `_to_silver`); 3-copy dims (assets/performance across api_dims/ + flat); legacy `convert_orion_to_silver`, stray `silver/orion-rest`, `silver/accounts_dim`. | believed "one converter → api_dims"; actually sprawl + flat duplicates (refactor SPEC-2 target) |
| SEMANTIC | **PASS** | positions_mv silver 06-30 = Orion $202.13M; full fidelity (eclipse converter = `pd.DataFrame(raw)`+rename+coerce+dedup, zero slim, Rule-17 header). | — |

**Seam 2 verdict: BROKEN@DECLARATIVE** (converter/layout sprawl — refactor scope; data fresh+correct+full-fidelity today).

---

## SEAM 3: SILVER → GOLD (scale: MESO) ★ THE LIVE BREAK

**Def.** A = silver positions_mv (fresh 06-30). B = gold/canonical/holdings_{date} → INF_D_04 served total.aua. Boundary = INF_B_00 (positions_mv→holdings) + load_latest_holdings (D_04 read). Contract = current-day holdings built daily; served AUA == current-day == Orion.

| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL | **FAIL** | silver positions_mv 06-30 FRESH, but gold holdings stuck at holdings_06-29 (DS manual 17:39Z); NO holdings_06-30; pipeline-complete.json still 06-29 14:35Z. The fresh silver is NOT carried to gold. | the silver→gold producer (INF_B_00) did not run-to-current-day; gold frozen at 06-29 while silver advanced to 06-30 |
| DECLARATIVE | **FAIL** | `load_latest_holdings()` (name implies "latest") silently picks the max-date partition = stale T-1 when current-day is missing; no fail-loud. TO-2 fixed the clobber, NOT this. | believed "serves latest"; actually serves newest-EXISTING (= stale T-1) with no guard |
| SEMANTIC | **FAIL** | served total.aua = stale T-1 ($202,711,894.29) vs Orion $200,987,115.59 — +$1,724,778.70 (+0.86%) wrong. | wrong value (stale-vintage; right shape, wrong number) |

**Seam 3 verdict: BROKEN@MECHANICAL + DECLARATIVE + SEMANTIC.**

**MECHANISM (grounding: SOURCE-CONFIRMED — eventbridge.tf:164 `mode=full` + CHAIN_FULL order PERF(pos1)<POSITIONS/B_00(pos9/11) + AE hang ground-truth 103/41min, DS~A 160944Z, CVO-verified):** the scheduled nightly is `--chain FULL` (NOT incremental — my earlier premise refuted). The full chain HANGS on the inline `pull_inflection_performance_rest.py` (which sits BEFORE positions/B_00) → the chain dies before INF_B_00 → no current-day gold holdings. The deployed timeout-tolerate is the durable fix.

**Cross-connection (grounding: SOURCE-CONFIRMED — commit `9ea447b3a` + live):** the fix commit names it verbatim: *"the persistent `pull_inflection_performance_rest.py` hang (103min then 41min on Orion perf endpoint, BEFORE positions in CHAIN_FULL) was blocking B_00 under set -e ... **Tolerate falls back to cron-landed fresh bronze**."* This confirms: (1) the hang IS the gold chain's INLINE perf RE-pull (`_rest`); (2) it's before positions/B_00; (3) the fix's fallback is the CRON-landed bronze → i.e. **the inline pull is redundant with the cron pull**. The per-request `timeout=REQUEST_TIMEOUT_S` in the script was insufficient (endpoint-level hang); the dispatch-level `timeout(-k30,600s)` wrap is the tactical fix. **=> SPEC-1's single-pull-layer is PROMOTED from cleanup to a STRUCTURAL durable fix** — remove the inline re-pull entirely and the chain reads cron bronze (exactly what timeout-tolerate does as a fallback), eliminating the hang locus rather than time-boxing it.

**LIVE STATE (re-checked, current):** timeout-tolerate DEPLOYED ~16:07Z (`9ea447b3a`) + a fresh chain dispatched — BUT the recovering chain has NOT yet landed a fresh served artifact. RIGHT NOW: gold still `holdings_06-29` (manual), pipeline-complete still 06-29 14:35Z, **served header still the 06-29 22:07Z 132B stub** (`data_as_of 06-29`, total_aua $202,582,215.84). The break is STILL LIVE; the fix is deployed-not-landed (deployed != resolved). CVO co-sign withheld until the recovered chain produces a current-day partition + a RICH served header == Orion to the cent (value-parity exact).

---

## MACRO VERDICT (weakest-seam-binds)

Inflection pipeline = **BROKEN @ the silver→gold seam.** Bronze + silver carry fresh, correct, full-fidelity data through 06-30 today; the break is entirely the silver→gold joint (gold frozen 06-29, served +$1.72M stale). Seams 1+2 are SOUND on data (their DECLARATIVE FAILs are the known refactor-scope variance, not a data break). The refactor specs address all of it: SPEC-1/2 the declarative variance; SPEC-3 the silver→gold break (timeout-tolerate + load_latest fail-loud + the value-parity gate).

## Knowledge-parity delta
- Corrected on the record (this session): the silver→gold break mechanism is the FULL-chain perf-hang (not incremental-skip — my refuted premise), and TO-2 did NOT fix the value defect (clobber only). The stale-partition is LIVE today (06-30 gold not produced).
- Routed: G-R1 reconciliation to COO/CTO (parked Part-1, Part-2 ships); the perf-hang/timeout-tolerate is the owner's durable fix.

## Residual / unknowns
- Does a NON-hanging full run build current-day (T) holdings or T-1? (06-29: B_00 wrote through 06-28 only.) The acceptance bar verifies it.
- The auth/OTP refresh (Seam-1 standing fragility) not exercised here — covered by SPEC-4.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| live S3 (06-30 bronze/silver/gold landing + version forensic) | the sharp current-day per-seam test | PASS (rail-checked) |
| eventbridge.tf:164 / CHAIN_FULL order / git show TO-2 | SOURCE-CONFIRM the silver→gold mechanism | PASS |
| (prior session) endpoint catalog, converter audit, holdings partition sums | the contract + semantic baselines | PASS |

— 3.0.0_SA_CVO
