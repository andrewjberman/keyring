# Session — RD-Requested Frontend Gap Closures

**Agent:** 0.4.0_DS_ClientPlatform~D
**Date:** 2026-04-20
**Scope:** Portal (DEV) + gold script fixes at 0.4.2_RD_AdvisorIntelligence behest
**Status:** COMPLETE — commits below; all pending gold rerun for live data

---

## 1. ADVI_ROLGAT — small_account_clients[] per role

**Trigger:** RD flagged data-contract gap: `book.role_breakdown[role]` had no per-relationship breakdown of small accounts within a role. RD proposed the full DS spec (groupby relationship_id, agg small_count + small_aua, merge cdim, sort desc by small_aua).

### DS change — D_02 (CLOUD, 42be5b21)

**File:** `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py`
**Location:** `build_advisor_books()`, `for role in available_roles` loop, ~L1425

Extracted `role_small_mask` from the existing inline `loc[]` call. Added post-mask pipeline:
```python
role_small_mask = role_acct_mask & (snap_latest['total_aua'] < SMALL_ACCOUNT_AUA_THRESHOLD_USD)
role_small_count = int(snap_latest.loc[role_small_mask, 'account_id'].nunique())
if role_small_mask.any():
    by_rel = (snap_latest[role_small_mask]
              .groupby('relationship_id')
              .agg(small_count=('account_id', 'nunique'), small_aua=('total_aua', 'sum'))
              .reset_index()
              .merge(cdim[['relationship_id', 'relationship_name']], on='relationship_id', how='left')
              .sort_values('small_aua', ascending=False))
    small_clients = [{'client_key': ..., 'client_name': ...,
                      'small_account_count': ..., 'small_account_aua': ...}
                     for r in by_rel.to_dict('records')]
else:
    small_clients = []
role_breakdown[role]['small_account_clients'] = small_clients
```
Additive — no existing field changed.

### Portal change — types.ts + AdvisorBookView.tsx (portal DEV, 060cf8b)

Swept into commit 060cf8b alongside Book Growth TTM (item 3 below). Portal changes were pre-existing uncommitted RD work:

**`types.ts`:**
```typescript
// role_breakdown entry gains:
small_account_clients?: Array<{
  client_key: string
  client_name: string
  small_account_count: number
  small_account_aua: number
}>
```

**`AdvisorBookView.tsx`:**
- Import `SmallAccountsByRoleModal`
- `useState<string | null>` for `openSmallAcctRole`
- Role display uses fixed `ROLE_ORDER` + `ROLE_LABELS` instead of raw Object.entries
- Small-account cards become `<button>` when `small_account_clients?.length > 0`; click sets `openSmallAcctRole`
- `SmallAccountsByRoleModal` mounted when `openSmallAcctRole` is set

**Render gate:** `small_account_clients?.length > 0` — static card until gold rerun populates field.

---

## 2. Advisor Book Overview — small_account_count subtext

**Trigger:** Andrew screenshot (Image #4): ACCOUNTS card shows `— small (<$40k)` instead of count.
**Investigation:** FE reads `bookData.book.small_account_count` (AdvisorBookView.tsx L421). D_02 emits `summary.small_account_count` (B9b, L1474). D_04 never mapped it.

### DS change — D_04 (CLOUD, 4299e1c0)

**File:** `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`
**Location:** `build_advisor_summaries()`, `summary.book` dict, ~L690

Added one line:
```python
'small_account_count': book_summary.get('small_account_count', 0),
```
Additive. No portal code change required.

---

## 3. Book Growth (TTM) tile — wired from hardcoded null

**Trigger:** Andrew screenshot (Image #5): "BOOK GROWTH (TTM)" shows `—`. Comment in AdvisorBookView.tsx:
> "nna_ttm pending per the CTO ping. Rendering em-dash until the emit lands."

**Investigation:** D_02 B3c already emits `growth.ttm_nna` + `growth.ttm_pct`. D_04 maps `growth: book.get('growth', {})`. The `AdvisorGrowth` type lacked `ttm_nna`/`ttm_pct` and the prop was hardcoded `null`.

### Portal changes (portal DEV, 060cf8b)

**`types.ts`:**
```typescript
export interface AdvisorGrowth {
  ytd_pct: number
  qtd_pct: number
  ttm_nna?: number   // Trailing-12-month NNA ($) — D_02 B3c
  ttm_pct?: number   // TTM NNA / period-start AUA
}
```

**`AdvisorBookView.tsx`:**
```diff
- bookGrowth={null}
+ bookGrowth={bookData.book.growth?.ttm_nna ?? null}
```

No backend change needed. Will render after gold rerun.

---

## 4. Lifetime Activity chart — role_aua split denominator fix

**Trigger:** RD flagged: chart AUA values = 1/5 of leaderboard for Travis Penfield (architect 80.7M chart vs 400M leaderboard). Root cause: `_emit_role_aua_shadow` used total role slots on account as denominator; D_00c leaderboard uses per-(advisor × account) slot count.

### DS change — D_02 (CLOUD, 6f724293)

**File:** `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py`
**Function:** `_emit_role_aua_shadow()`

Before (buggy):
```python
# Pre-melt: divide by ALL advisors on account
merged['_n_roles'] = merged[team_cols].notna().sum(axis=1)  # total slots
merged['_aua_share'] = merged['total_aua'] / merged['_n_roles']
melted = merged.melt(id_vars=['account_id', '_aua_share'], ...)
```

After (fixed):
```python
# Post-melt: divide by THIS advisor's roles on this account only
melted = merged.melt(id_vars=['account_id', 'total_aua'], ...)
n_roles_per_pair = melted.groupby(['account_id', 'advisor'])['role'].transform('size')
melted['_aua_share'] = melted['total_aua'].fillna(0.0) / n_roles_per_pair
```

`source_filter_stack` updated to `'p1_shadow_per_pair_split_no_fee_bucket_no_flow_join'`.

Added `--backfill-role-aua` CLI flag. **AE must run once:**
```
python D_02.advisor_client_detail.py --upload --backfill-role-aua
```
Iterates all unique dates in `acct`, regenerates every `gold/canonical/role_aua/{date}.parquet` partition. Normal runs (no flag) emit latest date only.

---

## Commit Summary

| SHA | Branch | Files | Description |
|---|---|---|---|
| 42be5b21 | CLOUD | D_02 | ADVI_ROLGAT: emit small_account_clients[] per role |
| 4299e1c0 | CLOUD | D_00, D_04 | Firm fee splits + advisor small_account_count passthrough |
| 6f724293 | CLOUD | D_02 | role_aua split fix (n_roles_per_pair) + --backfill-role-aua flag |
| 060cf8b | portal DEV | types.ts, AdvisorBookView.tsx | TTM wire-up + ADVI_ROLGAT portal types + SmallAccountsByRoleModal |

## Pending Actions

- **AE**: Run `python D_02.advisor_client_detail.py --upload --backfill-role-aua` to regenerate all role_aua partitions.
- **All**: Gold rerun (--group D) required before any frontend changes are visible in live portal. COO coordinates PROD trigger post-FIX6 close.
- **Firm Overview fee splits** (Image #3, fee-paying/non-fee-paying client count + AUA): requires gold rerun after D_00 4299e1c0 lands in S3.
