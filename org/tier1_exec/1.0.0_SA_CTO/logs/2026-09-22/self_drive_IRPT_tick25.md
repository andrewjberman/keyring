# /self-drive IRPT_FNTEND IRPT_BCKEND -- ticks 23-25 (~03:0xZ-04:1xZ 2026-09-22)

| | |
|---|---|
| Arming record | carrier `c9ccd9f4e3` |
| Cron | `46e545b7` |
| State | **ARMED** |
| Projects | 2 of 2 `active` / EXECUTING |
| Sequence | no flags |
| COO lanes | 2 of 3 |
| Inbox | 0 unread; 99388 read and acked |

## Driver acts

**IB-rtk-1 (the capture tool's third publish): CTO half SIGNED @`993ff1fad3`** (msg 99389/99390).

- **What was signed:** the CORRECTED packet, blob `5d30a76a`. `2.0.0_SA_COO~B` had caught a wrong sha256 in it and fixed it @`2505e2c00a`.
  - cjs: blob `ded60502`, sha256 `f03666ef`.
  - Live S3 still serves `defcb585`, which is the rollback target.
- **Diagnostics run by this seat.** Both are CVO~B's diagnostics, unmodified, run against the fixed bytes. The prior bytes `c5a18898` were run the same way as a negative control.
  - **R10 lifecycle diagnostic:** exactly two cases flip from writes=1 to writes=0 — the interactive foreign hop, and the foreign hop followed by a clean retry. The positive control still writes.
  - **R9 diagnostic:** identical results on both byte sets.
  - Stated as: "passes the 6+6 cases at those pins."
- **Still HELD:** the capture ask to Andrew, pending CVO~B's R101-successor grade and an S3 readback of `f03666ef`.

## State

- **IRPT_BCKEND round 11:** rtk-1 is drained. The publish goes next, then CVO~B's grade.
- **IRPT_FNTEND round 11:** 6 of 9 drained so far — FE-s-65, 66, 68, 69, 71, 72 and 73. COO~F is amending FE-s-67 (a second correction) and FE-s-70 (a vacuous control fixed at `ea18c43025`).

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

`node` (CVO diagnostics R9/R10 plus a negative-control scratch tree), `git show | sha256sum`, `.tools/aws s3 cp`, `sequence-check.py`
