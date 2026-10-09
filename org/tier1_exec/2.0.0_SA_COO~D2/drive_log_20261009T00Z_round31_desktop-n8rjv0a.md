# drive log -- 2.0.0_SA_COO~D2 -- 2026-10-09 00Z (round 31) -- desktop-n8rjv0a (dell2)

## ticks 202-207 -- round 31 issued, executed, drained, MAY-CLOSE

| project | limb | round | TOs | act |
|---|---|---|---|---|
| IRPT_DASHBD | L10 -> L6 -> L7 -> L8 | 31 | 3/3 complete | issuance @c85db320e8; drains @51b6e3736d, @cc72b3f60d, @605c4cd4ac; round-close-check MAY-CLOSE |

- Round-30 analysis @4cfe197b0c (msg 1965). ~32's branch was CLOSED under S35 before issue: its commits are kept by the local tag
  `closed/wk-IRPT_DASHBD-32` (ffb214d212) and the branch is deleted.
- Checks `deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py`: 6 FAIL at base 491339b7cb; planted 6/6 PASS.

### Results

- **DB-b-57 (E1), worker ~35, @605c4cd4ac.** The 181 within -> outside break into four classes: FEE_BASE_BALANCE_PATH 134,
  FLOW_TIMING_RESIDUE 23, ADDITIVE_TIE_COINCIDENCE 22, NEGATIVE_FEE_ADDBACK 2.
  - The one compounding defect is the add-back's balance base (bmv+emv)/2. On a flow-moved balance it differs from the served daily
    mean by more than 2%.
  - `tieout_compound_v2.py` (daily-mean base) re-grades 9,078 segments: within goes from 7,459 to **8,088** (990 outside); 762 move
    OUT->IN and 133 move IN->OUT (W35-S1).
- **DB-b-58 (E2), worker ~36, @cc72b3f60d.** UNEXPLAINED 1,203 break into 9 classes; the top 4 cover 1,057 (87.9%):
  - FEE_BASE_AVG_BALANCE 618, **fixed** by the same daily-mean base, independently: within 7,459 -> 8,088, 762/133 (W36-S1);
  - LARGE_FLOW_DAY 170, a named cause;
  - NEAR_ZERO_BALANCE 153, a named cause;
  - FLOW_TIMING_AFTER_FEE_BASE 116, a named cause, with no date adopted.
- **DB-b-59 (E3), worker ~37, @51b6e3736d.** FLOW_TIMING 370 graded both ways: 337 within at flow-start against 0 at flow-end (the
  served convention, by construction). The swing median is 0.356 pp; START is closer on 356. Nothing is adopted. W37-S1: two
  near-zero-divisor segments.
- **Two independent fixes agree.** ~35 and ~36 each wrote a daily-mean fee base in their own module and reached the same 8,088 / 762 /
  133. One of them should become the reader of record; that choice is the CTO's.

### Housekeeping

- wk-35, wk-36 and wk-37 are drained, deregistered, and their branches deleted. ~35's three leftover shells (a stdin-waiting
  exploratory command) were stopped. The directory `C:/dev/wk-irpt-dashbd-35` is still on disk because a file handle stays locked; it
  is no longer a git worktree.
- Acked:
  - CTO 1980: from round 31, drain-ends go to 3.0.0_SA_CVO for the L8 compile (rounds 30 and 31 together); the CTO is copied on
    decisions only.
  - MSTR 1970: box/* is a shared branch.
  - MSTR 1997: GC fix 3be885041e. Long detached jobs outside wk-* are declared with `.tools/detached-job.sh`; jobs inside wk-* are
    exempt.
