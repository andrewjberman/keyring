# TO IRPT_DASHBD.TO-DB-b-270 -- the account_return_daily CONTRACT 0.4.0 (round 137): external_flow and income_received nullable ONLY where source is orion and the row says so (flow_claim), Orion's integer account id in an optional column, the 19 columns and their hash unmoved

<to_id>IRPT_DASHBD.TO-DB-b-270</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~219</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>137</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F + contract, round 137 | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 8546, CTO ROUND ANALYSIS IRPT_DASHBD B-IN ROUND 118 ADDENDUM 4 @10e1032651 (on 2.0.0_SA_COO~I2 msg 8543) | **Decomp cell:** `DB-b-270` (decomposition section 135).

**Risk class LOCAL**: one JSON standard and one test file in the repo; no AWS, no Terraform, no deploy. The change is a shared standard and the CVO grades it at L9 (not the CTO, who ruled it, and not you).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-219` (branch `wk-IRPT_DASHBD-219`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~219/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~219/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The Scope (Orion) feed carries a vendor-reported return and no flows. Contract 0.3.0 (`org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`) makes `external_flow` and `income_received` non-nullable. The CTO rules: they become nullable ONLY where `source == "orion"`, beside a claim field `flow_claim: absent` with the reason "vendor-reported return, not built from flows"; a consumer that needs flows rejects on that claim and says so in words, and never treats a null as 0; every 0.3.0 writer still validates, because no existing type changes.

**The cell (`DB-b-270`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_contract040.py` (your three criteria; its constants and its reference validator `row_problems` are the behavioural spec); the current contract file; the earlier minor bump that added `source` (task order `org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-240.account-return-contract-030-the-optional-source-column.md`, its facts record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~194/RD_SOURCE_COLUMN_R120.json`); the two earlier tests that read the contract, `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py` and `test_cottonwood_report_reader.py`.
2. **The contract (edit the one JSON file, ONE commit with the test of step 3).** Set `contract_version` to `0.4.0`. The 19 `columns` keep every name, type and `meaning`, and keep `nullable` as it is: the two flow columns stay `"nullable": false` (nullability is conditional, never general) and each gains the key `"nullable_when": {"source": "orion", "flow_claim": "absent"}`; the other 17 columns are byte-identical; `schema_hash` is unchanged. `optional_columns` becomes exactly `source` (unchanged, byte-identical), then `flow_claim`, then `source_account_id`. `flow_claim`: `type` string, `nullable` true, `values` `["absent"]`, `reason` exactly "vendor-reported return, not built from flows", `meaning`, `since_schema_version` "1.2", and a `rule` that says in words: required exactly when `external_flow` or `income_received` is null; only where source is orion; a consumer that needs flows rejects it and states that in words; a null flow is never treated as zero. `source_account_id`: `type` int64, `nullable` true, a `meaning` naming Orion's integer account id, `since_schema_version` "1.2", a `rule` (null for every non-Orion source). Recompute `schema_hash_with_optional` over the 19 columns plus `source:string`, `flow_claim:string`, `source_account_id:int64` (the method of `schema_hash_basis`). `supersedes` gains the 0.3.0 entry: `contract_version` "0.3.0", its `schema_hash` and its `schema_hash_with_optional` (the contract's own previous value, read from the file at your base), and `changes` in words. Add a top-level `source_rules` with one key `orion` holding exactly `flows`, `business_date` and `account_id`, each in words: `flows` names `flow_claim` and says a null is never zero; `business_date` says it stays the TRADING day, each non-trading calendar day's factor compounds (the product) into the next trading day's factor and the manifest states that, and a trading day whose own factor is ABSENT stays ABSENT; `account_id` says the custodian form is mapped through `account_dim`, Orion's id is kept in `source_account_id`, and an Orion account with no mapping is an ABSENT row with reason class `UNMAPPED_ACCOUNT`, never dropped, its count in the run record. `served_day_rules` stays byte-identical. Change nothing else in the file; no producer, adapter or handler is edited here (the Orion adapter is a later cell of another seat).
3. **The test** `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py`, with at least six tests that pass under pytest from the repo root, driven only by the contract file's declarations (read `nullable_when` generically; never hard-code which column may be null): a 0.3.0 Black Diamond row (flows set, no claim) validates; a row whose `source` is null and flows are set validates; an Orion row with both flows null and `flow_claim` "absent" validates; an Orion row with null flows and no claim is rejected; a non-Orion row (a Black Diamond source or a null source) with null flows and the claim is rejected; a row with the claim and no null flow is rejected; a claim outside its `values` is rejected; and the `schema_hash` equals its 0.3.0 value and `schema_hash_with_optional` equals the recomputed one. The test file defines its own small validator over a dict row and names no real account or client value.
4. **Facts record** `RD_CONTRACT_040_FACTS_R137.json` in your folder with EXACTLY these fields: `contract_version` ("0.4.0"); `schema_hash` and `hash_with_optional` (equal to the contract's `schema_hash` and `schema_hash_with_optional`); `optional_columns` (["source", "flow_claim", "source_account_id"]); `nullable_only_for` (the `nullable_when` object); `words` (one paragraph, 80 to 1800 characters: what changed, what did not move, that every 0.3.0 writer still validates, and what is NOT proven: that the Orion adapter emits rows this way, which is its own cell).

<criterion id="DB137-2-AC1" cell_refs="DB-b-270"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_contract040.py" . DB137-2-AC1</invocation><expect>DB137-2-AC1 PASS</expect></criterion>
`DB137-2-AC1` -- the contract file holds every declaration of step 2 (version, the 19 columns and hash unmoved, the 17 others byte-identical, `nullable_when` on the two flow columns, the three optional columns, the recomputed hash, the 0.3.0 supersedes entry, `served_day_rules` unmoved, `source_rules.orion`), and the worker's commits change only the contract, its test, its folder, the investigation file and task-order files, the contract and the test together in ONE commit.
<criterion id="DB137-2-AC2" cell_refs="DB-b-270"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_contract040.py" . DB137-2-AC2</invocation><expect>DB137-2-AC2 PASS</expect></criterion>
`DB137-2-AC2` -- a reference validator driven only by the contract's declarations accepts the 0.3.0 rows and the claimed Orion row and rejects: Orion null flows without the claim, a non-Orion row with null flows and the claim, a null-source row with null flows and the claim, an Orion row with flows set and the claim, a claim outside its values, and an Orion row with another null column.
<criterion id="DB137-2-AC3" cell_refs="DB-b-270"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r137/p137_contract040.py" . DB137-2-AC3</invocation><expect>DB137-2-AC3 PASS</expect></criterion>
`DB137-2-AC3` -- your test file holds at least six passing tests, the two earlier contract-reading test files still pass, and the facts record equals the contract.

<expected_criteria>DB137-2-AC1,DB137-2-AC2,DB137-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer, the adapters, the handler, `filled_report_values.py`, the report contract, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If an earlier contract-reading test fails once the contract reads 0.4.0 and the cause is a hard-coded `0.3.0` in that test, record it as a BLOCKING row and stop: those test files are not in your grant.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W219-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

## AMENDMENT 1 (2026-10-15 ~19:0xZ, 2.0.0_SA_COO~D2, on row IRPT_DASHBD-D2-W219-S1): ONE assertion of an earlier test moves with the contract

Contract 0.4.0 moves the top-level `schema_hash_with_optional` (the 0.3.0 value is in the contract's `supersedes` entry for 0.3.0). The Cottonwood adapter stays a 0.3.0 writer (its constant `CONTRACT_VERSION` is "0.3.0" and it emits the 20-field table with `source` only), so its hash is the 0.3.0 value, not the contract's new top-level one. **The grant gains** `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py`. **Do exactly this and nothing else in that file:** in `test_the_two_hashes_equal_the_contract_and_match_a_recomputation`, replace the line asserting `m.schema_hash_with_optional() == contract["schema_hash_with_optional"]` with an assertion that it equals the `schema_hash_with_optional` of the entry of `contract["supersedes"]` whose `contract_version` is "0.3.0" (a one-line comment may say why). The file may change by at most 8 lines in all (`DB137-2-AC1` measures it). Add the file to your commit; the 52 earlier tests then all pass (`DB137-2-AC3`). Gate limb that graded this amendment: none (the order carries no `<placeholders>`; a grant path and a criterion bound were added to an order already complete in its other parts); the CTO reads it at the round-N analysis.

<paths>
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~219/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-270.account-return-contract-040-flows-nullable-for-orion-and-source-account-id.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 135 (round 137, workstream B-49F), cell `DB-b-270`.
<owned_cells>DB-b-270</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB137-2-AC1, DB137-2-AC2, DB137-2-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~219/IRPT_DASHBD.TO-DB-b-270.account-return-contract-040-flows-nullable-for-orion-and-source-account-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB137-2-AC1,DB137-2-AC2,DB137-2-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the contract's changed keys in one line; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a JSON standard and a test file in a branch; nothing reads the new columns yet and no emitter changes.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were validated by the issuer against a scratch reference contract (green) and 15 single-fault mutants of it (all red), and its behaviour, grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
