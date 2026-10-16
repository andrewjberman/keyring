# TO IRPT_DASHBD.TO-DB-b-293 -- the HISTORY-SCOPE CLAIM in both contracts (round 149, CTO ruling msg 9226): the source table contract 0.4.6 gains the conditional column `history_scope_claim` (inferred), the series contract 0.3.3 gains the pair `history_scope_claim` + `history_scope_basis` and `history_scope_rule`, and its unreported-days rule is widened to every firm (CTO ruling msg 9224); both schema hashes unchanged

<to_id>IRPT_DASHBD.TO-DB-b-293</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~236</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>HISTSCOPE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** HISTSCOPE, round 149 | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 9226 (row D2-S113: "history_scope is DERIVED per account, never a constant ... an account whose first value day equals the source floor is PARTIAL, because it existed before our data starts; an account first seen after the floor is FULL, because we hold its whole history in this source; carry history_scope_claim = inferred, with the method 'first value day vs source floor'") and msg 9224 (the 49 Financial series state their unreported days) | **Decomp cell:** `DB-b-293` (decomposition section 153).

**Risk class LOCAL**: two JSON standards, one new test file and at most 60 changed lines (additions plus deletions) across the earlier contract tests; no AWS, no deploy, no push. Nothing writes or reads the new column or the new fields yet: the producer cell and the publisher cell that write them are the next cells, landed in the SAME drain.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~10:0xZ, on worker row IRPT_DASHBD-D2-W236-S1; gate limb: GATE (viii), an existing order modified with placeholders NONE unchanged; no criterion id, cell or path change):** the ceiling of 28 earlier-test lines was the issuer's guess from the last contract round and is WRONG for this one: the forced pinned-version edits across six earlier files measured 42 lines by `git diff --numstat` (additions plus deletions), all of them version pins. The ceiling is now 60 (the checker `p161_histscope_contracts.py` is updated via the carry commit); the rule that only what the edit forces may change stands, and any other failure of an earlier test is still a BLOCKING row. Row S2 (`_declared` needs a by-name exclusion) is ruled: that is a forced edit and is inside the 60. Re-run AC3, then finish the record, the proof instance and the flip.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-236` (branch `wk-IRPT_DASHBD-236`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~236/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~236/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** `account_return_daily.py` writes `history_scope` = `PARTIAL_HISTORY` on every row; the CTO ruled that a defect. The producer will derive it per account (the next cell): PARTIAL_HISTORY when the account's first value day equals the source floor (the earliest balance partition the source holds), FULL when it is after. A derived value that is not measured must carry its claim in a field a consumer can reject on: `history_scope_claim` = `inferred`, method `first value day vs source floor`. This order edits the CONTRACTS only. It also widens the series contract's unreported-days rule: the publisher now derives the pair from the gold partitions present for EVERY firm (an explicit `[]` where none is missing), where the rule's text said only a source carrying the report-build statement has it.

**The cell (`DB-b-293`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p161_histscope_contracts.py` (your three criteria; `check_source` and `check_series` are the exact spec of what may differ from the base and of the required words, `check_behaviour` is the behavioural spec); `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (0.4.5): its `conditional_columns` entry `income_claim` (the model), `rule24_record` and `supersedes`; `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (0.3.2): `series.optional`, the fields `income_claim`, `unreported_trading_days`, `unreported_trading_days_basis` (the model for a const text field) and `history_scope`, and the rules `unreported_days_rule` and `income_claim_rule`; the earlier contract tests under `data/assets/scripts/gold/irpt_reporting/tests/` (`test_account_return_contract_040.py` to `_044.py`, `test_income_reason_rename.py`, `test_series_contract_030.py`, `_031.py`).
2. **The SOURCE contract (edit the one JSON file; ONE commit with the test of step 4).** `contract_version` becomes `0.4.6`. `conditional_columns` keeps its entry `income_claim` byte for byte and gains ONE entry at the end with EXACTLY the keys `name` (`history_scope_claim`), `type` (`string`), `nullable` (false), `meaning` (words), `values` (`["inferred"]`), `method` (`first value day vs source floor`), `applies_to` (words: every row written by a producer that derives history_scope per account), `rule` and `since_schema_version` (`1.6`). The `rule` is words containing, at least: `history_scope`, `PARTIAL_HISTORY`, `FULL`, `first value day`, `source floor`, `earliest balance partition`, `inferred`, `optional_columns` (why the column sits outside it: it is not in the hash basis), `never` (the claim is inferred and never measured) and `no claim` (a row without the column makes no claim: a partition written before the derivation). The `meaning` contains `history_scope`, `inferred` and `account`. `supersedes` keeps every entry and gains ONE at the end: `{"contract_version": "0.4.5", "schema_hash": <the unchanged value>, "schema_hash_with_optional": <the unchanged value>, "changes": <one sentence naming history_scope_claim>}`. `rule24_record` keeps every key and gains ONE, `v046`: one paragraph naming `history_scope_claim`, its ONE value `inferred` and `no other state`, the method `first value day vs source floor`, and that it is an `account` property sharing history_scope's grain exception. EVERY other key (`columns`, `optional_columns`, `enums`, both schema hashes, the source and served-day rules, the producer pin) stays byte for byte; `schema_hash` AND `schema_hash_with_optional` stay UNCHANGED.
3. **The SERIES contract (edit the one JSON file, in the same commit).** `contract_version` becomes `0.3.3`. `lineage` keeps every entry and gains ONE: `{"contract_version": "0.3.2", "sha256": <the sha256 hex of the 0.3.2 file's bytes at your base, from `git show`>, "note": <words>}` (exactly those three keys). `series.optional` keeps its entries and appends `history_scope_claim` then `history_scope_basis`. `series.fields` gains exactly two entries: `history_scope_claim` with EXACTLY the keys `kind` ("scalar string"), `source` (words naming the source table contract's `history_scope_claim` column), `fixed_value` ("inferred"), `sentence`; and `history_scope_basis` with EXACTLY `kind` ("scalar string"), `source` ("a fixed text"), `fixed_value` ("first value day vs source floor"), `const` (true), `rule24_note` (one value, no other state), `sentence` (the model is `unreported_trading_days_basis`). Two existing field entries change in ONE key each: `history_scope.sentence` (words containing `derived`, `account`, `PARTIAL_HISTORY`, `FULL`, `source floor` and `never null`) and `unreported_trading_days.source` (words naming the publisher's derivation from the `gold partitions` present and keeping the `report-build` equality). `unreported_days_rule` keeps every key; ONLY `present_when` changes, to words containing `every firm`, `gold partitions` and `[]` and dropping the clause "carries neither field". A NEW top-level `history_scope_rule` with EXACTLY the keys `present_when` (words), `pair` (words containing `both`, `neither` and `lone`: both fields or neither, a lone field is invalid), `value` ("inferred"), `basis` ("first value day vs source floor"), `derivation` (words containing `PARTIAL_HISTORY`, `FULL`, `first_data_date`, `source floor` and `earliest`) and `absent_means` (words: no statement is made about how history_scope was set; the value stays as the gold wrote it). EVERY other key and section stays byte for byte (the manifest included).
4. **The test** `data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_claim_contracts.py`, at least eight passing tests driven only by the contracts' declarations: both versions; the source column's exact declaration; both source hashes unchanged and recomputed from the columns; a row with the claim and a legal scope accepted, a legacy row without the claim accepted, a wrong or null claim refused; the series pair declared and both-or-neither enforced by a reference rule built from `history_scope_rule`; the basis const text; the widened unreported rule's words; `supersedes`, `lineage` and the `v046` words. No real account or client value.
5. **The earlier tests** may need a minimal edit if one pins `contract_version` to 0.4.5 or 0.3.2 or the optional list: change ONLY what the edit forces, at most 60 lines in all (additions plus deletions, as `git diff --numstat` counts them) across the eight earlier files, each commented with this order's id. Any other failure of an earlier test is a BLOCKING row and you stop.
6. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p161_histscope_contracts.py" . DB161-1-AC1`, then AC2, then AC3.
7. **Record** `RD_HISTSCOPE_CONTRACTS_FACTS_R149.json` in your folder with EXACTLY these fields: `source_version` ("0.4.6"); `series_version` ("0.3.3"); `base_sha256` ({"source": <sha256 hex of the 0.4.5 file's bytes at your base>, "series": <sha256 hex of the 0.3.2 file's bytes at your base>}); `hashes` ({"schema_hash_unchanged": true, "schema_hash_with_optional_unchanged": true}); `new_fields` ({"source": ["history_scope_claim"], "series": ["history_scope_claim", "history_scope_basis"]}); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed, that both source hashes are unchanged, and what is NOT proven: that any producer writes the column or any publisher writes the fields, which are the next cells, and that any reader treats them correctly).

<criterion id="DB161-1-AC1" cell_refs="DB-b-293"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p161_histscope_contracts.py" . DB161-1-AC1</invocation><expect>DB161-1-AC1 PASS</expect></criterion>
`DB161-1-AC1` -- each contract differs from its base ONLY in the allowed places: the source contract in `contract_version`, one appended `supersedes` entry, one added `rule24_record` key (`v046`) and one appended conditional column with the declaration above; the series contract in `contract_version`, one appended `lineage` entry, `series.optional`, the two new fields and the two reworded keys, `unreported_days_rule.present_when` and the new `history_scope_rule`; both schema hashes, `columns`, `optional_columns` and every other section byte-identical.
<criterion id="DB161-1-AC2" cell_refs="DB-b-293"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p161_histscope_contracts.py" . DB161-1-AC2</invocation><expect>DB161-1-AC2 PASS</expect></criterion>
`DB161-1-AC2` -- a reference rule driven only by the contracts' declarations accepts three source rows (a claim beside PARTIAL_HISTORY, a claim beside FULL, a legacy row without the claim) and two series (the pair, or neither) and refuses four source rows (a wrong claim value, a null claim, a scope outside the enum, a null scope) and four series (a lone claim, a lone basis, a wrong claim value, a free-text basis).
<criterion id="DB161-1-AC3" cell_refs="DB-b-293"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p161_histscope_contracts.py" . DB161-1-AC3</invocation><expect>DB161-1-AC3 PASS</expect></criterion>
`DB161-1-AC3` -- your new test file holds at least eight passing tests, the eight earlier contract test files pass with at most 60 changed lines, the worker's commits change only the two contracts, the nine test files, the folder, the investigation file and task-order files, and the facts record equals the checker's recount.

<expected_criteria>DB161-1-AC1,DB161-1-AC2,DB161-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the producer, the publisher, the handlers, the source map, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W236-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements). Write the JSON files with LF line endings.

<paths>
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_claim_contracts.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_041.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_042.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_043.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_044.py
data/assets/scripts/gold/irpt_reporting/tests/test_income_reason_rename.py
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_031.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~236/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-293.history-scope-claim-contracts-046-033.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 154 (round 149, workstream HISTSCOPE), cell `DB-b-293`.
<owned_cells>DB-b-293</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB161-1-AC1, DB161-1-AC2, DB161-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~236/IRPT_DASHBD.TO-DB-b-293.history-scope-claim-contracts-046-033.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB161-1-AC1,DB161-1-AC2,DB161-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed keys in one line per contract; the test counts and the number of earlier-test lines changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: two JSON standards and test files in a branch; nothing writes or reads the new column or fields yet.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (19 source, 22 series, 3 behaviour, 9 facts and 3 grant red arms); its diff and behaviour clauses were validated by the issuer against reference 0.4.6 and 0.3.3 contracts built from the real 0.4.5 and 0.3.2 files (green).
lane: the <paths> block IS the grant.
</preflight>
