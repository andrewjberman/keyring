# ADVI_COTBKF decomposition -- ROUND 30 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~08:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 5 @abbf204c7e (msg 2921).
- FWD-3 is graded PARTIAL: REALIZED except the `account_day_value` levels of acct#79d02c2c and acct#4a890dd1.
- Cell 1 is a read-only trace of D2-S45's ~2.45x factor.
- The repair or the blanking under a pair is cut on the trace's result.

**Rule 24.** Domain: the enrichment list's three items.
- Item 1 (the D2-S45 trace) -> cell `CB-ad-1`.
- Item 2 (the W53-S3 dividend trace "if not yet drained") is DRAINED: CB-ac-2 @c55a950d71, graded MET at L9 @6c125e3353. No cell.
- Item 3 (the W53-S4 re-count "after the price fill"): no fill has landed. The store index read at ~08:4xZ shows `rows 32`,
  `as_of 2026-06-23`, the same as CB-ac-3's read. A re-count now would only re-read the same store, which is coverage alone, so no
  cell. It is re-cut when the index grows.

## Measured constraints

1. The served tables @476f970245 are built at `method_r28`, `run_commit=feeee0be4dec`. The `--data-dir .scratch/advi_cotbkf/r28` is
   the build's input. 0 readers (CTO ADDENDUM 5).
2. CB-ac-2's trace: r28/r26 day-value ratio 2.4365-2.4744 on the two accounts. Candidate CUSIPs 808524102 and 808524839, with applied
   Oct-2024 splits.
3. The split machinery is `data/assets/scripts/silver/commonwealth_daily_valuation.py`: `split_plan` :318 and `apply_splits` :380.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ad-1` | read-only trace of the r28/r26 day-value factor on acct#79d02c2c and acct#4a890dd1 to the input that moved | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~57` |

**Fan-out:** `1 of 1 chains, cap 8`.
- `CB-ad-2` (the repair, or the ABSENT blanking under a pair) is cut on `CB-ad-1`'s class. It is a dependent cell, not cut now.
