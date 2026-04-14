# 0.4.0_DS_ClientPlatform -- Full Session Log

**Date:** 2026-04-14 (EDT)
**Session span:** ~12:30 EDT to ~14:45 EDT
**Agent:** 0.4.0_DS_ClientPlatform

---

## Startup Reconciliation

Registered (PID 25028). Inbox empty on startup.

Four stale TO statuses corrected — all completed last session (2026-04-13) but not flipped:

| TO | Was | Now | Evidence |
|---|---|---|---|
| ADVI_OFFICE.W1 | pending | complete | commit 27471bed |
| ADVI_REBORN.W6-003 | pending | complete | commit 1d70ecaf |
| ADVI_GLDRST.021 | staged | complete | commit 9b4f7a77 |
| ADVI_GLDRST.021b | staged | complete | session log 2026-04-10 |

Commit: `f48ab17f`

---

## TOs Completed This Session

| Work Item | Type | Commit | S3 |
|---|---|---|---|
| D_00b fix #3 — OFC 1-office anomaly | Bug fix | `5b4439e1` | opal-data-bd/code/gold/D_00b — etag b1255ef7 |
| PROFAU.003 QA — platinum field verification | QA | (no code) | — |
| D_02 all-role canonical NNA + per-role breakdown | Feature | `d51e44ef` | opal-data-bd/code/gold/D_02 — etag bfa23e22 |

---

## D_00b Fix #3 — OFC 1-office aggregation anomaly

**Problem (from COO/AE):** D_00b produced `ofc: 2290 days, 1 offices` — 178 advisors loaded from the dim file but all relationships collapsed to a single bucket ("Other").

**Root cause:** `_build_rel_office_dim_d00b` built dict keys using `str(rid)` where `rid` is a float64 value (pandas coerces `relationship_id` to float64 when any NaN exists in the column). This produces `"12345.0"` keys. `_build_office_view` looked up those keys via `perf['relationship_id'].astype(str)` where `perf` has int64 `relationship_id` (from `account_performance` groupby), producing `"12345"` keys. Every lookup missed → all `fillna('Other')` → `top_offices` empty → `ofc_categories = ['Other']` → 1 office.

Note: the prior fix (`15512bed`) added `relationship_id` to `_AT_COLS` which was a prerequisite (without it, `_build_rel_office_dim_d00b` returned `{}` immediately). But the type mismatch was a second independent layer.

**Fix:** `try: rid_str = str(int(rid)) except: rid_str = str(rid)` at line 262. `int(12345.0)` = `12345`, `str(12345)` = `"12345"` — matches int64 `.astype(str)` output.

**Signals sent:** AE (0.6.0_AE_PartnerETL) GO for W2 + PROFAU.003 QA check bundled; COO status.

---

## PROFAU.003 QA — platinum field verification

**Triggered by:** COO message (D_03+D_04 ran locally at 14:09 UTC).

**Verified** across `platinum/advisors/travis_penfield`, `abby_horton`, `aj_lenartowicz`:

```
tax_exposure.capital_gains_ttm:   PRESENT (float, e.g. 0.0)
tax_exposure.cost_basis_by_year:  PRESENT (list of {purchase_year, cost_basis,
                                   market_value, unrealized_gain}, 30 entries)
tax_exposure.tax_exposure_fee_paying:  PRESENT (PROFAU.002 confirmed simultaneously)
tax_exposure.tax_exposure_no_fee:      PRESENT
```

Structural note for DE: `cost_basis_by_year` is a **list**, not a dict — component must iterate by index or `purchase_year` field.

**Signals sent:** DE (0.4.0_DE_ClientPlatform) unblocked for PROFAU.006 (TaxCostBasisPanel L2 wire); COO notified.

---

## D_02 — All-role canonical NNA + per-role breakdown

**Triggered by:** Andrew's investigation of Travis Penfield AdvisorPublicProfile showing two different lifetime NNA numbers ($253M Summary vs $221M Lifetime Activity).

### Investigation findings

Both panels use canonical NNA (transaction-based) but with different account attribution models:

| Panel | Source | Account scope | Value |
|---|---|---|---|
| Summary FLOWS | `employee_leaderboard.json` (D_00c) | ALL accounts where advisor has any role | $253M |
| Lifetime Activity | `timeseries.json` (D_02) `nna_canonical` | Accounts where advisor is first-encountered via global `drop_duplicates('account_id')` (architect-priority) | $221M |

The $31.8M gap = NNA from accounts where Travis is implementor/consultant/additional_advisor and another advisor is the architect. D_02's global `account_to_advisor` dict (built via `melted.drop_duplicates('account_id')`) assigned those accounts to the other advisor.

Delta breakdown: D_00c has +$9.7M more inflows and -$22.2M fewer outflows than D_02 canonical — consistent with Travis's non-architect accounts having different flow profiles.

Also confirmed: `deriveFlows()` function in AdvisorPublicProfile.tsx uses old `nna`/`cum_inflows`/`cum_outflows` fields but is marked `void` (unused). Summary FLOWS values come from `entry.inflows/outflows/nna` (leaderboard). Lifetime Activity hero metrics come from `last.nna_canonical - first.nna_canonical`.

### Fix

**Andrew's decision:** both panels should use "total NNA across all accounts the advisor touches" AND the data should be parseable by role.

Three changes to D_02:

**1. Preserve `_role` in melt loop:**
```python
sub['_role'] = role  # added in available_roles iteration
```

**2. Build `acct_adv_role` with equal-weight splits (before AUA dedup):**
```python
acct_adv_role = melted.drop_duplicates(subset=['account_id', 'advisor_name', '_role'])
acct_adv_role['weight'] = 1.0 / groupby(['account_id', 'advisor_name'])['_role'].transform('count')
```
Weight = `1/n_roles` per `(account, advisor)` so `sum(role_nna) == total_nna`. Mirrors D_00c's equal-split model.

**3. `_load_canonical_nna_per_advisor` refactored:**
- Old: single `{account_id: advisor_name}` dict → one advisor per account (architect wins)
- New: accepts `acct_adv_role` DataFrame → `merge` fans each account's daily NNA to every advisor tagged on it, multiplied by weight
- Returns `(date, advisor_name, _role, nna_txn_sum, inflow_sum, outflow_sum)` grain

**4. Two lookups built, two sets of fields emitted:**

```
canonical_lookup[(date, advisor_name)]          -> total nna_canonical (fixed, matches leaderboard)
role_canonical_lookup[(date, advisor_name, role)] -> per-role share
```

New fields in `timeseries.json` entries:
- `nna_canonical`, `inflows_canonical`, `outflows_canonical` — total (now correct)
- `architect_nna_canonical`, `implementor_nna_canonical`, `consultant_nna_canonical`,
  `local_ops_nna_canonical`, `additional_advisor_nna_canonical` — and `_inflows`/`_outflows` variants

Reconciliation guarantee: `sum({role}_nna_canonical) == nna_canonical` for every advisor-date.

After next D_02 gold run, Travis Penfield's Lifetime Activity will show `$253M` matching the Summary panel. Per-role fields are available for DE to wire up a role filter on the Lifetime Activity chart.

---

## MCP Signals Sent

| To | Subject | Outcome |
|---|---|---|
| 0.6.0_AE_PartnerETL | D_00b fix #3 GO + PROFAU.003 QA check | Delivered |
| 2.0.0_SA_COO | D_00b fix #3 shipped | Delivered |
| 2.0.0_SA_COO | PROFAU.003 QA confirmed | Delivered |
| 0.4.0_DE_ClientPlatform | PROFAU.003 confirmed, PROFAU.006 unblocked | Delivered |

---

## Compiler Tools

| Phase | Tool | Command | Result |
|---|---|---|---|
| D_00b investigation | Manual read | D_00b.portal_timeseries.py:248-267, 278 | Type mismatch root cause identified |
| D_00b investigation | Manual read | C_07.advisor_attribution.py:317-350 | Confirmed float64 coercion path |
| D_00b pre-commit | py_compile | D_00b.portal_timeseries.py | SYNTAX OK |
| PROFAU.003 QA | aws s3 cp | platinum/advisors/{3 advisors}/summary.json | capital_gains_ttm + cost_basis_by_year confirmed PRESENT |
| NNA investigation | aws s3 cp | platinum/advisors/travis_penfield/timeseries.json | nna_canonical=221M, inflows_canonical=410M traced |
| NNA investigation | aws s3 cp | platinum/firm/leaderboard.json | MAX nna=253M, inflows=419M traced |
| NNA investigation | comp-transform schema-check | AdvisorPublicProfile | entry source = leaderboard; deriveFlows() unused (void) |
| D_02 pre-commit | py_compile | D_02.advisor_client_detail.py | SYNTAX OK |
| comp-blast | Not run | Pure NNA attribution change, no new S3 keys or artifact shape changes | Blast radius unchanged vs prior |

comp-blast not run for D_02: the change is strictly additive (new fields in timeseries JSON entries, existing fields corrected in value). No new S3 key patterns, no schema removal, no downstream script dependencies on per-role canonical fields that would be affected.

---

## Do NOT Rules (session observations)

- Do NOT use `str(rid)` directly on a pandas float64 column value — use `str(int(rid))` for integer IDs that pandas may have coerced to float.
- Do NOT assume `drop_duplicates('account_id')` on a multi-advisor melted DataFrame gives the correct advisor scope — it picks one advisor per account (architect-priority), which is correct for deduplication but wrong for "all accounts this advisor touches" attribution.
- Do NOT compare leaderboard NNA and timeseries NNA without checking their account attribution models — they legitimately answer different questions and will differ unless explicitly aligned.
