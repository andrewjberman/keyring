# SEAMS: this session's shipped FE work -> live data + system  (scale: MACRO, decomposed)
**archetype:** VALIDATE
**by:** 0.4.0_DE_ClientPlatform · **2026-06-16 ~2035Z** · scope: TO-3 TTW (700ec9b4), TO-1 Global-SI (a447712b), ADVI Demo-default (8f564d42), + type-parity repair (a344b2bd)
**Grounding:** origin/DEV (pushed/shipped state, fetched + read via `git show origin/DEV:`) + the SERVED S3 artifacts (mpb_ttw.json 19:14Z, agg.json 18:37Z) + the deployed auth-gate mechanism. NOT local working tree, not self-report.

## OVERALL VERDICT: SOUND (decision-honest) — 1 type-parity gap FOUND & FIXED (a344b2bd); 1 deep-tail reconciliation residual FOUND (by DS~A's independent /seams, I CONFIRMED) — demarcation-mitigated, REFINE routed to COO; render residual deferred to promote smoke. See ADDENDUM.

---

## Seam group 1 — TO-3 TTW (700ec9b4)

### Seam 1a: served `model_portfolio_benchmarks.json` returns['TTW'] -> ModelPortfolios transform -> BenchmarkHeatmap
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | origin/DEV BenchmarkHeatmap: ALL_PERIODS has 'TTW' (L54), PERIOD_DATA_KEY['TTW']='TTW' (L75, 1:1), FIXED_PERIOD_TRADING_DAYS['TTW']=10 (L95). Served mpb (19:14Z) carries returns['TTW'] full field set. Page transform L710 generic (`Object.entries(model.returns)`) -> TTW passes to both index+ETF modes. |
| DECLARATIVE | PASS (post-repair) | FE key 'TTW' == producer key 'TTW'. Type gap FOUND: BenchmarkModelData.returns omitted 'TTW' -> FIXED a344b2bd (type now declares it). |
| SEMANTIC | PASS | TTW = total-return tail(10); my independent Phase-3 recompute matched served 0.004pp (5/5 models); AE confirmed total-return basis (index legs decisive); net proration 10/252. |

### Seam 1b: same served -> ReturnVolatilityScatter (return+vol toggle)
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | origin/DEV: ALL_PERIODS 'TTW' (L49) + PERIOD_DATA_KEY 'TTW':'TTW' (L56). Scatter reads periodData.model/model_volatility/benchmark/benchmark_volatility -> served TTW has model_volatility (1.06) + benchmark vols. |
| DECLARATIVE | PASS (post-repair) | type parity repaired (a344b2bd). |
| SEMANTIC | PASS | TTW vol present + total-return basis; same period data as the heatmap (one source). |

## Seam group 2 — TO-1 Global since-inception (a447712b)

### Seam 2a: served `aggregate-aua-timeseries.json` (sma_aua-free, floor 2024-11-01) -> globalMdpfData -> growth chart x-axis
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | origin/DEV has isGlobalSI gate; Global value path uses globalMdpfData (verified agg.json = 413 dates from 2024-11-01); rolling-1y filter gated OFF for Global -> full SI range; per-firm filter retained. |
| DECLARATIVE | PASS | sma_aua?: optional matches served-absent field; non_model_aua carries the fold. |
| SEMANTIC | PASS (demarcation-mitigated) + DEEP-TAIL RESIDUAL | per-firm UNCHANGED; Global extends to floor; DS never-widen $0. **BUT** the Global Non-Model BAND sources from non_model_assets.json (enterprise_total basis), NOT globalMdpfData.non_model_aua — so in the deep tail the band (old basis) + model bars (new .031 basis) overshoot opal_aggregate_aua by +22.38M/+2.88% @ 2024-11-01, -> $0 from 2026-01-14. Decision-HONEST (entirely inside the estimate-basis demarcation) but a real mixed-basis imperfection. See ADDENDUM. |

### Seam 2b: estimate demarcation ReferenceArea (boundary MDPF_ESTIMATE_BASIS_END='2026-01-16') vs served provenance
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | ReferenceArea on BOTH charts, Global-gated, est = fullDate/period < '2026-01-16'. |
| DECLARATIVE | PASS | boundary matches served meta.backfill_methods split (.031 2024depth pre-01-16 = estimate; .029 rps_calibrated from 01-16 = measured; idx 309). |
| SEMANTIC | PASS | estimate region = Nov2024->Dec2025 (clean monthly/quarterly boundary); estimate never renders as measured (shade + 'Estimated' label + footnote + SI helptip). |

### Seam 2c: sma_aua fold removal (per-firm path) value-preservation
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | L831/L893 now non_model_aua only; DS~A independently confirmed value-preserving (deployed non_model_aua=1b'=old nm+old sma; old +sma_aua was +0). |
| DECLARATIVE | PASS | type optional; cohort_class='sma' by_model filters retained (no double-count). |
| SEMANTIC | PASS | band value byte-unchanged (mutual DS+DE confirm). |

## Seam group 3 — ADVI Demo-default (8f564d42)

### Seam 3a: useAuth().user.email -> ADVI_DEFAULT_BY_EMAIL -> selectedFirmId -> PARTNER_VIEWS['demo'] -> DemoAdvisorIntelligence
| Axis | Verdict | Evidence |
|---|---|---|
| MECHANICAL | PASS | origin/DEV has map (L43) + `user` destructure (L48) + useState init from user?.email.toLowerCase() (L52). 'demo' valid (ALL_PARTNER_FIRMS L27 + PARTNER_VIEWS.demo->DemoAdvisorIntelligence L34 = real view). **Race check (sharp):** ProtectedRoute gates children behind `isLoading` + `isAuthenticated` (ProtectedRoute.tsx:24-31) -> user hydrated BEFORE ADVI mounts -> useState-init-once captures the real email. Worst-case (user null) degrades to '49financial' (safe). |
| DECLARATIVE | PASS | useAuth exposes user (AuthContextType extends AuthState, L53; AuthState.user L46; User.email L16); 'demo' a documented first-class firm. |
| SEMANTIC | PASS | Patricia->demo, all other internal->49F (default-only, switchable); external users unaffected (selectedFirmId internal-gated L45); `.toLowerCase()` defensive on case; AE login-verified the backend (opal-users-v2 firmId=opal-capital). |

## Knowledge-parity delta
ONE drift found + FIXED this pass: BenchmarkModelData.returns + ModelPortfolioData.returns omitted the 'TTW' key
(type lagged the shipped TO-3 FE + the served TO-4 producer; worked via the `as keyof` cast + generic transform,
but the type lied-by-omission). Repaired a344b2bd -> type now == served reality + FE usage. ETFBenchmarkData.returns
intentionally left without TTW (etf_returns.json has none; ETF mode reads etf_benchmark from the comprehensive file).
Everything else: believed == true (committed==pushed across all 4 commits; data seams match; auth-gate mechanism holds).

## Residual / unknowns
- **Browser render / live login NOT exercised** (the one consistent gap): I verified all seams at the CODE
  (origin/DEV) + DATA (served) + TYPE + AUTH-GATE-MECHANISM level — strong evidence — but did not run a browser
  smoke (CLI can't auth the demo tenant; portal dev-server+auth detour deferred). So: the TTW toggle/column render,
  the demarcation shade pixels, and an actual Patricia-login landing on Demo are EVIDENCED-not-EXERCISED ->
  deferred to the DT-promote visual smoke / Andrew (matches the ride-normal-cycle call). None can produce wrong
  VALUES (those are verified); the residual is render-correctness only.
- .X_ETF deep-value basis (model/ETF legs total-return) = AE high-confidence, routed to CVO value lane (non-gating, §5-moot).

## Compiler Tools
| Run | Result |
|---|---|
| git fetch origin DEV + `git show origin/DEV:<path>` (3 files) | committed==pushed; all TTW/SI/ADVI edits present on origin/DEV |
| tsc -b --noEmit --force (x2: post-ADVI, post-type-repair) | PASS exit 0 |
| safe-commit surface-check (ADVI + type-repair commits) | SEV1 advisory (advisor_intelligence / model_portfolios.benchmark) — value-safe |
| aws s3 (mpb_ttw / agg) + python parity (prior turns) | served TTW present + Phase-3 0.004pp; aggregate sma_aua-free + 2024-11-01 floor |
| read ProtectedRoute.tsx + AuthContext.context.ts | auth-gate holds children behind isLoading+isAuthenticated; user/User.email on the type |
| aws s3 cp non_model_assets.json + python reconcile (ADDENDUM) | CONFIRMED DS deep-tail finding to the dollar |

---

## ADDENDUM (post-report) — deep-tail Non-Model band reconciliation (Seam 2a SEMANTIC)

**Source:** DS~A's independent /seams on the TO-1 chain (logs/2026-06-16/seams_1905Z...) caught a semantic seam MY pass missed — I verified the band's presence/shape but did NOT reconcile model+band vs total in the deep tail. The value of an independent second pass.

**Independently CONFIRMED** (agg.json globalMdpfData + non_model_assets.json, served): the Global stacked-chart Non-Model band reads `non_model_assets.json` `non_model_aum` (enterprise_total basis), while the model bars read globalMdpfData `model_aua` (opal_aggregate_aua / .031 re-derive basis). Deep-tail mixed-basis overshoot:
- 2024-11-01: model 353.80M + band 444.74M = 798.54M vs total 776.17M -> **+22.38M (+2.88%)**
- ~+23M (2.3-2.9%) through the deep tail; **EXACTLY $0.00 from 2026-01-14** on (the calibration boundary).
- Cause: non_model_assets' deep-tail enterprise_total (798.54M) was not re-derived to the .031 basis; converges with opal_aggregate_aua at calibration.

**Disposition:** DECISION-HONEST — sits entirely inside the shipped estimate-basis demarcation (<2026-01-16 shaded + "not calibrated" footnote), so it does not mislead. NOT a correctness bug. It IS a real mixed-basis imperfection my SI extension exposed (the 1y cap previously hid it).
- **REFINE option (routed to COO 204927Z, my rec):** in the <2026-01-16 region, re-source the band from globalMdpfData (`opal_aggregate_aua[i] - model_aua[i]`) -> deep-tail stack reconciles to total by construction + shares the model-bar basis. Keep non_model_assets for >=2026-01-16 (already reconciles to $0). Value-affecting on the model_portfolios SEV1 surface -> COO accept/refine call; I implement same-turn on GO (DS supplies field path). NON-GATING for TO-1/TO-3 (both accepted; this is deep-tail-band polish).

**Verdict impact:** overall stays SOUND (decision-honest via demarcation); Seam 2a SEMANTIC carries this documented deep-tail residual pending COO's accept/refine.
