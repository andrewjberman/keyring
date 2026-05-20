# SSCN_DIVDEF.003 — DIVZ Preset Empirical Validation + Group Taxonomy Doc

| Field | Value |
|---|---|
| Agent | `0.3.0_DS_TradingOperations` |
| Date | 2026-05-19 |
| TO | `SSCN_DIVDEF.003.ds-divz-preset-empirical-validation-and-group-taxonomy-doc.md` |
| PRD | `docs/architecture/SSCN_DIVDEF.md` v0.1 commit `a5e1b7ef4` + v0.2 amendment commit `c34f16d13` |
| Status | **RAVC2 BLOCKED** — 3 AC failures surface to COO~B + CTO~B for adjudication; doc + script + CSV uncommitted pending path forward |
| Project | SSCN_DIVDEF (Security Scanner DIVZ Default Preset + 2026-05-18 Data Refresh) |
| Pod | 3 — TradingOperations |
| Dispatch chain | COO~B STAGED 15:26Z → COO~B pre-stage AUTHORIZED 15:29Z → COO~B EXTEND HOLD on split-vintage 15:43Z → CTO~B Path 2+1 ruling 15:47Z → COO~B PRD v0.2 RATIFY 16:44Z → COO~B GO direct 18:30Z (Andrew "proceed what you can" auth; DT 0.3.0 on P0 PM fix) → DT 0.3.0 belt-and-suspenders GO CC 18:32Z → DS Phase 2 execution |

## Objective

Validate the DIVZ-style 13-factor preset against the freshly-overwritten 2026-05-18 R1000 vintage produced by Lambda `security-scanner-v1.1.1`. Acceptance criteria AC1-AC6 from TO body §scope.

## Briefs Written

None this session. The new `SSCN_GROUP_TAXONOMY.md` doc IS the AC4 deliverable; routed at doc-commit-time post-adjudication.

## Work Completed

### Phase 1 (pre-stage, COO~B pre-GO authorization 15:29Z)

- Direct read of `infra/aws/lambda/opal_security_scanner_processor/factor_metadata_registry.json` (284 factors total).
- Extracted `category` + `relationship` + `name` per code for all 13 DIVZ preset codes.
- Cross-checked `relationship` field against PRD §6 anchor: **13/13 PASS** — registry agrees with FactSet semantics anchor.
- Authored skeleton at `docs/architecture/security-scanner-source/SSCN_GROUP_TAXONOMY.md` covering §1 rationale + §2 4-group↔registry-category mapping + §3 future-preset-author guidance (5 subsections) + §4.1 Phase 1 transcript + §6 provenance + §7 references.
- Added §3.6 universe-set selection note under COO~B PRD v0.2 ratification (covers 3-layer architecture + 3-step gate for new-universe presets + empirical 2026-05-19 v0.1→v0.2 anchor).

### Phase 2 (post-GO, COO~B direct GO 18:30Z + DT 0.3.0 CC 18:32Z)

- Pulled `s3://opal-data-portal-v2/json/security_scanner/latest/universes/r1000/scanner_data.json` (17.05 MB, LastModified 2026-05-19T18:27Z, 1005 rows, 284 pctls codes per row).
- Pulled `s3://opal-data-portal-v2/json/security_scanner/latest/factor_metadata.json` (68.5 KB, `.asOf == "2026-05-18"`).
- Pulled `s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/Screening_DIVZ_IDVZ_20260518.xlsx` (6.93 MB, for AC3 `wt_iwb` column extraction since wt_iwb is not exposed in scanner_data.json row payload).
- Authored `.runtmp/sscn_divdef_003_validation.py` (analysis script; AC1+AC2+AC3+AC5+AC6 single-pass run).
- Ran AC1/AC2/AC3/AC5/AC6 empirical validation. Wrote CSV `C:/Users/AndrewBerman/AppData/Local/Temp/sscn_divdef_top100_composite.csv` (100 rows: rank, ticker, composite_score, wt_iwb, name, null_codes).
- Filled all 21 TBD stubs in SSCN_GROUP_TAXONOMY.md with empirical data + FAIL annotations.
- Added §8 RAVC2 BLOCKED escalation section to SSCN_GROUP_TAXONOMY.md with per-failure root-cause + adjudication options.

## AC1-AC6 Results

| AC | Result | Detail |
|---|---|---|
| AC1 per-code pct non-null >= 90% (R1000, 13 codes) | **FAIL (12/13 PASS)** | `dps_gr_1yr` 67.06% (331/1005 R1000 stocks non-dividend-paying → growth structurally undefined when prior=0; sample: AMZN/META/GOOGL/TSLA/BRK.B/GOOG/NFLX/CRM/ADBE/AMD). Other 12 codes 95.32%-100.00%. |
| AC2 KS D<0.10 OR 10-bucket equal-count (13 codes) | **FAIL (12/13 PASS)** | `dy_ntm` KS_D=0.139 + bucket skew (270 of 975 stocks in [10,20) band; 0 in [0,10)). Root cause = 270 R1000 stocks with raw `dy_ntm=0` all tied at pctls=13.897 (`rank(pct=True, method='average')` semantics). Other 12 codes KS_D in [0.0010, 0.0868]. |
| AC3 top-rank composite >= 70.0 | **FAIL** | MO (Altria) at 68.65 vs threshold 70.0 (1.35-pt gap). DIVZ 4-group blend (40 Div / 30 Mom / 15 Val / 15 Qual) caps the diversified composite below 70 even for paradigmatic dividend names. |
| AC3 bottom-rank composite <= 40.0 | PASS | NOW (ServiceNow) at 31.13 (8.87-pt margin). |
| AC3 spread (informational) | — | 37.52 pts top-to-bottom; tilt directionally correct (dividend-payers high, growth-tech low). |
| AC5 inverse-class 3-ticker direction (4 codes × 3 tickers = 12 rows) | PASS (4/4) | `accruals_bs`/`leverage`/`short_pct_chg_12m`/`days_to_cover` all show HIGH-pctls raw < LO-pctls raw (sign-flip wired through Lambda correctly). |
| AC6 .asOf == "2026-05-18" | PASS | jq `.asOf` returns `"2026-05-18"` (cross-confirmed against DT 0.3.0 TO-2 RAVC2 18:28:34Z evidence). |

**Combined: the Lambda is computing correctly (AC5 + AC6 PASS; 11-12 of 13 codes pass AC1 + AC2 individually; AC3 produces meaningful 37.5-pt spread). The failures expose AC threshold-vs-empirical-reality misalignments on the dividend-related codes where R1000 universe has structural zero-mass.** Root-cause + adjudication options in SSCN_GROUP_TAXONOMY.md §8.

## Top-10 + Bottom-10 Composites (AC3 evidence)

| Rank | Ticker | Composite | wt_iwb | Notes |
|---:|---|---:|---:|---|
| 1 | MO | 68.65 | 0.1784 | [null=leverage] |
| 2 | MS | 66.26 | 0.2749 | |
| 3 | RTX | 65.97 | 0.2915 | |
| 4 | VZ | 65.15 | 0.3362 | |
| 5 | BMY | 64.47 | 0.2159 | |
| 6 | GS | 63.64 | 0.3453 | |
| 7 | PM | 63.39 | 0.3722 | [null=leverage] |
| 8 | WFC | 63.27 | 0.4802 | |
| 9 | T | 62.86 | 0.2991 | |
| 10 | GILD | 61.67 | 0.2084 | |
| ... | | | | |
| 91 | INTC | 39.46 | 0.1843 | |
| 92 | ADBE | 37.99 | 0.4115 | [null=dps_gr_1yr] |
| 93 | TSLA | 37.56 | 1.7260 | [null=dps_gr_1yr] |
| 94 | AMZN | 37.06 | 3.4747 | [null=dps_gr_1yr] |
| 95 | AMD | 36.64 | 0.3973 | [null=dps_gr_1yr] |
| 96 | ISRG | 36.49 | 0.3445 | [null=dps_gr_1yr] |
| 97 | UBER | 35.06 | 0.2601 | [null=dps_gr_1yr] |
| 98 | VRTX | 33.71 | 0.2178 | [null=dps_gr_1yr] |
| 99 | PANW | 32.43 | 0.2148 | [null=dps_gr_1yr] |
| 100 | NOW | 31.13 | 0.3877 | [null=dps_gr_1yr] |

DIVZ tilt is working directionally — top is dividend-paying mature names + financials; bottom is growth/non-dividend tech.

## Decisions Made

- **Used source XLSX `wt_iwb` column for AC3 top-100 selection** rather than scanner_data.json `mktVal` proxy. wt_iwb is not exposed in row payload; pulling the source XLSX (6.93 MB) gives exact PRD-specified sampling. Trade-off: ~30s extra wall vs unilateral substitution risk. Chose exact.
- **Null-code handling in composite computation:** for top-100 tickers with null pctls codes, renormalized DIVZ weights over non-null codes (preserves 0-100 composite scale). Affects 9 of 100 tickers (8 missing `dps_gr_1yr` + 2 missing `leverage`, with PM having both null). Documented in §5.3.
- **RAVC2 BLOCKED instead of partial-PASS or silent-pass.** PRD do_not §5 is explicit on AC3: "Either is BLOCKED-class — escalate via RAVC2 BLOCKED with offending tickers + per-code pctls breakdown." Also applies by extension to AC1 + AC2 hard fails on specific codes.
- **No commit on BLOCKED state.** Doc + script + CSV stay on-disk uncommitted; commit deferred to RAVC2 COMPLETE close after adjudication.

## Files Modified

| File | Change |
|------|--------|
| `org/tier2_senior/0.3.0_DS_TradingOperations/task_orders/SSCN_DIVDEF.003.ds-divz-preset-empirical-validation-and-group-taxonomy-doc.md` | `<status>` staged -> pending; `<dispatch_held>` true -> false (on GO 18:30Z) |
| `docs/architecture/security-scanner-source/SSCN_GROUP_TAXONOMY.md` | NEW — 331 lines; AC4 deliverable; §1-§8 fully written with empirical data + RAVC2 BLOCKED findings escalation; on-disk uncommitted pending adjudication |
| `.runtmp/sscn_divdef_003_validation.py` | NEW — analysis script (~200 lines); AC1+AC2+AC3+AC5+AC6 single-pass run; gitignored prefix |
| `C:/Users/AndrewBerman/AppData/Local/Temp/sscn_divdef_top100_composite.csv` | NEW — AC3 deliverable; 100 rows |
| `org/tier2_senior/0.3.0_DS_TradingOperations/logs/2026-05-19/sscn_divdef_003_divz_empirical_validation.md` | NEW — this session log |

## Compiler Tools

| Tool | Run | Result |
|------|-----|--------|
| Direct registry read | `python -c "json.load(...)"` on `factor_metadata_registry.json` for 13 DIVZ codes | 13/13 codes present; relationship + category + name extracted. AC5 input (Phase 1). |
| AC1/AC2/AC3/AC5/AC6 analysis | `python .runtmp/sscn_divdef_003_validation.py` | 3 AC failures surfaced (AC1 dps_gr_1yr, AC2 dy_ntm, AC3 top-rank). PASS-class: AC5 (4/4 inverse direction) + AC6 (.asOf). |
| `comp-validate` | Not applicable — this TO validates a Lambda S3 OUTPUT against acceptance criteria, not a gold script artifact. The PRD-defined ACs ARE the validation; no `gold_validate_config.yaml` registered for SSCN. |

`.comp-graph/.agent_context` updated: SERIAL=`0.3.0_DS_TradingOperations`, TO_ID=`SSCN_DIVDEF.003.ds-divz-preset-empirical-validation-and-group-taxonomy-doc`. Auto-logged to `org/compiler-tools-log.md` per startup mandate.

## Blockers

**RAVC2 BLOCKED — pending COO~B + CTO~B adjudication on three AC failures (see SSCN_GROUP_TAXONOMY.md §8).**

Adjudication options summarized:
- AC1: revise `dps_gr_1yr` threshold to ~65%, OR per-code exception, OR drop `dps_gr_1yr` from preset.
- AC2: revise `dy_ntm` KS check (ties-at-zero exemption), OR change Lambda percentile `method`, OR accept structural failure.
- AC3: revise top-rank threshold to >=65 + add spread >=30-pt check, OR re-weight DIVZ to increase Dividend group (mutates Andrew's intent — Andrew judgment required).

DS recommendation: PRD v0.3 threshold revision (preserves Andrew's intent; aligns ACs with empirical reality; closes TO-3 fast).

## Current State

- TO-3 `<status>` = pending (flipped on GO at 18:30Z); `<dispatch_held>` = false.
- All AC evidence captured + filled into SSCN_GROUP_TAXONOMY.md.
- Doc + analysis script + CSV uncommitted on disk.
- RAVC2 BLOCKED MCP next, then idle pending adjudication.

## Next Steps

- `[2.0.0_SA_COO~B + 1.0.0_SA_CTO~B]` Adjudicate the 3 AC failures per SSCN_GROUP_TAXONOMY.md §8 options. PRD v0.3 threshold revision is the DS recommendation.
- `[0.3.0_DS_TradingOperations]` Idle pending adjudication. On revised-AC dispatch: re-evaluate per new thresholds, update §5 + §8 of the doc accordingly, commit + RAVC2 COMPLETE close.
- `[Andrew]` Q for §8.3 if re-weight path chosen: should the DIVZ Dividend group be raised from 40% to ~50-60% to push the top-rank composite >=70, or accept the diversification-driven 68.65 ceiling?
