# TO IRPT_DASHBD.TO-DB-b-282 -- the SOURCE TABLE contract 0.4.3 (round 147): `income_received` may be null where the row's `source` is 'computed from Black Diamond values and flows', one declared attribute on one column; both schema hashes and everything else byte-identical

<to_id>IRPT_DASHBD.TO-DB-b-282</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~227</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>147</round>
<workstream>CONTRACT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CONTRACT, round 147 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md ADDENDUM v0.16 item 4 and the CTO boundary ruling msg 8803 ("~D2 owns handler.py, publisher.py, the publish tf root and the sources entry. The first Cottonwood series publish is ~D2's cell, under its own pair and in one drain with the contract field.") | **Decomp cell:** `DB-b-282` (decomposition section 145).

**Risk class LOCAL**: one JSON standard, one new test file and at most fourteen changed lines across the three earlier contract tests; no AWS, no deploy, no push. Nothing reads the new attribute yet: it only makes a declared fact (the Black Diamond-computed method states no income) true in the contract.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-227` (branch `wk-IRPT_DASHBD-227`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~227/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~227/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The source table contract declares `income_received` non-nullable except for source `orion` with `flow_claim` `absent`. The Cottonwood gold table (source `computed from Black Diamond values and flows`) carries `income_received` null on 52,468 of 52,468 rows from its floor day, because that method separates no income (its adapter says so). The table contradicts its contract (row IRPT_DASHBD-D2-S104). The series contract 0.3.0 already makes the series `income` array number-or-null; this edit makes the source contract say the same, so the null is declared and not an accident.

**The cell (`DB-b-282`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p150_contract043.py` (your three criteria; its `check_diff` is the exact spec of what may differ from the base); `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (0.4.2); the three earlier tests `test_account_return_contract_040.py`, `_041.py`, `_042.py` under `data/assets/scripts/gold/irpt_reporting/tests/`; `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (header lines on income; read only).
2. **The contract (edit the one JSON file; ONE commit with the test of step 3).** `contract_version` becomes `0.4.3`. In `columns`, the `income_received` entry gains ONE new key, `also_nullable_when`, with the value `[{"source": "computed from Black Diamond values and flows"}]`; its other keys stay byte-identical and no other column changes. `supersedes` keeps every entry byte-identical and gains ONE at the end: `{"contract_version": "0.4.2", "schema_hash": <the contract's current schema_hash>, "schema_hash_with_optional": <the contract's current schema_hash_with_optional>, "changes": <one sentence: income_received became nullable for the Black Diamond-computed source, declared by also_nullable_when>}`. `schema_hash` and `schema_hash_with_optional` DO NOT CHANGE (the new key is not among the hashed fields; confirm by recomputing with the contract's own method as the earlier tests do). `rule24_record` keeps every earlier key and gains ONE key, `v043`, one paragraph of words that names `income_received`, the source value `computed from Black Diamond values and flows`, and says that no enum member is added (so the word-boundary census of the earlier records is untouched). Every other section stays byte-identical. No adapter, producer, publisher or portal file is edited.
3. **The test** `data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_043.py`, at least eight passing tests driven only by the contract's declarations: the version, the attribute's exact value, both hashes equal to the 0.4.2 values and to a recomputation, a null income allowed for a Black Diamond-computed row and for an Orion row with the claim, refused for a holdings-sourced row, an Orion row without the claim, a row with no source and one with a null source, and the supersedes entry. No real account or client value.
4. **The earlier three tests** may need a minimal edit if one pins `contract_version` to 0.4.2 or a section's bytes: change ONLY what the 0.4.3 edit forces, at most 14 lines in all across the three files, each edit commented with this order's id. If an earlier test fails for any other reason, file a BLOCKING row and stop.
5. **Facts record** `RD_CONTRACT_043_FACTS_R147.json` in your folder with EXACTLY these fields: `contract_version` ("0.4.3"); `base_sha256` (the sha256 of the 0.4.2 file's bytes at your base commit, from `git show`); `also_nullable_when` (equal to the column's value); `hashes_unchanged` (true); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed, that both schema hashes are unchanged, and what is NOT proven: that any producer writes or any reader treats the null correctly beyond the Cottonwood adapter that already writes it).

<criterion id="DB150-1-AC1" cell_refs="DB-b-282"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p150_contract043.py" . DB150-1-AC1</invocation><expect>DB150-1-AC1 PASS</expect></criterion>
`DB150-1-AC1` -- the contract differs from the base ONLY in `contract_version`, one appended `supersedes` entry, one added `rule24_record` key (`v043`) and `income_received.also_nullable_when`; both schema hashes and every other column, enum and section are byte-identical.
<criterion id="DB150-1-AC2" cell_refs="DB-b-282"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p150_contract043.py" . DB150-1-AC2</invocation><expect>DB150-1-AC2 PASS</expect></criterion>
`DB150-1-AC2` -- a reference rule driven only by the contract's declarations allows a null income on five rows (Black Diamond-computed and Orion with the claim) and refuses it on five (holdings, Orion without the claim, no source, null source, a near-miss source).
<criterion id="DB150-1-AC3" cell_refs="DB-b-282"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p150_contract043.py" . DB150-1-AC3</invocation><expect>DB150-1-AC3 PASS</expect></criterion>
`DB150-1-AC3` -- your new test file holds at least eight passing tests, the three earlier contract test files pass with at most fourteen changed lines, the worker's commits change only the contract, the four test files, the folder, the investigation file and task-order files, and the facts record equals the contract.

<expected_criteria>DB150-1-AC1,DB150-1-AC2,DB150-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the adapter, the producers, the publisher, the series contract, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W227-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_043.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_041.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_042.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~227/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-282.source-contract-043-income-null-for-bd-computed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 145 (round 147, workstream B-49F + contract), cell `DB-b-282`.
<owned_cells>DB-b-282</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB150-1-AC1, DB150-1-AC2, DB150-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~227/IRPT_DASHBD.TO-DB-b-282.source-contract-043-income-null-for-bd-computed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB150-1-AC1,DB150-1-AC2,DB150-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed keys in one line; the test counts and the number of earlier-test lines changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a JSON standard and test files in a branch; nothing reads the new attribute and no writer changes.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its diff, behaviour, grant and facts clauses were validated by the issuer against a reference 0.4.3 built from the real 0.4.2 contract (green) and 12 single-fault arms (all red) by the self-test.
lane: the <paths> block IS the grant.
</preflight>
