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

## ADDENDUM 7 (2026-10-09 ~09:3xZ) -- round 31 (CVO slug msg 3003, `REMEDIATION_v22.md` @c592a742ed)

**D2-S45 is CLOSED on Branch A.**
- The Yahoo as-traded closes for 2022-10-12 are 41.94 and 44.93, which sit at r28's level, not r26's (3x and 2x lower).
- Yahoo's split series names the same x3 and x2.
- No split re-mint is owed. **FWD-3's PARTIAL lifts for the two accounts' levels.** FWD-3 is REALIZED, except the W53-S3 four ABSENT account-months, which stay
  ABSENT with their reason.

**W58-S1 (BLOCKING) is a separate finding:** the chain's base close for SCHB and SCHZ sits 4.6% and 12.2% under as-traded, on both methods.

**RULING (round 32): trace it per the packet's option (b).** That is a read-only trace of which base date and price source the chain uses for those two
tickers, against the Yahoo as-traded series already landed. **Nothing served moves until the trace names the cause.**
- If the base is wrong, the repair rides a pair.
- If the 4.6% and 12.2% are distribution adjustments (an adjusted-close base), the trace says so and the methodology is ruled on, not patched.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 8 (2026-10-09 ~09:5xZ) -- round 32 (CVO slug msg 3055, `ADJUDICATION_v25.md` @261fab3ccc): the price-basis ruling (W59-S1)

**Read:**
- CB32af1-AC2 is MET. SCHB sits just over the tolerance, which changes no reading.
- **W59-S1:** the chain's one price store is a DIVIDEND-ADJUSTED Yahoo vintage, while dividends also book as cash. If that holds store-wide:
  - a payer is valued LOW before its ex-dates;
  - each distribution is counted twice, once in the adjusted price path and once as cash.
  This bears on FWD-3's served tables.

**RULING: the valuation basis is the AS-TRADED close (unadjusted for dividends, adjusted for splits only). Dividends and distributions enter ONLY as cash
flows.**
- **Why:** a position's market value on a day is quantity times that day's traded price. Total return then comes from price change plus the cash the account
  actually received. A dividend-adjusted close already folds the dividend into the price history, so adding the cash too double-counts.
- This is the same basis the D2-S45 settlement used (Yahoo as-traded closes) and the one the custodian statement reports.

**Round 33:**
1. **A read-only census of the price store:** which tickers and dates are held adjusted versus as-traded. It prints the denominator and the vintage per
   ticker. Yahoo is the source of record (yfinance first), and its raw `Close` (as-traded) is separable from `Adj Close`.
2. **If any served table was built on adjusted prices,** the repair is a REBUILD on the as-traded basis under a never-widen pair. The pair names every table and
   date that moves and its rollback version. Until it lands, FWD-3's affected rows are marked with `price_basis: dividend_adjusted (known wrong; rebuild
   owed)`, a claim a consumer can reject on. They are not silently served as correct.
3. **SCHB just over tolerance** is re-read after the rebuild. Nothing is tuned to fit it.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9 (2026-10-09 ~10:5xZ) -- round 33 (CVO slug msg 3179, `ADJUDICATION_v26.md` @273d6e934d)

**Read:**
- CB33ag1-AC2 is MET.
- **D2-S50 (BLOCKING):** served `account_day_value` rests on dividend-adjusted or mixed prices for 638,948 of 1,669,040 account-days (688 accounts), and nothing marks
  them.

**FWD-3 is re-graded NOT REALIZED.** The served tables are on the wrong basis for 38% of account-days (ADDENDUM 8's ruling).

**RULING on D2-S50: rebuild, with a reader gate in place of the interim marking.**
- The FWD-3 tables have 0 readers, measured at the mint, so no consumer can be misled today.
- Writing a `price_basis` column into 1.67M served rows only to overwrite it at the rebuild is a served move with no reader benefit.
- So ADDENDUM 8's interim marking is REPLACED by an explicit gate: **no reader, role, route or export is granted on the four FWD-3 tables until the as-traded rebuild
  lands and is graded.** A grant request before that is refused, citing this addendum.
- **Round 34 cuts the rebuild on the as-traded basis** under a never-widen pair: every table and date that moves, with its prior version.

**W60-S1, `bd_txn_price` in `opal-data-cot` written only under `data/black_diamond/`: MEASURE FIRST, then rule.** The cross-firm NEVER turns on the INPUT, not the folder name.
**Round 34 cell 1 is a read-only trace** that names, by file and line:
- the writer;
- every input it reads (bucket and key prefix);
- the account ids it covers.

**The rule, stated before the read:**
- **If it reads only Cottonwood's own Black Diamond account data and writes only `opal-data-cot`,** it is a shared BD platform serving each firm into its own bucket. That is
  allowed, and the folder name is a naming matter.
- **If it reads any other firm's data (49F's BD feed included) to write `opal-data-cot`,** it is the cross-firm NEVER. That is a BLOCKING row, and
  `.tools/ds-precommit-check.py`'s foreign-prefix list gains the path. The served `bd_txn_price` objects are then held from FWD-3's rebuild until re-sourced.
- Cottonwood and BD/49F are separate firms and are never mirrored (CLAUDE.md 13).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 9.1 (~11:1xZ, `~C2` msg 3187, row W61-S1 BLOCKING): `bd_txn_price` is CROSS-FIRM -- who edits the guard

**Measured by worker `~61`** (`deliverables/0.9.0_WK_ADVI_COTBKF~61/bd_txn_writer_trace.md`, @248cb44fa0):
- The label's only writer is 49 Financial's `data/black_diamond/scripts/silver/inject_scoped_overrides.py:136`.
- It reads 49F's `scoped_price_exceptions.json` and `s3://opal-data-bd/silver/prices/canonical_prices.parquet`.
- **The cot store's three bonds carry 49F's constants**, and cot's pipeline does not run that inject.

**The guard already forbids the code path.** `.tools/ds-precommit-check.py`'s `_CROSS_FIRM_FOREIGN_BUCKETS` already lists:
- `data/cot/` -> `opal-data-bd`, `opal-data-49financial`;
- `data/black_diamond/` -> `opal-data-cot`.
That block is GENERATED from `infra/logic/registry/scopes.json` and is never hand-edited. So no current cot code path reads 49F's prices without the gate refusing it.
**The contamination is DATA that reached the cot store by some other route** (an earlier copy or seed). Another gate line is not the remedy.

**RULING (round 34 or 35, `~C2`):**
1. **A read-only provenance trace of the three cot objects:** each key's version history, writer metadata and first-write time, against the commit history of every
   cot writer. The trace names HOW 49F's constants entered `opal-data-cot`.
   - If a live code path is found that the generated guard misses, the fix is a `scopes.json` row, regenerated by `python lib/opal_naming.py generate`. Its owner is
     the registry lane (LGIC). `~C2` may carry it as an in-grant cell on the IB-rtf-4 precedent, under the naming gate.
2. **The three bonds stay held from the as-traded rebuild** (COO half @0071b97a83). Their prices are re-sourced from Cottonwood's own source of record (Yahoo
   as-traded, ADDENDUM 8). They are never taken from 49F's overrides.
3. **The contaminated objects are NOT deleted by a seat.** Their removal is an S3 delete, Andrew's act, listed with keys and versions once the trace names them.
   Until then they are excluded from every read by the rebuild.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 10 (2026-10-09 ~12:2xZ) -- round 35 (CVO slug msg 3260, `ADJUDICATION_v27.md` @1ba319c437)

**Read:**
- CB35ai1-AC2 is MET. The detector changed after run 1; 319a716cb4 corroborates the class.
- **W60-S1 is ANSWERED:** a since-removed shared-builder chain wrote 49F bond overrides into cot. The live code path is gone, which matches ADDENDUM 9.1 (the guard
  already bars it).
- **D2-S52 (BLOCKING):** those 49F rows remain in 38 full Cottonwood price keys.

**RULING: a REWRITE under a never-widen pair, not a delete. This is the CVO's recommendation.**
- The cot bucket is versioned, so a rewrite writes a new version of each of the 38 keys and keeps every prior version. That is reversible, and it is not the S3 delete
  reserved to Andrew.
- **The rewrite:**
  - removes the 49F-sourced rows;
  - re-prices the three bonds from **Cottonwood's source of record: Yahoo as-traded closes** (ADDENDUM 8, yfinance first);
  - leaves every other row byte-identical. The pair proves it with a per-key diff of the row counts (only the 49F rows and the three bonds' prices move).
- **The pair names all 38 keys with their prior version ids, and rollback is a copy-object of each.**
- **Deleting the old versions that carry the 49F rows is a separate act, reserved to Andrew** (CLAUDE.md Agent Autonomy). It is listed for him, and it is not needed for
  correctness, since every reader reads the latest version.
- **The as-traded FWD-3 rebuild (ADDENDUM 9) reads the REWRITTEN keys.** It is sequenced after this rewrite.

Round 34 stays open (`~C2`). The rewrite cell and its pair go into the next issuance.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 11 (2026-10-09 ~13:0xZ) -- round 34 (CVO slug msg 3298, `ADJUDICATION_v28.md` @7579e95822, grade `ADVI_COTBKF_ROUND_34_L9_GRADE_20261009.md`)

CB34ah1-AC2 and CB34ah2-AC3 are MET. The three FWD-3 tables are served at `price_basis=as_traded` (CB-ah-3, @20e7c39855): MATCH 3,678, DIFF 293.
D2-S50, W59-S1 and W53-S3 are closed. REMEDIATION_v26 carries 6 OPEN rows.

**FWD-3 is re-graded REALIZED, with two named exceptions** (the ADDENDUM 7 pattern):
1. the 5 account-months ABSENT under the as-traded basis (`REGRESSED_UNDER_AS_TRADED`, D49151054 about 0.6 pp), each carrying its row;
2. the 988 held bond account-days (three cross-firm bonds, `HELD_SOURCE_UNDER_REVIEW`). They re-enter only through the ADDENDUM 10 38-key rewrite and a later delta.

**RULING on the reader gate (ADDENDUM 9): its condition is MET, and it opens after ONE row.**
- `~C2` appends one row explaining `control_same=False`: the control accounts moved because the basis changed for every account, so the
  re-grade has no no-change arm. The row states this, with the count of control accounts that moved and the largest move.
- **If any control account moved for a reason other than the basis change, the gate stays shut** and the row is BLOCKING.
- Opening the gate grants nothing by itself. **Each reader, role, route or export is its own never-widen pair.** That pair's blast radius
  names both exceptions above, so a reader is told what is blank and why.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 11.1 (~13:1xZ, `~C2` msg 3326): the reader gate is OPEN

**The gate condition is met (row D2-S59 @1dc34e3f03).**
- 7 of 566 control months moved, across 5 accounts.
- Every changed held price is a re-priced canonical-store point, and there is no other cause.
- The largest move is RGY005018 2024-11, -0.83 pp (DIFF to MATCH).

**The ADDENDUM 9 gate is therefore OPEN. Nothing is granted by this line.** Each reader, role, route or export is its own never-widen pair, naming both ADDENDUM 11
exceptions. Every reader read stays inside this firm's tree (CLAUDE.md, the cross-firm NEVER).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 11.2 (~13:3xZ): enrichment item from IRPT_DASHBD -- the Cottonwood daily returns gold

`s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/` holds 0 objects (IRPT_DASHBD row S43). IRPT_DASHBD FWD-12, the first real custody
statement, needs it. **COTBKF's next issuance carries ONE cell:**
- mint that table from the as-traded FWD-3 tables, with its address from `opal_naming address()`;
- give it the same two named exceptions (the 5 ABSENT months and the held bonds) as blanks with reasons;
- write it under its own never-widen pair.

The ADDENDUM 11.1 reader gate applies: readers come one pair at a time. The first reader is the laptop's hop3 leg (IRPT_DASHBD ADDENDUM 11.1).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 12 (2026-10-09 ~13:4xZ) -- round 37 (CVO slug msg 3387, `ADJUDICATION_v29.md` @b040240378)

CB37ak1-AC2 is MET (row D2-S61).
- All 988 held account-days belong to the Wells Fargo 4.15% 2029 bond.
- BNP and Newmont have NO Cottonwood holder, so their 49F rows were pure contamination.
- By the CB-aj-2 half's source order, all three stay UNPRICED until a firm-owned custodian price is found.

**RULING on D2-S62: the cross-firm test keys on a FIRM FIELD, never a token.**
- `bd_` names two different things:
  - the Black Diamond PLATFORM, a custodian or reporting vendor that serves Cottonwood; its data is Cottonwood's own;
  - the bd FIRM, another firm.
  A token cannot tell them apart, so a token test either wrongly refuses Cottonwood's own platform data or wrongly admits the other firm's.
- **Every price row carries `source_firm`.** It holds the firm whose data or configuration produced the row, set by the writer from its INPUT's address (the bucket and
  key prefix it read), never from a name or ticker token.
- The cross-firm check reads `source_firm != cottonwood` as the breach. A missing `source_firm` is `absent`, which the check grades as NOT-CLEAN (A VALUE MUST CARRY ITS
  CLAIM).
- **COTBKF next issuance, ONE cell:** add `source_firm` at the cot price writer (`build_canonical_prices_v2.py`) and to the rewrite census.
  - The 38 rewritten keys are not re-minted for this. The field arrives with the next silver-prep under its own pair.
  - The repo-side guard (`.tools/ds-precommit-check.py`) is bucket- and prefix-based already, and is unchanged.

**Enrichment list for round 38:**
1. `gold/account_return_daily` (ADDENDUM 11.2);
2. the `_ff_worker` carry-forward flag (CB-aj-2 half AMENDMENT 1);
3. `source_firm` on price rows (this addendum);
4. the bonds' firm-owned price measurement (W64-S1 ruling).

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 13 (2026-10-09 ~14:1xZ) -- rounds 36 and 39 (CVO slug msg 3419, `ADJUDICATION_v30.md` @5c363d0c76): both MET

1. **D2-S52 is CLOSED.** 1,734 49F rows were removed from the 38 cot keys, verify reads 38/38, and every other row is identical. The cross-firm breach in Cottonwood's
   store is gone at the current version.
   - **Deleting the 38 prior versions is Andrew's act.** It is on the act list, each key named in `~CB2`'s apply report @e5eb80c75f.
2. **The `_ff_worker` carry-forward stamp is BUILT, not deployed.** The next issuance cuts ONE SERVED cell to deploy it under its own pair.
   - Its packet's census must show only the carry-forward members.
   - Its proof drives the carry-forward on a synthetic day and reads the stamp.
   - The path is unreachable for cot today, so the proof is not read from a live fire.
3. **D2-S62 waits on round 40's `source_firm` cell** (ADDENDUM 12).
4. **Round 38 (CB-al-2) stays HELD** on the IRPT_DASHBD sources-fields cell (IRPT_DASHBD ADDENDUM 13.1). That is the only thing it waits on.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 14 (2026-10-09 ~14:2xZ) -- round 40 (CVO slug msg 3441, `ADJUDICATION_v31.md` @615a267925): MET

CB40an1-AC2 is MET:
- `source_firm` comes from the input address via the registry, with no typed token;
- absent is never defaulted;
- the census grades absent as NOT-CLEAN.

**RULING on W68-S2: the writer's deploy ships the registry it reads, in the SAME pair.**
- The cot gold run syncs only `code/gold/`. A writer deployed without its registry reads every row `source_firm: absent`. That is safe, because it grades NOT-CLEAN,
  but it is useless.
- **One SERVED cell with one pair and two keys:**
  - the writer at `code/gold/`;
  - the registry file it resolves firms from, at a `code/gold/` key the sync already carries, pinned to its blob.
  - The writer loads it from its own directory. No new sync prefix and no second path.
- The packet's census shows exactly those two keys.
- **The proof is the next silver-prep census:** `source_firm=cottonwood` on every row, and `BREACH=0`. **That read closes D2-S62.**

**W68-S1 (a dead share-class check): REMOVE it in the same cell (YAGNI).** It is a deletion of unreachable code, and the cell's own test proves no path reached it.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 15 (2026-10-09 ~14:4xZ) -- round 41 (CVO slug msg 3473, drain-end @aee55e309d): MAY-CLOSE

- **The carry-forward stamp is live:** `code/gold/B_00.canonical_holdings.py` is at version `hU7ZrZTD` (14:19:29Z), sha256 `45fbbd92...`, equal to the repo file.
  - The proof ran on the SERVED bytes (3 passed).
  - A planted mutant drove it to fail, so the test binds to those bytes (`~CB2` @3b9c1f32a4).
- **The CB-ao-1 half's condition 4 is re-stated, because the cot gold run is MANUAL, not scheduled.** The CVO read it; no wait without a clock is allowed.
  - **The on-demand proof is the reachability read:** `~C2` re-reads `schwab/silver/rps/` as empty, against the `silver/prices/` positive control, once in the round-42
    drain. That is the condition under which output cannot move.
  - The output-fingerprint read stays a watch row with no clock. It is graded at whichever cot gold run comes next, manual or not.
- No rows; ARMED 0.

-- 1.0.0_SA_CTO~DELL2
