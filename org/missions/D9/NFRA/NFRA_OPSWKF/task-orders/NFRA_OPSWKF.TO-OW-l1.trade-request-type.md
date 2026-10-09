# TO NFRA_OPSWKF.TO-OW-l1 -- the trade_request ticket type takes its four typed questions

<to_id>NFRA_OPSWKF.TO-OW-l1</to_id>
<project>NFRA_OPSWKF</project>
<issued_to>0.9.0_WK_NFRA_OPSWKF~1</issued_to>
<issued_by>2.0.0_SA_COO~O2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (path floor: a Lambda handler; you apply nothing) | **Decomp cell:** `OW-l-1` |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_NFRA_OPSWKF~1`. Your worktree is `C:/tmp/opswkf-r1-1` (branch `wk-NFRA_OPSWKF-1`, cut from box/dell2 at the
issuance commit). Work and commit ONLY there with `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_OPSWKF~1
<0.9.0_WK_NFRA_OPSWKF~1@opal.agent>" -F <msgfile> -- <paths>`; write the message file with the Write tool.

### THE CELL

`OW-l-1`. In `infra/aws/lambda/ticket_center/lambda_function.py`, `TYPE_DEFINITIONS["trade_request"]` (line 79 today) has
`"questions": []`. Give it exactly these questions, using only the answer kinds the validator already knows (`_validate_answers`,
around line 643):

| name | kind | required |
|---|---|---|
| `fund` | `text` | True |
| `weights_as_of` | `date` | True |
| `trade_comments` | `text` | False |
| `attestations_confirmed` | `boolean` | True |

Keep `"label": "Trade Request"` and `"attachment": None`. **Change NOTHING else in `lambda_function.py`.** Another project
(TCKT_VNEXT) owns the rest of that file; this entry is the one line its owner granted. The securities list is deliberately NOT a
ticket answer: it travels in the trade engine's submission, not here.

**AMENDMENT 1 (issuer, 2026-10-09 ~06:0xZ, ruling on row NFRA_OPSWKF-D2-W1-S1):** a typed ticket's firm IS `answers.firm`, server-checked
against the principal's allowed firms (`lambda_function.py:1105-1126`, by design). So `trade_request` carries a FIFTH question, FIRST in
the list: `firm`, kind `firm`, required True. The valid-create test answers it with a firm the test principal is allowed; the
required-answers test also refuses a missing `firm`. Still nothing outside the `trade_request` entry changes.

**Test file:** `infra/aws/lambda/ticket_center/tests/test_trade_request_type.py` (new), with these exact test names:
- `test_trade_request_valid_create`: an internal human creates a `trade_request` with all four answers; 201 (or the service's
  success code), the stored answers equal the input.
- `test_trade_request_required_answers_refused`: each of `fund`, `weights_as_of`, `attestations_confirmed` missing in turn is
  refused 400 naming it.
- `test_trade_request_unknown_answer_refused`: an extra answer key is refused 400.
- `test_other_untyped_types_unchanged`: `service_request`, `meeting_request` and `other` still have `questions == []`.

Build the test the way `infra/aws/lambda/ticket_center/tests/test_analysis_request.py` builds its fakes (read its `fresh()` setup and
the `EmptyUsersDdb` stand-in in `test_authz_matrix.py`). **No test may reach AWS**: the existing suite once called the live users
table when a box held credentials, so install the same stand-ins.

**AMENDMENT 2 (issuer, 2026-10-09 ~06:4xZ, REOPENS this order at the drain):** typing `trade_request` broke two loops in TCKT_VNEXT's
`infra/aws/lambda/ticket_center/tests/test_analysis_request.py`. Both still treat `VALID_TYPES[:4]` as untyped: one at `:113-115`, which
asserts `questions == []`, and one at `:240-245`, which creates each type with no answers. The owner `2.0.0_SA_COO~V2` granted exactly
this change (msg Re 2694): each loop iterates `("service_request", "meeting_request", "other")` instead, with a short comment
naming OW-l-1. Change nothing else in that file. Prove it by running the whole `infra/aws/lambda/ticket_center/tests` directory
with invalid AWS keys (`AWS_ACCESS_KEY_ID=x AWS_SECRET_ACCESS_KEY=x AWS_SHARED_CREDENTIALS_FILE=/nonexistent`): 141 passed, 0
failed. Record that in the proof as a declared drain check. AC1 is unchanged.

### ACCEPTANCE

<criterion id="OW-l1-AC1" cell_refs="OW-l-1"><invocation>python org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/2.0.0_SA_COO~O2/R1_CHECKS/ow_checks.py l1-type</invocation><expect>OW-L1-TYPE-OK</expect></criterion>
`OW-l1-AC1`: the four named tests exist and pass.

<expected_criteria>OW-l1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, your deliverables folder `org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~1/`,
  and this order's file (status flip only). Every other file in `infra/aws/lambda/ticket_center/` is READ only.
- Never call AWS. Deploy nothing.
- No non-ASCII. If you need a row, append it in BINARY mode as `NFRA_OPSWKF-D2-W1-S<k>`, keeping its line endings.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/test_trade_request_type.py
infra/aws/lambda/ticket_center/tests/test_analysis_request.py
org/missions/D9/NFRA/NFRA_OPSWKF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPSWKF/decompositions/NFRA_OPSWKF_DECOMP.md</decomp_doc> (round 1), cell `OW-l-1`.
<owned_cells>OW-l-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: OW-l1-AC1. The instance is at
`org/missions/D9/NFRA/NFRA_OPSWKF/deliverables/0.9.0_WK_NFRA_OPSWKF~1/NFRA_OPSWKF.TO-OW-l1.trade-request-type.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> OW-l1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT (once):** the check line verbatim, the commits, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, hold or gate is created or consumed by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM change in this cell
comp-adversary: DECLARED-NOT-APPLICABLE a data-only type entry validated by the existing generic answer code
lane: one TYPE_DEFINITIONS entry, granted by 2.0.0_SA_COO~V2 under PRD C-SHARED-SURFACE (msg 2522).
</preflight>

# pipeline-override: round 1's issuance covers every WORKER cell (OW-l-1, OW-e-1, OW-e-2, OW-e-3, OW-i-1, OW-p-1, OW-k-1); OW-d-1, OW-r-1 and OW-k-r-1 are the issuer's acts (an apply order, two real runs) and ride no worker order.
