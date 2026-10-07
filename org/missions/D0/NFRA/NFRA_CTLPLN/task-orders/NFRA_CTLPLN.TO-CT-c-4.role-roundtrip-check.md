# TO NFRA_CTLPLN.TO-CT-c-4 -- round 3 CT-c-4: the round trip check -- a Dell writes in, the laptop answers, the Dell creates with the role

<to_id>NFRA_CTLPLN.TO-CT-c-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~4</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-c-4` (`decompositions/NFRA_CTLPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-10 |
**depends_on:** CT-c-2 (the writer), CT-c-3 (the renderer) -- both merged before this order is handed

---

## WORKER FACE

### THE CELL

`CT-c-4`, PRD v0.8 C-ROLE-REQUEST (c): "one exercised round trip: a Dell writes in, the laptop applies, the Dell creates a function with
that role, and a pass of an unnamed role is refused." You BUILD the two instruments that round trip runs on and prove them against
stand-ins. You do NOT run the live round trip: it needs a Dell, the laptop's role apply and the Dell policy's apply, and it is run after
your order by the issuer's route.

**What exists after CT-c-2 and CT-c-3:** `org/devices/role_request.py` (`write`, `validate`, `list`), the records under
`org/devices/role_requests/<device>/`, `infra/aws/terraform/nfra-ctlpln-identity/tests/render_passrole.py`.

**Build:**

1. `org/devices/role_request.py` gains the laptop's verb `mark-applied <record> --role-arn <arn> --commit <hash>` and
   `mark-refused <record> --reason <text>`: refuse unless `AGENTBUS_DEVICE` names the device whose register `role` is `control-plane`;
   refuse an ARN that is not `arn:aws:iam::313476888478:role/<literal name>`; the answer is written to
   `org/devices/role_requests/<laptop device>/answers/<request_id>.json` (the laptop's own directory -- one writer per file, so the
   laptop never edits the Dell's record), carrying `request_id`, `status`, `role_name`, `role_arn`, `applied_at`, `applied_by`,
   `commit` or `reason`. The answer's shape is already in `org/standards/ROLE_REQUEST.schema.json`, and `list` and the CT-c-3
   renderer already read answers from that directory; validate what you write against the schema.
2. `org/devices/role_roundtrip_check.py` -- the script a Dell runs. Arguments: `--project`, `--root`, `--function-name`,
   `--unnamed-role-arn`, `--wait-seconds` (default 1800), `--poll-seconds` (default 30), and `--aws` (the AWS command, default the
   repo's `.tools/aws` shim). Steps, each printed as one line with its result:
   (1) write the request with `role_request.py write` for kind `aws_lambda_function`, service `lambda.amazonaws.com`, one permission
       (`logs:CreateLogStream` on the function's log group, `code_ref` this script's own line);
   (2) poll, by `git fetch` and a read of `origin/CLOUD:org/devices/role_requests/<laptop>/answers/<request_id>.json`, until an answer
       exists or the wait ends; `refused` or a timeout ends the run with `ok=False`;
   (3) `lambda create-function` for `--function-name` with the answered role and a ten-line inline zip handler, then
       `lambda get-function` to read it back;
   (4) `lambda create-function` for `<function-name>-unnamed` with `--unnamed-role-arn`: the EXPECTED result is an AccessDenied on
       `iam:PassRole`; any other result is a failure;
   (5) one IAM write attempt, `iam tag-role` on the answered role: the EXPECTED result is AccessDenied.
   LAST line `ROLE-ROUNDTRIP request=<id> answered=<applied|refused|timeout> create=<ok|fail> unnamed_pass=<refused|ALLOWED|error> iam_write=<refused|ALLOWED|error> ok=<True|False>`.
   The script deletes nothing: a Dell holds no delete. It prints the two names the laptop must remove afterwards.
3. `org/devices/test_role_roundtrip.py` -- the script run end to end against stand-ins: a temporary register and records directory, a
   fake `--aws` command (a small Python script the test writes) that answers each call from a table, and a local bare git remote that
   plays `origin` so step (2) reads a real fetched ref. Cases: the happy path (`ok=True`); the laptop refuses (`answered=refused`,
   `ok=False`); no answer inside the wait (`answered=timeout`); the unnamed pass is ALLOWED by the fake (`unnamed_pass=ALLOWED`,
   `ok=False`); the IAM write is ALLOWED by the fake (`ok=False`); `mark-applied` run as a Dell is refused; `mark-applied` with a
   wildcard ARN is refused. LAST line `ROLE-ROUNDTRIP-SELFTEST cases=<k>/7 ok=<True|False>`. Keep waits in the tests at one or two
   seconds so the whole file ends well inside 120 s.

### ACCEPTANCE

<criterion id="CT3c4-AC1" cell_refs="CT-c-4"><invocation>python org/devices/test_role_roundtrip.py</invocation><expect>ROLE-ROUNDTRIP-SELFTEST cases=7/7 ok=True</expect></criterion>
`CT3c4-AC1` -- the check reports success only when the request is answered, the create succeeds, the unnamed pass is refused and the
IAM write is refused; each of the four failure arms turns `ok` false.

<criterion id="CT3c4-AC2" cell_refs="CT-c-4"><invocation>python org/devices/test_role_request.py</invocation><expect>ROLE-REQUEST cases=10/10 ok=True</expect></criterion>
`CT3c4-AC2` -- the control: CT-c-2's ten cases still hold with the two new verbs and the answer-file read in place.

<expected_criteria>CT3c4-AC1,CT3c4-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No AWS call of any kind, no live bus send, no push, no role, no function.** Every AWS call in your tests goes to the fake command.
- No non-ASCII in any file you write.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
org/devices/role_request.py
org/devices/role_roundtrip_check.py
org/devices/test_role_roundtrip.py
org/devices/test_role_request.py
org/standards/ROLE_REQUEST.schema.json
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `org/devices/DEVICES.json`, `.tools/agentbus-sqs.sh`, `.tools/aws`,
`infra/aws/terraform/nfra-ctlpln-identity/tests/render_passrole.py`, `org/devices/role_requests/`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round3.md</decomp_doc> (round 3), cell `CT-c-4`.
<owned_cells>CT-c-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT3c4-AC1, CT3c4-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~4/NFRA_CTLPLN.TO-CT-c-4.role-roundtrip-check.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT3c4-AC1,CT3c4-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the exact command line a Dell runs; the exact `mark-applied` line the laptop runs; the two names the laptop
removes afterwards; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE at the worker (no AWS call); the live run's refusals (steps 4 and 5) are the IAM read, taken by the issuer at the close.
comp-adversary: RUN -- a check that passes without discriminating (four failure arms in AC1, each turning ok false); a Dell marking its own request applied (mark-applied refuses a non-control-plane device; answers live in the laptop's directory; one-writer stage 12); a wildcard role answer (refused); BLIND: the live run itself -- a fake AWS command cannot show the real policy's behaviour; the issuer's one real run at the close does.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.8 @6df8d231f4 ADDENDUM v0.8 C-ROLE-REQUEST (c); CTO msg 105999; decomposition round 3. Base dry-run at the cut:
CT3c4-AC1 base FAIL as expected (no file); CT3c4-AC2 is a control and reads PASS only after CT-c-2 merges (FAIL at this base: the file
does not exist yet -- stated, not hidden).
