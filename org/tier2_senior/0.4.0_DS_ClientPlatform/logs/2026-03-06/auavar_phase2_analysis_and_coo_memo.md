# ADVI_AUAVAR Phase 2: Missing Cube Account Analysis + COO Variance Memo — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Start Time:** 16:00
**End Time:** 17:00

## Objective

Analyze Phase 2 diagnostic results (895 missing cube accounts), complete the full gap
attribution, and produce the COO variance memo. This closes the DS deliverable chain
for ADVI_AUAVAR Phase 1.

---

## Work Completed

### 1. Read Phase 1 JSON from S3

Key facts extracted from `aua_gap_decomposition_2026-03-02.json`:
- `alloc_rows_per_account_avg = 1.0` — confirmed 6,326 unique accounts, one row each
- Allocations has `account_is_open`, `closed_date`, `account_type`, `cash_market_value` columns
- `gold_cash_total = $23.2M` — cube counts cash positions at price=1.0
- `alloc_cash_total = null` — allocations has no security_name column (portfolio-level, not position-level)

### 2. Designed and Committed Phase 2 Script

`diag_aua_missing_cube_accounts.py` — classifies the 895 accounts using:
- BD's own `account_is_open` flag
- `closed_date` and `relationship_termination_date` presence
- `account_type` distribution
- `accounts_dimension` cross-reference with status columns
- 90-day transaction history check (parallel load, 32 workers)

Commits: `2b76456c` (script), `8078f1c0` (DT brief). DT executed via SSM (fee86061 pushed).

### 3. Analyzed Phase 2 Results

Results from `aua_missing_cube_accounts_2026-03-02.json`:

| Bucket | Count | BD MV | Classification |
|--------|-------|-------|----------------|
| Closed per BD (account_is_open=False) | 0 | $0 | — |
| Open + has transactions (B1) | 397 | $13.9M | Coverage gap — true bug |
| Open + no transactions (B2) | 498 | $90.1M | Explainable structural |

B2 breakdown:
- Insurance/Annuity/TermLife: 118 accts, ~$59.5M — non-investment products, no priced positions
- Mortgage/Loans/CC: 26 accts, -$3.5M — liability accounts, negative MV
- Cash-only/new (standard types, no txn history): ~354 accts, ~$34.1M

### 4. Full Gap Attribution

| Component | Amount | Type |
|-----------|--------|------|
| Non-investment products (insurance/annuity) | +$59.5M | Structural exclusion |
| Cash in gold cube (BD separates cash) | -$23.2M | Structural offset |
| Cash-only/new accounts | +$34.1M | Scope question |
| Coverage gap (open+active, not in cube) | +$13.9M | Addressable bug |
| Liability accounts | -$3.5M | Structural exclusion |
| Pricing/timing spread + set overlap | ~-$7.1M | Normal variance |
| **Total** | **+$73.6M** | |

### 5. Revised Apples-to-Apples Comparison

BD investment-only AUA (strip non-investment + liabilities): ~$1,571.6M
Gold non-cash AUA ($1,553.9M - $23.2M): $1,530.7M
True investable gap: **~$40.9M (2.6%)** — not $73.6M

Of that $40.9M:
- $34.1M = cash-only/new accounts (scope decision, not a bug)
- $13.9M = coverage gap in Script 02 filter chain (bug, low severity)
- -$7.1M = normal variance

### 6. Produced COO Variance Memo

`docs/briefs/data-scientist-auavar-variance-memo.md` — full waterfall, segment
detail, recommendations by type, and proposed "non-cash AUA" definition for
future BD comparisons.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Define "non-cash AUA" formally in memo | Prevents future confusion; gives COO a clear definition to reference |
| Classify coverage gap as low severity | $13.9M = 0.9% of AUA; no user-facing impact today |
| Recommend balance-feed scope decision for cash-only accounts | Cannot be resolved in gold layer without architectural change; COO decides |
| No immediate code change | All findings are diagnostic; implementation deferred pending COO review |

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| COO variance memo | `docs/briefs/data-scientist-auavar-variance-memo.md` | 2.0.0_SA_COO, 1.0.0_SA_CTO |
| DT brief (phase 2 run) | `docs/briefs/devops-brief-auavar-missing-cube-accounts-ec2-run.md` | 0.4.0_DT_ClientPlatform |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `data/black_diamond/scripts/diagnostics/diag_aua_missing_cube_accounts.py` | New | `2b76456c` |
| `docs/briefs/devops-brief-auavar-missing-cube-accounts-ec2-run.md` | New | `8078f1c0` |
| `docs/briefs/data-scientist-auavar-variance-memo.md` | New | `2badb2e5` |

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE (DS deliverables for ADVI_AUAVAR Phase 1)
**Active branch:** `CLOUD`

Full gap attribution is complete. COO memo committed at `2badb2e5`. The $73.6M gap
is fully explained: $59.5M structural (non-investment products), -$23.2M cash offset,
$34.1M scope question (cash-only/new accounts), $13.9M addressable coverage gap.
The true investment-only comparable gap is ~$40.9M (2.6%). No emergency.

---

## Next Steps

1. **[2.0.0_SA_COO] Review** `docs/briefs/data-scientist-auavar-variance-memo.md`
   - Approve non-cash AUA definition
   - Decide on balance-feed scope for ~354 cash-only/new accounts ($34.1M)

2. **[0.4.0_DE_ClientPlatform] Optional** — update portal AUA display to use
   non-cash AUA metric if COO approves the definition

3. **[0.4.0_DS_ClientPlatform] Follow-up** — investigate 397-account coverage gap
   in Script 02 filter chain (low priority, pending COO review of memo)

**Do NOT:**
- Modify Script 02 or any gold layer script before COO reviews the memo
- Net cash from portal AUA display without DE alignment
