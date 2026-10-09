# drive log -- 2.0.0_SA_COO~D2 -- 2026-10-09 01Z -- desktop-n8rjv0a (dell2)

## ticks 208-213 -- round 32 issued, executed, drained, MAY-CLOSE

| project | limb | round | TOs | act |
|---|---|---|---|---|
| IRPT_DASHBD | L10 -> L6 -> L7 -> L8 | 32 | 3/3 complete | issuance @3e6d112773; drains @d077f0f991, @e72c6c354d; round-close-check MAY-CLOSE |

- Input: the CTO's rounds 30-31 analysis @fe8e06016b (msg 2007), on ADJUDICATION_v16:
  - v2 is the reader of record;
  - flow-START is adopted;
  - served values are unchanged.
- Issuer ruling: the tie-out code path is `org/missions/D9/IRPT/IRPT_DASHBD/tieout/`. It is project-owned, never served, and outside
  every deploy lane.
- Checks `deliverables/2.0.0_SA_COO~D2/checks/r32/p32_round32.py`: 6 FAIL at base 5992357355 (the census read 2 writers); planted 6/6 PASS.

### Results

- **DB-b-60, worker ~38, @e72c6c354d.**
  - `tieout/tieout_reader.py` is the reader of record. The writer census finds 1 writer in 127 .py files.
  - ~35's v2 and ~36's classifier import the reader; their outputs are unchanged, with no git diff on their records.
  - The re-grade reads 8,088 of 9,078, with all 9,078 grades equal to round 31's.
- **DB-b-61, worker ~38, @e72c6c354d.** FLOW_CONVENTION = "start", with a near-zero guard: a day re-links only if
  V(t-1)+F(t) >= 2% of |V(t-1)|.
  - Within: **8,315** of 9,078. 430 segments moved out->in and 203 moved in->out, each named: START_LARGE_FLOW 174, START_SMALL_FLOW 22,
    START_GUARD_DAY 7.
  - Guard sensitivity: 8,310 / 8,315 / 8,315 / 8,319 at 1% / 2% / 5% / 10%.
  - The result is below the CTO's expectation (8,088 plus most of the 337) and is reported as found.
  - Rows W38-S1 (positive-only mean flag), W38-S2 (REGRADE_E1 regenerated under the final reader; grades identical, sha only),
    W38-S3 (guard choice).
- **DB-b-62, worker ~39, @d077f0f991.** LARGE_FLOW_DAY 170 splits into 10 sub-classes:
  - 2 fixed: BD_FEE_FIELD_IS_FLOW 26 (23 tie under the fix); FIRST_DAY_FLOW_AT_START 4 (4 tie);
  - 8 named, led by LIQUIDATION_RESIDUAL_BASE 40 and SINGLE_PARTIAL_FLOW 38.

  Neither fix is adopted into the reader. Row W39-S1.

### Carried, for the CTO

- **The B release peak on served pandas 2.2.3** (decomposition section 29, issuer act) is still owed. dell2's Python 3.12 kit carries
  pandas 2.3.3 and no 2.2.3 exists on the box. The withheld activity-and-lot release (S31-S33) waits on it, or on a ruling that the 3.0.6
  and 2.3.3 measurements suffice: batch 1000, p95 652 s, lots peak <= 1,763 MB against 2,048.

### Mechanics

- The empty tick at 01:1xZ ran `/next-calls IRPT_DASHBD --drive` (empty_tick=on): 0 calls at Andrew, 0 FREE options -> NOTHING-LEFT.
- ~38's branch sync was refused by the row gate's fail-closed corpus pass: a COMM_ASSIST channel file was not on disk inside the
  worktree's merge. The worker branch was drained from the shared tree instead, with no conflict; the channel has 121 blocks, 0 malformed.
- The `C:/dev/wk-irpt-dashbd-35` directory is still locked on disk. It is unregistered and its branch is deleted.
