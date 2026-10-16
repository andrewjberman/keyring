# TO-AR-tz-61 -- FWD-5 acceptance tests (red): the client notice goes to the ticket firm's contact, never to a body address (AR-tz-61, round 47, workstream ~TX)

<to_id>IRPT_ANLREQ.TO-AR-tz-61</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~221</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>47</round>
<workstream>~TX</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~TX (gates and tests) | **Decomp cell:** `AR-tz-61` (`decompositions/IRPT_ANLREQ_DECOMP_R47_TX.md`) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-tz-61`: "FWD-5 acceptance tests (red): the client notice goes to the ticket firm's contact, never to a body address." A TEST cell: you add ONE new test file and edit no other file. The CTO ruled the four cross-firm admissions that round 45 found in the ticket service (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md`, ADDENDUM 7), `2.0.0_SA_COO~V2` builds the fixes, and these tests are the ACCEPTANCE of fix 1: red before the fix, green after.

**Contract rule 1 (V2 round 19, `R19-nr-1`).** Env `CLIENT_NOTICE_CONTACT_MAP` is JSON `{"<firm id>": ["<address>", ...]}` (default `{}`; malformed = `{}` and a log line). The client notice's recipient for a ticket is derived ONLY from `map[ticket.requester.firm]`: if the stored `requester.email` (stripped, lower-cased) is IN that list it is the recipient; otherwise the FIRST address of the list is, and the body value is ignored and logged as `WE_CLIENT_RECIPIENT_IGNORED firm=<f> to_digest=<digest of the ignored address>` (never the address itself). An absent firm or an empty list: NO send, and a log line `WE_CLIENT_NO_CONTACT firm=<f>`. `requester.email` is still STORED as today. Today the service sends the notice to the body address (`infra/aws/lambda/ticket_center/lambda_function.py` `_client_recipients`, about line 1182 to 1210, and `create_ticket` about line 1373).

**Tests to write (each named `test_cross_firm_<what>`):** (1) a ticket of firm-a whose body `requester.email` is `attacker@example.invalid` and a map `{"firm-a": ["contact-a@example.invalid"]}`: the notice's only recipient is `contact-a@example.invalid` and the attacker address appears in no send and in no log line (RED); (2) the log carries `WE_CLIENT_RECIPIENT_IGNORED` and `firm=firm-a` but not the ignored address (RED); (3) a ticket of firm-a whose `requester.email` IS in the list: that address is the recipient (control, passes today); (4) a firm absent from the map, an empty list, and a malformed map each send NOTHING and log `WE_CLIENT_NO_CONTACT` (RED); (5) the ticket STORES the body `requester.email` unchanged (control, passes today).

**Harness to copy:** `infra/aws/lambda/ticket_center/tests/test_client_notify.py` (it loads `test_authz_matrix.py` as the harness: `FakeTable`, `ev`, the principals, and how a send is captured) and `infra/aws/lambda/ticket_center/tests/test_client_mail_digest.py`.

**Environment:** Set `CLIENT_NOTICE_CONTACT_MAP` in `os.environ` BEFORE the module is loaded through the harness (the V2 cell may read it at import or at call time; set the env first, load the module fresh, and also set the module attribute if one by that name exists), and restore the environment after each test.

**How to write the tests.** Open the harness files named below (they hold the table doubles, the caller principals and the way the ticket service module is loaded) and copy that construction in your new file. Use plain synthetic names (`firm-a`, `firm-b`, `firm-c`, addresses ending `@example.invalid`); no real client, firm or person name, no credential. Name EVERY test function `test_cross_firm_<what>`; the check refuses any other test name. Each contract rule below is an ACCEPTANCE test of a fix that `2.0.0_SA_COO~V2` is building as TCKT_VNEXT round 19 (contract `org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R19.md`): at your base the fix is NOT in the code, so the tests that assert the NEW behaviour FAIL today (red) and the tests that assert the unchanged behaviour (a control per rule) PASS today. The check requires at least the stated number of failures and no collection or setup error: a red test must fail on an assertion about the behaviour, never on an import or a typo. Do NOT edit the code under test and do NOT make a red test pass by changing it. The tests turn green when V2's release lands; you do not wait for it.

**File you create (the only source-tree file you may write):**

infra/aws/lambda/ticket_center/tests/test_cross_firm_notice_recipient.py

**Run it** from your worktree root with `python -m pytest -q infra/aws/lambda/ticket_center/tests/test_cross_firm_notice_recipient.py`: the RED tests must fail on an assertion about the behaviour, the controls must pass. A package the sparse cone lacks: widen nothing, file a `BLOCKING` surprise row naming the folder (`IRPT_ANLREQ-D2-W221-S<k>`, next unused) and stop on that test.

### ACCEPTANCE

<criterion id="AR61-tz-AC1" cell_refs="AR-tz-61"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py red 3 infra/aws/lambda/ticket_center/tests/test_cross_firm_notice_recipient.py</invocation><expect>R46-RED-OK</expect></criterion>
`AR61-tz-AC1` -- the file exists, every test function is named `test_cross_firm_*`, at least 3 test(s) fail now and none errors out at collection or setup. Dry-run at box/dell2 3086b5fe82: `R46-RED-FAIL absent: ...` -- FAIL as expected. The checker's `--self-test` (green pair plus four mutants refused, red mode plus three mutants refused) reads `R46-SELFTEST-OK`.

<expected_criteria>AR61-tz-AC1</expected_criteria>

## BOUNDS

- **Grant.** The test file listed, this order's file, your deliverables folder, the surprise channel. You edit NO code under test and NO other test.
- **No network, no AWS, no secret, no deploy.** Doubles only.
- **Refusal clause.** If a cited line is not what the contract says, write the test for the contract and file a surprise row; if the harness cannot build a case, file the `BLOCKING` row and stop on that test.
- **No alarms, monitors or notifications.** A refusal is a test.

<paths>
infra/aws/lambda/ticket_center/tests/test_cross_firm_notice_recipient.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ. The checker `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R46_CHECKS/r46_checks.py` is in your cone.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R47_TX.md</decomp_doc> (round 47, workstream ~TX), cell `AR-tz-61`.
<owned_cells>AR-tz-61</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: AR61-tz-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~221/IRPT_ANLREQ.TO-AR-tz-61.fwd5-notice-recipient-acceptance-tests.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR61-tz-AC1` BEFORE the flip. Commit the test file first, then pin.
</proof_of_spec>

**REPORT:** the test file, the count failing and passing, for each RED test the one assertion that fails, for each control that it passes, the check line, commits.

---

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a new test file only; no source file, edge or consumer changes. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no permission change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-routes and comp-cache: DECLARED-NOT-APPLICABLE.
comp-adversary: RUN -- `comp-adversary compose` on this order at read-vintage HEAD: the neighborhood is the decomposition only, 0 unproven dependencies; the only cited paths it flags GONE are the files this order creates and its proof instance. Traps named for the worker: a red test that fails on an import or a typo instead of the behaviour; a control that is not run against the same fixture as its red twin; a test that mocks the very check it claims to prove; making a red test pass by editing the code under test; a register parse that hard-codes an absolute path.
</preflight>

- Cut on the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FOUR_LANES_END_TO_END_20261015.md` ADDENDUM 7 (msg 8834, row IRPT_ANLREQ-D2-S134): "your FWD-5 tests are the acceptance (red now, green after). Next issuance keeps fan-out at 4". Risk WORLD only because the gate's path floor (`<paths>` under `infra/`, spine v3.19 L6) admits no lower class: the work is one new test file and no deploy, no AWS call, no source edit.
- Base: `AR61-tz-AC1` FAIL as expected (`R46-RED-FAIL absent`) at box/dell2 3086b5fe82, run by the issuer before the cut.
