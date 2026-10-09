# TO NFRA_OPSWKF.TO-OW-e1 -- the trade engine takes the submitter from the verified token, never the body

<to_id>NFRA_OPSWKF.TO-OW-e1</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~2</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (path floor: a Lambda handler; you apply nothing) | **Decomp cell:** `OW-e-1` |
**outcome_ref:** FWD-1 (PRD C-INITIATOR) | **depends_on:** none. Your NEXT order on this slot is `TO-OW-e2` (same file).

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~2`. Your worktree is `C:/tmp/opswkf-r1-2` (branch `wk-NFRA_OPSWKF-2`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~2
<0.9.0_WK_NFRA_OPSWKF~2@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### THE CELL

`OW-e-1`. `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py:117` reads
`initiator_email = body.get('initiator_email', '').lower()`: the submitter is whoever the BODY says. Change it so the submitter
comes from the API Gateway authorizer context, exactly as the workflow handler already does
(`infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/workflow_handler.py:155-187`, read it):

1. `ctx = event.requestContext.authorizer`; claims = `ctx.get('lambda', ctx)`; `email` = claims `email`, lowercased.
2. No email in the context -> return `cors_response(403, ...)` before anything is written.
3. A body `initiator_email` that is present and differs (case-insensitive) from the token email -> 403. Present and equal, or
   absent -> accepted.
4. `initiator_email` = the token email. `initiator_name` = claims `name` if present, else body `initiator_name`, else the email.
5. Everything else in the handler is unchanged.

**Tests:** `infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_initiator_from_token.py` (new), exact names:
- `test_initiator_is_token_email`: the stored item's `initiator_email` is the token's, even when the body omits it.
- `test_no_authorizer_context_403`: no context -> 403 and `put_item` never called.
- `test_conflicting_body_initiator_403`: body says someone else -> 403 and `put_item` never called.
- `test_legacy_body_without_initiator_accepted`: a TradeSubmission-page body with a matching `initiator_email` still stores.

Stub DynamoDB and the user lookup the way `tests/test_model_upload.py` does. **The existing `test_model_upload.py` builds events
with no authorizer context**, so after your change its submits would 403. Give its events an authorizer context whose email equals
their body's `initiator_email`. Change nothing else in that file.

### ACCEPTANCE

<criterion id="OW-e1-AC1" cell_refs="OW-e-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py e1-token</invocation><expect>OW-E1-TOKEN-OK</expect></criterion>
`OW-e1-AC1`: the four named tests exist and pass.

<expected_criteria>OW-e1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~2/`,
  and this order's file (status flip only). `workflow_handler.py` is READ only.
- Never call AWS. Deploy nothing.
- No non-ASCII. If you need a row, append it in BINARY mode as `NFRA_OPSWKF-D2-W2-S<k>`, keeping its line endings.

<paths>
infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py
infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_initiator_from_token.py
infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_model_upload.py
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (round 1), cell `OW-e-1`.
<owned_cells>OW-e-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-e1-AC1. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~2/NFRA_OPSWKF.TO-OW-e1.initiator-from-token.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-e1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM change in this cell
comp-adversary: DECLARED-NOT-APPLICABLE at the cut (nothing built yet); the adversarial read of this identity change runs at the drain on the merged handler, and the conflicting-body and no-context arms are its tests
lane: trade-pipeline submission handler; TRSB_LEDGER (inactive) wrote it last; no open order on it.
</preflight>
