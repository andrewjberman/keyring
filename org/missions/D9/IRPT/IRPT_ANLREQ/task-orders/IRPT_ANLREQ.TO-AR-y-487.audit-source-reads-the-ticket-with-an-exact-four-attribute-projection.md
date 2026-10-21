# TO IRPT_ANLREQ.TO-AR-y-487.audit-source-reads-the-ticket-with-an-exact-four-attribute-projection -- BUILD AND PROVE OFFLINE: ticket_audit_source.py reads the ticket with a ProjectionExpression of exactly ticket_id, ticket_type, answers, created_at, and no longer reads filer_user_type; nothing is run against AWS

<to_id>IRPT_ANLREQ.TO-AR-y-487.audit-source-reads-the-ticket-with-an-exact-four-attribute-projection</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~361</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ146</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-487` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** C-AUDIT-RECORD (PRD v0.28) | **depends_on:** CTO ruling A, msg 11858 (attribute-restricted GetItem on opal-tickets, own pair; the code ships in a later release, not r34q)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~361`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-361` (branch `wk-IRPT_ANLREQ-361`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~361 <0.9.0_WK_IRPT_ANLREQ~361@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W361-S<k>`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING, with `spec_asserts` and `world_is` fields. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy, no release build.** Terraform is not installed on this box: do not try to run it. The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~325/IRPT_ANLREQ.TO-AR-y-459.run7b-browser-leg-script-re-proved-offline-against-the-advisor-required-form.proof_of_spec.json` (read it first; `controls` holds `mutant` and `determinism` only), with `to_id` exactly the order's id; run `python .tools/proof-of-spec-check.py <instance> "AR487-y-AC1,AR487-y-AC2,AR487-y-AC3"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (with the instance, one commit) only on VALID. The instance's check-script reference is pinned to a commit that EXISTS (commit the script first, then pin it).

### THE CELL (`AR-y-487`, inlined)

*Why.* The CTO ruled (msg 11858) that the resident role's read of `opal-tickets` is a `GetItem` restricted by IAM to the attributes `ticket_id`, `ticket_type`, `answers`, `created_at`, and that the audit source sends a `ProjectionExpression` of exactly that set; `filer_user_type` is dropped from the read so the code and the policy (sister cell AR-y-486) name the same four. Without the projection the IAM condition denies the read. The ticket service writes no `filer_user_type` onto the item today, so the audit record's `filer.user_type` stays null (AR-y-469 S2).

*The change.* In `infra/aws/lambda/investor-reporting/ycharts/generate/ticket_audit_source.py` (read it in full first, 95 lines): the single `dynamodb.get_item(...)` call becomes `get_item(TableName=table, Key={"ticket_id": {"S": ticket_id}}, ConsistentRead=True, ProjectionExpression=<the four names>, ExpressionAttributeNames=<alias per name>)` where the aliases are `#t0`..`#t3` (`#t0`=ticket_id, `#t1`=ticket_type, `#t2`=answers, `#t3`=created_at) so no name depends on DynamoDB's reserved-word list; the module declares the four names once as a module-level tuple `PROJECTED_ATTRIBUTES` in that order, and the expression and the alias map are built from it. Remove the read of `found["filer_user_type"]` and the code that validates it: the returned ticket dict still carries the key `filer_user_type` with the value `None` (the consumer, `reports/analysis_audit.py`, expects the key); update the module docstring paragraph about `filer_user_type` to say it is never read (the role may not read it) and is None. Everything else is unchanged (the miss-is-None behaviour, the tenant check, ASCII only, no value in any exception). New test file `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_audit_projection.py` (hermetic, fake dynamodb client recording its call, in the style of the existing audit tests): the recorded call carries `ProjectionExpression` equal to the four aliases joined by `, ` and `ExpressionAttributeNames` mapping exactly the four aliases to the four names, and `ConsistentRead` True, and no other attribute name appears anywhere in the call; a fake item that ALSO carries `filer_user_type`, `requester` and `created_by` yields a result that contains none of their values and a `filer_user_type` of None; a fake item lacking `answers` yields None (a miss); `PROJECTED_ATTRIBUTES` equals the tuple exactly. Update `test_audit_live_wiring.py` only where an existing assertion depends on `filer_user_type` being read from the item (read it; keep every other assertion; no test deleted or skipped).

*The checks.* In `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~361/`: `check_audit_projection.py` (stdlib only, ruff clean, offline). It reads `ticket_audit_source.py` as TEXT and prints `AUDIT-PROJECTION-OK attrs=ticket_id,ticket_type,answers,created_at projection=yes filer_user_type_read=no` only if: `PROJECTED_ATTRIBUTES` equals the four names in that order; the source contains `ProjectionExpression=` and `ExpressionAttributeNames=` in the `get_item` call; the text `found["filer_user_type"]` and `"filer_user_type" in found` do not occur; `requester` and `created_by` occur only in comments or the docstring (not in code lines). Else `AUDIT-PROJECTION-BAD <why>` (rc 1). `--selftest` mutates the text in memory three ways (the `ProjectionExpression=` argument removed; a fifth name added to the tuple; the `found["filer_user_type"]` read put back) and prints `CONTROL-FIRES` only when ALL THREE read BAD. Commit order: the code and test edits as ONE commit first, message citing AR-y-487; then your deliverables and instance.

---

## ACCEPTANCE

<criterion id="AR487-y-AC1" cell_refs="AR-y-487"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~361/check_audit_projection.py</invocation><expect>^AUDIT-PROJECTION-OK attrs=ticket_id,ticket_type,answers,created_at projection=yes filer_user_type_read=no$</expect></criterion>
<criterion id="AR487-y-AC2" cell_refs="AR-y-487"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~361/check_audit_projection.py --selftest</invocation><expect>^CONTROL-FIRES$</expect></criterion>
<criterion id="AR487-y-AC3" cell_refs="AR-y-487"><invocation>(cd infra/aws/lambda/investor-reporting && python -m pytest ycharts/generate/tests/test_ticket_audit_projection.py reports/tests/test_generate_installed.py ycharts/generate/tests/test_audit_live_wiring.py reports/tests/test_analysis_audit.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)</invocation><expect>^[0-9]+ passed in </expect></criterion>

<proof_of_spec>
The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~361/IRPT_ANLREQ.TO-AR-y-487.audit-source-reads-the-ticket-with-an-exact-four-attribute-projection.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-487.audit-source-reads-the-ticket-with-an-exact-four-attribute-projection`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR487-y-AC1,AR487-y-AC2,AR487-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-487</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write. `test_audit_live_wiring.py` leaks `sys.path` at module level (row W350-S1): where it is in a pytest line it is listed last-but-one as written; report any other order problem as a row and do not fix files outside the grant.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/ticket_audit_source.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ticket_audit_projection.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_audit_live_wiring.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~361/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-487.audit-source-reads-the-ticket-with-an-exact-four-attribute-projection.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one source file and two test files; nothing is deployed, built into a release or run against AWS; the code ships in a release after r34q under its own pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the source, the CTO's ruling and the consumer analysis_audit.py against this cell; the lens: a projection that names a fifth attribute, an alias list that does not match, a result that still carries requester or created_by values, the filer_user_type read left in place, a consumer broken by a dropped key, a test deleted or skipped, a control that cannot fire. NOT seen (blind): how DynamoDB counts aliased names for the IAM attribute condition (the applier's live read decides); denominator: three criteria.
</preflight>
