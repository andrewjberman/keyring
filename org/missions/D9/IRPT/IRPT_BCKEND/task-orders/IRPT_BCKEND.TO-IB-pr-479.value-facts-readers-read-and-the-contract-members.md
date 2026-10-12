# TO IRPT_BCKEND.TO-IB-pr-479 -- C-VALUEFACTS step 1: every reader of `value_facts` (backend and portal), and the two members declared in both schema copies

<to_id>IRPT_BCKEND.TO-IB-pr-479</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~334</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>166</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6503 (CTO ROUND-166 ANALYSIS section 2 row D2-W321-S1 and section 3 item 5; PRD ADDENDUM v0.50, contract C-VALUEFACTS, line 1320) | **Decomp cell:** `IB-pr-479` (decomposition section 158) | **outcome_ref:** FWD-3

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-334/` (bash `/c/dev/wk-irpt-bckend-334`). Work only there, except for READS of the portal checkout named below; `git rev-parse HEAD` before your first commit is `base_commit` (state it).

**HARD BOUNDS.** READ the readers; BUILD only the schema declaration below. No AWS call, no Lambda invoked, no route called, nobody signs in, no vendor call, nothing deployed. The portal checkout is READ-ONLY: you edit no file there and run no build, install or test there. NO figure, account id or client name goes into any file you write.

**Why.** PRD `## ADDENDUM v0.50` (line 1320 of `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`; read it whole) names the contract: **C-VALUEFACTS.** `optional_facts.value_facts`, when not null, carries `start_value` (the window's opening value) and `end_value` (its closing value), as three emitters write them today (`holdings_gold.py:273`, `f49_engine.py:229`, `orion_adapter.py:169-170`); no other spelling is a member.
`bd_adapter.py` (lines about 194-195) alone writes `beginning_market_value` and `ending_market_value`, and the portal adapter reads those names. The whole change ships later as ONE never-widen pair in this order: step 1 the portal adapter reads the contract members (keeping the market-value names as a read for the Black Diamond path only until step 2 is live); step 2 `bd_adapter.py` renames; step 3 the fallback read is removed.
That pair is cut on THIS cell's read. This cell therefore does two things and edits no emitter and no portal file.

**Read (the record).** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~334/IB166-4_value_facts_readers.json`:
1. `backend_readers`: every place under `infra/aws/lambda/investor-reporting/` (the service, normalize, adapters, narrative, the contracts, the tests and their fixtures) that READS a member of `value_facts` or the two market-value names (not the writers; the writers are in `~326`'s record `IB165-1_value_member_names.json`). Each `{cite, reads_names, in_words}`. `backend_census: {pattern, files_searched, files_with_a_hit}` with the denominator printed (the native Grep tool).
2. `portal_readers`: every reader of `value_facts` and of those names in the PORTAL source, read at the shared portal checkout `C:/dev/ajb_workspace/portal/src` (search it with the native Grep tool by absolute path). Each `{cite, reads_names, in_words}` where `cite` is `src/<path>:<line>` relative to the portal root (the first known one is `src/pages/InvestorReporting/contracts/adapt.ts` about lines 797-799 and 839-840, and the tile code `tabs/reporting/PerformanceHeadline.tsx`; find the rest). For each, say whether it renders a value tile, and what it shows when the member is absent.
   `portal_census: {pattern, files_searched, files_with_a_hit}`. State the portal checkout's VINTAGE: `portal_commit` is the 40-hex output of `git -C C:/dev/ajb_workspace/portal rev-parse HEAD`; `portal_dev_head` is the 40-hex portal `DEV` head you can read (`git -C C:/dev/ajb_workspace/portal rev-parse origin/DEV` or `DEV`; no fetch), or `null` with `portal_dev_head_reason` if you cannot read it. Do NOT fetch, pull or check anything out in the portal.
3. `not_established` (a list): at least the served response (no answer was fetched) and anything you could not read.

**Build (the schema).** In BOTH `infra/aws/lambda/investor-reporting/_contracts/PerformanceReport.schema.json` and `docs/contracts/investor-reporting/v1/PerformanceReport.schema.json`, declare under `optional_facts.properties.value_facts.properties` the members `start_value` and `end_value`, each type `["number","null"]`, each with a description naming the window's opening or closing value; the object's other members STAY open (`additionalProperties` is not set to false), and `value_facts` stays `object or null`. Keep the two copies in step with each other (they differ today only in their `$id`). The fixtures stay as they are (they are null-valid); do not edit them unless a contract test requires a read of them.

<criterion id="IB166-4-AC1" cell_refs="IB-pr-479"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-4-AC1</invocation><expect>IB166-4-AC1 PASS</expect></criterion>
<criterion id="IB166-4-AC2" cell_refs="IB-pr-479"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-4-AC2</invocation><expect>IB166-4-AC2 PASS</expect></criterion>
<criterion id="IB166-4-AC3" cell_refs="IB-pr-479"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r166/p166_cells.py" . IB166-4-AC3</invocation><expect>IB166-4-AC3 PASS</expect></criterion>

<expected_criteria>IB166-4-AC1, IB166-4-AC2, IB166-4-AC3</expected_criteria>

What the checks grade: AC1 the record's form (at least 3 resolving backend cites, at least 1 portal reader with a `src/...:line` cite, both censuses with a denominator above 0, the 40-hex `portal_commit`, the six bound counters 0) and that nothing outside the two schema copies, `_contracts/`, `docs/contracts/investor-reporting/`, your deliverables, rows and order changed;
AC2 both schema copies declare the two members as number-or-null with the others open, the valid fixture still validates, the invalid one still fails, a `value_facts` with the two members and an open member validates, and a string `start_value` is rejected; AC3 the `_contracts` suite (203 passed and 2 failed at base, the two failures being
`test_every_declared_route_has_a_response_contract_whose_refs_resolve` and `test_control_a_known_good_document_conforms_and_a_known_bad_one_does_not[analysis-request-original]`, not yours) reads no new failure. AC3 PASSes at base BY DESIGN: it is the regression guard.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. NO emitter (`holdings_gold.py`, `f49_engine.py`, `orion_adapter.py`, `bd_adapter.py`) and NO portal file is edited; the rename and the portal move are cut on your read, in a later round.
- **Refusal clause:** a reader you cannot read, a schema change that breaks a contract test, a portal checkout you cannot read: file a row and report. Never weaken a check or a test; do not edit `p166_cells.py`.
- **Hash pins:** list any test, manifest or SHA256SUMS that pins the bytes of a schema file you change (`hash_pins` in the record) and say what you did; regenerate one only if it is inside your `<paths>`.
- **Row ids** are `IRPT_BCKEND-D2-W334-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~334" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~334@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~334 <0.9.0_WK_IRPT_BCKEND~334@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/_contracts/PerformanceReport.schema.json
infra/aws/lambda/investor-reporting/_contracts/fixtures/
infra/aws/lambda/investor-reporting/_contracts/tests/
docs/contracts/investor-reporting/v1/PerformanceReport.schema.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~334/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-479.value-facts-readers-read-and-the-contract-members.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 158 (round 166, workstream ~P), cell `IB-pr-479`.
<owned_cells>IB-pr-479</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB166-4-AC1, IB166-4-AC2, IB166-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~334/IRPT_BCKEND.TO-IB-pr-479.value-facts-readers-read-and-the-contract-members.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; every backend reader and every portal reader with the names it reads and what it shows when a member is absent; the portal checkout's commit and DEV head; both censuses and their denominators; what is not established; the schema change in a sentence and that the two copies agree;
the `_contracts` suite's last line before and after; the hash pins found and what you did; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell reads readers and edits two contract schema copies in the repo; no emitter or served artifact changes; the schema reaches a package only in a later build under the pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change; no route is called.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p166_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~19:3xZ: IB166-4 AC1 FAIL (no record), AC2 FAIL (start_value is not declared in the schema), AC3 PASS (the regression guard: _contracts reads 203 passed, 2 failed, the two known); commit-gate clean. Measured by the issuer at base: the two PerformanceReport schema copies differ only in `$id` (diff read) and `value_facts` has no properties; jsonschema 4.26 is importable for AC2. The portal is read at the shared checkout, whose gitlink and checkout commits differ (the main tree shows the portal gitlink modified); the worker states which commit it read.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
