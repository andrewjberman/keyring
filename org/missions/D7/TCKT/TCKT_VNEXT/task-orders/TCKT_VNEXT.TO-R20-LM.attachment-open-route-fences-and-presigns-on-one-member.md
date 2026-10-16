# TO TCKT_VNEXT.TO-R20-LM -- BUILD the attachment open route's same-member fence: refuse a ticket whose requester firm and answers firm differ, and presign from the fenced member (row C-S11; source and tests only)

<to_id>TCKT_VNEXT.TO-R20-LM</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~49</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a Lambda source path; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `R20-lm-2` (`decompositions/TCKT_VNEXT_DECOMP_R20.md`) | **outcome_ref:** the CTO's rounds 18-19 ruling 5; row `TCKT_VNEXT-C-S11` | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~49`.
- **Worktree:** `C:/dev/wk-tckt-vnext-49` (branch `wk-TCKT_VNEXT-49`), provisioned by the issuer. Work and commit only there, with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~49 <0.9.0_WK_TCKT_VNEXT~49@opal.agent>" -F <msgfile> -- <paths>`. If a `portal`
  folder exists in the worktree it is a separate repository: never touch or stage it.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `TCKT_VNEXT-D2-W49-S<k>` (take the next free `<k>`). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before
  its commit (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every
  non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call of any kind: no AWS, no network, no
  mail, no deploy, no apply, no Terraform (`tests/conftest.py` refuses a real call). **Run NO test file by path (`python <file>`): pytest only, with `-p no:cacheprovider`.** Scratch outside the product tree.

### WHY

The CVO's `ADJUDICATION_v8` row `TCKT_VNEXT-C-S11` (latent, INERT): the attachment open route fences a ticket on `requester.firm` but builds the bucket and the key prefix from `answers.firm`. Today the two cannot differ (create sets `requester.firm` from `answers.firm` and refuses a differing `requester_firm`), so it is safe only by an invariant elsewhere. The CTO's ruling 5 (rounds 18-19 analysis): close it now, cheaply: fence and presign on the SAME member, one test per side.

### THE CELL (`R20-lm-2`, inlined) -- BUILD ONLY. Nothing is deployed, applied or invoked.

In `infra/aws/lambda/ticket_center/lambda_function.py`, `attachment_open_ticket(event, tid)` (read it first, about lines 2105 to 2135; it uses `_resolve_scope`, `_in_profile_scope`, `_PLAIN_FIRM_RE`, `_attach_templates`, `_safe_attach_name`, `_s3_client`):

1. **The fence member.** After the existing ticket lookup and `_in_profile_scope` test, read `req_firm = str((cur.get("requester") or {}).get("firm") or "")` and keep `firm = str((cur.get("answers") or {}).get("firm") or "")`. **If `req_firm` is not equal to `firm`, return the SAME 404 body the function already returns for a ticket that carries no attachment** (`{"error": f"ticket {tid} carries no attachment"}`, status 404): the caller learns nothing about why. The existing checks that follow (`att` is a dict with a string `key`, `firm` matches `_PLAIN_FIRM_RE`) stay.
2. **The presign member.** Build the bucket and the key prefix from `req_firm` (the fenced member), never from a separately read value: after step 1 the two are equal, and the code must read as ONE member (for example `firm = req_firm` after the equality test, and every later use of `firm`). The response shape on success is unchanged.
3. **Nothing else changes.** No other route, no `attachment_upload_ticket`, no `create` path, no `MATRIX`, no scope function.
4. **Tests** in the new file `infra/aws/lambda/ticket_center/tests/test_attachment_open_same_member.py` (copy the style of `tests/test_trade_form_attachment.py`: a fake table and a fake S3 client that records the `Params` of `generate_presigned_url`; no AWS). One named test per case:
   - `test_open_refuses_a_ticket_whose_requester_firm_differs_from_answers_firm`: requester firm `inflection`, answers firm `cottonwood`, the caller scoped to both: status 404, the body equals the no-attachment body, and the fake S3 client was NOT called;
   - `test_open_refuses_a_ticket_with_no_requester_firm`: the requester has no firm: 404, no presign;
   - `test_open_presigns_from_the_fenced_member_when_both_agree`: requester firm and answers firm both `cottonwood`: 200, the presigned `Bucket` is the cottonwood bucket and the `Key` starts with the cottonwood prefix;
   - `test_open_still_refuses_a_caller_outside_the_firms_scope`: a caller scoped to another firm gets the 404 of the existing fence and no presign;
   - `test_open_still_refuses_a_key_outside_the_firms_prefix`: the existing prefix check still answers 404.
5. **Do not change any existing assertion.** If an existing test builds a ticket whose requester firm and answers firm differ and expects 200, STOP and file a BLOCKING row naming it; do not edit it.
6. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~49/mutant_check.py`** (AC2 below) and a short `R20_LM_RECORD.json`: the lines you changed, the test counts, the before-arm (the new tests on the base: the first two cases FAIL), `not_read`.

### ACCEPTANCE

<criterion id="R20LM-AC1" cell_refs="R20-lm-2"><invocation>python -m pytest C:/dev/wk-tckt-vnext-49/infra/aws/lambda/ticket_center/tests/test_attachment_open_same_member.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`R20LM-AC1`: the new test file passes with every case of step 4 named in a test, no failures or errors. Also run the whole `infra/aws/lambda/ticket_center/tests/` folder once and record the counts in your record (a drain check; the issuer re-runs it).

<criterion id="R20LM-AC2" cell_refs="R20-lm-2"><invocation>python C:/dev/wk-tckt-vnext-49/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~49/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R20LM-AC2` (the one mutant that fails): you write `mutant_check.py`: it copies `lambda_function.py` to a scratch folder OUTSIDE the product tree with the equality test of step 1 removed (the route then presigns from a ticket whose two firms differ), runs the new test file against the copy with pytest, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R20LM-AC3J" cell_refs="R20-lm-2" judgment="true"/>
`R20LM-AC3J` (judgment, graded at L9, never by you): the open route fences and presigns on ONE member, refuses a ticket whose requester firm and answers firm differ with the same body as a ticket with no attachment, and nothing else in the function changed.

<expected_criteria>R20LM-AC1 R20LM-AC2 R20LM-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~49/` and this order's file
  (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else, including `infra/aws/terraform/`. Touch ONLY `attachment_open_ticket`.

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R20.md</decomp_doc>
<owned_cells>R20-lm-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~49/TCKT_VNEXT.TO-R20-LM.attachment-open-route-fences-and-presigns-on-one-member.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R20-LM`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R20LM-AC1,R20LM-AC2,R20LM-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source in a worker worktree; nothing is deployed, applied or invoked. The release is a later ticket-service release.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler reads the table and presigns with the client it already uses.
comp-adversary: RUN -- by reading row C-S11, the CTO's ruling 5 and `attachment_open_ticket` against this cell; the lens: a fence that refuses a legitimate ticket (requester firm and answers firm are equal on every ticket the create path writes, so none), a presign from a member the fence did not test, and a response that tells the caller why it was refused (the same 404 body). BLIND to: the deployed function and the live tickets (denominator: 1 route read).
</preflight>

---

## RECORD FACE

- Cut on the CTO's rounds 18-19 analysis (ruling 5, enrichment item 3) in round 20; fan-out 2 of 2 chains, cap 4. Base: `R20LM-AC1` and `R20LM-AC2` FAIL as expected (no test file, no checker file).
