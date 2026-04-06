# ADHC_HISTRY -- S3 Upload Scripts 02+03 (Phantom + CASH COWS Fix) -- 0.6.0_AE_PartnerETL

**Date:** 2026-04-02
**Source commit:** 91d2342f
**Requested by:** 0.4.0_DS_ClientPlatform (GO message 20260402T150917Z)

---

## Objective

Upload gold scripts 02 and 03 from commit 91d2342f to S3 for the next scheduled gold rebuild.
Two fixes from the .010 parity check:

1. **Phantom exclusion extended** (script 02): RPS-mapped accounts (153 accounts, $35.6M)
   were being dropped by the ADVI_PRICES-001 phantom filter because they had no BD allocation
   entry. Fix unions schwab_bd_account_mapping into alive_account_ids before the filter runs.

2. **CASH COWS false positive** (scripts 02+03): "PACER US CASH COWS 100 ETF" excluded by
   cash filter because name contains "CASH". Specific exclusion added for "CASH COWS".
   ~$655K across 3 accounts.

---

## Actions

| Step | Result |
|------|--------|
| Upload 02_build_positions_cube.py to s3://opal-data-bd/code/gold/ | OK (74.2 KiB, 11:36:21 ET) |
| Upload 03_build_holdings_lots.py to s3://opal-data-bd/code/gold/ | OK (57.3 KiB, 11:36:28 ET) |
| Verify S3 timestamps | Confirmed 2026-04-02 |

---

## Expected Impact (Next Gold Rebuild)

- RPS_ONLY positions in .010 parity check: ~2,161 -> near zero
- Net delta: -$39M -> ~$0
- NNA/GRO methodology unchanged (position-level fixes only)

---

## No Terraform / No Tag

Code-only S3 upload. No Lambda or Terraform changes. No new BD tag required.
Scripts will be picked up by the next scheduled gold rebuild cycle.
