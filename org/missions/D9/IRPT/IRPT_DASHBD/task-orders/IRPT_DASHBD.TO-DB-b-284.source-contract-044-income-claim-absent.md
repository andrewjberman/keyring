# TO IRPT_DASHBD.TO-DB-b-284 -- the SOURCE TABLE contract 0.4.4 (round 148): a new OPTIONAL column `income_claim` = `absent` with the fixed reason SOURCE_REPORTS_NO_INCOME, required exactly where income_received is null for the Black Diamond-computed source; schema_hash unchanged, schema_hash_with_optional recomputed

<to_id>IRPT_DASHBD.TO-DB-b-284</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~228</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>148</round>
<workstream>CONTRACT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CONTRACT, round 148 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_147_20261016.md @026e67f3a7 (msg 9060) ("In contract 0.4.4, add income_claim absent with reason SOURCE_REPORTS_NO_INCOME, carried through to the series. You own S104.") | **Decomp cell:** `DB-b-284` (decomposition section 147).

**Risk class LOCAL**: one JSON standard, one new test file and at most fourteen changed lines across the four earlier contract tests; no AWS, no deploy, no push. Nothing writes or reads the new column yet: the producer cell that writes it, and the publisher that carries it, are later cells.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~06:0xZ, on worker rows IRPT_DASHBD-D2-W228-S1, S2 and S3; gate limb: an existing order modified, placeholders NONE unchanged, no criterion id, cell or path change):** the three rows are one DEFECT OF THE ISSUER'S DESIGN, ruled here: a seventh entry in `optional_columns` moves `schema_hash_with_optional`, which the Inflection adapter's pinned tests (outside your grant) and the 041/042 `_required` helpers read as the whole of the optional set; and no emitter writes all seven (the claim is emitted by one SOURCE). **Step 2 is REPLACED:** `optional_columns` stays BYTE-IDENTICAL, `schema_hash` AND `schema_hash_with_optional` stay UNCHANGED (revert your edit to them), and the new column goes in a NEW top-level section `conditional_columns` (a list of exactly ONE entry) with the keys `name` (income_claim), `type` (string), `nullable` (true), `meaning`, `values` (["absent"]), `reason` ("SOURCE_REPORTS_NO_INCOME"), `emitted_when` ({"source": "computed from Black Diamond values and flows"}), `required_when` ({"source": "computed from Black Diamond values and flows", "income_received": null}: the whole condition as ONE dict of equalities, a JSON null for the null income, so a generic reader that tests every key of `required_when` against the row reads it right), `rule` (words as before, and ALSO saying why it sits outside `optional_columns`: one source emits it, so it is outside the hash basis) and `since_schema_version` ("1.5"). `supersedes` still gains the 0.4.3 entry (both hashes are the unchanged ones), `rule24_record` still gains `v044`. **The facts record's `hashes` block** is now exactly {"schema_hash_unchanged": true, "schema_hash_with_optional_unchanged": true}; `new_column`, `census`, `tests` and `words` as before (the census stands). **The earlier tests:** keep ONLY the pinned-version lines you changed in 042 and 043; revert any other edit; the 041/042 `_required` helpers and the Inflection tests must pass UNEDITED because nothing they read has moved. The checker `p152_contract044.py` is updated (in your tree via the carry commit): read `check_diff` again. Your tests for the rule now read the `conditional_columns` entry.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-228` (branch `wk-IRPT_DASHBD-228`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~228/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~228/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Under "a value must carry its claim", the Cottonwood rows' null `income_received` (52,468 of 52,468 rows, row S104) cannot be told from a failed read: the contract (0.4.3) makes the null legal but states no claim. The CTO rules that the row gains `income_claim` = `absent` with the fixed reason `SOURCE_REPORTS_NO_INCOME`, the same way Orion's rows carry `flow_claim`. This order edits the CONTRACT only.

**The cell (`DB-b-284`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p152_contract044.py` (your three criteria; `check_diff` is the exact spec of what may differ from the base, and `claim_required` / `row_ok` are the behavioural spec); `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (0.4.3) and in particular its `flow_claim` optional column (the model for the new one) and its `rule24_record`; the four earlier tests `test_account_return_contract_040.py` to `_043.py` under `data/assets/scripts/gold/irpt_reporting/tests/`.
2. **The contract (edit the one JSON file; ONE commit with the test of step 3).** `contract_version` becomes `0.4.4`. `optional_columns` keeps every entry byte-identical and gains ONE at the end: `{"name": "income_claim", "type": "string", "nullable": true, "meaning": <words: the reason an account-day carries no income: the method states none (the Black Diamond-computed method separates no income; its income is inside the account value through cash)>, "values": ["absent"], "reason": "SOURCE_REPORTS_NO_INCOME", "required_when": {"source": "computed from Black Diamond values and flows"}, "required_when_null": "income_received", "rule": <words, containing: required exactly when income_received is null and the source is 'computed from Black Diamond values and flows'; a row carrying the claim with an income is invalid; a consumer that needs income rejects a row carrying this claim and says so in words; it never treats the null as zero>, "since_schema_version": "1.5"}`. `columns` (the 19) and `schema_hash` stay byte-identical; `schema_hash_with_optional` MOVES: it becomes the sha256 over the sorted `name:type` lines of the 19 columns plus all seven optional columns (the contract's own method; the 0.4.3 test shows it). `supersedes` keeps every entry and gains ONE at the end: `{"contract_version": "0.4.3", "schema_hash": <the unchanged schema_hash>, "schema_hash_with_optional": <the 0.4.3 value, from `git show` of the base>, "changes": <one sentence>}`. `rule24_record` keeps every key and gains ONE, `v044`: one paragraph of words that names `income_claim`, `income_received` and the reason code, and says that the claim has ONE value and NO OTHER STATE (a row either carries `absent` or carries no claim; there is no 'present' value, because a number is its own claim). Every other section stays byte-identical. No adapter, producer, publisher or portal file is edited.
3. **The test** `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_044.py`, at least eight passing tests driven only by the contract's declarations: the version; the new column's exact declaration; `schema_hash` unchanged and recomputed; `schema_hash_with_optional` recomputed over all seven optional columns and different from 0.4.3's; the rule: a Black Diamond-computed row with a null income must carry the claim, with an income must not, an Orion row (covered by its flow claim) and a holdings row must not carry it, a value other than `absent` is invalid; the supersedes entry; the `v044` words. No real account or client value.
4. **The earlier four tests** may need a minimal edit if one pins `contract_version` to 0.4.3 or the optional list or a hash: change ONLY what the 0.4.4 edit forces, at most 14 lines in all across the four files, each commented with this order's id. Any other failure of an earlier test is a BLOCKING row and you stop.
5. **Facts record** `RD_CONTRACT_044_FACTS_R148.json` in your folder with EXACTLY these fields: `contract_version` ("0.4.4"); `base_sha256` (the sha256 of the 0.4.3 file's bytes at your base, from `git show`); `new_column` ({"name": "income_claim", "values": ["absent"], "reason": "SOURCE_REPORTS_NO_INCOME"}); `hashes` ({"schema_hash_unchanged": true, "schema_hash_with_optional": <the new value>}); `census` ({"method": <words including the phrase `git grep -l -w`>, "counts": {"SOURCE_REPORTS_NO_INCOME": n, "income_claim": n}}: the number of FILES that `git grep -l -w -e <token> <your base commit>` finds, run by you at your base commit, for each of the two tokens); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed, that `schema_hash` is unchanged and `schema_hash_with_optional` moved, and what is NOT proven: that any producer writes the column, which is a later cell, and that any reader treats it correctly).

<criterion id="DB152-1-AC1" cell_refs="DB-b-284"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p152_contract044.py" . DB152-1-AC1</invocation><expect>DB152-1-AC1 PASS</expect></criterion>
`DB152-1-AC1` -- the contract differs from the base ONLY in `contract_version`, one appended `supersedes` entry, one added `rule24_record` key (`v044`), one appended optional column `income_claim` with the declaration above and the recomputed `schema_hash_with_optional`; `schema_hash` and every column, enum and other section are byte-identical.
<criterion id="DB152-1-AC2" cell_refs="DB-b-284"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p152_contract044.py" . DB152-1-AC2</invocation><expect>DB152-1-AC2 PASS</expect></criterion>
`DB152-1-AC2` -- a reference rule driven only by the contract's declarations accepts five rows (a BD null income with the claim, a BD income without it, income 0.0 without it, an Orion null income covered by its flow claim, a holdings income) and refuses six (a BD null income without the claim, a BD income with it, Orion with it, holdings with it, a value outside the column's values, income 0.0 with it).
<criterion id="DB152-1-AC3" cell_refs="DB-b-284"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p152_contract044.py" . DB152-1-AC3</invocation><expect>DB152-1-AC3 PASS</expect></criterion>
`DB152-1-AC3` -- your new test file holds at least eight passing tests, the four earlier contract test files pass with at most fourteen changed lines, the worker's commits change only the contract, the five test files, the folder, the investigation file and task-order files, and the facts record equals the contract and the census recounted by the checker.

<expected_criteria>DB152-1-AC1,DB152-1-AC2,DB152-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the adapter, the producers, the publisher, the series contract, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W228-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_044.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_041.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_042.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_043.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~228/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-284.source-contract-044-income-claim-absent.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 147 (round 148, workstream CONTRACT), cell `DB-b-284`.
<owned_cells>DB-b-284</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB152-1-AC1, DB152-1-AC2, DB152-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~228/IRPT_DASHBD.TO-DB-b-284.source-contract-044-income-claim-absent.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB152-1-AC1,DB152-1-AC2,DB152-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed keys in one line; the test counts and the number of earlier-test lines changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a JSON standard and test files in a branch; nothing writes or reads the new column.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its diff, behaviour, grant and facts clauses were validated by the issuer against a reference 0.4.4 built from the real 0.4.3 contract (green) and 17 single-fault arms (all red) by the self-test.
lane: the <paths> block IS the grant.
</preflight>
