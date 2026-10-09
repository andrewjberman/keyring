# CTO ROUND ANALYSIS -- ADVI_COTBKF round 24 (rebuild on Commonwealth's stated method)

**Seat:** `1.0.0_SA_CTO~DELL2` | **Date:** 2026-10-09 ~00:1xZ | **Input:** the CVO's L10 slug msg 1956, grade
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_24_L9_GRADE_20261008.md` @f7845571f2.
The COO packet is `deliverables/0.9.0_WK_ADVI_COTBKF~46/sweep_regrade.md` (@b9f31e686c).

## Measured (from the grade)

- MATCH rose from 2,058 to 3,059. Round 22's 25 months all match. ARMED 0. MAY-CLOSE.
- All 98 regressions are named, each with one traced cause:
  - unlisted types: 35;
  - pay-dated dividends: 22;
  - carried levels: 39;
  - `man`: 2.

  This meets this seat's msg-1939 condition, so **the method is now the default.**
- **CB24x1-AC4 is NOT MET on one clause:** "every cross-month dividend month graded both ways". No dividend row carries an ex-date
  (row D2-W46-S2). The pay/ex option is built and tested.

## The decision asked: route ex-dates through the dell1 data queue, or amend the clause by name?

**RULING: route; do NOT amend.**
- The clause measures a real claim. Amending it by name would turn data the fabric lacks into a pass.
- The ex-date feed is requested through dell1's single data-queue project as a **pre-arranged input**:
  - Owner: `2.0.0_SA_COO~C2`, which files the need with its ranked list.
  - Un-park condition: ex-dates land for the 22 pay-dated months.
- **The NO-STOP RULE applies:** the clause stays NOT MET and parked as ONE hop. Round 25 does not wait on it.

## Enrichment list (round 25)

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | Unlisted types, `ftax` first (35 regressions) | each of the 35 is MATCH or carries a traced cause the CRO's table names; no new regression |
| E2 | Carried levels (39) | each traced to its first wrong month; any fix leaves the 3,059 matches unchanged |
| E3 | The ex-date input, filed with dell1's data queue | the request is filed, with its owner and the 22 months named; when ex-dates land, the 22 are graded both ways with the swing printed (AC4's clause) |

-- 1.0.0_SA_CTO~DELL2
