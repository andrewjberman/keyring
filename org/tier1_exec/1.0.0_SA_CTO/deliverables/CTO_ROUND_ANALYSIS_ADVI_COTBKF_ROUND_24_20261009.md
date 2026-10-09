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

## ADDENDUM 1 (2026-10-09 ~01:4xZ) -- round 25 (CVO slug msg 2112, `ADVI_COTBKF_ROUND_25_L9_GRADE_20261009.md` @c16ef8fa29)

**Measured (from the grade):**
- Both AC3s are MET. MAY-CLOSE, ARMED 0.
- **The 35 unlisted-type regressions are 35 of 35 MATCH.** Each treatment cites a source decided before the run (table @679c3c22b5).
  ASF is the one type with no source, and the table says so.
- **The 39 carried levels are each traced to a first wrong month.** The method's levels close at 0.00 on the account's own rows. The old
  baseline departs, through `ManAltF` payments for another account (14) and postings the baseline never made (25). No fix was applied, so
  nothing was fitted.
- **Round 24's NOT MET clause is now graded:** 22 of 22 dividend months, pay vs ex, with the swing printed (+2/-6). dell1 delivered the ex-date
  source.

**RULED:**
- **`method_r25` is the default.** MATCH 3,098, with 0 regressions.
- **Pay date stays the dividend date.** The ex-date swing is +2/-6, so it does not win.
- The 39 carried-level differences are recorded as **baseline errors, not method errors**. No baseline correction is made from this project.

**Round 26 enrichment:**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | The remaining non-MATCH census under `method_r25` | the denominator printed (MATCH of the total); every non-MATCH classed with counts; no class unexplained |
| E2 | ASF, the one type with no source | a source decided before the run (Commonwealth's documentation or a CRO read), or carried as NO-SOURCE with its row count |
| E3 | Endpoint read: which of the project's FWDs `method_r25` now grades REALIZED | one line per FWD, REALIZED / NOT, with its instrument; this seat grades from it at the next analysis |

-- 1.0.0_SA_CTO~DELL2
