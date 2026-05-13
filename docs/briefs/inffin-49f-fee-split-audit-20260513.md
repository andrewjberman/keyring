# INFFIN 49F BD-pipeline Fee-Split Audit

**Author:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-13
**TO:** ADVI_INFFIN.005 (P1, ~2-3h investigation deliverable)
**Audience:** 2.0.0_SA_COO (RAVC), 0.4.0_DS_ClientPlatform~C (.003 INF schema normalization)
**Purpose:** Audit 49F BD-pipeline fee-split emit shape; produce schema-parity recommendations for INF normalization.

## 1. Executive Summary

49F's BD-pipeline emits a **richer, fee-aware advisor book.json schema** than INF's current advisor book.json. Key structural divergence: 49F uses a top-level `book` block carrying 4 AUA-state fields (`fee_earning_aua / non_fee_earning_aua / tagged_aua / total_aua`) + 2 account-count fields (`fee_earning_account_count / non_fee_earning_account_count`) + revenue fields (`implied_annual_revenue / avg_fee_bps_earned`). INF currently emits these scattered between `headline` and `headline.billing` sub-blocks with different field names, and crucially **omits 5 fields**: `non_fee_earning_aua`, `non_fee_earning_account_count`, `implied_annual_revenue`, `avg_fee_bps_earned`, and per-client `is_fee_paying`.

49F has a separate top-level **`fee_summary`** block carrying `weighted_avg_fee_bps + annual_implied_revenue + by_role[] + (FE type also has by_account[])`. INF has no equivalent — fee aggregations live inside `headline.billing`. The FE consumes `FeeSummaryByAccount` shape across both partners (single accessor), so INF must emit a parallel `fee_summary` block for the FeeSummaryPanel to render on Inflection.

Per-client `is_fee_paying` flag is **the most material gap** — INF clients[] has zero coverage (all 199 sampled = `None`). 49F has it populated 100% as boolean. Andrew's directive ("DS can look into implementation for 49 as well to try and keep shapes similar") points to mirroring 49F's `book.clients[].is_fee_paying` semantic for INF.

Recommendation summary: **6 INF additions** (mirror 49F shape) + **3 INF renames** (cosmetic alignment) + **1 structural reshape** (`headline.billing → book + fee_summary` top-level blocks). All 49F fields have clean non-null emit semantics per audit; no BD-pipeline cleanup TO needed from this audit.

## 2. 49F Per-Account Fee Field Inventory

**Source script:** `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py`
**S3 emit:** `s3://opal-data-bd/platinum/advisors/{advisor_key}/summary.json`

### Top-level `book` block (per-advisor)

Sampled `abby_horton/summary.json`:

| Field | Type | Sample value | Null-state |
|---|---|---|---|
| `book_name` | str | `"Abby Horton"` | Never null (advisor display name) |
| `client_count` | int | `13` | Never null (integer count, 0 if empty book) |
| `account_count` | int | `26` | Never null |
| **`fee_earning_account_count`** | int | `24` | Never null (0 if no fee-earning accounts) |
| **`non_fee_earning_account_count`** | int | `2` | Never null |
| `small_account_count` | int | `5` | Never null |
| `total_aua` | float | `4214083.48` | Never null |
| `tagged_aua` | float | `4214083.48` | Never null (= total_aua when 100% tagged) |
| **`fee_earning_aua`** | float | `4093767.53` | Never null |
| **`non_fee_earning_aua`** | float | `120315.94` | Never null |
| **`implied_annual_revenue`** | float | `17588.33` | Never null |
| **`avg_fee_bps_earned`** | float | `42.96` | Never null (literal 0.0 when `fee_earning_aua == 0`) |
| `nna_qtd` | float | `376676.94` | Never null |
| `nna_ytd` | float | `444026.94` | Never null |
| `nna_mtd` | float | `28946.19` | Never null |
| `growth` | dict | `{ytd_pct, qtd_pct, ttm_nna, ttm_pct}` | Never null |

### Emit logic (BD D_02:1281-1299)

```python
fee_earning_mask = advisor_splits > 0
if billable_account_ids is not None:
    fee_earning_mask = fee_earning_mask & snap_latest['account_id'].astype(str).isin(billable_account_ids)
fee_earning_aua = float(snap_latest.loc[fee_earning_mask, 'total_aua'].sum())
non_fee_earning_aua = float(snap_latest.loc[~fee_earning_mask, 'total_aua'].sum())
fee_earning_account_count = int(snap_latest.loc[fee_earning_mask, 'account_id'].nunique())
non_fee_earning_account_count = int(snap_latest.loc[~fee_earning_mask, 'account_id'].nunique())
implied_annual_revenue = float((advisor_fee_dollars * billable_mask).sum())  # accounts that are billable
avg_fee_bps_earned = (implied_annual_revenue / fee_earning_aua * 10000 if fee_earning_aua > 0 else 0.0)
```

**Critical:** 49F's `fee_earning_mask` = `(advisor_splits > 0) AND (account_id in billable_account_ids)`. Both conditions required. Accounts with split > 0 but NOT in the billable set are non-fee-earning. Accounts in the billable set but with split == 0 are non-fee-earning.

### Per-client `is_fee_paying` (book.clients[])

Sampled `abby_horton/summary.json.book.clients[0]`:

```json
{
  "client_key": "z08324782",
  "client_name": "Horton, Eric & Alison",
  "aua": 867538.7,
  "is_fee_paying": true,
  "small_account_count": 0,
  "relationship_since": "2025-02-18"
}
```

**Logic (BD D_02:1373):** "Per-relationship `is_fee_paying`: True if any account in the relationship..." (boolean OR across accounts; True if any account is fee-earning).

**Null-state:** Always emitted as boolean (true/false). Never null. 100% coverage on 49F sampled book.

## 3. 49F Per-Period Fee-Split Field Inventory

**Source script:** `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py` lines 1017, 1065 (`weighted_avg_fee_bps` emit).

49F **does NOT have per-period fee-split parallel emit** (e.g., `aua_fee_paying_qtd / aua_no_fee_qtd`). Fee-split fields are point-in-time (latest snapshot) only. Per-period AUA is in `nna_qtd / nna_ytd / nna_mtd` (single AUA-state per period, no fee-split partition).

49F also has `mix_periods` top-level array (per-quarter quarter-end snapshots) carrying `period, total_aua, nna_canonical` — but again no fee-state partition per period.

**Conclusion for Surface #8 parity (fee-paying / no-fee toggle reactivity):** 49F FE drives the toggle from the per-account `is_fee_paying` flag + `book.fee_earning_aua / non_fee_earning_aua` headline totals. There's no separate per-period fee-paying timeseries to mirror — the toggle filters the existing AUA snapshot, not switches between two pre-computed series.

If INF wants reactive toggle parity with 49F, the necessary DS emit is the SAME 4 AUA fields + per-client `is_fee_paying` — FE handles the toggle reactivity from those, no additional per-period fields needed.

## 4. 49F Red-Flag Account Handling

49F's `book` block does NOT emit `null` for any fee fields. The pattern is:

- **`fee_earning_aua == 0`** → emit literal `0.0`, never `null`. Downstream calculations gracefully handle zero division (`avg_fee_bps_earned` returns `0.0` when divisor is zero).
- **`non_fee_earning_aua == 0`** → emit literal `0.0`.
- **`fee_earning_account_count == 0`** → emit literal `0`.

**No sentinel `fee_structure` field** at the account or advisor level in the sampled 49F shape. Red-flag accounts (e.g., billable but $0 fee = pricing anomaly) are NOT separately surfaced in the summary.json emit — they're absorbed into the standard fee-earning vs non-fee-earning partition based on the `billable_account_ids` set membership at line 1283.

**Implication:** 49F has implicit "fee-paying = (split > 0) AND (billable)" definition. The 2-of-2 condition is the structural truth. There's no special handling for accounts that LOOK fee-earning but aren't (e.g., billable set membership = false despite split > 0) — those just flow to non-fee-earning bucket cleanly.

**Recommendation for INF:** Match the same 2-of-2 definition. If Inflection has accounts in a billable cohort but with $0 fee, those should land in `non_fee_earning_*` cleanly without `null` sentinels.

## 5. 49F FE Accessor Canonical Shape

**File:** `portal/src/pages/AdvisorIntelligence/_shared/tabs/FeeSummaryPanel.tsx`

The FE consumes the type `FeeSummaryByAccount` defined in `_shared/types.ts:1807-1817`:

```typescript
export interface FeeSummaryByAccount {
  weighted_avg_fee_bps: number
  annual_implied_revenue: number
  window_revenue?: {
    qtd: { firm_revenue_usd: number; advisor_revenue_usd: number }
    ytd: { firm_revenue_usd: number; advisor_revenue_usd: number }
    max: { firm_revenue_usd: number; advisor_revenue_usd: number }
  }
  by_account: FeeAccountBreakdown[]
}
```

Per-account breakdown:

```typescript
export interface FeeAccountBreakdown {
  account_id: string
  fee_bps: number
  aua: number
  team_attribution?: FeeAccountTeamShare[]
}

export interface FeeAccountTeamShare {
  advisor_id: string
  display_name: string
  fee_share_usd: number
  fee_share_bps?: number
  window_fee_share_usd?: { qtd: number; ytd: number; max: number }
}
```

**Critical:** The FE's `FeeSummaryByAccount` is the SHARED ACCESSOR Andrew wants. Both 49F + INF FeeSummaryPanel mount this type. INF's emit MUST conform to this contract for the panel to render — currently it does NOT (no `fee_summary` block at all in INF summary.json).

**Empirical sample (49F abby_horton.summary.json.fee_summary):**
```json
{
  "weighted_avg_fee_bps": 43.0,
  "annual_implied_revenue": 17588.33,
  "by_role": [
    {"role": "implementor", "aua": 3444661.92, "fee_bps": 46.8, "pct_of_book": 0.8414},
    {"role": "consultant",  "aua": 328349.05, "fee_bps": 20.6, "pct_of_book": 0.0802},
    {"role": "architect",   "aua": 320756.56, "fee_bps": 25.0, "pct_of_book": 0.0784}
  ]
}
```

Note: 49F currently emits `by_role[]` but the TYPE expects `by_account[]`. Either the FE adapter handles `by_role` separately OR `by_account[]` is emitted in a different artifact (composition.json or per-relationship view). Worth COO/CTO clarification.

## 6. Cross-Firm Field Categorization

| Field | 49F | INF | Category | Recommendation |
|---|---|---|---|---|
| `book.book_name` | YES (top-level `book`) | YES (top-level `book_name`) | DIVERGENT-STRUCTURE | INF: nest under top-level `book` |
| `book.client_count` | YES (`book.client_count`) | YES (`headline.client_count`) | DIVERGENT-STRUCTURE | INF: move to `book.client_count` |
| `book.account_count` | YES (`book.account_count`) | YES (`headline.account_count`) | DIVERGENT-STRUCTURE | INF: move to `book.account_count` |
| `book.fee_earning_account_count` | YES (`book`) | YES (`headline.billing.fee_earning_account_count`) | DIVERGENT-STRUCTURE | INF: move to `book.fee_earning_account_count` |
| `book.non_fee_earning_account_count` | YES (`book`) | **MISSING** | 49F-ONLY | INF: ADD to `book.non_fee_earning_account_count` |
| `book.small_account_count` | YES (`book`) | **MISSING** | 49F-ONLY | INF: ADD (semantic — sub-$100K account count) |
| `book.total_aua` | YES (`book`) | YES (`headline.total_aua`) | DIVERGENT-STRUCTURE | INF: move to `book.total_aua` |
| `book.tagged_aua` | YES (`book`) | YES (`headline.tagged_aua`) | DIVERGENT-STRUCTURE | INF: move to `book.tagged_aua` |
| `book.fee_earning_aua` | YES (`book`) | YES (`headline.billing.fee_earning_aua`) | DIVERGENT-STRUCTURE | INF: move to `book.fee_earning_aua` |
| `book.non_fee_earning_aua` | YES (`book`) | **MISSING** | 49F-ONLY | INF: ADD `book.non_fee_earning_aua = total_aua - fee_earning_aua` |
| `book.implied_annual_revenue` | YES (`book`) | YES (`headline.billing.total_fee_amount`) | DIVERGENT-NAME | INF: rename `total_fee_amount → implied_annual_revenue` |
| `book.avg_fee_bps_earned` | YES (`book`, bps) | YES (`headline.billing.weighted_avg_annual_fee_pct`, pct) | DIVERGENT-NAME-UNIT | INF: rename `weighted_avg_annual_fee_pct → avg_fee_bps_earned`; convert pct (1.024) → bps (102.4) |
| `book.nna_qtd / nna_ytd / nna_mtd` | YES (`book`) | YES (`headline.ytd_nna`) | DIVERGENT-STRUCTURE+SCOPE | INF: add `nna_qtd / nna_mtd`; rename `ytd_nna → nna_ytd`; move all under `book` |
| `book.growth` | YES (`book.growth = {ytd_pct, qtd_pct, ttm_nna, ttm_pct}`) | **MISSING** | 49F-ONLY | INF: ADD `book.growth` dict |
| `book.clients[].client_key` | YES | YES | IDENTICAL | (no change) |
| `book.clients[].client_name` | YES | NO (uses `display_name`) | DIVERGENT-NAME | INF: rename `display_name → client_name` |
| `book.clients[].aua` | YES | YES | IDENTICAL | (no change) |
| **`book.clients[].is_fee_paying`** | YES (bool, 100% coverage) | **MISSING** | 49F-ONLY | **INF: ADD per-client `is_fee_paying` (primary Andrew ask)** |
| `book.clients[].small_account_count` | YES | NO (has `account_count`) | DIVERGENT-NAME | INF: rename or ADD parallel |
| `book.clients[].relationship_since` | YES | YES | IDENTICAL | (no change) |
| `fee_summary` (top-level block) | YES (full FeeSummaryByAccount-shape) | **MISSING** | 49F-ONLY | **INF: ADD top-level `fee_summary` block (FE FeeSummaryPanel mounts this)** |
| `distribution` (top-level) | YES (per-advisor AUA histogram) | NO | 49F-ONLY | Out-of-scope for fee-split audit; flag for follow-on |
| `mix` / `mix_periods` (top-level) | YES | NO mix; INF has `composition` (different shape) | DIVERGENT-STRUCTURE | Out-of-scope; existing INF ADVI_INFTGT Brief #11 in flight |
| `top_holdings` (top-level) | NO | YES | INF-ONLY | (keep INF unchanged) |
| `tax_exposure` (top-level) | YES | NO at top-level (under `summary` block?) | DIVERGENT-STRUCTURE | Out-of-scope |
| `role_breakdown` (top-level) | YES | NO at top-level | DIVERGENT-STRUCTURE | Out-of-scope |
| `concentration` (top-level) | YES | NO at top-level | DIVERGENT-STRUCTURE | Out-of-scope |
| `active_since` (top-level) | YES | NO | 49F-ONLY | Out-of-scope (separate ADVI_INFTGT TO-9 closed earlier today) |

## 7. Normalization Recommendations for DS~C INF Schema (.003 scope)

### 7.1 Critical (Surface #6 + #8 primary asks)

**Add per-client `is_fee_paying` (boolean, 100% coverage required):**
- Emit in `book.clients[].is_fee_paying` (after Step 7.2 restructure)
- Logic: True if any account in the relationship has split > 0 AND billable
- **Andrew flagged this as the leading gap** — this is the highest-priority emit.

**Add `book.non_fee_earning_aua` + `book.non_fee_earning_account_count`:**
- Mirror 49F's two-bucket partition exactly
- Logic: `non_fee_earning_aua = total_aua - fee_earning_aua`
- Same for accounts

**Add top-level `fee_summary` block:**
- Must conform to FE `FeeSummaryByAccount` type
- Minimum fields: `weighted_avg_fee_bps`, `annual_implied_revenue`, `by_role[]` (for current FE adapter); `by_account[]` per type spec (clarify with COO/CTO on whether 49F's `by_role[]` is shimmed or `by_account[]` should be authoritative)

### 7.2 Structural reshape (top-level book block)

Move INF's `headline` + `headline.billing` fields into a top-level `book` block matching 49F:

```python
# BEFORE (INF current shape)
{
  "headline": {
    "total_aua": ...,
    "tagged_aua": ...,
    "account_count": ...,
    "client_count": ...,
    "ytd_nna": ...,
    "billing": {
      "fee_earning_account_count": ...,
      "fee_earning_aua": ...,
      "total_fee_amount": ...,
      "weighted_avg_annual_fee_pct": ...,
    }
  }
}

# AFTER (49F-parity shape)
{
  "book": {
    "book_name": ...,
    "client_count": ...,
    "account_count": ...,
    "fee_earning_account_count": ...,
    "non_fee_earning_account_count": ...,        # NEW
    "small_account_count": ...,                  # NEW (optional but recommended)
    "total_aua": ...,
    "tagged_aua": ...,
    "fee_earning_aua": ...,
    "non_fee_earning_aua": ...,                  # NEW
    "implied_annual_revenue": ...,               # RENAMED from total_fee_amount
    "avg_fee_bps_earned": ...,                   # RENAMED + UNIT FIX (pct→bps)
    "nna_qtd": ...,                              # NEW (currently only ytd)
    "nna_ytd": ...,                              # RENAMED from ytd_nna
    "nna_mtd": ...,                              # NEW
    "growth": {"ytd_pct": ..., "qtd_pct": ..., "ttm_nna": ..., "ttm_pct": ...},  # NEW
    "clients": [...]
  }
}
```

**Important:** This is a STRUCTURAL RESHAPE, not just additions. Existing INF FE consumers reading `headline.billing.*` will break unless adapter logic is added OR the rewrite is paired with FE consumer migration. Recommend phased approach:

1. **Phase 1 (this normalization):** ADD the new fields under `book.*` while KEEPING the existing `headline.*` + `headline.billing.*` for backward-compat. Both blocks emit.
2. **Phase 2 (DE follow-up PR):** FE migrates consumers from `headline.*` → `book.*` paths. Once all consumers migrated, DS removes `headline.*` legacy emit (or marks deprecated).

This phased approach mirrors how I handled the legacy `activity_scan.json` preservation pattern in commit `f244b425a` — additive ship with backward-compat preserved until FE migration completes.

### 7.3 Per-client schema rename

```python
# BEFORE (INF current)
{
  "household_id": 226,
  "client_key": "226",
  "display_name": " Judith Ozinga",
  "aua": 4617355.0,
  "account_count": 3,
  "ytd_nna": -789620.0,
  "relationship_since": "2023-10-02"
}

# AFTER (49F-parity)
{
  "client_key": "226",
  "client_name": "Judith Ozinga",                # RENAMED from display_name (also: trim leading space)
  "aua": 4617355.0,
  "is_fee_paying": True,                          # NEW (primary Andrew ask)
  "small_account_count": 1,                       # NEW (sub-$100K accounts in this relationship)
  "relationship_since": "2023-10-02",
  # Backward-compat (Phase 1 keep):
  "household_id": 226,                            # INF-ONLY (keep, used by drill nav)
  "display_name": " Judith Ozinga",              # KEEP (legacy alias)
  "account_count": 3,                             # INF-ONLY (keep)
  "ytd_nna": -789620.0                            # INF-ONLY (keep)
}
```

### 7.4 fee_summary block emit (FeeSummaryByAccount-conformant)

```python
{
  "fee_summary": {
    "weighted_avg_fee_bps": float,           # advisor-level weighted avg
    "annual_implied_revenue": float,         # advisor-level total
    "by_role": [                             # optional but 49F-parity
      {"role": "implementor", "aua": ..., "fee_bps": ..., "pct_of_book": ...},
      {"role": "consultant", ...},
      {"role": "architect", ...}
    ],
    "by_account": [                          # per FeeAccountBreakdown type
      {
        "account_id": str,
        "fee_bps": float,
        "aua": float,
        "team_attribution": [...]            # optional per FeeAccountTeamShare
      }
    ]
  }
}
```

Open question for clarification: 49F currently emits `by_role[]` but the FE TYPE specifies `by_account[]`. Either (a) the type is forward-looking and FE has a 49F-specific adapter shimming role↔account, or (b) `by_account[]` is emitted elsewhere (different artifact). Resolve before final INF emit shape.

## 8. 49F Null-Elimination State Audit

**Result: 49F has clean null-elimination discipline. No fee fields emit `null` in sampled summary.json.**

All numeric fee fields (`fee_earning_aua`, `non_fee_earning_aua`, `fee_earning_account_count`, `non_fee_earning_account_count`, `implied_annual_revenue`, `avg_fee_bps_earned`) emit literal `0.0` or `0` (integer) when there's no fee-earning state. Per-client `is_fee_paying` emits literal `false` boolean, never `null`.

**No BD-pipeline cleanup TO needed from this audit** for the 49F side. The pattern is already canonical: zero, not null.

**Implication for INF:** When INF's normalization lands, the same discipline applies — emit `0.0` / `0` / `false` for absent state, never `null`. Andrew's "no nulls in production" directive already drives this; the 49F precedent confirms it works at firm scale.

## 9. Open Questions

1. **`fee_summary.by_account[]` vs `by_role[]`:** 49F currently emits `by_role[]` but FE TYPE spec is `by_account[]`. Single-source-of-truth ambiguity. CTO/Andrew clarification needed before INF emits.

2. **`small_account_count` definition:** 49F has it at both `book.small_account_count` (firm-level count) and `book.clients[].small_account_count` (per-client). What's the threshold ($100K? $50K?). Worth empirical check across more 49F advisors to confirm sub-threshold rule.

3. **`avg_fee_bps_earned` 0.0 default semantic:** When `fee_earning_aua == 0`, 49F emits `0.0`. But conceptually that means "no fee data" not "zero fees." Is this acceptable for FE rendering, or should it use a different sentinel (e.g., omit the field)? Cross-ref Andrew's `manual_review` bucket for `Remark` — same class of question.

4. **`mix_periods` parity scope:** 49F has top-level `mix_periods` array (per-quarter snapshots). INF's parity is in flight via ADVI_INFTGT Brief #11 (chain #25 noted as MISSING; will fix at chain #25 with v1.7.53 Lambda). Out of scope here; flag for cross-reference in DS~C .003.

5. **`distribution`, `concentration`, `tax_exposure`, `role_breakdown` top-level blocks:** 49F has these; INF doesn't at top-level. Each is its own scope item — INFFIN focuses on fee-split; these are independent surfaces. Recommend separate TOs for the rest (likely ADVI_INFFIN.006+ or new project codes).

6. **`active_since` field:** 49F has top-level `active_since`. ADVI_INFTGT TO-9 closed earlier today added INF AdvisorAnalytics panel with this. Confirm INF schema has `active_since` at the correct level (maybe `book.active_since` for advisor lifetime).

---

## Cross-References

- TO: `org/tier1_exec/2.0.0_SA_COO/task_orders/ADVI_INFFIN.005.dsb-49f-fee-split-audit.md`
- 49F source script: `data/black_diamond/scripts/gold/D_02.advisor_client_detail.py:1281-1299, 1373`
- 49F S3 sample: `s3://opal-data-bd/platinum/advisors/abby_horton/summary.json`
- INF S3 sample: `s3://opal-data-inf/platinum/advisors/peter_lee/book.json`
- FE accessor: `portal/src/pages/AdvisorIntelligence/_shared/tabs/FeeSummaryPanel.tsx`
- FE types: `portal/src/pages/AdvisorIntelligence/_shared/types.ts:1779-1817`
- DE INFFIN brief: `docs/briefs/inflection-finalize-20260513.md` (§Surface #6 + §Surface #8)
- Sibling TO: `.003` DS~C INF emit batch (consumes this audit's recommendations)

— 0.4.0_DS_ClientPlatform~B 2026-05-13
