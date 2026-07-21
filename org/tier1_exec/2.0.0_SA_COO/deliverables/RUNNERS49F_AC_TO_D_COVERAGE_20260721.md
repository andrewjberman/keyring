# 49F runner -- Group A+C -> Group D coverage check (Andrew-direct, 2026-07-21)

**By:** 2.0.0_SA_COO~A (read-only verification; Andrew asked "test compile end to end + see if A+C serve everything Group D needs"). No writes, no runs -- py_compile + static read of the D publishers' inputs vs the A+C outputs.

## 1. Compile -- PASS (15/15)
`py_compile` on every script in `data/assets/scripts/gold/runners_49f/`:
a00_dim_account, a00_runner, a01_dim_relationship, a01_runner, c00_account_gains, c00_runner, c01_account_performance, c01_runner, c02_client_performance, c02_runner, c03_nna, c03_runner, c04_recon_guard, dryfit_driver, fit_harness -> **OK=15 FAIL=0.** (Syntax/parse clean; a full import needs pandas/pyarrow + the silver inputs, out of scope for a compile check.)

## 2. Coverage -- PARTIAL. Core spine covered; Group B + several C-series unported.
The original 49F gold runner (`data/black_diamond/scripts/gold/`) is ~21 scripts: A_00-A_04 (dims), B_00-B_03 (holdings/lots), C_00-C_08 (metrics). The new runner ports **7**: a00<-A_00, a01<-A_01, c00<-B_03 account_gains, c01<-C_03 account_performance, c02<-C_02 client_performance, c03<-C_01 canonical_nna, c04<-C_04 validate_aua. The **8 Group D publishers** (`D_00 ... D_04`) read the gold tables below.

### Covered -- the core spine A+C DOES serve
| Group D reads | Producer (seed) | Ported? |
|---|---|---|
| account_performance | C_03 | YES -> c01_account_performance |
| client_performance | C_02 | YES -> c02_client_performance |
| account_gains / AUA decomposition | B_03 | YES -> c00_account_gains |
| canonical_nna (atomic/daily) | C_01 | YES -> c03_nna |
| dim_account / accounts_dimension | A_00 | YES -> a00_dim_account |
| dim_relationship / advisor_assignments | A_01 | YES -> a01_dim_relationship |

### GAPS -- Group D reads these, NO A+C script produces them
| Group D reads | Producer (seed, UNPORTED) | D consumer + impact |
|---|---|---|
| **canonical_holdings / holdings_lots** | **B_00 / B_01 / B_02 (all of Group B)** | **HARD GAP.** `D_03.composition_artifacts:576` `holdings_key = _find_latest_holdings_lots(); if not holdings_key: return` -> **composition surfaces cannot be built at all** without holdings. |
| **canonical_role_aua** | **C_01b / C_01c (role_aua backfill + flow-join)** | SOFT. `D_00b.portal_timeseries` loads `CANONICAL_ROLE_AUA_PREFIX`; absent -> `WARN ... fallback to local-compute` (heavier + loses the 49F advisor-role decomposition fidelity). Also read by D_00c, D_01. |
| **account_team** | **C_07.advisor_attribution** (`_write(acct_team, ...)`) | SOFT. `D_00.portal_aggregates:387` loads `ACCOUNT_TEAM`; absent -> `:389` fallback derives a thin account_team from the accounts dim (loses the attribution architecture). |
| **fee_rate_history / fee splits** | **A_02.fee_rate_history / C_08.advisor_fee_efficiency** | SOFT. `D_00.portal_aggregates:339` loads `FEE_RATE_HISTORY`; absent -> `:344 WARN ... fee splits will be null`. The 49F split-fee layer renders NULL. |
| client_tax_liability | C_05 | tax surfaces (D_04) |
| client_mix_timeseries | C_06 | mix/timeseries + composition |
| positions_cube | A_03 | feeds holdings/composition |
| canonical_performance (base) | C_00 | check vs c01/c02 supersession |

## 3. Verdict
- **A+C compile and are internally sound.** They faithfully cover the **performance + NNA + identity-dim spine** (the fit_harness proves *that* subset to the cent).
- **They do NOT yet serve everything Group D needs.** The sharpest is **all of Group B (holdings/lots) is unported, and `D_03` composition HARD-RETURNS without it.** role_aua, advisor attribution/account_team, and the fee layer are unported too -- D degrades to fallbacks / nulls, not full fidelity.
- **This is why the A3 dry-fit used a SHIM** (recorded "coverage MATERIALLY LOW", 997 dropped-and-counted): the shim stood in for exactly these unported pieces. The 4.1M-field cent-parity is real *on the covered surfaces*; the coverage is incomplete.

## 4. What it means for finalizing the runner (B)
To have A+C serve a re-pointed Group D end-to-end, the remaining port/re-source work is:
1. **Group B holdings** (B_00/B_01/B_02) -- either port them, or re-source `canonical_holdings` from the monolith silver `fact_position` (c00 already reads `dim_position` for market value, so the silver is there; the served holdings table is not). **Blocks composition (D_03) outright.**
2. **role_aua** (C_01b/C_01c) -- the 49F advisor-role AUA decomposition (leaderboard/timeseries/partner-analytics fidelity).
3. **advisor attribution / account_team** (C_07) + **fee layer** (A_02/C_08) -- attribution + fee-split surfaces.
4. **tax (C_05), mix-timeseries (C_06), positions (A_03)** -- remaining composition/tax/timeseries feeds.

Grounded: `data/assets/scripts/gold/runners_49f/` (7 scripts) vs `data/black_diamond/scripts/gold/{A,B,C,D}_*.py`; hard/soft classified from the D scripts' own load-or-fallback branches (line-cited above).
