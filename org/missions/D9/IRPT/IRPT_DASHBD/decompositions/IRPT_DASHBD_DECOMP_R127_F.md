# IRPT_DASHBD round 127 -- workstream F-SHIP (~F2) decomposition: the FWD-5 transaction contract and the 49 Financial producer

Issuer `2.0.0_SA_COO~F2`, 2026-10-16 ~06:1xZ. Gate key: `<round>127</round><workstream>~F2</workstream>`. Workstream label beside the round: **F-SHIP, round 127**.

**Answers:** the CTO's round-124 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_124_20261016.md`, msg 9097): the FWD-5 words are RATIFIED (49 Financial at `tran_srcde` grain, 160 codes, 16 UNMAPPED; Cottonwood and Inflection as proposed); flow class is a property of each code, from the CRO table; "`~F2` writes the transaction contract and its per-firm producer (row S103) on these words". Also the round-123 analysis (msg 9064) ruling 1 (a computed field carries `inferred` plus a method, never `absent`) and the round-121 analysis (the first served account is a 49 Financial one).

## What was measured at the cut

- The ratified proposal is `deliverables/0.9.0_WK_IRPT_DASHBD~1001/FWD5_WORDS_PROPOSAL_R124.json` (21 type words each carrying an action, 8 action words, 224 mapping rows). The ground read (round 123) found 7 of the brief's 14 columns have a 49 Financial silver source and 4 are plainly absent (`settle_date`, `asset_name`, `fee`, `source_txn_id`); the rest are computed.
- The CRO table has 30 distinct `(partition, rule)` pairs; 7 codes sit under more than one partition. A code's flow class is therefore computed by a rule over its rows (one class when they agree, `UNRESOLVED` when they disagree). The rule table is the issuer's decision, stated in the order and held by the checker; it maps INCOME and CORPORATE_ACTION out of the table's INTERNAL partition by `rule`, and sends the counterparty-conditional and direction-conditional pairs to `UNRESOLVED` (they cannot be classed without the counterparty or the direction, which a line does not carry).
- The three silver-only codes' flow classes are decided here on their descriptions' words: `EXWT` and `RDPC` CORPORATE_ACTION, `SQDAJ` UNRESOLVED.
- The class pair (contract `IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json`, producer `account_class_daily.py`, test `test_account_class_daily.py`) is the model for the shape.

## Cells (ONE issuance; LOCAL; a chain of two)

| item | cell | serves | risk | depends on | chain |
|---|---|---|---|---|---|
| 1. The TRANSACTION CONTRACT 0.1.0 and the mapping data file: 17 columns with a claim each, the ratified enums and type-to-action table, the 30-pair flow-class rule, the 224-row source mapping with each 49 Financial code's flow class; the same mapping as `transaction_words.json` | `DB-f-1301` | FWD-5 | LOCAL | none | R127-A |
| 2. The 49 FINANCIAL PRODUCER `account_transaction.py` and its offline tests, bound to the contract by schema hash and mapping; not wired | `DB-f-1302` | FWD-5 | LOCAL | `DB-f-1301` | R127-A |

**Not in this round (stated, with the reason):** the wiring into `reporting-gold/handler.py`, the Terraform write list and the never-widen release for the new gold prefix (a later cell and a sign-off of the CTO and the COO; the owner of that Terraform root applies); the Cottonwood and Inflection producers (their ground read is round 126); the reader, the route member and the table component (wait on the contract and the release); the FWD-3 mount (waits on `~D2`'s `class_object` 0.4.0 and `~S2`'s route member).

**Decisions inside this decomposition (the issuer's, stated):** (a) the workers write the contract and the producer; this seat is the contract's sole writer by the CTO's ruling and acts through its workers; (b) the contract serves 49 Financial only; Cottonwood and Inflection mapping rows are carried with a null flow class, `firms_pending` stating why; (c) the checker holds the rule table, the silver-only decisions and IRAWH / MCE as fixed points and computes every 49 Financial code's flow class from the CRO table; (d) the producer is not wired, imported by nothing, and run only offline; (e) the mapping data file is generated from the contract by a script, and a test and the checker hold the two equal; (f) four mechanical criteria across two orders (two each, within the cap of three per cell).

**Four-postulate record.** (i) Domain: the 17 columns (a printed list, exact order), the 30 CRO pairs, the 224 ratified rows and the 160 live codes, each compared by the checker. (ii) Same grain: one account-transaction line. (iii) One intent per cell: the shape and its words (1301); the code that fills the shape (1302). (iv) Not moved: the ratified words, the CRO table, the class pair, the handler, every Terraform file and every served file.

**Chain read.** M = 1 (A: 1301 then 1302), N = 1. The second order is spawned when the first has merged.

fanout: 1 of 1 chains, cap 8 (the CTO's CPU budget holds `~F2` at 4 per issuance; worker `~1201` of round 126 is also running), portal_ref: none, reason: one chain whose second cell reads the first cell's files. Workers `0.9.0_WK_IRPT_DASHBD~1301` (`DB-f-1301`) then `~1302` (`DB-f-1302`).

| criterion | invocation | base reading |
|---|---|---|
| DBF127-1-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r127/p127_contract.py . DBF127-1-AC1` | FAIL (no contract) |
| DBF127-1-AC2 | `... p127_contract.py . DBF127-1-AC2` | FAIL (no contract) |
| DBF127-2-AC1 | `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r127/p127_producer.py . DBF127-2-AC1` | FAIL (no test file) |
| DBF127-2-AC2 | `... p127_producer.py . DBF127-2-AC2` | FAIL (no producer) |
