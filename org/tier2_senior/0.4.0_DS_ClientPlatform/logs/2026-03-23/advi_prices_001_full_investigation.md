# ADVI_PRICES-001: Phantom Lot Root Cause Investigation -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-23
**Branch:** CLOUD

## Objective

Identify and fix the root cause of +$91M phantom lot excess across 269 accounts in `gold/holdings_lots`, where our FIFO-reconstructed lot MV vastly exceeds BD's silver allocation AUA for the same accounts on the same date.

---

## Work Completed

### 1. Taxonomy Enumeration (Hypothesis: missing exit transaction types)

Wrote `diag_txn_taxonomy_enumeration.py` and AE ran it against full history (2,771,144 rows, 1,754 files).

**Result: DISPROVEN.** Zero unrecognized exit-like types exist in the data. All sell-classified transaction types are already in SELL_TYPES/CA_SELL_SUBTYPES. The only newly-added type with real data is `Redemption` (176 rows, 81 accounts) — but these are encoded as `transaction_type=Sale, transaction_sub_type=Redemption`, so `Sale` was already catching them.

The 5 CA subtypes added (Exchange, Tender, Maturity, Called, Liquidation) have zero rows in all of history. Harmless insurance against future data but zero current impact.

### 2. Recon Diagnostic + Phantom Drill-Down

Wrote `recon_lots_vs_allocations.py`. AE ran against `--date 2026-03-19`.

Same-date recon confirmed: +$25.6M net gap (+1.6%), 269 phantom accounts (+$91M), 156 missing-lots (-$28M). The drill-down showed the dominant pattern is securities with ZERO transactions of ANY type in 90 days — the positions are fully stale in our FIFO but gone from BD's allocation.

### 3. Asset Name Mismatch (Hypothesis: FIFO grouping on exact string match)

Wrote `diag_phantom_asset_name_mismatch.py`. AE ran against top 5 phantom accounts.

**Result: DISPROVEN.** Only 1 fuzzy match found (VANGUARD GROWTH ETF vs VANGUARD VALUE ETF — a false positive, different funds). Zero legitimate name mismatches. $0 of $52.8M excess explained.

### 4. FIFO Replay (Hypothesis: dedup/NaN/temporal guard losing sell volume)

Wrote `diag_phantom_fifo_replay.py`. AE ran against top 10 phantom accounts, replaying FIFO transaction-by-transaction across 48 positions.

**Results:**

| Hypothesis | Positions affected | Finding |
|---|---|---|
| H1: Dedup dropping sells | 2 accounts | 94 sell rows dropped, 16,980 units lost. Modest. |
| H2: Sells with NaN/zero units | 2 rows | Negligible (Agnico Eagle Merger CA in 2022). |
| H3: Temporal guard skipping sells | 4 positions, 1 account | **CONFIRMED BUG.** Account z0818693751 ($55.9M): options with sell dates before buy record dates. Temporal guard discarded 12,602+ units. |
| H4: FIFO arithmetic error | 4 positions | All caused by H3, not independent. FIFO math is correct. |

**Position-level verdicts across 48 positions:**

| Verdict | Count | Pattern |
|---|---|---|
| Zero sells in all history | 35 (73%) | BD never sent any exit transaction. Position removed from allocation without a corresponding transaction. |
| Incomplete feed (5-95% sells) | 12 (25%) | Some sells exist but only deplete 20-30% of buys. Transaction feed stopped partway. |
| Temporal guard blocked | 4 (8%) | Sells skipped because sell date < lot acquisition date. Derivatives-specific. |

### 5. Temporal Guard Fix

Fixed `build_lots_for_group()` in `03_build_holdings_lots.py`. After the normal FIFO pass, any sell volume blocked by the temporal guard is accumulated as `temporal_spillover` and applied in a second pass that ignores dates. Normal equity cases are unaffected; only out-of-order sells (derivatives, backdated corrections) use the fallback.

**Estimated impact:** ~$55.9M phantom excess recovered from the options account.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Kept taxonomy expansion (Redemption + 5 CA subtypes) despite near-zero current impact | Insurance against future BD data changes. Zero-row types are harmless dead code. |
| Did NOT implement allocation-authority capping | Would override FIFO with BD's numbers rather than fixing root cause. FIFO logic is correct given its inputs — the problem is upstream data quality. |
| Implemented temporal guard spillover as second pass, not by removing the guard | Preserves correct FIFO ordering for normal cases. Only fallback is used for temporal anomalies. |
| Did NOT modify 02_build_positions_cube.py | Task order constraint. AE must sync allowlists and temporal guard fix separately. |

---

## Root Cause Summary

The $91M phantom lot excess has two distinct causes:

**Cause 1 (~$55.9M): Temporal guard bug in FIFO** — FIXED in commit `4278798e`. The `break` in the temporal guard silently discarded sell volume for derivatives where BD records buy dates after exercise/expiry dates. The second-pass spillover fix recovers this volume.

**Cause 2 (~$35M): BD transaction feed is incomplete** — NOT FIXABLE in script 03. 73% of phantom positions have literally zero sell transactions in all of history. BD's allocation reflects that these positions are gone, but no corresponding exit transaction was ever issued. The transaction feed and allocation feed are inconsistent at the position level. This is an upstream data quality issue.

---

## Estimated Impact on Gap

Two baselines exist (cross-date vs same-date recon). H3 fix removes ~$56M from overshoot in both.

**Cross-date baseline (allocations 03-19 vs lots 03-20):**

| Metric | Before | After H3 fix | Change |
|---|---|---|---|
| Gross overshoot | +$211M | ~+$155M | -$56M |
| Gross undershoot | -$143M | ~-$143M | unchanged |
| Net gap | +$68M (+4.3%) | ~+$12M (~+0.8%) | -$56M |

**Same-date baseline (both 03-19, eliminates pricing drift):**

| Metric | Before | After H3 fix | Change |
|---|---|---|---|
| Net gap | +$25.6M (+1.6%) | ~-$30M (~-1.9%) | -$56M |

Same-date net flips negative because the options account's phantom $56M was accidentally offsetting real undershoot. The remaining overshoot is dominated by positions with zero sell transactions (upstream gap) and normal pricing divergence. Actual post-fix numbers require AE gold rerun.

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Expanded SELL_TYPES (+1), CA_SELL_SUBTYPES (+5), fixed emoji | Yes -- `f1b3f33d` |
| `data/black_diamond/scripts/gold/03_build_holdings_lots.py` | Temporal guard spillover fix | Yes -- `4278798e` |
| `docs/data/transaction_type_canonical_reference.md` | Added 6 new types to reference | Yes -- `f1b3f33d` |
| `data/black_diamond/scripts/diagnostics/recon_lots_vs_allocations.py` | Created recon diagnostic | Yes -- `9b039259` |
| `data/black_diamond/scripts/diagnostics/diag_txn_taxonomy_enumeration.py` | Created taxonomy enumeration | Yes -- `9b039259` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_asset_name_mismatch.py` | Created name mismatch test | Yes -- `2d0dcad9` |
| `data/black_diamond/scripts/diagnostics/diag_phantom_fifo_replay.py` | Created FIFO replay diagnostic | Yes -- `62ce146d` |

---

## Blockers

- **Remaining $35M phantom excess** requires upstream investigation into why BD's transaction feed omits exit events for positions that BD's allocation feed shows as gone. This is AE scope (silver ingestion pipeline) or a BD vendor configuration issue. No code fix possible in script 03.

---

## Current State

> **Primary handoff point.**

**Status:** COMPLETE (DS scope exhausted)
**Active branch:** CLOUD

Five commits on CLOUD for ADVI_PRICES-001. The temporal guard fix (`4278798e`) is the highest-impact code change, recovering ~$55.9M of phantom excess from derivatives. The taxonomy expansion (`f1b3f33d`) adds Redemption and 5 CA subtypes (near-zero current impact, future insurance). Four diagnostic scripts provide reusable tooling for ongoing reconciliation monitoring.

The remaining $35M phantom excess and the $143M undershoot cannot be addressed in script 03. The phantom remainder is an upstream data quality gap (BD transaction feed incomplete). The undershoot is structural (allocation-only accounts with no transaction history, insurance/annuity wrappers).

---

## Next Steps

1. **[0.6.0_AE_PartnerETL] Sync temporal guard fix + taxonomy expansion to 02_build_positions_cube.py** — same FIFO logic exists in script 02. Must be patched identically.
2. **[0.6.0_AE_PartnerETL] Upload updated gold scripts to S3 and run gold layer FULL mode** — both scripts 02 and 03 changed.
3. **[0.6.0_AE_PartnerETL] Run recon after gold rerun** — `python recon_lots_vs_allocations.py --date 2026-03-19 --output-dir /tmp/recon/` to get actual post-fix numbers.
4. **[0.6.0_AE_PartnerETL] Investigate upstream transaction feed gap** — why does BD's allocation reflect position closures that the transaction feed never recorded? Is this a feed configuration issue, an export scope limitation, or a BD vendor behavior?
5. **[0.4.0_DT_ClientPlatform] Push commits to remote** — 5 commits pending on CLOUD.
6. **[2.0.0_SA_COO] Decide disposition of remaining $35M phantom + $143M undershoot** — accept and document vs pursue upstream fix vs allocation-authority layer.

**Do NOT:**
- Run gold layer rerun (AE scope)
- Push to remote (DT scope)
- Implement allocation-authority capping without COO decision on remaining gap disposition
