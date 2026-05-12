# DS~D 2026-05-12 session 2 — 49F capital_gains_ttm TTM-correction (BD parity port of DS~B INF pattern)

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Window:** ~20:53Z 2026-05-12 → 21:00Z 2026-05-12 (~30min focused implementation)
**Trigger:** Andrew direct directive — "take care of the 49F capital gains issue" (~20:53Z). Pre-existing brief: RD 0.4.2 brief routed via DS~C 2026-05-12T18:53Z. Non-urgent per SYNC #2 — Andrew prioritized after INF NNA chain went into AE-pending state.

---

## TL;DR

Single commit `094014158` (3 files, +186/-34) ports DS~B's INF TTM-locked pattern (`2e5539bac`) to BD pipeline. Replaces inception-cumulative `nq_unrealized` (a misnomer — field was named `capital_gains_ttm` but emitted lifetime-since-account-open unrealized gain) with proper 365-day TTM rollup across taxable accounts. Three emit sites + D_04 passthrough confirmed unchanged. Shared helper in `lib/gold_utils.py` so all sites consume the same pre-computed per-account TTM dict (built once per `main()`, no per-iteration re-aggregation of the 6.7M-row `account_performance` timeseries).

---

## Pre-fix state

| Emit site | Code | Value type | What it emitted |
|---|---|---|---|
| `D_00.portal_aggregates.py:537` | `'capital_gains_ttm': round(nq_unrealized, 2)` | firm headline (`clients_tab.json#tax`) | `tax_taxable['total_accrued_gain'].sum()` — inception-cumulative |
| `D_02.advisor_client_detail.py:925` | `'capital_gains_ttm': round(nq_unreal_gain, 2)` | advisor `book.json#summary.tax` | `book_tax['total_accrued_gain'].sum()` — inception-cumulative |
| `D_02.advisor_client_detail.py:2417` | `'capital_gains_ttm': round(nq_unrealized, 2)` | client `detail.json#tax` | `tax_taxable['total_accrued_gain'].sum()` — inception-cumulative |
| `D_04.client_portal_summary.py:2480` | `headline.get('capital_gains_ttm', 0)` | slim passthrough | passthrough only — no code change needed |

All three downstream emits derived from `client_tax_liability.parquet.total_accrued_gain` which is a single-snapshot field representing **lifetime** accrued unrealized gain on the lot (cost_basis → market_value delta since lot acquisition). The field name says TTM; the value was inception.

## Methodology adaptation — INF vs BD

DS~B's INF pattern uses `account_performance.unrealized_gain` (a per-day cumulative-from-inception column on INF's account_performance table). TTM = `latest_value - 365d-prior_value` (delta).

BD's `account_performance.parquet` does NOT carry `unrealized_gain` (confirmed via empirical schema dump — columns: `account_id, additional_advisor, architect, aua_change, aua_residual, consultant, cum_inflows, cum_outflows, daily_inflow, daily_outflow, date, growth, implementor, local_ops, relationship_id, tax_status, total_aua`). It has `growth` instead.

Verified empirically that BD's `growth` is **per-day market-driven AUA change** (= `aua_change - (daily_inflow - daily_outflow) - aua_residual`). Sample (account z0812152081, 2026-05-04 → 2026-05-08):
- 5-day sequence: aua_change = growth (= -191.86, +593.56, +1146.18, -703.01, +435.86) on days with zero flows
- Confirms `growth` is the market-gain component, daily, per-account

**Semantic equivalent:** summing `growth` over a 365-day window per account ≡ INF's `unrealized_gain` delta over the same window. Both treat partial-period accounts (created within the TTM window) as fully-accrued in the period (matches DS~B's INF rule).

## Implementation

### `lib/gold_utils.py` — shared helper (NEW)

Two functions:
```python
def compute_capital_gains_ttm_by_account(perf, today, taxable_only=True) -> dict:
    """Per-account TTM capital gains. Returns dict[account_id_str -> float]."""
    # mask: (date > today - 365) & (date <= today) & (tax_status == 'taxable' if taxable_only)
    # window.groupby('account_id')['growth'].sum()
    # returns dict{account_id_str: float}

def sum_capital_gains_ttm_for_accounts(dict, account_ids) -> float:
    """Sum dict values across account_ids (str-coerced lookup, 0.0 fallback)."""
```

Built ONCE per `main()` invocation. Callers sum across scope by account_id lookup. O(n_accounts) per scope — no re-aggregation of the 6.7M-row timeseries per scope iteration.

### D_00 — firm-level wiring

`_build_tax_section(perf_latest, tax, cap_gains_ttm_by_account=None)`:
```python
'capital_gains_ttm': (
    sum_capital_gains_ttm_for_accounts(
        cap_gains_ttm_by_account,
        tax_taxable['account_id'].astype(str).unique()
    ) if cap_gains_ttm_by_account else round(nq_unrealized, 2)
)
```

`build_clients_tab` computes the dict from `perf` (full `account_performance` already in scope) + `today`, passes through to `_build_tax_section`.

### D_02 — advisor + client wiring

`_build_advisor_tax_exposure(tax, rel_ids, acct_snap=None, billable_account_ids=None, cap_gains_ttm_by_account=None)`:
```python
'capital_gains_ttm': (
    sum_capital_gains_ttm_for_accounts(
        cap_gains_ttm_by_account,
        acct_snap.loc[acct_snap['tax_status'] == 'taxable', 'account_id'].astype(str).unique()
    ) if cap_gains_ttm_by_account is not None and acct_snap is not None and not acct_snap.empty
      else round(nq_unreal_gain, 2)
)
```

`_build_tax(acct, tax, lots, today, cap_gains_ttm_by_account=None)`: same pattern but using `snap = acct[acct['date'] == latest_date]` as the per-client scope filter.

`build_advisor_books` and `build_client_details` each compute the dict ONCE near function entry (both have `acct` = full perf + `today` in scope), then pass to `_build_advisor_tax_exposure` / `_build_tax` per iteration.

### Fallbacks

All three sites preserve the prior `nq_unrealized` / `nq_unreal_gain` fallback when `cap_gains_ttm_by_account` is None or empty. Two practical effects:
1. If `account_performance.growth` column ever disappears (schema drift), output falls back to legacy inception-cumulative value rather than emitting 0 or crashing.
2. Backward-compat during the deploy window — old `D_00` calling new `_build_tax_section` without the kwarg still emits a legacy value.

## Carried hygiene on D_02 (gate-driven)

ds-commit-gate flagged 20 pre-existing ruff violations on D_02. Categorical breakdown:
- **13 × E712** pandas boolean masks on `qualified_flag`/`is_billable`/`is_current`/`is_open` columns — EXACTLY the same NaN-risk pattern that caused my D_00 NaN regression earlier today (commit `9b2829db3`). Pinned each with `# noqa: E712` + (for one diagnostic) `# noqa: F841` — preserves the NaN-safe `== True/== False` form, resists future ruff `--unsafe-fixes` re-introducing the ValueError. Memory feedback `feedback_ruff_unsafe_fix_pandas_nan.md` already captured the rule.
- **5 × F541** empty f-strings (no placeholders) — safe auto-fix.
- **1 × F401** unused `sys` import — safe auto-fix.
- **1 × F841** unused `total_aua` variable on line 1043 (diagnostic placeholder, kept with `# noqa: F841` + explanatory comment).
- **Rule 15** missing `from __future__ import annotations` on D_02 (3248 lines) — added.

`lib/gold_utils.py` also got Rule 15 future-import + 4 unused-import cleanups (ThreadPoolExecutor, as_completed, datetime, timezone).

## Commits

| SHA | Description |
|-----|-------------|
| `094014158` | feat(D_00+D_02+lib): 49F capital_gains_ttm TTM-correction (RD brief, DS~B INF parity) |

3 files changed, 186 insertions, 34 deletions. Push + safe-deploy.sh hook deployed `D_00`, `D_02`, `lib/gold_utils.py` to `s3://opal-data-bd/code/gold/` with SHA-MATCH verification.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `ds-commit-gate.sh` | 4× (iteratively as I added Rule 15 + noqa pins + F-string cleanups) | Final PASS on all 3 files |
| `.tools/safe-commit.sh` | 1× | Clean (no owned-paths violations, no contamination) |
| `safe-deploy.sh` pre-push hook | 1× | 3/3 DEPLOYED + SHA-MATCH on `opal-data-bd/code/gold/` |
| `comp-pipescript io D_00` / `comp-pipescript io D_02` | (skipped — no schema change, only field-value semantics flip) | n/a |

`comp-pipescript io` skipped because the change is field-value semantics, not new I/O. Field names, paths, downstream consumers all unchanged.

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/lib/gold_utils.py` | NEW helpers (`compute_capital_gains_ttm_by_account`, `sum_capital_gains_ttm_for_accounts`) + Rule 15 + unused-import cleanup |
| `data/black_diamond/scripts/gold/D_00.portal_aggregates.py` | Import new helpers; `_build_tax_section` accepts `cap_gains_ttm_by_account` kwarg; `build_clients_tab` builds dict from `perf` + `today` |
| `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` | Import new helpers; `_build_advisor_tax_exposure` + `_build_tax` accept `cap_gains_ttm_by_account` kwarg; `build_advisor_books` + `build_client_details` build dict from `acct` + `today`; Rule 15; 14 noqa E712 + 1 F841 pins; 5 F541 + 1 F401 auto-fixes |

## Cross-firm parity AC (post-chain)

Per RD brief: pick a comparable advisor at 49F and Inflection (e.g. Tim Rodgers, Travis Penfield, David Farrell on the 49F side; Peter Lee on Inflection). Both `capital_gains_ttm` values should represent the same 12-month window meaning (cumulative market-driven gain on taxable accounts in trailing 365d), within methodology tolerance.

Tolerance considerations:
- INF's `unrealized_gain` is computed off cost-basis lots from Orion's lot-level data
- BD's `growth` is computed at account-grain from cube positions × canonical prices delta
- Both should produce ~similar TTM magnitudes for accounts that didn't have unusual structural events (M&A, account transfers, cost-basis resets), but exact-equality won't hold

## Current State

| Item | Status |
|---|---|
| 49F `capital_gains_ttm` TTM-correction | SHIPPED commit `094014158`; S3-deployed; awaiting next BD gold chain (next nightly is 04:00Z 2026-05-13 unless Andrew/AE fires earlier) |
| INF NNA donut+drill (from session 1) | SHIPPED commits `7bcaac70e` + `55e37ebcb`; S3-deployed; AE 0.6.1 OFFLINE since ~20:40Z, gold-d dispatch request queued in their inbox |

## Next Steps

1. **[Self — passive]** When nightly BD chain runs (04:00Z 2026-05-13 unless triggered earlier), pull `gold/artifacts/clients_tab.json#headline.capital_gains_ttm` + sample advisor `book.json#summary.tax.capital_gains_ttm` + sample client `detail.json#tax.capital_gains_ttm`. RAVC2 DS~C + DE + Andrew with pre/post numbers for cross-firm-parity sentinel check.
2. **[AE 0.6.1]** When they come back online, fresh orion-gold-dispatch `gold-d` to pick up INF NNA fix commits. Then I RAVC2 with INF empirical pre/post.
3. **[Self]** If Andrew prioritizes either chain earlier than nightly, route via COO with "AE-unavailable" flag per AE 0.7's standing guidance from earlier today.

## Pacing reflection

This was a focused 30-min implementation after the day's marathon. The DS~B pattern handed me a clear template — the work was correctly identifying the BD-side semantic equivalent (`growth` per-day sum vs INF's cumulative delta) and threading the shared helper through 3 emit sites without restructuring the calling functions. The carried hygiene on D_02 was substantial (20 ruff violations) but Andrew's morning incident report and my own memory feedback (`feedback_ruff_unsafe_fix_pandas_nan.md`) gave me the exact playbook — pin `# noqa: E712` rather than accept the unsafe-fix that broke D_00 hours earlier. Same-day learning loop closed cleanly: I shipped the bug, I caught it, I wrote the memory, I applied the memory to prevent the next instance.
