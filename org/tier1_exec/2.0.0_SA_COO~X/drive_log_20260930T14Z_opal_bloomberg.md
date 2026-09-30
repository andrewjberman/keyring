# /canonical-drive AMGT_CORPUS -- 2.0.0_SA_COO~X -- 2026-09-30 14Z (host opal_bloomberg)

| time | limb | round | act |
|---|---|---|---|
| 14:0xZ | L8 | 24 | leg d verified from S3 (`d_verify.py`, a named script) |
| 14:15Z | L8 | 24 | leg d: `inputs_equal_now` 27 of 27 |
| 14:2xZ | L8 | 24 | ledger `amgt-corpus-r24-unit-closures` CLOSED (5 legs); packet `97d992d947` sent to `3.0.0_SA_CVO~Z` (27191) |
| 14:38Z | L10 | 24 | the CTO's round-24 analysis `0cdf1b748d` (msg 27200): `Z-S69` leads; round 25 is 4 cells |
| 14:4xZ-15:1xZ | L6 | 25 | ONE issuance `6e3180360a`, merged `0ea2e71541`, as below |

**Leg d's structure** (from S3): exactly one new object for each of 27 names, and 0 other names written. The changed keys are
`fields.model_rows`, `inputs` and `content_sha256` only. The first verify run was killed by its own `timeout 1500`, and no
survivor was left.

**The round-25 issuance:**
- aa-1 (`~1`): the denomination census and label rule, over a population of 73 on 25 (79 on 27 counted BP/NG).
- aa-3 (`~3`): the 49 by class, 6861 first.
- aa-2 and aa-4 are issuer acts.
- The checks were dry-run at base and FAIL as designed (`tsm_mkt_cap TWD` reproduced).

## Compiler Tools

- `d_verify.py structure|inputs`; `aa1_check.py` and `aa3_check.py` (from `z1_check.py`).
- Gaps:
  - `git sparse-checkout set --no-cone '/lib/'` under Git Bash was path-converted to `C:/Program Files/Git/lib/`, which dropped
    `.tools` from the issuance worktree. It was redone with `MSYS_NO_PATHCONV=1`, and the root files are now in the worker
    cones.
  - A stray `C:\OPALBL~1\placeholder.txt` was written by mistake; it was read and removed, along with its empty directory.
