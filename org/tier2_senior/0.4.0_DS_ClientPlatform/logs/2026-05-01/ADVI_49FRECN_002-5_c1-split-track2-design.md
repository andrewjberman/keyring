# Session Log — ADVI_49FRECN.002.5 — C1 Split + Track 2 Design Recommendation

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-01
**Task Order:** ADVI_49FRECN.002.5
**Status:** COMPLETE

---

## Summary

Executed Phase 1.5 sub-investigation for the 49Financial reconciliation. Precisely classified all C1 accounts (updated count: 64 accounts / $64.8M, vs Phase 0 estimate of 60 / $55.5M due to rounding in original pass). Identified three distinct root-cause mechanisms, traced the divergence through the full silver-to-gold stack for a 10-account sample, surveyed the "in book" definition, and produced a Track 2 design recommendation. Deliverable appended to `docs/architecture/49F_RECONCILIATION_2026-05-01.md` (routed to CTO for commit per owned-paths lane).

---

## Findings Summary

### C1a/C1b Classification

- **C1a (genuinely closed): 0 accounts.** All 64 C1 accounts have account_is_open=True, closed_date=NULL, non-zero AUA.
- **C1b total: 64 accounts, $64,761,933.**

| Sub-bucket | N | AUA | Mechanism |
|-----------|---|-----|-----------|
| C1b-RECONCILE_DROP | 40 | $38,546,209 | B_00 bd_stale drops positions present in cube |
| C1b-AQR | 6 | $11,823,385 | AQR alternative fund, no TXN_DAILY, A_03 gap |
| C1b-TXN_LAG | 10 | $6,826,769 | In unrealized + TXN exists, cube predates TXN |
| C1b-NEW | 4 | $4,081,523 | No BD linkage; ~400 days old (anomalous) |
| C1b-SMA-UNREALIZED | 2 | $3,224,446 | Large SMA (307-398 securities), UNREALIZED only |
| C1b-CASH | 2 | $259,601 | Cash-only in unrealized |

### Root Cause Mechanisms

1. **B_00 bd_stale (59.5%):** B_00 `reconcile_date()` labels all positions `bd_stale` for recently-opened accounts where Schwab RPS hasn't yet confirmed positions. BFIX2 misses them (they have rows in reconcile output, just units=0). The `holdings[units > 0]` filter drops them silently. All 40 accounts have real position data in positions_cube.

2. **A_03 ingestion gap (34.2%):** A_03 reads only TXN_DAILY. AQR TA DELPHI PLUS FUND LLC and large SMA portfolios are delivered by BD via UNREALIZED_DAILY only — they generate no TXN_DAILY records. BD's allocation feed prices them correctly (silver/allocations `account_market_value` includes them).

3. **Genuinely new (6.3%):** 4 accounts with no custodian linkage; ~400 days old. Likely onboarded to 49F but not yet linked to BD custodian account. Resolve organically or via Option A fallback.

### "In Book" Definition

49F's 6,611 count = silver/allocations snapshot exactly. 49F counts every account where BD has an allocation record — regardless of position activity, account type, or gold eligibility. NOT transaction-based.

### Track 2 Design Recommendation

**Option D + Option B hybrid:**
- **Option D (primary, $38.5M):** Extend B_00 BFIX2 — for accounts where all non-cash positions are bd_stale AND account_create_date within last N days (recommend N=60), reclassify from bd_stale to bd. No data synthesis — uses real positions already in positions_cube.
- **Option B (secondary, $22.1M):** Add silver/unrealized ingestion pass in A_03 for accounts in silver/allocations but absent from TXN_DAILY. Covers AQR, SMA-UNREALIZED, TXN_LAG sub-buckets.
- Options A and C rejected as primary fixes: A synthesizes data for accounts that have real positions; C does not address the B_00 layer where the drop actually occurs.

**Combined projected recovery: 62 of 64 accounts, $60.4M (93.3% of C1 AUA).**

### Custodian Source-of-Truth Trace (10 accounts)

BD bronze carries a current balance for ALL 10 sampled accounts (confirmed via silver/unrealized). Divergence is entirely Opal-internal:
- RECONCILE_DROP: divergence at B_00 reconcile_date() — positions present in cube, zeroed by bd_stale label
- AQR: divergence at A_03 — positions in silver/unrealized, never entered TXN_DAILY path

### Open Questions for Andrew (4 items)

1. Business rule on bd_stale: trust BD TXN-derived positions before Schwab RPS confirms (for newly-opened accounts)?
2. Is AQR TA DELPHI PLUS FUND LLC expected in 49F display? Confirms Option B scope.
3. Are the 4 C1b-NEW accounts 49F-side-only (never BD-linked) or mismatched BD account_ids?
4. Anomalous 869-day-old TXN_LAG IRAs: transfer-in or rebooking event?

---

## Compiler Tools

| Tool | Target | Result |
|------|--------|--------|
| comp-pipescript io | A_03.positions_cube | Read to understand TXN_DAILY ingestion path |
| comp-pipescript io | B_00.canonical_holdings | Read to confirm reconcile_date() bd_stale + BFIX2 gap |

---

## Files Modified

| File | Change |
|------|--------|
| docs/architecture/49F_RECONCILIATION_2026-05-01.md | Appended Phase 1.5 section (AC#1-5); routed to CTO for commit |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_49FRECN.002.5 | Status: pending -> complete |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-01/ADVI_49FRECN_002-5_c1-split-track2-design.md | This log |

---

## Next Steps

[CTO] Receive RAVC4, commit Phase 1.5 section to docs/architecture/49F_RECONCILIATION_2026-05-01.md (owned-path lane). Author Track 2 fix TO (Option D: B_00 BFIX2 extension + Option B: A_03 unrealized ingestion) after Andrew answers the 4 open questions.

[Andrew] Answers to Open Questions #1-4 before Track 2 fix TO can be scoped precisely.
