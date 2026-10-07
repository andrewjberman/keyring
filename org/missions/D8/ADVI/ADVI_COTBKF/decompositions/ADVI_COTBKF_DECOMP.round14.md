# ADVI_COTBKF decomposition -- ROUND 14 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~16:0xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-13 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_13_20261007.md` @d9877f9754 (msg 812).

**Rule 24.** Domain: E1, E2.
- **E1 (re-apply the crosswalk and account links):** DONE by the issuer's act under the pair (COO @cff9b1431a, CTO @d9877f9754); ledger
  `advi-cotbkf-r14-reapply-crosswalk-links-20261007` CLOSED 3/3 @ad6d5be150: 471 MATCHED, 212 LINKED with the two named swaps, diff vs the
  new tables 0 changed. No cell.
- **E2 (the 5 remaining fractional residuals explained):** one cell, `CB-n-1`.

## The cell

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-n-1` | each of the 5 fractional residuals left by the one-table rebuild explained from its transaction rows and classed SIGN_GAP / VENDOR_ROUNDING / SOURCE_GAP; any sign change goes through `commonwealth_signs.py` with the type census and the rebuild re-run, never a per-account patch | FWD-3 (C-DAILY step 1) | LOCAL | `0.9.0_WK_ADVI_COTBKF~30` |

**Write set:** `data/assets/scripts/analysis/commonwealth_residuals_explain.py` (new) + its test; `commonwealth_signs.py` and its test only if
a SIGN_GAP is found; the deliverables folder; the channel. **Fan-out:** `1 of 1 chains, cap 8`.
