# ADVI_VALFIN.001 -- Inflection Books-Tab Validation Brief
**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-05-23  
**TO:** ADVI_VALFIN.001.ds-books-tab-validation-spearhead.md  
**Branch:** CLOUD  
**Status:** Phase A complete; Phase B (ADVI_VALFIN.008 Phase B) banked pending DE pod-4 re-spawn

---

## Summary

3-layer validation (verify-channel 4-check + meta-analysis correctness + portal-consumer confirm) applied to all 9 in-scope gold scripts + INF_D_02 (expanded) + silver tax dims for the Inflection books-tab cost-basis cluster.

Results:
- Phase-1 (verify-channel): All scripts FRESH/SCALED/NOT-FROZEN as of 2026-05-22
- Phase-2 (methodology): 6 findings; 0 gold-script defects; 1 structural pipeline gap fixed; 1 field-name defect fixed via dual-emit shim
- Phase-3 (portal consumer confirm): All books-tab fields correctly wired; no consumer breaks
- 2 corrections deployed: INF_B_00 bronze-complete gate (0419ae771) + INF_D_00/D_02 dual-emit shim (92a18ce03)

---

## In-Scope Scripts

Gold scripts validated:
1. INF_B_00 -- canonical holdings
2. INF_B_01 -- B-chain lots (positions cube input)
3. INF_B_01b -- B01 supplement
4. INF_B_02 -- FIFO lot cost basis
5. INF_B_03 -- lot enrichment
6. INF_C_05 -- performance + gain aggregation
7. INF_C_07 -- book growth (advisory; HOLD on edits per COO coordination)
8. INF_C_08 -- fee billing (HOLD; fee billing gap routed as biz question to COO; awaiting Andrew confirm)
9. INF_D_00 -- portal aggregates (CORRECTED: dual-emit)
10. INF_D_02 -- advisor client detail (CORRECTED: dual-emit)

Silver dims validated:
- silver/api_dims/tax_realized
- silver/api_dims/tax_unrealized
- silver/api_dims/accounts_dimension

---

## Phase-1: Verify-Channel 4-Checks (All Scripts)

All 10 gold scripts + silver dims passed EXISTS / FRESH / SCALED / NOT-FROZEN checks as of 2026-05-22.

One anomaly surfaced for follow-up in Phase-2:
- INF_B_00 2026-05-20: SCALED at 64% expected rows (277 tickers vs 1,558 expected) -- root-caused in Phase-2 as Orion API ReadTimeout causing missing assets.csv

See session log: org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-22/session_valfin_001_phase1_c07_to_d02.md (commit c02c9c1ed)

---

## Phase-2: Methodology Findings

### Finding P2-1: INF_B_00 Silent Bronze Partial-Run (CORRECTED)

**Root Cause:** Orion API ReadTimeout during 2026-05-20 bronze ETL → `assets.csv` absent → INF_B_00 fell back to PMV-only path (10,691 rows/$200M, no account dimension) → output presented as valid platinum. Structural gap: no gate existed to skip a date on `_BRONZE_COMPLETE.json` overall=failure + assets dim=fail.

**Fix:** Added `_bronze_assets_ok()` gate in INF_B_00. Reads `_BRONZE_COMPLETE.json`; skips date and emits `platinum/firm/_meta/bronze_skip_warning_{date}.json` warning sentinel if assets dim failed. Pre-existing dates (no manifest) pass through.

**Commit:** 0419ae771  
**Deployed:** safe-deploy PASS  
**Scope:** ADVI_VALFIN.001 TO-5 (pipeline robustness umbrella)  
**Result:** CLOSED

---

### Finding P2-2: `capital_gains_ttm` Field Name Misleading (CORRECTED via ADVI_VALFIN.008 Phase A)

**Root Cause:** `capital_gains_ttm` in book.json / portal_aggregates computes delta cumulative UNREALIZED gain over TTM window (account_performance.parquet: `sum(ug_end) - sum(ug_start)` over nearest-date TTM anchor). Field name implies realized capital gains. CVO LD-0012 YELLOW verdict (commit 1247fa15b) flagged the name misleading when Andrew read peter_lee's -$54.8M value in a session log.

**DS Phase-2 forensic (this session, f55ef0dc7):**
- Source: `gold/timeseries/account_performance.parquet` (1,265,485 rows; peter_lee: 609 accounts, 841,647 rows)
- TTM probe: sum(delta_unrealized) = -$54,807,680 matches book.json -$54,807,679 to $1 rounding
- No single-account dominance (top-10 ~$1-2M each, none >5% of total)
- Top negatives have ug_end=0 (sold positions; unrealized→realized conversion) -- consistent mechanism
- 121 new accounts contributed $0 net -- rules out asymmetric-treatment hypothesis
- Computation: CORRECT. Defect is purely the field name.

**Fix (ADVI_VALFIN.008 Phase A):** Dual-emit shim:
- Both INF_D_02 (advisor + household level) and INF_D_00 (firm scope) now emit BOTH keys with identical values
- `capital_gains_ttm` retained as deprecated key (portal reads it during Phase B transition)
- `unrealized_gain_change_ttm` new semantically correct key

**Commit:** 92a18ce03  
**CVO ratification:** VALFIN.008 Phase A GREEN (CVO message 20260523T070944Z)  
**Phase B (portal types/components swap):** BANKED -- DE pod-4 killed by MSTR LD-0014; gated on re-spawn  
**Phase C (collapse old key):** BANKED -- gated on Phase B production-deploy verify  
**Result:** Phase A CLOSED; Phase B/C tracked under ADVI_VALFIN.008

---

### Finding P2-3: INFLECTION_REP_IDS Consistency (NO DEFECT)

Rep filter `frozenset({3, 6, 11, 12})` verified consistent across INF_B_00, INF_D_08, INF_D_00e. No inconsistency found. PASS.

---

### Finding P2-4: SOURCE_SCHEMA_VERSION Branching Risk (NO DEFECT)

INF_B_00 writes `SOURCE_SCHEMA_VERSION = 'bronze_pmv_hybrid_v1'` to `_meta` sidecar only. Downstream B-chain scripts (INF_B_01/B_02/B_03) do NOT read or branch on it. PASS.

---

### Finding P2-5: INF_B_01b Coverage Gap (IMMATERIAL, NOTED)

INF_B_01b covers $83,119 (0.50%) of peter_lee's unrealized gain outside INF_B_01's primary population. Below materiality threshold for investigation. Documented; no correction warranted.

---

### Finding P2-6: Gold vs Orion Unrealized Gap (METHODOLOGY, NOT DEFECT)

Peter_lee unrealized: gold=$3.7M (22%) below Orion API snapshot. Gap attributable to:
- T+0 vs T+1 computation window (INF_B_00=REST API same-day vs INF_B_01=TRN-reconstructed T+1)
- Population scope (INF gold covers positions via B-chain; Orion API includes all positions including edge cases)
- Date anchoring (gold uses data_as_of; Orion API is live)

This is expected methodology divergence, not a data defect. NOTED in brief; no correction warranted.

---

## Phase-3: Portal Consumer Confirm

### tax_exposure block

comp-platinum reverse result for `tax_exposure`:
```
SERVED VIA: getPlatinumAdvisorSummary: /api/scoped/partners/books/advisor/{param}/platinum-summary
CONSUMED BY: AdvisorBookView via getPlatinumAdvisorSummary (tax_exposure)
```

### AdvisorBookView.tsx:565-575 -- all books-tab fields wired

```typescript
taxable:           bookData.tax_exposure.taxable,
taxablePct:        bookData.tax_exposure.taxable_pct,
taxDeferred:       bookData.tax_exposure.tax_deferred,
taxDeferredPct:    bookData.tax_exposure.tax_deferred_pct,
taxFree:           bookData.tax_exposure.tax_free,
taxFreePct:        bookData.tax_exposure.tax_free_pct,
capitalGainsTtm:   bookData.tax_exposure.capital_gains_ttm,   // line 571
costBasisByYear:   bookData.tax_exposure.cost_basis_by_year,  // line 572
topGainPositions:  bookData.tax_exposure.top_gain_positions ?? [],
realized:          bookData.tax_exposure.realized,
unrealized:        bookData.tax_exposure.unrealized,
```

### ClientsTab.tsx:839 -- firm-scope capital_gains_ttm wired

```typescript
capitalGainsTtm: clientsTabData.tax.capital_gains_ttm,
```

**Result:** All books-tab fields correctly wired. `capital_gains_ttm` continues to be read at both consumer locations during Phase B transition window. `unrealized_gain_change_ttm` present in platinum but not yet consumed (Phase B DE work, expected). PASS.

---

## Pre-existing comp-validate ERRORs (Routed to COO)

Two pre-existing comp-validate config issues surfaced during Phase-3. Neither caused by this session's changes.

### INF_D_02 comp-validate ERROR: stale config path

Config references `platinum/advisors/inflection_wealth_management/advisor_client_detail.json` with `clients` count_min=100. This artifact does not exist at that path -- INF_D_02 writes individual `platinum/clients/{hh_id}/detail.json` per household (no firm-level aggregate client detail file). Config path is stale/wrong. Per COMP_VALIDATE_PROTOCOL §4.2 false-positive: config needs update to reference the correct artifact path. Routed to COO for config correction TO.

### INF_D_00 comp-validate ERRORs: geo_drill / geo_aua on timeseries_chart.json

Two ERRORs on `gold/artifacts/timeseries_chart.json`:
- `geo_drill key present` -- config states fix: "add client_city to _load_parquet(ACCOUNTS_DIMENSION, columns=[...]) at line 886." Pre-existing; not affected by dual-emit change (line 837-838).
- `geo top-level aua nonzero` -- zero firm AUA in geo cohort. Pre-existing.

These are in-scope for INF_D_00 but NOT for the dual-emit change (which touched only `firm_tax_for_emit`). Routing to COO for scheduling under a separate geo_drill investigation TO to avoid VALFIN.001 scope-creep.

---

## Acceptance Criteria Status

| AC | Description | Result |
|---|---|---|
| AC1 | Each books-tab number matches gold artifact (artifact-match) | PASS -- all fields wired; dual-emit ensures no breakage |
| AC2 | Each number passes reasonableness check (series-walk + bounds + sentinel case) | PASS -- peter_lee TTM probe to $1 rounding; 3-advisor dual-emit sentinel all IDENTICAL |
| AC3 | Methodology documented in plain English; non-obvious caveats flagged | PASS -- P2-2 finding documents TTM semantic; P2-6 documents methodology gap |
| AC4 | Every finding has terminal disposition (corrected or routed) | PASS -- P2-1 corrected (0419ae771); P2-2 corrected (92a18ce03 Phase A, B/C banked); P2-3/4/5/6 documented; comp-validate config ERRORs routed to COO |
| AC5 | Zero out-of-scope edits | PASS -- safe-commit.sh contamination guard clean on all commits |
| AC6 | Session log + validation brief; RAVC2 to COO | PASS (this document) |

---

## Open Items

1. **ADVI_VALFIN.008 Phase B (DE-lane):** Portal types.ts + AdvisorBookView.tsx + ClientsTab.tsx + adapter swap to `unrealized_gain_change_ttm`. Gated on DE pod-4 re-spawn (MSTR LD-0014).
2. **ADVI_VALFIN.008 Phase C (DS-lane):** Collapse dual-emit; remove old `capital_gains_ttm` emit. Gated on Phase B production-deploy verify.
3. **INF_C_08 fee billing gap:** 0-row `fee_rate_history.parquet` -- awaiting Andrew biz confirm from COO (biz question: expected-empty vs data gap).
4. **comp-validate config corrections:** INF_D_02 stale path + INF_D_00 geo_drill ERRORs -- routed to COO for separate correction TO.
5. **INF_C_07/D_00c book-growth edits:** HOLD per COO + INFGRO coordination requirement. No edits made.

---

## Commits in This TO

| Commit | Description |
|---|---|
| c02c9c1ed | log(ADVI_VALFIN.001/Phase1): session log Phase-1 C07-D02 + silver tax dims |
| f55ef0dc7 | log(ADVI_VALFIN.001/Phase2): methodology findings -- 6 items, 0 gold corrections |
| 0419ae771 | feat(ADVI_VALFIN.001/TO-5): INF_B_00 bronze-complete gate for asset-dim fail |
| 92a18ce03 | feat(ADVI_VALFIN.008/PhaseA): dual-emit capital_gains_ttm + unrealized_gain_change_ttm |
| a1b80c9e8 | log(ADVI_VALFIN.008/PhaseA): session log + AC evidence -- dual-emit sentinel PASS |
| [this commit] | brief(ADVI_VALFIN.001): validation brief |

---

*Generated by 0.4.0_DS_ClientPlatform, 2026-05-23T07:25Z*
