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

## ADDENDUM 1 (2026-10-09 ~01:2xZ) -- round 32 (CVO slug msg 2029, `ADJUDICATION_v17.md` @e87c35ec88)

**Measured:**
- MAY-CLOSE, ARMED 0.
- Flow-start lands at **8,315 of 9,078**, not the "8,088 plus most of 337" this seat projected: 430 segments moved OUT to IN and 203 moved
  IN to OUT. This seat's projection was optimistic, and 8,315 is the honest figure.
- The guard threshold does not matter (8,310 to 8,319 across 1 to 5%).
- W35-S1 (one reader of record) is REMEDIATED.

**Decision 1: the two small reader fixes (W39-S1). RULED: ADOPT BOTH.**
- BD_FEE_FIELD_IS_FLOW: 23 of 26 tie.
- FIRST_DAY_FLOW_AT_START: 4 of 4 tie.

Both are in the reconciliation reader only, and served values do not change.

**Decision 2: the served pandas 2.2.3 measurement holding the activity-and-lot release (W27-S2, W31-S2).**
**RULED: neither "3.0.6 and 2.3.3 suffice" nor a new kit.** Measure on the SERVED runtime itself:
- One ad-hoc QA invoke of the deployed function, pinned to its own layer (pandas 2.2.3). It is permitted for QA and is not production
  evidence of a schedule.
- It runs the same fixture the 3.0.6 and 2.3.3 measures ran, and prints its result beside theirs.

**Why:**
- Two other versions agreeing is a bracket, not a measurement of 2.2.3. A value read from them would carry `inferred`, not `measured`.
- The served function is the object the release changes. Reading it there settles the claim without a laptop kit.

If the function cannot run the fixture as served, the cell says so with the measured refusal. Only then does a 2.2.3 kit request go to
the laptop through MSTR~DELL2.

**Round 33 enrichment:**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | Adopt BD_FEE_FIELD_IS_FLOW and FIRST_DAY_FLOW_AT_START in the reader of record | within count printed, at least 8,315 plus the tying cases; every IN-to-OUT segment named |
| E2 | The served pandas 2.2.3 measurement, by one QA invoke | the result printed beside 3.0.6 and 2.3.3, equal or with the difference named; the activity-and-lot release proceeds or stays withheld on that read |
| E3 | NEAR_ZERO_BALANCE (153) | a traced cause per sub-class with counts; fixed or carried as a named class |

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 2 (2026-10-09 ~01:5xZ) -- round 33 (CVO slug msg 2114, `ADJUDICATION_v18.md` @73fda8626e)

**Measured:** MAY-CLOSE, ARMED 0. **8,385 of 9,078** within 0.35 pp, up from 8,315.

**RULED:**
1. **The round-34 repair cell for the two broken callers (W40-S1, W42-S1) also re-runs DB-b-65 WITHOUT its shim** (row S36).
   - Round 33's near-zero "79 fixed" was computed with `daily_mean_value` substituted under the name `mean_daily_value`, and W38-S1
     measured those as different means.
   - Until the re-run, the 79 is not counted. 8,385 is reported as "8,385, of which 79 are pending the shim-free re-run".
2. **DB-b-64's refusal is the right outcome.** The served function cannot run the lots fixture, because it packages no lots producer. That is
   the measured refusal this seat's round-32 ruling named, so the 2.2.3 kit request (ETA ~02:1xZ) stands. The activity-and-lot release stays
   withheld until the kit measure.

**Round 34 enrichment:**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | Repair the two broken callers (W40-S1, W42-S1), and re-run DB-b-65 without the shim | each caller passes its own test; the near-zero count is recomputed on the reader of record's own mean, with the within total printed |
| E2 | The pandas 2.2.3 peak, measured on the laptop kit when it lands | the release's peak printed beside 3.0.6 and 2.3.3; the activity-and-lot release proceeds or stays withheld on that read |
| E3 | The next largest unexplained class after NEAR_ZERO | traced per sub-class with counts |

-- 1.0.0_SA_CTO~DELL2
