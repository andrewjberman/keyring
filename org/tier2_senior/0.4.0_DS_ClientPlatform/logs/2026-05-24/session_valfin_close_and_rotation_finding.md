# Session Log: ADVI_VALFIN.001 + .008 Phase A Close + Rotation-Artifact Finding
**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-05-24 (session began 2026-05-23 post-compaction)  
**Branch:** CLOUD  
**Prior context:** Session was compacted mid-execution of ADVI_VALFIN.005 Phase A (dual-emit edits in place, not yet committed)

---

## Session Summary

This session completed:
1. ADVI_VALFIN.008 Phase A (dual-emit field rename shim) -- commit through sentinel verify through COO RAVC2-ACCEPT
2. ADVI_VALFIN.001 Phase 3 (portal consumer confirm) -- all books-tab fields wired
3. ADVI_VALFIN.001 validation brief authored and committed
4. New product-level finding: `unrealized_gain_change_ttm` is a rotation artifact, not a performance signal -- routed as TO-7 meta-analysis finding per Andrew direct

---

## Part 1: ADVI_VALFIN.008 Phase A Execution

### Context Recovery

Session resumed with three uncommitted edits in place (from prior session):
- INF_D_02:1899 (advisor-level): dual-emit `capital_gains_ttm` + `unrealized_gain_change_ttm`
- INF_D_02:2278 (household-level): same
- INF_D_00:837-838 (firm-scope): same

### Phase 2 Compiler Mandate

**ds-commit-gate.sh (INF_D_02 + INF_D_00):**
```
All checks passed!
All checks passed!
OK: pre-commit gate clean for 2 file(s)
```
py_compile + AST scanner + ruff: PASS on both scripts.

**git diff --stat:**
Two target files in diff (+ 4 others in working tree not in commit scope):
```
 data/orion/scripts/gold/INF_D_00.portal_aggregates.py     |   3 +-
 data/orion/scripts/gold/INF_D_02.advisor_client_detail.py |   6 +-
```
Sentinel string check: `capital_gains_ttm` present in both files (deprecated key retained). `unrealized_gain_change_ttm` present in both files (new key). No scope-creep. PASS.

**safe-commit.sh:**
```
[CLOUD 92a18ce03] feat(ADVI_VALFIN.005/PhaseA): dual-emit capital_gains_ttm + unrealized_gain_change_ttm
 Author: 0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>
 2 files changed, 6 insertions(+), 3 deletions(-)
```
Note: unstaged contaminating file `ADVI_VALFIN.008.ds-capital-gains-ttm-field-rename.md` (COO-staged TO file, not in my pathspec) before committing.

### Phase 3 Compiler Mandate

**safe-deploy (pre-push hook):**
```
safe-deploy: 2 script file(s) to deploy
  DEPLOYED  [inf] data/orion/scripts/gold/INF_D_00.portal_aggregates.py
  DEPLOYED  [inf] data/orion/scripts/gold/INF_D_02.advisor_client_detail.py
OK: safe-deploy gate PASS -- all files deployed and verified
```
Both scripts at commit 92a18ce03 confirmed on S3.

Note: `comp-pipescript deployed INF_D_02` returns no match -- tool is keyed to BD pipeline (opal-data-bd). INF scripts use safe-deploy gate as authoritative per §5.3 analogous limitation.

**Gold runner dispatch:**
Full chain triggered via inf-gold-trigger Lambda at 2026-05-23T07:00:48Z. Chain aborted at step 4 (INF_API_PULL_ASSETS_V2 failed -- Orion API ReadTimeout, same mechanism as the 2026-05-20 SCALED anomaly from Phase-2 P2-1). EC2 remained running.

Follow-up: SSM dispatch of `--single INF_D_02` sent directly to running EC2 instance (command_id: ce7ac274-e44f-4ad6-b5da-d0f02b7b784b). Status: Success.

**Sentinel verify (AC3) -- platinum/advisors/{advisor}/book.json:**

| Advisor | capital_gains_ttm | unrealized_gain_change_ttm | Identical |
|---|---|---|---|
| peter_lee | -54,807,679.9 | -54,807,679.9 | PASS |
| patrick_scanlan | -11,739,001.09 | -11,739,001.09 | PASS |
| joe_brandenburg | -4,893,738.15 | -4,893,738.15 | PASS |

All 3 advisors: both keys present, values identical. AC3 PASS.

**AC4 computation-unchanged:**
Pre-deploy (Phase-2 forensic): peter_lee capital_gains_ttm = -54,807,679. Post-deploy: -54,807,679.9. Delta = $0.90 (< $1 threshold). PASS.

**comp-blast capital_gains_ttm:**
1 downstream gold node in INF_D_00. No new consumers added during write window.

**comp-platinum reverse capital_gains_ttm (Phase 3 consumer check):**
Same 3 raw hits as Phase 1 check:
```
portal/src/api/endpoints/advisor-intelligence.ts:1013  (comment)
portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx:571  (live read)
portal/src/pages/AdvisorIntelligence/_shared/types.ts:934  (type field)
```
No new consumers added during write window. PASS.

**RAVC2 to COO + CC CVO:**
Sent 2026-05-23T07:15Z. All 8 ACs evidenced.

**COO RAVC2-ACCEPT:** Received 2026-05-23T07:16Z.
**CVO GREEN verdict:** Received 2026-05-23T07:09Z. Verified 4 emission sites, mathematically guaranteed identical values by construction (both keys read from same scalar). AC4 computation-unchanged confirmed via direct diff read.

**Session log:** org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-23/session_valfin_005_phaseA_dual_emit.md (commit a1b80c9e8)

---

## Part 2: ADVI_VALFIN.001 Phase 3 -- Portal Consumer Confirm

### comp-validate on corrected scripts

**comp-validate B_00:** INFO check only (no primary artifact, pricing script_check). Exit 0. PASS.

**comp-validate INF_D_02:** ERROR -- stale config path. Config references `platinum/advisors/inflection_wealth_management/advisor_client_detail.json` (does not exist; INF_D_02 writes per-household `platinum/clients/{hh_id}/detail.json`). Pre-existing config issue, not caused by dual-emit change. Routed to COO per COMP_VALIDATE_PROTOCOL §4.2.

**comp-validate D_00:** Two pre-existing ERRORs on `gold/artifacts/timeseries_chart.json`:
- `geo_drill key present` (ERROR): client_city not loaded from accounts_dimension; state clickability non-functional. Fix documented in config (`add client_city to _load_parquet line 886`) but not applied in this TO (out-of-scope per AC5).
- `geo top-level aua nonzero` (ERROR): zero firm AUA in geo cohort. Pre-existing.
Neither caused by dual-emit (which touched only `firm_tax_for_emit` ~line 837-838). Routed to COO per §4.2.

### comp-platinum reverse -- books-tab fields

**tax_exposure:**
```
SERVED VIA: getPlatinumAdvisorSummary /api/scoped/partners/books/advisor/{param}/platinum-summary
CONSUMED BY: AdvisorBookView via getPlatinumAdvisorSummary (tax_exposure)
```
Portal consumer correctly wired. PASS.

**unrealized_gain_change_ttm:** Not found -- case [a] genuinely absent, expected (Phase B DE work; portal not yet updated to read new key).

**cost_basis / unrealized_gain:** 3 raw hits each (indexer gap -- access pattern not captured by comp-platinum index). Direct portal source read confirms wired (see below).

### Direct portal source confirm

**AdvisorBookView.tsx:565-575 -- all books-tab fields:**
```typescript
taxable:           bookData.tax_exposure.taxable,
taxablePct:        bookData.tax_exposure.taxable_pct,
taxDeferred:       bookData.tax_exposure.tax_deferred,
taxDeferredPct:    bookData.tax_exposure.tax_deferred_pct,
taxFree:           bookData.tax_exposure.tax_free,
taxFreePct:        bookData.tax_exposure.tax_free_pct,
capitalGainsTtm:   bookData.tax_exposure.capital_gains_ttm,   // line 571 -- reads deprecated key correctly
costBasisByYear:   bookData.tax_exposure.cost_basis_by_year,  // line 572
topGainPositions:  bookData.tax_exposure.top_gain_positions ?? [],
realized:          bookData.tax_exposure.realized,
unrealized:        bookData.tax_exposure.unrealized,
```

**ClientsTab.tsx:839 -- firm-scope:**
```typescript
capitalGainsTtm: clientsTabData.tax.capital_gains_ttm,
```

All books-tab fields confirmed wired. `capital_gains_ttm` continues to be read at both consumer locations under the dual-emit shim. PASS.

### Validation brief

Written and committed: docs/briefs/advi-valfin-001-inflection-books-tab-validation-20260523.md (commit 5365d96f2)

### RAVC2 to COO

Sent 2026-05-23T07:30Z. All 6 ACs evidenced. Pre-existing comp-validate config ERRORs routed for config correction TOs. Open items documented.

---

## Part 3: Rotation-Artifact Finding (Andrew Direct -- TO-7 Routing)

### Andrew's Observation

After reviewing the -$54.8M sentinel value, Andrew identified a more fundamental problem with the metric beyond the misleading field name:

> "this to me sounds more like capturing of all rotated asset value rather than capital gains -- accordingly very misleading"

### Analysis

`unrealized_gain_change_ttm` (formerly `capital_gains_ttm`) computes: sum(delta_unrealized) over the TTM window. When an advisor rotates a position:
1. Sells stock A: `ug_end = 0` for that position → large negative delta_unrealized recorded
2. Buys stock B: starts with `ug_start = 0` → zero contribution to future delta_unrealized

Even if the rotation was profitable (sold at a gain), the metric records a large negative. An actively managed book with frequent rotation will systematically show large negative `unrealized_gain_change_ttm` regardless of whether the rotations were beneficial.

This means the metric is doubly misleading:
1. "Capital gains" implied realized gains (tax concept) -- this is unrealized. The rename to `unrealized_gain_change_ttm` addresses this.
2. Even with the correct name, heavy rotation drives the number negative in a way that looks like underperformance but actually reflects portfolio activity. A high-performing advisor who rotates frequently would score worse than an underperforming advisor who holds forever.

The -$54.8M for peter_lee is almost entirely rotation-driven per the Phase-2 forensic (top contributors all have `ug_end=0` = sold positions).

### Disposition

This is a **TO-7 meta-analysis finding** -- a non-obvious methodological caveat that the UI label does not surface and that requires product-level judgment to resolve.

Options (not decided; routing to COO for product call):
1. Add tooltip/footnote to portal explaining the rotation mechanic when displaying this field
2. Compute a rotation-adjusted version (market-driven unrealized change only, excluding positions that went to zero via sale)
3. Replace with a more direct metric (e.g., total realized gains TTM from silver/api_dims/tax_realized)
4. Remove from the books-tab entirely pending a cleaner replacement

The Phase B DE rename (portal consuming `unrealized_gain_change_ttm`) should be held until this product question is answered. Renaming alone without label context doesn't prevent the same misread on the portal surface.

**Routing:** RAVC2 to COO with TO-7 meta-analysis finding for product-judgment decision on (a) whether to display this metric at all, (b) label/tooltip design if retained, (c) whether to compute a rotation-adjusted version.

---

## Commits This Session

| Commit | Author | Description |
|---|---|---|
| 92a18ce03 | 0.4.0_DS_ClientPlatform | feat(ADVI_VALFIN.005/PhaseA): dual-emit capital_gains_ttm + unrealized_gain_change_ttm |
| a1b80c9e8 | 0.4.0_DS_ClientPlatform | log(ADVI_VALFIN.005/PhaseA): session log + AC evidence |
| 5365d96f2 | 0.4.0_DS_ClientPlatform | brief(ADVI_VALFIN.001): validation brief -- Phase A complete, portal consumer confirm PASS |
| [this commit] | 0.4.0_DS_ClientPlatform | log(session close): VALFIN close + rotation-artifact finding |

---

## Open Items

| Item | Status | Owner |
|---|---|---|
| ADVI_VALFIN.008 Phase B (portal swap to new key) | BANKED | DE pod-4, gated on LD-0014 re-spawn |
| ADVI_VALFIN.008 Phase C (collapse old key) | BANKED | DS, gated on Phase B production-deploy |
| INF_C_08 fee billing gap | Awaiting Andrew biz confirm | COO routing |
| comp-validate config: INF_D_02 stale path | Routed to COO | Config correction TO |
| comp-validate config: INF_D_00 geo_drill ERRORs | Routed to COO | Geo drill investigation TO |
| INF_C_07/D_00c book-growth edits | HOLD | COO + INFGRO coordination required |
| unrealized_gain_change_ttm rotation-artifact product question | TO-7 routing | COO product-judgment call |

---

*0.4.0_DS_ClientPlatform, 2026-05-24*
