# TO IRPT_DASHBD.TO-DB-f-1302 -- the FWD-5 49 FINANCIAL PRODUCER: `account_transaction.py` (one day of the custody transaction silver to `account_transaction` rows by the contract's mapping, a vocabulary check and a builder-address writer) and its offline tests; bound to the contract by its schema hash and its mapping; NOT wired into the reporting-gold handler, never run against S3, nothing served

<to_id>IRPT_DASHBD.TO-DB-f-1302</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~1302</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>127</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-124 analysis for F-SHIP (msg 9097: `~F2` writes the transaction contract and its per-firm producer, row S103; "A new code in the silver that is not in the mapping reads `UNMAPPED` with reason `CODE_NOT_IN_MAPPING` until a row is added: it is counted, never dropped") and the round-121 analysis (the first served account is a 49 Financial one) | **Rows:** IRPT_DASHBD-D2-W1302-S<k> | **Decomp cell:** `DB-f-1302` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R127_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** DB-f-1301 (the contract and `transaction_words.json` are on trunk before this order is spawned)

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-1302` (branch `wk-IRPT_DASHBD-1302`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1302/`. The folders `org/standards`, `lib`, `data/assets/scripts/gold/irpt_reporting` and `infra/logic` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. Offline only: no AWS call, no network, no vendor call, no secret read; the tests use synthetic frames and a stub S3 client. No real client, household or account id and no client figure anywhere; test accounts and symbols are made up.

**Why.** The contract (`org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json`, cell `DB-f-1301`) fixes the table: 17 columns, the ratified words, the per-code flow class. The producer turns one day of 49 Financial's `fact_trn` into those rows. It is the second instance of the shape `account_class_daily.py` has (read it first; copy its structure, not its logic): a pure normaliser, a vocabulary check that refuses rather than serves, and a writer at the builder address. It is not wired into `reporting-gold/handler.py` and no Terraform changes: wiring and the new gold prefix are a later never-widen release.

**The cell (`DB-f-1302`).**
1. **Read first.** The contract and `data/assets/scripts/gold/irpt_reporting/transaction_words.json`; `data/assets/scripts/gold/irpt_reporting/account_class_daily.py` (`TABLE_CLASS`, `ARROW_SCHEMA`, `check_class_rows`, `emit_class_day`, `read_trn_window`) and its test file `tests/test_account_class_daily.py` (the offline test style: `importlib` load, stubs); `account_return_daily.py` for how `gross_amount` and `debit_credit` are read and signed. Run `python -m pytest data/assets/scripts/gold/irpt_reporting/tests/test_account_class_daily.py -q` once before any edit.
2. **ONE new source file** `data/assets/scripts/gold/irpt_reporting/account_transaction.py` exporting, with exactly these names:
   - `TABLE_TRANSACTION = "account_transaction"`.
   - `ARROW_SCHEMA`: the pyarrow schema whose fields are the contract's 17 columns, in order, with the contract's types (`string`, `date32[day]`, `double`) and nullability. A test asserts its name:type lines hash to the contract's `schema_hash`.
   - `load_words()`: reads `transaction_words.json` beside the module (a path derived from `__file__`, never typed) and returns the dict.
   - `normalize_trn(frame, firm, words=None)`: `frame` is a pandas frame with the `fact_trn` columns `account_id`, `business_date`, `trade_date`, `tran_srcde`, `quantity`, `price`, `gross_amount`, `debit_credit`, `ticker_symbol` (it may carry others; they are ignored). Returns a LIST of dicts, ONE PER INPUT ROW IN INPUT ORDER (never fewer: a row is counted, never dropped), each with exactly the contract's 17 keys in the contract's order. Only `firm == "49financial"` is supported (any other firm: `SystemExit("REFUSED: no transaction producer for firm ...")`). Per row: `firm`; `account_id` as given; `business_date` and `trade_date` as `datetime.date`; `settle_date`, `asset_name`, `fee`, `source_txn_id` always `None`; `symbol`, `units`, `price` from `ticker_symbol`, `quantity`, `price` (a missing or NaN value is `None`, never zero); `amount` from `gross_amount` signed the way the contract's `meaning` says (if the existing returns code signs by `debit_credit`, do the same; say which in a docstring); `custodian` the custody entry's constant (take it from the declaration the way `account_class_daily.py` or `account_return_daily.py` reads the custody entry; never a typed token if the declaration holds it; if it holds none, use the constant the existing code uses and file a row); `txn_type`, `flow_class` and `action` as follows. **Mapped code** (in `source_mapping` for 49financial with a word): `txn_type` the word, `action` = `type_action[word]`, `flow_class` the row's, `coverage` `"MEASURED"`. **Code the table maps to `UNMAPPED`:** `txn_type` `"UNMAPPED"`, `action` `None`, `flow_class` the row's, `coverage` `"UNMAPPED_BY_TABLE"`. **Code the mapping lacks:** `txn_type` `"UNMAPPED"`, `action` `None`, `flow_class` `"UNRESOLVED"`, `coverage` `"CODE_NOT_IN_MAPPING"`.
   - `check_transaction_rows(rows)`: raises `SystemExit("REFUSED: ...")` if a row's `txn_type` is outside the contract's `enums.txn_type` plus `"UNMAPPED"`, `action` outside `enums.action` (or `None`), `flow_class` outside `enums.flow_class`, or `coverage` outside `enums.coverage` (the contract's closed sets, read from `load_words()` or the contract file's values carried in `transaction_words.json`; if `transaction_words.json` does not carry the enums, derive them from the mapping and `type_action` and the three constants, and say so in a docstring).
   - `emit_transaction_day(s3, rows, firm, day, *, upload)`: the same shape as `emit_class_day`: the builder address from `opal_naming.address("irpt", firm, "gold", TABLE_TRANSACTION, "date=<day>")` (never a typed key), the rows typed by `ARROW_SCHEMA`, written through the same helper `emit_class_day` uses, with a manifest; `upload=False` makes NO call on `s3` and returns the row count and the address.
3. **ONE new test file** `data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction.py`, offline, made-up rows, at least 14 tests, whose function names together contain the words `mapping`, `unmapped`, `new_code`, `flow`, `action`, `absent`, `schema` and `vocabulary`. They cover: the schema hash equals the contract's and the field order is the contract's; `load_words()` equals the contract's `source_mapping` and `type_action`; a mapped code gets its word, its derived action, its flow class and `MEASURED`; a code the table maps to UNMAPPED gets `UNMAPPED_BY_TABLE` and keeps its flow class; **a new code gets `UNMAPPED`, `UNRESOLVED`, `CODE_NOT_IN_MAPPING` and is counted (the row count in equals the row count out)**; IRAWH is EXTERNAL_OUT and a silver-only code from the census record (`EXWT`) maps as the contract says; the four absent columns are `None` on every row; a missing quantity or price is `None` not zero; the amount sign; the input order is kept; another firm is refused; `check_transaction_rows` refuses a word outside the vocabulary, a flow class outside the seven and a coverage outside the three; `emit_transaction_day` with `upload=False` makes no S3 call (a stub that fails on any call) and its address comes from the builder (a test of the string, with no real account); **every one of the 160 codes in `deliverables/2.0.0_SA_COO~F2/R124_LIVE_SILVER_CENSUS_49F.json` normalises to a row with a defined `txn_type` and `coverage`** (the mapping covers the live silver).
4. **Gates, once, after your last edit:** run `python -m pytest data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction.py -q -p no:cacheprovider` and the existing `tests/test_account_class_daily.py` (both must pass); `.tools/commit-gate.sh` then runs at commit (py_compile, ds-precommit, ruff py39): fix what it names. No non-ASCII in the source file.
5. **Mutant** (temporary, reverted): make a code the mapping lacks come out `MEASURED`; at least one test must fail. Say which.

<criterion id="DBF127-2-AC1" cell_refs="DB-f-1302"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r127/p127_producer.py" . DBF127-2-AC1</invocation><expect>DBF127-2-AC1 PASS</expect></criterion>
`DBF127-2-AC1` -- `tests/test_account_transaction.py` has test function names containing the eight words `mapping`, `unmapped`, `new code`, `flow`, `action`, `absent`, `schema`, `vocabulary` (underscores read as spaces), and `python -m pytest` on it passes with 0 failures, 0 errors and at least 14 tests. Base: FAIL (no file).
<criterion id="DBF127-2-AC2" cell_refs="DB-f-1302"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r127/p127_producer.py" . DBF127-2-AC2</invocation><expect>DBF127-2-AC2 PASS</expect></criterion>
`DBF127-2-AC2` -- the producer against the contract, run by the checker: `ARROW_SCHEMA`'s field names are the contract's 17 columns in order and its name:type lines hash to the contract's `schema_hash`; `TABLE_TRANSACTION` is `account_transaction`; `load_words()` equals the contract's mapping and `type_action`; `normalize_trn` on a three-row frame (a mapped code, a code the table maps to UNMAPPED, a code the mapping lacks) returns three rows with the contract's keys in order, the four absent columns `None`, the mapped row's word, action, flow class and `MEASURED`, the table-UNMAPPED row `UNMAPPED_BY_TABLE` with its flow class, and the unseen row `UNMAPPED`, `UNRESOLVED`, `CODE_NOT_IN_MAPPING` and a `None` action; and `check_transaction_rows` accepts those rows and refuses a word outside the vocabulary. Base: FAIL (no producer).

<expected_criteria>DBF127-2-AC1,DBF127-2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the contract, `transaction_words.json`, every other producer and test, `reporting-gold/handler.py`, every Terraform file, the issuer's checker.
- **NOT WIRED.** Do not import the new module from any other file; do not edit the handler or any Terraform; no S3, no DynamoDB, no network; `upload=False` is the only path any test takes.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the contract and this order disagree, report a row and follow the contract's shape (it is bound by the hash); the issuer amends this order.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W1302-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1302/
data/assets/scripts/gold/irpt_reporting/account_transaction.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_transaction.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-1302.fwd5-49-financial-account-transaction-producer-offline-tests-not-wired.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R127_F.md</decomp_doc> round 127, workstream ~F2 (F-SHIP), cell `DB-f-1302`.
<owned_cells>DB-f-1302</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF127-2-AC1, DBF127-2-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~1302/IRPT_DASHBD.TO-DB-f-1302.fwd5-49-financial-account-transaction-producer-offline-tests-not-wired.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF127-2-AC1,DBF127-2-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the exported names; the test counts, the mutant result and the existing class-test result; how `amount` is signed and where the custodian constant comes from; whether the 160 live codes all normalise; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new module and its offline tests in a branch; imported by nothing; not wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the producer is not scheduled.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF127-2-AC1 and AC2 FAIL at base (no producer) and the checker's helpers are exercised by its self-test (7 arms).
lane: the <paths> block IS the grant.
</preflight>
