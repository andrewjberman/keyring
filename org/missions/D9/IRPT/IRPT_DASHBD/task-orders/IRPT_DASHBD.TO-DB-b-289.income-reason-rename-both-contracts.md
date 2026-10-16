# TO IRPT_DASHBD.TO-DB-b-289 -- the RENAME of the income claim's reason in BOTH contracts (round 149): `SOURCE_REPORTS_NO_INCOME` is false (the source carries income; the Black Diamond-computed return method does not separate it), so it becomes `RETURN_METHOD_DOES_NOT_SEPARATE_INCOME`: source contract 0.4.5 and series contract 0.3.2; both schema hashes unchanged

<to_id>IRPT_DASHBD.TO-DB-b-289</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~233</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>CONTRACT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** CONTRACT, round 149 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUNDS_147P_148_20261016.md @5daaee121d (msg 9158, ruling B) ("The reason is renamed RETURN_METHOD_DOES_NOT_SEPARATE_INCOME, before any series carries it."; "landed in ONE drain with any further contract touch") | **Decomp cell:** `DB-b-289` (decomposition section 150).

**Risk class LOCAL**: two JSON standards, one new test file and a few pinned lines in the earlier contract tests; no AWS, no deploy, no push. This branch is HELD by the issuer and lands in ONE drain with the writer cell (`DB-b-287`): do not expect it to merge the moment you finish.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-233` (branch `wk-IRPT_DASHBD-233`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~233/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~233/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The CTO measured that Cottonwood's transaction silver carries non-zero Income on 343,256 of 1,096,830 rows. The claim's reason `SOURCE_REPORTS_NO_INCOME` therefore says something false: the SOURCE reports income; it is the Black Diamond-computed RETURN METHOD that does not separate it from the account value. No series carries the reason yet. Both contracts name it and both explain it in words that say "the source reports no income". Rename the code and correct the words in both, and nothing else.

**The cell (`DB-b-289`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p157_reasonrename.py` (your three criteria; `check_source` and `check_series` are the exact specs of what may differ from each base; `check_live` the words test); `org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json` (0.4.4: `conditional_columns[0]`, `rule24_record.v044`, `supersedes`) and `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (0.3.1: `series.fields.income_claim`, `income_claim_rule`, `lineage`); the earlier tests `test_account_return_contract_040.py` to `_044.py`, `test_series_contract_030.py` and `_031.py` under `data/assets/scripts/gold/irpt_reporting/tests/`.
2. **The SOURCE contract (0.4.4 -> 0.4.5), edit the one JSON file.** `contract_version` becomes `0.4.5`. In `conditional_columns[0]` ONLY `reason` becomes exactly `RETURN_METHOD_DOES_NOT_SEPARATE_INCOME`, `meaning` is rewritten to say that the source DOES carry income and the Black Diamond-computed RETURN METHOD does not separate it from the account value (the words contain `source`, `return method` and `separate`), and `rule` has the old code replaced by the new one and keeps every clause it has (`income_received`, the source value, `optional_columns`, never, zero, reject). `supersedes` keeps every entry and gains ONE at the end: `{"contract_version": "0.4.4", "schema_hash": <unchanged>, "schema_hash_with_optional": <unchanged>, "changes": <one sentence naming the new code>}`. `rule24_record` keeps every key and gains `v045`: one paragraph naming the new code and the old, the 343,256 rows, and that the claim still has ONE value and no other state. Every other key, `optional_columns` and BOTH schema hashes stay byte-identical. The old code stays ONLY in the historical `rule24_record.v044` and the earlier `supersedes` entries.
3. **The SERIES contract (0.3.1 -> 0.3.2), edit the one JSON file.** `contract_version` becomes `0.3.2`. `lineage` keeps every entry and gains ONE: `{"contract_version": "0.3.1", "sha256": <the sha256 of the 0.3.1 file's bytes at your base, from `git show`>, "note": <one sentence>}`. In `series.fields.income_claim` ONLY `fixed_reason` (exactly the new code), `source` and `sentence` change: the words say the RETURN METHOD does not separate income (the source carries it), keep `income`, `null`, `never` and `zero`, and carry neither the old code nor "the source reports no income". In `income_claim_rule` ONLY `present_when` (keep `every` and `income` and `null`; drop the claim that the source reports no income) and `reason` (the new code) change; `value` and `absent_means` stay. Every other key stays byte-identical.
4. **The tests.** A NEW file `data/assets/scripts/gold/irpt_reporting/tests/test_income_reason_rename.py`, at least six passing tests reading both contract files: the versions; the new code in the live parts and the old code in none of them; the words (`return method`, `separate`); both schema hashes equal to their 0.4.3 values; the history keeps the old code only where it is history; `income_claim`'s other declarations unchanged. The EARLIER contract tests (`test_account_return_contract_040.py` to `_044.py`, `test_series_contract_030.py`, `_031.py`) change by at most TWENTY-EIGHT lines in all, each edit commented with this order's id and forced by the version bump or the renamed string; any other failure of an earlier test is a BLOCKING row. The publisher's and handler's tests are not yours.
5. **Facts record** `RD_INCOME_REASON_RENAME_FACTS_R149.json` in your folder with EXACTLY these fields: `source_version` ("0.4.5"); `series_version` ("0.3.2"); `reason` (the new code); `old_code_in_live_parts` (0); `base_sha256` ({"source": <sha256 of the 0.4.4 file's bytes at your base>, "series": <sha256 of the 0.3.1 file's bytes at your base>}); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what was renamed and why, that both schema hashes are unchanged, and what is NOT proven: that any series carries the reason, which is the writer cell's and the republish's).

<criterion id="DB157-1-AC1" cell_refs="DB-b-289"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p157_reasonrename.py" . DB157-1-AC1</invocation><expect>DB157-1-AC1 PASS</expect></criterion>
`DB157-1-AC1` -- each contract differs from its base ONLY in the allowed places: the version, one appended history entry, the renamed reason and its words, one rule-24 key (source), the claim rule's `present_when` and `reason` (series); both schema hashes, `optional_columns` and every other key are byte-identical.
<criterion id="DB157-1-AC2" cell_refs="DB-b-289"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p157_reasonrename.py" . DB157-1-AC2</invocation><expect>DB157-1-AC2 PASS</expect></criterion>
`DB157-1-AC2` -- the live parts of both contracts name `RETURN_METHOD_DOES_NOT_SEPARATE_INCOME`, carry no `SOURCE_REPORTS_NO_INCOME`, and do not say the source reports (or states) no income; the words say the return method does not separate income.
<criterion id="DB157-1-AC3" cell_refs="DB-b-289"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p157_reasonrename.py" . DB157-1-AC3</invocation><expect>DB157-1-AC3 PASS</expect></criterion>
`DB157-1-AC3` -- your new test file holds at least six passing tests, the earlier contract tests pass with at most twenty-eight changed lines in all, the worker's commits change only the two contracts, the test files, the folder, the investigation file and task-order files, and the facts record equals the recount.

<expected_criteria>DB157-1-AC1,DB157-1-AC2,DB157-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the publisher, the handlers, the adapters, the other contracts, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic. The 343,256 and 1,096,830 are counts the CTO measured, quoted as counts.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W233-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/tests/test_income_reason_rename.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_040.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_041.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_042.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_043.py
data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_044.py
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_030.py
data/assets/scripts/gold/irpt_reporting/tests/test_series_contract_031.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~233/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-289.income-reason-rename-both-contracts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 150 (round 149, workstream CONTRACT), cell `DB-b-289`.
<owned_cells>DB-b-289</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB157-1-AC1, DB157-1-AC2, DB157-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~233/IRPT_DASHBD.TO-DB-b-289.income-reason-rename-both-contracts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB157-1-AC1,DB157-1-AC2,DB157-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed keys of each contract in one line each; the test counts and the earlier-test lines changed; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: two JSON standards and test files in a branch; nothing writes or reads the renamed code yet.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its diff, words, grant and facts clauses were validated by the issuer against references built from the real 0.4.4 and 0.3.1 contracts (green) and 35 single-fault arms (all red) by the self-test.
lane: the <paths> block IS the grant.
</preflight>
