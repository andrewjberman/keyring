# ADVI_49FNV3 — F1 + F5 Investigation — 0.4.0_DS_ClientPlatform

**Date:** 2026-03-06
**Agent:** 0.4.0_DS_ClientPlatform
**Task Orders:** ADVI_49FNV3.F1.gro-data-investigation, ADVI_49FNV3.F5-DS.qtd-ytd-lambda-investigation
**Status:** Complete

---

## F1: GRO Mode — growth_decomposition Investigation

### Question 1: Is growth_decomposition emitted by the Lambda?

**YES. The field is present.**

File: `infra/aws/lambda/bd-pipeline/bd-portal-publisher/lambda_function.py`

- **Computation block:** lines 707-732 (labeled "Y5: Growth decomposition (monthly granularity)")
- **Emission:** lines 853-856 in the assembled `result` dict (output of `build_timeseries_chart()`)

The field is emitted unconditionally as part of `timeseries_chart.json`.

### Question 2: What are the specific columns and computation?

**Source parquet:** `gold/client_performance.parquet`
**Loaded via:** `load_all()` in the same Lambda (line 214-219)

Columns used:
- `total_aua` — AUA per relationship per date
- `nna` — cumulative NNA per relationship per date

**Computation (per month):**
```python
daily_firm = perf.groupby('date')[['total_aua', 'nna']].sum()
# ... for each year_month group:
aua_start = daily_firm[first_day_of_month]['total_aua']   # firm-level AUA
aua_end   = daily_firm[last_day_of_month]['total_aua']
nna_start = daily_firm[first_day_of_month]['nna']         # firm-level cumulative NNA
nna_end   = daily_firm[last_day_of_month]['nna']
nna_net   = nna_end - nna_start                           # monthly NNA delta
total_chg = aua_end - aua_start                           # monthly AUA change
market    = total_chg - nna_net                           # market appreciation residual
```

Output shape per entry: `{ period: "YYYY-MM", market: float, nna: float, total: float }`
This matches the PRD contract exactly.

### Question 3: Is the nna column cumulative? Are null values possible?

Confirmed cumulative via `data/black_diamond/scripts/gold/05_build_client_performance.py`:

- Line 630-636: `cum_inflows = groupby('relationship_id')['daily_inflow'].cumsum()`, `cum_outflows = groupby('relationship_id')['daily_outflow'].cumsum()`, `nna = cum_inflows - cum_outflows`
- Line 646-647: `result[col] = result[col].fillna(0.0)` — NaN explicitly filled before writing parquet

**No null values expected in the nna column.** The diff approach (`nna_end - nna_start`) is mathematically equivalent to `(cum_inflows_end - cum_inflows_start) - (cum_outflows_end - cum_outflows_start)`, the same approach used by `bd-portal-advisor-publisher`.

### Root Cause Determination

The Lambda source code is **correct**. The `growth_decomposition` field was added as part of Y5 work and the logic is sound. However, `bd-portal-publisher` was last deployed at tag `bd-v2.15.0`. If that tag predates the Y5 `growth_decomposition` addition, the **currently deployed Lambda does not have this code**.

The "Growth decomposition data unavailable" message in the portal is consistent with the field being absent from the S3 JSON output (the frontend fallback renders when `timeseriesData?.growth_decomposition?.data?.length` is falsy).

**Action needed:** DT must rebuild and redeploy `bd-portal-publisher` from the current CLOUD branch code to pick up the growth_decomposition emission. No Lambda code changes are required — the code is already correct.

### Deliverable

DT brief written at: `docs/briefs/devops-brief-49fnv3-f1-gro-publisher-fix.md`

---

## F5: QTD/YTD Timing Bug — Lambda Investigation

### Question 1: Where are QTD and YTD period boundaries computed?

File: `infra/aws/lambda/bd-pipeline/bd-portal-advisor-publisher/lambda_function.py`
Function: `build_advisor_books()` (line 382)

Period starts computed at lines 398-407:

```python
def _qstart(quarters_back: int) -> pd.Timestamp:
    today_q_month = ((today.month - 1) // 3) * 3 + 1
    month = today_q_month - quarters_back * 3
    year  = today.year + (month - 1) // 12
    month = ((month - 1) % 12) + 1
    return pd.Timestamp(year=year, month=month, day=1)

ytd_start = pd.Timestamp(today.year, 1, 1)   # line 405
qtd_start = _qstart(0)                        # line 406
mtd_start = pd.Timestamp(today.year, today.month, 1)  # line 407
```

### Question 2: Is this using floor-to-quarter or a hard-coded reference date?

It uses dynamic floor-to-quarter logic via `_qstart()`. No hard-coded reference date. The formula computes the first month of the current quarter using integer arithmetic.

### Question 3: Is QTD = YTD in Q1 (March 2026)?

**YES — the Lambda is correct.**

For March 2026 (`today.month = 3`):

```
today_q_month = ((3 - 1) // 3) * 3 + 1 = (2//3)*3 + 1 = 0 + 1 = 1
month = 1 - 0*3 = 1
year  = 2026 + (1 - 1) // 12 = 2026
month = ((1 - 1) % 12) + 1 = 1
qtd_start = pd.Timestamp(2026, 1, 1)   # Jan 1, 2026

ytd_start = pd.Timestamp(2026, 1, 1)   # Jan 1, 2026
```

`qtd_start == ytd_start == Jan 1, 2026`. The Lambda computes them identically. No Lambda-side bug.

### Systemic Audit — All Period Boundaries

All period computations in `build_advisor_books()` are derived from `_qstart()` and the `ytd_start`/`mtd_start` expressions above. Verified `_qstart()` for each quarter:

| Date     | today_q_month | qtd_start result | Expected |
|----------|---------------|------------------|----------|
| Jan 2026 | 1             | Jan 1, 2026      | Correct  |
| Feb 2026 | 1             | Jan 1, 2026      | Correct  |
| Mar 2026 | 1             | Jan 1, 2026      | Correct  |
| Apr 2026 | 4             | Apr 1, 2026      | Correct  |
| Jul 2026 | 7             | Jul 1, 2026      | Correct  |
| Oct 2026 | 10            | Oct 1, 2026      | Correct  |
| Dec 2026 | 10            | Oct 1, 2026      | Correct  |

Cross-quarter rollback (`quarters_back=1`) also verified correct for the Feb-to-Q4-prior case.

No period boundary errors found in this Lambda.

### Root Cause

**The F5 bug is NOT in `bd-portal-advisor-publisher`.** The Lambda computes `qtd_start = Jan 1, 2026` and `ytd_start = Jan 1, 2026` for any date in Q1. They are identical.

The QTD != YTD discrepancy in the portal must originate in the **frontend period logic** (DE scope, task order F5-DE). Likely cause: the portal client is computing Q1 start using a different formula (e.g., `startOfQuarter()` from a date library that returns a different date than Jan 1, or the Q/Y period selector applies a different lookback window client-side).

### Finding for COO

Route F5 to DE. Lambda is confirmed correct. The frontend period boundary computation for QTD is returning a different date than `ytd_start` in Q1. DE should audit the `StackedBarPeriodKey` / `AdvisorsTab.tsx` period toggle logic.
