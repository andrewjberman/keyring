# TO IRPT_DASHBD.TO-DB-b-274 -- the CHAIN CAP of the Cottonwood report-build handler (round 141, workstream B-49F): MAX_DAYS_PER_FIRE holds across the whole chain, by a budget each self-invoke carries, before the reporting-gold schedule is ever enabled

<to_id>IRPT_DASHBD.TO-DB-b-274</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~222</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>141</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 141 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUNDS_133_TO_137_20261015.md ADDENDUM 1 term 4 (msg 8615) ("The cap defect is a build cell (row, owner ~D2). `chain_next` honours `MAX_DAYS_PER_FIRE` across the whole chain, with a test. It lands BEFORE the reporting-gold schedule is ever enabled, because a scheduled `{}` after a gap would otherwise chain without a bound.") | **Decomp cell:** `DB-b-274` (decomposition section 139).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order edits a handler and its tests and runs no AWS call and no Terraform command. The handler's bytes change here, so the deployed function (applied under the revision-2 pair, `CodeSha256` `8pQOR3...`) differs from the repo until a later code-update pair; that pair and the schedule enable are the CTO's and the issuer's later acts and are not part of this order.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-222` (branch `wk-IRPT_DASHBD-222`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~222/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~222/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The handler caps the OWED LIST at `MAX_DAYS_PER_FIRE` (10) but `chain_next` is given the next owed day of that list, and each hop recomputes the list from the newest landed day, so the chain never ends until nothing is owed: one `{}` event over a 65-day backlog chains 68 invocations. The cap must hold across the whole chain.

**The cell (`DB-b-274`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r141/p141_chaincap.py` (your three criteria; its PROBE is the behavioural spec for this cell and it also runs every clause of rounds 135, 137 and 138); the current handler `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py` (`lambda_handler`, `owed_days`, `chain_next`, `_event_day`, `MAX_DAYS_PER_FIRE`) and its tests.
2. **The handler (edit `handler.py`, ADDITIVE; every earlier behaviour and test stays; no new import, no new environment variable).**
   - **The budget.** An event may carry the integer key `chain_left`: the number of further days this chain may build AFTER the day this invocation builds. An event WITHOUT the key (the scheduled fire, an empty event, an explicit `day` event) starts a chain with `chain_left = MAX_DAYS_PER_FIRE - 1`, so the whole chain builds at most `MAX_DAYS_PER_FIRE` days in all.
   - **Validation, before any client is created or any call is made** (with the existing day validation): `chain_left`, when present, must be an `int` that is not a `bool` and lies in `0` to `MAX_DAYS_PER_FIRE - 1`; anything else (`10`, `-1`, `True`, `"3"`, `2.0`, `None`, `99`) raises `SystemExit("REFUSED: ...")` naming `chain_left`, with zero calls.
   - **The chain.** After a non-dry-run day is built, `chain_next` self-invokes only when `chain_left > 0` and a next owed day exists, with the payload `{"day": <next>, "chain_left": <chain_left - 1>}` (still ONE asynchronous `Event` invoke of the function's own ARN). When `chain_left` is 0 the day is built and NOTHING is invoked; the returned `chain` states `{"invoked": False, "day": <next owed day or None>, "capped": True}` when a next owed day exists and the budget ended it, and keeps its present form otherwise. A dry run chains nothing, as today.
   - The day's `result`, its `next` key and every claim and count key are unchanged.
3. **Tests** (extend `tests/test_reporting_gold_cot.py` or add `tests/test_chain_cap.py`; `pytest` passing from the repo root; at least six NEW tests, all earlier tests still passing, still naming cottonwood only): an empty event over 30 owed days, driven hop by hop through a fake S3 and a fake lambda client (feed each recorded payload back as the next event), builds exactly ten days, the oldest first, the payloads carrying `chain_left` 8 down to 0, and the tenth hop chains nothing; a backlog of four days stops at four; an explicit `day` event is capped at ten days in all; `chain_left` 0 builds the day and chains nothing; each of the seven bad budgets above refuses with zero calls; a dry run with a budget chains nothing and writes nothing.
4. **Facts record** `RD_COT_CHAIN_CAP_FACTS_R141.json` in your folder with EXACTLY these fields: `cap` (10); `payload_key` ("chain_left"); `budget_range` ([0, 9]); `applies_to` (["empty event", "explicit day event", "scheduled fire"]); `words` (one paragraph, 80 to 1800 characters: what the budget is and where it is validated, why the cap now holds across the whole chain, and what is NOT proven: the Lambda runtime and the deployed function, which still holds the earlier code).

<criterion id="DB141-1-AC1" cell_refs="DB-b-274"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r141/p141_chaincap.py" . DB141-1-AC1</invocation><expect>DB141-1-AC1 PASS</expect></criterion>
`DB141-1-AC1` -- the handler's source holds every round-138 clause and now holds the word `chain_left`; the worker's own commits touch only the handler directory, the deliverables folder, the investigation file and task-order files.
<criterion id="DB141-1-AC2" cell_refs="DB-b-274"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r141/p141_chaincap.py" . DB141-1-AC2</invocation><expect>DB141-1-AC2 PASS</expect></criterion>
`DB141-1-AC2` -- the checker stages the handler as packaged and drives it through a fake S3 and a fake lambda client: every round-138 scenario still passes; a whole chain from an empty event over 32 owed days builds exactly ten days, the oldest first, each self-invoke carrying `chain_left` one less than the hop before, and stops; a four-day backlog stops at four; an explicit day event is capped at ten days in all; a budget of zero builds the day and chains nothing; seven bad budgets refuse with zero calls; a dry run chains nothing and writes nothing.
<criterion id="DB141-1-AC3" cell_refs="DB-b-274"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r141/p141_chaincap.py" . DB141-1-AC3</invocation><expect>DB141-1-AC3 PASS</expect></criterion>
`DB141-1-AC3` -- the worker's tests pass under pytest and name cottonwood and no other firm; the probe passes again; the facts record has exactly the form of step 4.

<expected_criteria>DB141-1-AC1,DB141-1-AC2,DB141-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `filled_report_values.py`, the adapters, the Terraform roots, the source map, `lib/`, the registry, the contracts, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests use fakes; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic (account ids like `A1`, household ids like `HH1`).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If an earlier test pins the exact chain payload `{"day": <next>}`, change it to read the `day` key only and say so in a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W222-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-gold-cot/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~222/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-274.cottonwood-report-build-handler-chain-cap-across-the-whole-chain.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 139 (round 141, workstream B-49F), cell `DB-b-274`.
<owned_cells>DB-b-274</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB141-1-AC1, DB141-1-AC2, DB141-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~222/IRPT_DASHBD.TO-DB-b-274.cottonwood-report-build-handler-chain-cap-across-the-whole-chain.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB141-1-AC1,DB141-1-AC2,DB141-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the budget rule in one line; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a handler edit, tests and a facts record in a branch; nothing is wired to AWS, packaged, planned, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes: the handler's calls are the ones it already makes, with a budget on the self-invoke payload.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its probe was validated by the issuer against a scratch reference handler (green) and single-fault mutants of it (all red), and its static, grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
