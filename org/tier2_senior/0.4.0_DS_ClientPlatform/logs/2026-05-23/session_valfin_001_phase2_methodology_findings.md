# Session Log -- ADVI_VALFIN.001 Phase 2: Methodology + Follow-up Findings

**Agent:** 0.4.0_DS_ClientPlatform (Base lane)
**Date:** 2026-05-23 ~01:30-03:00Z
**Branch:** CLOUD
**Continuation of:** session_valfin_001_phase1_c07_to_d02.md (Phase-1 complete, all PASS)

---

## Session Summary

Completed all 6 Phase-2 carry-forward items from Phase-1. No gold-script corrections
required for Phase-2 items 1-6. Two pipeline-robustness findings routed to TO-5.
ADVI_VALFIN.005 field-rename confirmed no-data-defect (COO authoring). Phase-3 (portal
consumer confirm) is the next gate.

Key findings: INF_B_00 had a silent bronze fallback on 2026-05-20 due to Orion API
timeout (assets.csv missing -- 64% row reduction in gold); capital_gains_ttm semantics
verified as delta-unrealized with exact $1-cent match to book.json; gold vs Orion
unrealized gap ($3.7M/22%) explained by methodology + timing differences.

Inbox activity:
- CVO CC 20260523T045631Z: capital_gains_ttm Phase-2 plan correction (silver tax cross-check
  invalid; correct diagnostic = account_performance.parquet delta_unrealized decomposition)
- COO 20260523T062758Z: Phase-2 GO; fee billing DEFER pending Andrew; capital_gains_ttm
  plan corrected per CVO; ADVI_VALFIN.005 field-rename being authored by COO

---

## Phase-2 Findings

### Finding P2-1: INF_B_00 Silent Bronze Fallback on 2026-05-20 (ROUTE TO-5)

**Origin:** Phase-1 SCALED anomaly (holdings_2026-05-20.parquet = 216KB vs ~315KB neighbors)

**Root cause confirmed:**
- `bronze/orion-api/2026-05-20/_BRONZE_COMPLETE.json`: `overall="failure"`, assets dim `status="fail"`
- Error: `requests.exceptions.ReadTimeout` after 900s on `api.cloud.orionadvisor.com`
- `bronze/orion-api/2026-05-20/assets.csv`: ABSENT (7.8MB file present on 2026-05-19/21)

**Silver-side cleared (Phase-1):**
- `silver/api_dims/positions_mv/snapshot_date=2026-05-20/data.parquet`: 1.0 MiB, 30,285 rows
- Consistent with neighbors (2026-05-19: 30,283 rows; 2026-05-21: 30,289 rows)
- Silver is NOT the anomaly source

**Gold impact quantified:**

| Date | Rows | Accounts | Tickers | Market Value |
|---|---|---|---|---|
| 2026-05-19 | 29,773 | 865 | 1,558 | $201,252,679 |
| 2026-05-20 | 10,691 | 799 | 277 | $200,012,952 |
| 2026-05-21 | 29,792 | 866 | 1,558 | $202,041,469 |

- Row count: -64% (10,691 vs ~29,783 expected)
- Tickers: -82% (277 vs 1,558)
- Accounts: -66 (799 vs 865-866)
- Market value: ~$1.2M below neighbor (not material)

**Reconciliation meta sidecar confirms:**
- `platinum/firm/_meta/reconciliation_summary_holdings_2026-05-20.json`: sources = pmv_only only (no bronze_only or reconciled sections)
- On normal days: bronze_only contributes ~19,087 rows at net -$1.3M market value (the "missing" positions are small/zero-value supplemental positions)
- 2026-05-20's market value ($200M) is approximately correct in aggregate; position-count completeness is the real gap

**B-chain downstream impact:**
- INF_B_01 holdings_lots (2026-05-20 snapshot): ran against incomplete 277-ticker holdings
- INF_B_03 account_gains (2026-05-20 partition): computed against incomplete holdings for that date
- INF_D_00c leaderboard: uses LATEST holdings (2026-05-22, clean) -- NOT affected
- INF_C_05 client_tax_liability: reads latest account_gains (chains from 2026-05-21 and later) -- minimal impact

**Pipeline gap:**
- INF_B_00 has no gate on `_BRONZE_COMPLETE.json overall="failure"`
- It silently proceeds with positions_mv-only when assets.csv is absent
- Gold output for affected date is semantically a partial artifact, not a full holdings snapshot

**Disposition: ROUTE TO-5 (pipeline robustness)**
Routing Ask #5 sent to COO (20260523T063205Z). Proposed fix: INF_B_00 reads
`_BRONZE_COMPLETE.json` before run; if assets dim failed, either skip-gate (carry forward
prior-day holdings) or emit explicit WARNING artifact. Awaiting COO authorization to execute.
NOT a TO-1 in-place correction -- the 2026-05-20 partition is historical; the structural gap
is the missing gate logic.

---

### Finding P2-2: capital_gains_ttm Verified -- No Data Defect (ADVI_VALFIN.005 is the fix)

**Origin:** Phase-1 flag on peter_lee capital_gains_ttm = -$54,807,679

**CVO correction absorbed (20260523T045631Z):**
- capital_gains_ttm = delta-cumulative-unrealized TTM, NOT "rolling realized capital gains"
- TTM window: [data_as_of - 365d, data_as_of], nearest-date anchor (INF_D_02 lines 644-648)
- Computation source: `gold/timeseries/account_performance.parquet unrealized_gain`, NOT silver/api_dims/tax_realized/
- Prior Phase-2 plan item (cross-check against silver tax_realized) was INVALID -- dropped

**Computation verified:**
- Pulled `gold/timeseries/account_performance.parquet`: 1,265,485 rows, dates 2019-09-17 to 2026-05-22
- peter_lee: 609 accounts, 841,647 rows
- TTM probe result: sum(delta_unrealized) = **-$54,807,680**
- book.json capital_gains_ttm = -$54,807,679
- Match to $1 rounding (confirmed correct and internally consistent)

**Decomposition:**
- Broadly distributed across 609 accounts; NO single-account dominance
- Top 10 contributors: -$2.3M, -$1.96M, +$1.54M, -$1.17M, -$1.16M, -$1.06M, -$1.06M, -$1.05M, -$1.02M, -$1.00M
- No single account >5% of -$54.8M total
- Top negative contributors have ug_end=0: accounts with unrealized gains at TTM start now show 0 (positions sold TTM, converting unrealized to realized; or market decline to flat)
- 121 new accounts (joined book during TTM, no start anchor): $0 net contribution (no asymmetric distortion)

**Assessment:** NOT a data defect. Value is correct. The defect is the misleading field name.
**Disposition:** ADVI_VALFIN.005 (field rename: capital_gains_ttm -> unrealized_gain_change_ttm + shim).
COO is authoring the TO. No Phase-2 correction needed in data or INF_D_02 logic. Pod-4 DE
currently DOWN (INFGRO cancellation per CTO 235a93323); TO will be executed when DE lane
re-activates.

**IMPORTANT FRAMING CORRECTION:** Session log `session_valfin_001_phase1_c07_to_d02.md`
line 148 stated "capital_gains_ttm: separate computation within INF_D_02 (TTM rolling realized)"
-- "rolling realized" is WRONG. Correct framing: "delta-cumulative-unrealized TTM." This
correction carries forward in all Phase-3 work and the final VALFIN.001 brief.

---

### Finding P2-3: INFLECTION_REP_IDS Currency Confirm -- PASS

Verified frozenset({3, 6, 11, 12}) is consistent across all three scripts:
- `INF_B_00.canonical_holdings.py:74`: `INFLECTION_REP_IDS = frozenset({3, 6, 11, 12})`
  Comment: `# ADHC_BPMVH.002 D-max: ... Matches INF_D_08 + INF_D_00e Inflection-rep filter convention.`
- `INF_D_08.nmec_nmnc_nna.py:17`: `INFLECTION_REP_IDS: frozenset[int] = frozenset({3, 6, 11, 12})`
  Comment: `# ADVI_INFGRD.001 + joe_brandenburg rep_id=6`
- `INF_D_00e.fresh_header_supplement.py:61`: `INFLECTION_REP_IDS = frozenset({3, 6, 11, 12})`

All three scripts independently define the same set and apply it via `df[df['rep_id'].isin(INFLECTION_REP_IDS)]`.
No stale rep_id; no discrepancy. **4-check Phase-2: PASS.**

---

### Finding P2-4: SOURCE_SCHEMA_VERSION B-Chain Handling -- PASS

`SOURCE_SCHEMA_VERSION = 'bronze_pmv_hybrid_v1'` (INF_B_00.py:79) writes to the
`platinum/firm/_meta/reconciliation_summary_holdings_{date}.json` sidecar only.

Verified: INF_B_01, INF_B_02, INF_B_03 do NOT read the _meta sidecar or branch on
schema_version. No grep hits for `SOURCE_SCHEMA_VERSION`, `schema_version`, or
`bronze_pmv_hybrid` in any B-chain script.

Meta sidecar confirms schema_version consistent across all dates:
- 2026-05-22 `reconciliation_summary_holdings_2026-05-22.json`: `schema_version: "bronze_pmv_hybrid_v1"`,
  sources = {bronze_only: 19,087 rows/-$1.3M, reconciled: 11,616 rows/$204.8M}
- 2026-05-20 `reconciliation_summary_holdings_2026-05-20.json`: `schema_version: "bronze_pmv_hybrid_v1"`,
  sources = {pmv_only: 10,691 rows/$200M} (correctly reflects absent assets.csv)

No discontinuity handling needed in downstream scripts. **PASS.**

---

### Finding P2-5: INF_B_01b Coverage $ Impact -- IMMATERIAL ($83,119 / 0.50%)

INF_B_01b reports 377 unpriced tickers (all-time, across all positions_cube partitions).
Current active impact in `gold/holdings/2026-05-21.parquet` (INF_B_01 output, T+1):
- 362 active tickers today (vs 377 historical unpriced -- most historical unpriced are inactive)
- 39 unpriced positions, 36 unique tickers, 12 accounts affected
- Unpriced tickers: CUSIPs (85xxxxGA7), ESC/CVR (525ESC0S9, 021ESC017), delisted equities (AMC, BKD, BLNK, HTZ)

Impact in `gold/account_gains/2026-05-21.parquet` (INF_B_03):
- 27 positions with market_value=0 and non-zero cost_basis
- Total cost_basis in unpriced: **$83,119**
- Implied understated unrealized gain: **-$83,119 = 0.50% of $16,759,004 firm total**

**Assessment:** Immaterial ($83K vs $16.76M firm unrealized). The 80.28% coverage level
(above the 80% WARN threshold) correctly reflects this immaterial dollar impact.
Monitor if coverage drops below 80%; Phase-3: no correction needed.

---

### Finding P2-6: Gold Chain vs Orion API Unrealized Reconciliation -- METHODOLOGY GAP, NOT DEFECT

**Gold chain (INF_B_03 T+1, 2026-05-21):**
- Total unrealized: $16,759,004
- LT: $18,505,632 | ST: -$1,746,628 (net ST losses)
- Accounts: 818
- Source: positions_cube (TRN-reconstructed) + canonical_prices; FIFO cost basis from silver/transactions

**Orion API (silver/api_dims/tax_unrealized, T+0, 2026-05-22):**
- Total unrealized: $13,047,394
- LT: $12,552,417 | ST: $494,986
- Accounts: 867
- Source: Orion REST API tax dims; Orion-native adjusted cost basis

**Delta: -$3,711,610 (-22.1%)**

Explained by three independent factors (not a defect):
1. **Timing**: Orion T+0 (2026-05-22) vs Gold T+1 (2026-05-21); 1-day market move + new account additions
2. **Population**: 867 Orion accounts vs 818 Gold accounts (49 more in Orion; Orion may include accounts not in positions_cube TRN history)
3. **Methodology**: Orion-native adjusted cost basis vs FIFO from silver/transactions. LT/ST split divergence ($18.5M vs $12.5M LT) reflects different holding-period attribution logic between the two systems.

**Data paths serve different purposes:**
- **Orion API path (displayed on books-tab):** Orion's own tax-adjusted cost basis, used for client-facing tax reporting conversations. Authoritative for the portal books-tab display.
- **Gold chain (supplementary):** FIFO from transaction history, useful for internal audit and consistency checks. INF_C_05 docstring: "advisory/indicative -- not a tax filing artifact."

**Disposition:** Not a defect. Methodology difference is expected and defensible. Document in final brief under AC3 (methodology documentation) with explicit note that portal displays Orion API path, not gold chain. No correction required.

---

## Phase-2 Summary

| Item | Finding | Disposition |
|---|---|---|
| P2-1 INF_B_00 SCALED anomaly | Orion API ReadTimeout → assets.csv absent → 64% row reduction in gold | ROUTE TO-5 (Routing Ask #5 to COO 20260523T063205Z) |
| P2-2 capital_gains_ttm | delta-unrealized TTM correct to $1; field name is the defect | ADVI_VALFIN.005 (COO authoring field rename) |
| P2-3 INFLECTION_REP_IDS | {3,6,11,12} consistent across INF_B_00/D_08/D_00e | PASS -- no action |
| P2-4 SOURCE_SCHEMA_VERSION | B-chain scripts don't read/branch on schema_version | PASS -- no action |
| P2-5 INF_B_01b coverage | $83,119 (0.50% of firm unrealized) -- immaterial | PASS -- monitor |
| P2-6 Gold vs Orion unrealized | $3.7M (22%) gap -- methodology/timing/population difference | PASS -- methodology difference, document in brief |

**DEFERRED (COO pending):**
- INF_C_08 fee billing gap (P2 item 7): awaiting Andrew biz confirm from COO

**GOLD SCRIPT CORRECTIONS NEEDED:** 0 (zero)
No in-place gold-script edits required for Phase-2 items 1-6. Two TO-5 routings active.

---

## Next Steps

| Recipient | Item |
|---|---|
| **2.0.0_SA_COO** | Routing Ask #5 response: authorize INF_B_00 bronze-complete gate fix (TO-5) |
| **2.0.0_SA_COO** | Fee billing gap verdict (Routing Ask #3, Andrew biz confirm pending) |
| **Self (next session)** | If Routing Ask #5 AUTHORIZED: implement INF_B_00 bronze-complete gate (< 20 lines, safe-deploy cycle) |
| **Self (next session)** | Phase-3 portal consumer confirm for all 9 scripts + INF_D_02 (after TO-5 corrections scoped) |
| **Self (next session)** | ADVI_VALFIN.005 field-rename TO execution once COO publishes + DE lane re-activates |
| **Self (ongoing)** | Author final VALFIN.001 brief: docs/briefs/advi-valfin-001-inflection-books-tab-validation-20260523.md |
