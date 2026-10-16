# TO IRPT_DASHBD.TO-DB-f-2001 -- the FWD-5 PER-ROW BUSINESS-DATE CLAIM AND THE CONTRACT 0.5.0, ONE CELL, ONE DRAIN: the CTO's round-132 ruling 1 (msg 9498): a row whose business date equals its trade date is `measured`, a rolled line's business date is computed by the rule and is `inferred` with the basis "first NYSE trading day on or after the trade date"; a 19th column `business_date_claim` carries it on every row of all three firms, from ONE shared function in `account_transaction.py`, in one drain with the contract text

<to_id>IRPT_DASHBD.TO-DB-f-2001</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2001</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>134</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-132 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_132_20261016.md` @0791af7d64, msg 9498; the CVO's v142: AC1 to AC3 PASS, J1 Inflection and J2 49 Financial PASS 20/20): "The business-date claim is per row. A line whose business date equals its trade date (a trading day, as received) is `measured`. A rolled line's business date is computed by the rule, so its claim is `inferred`, with the basis 'first NYSE trading day on or after the trade date'. Today every row reads `measured`, which overstates the rolled lines (the claim law). This is one producer change across the three firms, through the shared function, in one drain with the contract text." | **Rows:** IRPT_DASHBD-D2-W2001-S<k> | **Decomp cell:** `DB-f-2001` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R134_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2001` (branch `wk-IRPT_DASHBD-2001`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2001/`. The folders `org/standards`, `lib`, `data/assets/scripts/gold/irpt_reporting`, `data/assets/scripts/lib`, `data/inf`, `infra/logic` and `org/tier1_exec/4.0.0_SA_CRO/deliverables` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. Offline tests only (synthetic frames, a stub S3 client; `upload=False`). **You have NO AWS in this order: make no AWS call of any kind.** No real client, household or account id, no client figure and no security name anywhere; test accounts, symbols and product names are made up.

**Why.** Since round 132 every producer computes `business_date` as the first NYSE trading day on or after the trade date and keeps `trade_date` as received. On a trading day the two are equal and the date is read from the source; on a rolled line (a weekend or holiday trade date: 296 of 3,354,885 49 Financial rows, the Saturday transDates of Inflection, Cottonwood's weekend Trade Dates) the business date is COMPUTED. The contract still calls `business_date` `measured` for every row, which overstates the rolled lines. The claim law: a value carries its claim in a field a consumer can reject on. So each row gets a field, and the column's own claim becomes the weakest row's.

**The inputs (read, never edited).** (a) The contract 0.4.2 on trunk (`org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json`) and its generator `deliverables/0.9.0_WK_IRPT_DASHBD~1901/gen_transaction_contract_0_4_2.py` (copy it to `gen_transaction_contract_0_5_0.py` in YOUR folder and change it: never edit the contract by hand), `data/assets/scripts/gold/irpt_reporting/transaction_words.json`; (b) the three producers and their tests (`account_transaction.py`, `account_transaction_cottonwood.py`, `account_transaction_inflection.py`, `tests/test_account_transaction*.py`), `lib/trading_calendar.py` (`first_trading_day_on_or_after`, unchanged); (c) the issuer's records in `deliverables/2.0.0_SA_COO~F2/` (read by the checkers; unchanged); (d) the four checkers in `deliverables/2.0.0_SA_COO~F2/checks/r134/`: `p134_contract.py`, `p134_dates.py`, `p134_inflection.py` and the regression leg `p134_cottonwood.py` that `p134_dates.py` runs (**read them first; they state every rule; their reason lines tell you what to fix; each has a `--selftest`**).

**The cell (`DB-f-2001`), in this order; commit after each of steps 2 and 4.**

1. **The one claim function and the 19th column, in `account_transaction.py`** (the shared module; the other two producers import from it, never copy):
   - `business_date_with_claim(trade_day, window=BUSINESS_DATE_WINDOW)` returns `(business_day, claim)`: `business_day` is `trading_calendar.first_trading_day_on_or_after(trade_day, window)`; `claim` is `"measured"` when `business_day` equals the trade day (as a date), else `"inferred"`; `(None, None)` when no trading day lies in the window. It accepts a `datetime.date` or an ISO string. It is the ONLY place the claim is decided.
   - A 19th column LAST: `business_date_claim`, `pa.string()`, NOT nullable (`COLUMNS`, `ARROW_SCHEMA`, the writer and every existing test move with it).
   - `check_transaction_rows` refuses (`SystemExit` whose message contains the word `claim`) a row whose `business_date_claim` is not `measured` or `inferred`, or is `measured` while `business_date` differs from `trade_date`, or `inferred` while they are equal.
2. **The three producers call it.** In `account_transaction.py` (49 Financial), `account_transaction_cottonwood.py` and `account_transaction_inflection.py`: where each now calls `first_trading_day_on_or_after`, call `business_date_with_claim` instead and write the claim as the 19th key `business_date_claim`; a `(None, None)` is refused exactly as the old `None` was. The source's own business date is still not the answer. Nothing else in any producer changes (the status filter, the key function, the reasons, the offsets, the writers' partition refusal). Update the docstrings that describe the day. Add tests: at least 4 for 49 Financial (so its file passes at least 55), at least 4 for Cottonwood (at least 56), at least 4 for Inflection (at least 60, names additionally containing `claim`): a trading-day line is measured, a rolled line (a Saturday) is inferred with `trade_date` as received, the check refuses a lying claim and a word outside the two, and each writer refuses a rolled line whose claim says measured.
3. **Words file and contract generator**: `gen_transaction_contract_0_5_0.py` (adapted from the 0.4.2 generator) writes the contract AND `transaction_words.json`; the words file keeps exactly its sections, each equal to the contract's; its `contract_version` is "0.5.0".
4. **The contract 0.5.0** replaces the file, with EXACTLY the top-level keys of 0.4.2 (the checker's `KEYS` list is the list). `contract_version` "0.5.0"; `supersedes` begins "0.4.2"; `authored_by` your serial. Changes, and only these:
   - `columns`: 19, `business_date_claim` last: `string`, `nullable` false, claim `inferred`, `method` saying: it is computed by the producer from the two dates; **measured** where `business_date` equals `trade_date` (a trading day, as received), **inferred** where the line was rolled forward by the rule; `meaning` naming both words. The schema hash is recomputed by the generator (it CHANGES: 19 names).
   - `columns[business_date]`: `claim` becomes `inferred` (its weakest row) and its `method` names the per-row field `business_date_claim` and the basis "first NYSE trading day on or after the trade date"; its `meaning` still names `first_trading_day_on_or_after`.
   - `business_date_rule` gains: `claim_field` "business_date_claim"; `basis` "first NYSE trading day on or after the trade date"; `claims` `{"measured": "business_date equals trade_date, a trading day as received", "inferred": "rolled forward by the rule"}`. The existing keys stay.
   - `served_note` gains one sentence naming the per-row claim. Unchanged: everything else in 0.4.2 (including `round_132_censuses`, `s6_ruling`, `row_filter`, `price_rule`).
5. **Mutants** (temporary, reverted): (a) make `business_date_with_claim` return `"measured"` always: at least one test of each producer file must fail; (b) make `check_transaction_rows` skip the claim consistency: at least one 49 Financial test must fail. Say which test failed each. Run `tests/test_account_class_daily.py` and `lib/tests/test_trading_calendar.py` once (both must still pass).

<criterion id="DBF134-1-AC1" cell_refs="DB-f-2001" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r134/p134_contract.py" . DBF134-1-AC1</invocation><expect>DBF134-1-AC1 PASS</expect></criterion>
`DBF134-1-AC1` -- the contract 0.5.0 in one verdict: its form (the keys, version 0.5.0 superseding 0.4.2, 19 columns and the recomputed schema hash), then every binding of 0.4.2 plus the per-row claim: the `business_date_claim` column (non-null string, inferred, a method that says when it reads measured and when inferred), the `business_date` column's claim `inferred` with a method naming the field, and `business_date_rule` carrying the claim field, the basis and the two claim texts; the words file equal to the contract's sections. Base: FAIL (the contract is 0.4.2).
<criterion id="DBF134-1-AC2" cell_refs="DB-f-2001" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r134/p134_dates.py" . DBF134-1-AC2</invocation><expect>DBF134-1-AC2 PASS</expect></criterion>
`DBF134-1-AC2` -- the per-row claim across the 49 Financial and Cottonwood producers and the shared function, run by the checker: `business_date_with_claim` behaves as step 1 (measured on a trading day, inferred on a Saturday and a holiday, (None, None) in a too-small window, an ISO string accepted); 49 Financial reads measured, inferred, measured on its three test lines and Cottonwood inferred on a Saturday trade date and measured on a trading day; `check_transaction_rows` refuses a claim that disagrees with the dates and a word outside the two in both modules; the round-132 date rule, the writers' partition refusal and the calendar tests (at least 26), the 49 Financial and Cottonwood test files (at least 55 and 56 tests) and the round-131 key criteria on the 19-column schema (87 Actions, 33 pairs, 160 codes) still hold. Base: FAIL.
<criterion id="DBF134-1-AC3" cell_refs="DB-f-2001" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r134/p134_inflection.py" . DBF134-1-AC3</invocation><expect>DBF134-1-AC3 PASS</expect></criterion>
`DBF134-1-AC3` -- the Inflection producer on the 19-column schema, run by the checker: its test file passes at least 60 tests (names additionally containing `claim`); a trading-day transDate reads measured, a Saturday transDate keeps `trade_date` as received, rolls `business_date` to the Monday and reads inferred; the check refuses a measured claim on a rolled line; every round-132 rule (status, the one key function, the fund-only price and reasons, the Reversed offsets, the partition refusal, the 48 live descriptions) still holds. Base: FAIL.
<criterion id="DBF134-1-J1" cell_refs="DB-f-2001" judgment="true">JUDGMENT, graded only by 3.0.0_SA_CVO at L9, never self-graded: the CVO compares **20 sampled rows of the Inflection producer's output, drawn FRESH after this merge, against the source rows by their NATURAL KEY**, field by field for the 19 columns, including that `business_date_claim` is `measured` exactly where `business_date` equals `trade_date` and `inferred` on a rolled line. The sample includes at least one rolled line and at least one measured line. The issuer produces the sample after the merge (read-only, `upload=False`), drawn only from Complete rows whose natural key is unique within its partition, and prints the duplicate census over the FULL domain (every partition: the CTO's round-130 rule, msg 9498 ruling 3) beside it; the committed form holds the day, the key hash and the non-figure results.</criterion>
<criterion id="DBF134-1-J2" cell_refs="DB-f-2001" judgment="true">JUDGMENT, graded only by 3.0.0_SA_CVO at L9, never self-graded: the CVO compares **20 sampled rows of the 49 Financial producer's output, drawn FRESH after this merge, against the source rows by their NATURAL KEY**, field by field for the 19 columns, including the per-row claim; the sample includes at least one of the lines whose trade date falls on a non-trading day (so it reads `inferred`) and at least one `measured` line. Drawn and committed as for J1. S102, S103, S106 and S107 stay ARMED to the release after-reads.</criterion>

<expected_criteria>DBF134-1-AC1,DBF134-1-AC2,DBF134-1-AC3,DBF134-1-J1,DBF134-1-J2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `lib/trading_calendar.py`, the censuses, the ground-read records, the CRO table, the taxonomy, the adapters, every other producer and test, the handler, every Terraform file and the issuer's checkers and tools.
- **AWS: none.** No call, no listing, no read of a value, no write.
- **NOT WIRED.** No producer is imported by any other file; do not edit the handler or any Terraform. The contract says `served` false.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker rule and this order disagree, follow this order and file a row. A neighbouring test that pins a contract version or a column count outside the grant is reported as a row, not edited.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2001-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write. ONE merge lands the claim function, the 19th column, the three producers, the contract and the words file together. If a commit is refused because the order is `complete`, stop and report; the issuer reopens it.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2001/
org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/transaction_words.json
data/assets/scripts/gold/irpt_reporting/account_transaction.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction.py
data/assets/scripts/gold/irpt_reporting/account_transaction_cottonwood.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction_cottonwood.py
data/assets/scripts/gold/irpt_reporting/account_transaction_inflection.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction_inflection.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2001.fwd5-per-row-business-date-claim-and-contract-0-5-0-one-drain.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R134_F.md</decomp_doc> round 134, workstream ~F2 (F-SHIP), cell `DB-f-2001`.
<owned_cells>DB-f-2001</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF134-1-AC1, DBF134-1-AC2, DBF134-1-AC3 (mechanical); DBF134-1-J1, DBF134-1-J2 (judgment, the CVO's). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2001/IRPT_DASHBD.TO-DB-f-2001.fwd5-per-row-business-date-claim-and-contract-0-5-0-one-drain.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF134-1-AC1,DBF134-1-AC2,DBF134-1-AC3 --governing-order <this order>` BEFORE the flip (the judgment criteria carry no worker verdict); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each mechanical criterion's last line; the test counts of the three producer test files, the calendar test file and the existing class-test result; the two mutants and which test failed each; the contract's NEW schema hash and the old one; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract, a data file, three modules imported by nothing and their offline tests in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access in this order.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the producers are not scheduled.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF134-1-AC1, AC2 and AC3 FAIL at base and the checkers' helpers are exercised by their self-tests (59, 8 and 14 arms).
lane: the <paths> block IS the grant.
</preflight>
