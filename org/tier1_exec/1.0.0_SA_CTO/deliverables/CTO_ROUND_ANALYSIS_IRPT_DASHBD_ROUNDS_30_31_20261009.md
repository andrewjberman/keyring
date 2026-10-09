# CTO ROUND ANALYSIS -- IRPT_DASHBD rounds 30-31 (on the CVO's joint compile)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~00:5xZ | **Input:** the CVO's L10 slug msg 2006,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v16.md` @c33fea078b. Both rounds MAY-CLOSE, ARMED 0.
**This supersedes** the provisional `CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_30_20261009.md` (@4cfe197b0c, ADDENDUM 1 @b88cc62432).

## Measured (from the compile and the drains)

- **Within 0.35 pp:**
  - round 18 (additive add-back): 5,416;
  - DB-b-53 (compounded): 7,459;
  - **DB-b-57 and DB-b-58, independently (daily-mean fee base): 8,088 of 9,078.**
  - 762 segments moved OUT to IN, and 133 moved IN to OUT.
- **The 990 still outside are all named by class:**
  - LARGE_FLOW_DAY 170;
  - NEAR_ZERO_BALANCE 153;
  - FLOW_TIMING_AFTER_FEE_BASE 116;
  - smaller classes.
- **FLOW_TIMING (370):** 337 tie at flow-start and 0 at flow-end. Flow-end is the reader's current convention, so 0 there is by construction.
  Flow-start is closer on 356.

## Decision 1: ONE daily-mean fee-base module as the reader of record (W35-S1)

**RULING: `tieout_compound_v2.py`** (worker ~35, DB-b-57, drain @605c4cd4ac) is the reader of record.
- **Why:** it is the tie-out reader's own line (`tieout_compound.py`, then v2). ~36's `unexplained_classes.py` is a classifier that reached
  the same base independently.
- The two agree (8,088 each). That agreement is the evidence, and two homes for one rule is the defect.
- Round 32 moves v2 out of the worker deliverables folder into the project's code path. The classifier then imports its fee base from v2
  instead of computing it again.

## Decision 2: the FLOW_TIMING convention

**RULING: the tie-out reader adopts flow-START for a flow day's fee base.**
- **Why:** 337 of 370 tie at flow-start against 0 at flow-end, and start is closer on 356. The measured reference behaves as flow-start.
- **This is the reconciliation reader's convention only.** The served dashboard values do not change under this ruling.
- If a later cell finds that the served producer itself must change, that change moves served output and needs a never-widen pair
  (CLAUDE.md NEVER-1). This ruling does not authorize it.

## Enrichment list (round 32)

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | `tieout_compound_v2.py` becomes the reader of record in the project code path; the classifier imports its fee base | one module computes the daily-mean fee base (writer count printed = 1); the re-grade still reads 8,088 |
| E2 | Flow-start adopted in the reader; full re-grade | within count printed, expected at least 8,088 plus most of the 337; every segment that moves IN to OUT is named |
| E3 | LARGE_FLOW_DAY (170) | a traced cause per sub-class with counts; fixed or carried as a named class |

Drain-ends go to `3.0.0_SA_CVO` (ruling of 00:3xZ).

-- 1.0.0_SA_CTO~DELL2
