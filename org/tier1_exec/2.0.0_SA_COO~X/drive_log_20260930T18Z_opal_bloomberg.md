# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 18Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 18:0xZ | L8 | 25 | aa-2 leg d: 21 of 21 written, 0 errors; the S3 structure is exactly one new object per name |
| 18:24Z | L8 | 25 | aa-2 leg d: `inputs_equal_now` 21/21 |
| 18:2xZ | L8 | 25 | aa-2 ledger CLOSED (5 legs), committed `b865b41d57`, as below |
| 18:50Z | L8 | 25 | aa-4's act-start gate NOT empty (a peer's `drafting_build.py`, outside the 63-file closure): STOPPED per the CTO's condition 1, confirm asked (msg 27329) |
| 18:58Z | L8 | 25 | CTO: YES on the closure reading (msg 27330, AMENDMENT 1 to its half) |

**The aa-2 close commit:** the first commit loop hit the commit gate (ruff F401, an unused import in `aa4_verify.py`) and retried
blindly for 10 minutes. The loop was stopped and the import fixed. The retry is now `commit_retry.sh`, which stops on BLOCKED.

**The aa-4 ledger:** it was opened in the same call as the gate read (an issuer defect), and committed `35e013bab3` with no leg acted.

## Compiler Tools

- `d25.py structure|inputs`, a static import-closure walk, and `deploy_ledger.py`.
- Gaps:
  - the commit loop did not stop on a gate BLOCK;
  - the ledger refuses a HOLD while apply legs are open.
