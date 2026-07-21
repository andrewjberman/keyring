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

---

## 5. CORRECTION -- Andrew reframe: it is FIELDS, not scripts (the refactor's whole point)
The v1 had 21 scripts because it accreted patches/cruft; the v2 goal is to serve the FIELDS Group D consumes, efficiently, from the canonical silver -- NOT to re-port the sprawl. Re-run at the FIELD level, the "gaps" above mostly dissolve -- the fields already exist in the silver or the A+C spine:

**The advisor-ROLE decomposition (the biggest apparent gap) is ALREADY INGESTED + RESIDENT -- this is exactly what OPAL_ASSETS_49METATABLES was designed for (Andrew-confirmed).**
- Table: **`opal-data-assets/blackdiamond/49f/silver/dim_advisor_fee_role/`** (SCD2, per-row provenance), producer `data/assets/scripts/silver/bd49f_dim_conversion.py`.
- Ingest source: `blackdiamond/49f/bronze/allocation_390224/{date}/data.xlsx` (the D1a "Allocation_Template 390224" BD REST pull -- roles+splits+fee block).
- Emits the FULL decomposition: **architect / implementor / consultant / local_ops / additional_advisor** + splits + fee -- the exact fields all 8 D publishers read.
- **LIVE:** bronze + silver both landing on trading days through `date=2026-07-20` (T-1; 07-18/19 = weekend). Grain-guarded (role/split constant-within-account, GrainConflict refuses).
- **Already wired:** `a00_runner.py:15,45` joins `dim_advisor_fee_role` as join-dim-2.

**Field-level coverage (corrected):**
| D field group | v2 source | Status |
|---|---|---|
| advisor roles (architect/consultant/implementor/local_ops/additional_advisor) + splits + fee | silver `dim_advisor_fee_role` (49METATABLES, LIVE), joined by a00 | INGESTED -- last mile = EMIT in the gold dim contract D reads |
| account_id / relationship_id / advisor | a00 / a01 | present |
| account/client performance, total_aua | c01 / c02 | present |
| AUA decomposition: market_growth / income / fees | c00 | present |
| NNA: daily_inflow / daily_outflow / nna_txn | c03 | present |
| holdings/composition: market_value / cusip / quantity | silver `fact_position` (`data/canonical/schwab/silver/build_fact_position.py`) | present in silver; ticker/asset_name via a cusip->security bridge; is_open derivable -> composition buildable from silver, no B_00 cruft |
| synthetic_correction / churn / aua_residual_sum | not in c00 | small field-add OR D-derivable from market_growth+flows -- confirm |
| xref bridge | silver `dim_account_xref` (LIVE, date=2026-07-14+) | present |

**Corrected verdict:** at the FIELD level the estate already provides nearly everything Group D needs -- the role/fee decomposition is live-ingested (`dim_advisor_fee_role`) and joined by a00, holdings fields are in silver `fact_position`, and the performance/NNA/dim fields are in A+C. The refactor premise HOLDS: D can be rebuilt efficiently from the canonical silver + the A+C spine **without** porting v1's ~14 extra scripts. The real remaining work is **last-mile field-emit in the gold dim/cohort contracts** (surface the role columns a00 already joins; add a cusip->ticker bridge for composition) + confirm synthetic_correction/churn -- NOT a script-porting effort. My section-2 "unported scripts = gaps" framing is SUPERSEDED by this.
