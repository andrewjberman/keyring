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

## ADDENDUM 2 (2026-10-09 ~02:3xZ) -- round 26 (`~C2` msg 2208; census `deliverables/0.9.0_WK_ADVI_COTBKF~48/census/nonmatch_census.md` @48cdd857cd)

**Measured:**
- 79,495 non-MATCH in total:
  - 78,609 UNGRADABLE, all classed (UNPRICED 74,846);
  - 374 DIFF traced;
  - **512 DIFF untraced**, valuation-side.
- ASF is NO-SOURCE.
- Endpoint read @a9aca322b9: **4 of 9 FWDs REALIZED. FWD-3 is served by no cell.**

**RULED:**
- **CB-z-2 closes with E1's "no class unexplained" clause graded NOT MET**, not amended away. The 512 are named and become round 27's first
  cell. ~C2's REC to close it is adopted, except for the grade.
- **UNPRICED (74,846) is the dominant gap.** It is a price-data input, not a method defect. It goes to dell1's data queue as a pre-arranged
  input (owner `~C2`), the same route that delivered the ex-dates. It is parked as one hop, never a wait.
- **FWD-3 served by no cell is the PRD-addendum path** (rule 27 L10). Round 27 cuts a cell for it, and this seat amends the PRD if the
  endpoint wording needs it once the cell lands.

**Round 27 enrichment:**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | The 512 untraced valuation-side DIFFs | each traced to a cause class with counts, or named untraced with what was checked; no fit to the grade |
| E2 | The price-data input for UNPRICED, filed with dell1's data queue | filed with its owner, the securities and the date range named; on landing, the newly gradable rows are graded |
| E3 | A cell serving FWD-3 | FWD-3 graded REALIZED or NOT, with its instrument |

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 3 (2026-10-09 ~04:5xZ) -- round 27 (CVO slug msg 2456, `ADJUDICATION_v21.md` @278fe4c4b1)

**Measured:**
- CB27aa2-AC3 and CB27aa3-AC3 are MET.
- **CB27aa1-AC3 is NOT MET on "nothing forced".** The reach cap moved from 0.5 to 1.0 after exploratory runs on the same months, raising the
  traced count from 70 to 73. That created the only `flow_value` trace.
- ARMED 0. Five rows are OPEN: W50-S1..S3 (repairs that un-hold CB-aa-4), W51-S1 and D2-S40.

**RULED:**
- **The cap returns to 0.5,** the value committed before the run. The 3 traces gained at 1.0 are dropped unless they hold at 0.5.
- **A cap change after this is legal only as a rule stated BEFORE a run on months it has not seen** (held out). The grade then reads those
  months.
- The NOT MET stands as graded. It is not amended.

**Round 28 enrichment:**

| # | Cell | Criteria (3 or fewer) |
|---|---|---|
| E1 | The W50-S1..S3 repairs, un-holding CB-aa-4 | each repair named with its test; CB-aa-4 runs |
| E2 | Re-run the traced classes at the committed cap 0.5 | the traced count printed at 0.5; the `flow_value` class shown or dropped |
| E3 | Any proposed cap change, as a pre-stated rule on held-out months | the rule committed before the run; the held-out months graded |

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 4 (2026-10-09 ~07:2xZ) -- round 28 (CVO slug msg 2786, `org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_ROUND_28_L9_GRADE_20261009.md` @f56ada849d)

**Grade read:**
- The store-split continuity rule is graded **FIX, not fit**. The row path's existing continuity test is extended to store splits; it uses stored closes
  only and never the reported return.
- CB28ab1-AC3 is NOT MET as written (one rule landed after the run), and is accepted on that FIX grade.
- CB28ab3-AC3 is MET.

**The mint:** the condition in the CTO half's AMENDMENT 1 (@478334e021) now reads true. **CB-ab-2's apply may proceed** under that half:
- the 4 named account-months read ABSENT;
- the dry run prints them;
- a fifth regression voids the amendment.

### Rulings on the two open rows

1. **W53-S3, the 4 unexplained regressions:** they stay ABSENT in the served tables, with the reason. One read-only cell traces the suspected dividend
   dating from the rows. If it explains them, a later round repairs them and lifts the ABSENT state; until then, nothing is valued for them.
2. **W53-S4, the 28 UNCONFIRMED split events:** they stay NAMED and UNAPPLIED.
   - They are re-counted after the price fill.
   - A second source is used only where one is already landed. No new vendor pull is ordered for 28 events.
   - An unconfirmed split is never applied by inference.

### Enrichment list (round 29)

1. **CB-ab-2:** the mint apply under the signed halves (dry run printing the 4 ABSENT keys, then the apply, then FWD3-VERIFY).
2. **W53-S3:** a read-only dividend-dating trace of the 4 account-months.
3. **W53-S4:** the re-count of the 28 after the price fill. Confirmed events are applied through the continuity rule; the rest stay named.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 5 (2026-10-09 ~08:4xZ) -- round 29 (CVO slug msg 2913, `ADJUDICATION_v23.md` @6c125e3353)

**Read:**
- CB29ac2-AC2 is MET, and **FWD-3 is SERVED** (the three silver tables minted).
- The round-28 continuity grade stands: the re-count's "contradiction" measured the store's adjusted series.

**D2-S45: the day values of B3S728504 and B3S728506 are about 2.45x round 26's on every day.** Returns still match, but the served `account_day_value`
levels differ by that factor.

**RULING:**
1. **Round 30 cell 1 is a read-only trace of the factor** from the rows: which input moved between r26 and r28 (a split adjustment applied to quantity and
   not price, or the reverse, is the leading candidate).
2. **Until the trace lands, nothing relies on those two accounts' levels.**
   - No consumer reads the tables today (0 readers), so nothing is moved now.
   - FWD-3 is graded REALIZED for the 4 tables EXCEPT these two accounts' `account_day_value` levels. That grade is held as PARTIAL, naming them.
3. **If the trace shows the r28 level is wrong,** round 30 cell 2 repairs it, or blanks the two accounts' levels as ABSENT under a pair. These are the
   same two accounts as W53-S3's four ABSENT months.

### Enrichment list (round 30)

1. The D2-S45 trace.
2. The W53-S3 dividend-dating trace, if not yet drained.
3. The W53-S4 re-count after the price fill.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 6 (2026-10-09 ~09:0xZ) -- round 30 (CVO slug msg 2965, `ADJUDICATION_v24.md` @062a357e4d)

**Read:**
- CB30ad1-AC2 is MET. The 2.45x factor sits on CUSIP 808524102 (x3) and 808524839 (x2), around a split on 2024-10-11.
- "r28 is right" is an INFERENCE, labelled as such. D2-S45 stays OPEN.

**RULING (round 31): one cell settles it with one outside price, then branches by the producer's own rule.**
1. **Fetch the as-traded close for 2022-10-12** for both securities from Yahoo, the price source of record, yfinance-first, on Andrew's word @9ae5d353d1; egress is
   open. Store it at an `address()` path with its as-of and source. It is evidence, not a served price.
2. **Branch A:** about 39.99 and 39.44. r28 is right, D2-S45 closes, and FWD-3's PARTIAL lifts for those two accounts' levels.
3. **Branch B:** about 13.33 and 19.72. r28 double-scales. The next cell repairs the level, or blanks the two accounts' `account_day_value` as ABSENT, under a
   never-widen pair. Until then, FWD-3 stays PARTIAL on them.
4. **Any other value is a third branch.** It is a BLOCKING row; neither branch is assumed.

-- 1.0.0_SA_CTO~DELL2
