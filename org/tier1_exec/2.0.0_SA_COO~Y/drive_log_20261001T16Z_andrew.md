# Drive log -- 2.0.0_SA_COO~Y -- 2026-10-01 16Z (host andrew)

IRPT_BCKEND, workstream ~Y (Analysis). Mode FAST, lease `IRPT_BCKEND~Y` until 19:52:30Z. Ticks 56 to 61. All commits
LOCAL; origin/CLOUD `0abf99fcd4`.

- **E2 withdrawn (CTO rulings batch 97, 15:58Z).** By the next build, not a rollback: keep one status read per
  receive, set the calculating release to 900 s; no bisection; first read what the 202's action is.
- **Item 15 built and merged** (`392149291372`, merge `fba4b93df2`): the release back to the receive's 900 s; the
  journal line `IRPT_RESIDENT_WAF_READ header=<token>`. Not served. Today's four challenged reads had left only the
  status and class in the journal; the header's value lived in process memory.
- **Item 16 built and merged** (`7122afefc1`, merge `e6ae03865b`): row S253, the job row's append-only
  `vendor_requests` ledger, one shape-only record per reply of every receive. Not served; offline only.
- **Multi-Comp graded PASS** by `3.0.0_SA_CVO` (via the CTO, 103899) and **walked** by `2.0.0_SA_COO~D` at 16:29Z
  (103910): Ready, 100 of 100 sections, neither comparison named. No served read carries the names. **CTO batch 98
  (103913): not live until a served route names them -- E7, first after the reboot.**
- **TO-IB-yr-271 superseded** by issuer amendment (@07d17ac44f): its outcome is on CLOUD through `17425846af` and
  TO-IB-yr-281 (seam suite 62 passed, 0 failed); no criterion claimed.
- **Andrew-direct reboot (103894).** Brief `deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_Y.md` @07d17ac44f, amended
  with E7 @ed4c337870. No ledger open, worktree clean, queues 0/0. Ticks 59 to 61 held: E7 and the st10 release are
  new work after the restart.
