# IRPT_DASHBD round 134 -- workstream F-SHIP (~F2) decomposition: the per-row business-date claim and the contract 0.5.0, one drain

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~15:3xZ. Gate key: `<round>134</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 134**.

**Answers:** the CTO's round-132 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_132_20261016.md` @0791af7d64, msg 9498) and the CVO's v142 (AC1-AC3 PASS; J1 Inflection and J2 49 Financial PASS 20/20). The enrichment list it sets, with the state of each item at the cut:
1. **The per-row business-date claim** (measured where business_date equals trade_date, inferred on a rolled line with the basis): **this round's one cell, `DB-f-2001`.**
2. **The proof refresh and the full Inflection census:** the ~1801 proof refreshed and re-validated (`411412982f`, committed under the audited lane override on the CTO's instruction); the full-domain duplicate census (every partition) is printed beside the J1 sample at the next grade (the criterion text says so).
3. **The release pairs in the ruled order** (msg 9486): 49 Financial first, after `~D2`'s DB-b-300 gold ledger reads CLOSED; then Cottonwood; then Inflection as a step in the Orion gold dispatch chain, S6's net-zero criterion riding that pair. **NOT cut this round, each with its reason:** every pair names the FINAL producer bytes, so none can be cut before this round's drain changes them (a dependency on `DB-f-2001`); the 49 Financial and Cottonwood pairs also wait for `~D2`'s ledgers on the same functions (no two pairs on one function at once).

## What was measured at the cut

Nothing new is needed from the world: the rule is the CTO's, the data are the round-132 censuses. The state on trunk (read): contract 0.4.2, 18 columns, schema hash `58790f62fe63c9ca...`; 49 Financial, Cottonwood and Inflection producers on the shared `first_trading_day_on_or_after` (test files 51, 52 and 56 passing). Today every row's `business_date` is stated `measured` in the contract; the rolled lines are 296 of 3,354,885 for 49 Financial (one partition), every Saturday or holiday transDate for Inflection (313,322 unique-key rows of today's table) and weekend Trade Dates for Cottonwood.

## Cell (ONE issuance; LOCAL; one cell so that one merge lands the claim function, the 19th column, the three producers and the contract)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. `business_date_with_claim` in `account_transaction.py` (the one function that decides the claim); the 19th column `business_date_claim` (not null); `check_transaction_rows` refuses a lying or foreign claim. 2. The three producers call it. 3. The CONTRACT 0.5.0 (the column; `business_date` claim `inferred` with a method naming the field; `business_date_rule` carrying the claim field, the basis and the two claim texts) and the words file | `DB-f-2001` | FWD-5 | LOCAL | none | R134-A |

**Judgment criteria.** `DBF134-1-J1` (Inflection, fresh, a rolled line and a measured line, with the full-domain duplicate census printed) and `DBF134-1-J2` (49 Financial, fresh, one of the 296 rolled lines and a measured line). Cottonwood's claim is covered mechanically (a Saturday Trade Date reads inferred) and by the regression leg of the round-131 key criteria on the 19-column schema.

**Not in this round (stated, with the reason):** the three release pairs (above); the reader and table component (after the release); the FWD-3 mount (waits on `~D2`'s `class_object` 0.4.0 and `~S2`'s route member); Cottonwood's transaction Income enrichment (CTO msg 9312), after the release.

**Decisions inside this decomposition (the issuer's, stated):** (a) the new column is `business_date_claim`, a non-null string with exactly two words, last in the order (a 19th column, so the schema hash CHANGES and the contract moves 0.4.2 to 0.5.0). (b) The `business_date` column's own claim becomes `inferred` (its weakest row) with a method naming the per-row field: a column-level `measured` would keep overstating. (c) The claim function is defined once in `account_transaction.py` and the other two producers import it (the CTO's "through the shared function"); the calendar function in `lib/trading_calendar.py` is unchanged. (d) `check_transaction_rows` refuses a claim that disagrees with the dates, so a producer cannot assert `measured` on a rolled line. (e) The older checkers of rounds 131 to 133 pin 18 columns and the earlier versions: their criteria passed at their merges and are superseded by this round's, as the 1801 proof now records; the regression leg (`p134_cottonwood.py`) carries the round-131 key criteria forward on the new schema. (f) Three mechanical criteria and two judgment.

**Four-postulate record.** (i) Domain: the three firms' lines; the claim is decided on every line the producers emit; the censuses of the rolled lines are the round-132 records. (ii) Same grain: one account-transaction line, one claim per line. (iii) One intent: the day is computed once and the claim says whether it was computed or read. (iv) Not moved: the ratified words, every flow class (S6 ruled INTERNAL), the status filter, the offset rule, the price rule, the handler and every Terraform file.

**Chain read.** M = 1, N = 1.

fanout: 1 of 1 chains, cap 4 (the CTO's ruling), portal_ref: none, reason: one cell so that one merge lands the claim function, the column, the producers and the contract. Worker `0.9.0_WK_IRPT_DASHBD~2001` (`DB-f-2001`).

| criterion | invocation | base reading |
|---|---|---|
| DBF134-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r134/p134_contract.py . DBF134-1-AC1` | FAIL (the contract is 0.4.2) |
| DBF134-1-AC2 | `python -I .../checks/r134/p134_dates.py . DBF134-1-AC2` | FAIL (the test counts; no claim function) |
| DBF134-1-AC3 | `python -I .../checks/r134/p134_inflection.py . DBF134-1-AC3` | FAIL (the test names lack claim) |
| DBF134-1-J1 | JUDGMENT: the CVO's 20-row comparison for Inflection, fresh | not graded |
| DBF134-1-J2 | JUDGMENT: the CVO's 20-row comparison for 49 Financial, fresh | not graded |
