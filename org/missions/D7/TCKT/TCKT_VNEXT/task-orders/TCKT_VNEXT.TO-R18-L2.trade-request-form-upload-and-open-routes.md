# TO TCKT_VNEXT.TO-R18-L2 -- BUILD the trade_request form attachment: the upload-presign route, the open-presign route and the validated attachment, in the ticket service (source and tests only)

<to_id>TCKT_VNEXT.TO-R18-L2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~41</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply; the worker deploys, applies and invokes NOTHING)
**Decomp cell:** `R18-tf-2` (`decompositions/TCKT_VNEXT_DECOMP_R18.md`) | **outcome_ref:** FWD-10 | **depends_on:** `R18-mt-1` (same slot, same file: you start it after `TO-R18-L1` is terminal and merged into your branch)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~41` (the same worker, continued; your worktree is `C:/dev/wk-tckt-vnext-41`, branch `wk-TCKT_VNEXT-41`).
Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~41 <0.9.0_WK_TCKT_VNEXT~41@opal.agent>" -F <msgfile> -- <paths>`.
The rules of `TO-R18-L1`'s face stand: message files by the Write tool, rows `TCKT_VNEXT-D2-W41-S<k>` (next free `<k>`), `surfaced_at` =
`date -u +%FT%TZ`, each `.py` through `bash .tools/commit-gate.sh`, no non-ASCII, and NO live call of any kind (no AWS, no network, no
mail, no deploy, no apply; the S3 client is a fake in every test). A `controls.mutant` MUST be a mutant that FIRES.

### THE CELL (`R18-tf-2`, inlined) -- BUILD ONLY.

*PRD v0.6 C-TRADE-REQUEST and C-ATTACH: an Opal staff person files a Trade Request by choosing a firm and uploading the trade request
form (PDF, XLSX or CSV); the OPEN ticket carries the form as an attachment opened from the ticket page. The form's bytes live in an
S3 object at a firm-tenant key; the ticket stores the REFERENCE only; the upload and the open are by short-lived presigned URLs the
ticket API issues after the firm fence. No trade is sent anywhere. The bucket and the key prefix are CONFIG, set by environment
variables another cell writes into Terraform: `TICKET_ATTACH_BUCKET` and `TICKET_ATTACH_KEY_TEMPLATE` (a string with `{firm}` exactly once, ending
in `/`, for example `portal/{firm}/bronze/ticket-attachments/trade-form/`). The firm segment is in the MIDDLE of a real key, so there is no
fixed prefix: a firm's prefix is `KEY_TEMPLATE.format(firm=<firm>)`.*

The wire contract is `org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md`, section WIRE CONTRACT, items 2 and 3 and the
`trade_request` paragraph. Read it first, then in `infra/aws/lambda/ticket_center/lambda_function.py`: `TYPE_DEFINITIONS` (about 88),
`_validate_answers` (about 704), `_validate_attachment` (about 753; its comment says a second kind is "unreachable until defined"),
`_create_firm_allowed` (about 367), `create_ticket` (about 1218), `get_ticket` (about 1402), `lambda_handler` (about 1889).

1. **The definition.** `trade_request` becomes: questions `firm` (kind `firm`, required) and the old four (`fund`, `weights_as_of`,
   `trade_comments`, `attestations_confirmed`) kept but NOT required; `attachment` = the new kind string `"trade_form"`. The existing
   test `tests/test_trade_request_type.py` pins the old shape: re-pin ONLY what the contract changes (the required flags and the
   attachment), case by case, and list each re-pin with its old and new assertion.
2. **The attachment.** `_validate_attachment` handles kind `trade_form`: the member is exactly `{key, filename, content_type, size}` (no other
   member); `content_type` one of the three types; `size` an int from 1 to 10485760; the filename's extension agrees with the type; `key`
   starts with `TEMPLATE.format(firm=<the ticket's answers.firm>)` (`TEMPLATE` is `os.environ["TICKET_ATTACH_KEY_TEMPLATE"]`, read at call
   time so a test sets it; unset, empty, without exactly one `{firm}` or not ending in `/`: refuse 503 and write nothing; the firm value is
   checked to be a plain id of letters, digits, dash and underscore before it is formatted in). `analysis_upload` behaves exactly as today. CREATE for
   `trade_request` stores the attachment REFERENCE in the row (never bytes) and makes NO engine or network call.
3. **The upload route.** `POST /api/scoped/tickets/attachment-upload` (`attachment_upload_ticket(event)`, `MATRIX` action `ATTACH_UPLOAD`
   permitted to INTERNAL only): body per the contract; `firm` passes `_create_firm_allowed(pc, actor, firm)`; type, size and extension
   checks as step 2; the key is `TEMPLATE.format(firm=firm) + uuid4().hex + "/" + <safe filename>` (the safe name keeps ASCII letters,
   digits, dot, dash and underscore, replaces anything else with `_`, and is at most 100 characters); the response is the contract's. Presign with
   `boto3.client("s3").generate_presigned_url("put_object", Params={"Bucket": os.environ["TICKET_ATTACH_BUCKET"], "Key": key, "ContentType":
   content_type}, ExpiresIn=300)` through a module-level seam (for example `_s3_client()`), so tests replace it; `TICKET_ATTACH_BUCKET`
   unset: 503 and nothing presigned. Nothing is written to the table.
4. **The open route.** `GET /api/scoped/tickets/{ticketId}/attachment` (`attachment_open_ticket(event, tid)`, `MATRIX` action `ATTACH_OPEN`
   permitted exactly as the existing GET action is): the ticket lookup and scope test are `get_ticket`'s (404 for not found or out of
   scope); the ticket must carry an `attachment` whose `key` starts with `TEMPLATE.format(firm=<the ticket's answers.firm>)`, else 404; the response
   is `{"url": <presigned get_object, ExpiresIn=300, ResponseContentDisposition = attachment; filename="<safe filename>">, "filename", "expires_in": 300}`.
5. **Not changed:** `analysis_request`, the package, report, claim, complete and commentary routes; the CLIENT submit path; the meeting
   code of `TO-R18-L1` (merge cleanly: it is in your branch).
6. **Tests.** The new file `tests/test_trade_form_attachment.py`, one named test per case: CREATE with a valid attachment stores the
   reference and returns 201, with no bytes and no engine call; CREATE with a key under ANOTHER firm's prefix is refused; a missing
   attachment is refused; an unknown member, a size of 0 and of 10485761, a `.exe` name, a type and extension that disagree are refused;
   `TICKET_ATTACH_KEY_TEMPLATE` unset, with no `{firm}`, with two, or not ending in `/` refuses 503; the upload route admits an INTERNAL human for a firm in scope and refuses a firm outside it, a
   CLIENT caller and a service subject (403), and a bad type or size (400); the presign is called with exactly the returned key and
   content type and `ExpiresIn` 300; `TICKET_ATTACH_BUCKET` unset is 503 with no presign; the open route returns a presigned URL for a ticket
   in scope and 404 for another firm's ticket, for a ticket with no attachment and for a key outside the firm's prefix; the old
   `analysis_request` cases still pass (run `test_analysis_request.py` and `test_submit_analysis_request.py` and print their counts).
7. **Write `deliverables/0.9.0_WK_TCKT_VNEXT~41/mutant_check_tf2.py`** (AC2) and a short `R18_L2_RECORD.json`: the lines changed, the
   counts, the before-arm (the new tests on the base FAIL), the exact environment variable names the Terraform cell must set, `not_read`.

### ACCEPTANCE

<criterion id="R18L2-AC1" cell_refs="R18-tf-2"><invocation>python -m pytest C:/dev/wk-tckt-vnext-41/infra/aws/lambda/ticket_center/tests/test_trade_form_attachment.py C:/dev/wk-tckt-vnext-41/infra/aws/lambda/ticket_center/tests/test_trade_request_type.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed</expect></criterion>
`R18L2-AC1`: both files pass, every case of step 6 named in a test, no failures or errors. Also run the whole
`infra/aws/lambda/ticket_center/tests/` folder once and record the counts (a drain check; the issuer re-runs it).

<criterion id="R18L2-AC2" cell_refs="R18-tf-2"><invocation>python C:/dev/wk-tckt-vnext-41/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~41/mutant_check_tf2.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R18L2-AC2` (the one mutant that fails): you write `mutant_check_tf2.py`: it copies `lambda_function.py` to a scratch folder OUTSIDE the
product tree with the firm-prefix test on the attachment key removed (so a key under another firm's prefix is admitted), runs the new test
file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R18L2-AC3J" cell_refs="R18-tf-2" judgment="true"/>
`R18L2-AC3J` (judgment, graded at L9, never by you): a firm can only upload to and open from its own prefix, the open route applies the
same fence as the ticket read, the bytes never pass through the Lambda, no trade is sent, and an unset bucket or prefix refuses rather than
guessing.

<expected_criteria>R18L2-AC1 R18L2-AC2 R18L2-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~41/` and this order's file
  (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else, including `infra/aws/terraform/` (routes, environment and the IAM permission are `TO-R18-TR3`) and `lib/opal_naming.py`
  (the bucket and prefix values come from `TO-R18-TR1`; this cell reads them from the environment and imports no naming module).

<paths>
infra/aws/lambda/ticket_center/lambda_function.py
infra/aws/lambda/ticket_center/tests/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md</decomp_doc>
<owned_cells>R18-tf-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~41/TCKT_VNEXT.TO-R18-L2.trade-request-form-upload-and-open-routes.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R18-L2`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R18L2-AC1,R18L2-AC2,R18L2-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- source in a worker worktree; nothing is deployed, applied or invoked. The release is `R18-tf-5` (`TO-R18-REL`).
comp-routes: DECLARED-NOT-APPLICABLE -- the two API route entries are Terraform SOURCE in `TO-R18-TR3`; this cell adds the handlers only. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- the S3 permission on the prefix is Terraform SOURCE in `TO-R18-TR3`; this cell calls S3 only through a faked seam.
comp-adversary: RUN -- by reading C-ATTACH and C-FENCE against this cell; the lens: a key built from the body instead of the verified firm, a presign for a path outside the firm's prefix, an open route with a weaker fence than the ticket read, an unset bucket that falls back to a default, bytes through the Lambda. The cell requires prefix-bound keys, the same fence, config-or-503, and a mutant that fires. NOT seen: the live bucket, its CORS and its policy (the laptop's role request, C-DEPLOY).
</preflight>

---

## RECORD FACE

- Cut on PRD v0.6 @c578883de8 (C-TRADE-REQUEST, C-ATTACH) and the CTO's ruling (b), msg 7818. Second order of slot 41's queue, after `TO-R18-L1`; round 18 chain A. Base: `R18L2-AC1` and `R18L2-AC2` FAIL as expected (no test file, no checker file).
- The old trade questions stay optional so a held engine-path ticket still reads (issuer's ruling inside its own decomposition, no gate limb graded it).
