# TO MDPF_DEMQUE.TO-DQ-t53 -- round 9 DQ-t-53: C-DEMQUE-SECCLASS-SYNC, DEMQUE's half -- one security's key printed equal on the request row, the unresolved entry and the classification row
<to_id>MDPF_DEMQUE.TO-DQ-t53</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~45</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SECCLASSSYNC</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-53` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 17) |
**outcome_ref:** C-IDENTITY, C-DEMQUE-SECCLASS-SYNC, FWD-5 | **depends_on:** none (read only)

---

## WORKER FACE

### THE CELL

The contract row `C-DEMQUE-SECCLASS-SYNC` in [MDPF_DEMQUE_PRD.md](file:///C:/dev/ajb_workspace/org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md) (repo-relative
`org/missions/D8/MDPF/MDPF_DEMQUE/prd/MDPF_DEMQUE_PRD.md`, the ADDENDUM at line 285; read it) says a security entering through any DEMQUE request carries ONE identity key, the same
key its unresolved list uses, and MDPF_SECCLASS's scheduled path writes its row in DynamoDB `etf-classifications`. **DEMQUE never classifies. DEMQUE's proof cell:** the same security's
key printed EQUAL on the queue's request row, its unresolved-list entry (or "resolved") and the classification row; and a negative arm: a security already classified entering through a
second request gets no second row. **This cell is a read-only proof. It writes nothing anywhere and makes no vendor call.**

Facts the issuer already measured (use them, do not redo): the table `etf-classifications` has ONE hash key, `ticker` (string), 11,361 items, a row carries `asset_class`,
`sub_asset_class`, `sector`, `management_style`, `name`, `last_updated`; one named-resource read works with the dell1 identity (`.tools/aws dynamodb get-item`). DEMQUE's
request rows carry `cusip` and a Yahoo `symbol`; the unresolved list (`~/.opal/demque/unresolved.csv`) carries `cusip` and `symbol`. So the "one key" a human reads across the three places is
the SYMBOL STRING; the CUSIP is DEMQUE's own identity and the symbol is the join. State this in the docstring and in the report.

**Build** (NEW `data/mdpf/scripts/demque/secclass_sync.py`; use `boto3` get_item for the table, `price_store.index` for landed names, the request files and the device queue
`~/.opal/demque/queue/*.json` for request rows; import, do not copy):
1. **`--prove`** (read only; ONE `get_item`, no `scan` of more than the candidate loop below): choose ONE real security deterministically: iterate the landed names of the price index in
   CUSIP order and take the FIRST whose `yahoo_symbol` has a row in `etf-classifications` (get_item per candidate, at most 60 calls). Print ONE JSON line:
   `{"security": {"cusip", "symbol"}, "request_row": {"file", "key"}, "unresolved": {"state": "resolved" | "listed", "key"}, "classification_row": {"table": "etf-classifications",
   "key", "present": true}, "equal": true|false, "negative_arm": {"second_request_rows", "classification_rows_for_key"}}`.
   - `request_row.key` = the `symbol` on the first request or queue row that carries the CUSIP (its file named); `unresolved` = `listed` with that row's `symbol` when the CUSIP is on
     the unresolved list, else `resolved`; `classification_row.key` = the table's `ticker`; `equal` = every key printed is the same string, case exactly as stored.
   - **Negative arm:** build, IN MEMORY, a second request row for the same CUSIP (never written), report `second_request_rows` 1, and read the table again for that key
     (`get_item`, plus a `query`-free check that the table has no second row: the key is the hash key, so `classification_rows_for_key` is 1 by construction, and the report says
     so and prints the item's `last_updated` unchanged between the two reads).
2. **`--coverage`** (read only, bounded): of the landed names whose Asset_Type is an ETF or fund type (from `lock.json`'s class where present), how many have a classification row
   (batch `get_item` through `batch_get_item`, at most 100 keys a call, at most 400 names), printed as `{"checked", "classified", "missing_examples": [up to 5 CUSIPs]}`. State in the report
   that this is the gap the classification path owns, not DEMQUE.
3. NEW `test_demque_secclass_sync.py` (pytest; a stub DynamoDB client and stub frames, no network) with exactly these names:
   `test_the_same_security_key_prints_equal_on_the_request_row_the_unresolved_entry_and_the_classification_row`,
   `test_a_security_already_classified_that_enters_through_a_second_request_gets_no_second_row`,
   `test_a_key_that_differs_between_the_three_places_is_reported_unequal_never_equal`.

### ACCEPTANCE

<criterion id="DQ9-t53-AC1" cell_refs="DQ-t-53"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t53_tests.py</invocation><expect>SYNC-OK</expect></criterion>
<criterion id="DQ9-t53-AC2" cell_refs="DQ-t-53"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t53_real.py</invocation><expect>SYNC-REAL-OK</expect></criterion>
`DQ9-t53-AC1` -- the three named tests. `DQ9-t53-AC2` -- on the REAL index, request files, unresolved list and the live table: one security's key printed equal across the three places, the
classification row present in `etf-classifications`, one row for the key. Report the whole folder `pytest data/mdpf/scripts/demque` once, and the `--coverage` line.

<expected_criteria>DQ9-t53-AC1,DQ9-t53-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `SYNC-BAD no file ...`; `SYNC-REAL-BAD no file ...secclass_sync.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **READ-ONLY: NO write to DynamoDB, S3, the ledger, the queue or any pacer state; NO Yahoo or Bloomberg call; no AWS write; no deploy; no timer.** The only DynamoDB calls are
  `get_item` and `batch_get_item` on `etf-classifications`; never `put_item`, `update_item`, `delete_item` or `scan`.
- **Account ids never enter a committed file.**
- **Refusal clause.** If a criterion cannot be met as written (for example no landed name has a classification row, or the read is refused), stop, write the reason in your report and a
  surprise row (id `MDPF_DEMQUE-D1-W45-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation file below, and do not weaken a
  check. Rows are APPEND-ONLY. Merge `box/dell1` into your branch (a merge, never a rebase) before you append rows.

<paths>
data/mdpf/scripts/demque/secclass_sync.py
data/mdpf/scripts/demque/test_demque_secclass_sync.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-53`.
<owned_cells>DQ-t-53</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t53-AC1, DQ9-t53-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~45/MDPF_DEMQUE.TO-DQ-t53.secclass-sync-key-proof.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t53-AC1,DQ9-t53-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--prove` line verbatim, the `--coverage` line, how the key is stated (symbol versus CUSIP), the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE two read calls on one DynamoDB table with the dell1 identity; no grant is requested or changed.
comp-adversary: DECLARED-NOT-APPLICABLE a read-only proof; DEMQUE never classifies and never writes the table.
risk: LOCAL -- code, tests and a printed proof.
direct_act: false -- a worker order.
</preflight>

Source: MDPF_DEMQUE PRD ADDENDUM (C-DEMQUE-SECCLASS-SYNC); CTO msg 5025; pivot packet O7; decomposition round 9.
