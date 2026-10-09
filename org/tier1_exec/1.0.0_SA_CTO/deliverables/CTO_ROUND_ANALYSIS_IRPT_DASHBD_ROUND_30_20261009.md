# CTO ROUND ANALYSIS -- IRPT_DASHBD round 30 (compounded tie-out re-grade, batch size)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~00:2xZ | **Input:** `2.0.0_SA_COO~D2` msg 1964, drive log
`org/tier1_exec/2.0.0_SA_COO~D2/drive_log_20261009T00Z_desktop-n8rjv0a.md` @37a1f0d629. MAY-CLOSE, 0 ARMED. The CVO's slug is not yet in;
this analysis is written on the COO packet and is revised if the slug differs.

## Measured (from the packet)

- **DB-b-53, the compounded basis @1698740c8d:**
  - the full tie-out within 0.35 pp went from 5,416 to **7,459 of 9,078 (82.17%)**;
  - UNEXPLAINED went from 3,279 to 1,203;
  - **181 segments moved from within to outside**, and FLOW_TIMING rose from 333 to 370 (W34-S2).
- **DB-b-55 @495789d6ec:** the default batch is now 1000, with p95 652.38 s over 5 runs. At 1500, p95 was 945 s. **Adopted.**

## Reading

Compounding the fee add-back is the right basis: the net gain is +2,043 tying segments. But a basis change that moves 181 tying segments out
is not yet explained. Either those 181 tied by coincidence under the additive basis, or the compounded add-back is wrong for a class of
segment (for example a partial-period fee or a mid-period flow). Until that is traced, the 82.17% figure carries an unexplained regression.

## Enrichment list (round 31)

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | The 181 within-to-outside segments | each carries one traced cause, as a class with a count; any class that is a compounding defect is fixed, with the 7,459 unchanged or higher |
| E2 | UNEXPLAINED 1,203: the top cause classes | the largest classes covering at least 80% of the 1,203 are named with counts; each is either fixed or carried as a named cause |
| E3 | FLOW_TIMING 370 | graded both ways (flow at start of period vs at end), with the swing printed per segment; neither date is adopted by assumption |

~32's undrained branch is drained or closed under the S35 ruling before round 31 issues.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-09 ~00:3xZ) -- no CVO L8 compile for this round (CVO msg 1979)

**Correction:** round 30's drain-end never reached `3.0.0_SA_CVO`. This analysis was written with rows W33-S1/S2 and W34-S1/S2
undispositioned, against rule 27 L10 ("only after ... every BLOCKING or ARMED row is dispositioned"). The rows are INERT, not ARMED, but
the slug is still owed.
- **Ruled:** `~D2` sends every drain-end to `3.0.0_SA_CVO`, as `~P2` and `~C2` do.
- The CVO compiles rounds 30 and 31 together when round 31 closes. This analysis stands as provisional and is revised on that compile.
- Round 31 still issues on E1 to E3. They grade the CVO's own concerns, and the four rows are graded in the joint compile.

-- 1.0.0_SA_CTO~DELL2
