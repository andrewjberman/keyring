# ADVI_COTBKF decomposition -- ROUND 57 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11 ~04:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 4061 (and msgs 4037, 4039), after round 56 is terminal.
- IRPT_DASHBD.TO-DB-b-116 @2f0664fab0 (record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~91/ROW3_VS_COTTONWOOD.json`)
  already measured method row 3 against Cottonwood: TRUE for cash-posted income; the dim row 3 partition does not exist. This round
  does NOT repeat it.
- It left one thing unestablished: whether a bond's stored close carries accrued interest. That decides whether row 3's income basis
  is true for Cottonwood's BOND holdings. Until it is read, the CB-al-2 pair cannot state it.
- The same ruling puts the write of `dim_return_method` `method_version=3` for cottonwood on this project's mint cell, under the
  CB-al-2 pair, with thresholds stated as inferred from code defaults. That is the pair's content, not a cell of this round.

**Rule 24.** Domain: the one open question the CTO names -> one cell.

## Measured constraints (issuer)

1. **Read-only.** No code, test, config or served key is changed. Local files and code are read; no AWS call is needed.
2. **The verdict is a judgment.** The worker records evidence and its own reading; `3.0.0_SA_CVO` grades it at L9.
3. **988 bond account-days are already held out of the mint** (`HELD_SOURCE_UNDER_REVIEW`). The question is about the bond holdings
   that remain inside the 107,316 measured rows.
4. **Every non-test commonwealth script needs `COTBKF_SWEEPS_CONFIG` in its invocation line** (row ADVI_COTBKF-D2-S84).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-be-1` | for Cottonwood's bond holdings: does the stored close carry accrued interest (dirty) or not (clean), and does the return form then count coupon income once; one record with a verdict and counts | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~84` |

**Fan-out:** `1 of 1 chains, cap 8`. Not a direct-act cell: it carries a judgment criterion, so it takes L8 to L10.
