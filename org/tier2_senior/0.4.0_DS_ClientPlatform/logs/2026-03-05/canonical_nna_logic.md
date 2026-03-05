# Canonical NNA Logic -- 0.4.0_DS_ClientPlatform

**Date:** 2026-03-05
**Context:** Follow-up to REQ_schwab_sot_cross_reference (2026-03-04)

## Problem Statement

Our NNA computation treated all BD transaction types equally: any Cash Deposit, Cash
Withdrawal, Transfer In, or Transfer Out counted as NNA. This conflated three distinct
categories of money movement:

1. **Real NNA** -- money entering or leaving the firm (ACAT transfers, wire deposits,
   client contributions, IRA rollovers)
2. **Internal movements** -- money moving between Schwab accounts or BD portfolios
   (journals, Schwab-to-Schwab transfers)
3. **Operational noise** -- automated sweeps with no economic meaning (SEP account
   manager sweeps, FDIC bank sweeps)

Schwab's NNA definition explicitly excludes categories 2 and 3. Our failure to do the
same produced a 13-month NNA of $211.6M vs Schwab's $353M (-40% gap), with wild
month-to-month divergence including sign reversals (we show negative NNA when Schwab
shows positive).

## The `action` Field Discovery

BD's transaction data contains an `action` field distinct from `transaction_type`. While
`transaction_type` has only 4 NNA-relevant values (Cash Deposit, Cash Withdrawal,
Transfer In, Transfer Out), `action` has **15 distinct values** that map to flow intent:

### Action Taxonomy (NNA transactions only)

**EXTERNAL -- Real Custodial Transfers:**

| action | transaction_type | Meaning | 4-month volume |
|---|---|---|---|
| `TOA - LONG` | Transfer In | Position transferred in from another custodian | $71.0M (2,341 events) |
| `ACAT In` | Transfer In | Explicit ACAT transfer in | $20.2M (1,558 events) |
| `ACAT Out` | Transfer Out | Explicit ACAT transfer out | $3.7M (389 events) |
| `EF Transfer In` | Transfer In | External fund transfer in | $1.5M (90 events) |
| `EF Transfer Out` | Transfer Out | External fund out | $12.0M (922 events) |
| `Cash Deposit` | Cash Deposit | All cash deposits | $104.0M (4,505 events) |
| `Cash Withdrawal` | Cash Withdrawal | All cash withdrawals | $84.1M (15,651 events) |
| `Transfer In` | Transfer In | Generic transfer in | $84K (25 events) |
| `Transfer Out` | Transfer Out | Generic transfer out | $113K (13 events) |
| `Transfer In of Accrued Interest` | Transfer In | Accrued interest on transfer | $1.8K (8 events) |
| `REC - LONG` | Transfer In | Received long position | $5.8K (2 events) |
| `ADJ - SHORT` | Transfer Out | Position adjustment | $2.6K (4 events) |
| `VOID - CREDIT` | Cash Deposit | Voided check reversal | $203K (2 events) |

**INTERNAL -- Not Real NNA:**

| action | transaction_type | Meaning | 4-month volume |
|---|---|---|---|
| `JNL - LONG` | Transfer In | Position journaled IN between BD accounts | $6.2M (248 events) |
| `JNL - SHORT` | Transfer Out | Position journaled OUT between BD accounts | $4.4M (222 events) |

### The Critical Distinction

`JNL - LONG` and `JNL - SHORT` are the only Transfer In/Out actions that represent
**internal position movements**. These are model rebalances, account restructures, and
portfolio journals -- money moving within the firm, not entering or leaving it.

Under the old logic, a $340K Fidelity Balanced position journaled from account A to
account B counted as +$340K NNA inflow on B and -$340K NNA outflow on A. If B was in
our universe but A was not (or vice versa), the journal created phantom NNA. Even when
both accounts were present, timing differences between the LONG and SHORT legs could
produce phantom flows on individual days.

The `action` field is the **only field** that distinguishes these from real `TOA - LONG`
or `ACAT In` events. `transaction_type` alone cannot make this distinction -- both
journals and real ACATs show as `Transfer In` / `Transfer Out`.

### Field Reliability

| Field | Present since | Distinct values (NNA) | Deterministic? | Role |
|---|---|---|---|---|
| `action` | 2020-03-06 (earliest file) | 15 | YES | Primary classifier |
| `transaction_type` | 2020-03-06 | 4 | YES | Current primary (too coarse) |
| `external_flow` | 2020-03-06 | 3 | YES | Direction only (redundant) |
| `is_nna` / `is_nna_inflow` / `is_nna_outflow` | 2020-03-06 | 2 (string) | YES | BD's NNA scope flag |
| `description` | 2020-03-06 | ~4,000 unique | PATTERN-BASED | Sub-classify cash flows |
| `transaction_sub_type` | 2020-03-06 | 4 | NO VALUE ADD | Always equals transaction_type |

## Description-Based Cash Flow Classification

For Cash Deposit and Cash Withdrawal, `action` is always `Cash Deposit` or
`Cash Withdrawal` -- it doesn't sub-classify. The `description` field provides
deterministic string prefixes set by Schwab that identify the flow type.

### Exclusion Patterns (Not NNA)

| Pattern | What It Is | Evidence |
|---|---|---|
| `TRF BTWN SCH ACCTS` | Schwab-to-Schwab internal transfer | Schwab glossary: "Clients moving from existing Schwab platforms to an Advisor are not considered NNA" |
| `TO SEP ACCT MGR` | Operational sweep to separately-managed account manager | ~10,571 events over 4 months, average $207, median $54. Pure operational noise. |
| `TRANSFER FUNDS TO SCHWAB BANK` | FDIC bank sweep to Schwab Bank | Automated cash management, not client-directed flow |

### Inclusion Patterns (Real NNA)

| Pattern | What It Is | Volume (4 months) |
|---|---|---|
| `WIRED FUNDS IN/OUT` | Wire transfers | $25.4M in / $32.6M out |
| `MONEYLINK TRANSFER` | ACH from external bank | $13.3M in / $11.5M out |
| `*DEPOSIT IRA ROLLOVER CONT` | IRA rollover contribution | $27.4M in |
| `TRANSFER ACCOUNT TOA ACAT` | Cash component of ACAT | $10.6M in / $0.2M out |
| `IRA TRANSFER / DSTRIB` | IRA distributions | $14.6M out |
| `CONTRIBUTION` / `DEPOSIT FUNDS RECEIVED` | General deposits | $0.2M in |
| Everything else (checks, ATM, Venmo, etc.) | Misc client-directed flows | Small dollar, real flows |

## Implementation

### Changes Made

**Files modified:**
- `data/black_diamond/scripts/gold/05_build_client_performance.py` (lines 238-275)
- `data/black_diamond/scripts/gold/05b_build_account_performance.py` (lines 313-344)

**Files NOT modified (pure consumers of pre-computed parquets):**
- `09_generate_partner_analytics.py`
- `10_generate_advisor_rolling_flows.py`

### Exclusion Filter

Inserted in `load_flows_from_transactions()` after composite dedup, before flow
classification. The filter runs in two passes:

**Pass 1 -- Action-based (primary):**
```
Exclude where action IN ('JNL - LONG', 'JNL - SHORT')
```
Guards: `if 'action' in txns.columns` (safe on legacy partitions)

**Pass 2 -- Description-based (secondary):**
```
Exclude where description CONTAINS:
  'TRF BTWN SCH'               -- internal Schwab transfers
  'TO SEP ACCT MGR'            -- operational sweeps
  'TRANSFER FUNDS TO SCHWAB BANK'  -- FDIC bank sweeps
```
Guards: `if 'description' in txns.columns` (safe on legacy partitions)

Both passes use `regex=False` for performance (literal string matching).

### What Was Preserved

- $50M per-event FLOW_CAP (unchanged)
- AUA-based outflow cap (unchanged)
- 90-day velocity cap (unchanged)
- INFLOW_TYPES / OUTFLOW_TYPES sets (unchanged)
- All downstream scripts (unchanged -- they consume pre-computed parquets)

### Expected Impact

Based on the 4-month sample (Jul 2024, Dec 2024, Jan 2025, Apr 2025):

| Category | Events Excluded | In Removed | Out Removed | Net Impact |
|---|---|---|---|---|
| JNL - LONG / SHORT | 470 | $6.2M | $4.4M | -$1.8M |
| TRF BTWN SCH ACCTS | 1,003 | $15.0M | $12.0M | -$3.0M |
| TO SEP ACCT MGR | 10,571 | $0 | $2.2M | +$2.2M |
| SCHWAB BANK sweep | 6 | $0 | $1.2M | +$1.2M |
| **Total** | **12,050** | **$21.3M** | **$19.7M** | **-$1.5M** |

Net NNA impact is small (-$1.5M over 4 months) because most exclusions are roughly
symmetric (internal transfers have matching in/out legs). The real improvement is
**noise reduction**: 12,050 fewer phantom events means cleaner per-account, per-advisor,
and per-month NNA figures. Individual months that previously showed sign reversals vs
Schwab will improve.

### What This Does NOT Fix

The classification fixes improve accuracy on transactions we DO capture but cannot close
the ACAT orphan gap ($456M over 13 months) where BD never generated a transaction
record. That requires the allocation-diff pipeline described in smoke_test_orphan_theory.md.

## Rebuild Sequence

After code change, the rebuild order is:

1. Run `05_build_client_performance.py` (writes `gold/client_performance.parquet`)
2. Run `05b_build_account_performance.py` (writes `gold/account_performance.parquet`)
3. Run view builders that feed 09/10 (`nna_aua_by_advisor`, `nna_aua_by_geography`)
4. Run `09_generate_partner_analytics.py` (reads updated parquets)
5. Run `10_generate_advisor_rolling_flows.py` (reads updated parquets)

Scripts 05 and 05b are independent of each other. Steps 4-5 depend on 1-3.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Filter on `action` not `transaction_type` | Only field that distinguishes JNL (internal) from TOA/ACAT (external) |
| Use literal string match, not regex | Performance; patterns are fixed Schwab prefixes |
| Guard both filters with column-exists check | Legacy transaction partitions may lack action/description |
| Keep existing caps alongside new filter | Caps handle data quality (Albemarle 401k); filter handles classification |
| Do not modify scripts 09/10 | They consume pre-computed parquets; changes propagate automatically |

## Current State

Status: COMPLETE
Active branch: CLOUD
Code changes in: 05_build_client_performance.py, 05b_build_account_performance.py
Rebuild: Not yet run (requires CEO approval before reprocessing gold layer)
