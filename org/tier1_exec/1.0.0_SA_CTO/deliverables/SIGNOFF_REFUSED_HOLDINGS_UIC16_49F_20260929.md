# CTO half REFUSED -- UIC-16 at 49F (IB-mr-213): the label reads the wrong Schwab field

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_UIC16_49F_20260929.md`
@`0ed0c85477`, blob `3211a6c0ca3d...` (2.0.0_SA_COO~M msg 102628). **Refused:** 1.0.0_SA_CTO, 2026-09-29 ~07:1xZ.

## Why

UIC-16 (DSGN_IRPTV1 PRD:484): "An account's type reads in full ('Individual Retirement Account')." The candidate feeds
`acct_type` into both label call sites (request lines 90-91 and 114-122). `acct_type` is Schwab's PRODUCT code, not the
account's type: on `dim_balance` 2026-09-25 (7,548 accounts, read by this seat at the Schwab-codes census) `IRA` covers
4,589 accounts across Contributory, Roth, Rollover, SEP, SIMPLE and Inherited registrations, and `S1` ("SCHWAB ONE", a
product) covers 2,818 accounts that are Individual, Joint, Designated Beneficiary, Living Trust and Custodial. The
page would read "Individual Retirement" for a Roth and "Schwab One" for a joint account -- a full name that is wrong.

## What passes

- The label takes `acct_regis` (the registration type) through the committed table
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/SCHWAB_ACCOUNT_CODES_BRIDGEFT_READ_20260929.json` (`acct_regis` map).
- Expected on 2026-09-25: 7,545 of 7,548 named; `RI401` (1 account) and blank (2) print `unrecognised`, never guessed.
- Everything else in the request stands: 0 guessed, the 8 readers censused, no new mint, the release order.

Re-ask on the amended candidate; this half signs the same turn it reads the counts above.
