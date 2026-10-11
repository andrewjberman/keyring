# TO TCKT_VNEXT.TO-R5-ml1 -- the client mail log lines carry a digest of the recipient and never the address

<to_id>TCKT_VNEXT.TO-R5-ml1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~18</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD; nothing is applied and nothing runs against AWS | **Decomp cell:**
`R5-ml-1` (`decompositions/TCKT_VNEXT_DECOMP_R5.md`) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~18`. Your worktree is `C:/tmp/tckt-r5-18` (cut from box/dell2 at the issuance commit). Work and
commit only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~18 <0.9.0_WK_TCKT_VNEXT~18@opal.agent>" -F <msgfile> -- <paths>`. Write
the message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or
stage it.

### WHY

`infra/aws/lambda/ticket_center/lambda_function.py` sends ONE notice to a ticket's client (`notify_client`, about lines 1010-1042) and logs the outcome on four
greppable lines (`WE_CLIENT_SENT`, `WE_CLIENT_SEND_FAILED`, `WE_CLIENT_NOT_SINGULAR`, `WE_CLIENT_NAME_DEGRADED`). None says WHO
the notice went to, so a seat reading the log cannot tell two recipients apart or show that a test notice went to a test
address. The address itself must never be logged. And today `WE_CLIENT_SEND_FAILED` prints the raw exception text
(`error={type(e).__name__}: {e}`), which for a mail service can contain the recipient address.

### THE CELL `R5-ml-1`

1. Add a helper `_recipient_digest(address) -> str`: the first 12 hex characters of the sha256 of the address, stripped and
   lower-cased, UTF-8. For a missing or empty address it returns the literal `none`.
2. `WE_CLIENT_SENT` gains ` to_digest=<digest>` (the one recipient it sent to). Nothing else on that line changes.
3. `WE_CLIENT_SEND_FAILED` gains ` to_digest=<digest>` and STOPS printing the exception's text: it prints
   `error=<the exception's class name>` only. If the single recipient could not be resolved before the failure, the digest is
   `none`. `notify_client_isolated` still raises nothing, ever, and a failed notice still never costs a ticket or a claim.
4. `WE_CLIENT_NOT_SINGULAR` and `WE_CLIENT_NAME_DEGRADED` are NOT changed (the first has no single recipient; the second names
   a claimer label, not a recipient).
5. No address, and no part of one, appears on any log line. No send is made by a test: use the folder's existing fakes
   (`tests/conftest.py` refuses a real call). Update the docstring of `notify_client_isolated` to name the new field.
   Change nothing else in the file. No non-ASCII.

### ACCEPTANCE

<criterion id="R5-ml1-AC1" cell_refs="R5-ml-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py ml-digest</invocation><expect>ML-DIGEST-OK</expect></criterion>
`R5-ml1-AC1`: the new file `infra/aws/lambda/ticket_center/tests/test_client_mail_digest.py` holds these tests and they pass:
`test_sent_line_carries_the_recipient_digest_and_not_the_address` (capture stdout; the address string and its local part are
absent; `to_digest=` equals the helper's value), `test_send_failed_line_carries_the_digest_and_no_error_text_with_the_address`
(the fake mail client raises an error whose text CONTAINS the recipient address; the log line does not contain it),
`test_digest_is_the_same_for_the_same_address_in_any_case`.

<criterion id="R5-ml1-AC2" cell_refs="R5-ml-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py ml-regress</invocation><expect>ML-REGRESS-OK</expect></criterion>
`R5-ml1-AC2`: the whole folder `infra/aws/lambda/ticket_center/tests` passes (at least 178 passed, 0 failed: the 175 at the base plus the 3
new). An existing test that asserts the old `WE_CLIENT_SEND_FAILED` text is changed to the new form; list each one changed.

<expected_criteria>R5-ml1-AC1 R5-ml1-AC2</expected_criteria>

Dry-run at base: AC1 FAIL (absent test file) and AC2 FAIL (175 passed, below 178), both as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only).
- Make no AWS call, no network call, no deploy. Run each invocation from the worktree root under `timeout 120`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W18-S<k>` with k from 1 upward, its own fenced block at the
  end of the investigation file, keeping the file's line endings; `surfaced_at` is `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof instance goes in your deliverables folder ROOT (`deliverables/0.9.0_WK_TCKT_VNEXT~18/`), validated from the worktree
  root; the check takes criterion ids COMMA-separated. Do not write report or markdown summary files.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~18/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R5_CHECKS/r5_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R5.md</decomp_doc> (round 5), cell `R5-ml-1`.
<owned_cells>R5-ml-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R5-ml1-AC1 R5-ml1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~18/TCKT_VNEXT.TO-R5-ml1.client-mail-log-recipient-digest.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R5-ml1-AC1,R5-ml1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** both check lines verbatim, the commits, the helper and the two changed log lines with line numbers, every existing test you
changed and why, the sha256 from `git show HEAD:infra/aws/lambda/ticket_center/lambda_function.py | sha256sum`, and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arm is the test whose mail error text carries the address.
</preflight>

Source: the CTO's round-5 analysis @d94b65958b section 3; decomposition `TCKT_VNEXT_DECOMP_R5.md`.
