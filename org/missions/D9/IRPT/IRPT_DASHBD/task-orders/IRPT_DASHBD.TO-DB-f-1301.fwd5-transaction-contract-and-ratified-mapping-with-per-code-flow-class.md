# TO IRPT_DASHBD.TO-DB-f-1301 -- the FWD-5 TRANSACTION CONTRACT: `IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json` 0.1.0 (the table `account_transaction`, its 17 columns with a claim each, the ratified enums, the type-to-action table, the 30-pair flow-class rule and the 224-row source mapping with each 49 Financial code's flow class) and the same mapping as the producer's data file `transaction_words.json`; a contract and a data file, no producer code, nothing served

<to_id>IRPT_DASHBD.TO-DB-f-1301</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1301</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>127</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-124 analysis for F-SHIP (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_124_20261016.md`, msg 9097: "RATIFIED ... `~F2` writes the transaction contract and its per-firm producer (row S103) on these words ... Each `tran_srcde` row carries its own `flow_class`, from the CRO classification table (IRAWH and MCE: EXTERNAL-OUT) ... `UNMAPPED` lines are shown as \"Other\" with their count ... A new code in the silver that is not in the mapping reads `UNMAPPED` with reason `CODE_NOT_IN_MAPPING` until a row is added: it is counted, never dropped") and the round-123 analysis (msg 9064, ruling 1: a field the producer computes carries `inferred` plus a method, never `absent`) | **Rows:** IRPT_DASHBD-D2-W1301-S<k> | **Decomp cell:** `DB-f-1301` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R127_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1301` (branch `wk-IRPT_DASHBD-1301`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1301/`. The folders `org/standards`, `org/tier1_exec/4.0.0_SA_CRO/deliverables` and `data/assets/scripts/gold/irpt_reporting` are materialized for reading and for the two granted files (if one is missing, run `git sparse-checkout add <folder>`: that is not a grant to edit). Never push; never commit the workspace `portal` gitlink. A READ plus two new files: no AWS call, no network, no vendor call, no secret read. No real client, household or account id, no client figure and no security name in the repo, a row or your report.

**Why.** The FWD-5 words were ratified (round 124). The contract is the one place the table's shape, claims, vocabulary and per-code mapping live; the producer (cell `DB-f-1302`, after this one) is bound to it by a schema hash and by a test. This seat is the contract's sole writer (CTO ruling 3, round 119), so you write it as this seat's worker under this order.

**The inputs (read, never edited).** (a) The ratified proposal `deliverables/0.9.0_WK_IRPT_DASHBD~1001/FWD5_WORDS_PROPOSAL_R124.json` (21 type words each with `action`, 8 action words, 224 mapping rows). (b) The CRO table `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json` (187 rows with `tran_srcde`, `partition`, `rule`). (c) The live census `deliverables/2.0.0_SA_COO~F2/R124_LIVE_SILVER_CENSUS_49F.json` (160 codes). (d) The round-123 ground read `deliverables/0.9.0_WK_IRPT_DASHBD~901/RD_FWD5_PRODUCER_GROUND_R123.json` (which columns have a silver source). (e) The class contract `org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json` for FORM only (its keys, how `columns`, `enums`, `schema_hash` and `served_note` are written). (f) The checker `deliverables/2.0.0_SA_COO~F2/checks/r127/p127_contract.py` (read it first: it states every rule the contract must meet; its reason line tells you what to fix).

**The cell (`DB-f-1301`).**
1. **The contract file** `org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json` with EXACTLY these top-level keys: `contract_version` "0.1.0", `project` "IRPT_DASHBD", `prd` (the PRD path), `authored_by` ("0.9.0_WK_IRPT_DASHBD~1301"), `authored_under` (this order's id and round, and the CTO analyses it follows), `table` "account_transaction", `grain` ("account x transaction line"), `partition` "date=YYYY-MM-DD", `producer` ("data/assets/scripts/gold/irpt_reporting/account_transaction.py"), `columns`, `enums`, `type_action`, `flow_class_rule`, `source_mapping`, `unmapped_display` "Other", `new_code_reason` "CODE_NOT_IN_MAPPING", `firms_served` ["49financial"], `firms_pending` (cottonwood and inflection, each {`firm`, `reason`}: no producer yet; the other firms' ground read is round 126; their mapping rows are carried with a null flow class), `rule24_record` (an object whose strings cite the ratified proposal, the CVO's grades and the CTO's ratification message 9097 and analysis path), `schema_hash`, `schema_hash_basis` (as the class contract states its basis), `served` false, `served_note` (nothing is written; the release is a never-widen act that waits on this contract and the producer).
2. **`columns`: exactly these 17, in this order,** each {`name`, `type`, `nullable`, `meaning`, `claim`, and `method` when the claim is `inferred`}. Types are `string`, `date32[day]` or `double`.
   - `firm` string, not null, inferred (method: the registry-derived firm scope of the custody entry, never a typed token). `account_id` string, not null, measured. `business_date` date32[day], not null, measured (the silver partition's business date).
   - `trade_date` date32[day], nullable, measured (the `fact_trn` `trade_date` column the lot source reads). `settle_date` date32[day], nullable, **absent** (no silver column supplies it).
   - `action` string, nullable (null only when the code is not in the mapping), inferred (method: from `txn_type` through `type_action`). `txn_type` string, not null, inferred (method: from `tran_srcde` through `source_mapping`; the string `UNMAPPED` when the mapping holds the code as UNMAPPED or lacks it).
   - `symbol` string, nullable, measured (`ticker_symbol`). `asset_name` string, nullable, **absent**. `units` double, nullable, measured (`quantity`). `price` double, nullable, measured. `amount` double, not null, measured (`gross_amount`; say in `meaning` how the sign is taken from `debit_credit` if the existing returns code (`account_return_daily.py`) signs it, and if it does not, say the amount is the custodian's unsigned gross and file a row).
   - `fee` double, nullable, **absent** (the fee rail is unused by design). `custodian` string, not null, inferred (method: the custody entry's constant). `flow_class` string, not null, inferred (method: per `tran_srcde` from `flow_class_rule` over the CRO table's `(partition, rule)` pairs; `UNRESOLVED` for a code whose CRO rows disagree or that the table does not hold). `source_txn_id` string, nullable, **absent** (no per-transaction id is read; `order_number` is an order-level id and is not used).
   - `coverage` string, not null, inferred (method: `MEASURED`, or `CODE_NOT_IN_MAPPING` for a code the mapping lacks, or `UNMAPPED_BY_TABLE` for a code the mapping holds as UNMAPPED).
   - A column the producer fills is never labelled `absent`; `absent` is only for the four above.
3. **`enums`**: exactly `txn_type` (the 21 ratified type words), `action` (the 8 ratified action words), `flow_class` (EXTERNAL_IN, EXTERNAL_OUT, INCOME, FEE, INTERNAL, CORPORATE_ACTION, UNRESOLVED, in this order) and `coverage` (MEASURED, CODE_NOT_IN_MAPPING, UNMAPPED_BY_TABLE, in this order). `type_action`: the object word to action word from the proposal's `opal_types`.
4. **`flow_class_rule`**: the issuer's 30-pair table, each row {`partition`, `rule`, `flow_class`, `reason`} (a one-sentence reason each). The table (copy it exactly; the checker holds it):

| partition | rule | flow_class |
|---|---|---|
| CONDITIONAL-BY-COUNTERPARTY | acct-transfer, journals, shares-delivered | UNRESOLVED |
| EXTERNAL | checks-classified, returned-deposits | UNRESOLVED |
| EXTERNAL-IN | deposits | EXTERNAL_IN |
| EXTERNAL-OUT | ira-withholding, schwab-checks-out, withdrawals | EXTERNAL_OUT |
| FEE-ADMIN | adr-fee, service-fees | FEE |
| FEE-MANAGEMENT | advisor-fee-explicit, advisory-fee | FEE |
| FEE-MANAGEMENT-VERIFIED | advisor-fee-verified | FEE |
| INTERNAL | alt-income, dividends, int-adj-fc, interest | INCOME |
| INTERNAL | cash-in-lieu, corp-actions, corp-actions-ic, corp-misc | CORPORATE_ACTION |
| INTERNAL | foreign-tax, reinvest, sweeps, trades, withholding | INTERNAL |
| UNRESOLVED | no-rule | UNRESOLVED |
| UNRESOLVED-PENDING-SPECIMEN | lending-misc-ic, misc-adj | UNRESOLVED |

   The reasons: a CONDITIONAL or EXTERNAL-direction pair cannot be classed without the counterparty or the direction, which the line does not carry (UNRESOLVED, counted and shown); an UNRESOLVED pair is the CRO table's own state; INCOME and CORPORATE_ACTION are read from the rule inside the table's INTERNAL partition, because the return engine treats both as inside the account; etc. Write each reason yourself in one sentence.
5. **`source_mapping`**: 224 rows, one per (firm, source value): {`firm`, `field` ("tran_srcde" for 49 Financial, "type" for the other two, as in the proposal), `source_value`, `opal_type` (the proposal's word or `UNMAPPED`, unchanged), `flow_class`, `reason` (the proposal's reason text for an `UNMAPPED` row and for the three silver-only codes, else null)}. `flow_class` for a 49 Financial code is **computed by applying `flow_class_rule` to the CRO table's rows of that code: one class when every row of the code agrees, `UNRESOLVED` when they disagree**; for the three silver-only codes it is fixed: `EXWT` CORPORATE_ACTION and `RDPC` CORPORATE_ACTION (a maturity and a partial call are the issuer-side end or redemption of a holding, the same events as the table's corp-actions codes) and `SQDAJ` UNRESOLVED (the description carries no transaction word); `IRAWH` and `MCE` come out EXTERNAL_OUT by the rule (they sit in the EXTERNAL-OUT partition). For Cottonwood and Inflection rows `flow_class` is null (their producers do not exist yet).
6. **The data file** `data/assets/scripts/gold/irpt_reporting/transaction_words.json`: `{"contract_version": "0.1.0", "type_action": <as the contract>, "source_mapping": <the same 224 rows>}`, written by a short python script from the contract (not by hand), so the two cannot differ. ASCII only; keys sorted or in the contract's order.
7. **`schema_hash`**: sha256 over the sorted `name:type` lines of `columns` joined by newline (the basis the class contract states); compute it, never type it.
8. **Run the checker** (below) until both criteria pass. Do not edit the checker.

<criterion id="DBF127-1-AC1" cell_refs="DB-f-1301"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r127/p127_contract.py" . DBF127-1-AC1</invocation><expect>DBF127-1-AC1 PASS</expect></criterion>
`DBF127-1-AC1` -- the contract has exactly the keys of step 1; `columns` are the 17 of step 2 in order with a type, a nullable boolean, a meaning and a claim from the four-word set, an `inferred` column carries a method, the four absent columns are `absent` and nullable and no filled column is `absent`; `schema_hash` is the sha256 over the sorted `name:type` lines; `enums.flow_class` and `enums.coverage` are as step 3; `unmapped_display` is `Other` and `new_code_reason` `CODE_NOT_IN_MAPPING`; `firms_served` is `["49financial"]` with cottonwood and inflection pending, each with a reason; `served` is false; ASCII only. Base: FAIL (no contract).
<criterion id="DBF127-1-AC2" cell_refs="DB-f-1301"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r127/p127_contract.py" . DBF127-1-AC2</invocation><expect>DBF127-1-AC2 PASS</expect></criterion>
`DBF127-1-AC2` -- the mapping: `flow_class_rule` is the 30 pairs with the classes of step 4 and a reason each; `enums.txn_type`, `enums.action` and `type_action` are the ratified proposal's; `source_mapping` words equal the ratified proposal's 224 rows exactly (no row added, none missing, none changed); every 49 Financial code's `flow_class` equals the class the checker computes from the CRO table by the rule (and the three silver-only decisions, and IRAWH and MCE EXTERNAL_OUT); Cottonwood and Inflection rows carry a null `flow_class`; the 49 Financial rows number the live census's 160 codes; `transaction_words.json` equals the contract's `source_mapping` and `type_action` and its version. Base: FAIL (no contract).

<expected_criteria>DBF127-1-AC1,DBF127-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the proposal, the CRO table, the census, the ground read, the class contract, the producer code and the issuer's checker.
- **No producer code, no wiring, no deploy, no push, no AWS, no network.** The contract says `served` false. Do not add a registry row.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker's rule and this order disagree, report it as a row and follow this order; the issuer amends its own checker.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1301-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1301/
org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/transaction_words.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1301.fwd5-transaction-contract-and-ratified-mapping-with-per-code-flow-class.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R127_F.md</decomp_doc> round 127, workstream ~F2 (F-SHIP), cell `DB-f-1301`.
<owned_cells>DB-f-1301</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF127-1-AC1, DBF127-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1301/IRPT_DASHBD.TO-DB-f-1301.fwd5-transaction-contract-and-ratified-mapping-with-per-code-flow-class.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF127-1-AC1,DBF127-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; how many 49 Financial codes fall in each of the seven flow classes; which codes are `UNRESOLVED` because their CRO rows disagree; how the `amount` sign is taken; the schema hash; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract and a data file in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF127-1-AC1 and AC2 FAIL at base (no contract) and the checker's helpers are exercised by its self-test (10 arms).
lane: the <paths> block IS the grant.
</preflight>
