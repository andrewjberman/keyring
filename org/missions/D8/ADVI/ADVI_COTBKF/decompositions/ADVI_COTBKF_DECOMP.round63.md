# ADVI_COTBKF decomposition -- ROUND 63 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T08:49Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** the laptop `1.0.0_SA_CTO` ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB_282F_INLINE_POLICY_NAME_AND_GATE_REFUSED_LEDGER_20261011.md` @e1267f773c (answering cross-box call XB-20261011T082334Z-282f; relayed in
msgs 4505 and 4507), and `1.0.0_SA_CTO~DELL2` msgs 4474 and 4516.
- Round 62's targeted apply (CB-bj-1) stopped before any write: the naming plan limb refused the inline policy's hand-typed name
  `restricted-prefix-get-put-list`. Nothing was created (issuer `get-role` at 08:20Z: NoSuchEntity).
- The laptop CTO fixed the canon (`lib/opal_naming.py`, in `box/dell2` HEAD by the issuer's `merge-base` read) and ruled the name:
  the inline policy is named `RestrictedPrefixGetPutList`. The gate's own suggestion, which carried another firm's token, is NOT adopted.
- This moves the `.tf` blob both halves of the FWD-7 pair pinned, so both halves are re-signed after this cell drains, and CB-bj-1 is
  re-released by amendment on the new pin.

**Rule 24.** Domain: the one hand-typed name -> one cell.

## Measured constraints (issuer)

1. **One line.** `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf` line 264 is the only place the old name appears in that file (issuer read).
2. **The carriers are not touched.** 14 of 15 generated carriers are stale at HEAD (row D2-S103); the canon's owner regenerates them.
   Nobody on dell2 runs `generate`, in whole or in part (CTO msg 4516).
3. **No terraform command and no AWS call in this cell.** The plan and the apply are CB-bj-1's.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bk-1` | the break-glass role's inline policy is named `RestrictedPrefixGetPutList` in the `.tf`; the old name appears nowhere in that file | FWD-7 | WORLD | none | `0.9.0_WK_ADVI_COTBKF~89` |

**Risk class:** WORLD is the gate's floor for an order whose `<paths>` name an infrastructure path; the cell itself runs no terraform
and makes no AWS call.

**Fan-out:** `1 of 1 chains, cap 8`.
