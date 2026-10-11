# TO NFRA_OPSWKF.TO-OW-s3 -- the trade submission route refuses every caller who is not Opal-internal, first

<to_id>NFRA_OPSWKF.TO-OW-s3</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~9</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>S</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (path floor: a Lambda handler; you apply nothing) | **Decomp cell:** `OW-s-3` |
**outcome_ref:** FWD-9 (PRD v0.8) | **depends_on:** none.

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~9`. Your worktree is `C:/tmp/opswkf-s-9` (branch `wk-NFRA_OPSWKF-9`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~9
<0.9.0_WK_NFRA_OPSWKF~9@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### THE CELL

`OW-s-3`. `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py` (read it whole first). Its
`lambda_handler` (from line 160) decides on two things only: that the authorizer context carries an email (403 at lines 187-190)
and that a body `initiator_email`, if present, equals it (403 at lines 192-195). Tier and firm are never read. So ANY signed-in
portal user with an email can store a PENDING_APPROVAL trade submission and cause a mail to the approvers group. The fix is the
rule the sibling function `trade-dashboard-api` already carries: read
`infra/aws/lambda/trade-pipeline/trade-dashboard-api/src/dashboard_api.py` lines 38-60 (`OPAL_INTERNAL_TIER`,
`OPAL_INTERNAL_FIRM_ID`, `_require_internal`) and write the SAME two comparisons here.

Build this, and nothing else:

1. Two module constants, `OPAL_INTERNAL_TIER = 'internal'` and `OPAL_INTERNAL_FIRM_ID = 'opal-capital'`, and a helper
   `_require_internal(event)`: it reads the authorizer context exactly as lines 184-185 do
   (`event.requestContext.authorizer`, then `.get('lambda', ctx)`), and returns `None` when
   `str(tier or '').strip() == 'internal'` OR `str(firmId or '').strip() == 'opal-capital'`. Both are EXACT matches, never
   truthiness (the authorizer sends the STRING `null` for an absent firmId). `userType` is not read. Otherwise it returns
   `cors_response(403, {'message': 'Forbidden: trade submission answers Opal staff only'})`. That message is EXACT and must
   differ from the handler's two existing 403 messages. It reads no table.
2. `lambda_handler` calls it FIRST: immediately after the CORS preflight return (lines 163-165) and BEFORE the body is parsed,
   before the email check, before any table, `get_user`, `get_users_by_group` or `send_approval_request`. A caller who is not
   Opal-internal therefore gets the new 403 whatever the body is, and whether or not it carries an email.
3. Everything after it is unchanged: an Opal-internal caller meets the email check, the `initiator_email` check, the
   `ticket_id` check (400 `ticket_id is malformed` at lines 200-202) and the rest exactly as today.

**Tests:** `infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_submit_internal_only.py` (new). Stub the table and
the lookups the way `tests/test_initiator_from_token.py` does (read it). Exact test names:

- `test_opal_firm_caller_reaches_the_ticket_check`: tier `advisor`, firmId `opal-capital`, an email, body with
  `ticket_id` `not-a-ticket-id` and NO `initiator_email` -> 400 with message `ticket_id is malformed`.
- `test_tier_internal_caller_reaches_the_ticket_check`: tier `internal`, firmId the string `null`, same body -> the same 400.
- `test_client_tier_refused_with_the_new_message`: tier `client`, another firm, WITH an email, same body -> 403 whose message
  is exactly the new one and is neither of the two existing 403 messages.
- `test_service_tier_refused_with_the_new_message`: tier `service`, firmId the string `null`, with an email -> the same 403.
- `test_outsider_without_email_gets_the_new_message_first`: tier `advisor`, firmId `49financial`, NO email -> 403 with the NEW
  message (not "no verified submitter identity").
- `test_refusal_touches_no_table_no_user_lookup_and_no_mail`: with `dynamodb`, `get_user`, `get_users_by_group` and
  `send_approval_request` replaced by stubs that raise on any use, a refused caller posting a complete valid body still gets
  the 403.
- `test_opal_caller_legacy_submit_still_stores`: tier `advisor`, firmId `opal-capital`, a complete valid body with no
  `ticket_id` -> 200 and one stored item whose `initiator_email` is the token's.

**The three existing test files build events whose authorizer context has no tier and no firmId**, so after your change their
submits would 403. In `test_initiator_from_token.py`, `test_ticket_bridge.py` and `test_model_upload.py`, give every authorizer
context that carries an email `"firmId": "opal-capital"` as well. Change nothing else in them, with one exception:
`test_no_authorizer_context_403` must still expect 403 (it now meets the new check first; if it asserts the old message, change
that one assertion to the new message and say so in your report).

### ACCEPTANCE

<criterion id="OW-s3-AC1" cell_refs="OW-s-3"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/S_CHECKS/ow_s_checks.py s9-tests</invocation><expect>OW-S9-TESTS-OK</expect></criterion>
`OW-s3-AC1`: the seven named tests exist and pass.

<criterion id="OW-s3-AC2" cell_refs="OW-s-3"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/S_CHECKS/ow_s_checks.py s9-probe</invocation><expect>OW-S9-PROBE-OK</expect></criterion>
`OW-s3-AC2`: the issuer's own probe of `lambda_handler` -- seven outsiders (five with an email, one without, one with no
context) on four bodies (a malformed `ticket_id`, a complete valid body, an empty body, a body naming another initiator) are
each answered 403 with the new message, with no table, user lookup or mail touched; two insiders (tier internal; tier advisor
with firmId `opal-capital`) posting the malformed `ticket_id` are answered 400 `ticket_id is malformed`.

<criterion id="OW-s3-AC3" cell_refs="OW-s-3"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/S_CHECKS/ow_s_checks.py s9-regress</invocation><expect>OW-S9-REGRESS-OK</expect></criterion>
`OW-s3-AC3`: the handler's whole test directory passes, the three pre-existing files included (22 tests pass at the base; the
count after your change is 22 plus yours).

<expected_criteria>OW-s3-AC1,OW-s3-AC2,OW-s3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~9/`,
  and this order's file (status flip only). `dashboard_api.py`, `email_utils.py`, `config.py`, `workflow_handler.py` and the check
  file `ow_s_checks.py` are READ only.
- Never call AWS. Deploy nothing. Touch no Terraform and no portal file.
- No non-ASCII in anything you write. If you need a row, append it in BINARY mode as `NFRA_OPSWKF-D2-W9-S<k>`, keeping the
  file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing.

<paths>
infra/aws/lambda/trade-pipeline/trade-submission-handler/src/submission_handler.py
infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_submit_internal_only.py
infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_initiator_from_token.py
infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_ticket_bridge.py
infra/aws/lambda/trade-pipeline/trade-submission-handler/tests/test_model_upload.py
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (workstream S), cell `OW-s-3`.
<owned_cells>OW-s-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-s3-AC1, OW-s3-AC2, OW-s3-AC3. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~9/NFRA_OPSWKF.TO-OW-s3.submit-internal-only.proof_of_spec.json`.
Validate it with the worktree's own `python .tools/proof-of-spec-check.py <instance> OW-s3-AC1,OW-s3-AC2,OW-s3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the three check lines verbatim, the commit, every line you changed in the three pre-existing test files (file
and what), and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM change; the handler reads no new resource
comp-adversary: DECLARED-NOT-APPLICABLE at the cut (nothing built yet); the adversarial read of this authorization change runs at the drain on the merged handler, and criterion OW-s3-AC2 is the issuer's own probe of it
lane: trade-pipeline submission handler; this project's OW-e-1 and OW-e-2 wrote it last (round 1, complete); no open order on it.
</preflight>

Release: PRD v0.8 @cfc5091071, ratified-text half SIGNED @1b8530a2fc (`1.0.0_SA_CTO~DELL2` msg 5710): FWD-9 is cut after
FWD-8's ledger closes, as its own cell and its own pair. The release (cell `OW-s-d-2`) is the issuer's; this order applies nothing.
