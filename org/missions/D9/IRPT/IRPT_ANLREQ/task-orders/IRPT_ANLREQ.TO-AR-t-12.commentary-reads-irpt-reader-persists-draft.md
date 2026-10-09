# TO-AR-t-12 -- the commentary reads through IRPT's svc-commentary reader, persists ONE DRAFT, sends I4 (FWD-1 hop 6)

<to_id>IRPT_ANLREQ.TO-AR-t-12</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~41</issued_to>
<issued_by>2.0.0_SA_COO~T2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~T</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~T (commentary) | **Decomp cell:** `AR-t-12` (`decompositions/IRPT_ANLREQ_DECOMP_R1.md`) |
**outcome_ref:** FWD-1, FWD-3 | **depends_on:** IRPT_ANLREQ.TO-AR-t-11 (same files; run it first)

---

## WORKER FACE

### THE CELL

`AR-t-12`: the drafter reads the READY request's data tenant-bound through IRPT (abstract fields only, C-KIMI), persists ONE DRAFT commentary,
then sends I4 = `queue_message("commentary_ready", {"tenant", "request_id"})`. CTO ruling msg 2341 / 2460: the read goes ONLY through IRPT's
svc-commentary reader; the commentary role holds no direct `dynamodb:GetItem`, `kms:Decrypt` or `s3:GetObject*` on IRPT data.

**The reader (landed, ~P2 msg 2404):** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~197/IB95-3_svc_commentary_surface.json`
-- direct-invoke Lambda named by `name('irpt', None, 'commentary-composition-read', 'lambda')`; request `{tenant, request_ref}` and nothing else;
response `{status:"OK", tenant, request_ref, composition, sha256, byte_length, redacted_count}` or `{status:"REFUSED", reason}`; caller IAM
= `lambda:InvokeFunction` via IRPT's `irpt-commentary-composition-invoke-policy`, attached to the commentary role "from the transcripts root".

**Issuer ruling (inside this workstream):** the decomposition's cell text names "AnalysisReport v2" surfaces; the only reader that exists is the
REQUEST_COMPOSITION one above, and the drafter's abstract request is built from the composition today (`entry.py:142-167`). This cell wires the
composition reader; report-level surfaces are carried to round 2 as enrichment.

**Build:**
1. `lambda_handler.py`: replace the `COMPOSITION_BUCKET`/`COMPOSITION_KEY_PREFIX` reader with a port that invokes the reader Lambda
   (`COMPOSITION_READ_FUNCTION` env, value = the builder call above recorded in `NAMES.json`, read by the tf) with exactly `{tenant, request_ref}`;
   OK -> the composition (verify `sha256` is a 64-hex string; any other status -> the record lands `failed` at the composition stage with the reason).
   `entry.py`: call the reader with the READY `tenant` and `request_ref`; drop the `owner.get("firm_id")` fallback (`entry.py:183`) so `firm`
   is the tenant only and `owner` is never read.
2. Persist ONE DRAFT per (tenant, request_id) through an injected `persist_draft(tenant, request_id, draft) -> commentary_ref` port; a second
   READY for the same pair finds the existing draft and does NOT call the model again. The live port raises `NO_COMMENTARY_STORE` in this
   cell. AMENDMENT 1 (issuer, 2026-10-09 ~04:5xZ): the driver ruled the store (decomposition AMENDMENT 1 row I4s @8412208d47, ~Y2 msg 2505):
   family `ANALYSIS_COMMENTARY` through `ArtifactRepository.put` under a new additive policy row `irpt-anlreq-x10-v1`, with `commentary_ref`
   set once on the acceptance record. That write surface is a later cell of this workstream; here, name the port's contract after it
   (`persist_draft(tenant, request_id, draft) -> {"artifact_id", "sha256", "version_id"}`) and keep the live port raising. After a successful persist, send
   `queue_message("commentary_ready", {"tenant": t, "request_id": r})` exactly once through an injected `send` port.
3. `commentary.tf`: REMOVE `DecryptWithTheIrptKey`, the irpt core remote-state data source if nothing else uses it, the composition env names
   and the conditional `ReadTheRetainedComposition`; ADD the `COMPOSITION_READ_FUNCTION` env and an `aws_iam_role_policy_attachment` of IRPT's
   invoke policy, its ARN resolved by a data source on the builder name (never typed). `NAMES.json`: replace the `composition` key with
   `composition_read` (builder call + name).
3a. AMENDMENT 2 (issuer, disarms row IRPT_ANLREQ-D2-W41-S1): `infra/aws/lambda/transcripts-pull/build.sh` copies, ADDITIVELY, exactly
   what `lambda_handler.admit_ready_message` loads by path -- `infra/aws/lambda/investor-reporting/_keys/keys.py` and the firm registry file it
   reads (measure the path from `keys.py`'s `firm_tokens()` / `_check_tenant`, e.g. `data/firm_registry.json`) -- into the same relative paths
   under `dist/pkg/`, so the deployed zip admits a valid `analysis_ready` message. Nothing else in the build changes. Add to the test file a
   `test_build_packages_keys_module` that runs `bash infra/aws/lambda/transcripts-pull/build.sh` (or reads the script's copy lines if bash is
   unavailable) and asserts both files are in the zip.
3b. AMENDMENT 3 (issuer, on the driver's decomposition AMENDMENT 4 @e124f00985, ~Y2 msg 2543): `commentary.tf` adds the `commentary_ready`
   queue and its DLQ beside `analysis_ready`, named by `name()` exactly as AR-t-11 named its pair (record both in `NAMES.json`); the commentary
   role gets `sqs:SendMessage` on it; its queue policy lets the resident role (the same `runner_role_arn` remote-state output AR-t-11 used)
   ReceiveMessage, DeleteMessage and GetQueueAttributes. The live `send` port sends I4 to that queue (`COMMENTARY_READY_QUEUE_URL` env from the
   tf). ~G2 wires the resident's poll. Extend `test_draft_persisted_then_one_commentary_ready` or the AR-t-11 tf test to assert the queue, the
   send grant and the receive policy exist.
4. `data/transcripts/scripts/tests/test_commentary_composition_port.py` (new, fakes only):
   `test_live_port_invokes_irpt_reader_with_tenant_and_request_ref` (a fake lambda client receives exactly those two keys and the builder name);
   `test_owner_never_read` (a composition carrying `owner` yields no owner value anywhere in the request or ticket context; firm == tenant);
   `test_draft_persisted_then_one_commentary_ready` (one persist, then exactly one send; a second READY for the same pair makes no model call and
   no second send). Update `test_commentary_live_ports.py` for the removed and added names. Keep every `test_commentary_*.py` green.

### AMENDMENT 4 (issuer, 2026-10-09 ~05:5xZ) -- RE-OPENED: cell AR-t-13, the DRAFT store (one round-1 issuance per workstream: the pipeline gate
refuses a new order file, so the cell rides here). Read `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IRPT_ANLREQ_SVC_COMMENTARY_ONE_NAMED_WRITER_20261009.md`
@ca645f8410 in full; it binds. Your first build (AC1) is merged @9eb1ee6eba and stays as is.

5. `infra/aws/lambda/investor-reporting/reports/repository.py`: a `SERVICE_WRITERS` table with exactly ONE entry
   `{"svc-commentary": frozenset({"ANALYSIS_COMMENTARY"})}`; `put()` admits a service principal ONLY through it, tenant-bound (`firm_id ==
   owner.firm_id`, never `global`/`opal-capital`), logical id = `request_id`, and refuses a second put on the same logical id (never overwrites).
   Every other service subject stays read-only; every other family stays refused to a service subject. Driver AMENDMENT 5 (~Y2 msg 2606): ONE
   `SERVICE_READERS` entry for the `package_principal` named by ~V2's AR-v-12, family `ANALYSIS_COMMENTARY` only; if AR-v-12 has not named it at
   your base, leave it out and file the row.
6. `infra/logic/registry/reporting_policies.json`: ONE additive policy row `irpt-anlreq-x10-v1` registering family `ANALYSIS_COMMENTARY` (copy
   the shape of an existing row such as `irpt-ycdgen-research-v1`; edit no other row); wire it as `reports/composition.py` wires
   `additional_policy_revisions` where the store builds its repositories.
7. `infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py` (new; mirror ~P2's `reports/commentary_composition.py`): a
   direct-invoke handler, request keys refused by name beyond these: `{"op":"put","tenant","request_id","draft"}` ->
   `{status:"OK", commentary_ref:{artifact_id, sha256, version_id}}`; `{"op":"get_ref","tenant","request_id"}` -> `{status:"OK", commentary_ref|null}`;
   else `{status:"REFUSED", reason}`. The SERVER builds `service_principal("svc-commentary", <tenant from the request record analysis#<request_id>#1>)`;
   a body tenant is never trusted. After a successful put, set `commentary_ref` ONCE on that request record by a conditional update
   (`attribute_not_exists(commentary_ref)`) in this module; do not edit `ycharts/generate/acceptance.py`.
8. `infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf` (new, DESIRED; mirror `commentary_composition.tf`): the function
   (`lib/opal_naming.py name('irpt', None, 'commentary-draft-store', 'lambda')`), its role (scoped to the ANALYSIS_COMMENTARY prefix of the served
   firms and the requests table), and an invoke policy (`name('irpt', None, 'commentary-draft-store-invoke', 'policy')`) for the commentary role.
   Register the zip in `infra/aws/lambda/ci/lambda-source-map.json` as the reader is registered.
9. Commentary side: the live `persist_draft` invokes the store with `op: put`, the live `existing_draft` with `op: get_ref`; env
   `DRAFT_STORE_FUNCTION` from `NAMES.json` (`draft_store` key, builder call recorded); `commentary.tf` attaches the store's invoke policy by a data
   source on the builder name; the commentary role gains no S3 or KMS grant. Driver AMENDMENT 6 (@27d4996a37, ~Y2 msg 2628): for an
   analysis_ready run the drafter posts NO separate svc-commentary ticket (the DRAFT reaches the request's ticket only as commentary_ref); the mail
   uses of `ticket_client` do not move.
10. Tests, `infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store.py` (new, fakes only), the CTO ruling's four, one
   each: `test_other_service_subject_refused`, `test_other_family_refused`, `test_second_put_same_request_refused`, `test_body_tenant_ignored`; plus
   a happy path. Keep every `test_commentary_*.py` and `infra/aws/lambda/investor-reporting/reports/tests` green.

### AMENDMENT 5 (issuer, 2026-10-09 ~06:3xZ) -- disposes rows IRPT_ANLREQ-D2-W41-S11, -S6, -S7

- **S11 (cell id):** the decomposition holds no `AR-t-13` row; the store is the decomposition's own `AR-t-12` text ("persists ONE DRAFT
  commentary") realized, so criterion `AR13-t-AC1` now cites `cell_refs="AR-t-12"`. The draft-store work keeps its AMENDMENT 4 steps 5-10.
11. **S6 (live write path):** `infra/aws/lambda/investor-reporting/reports/retention.py` `_allow` (:90-99) admits a service subject only to a
   liveness read, so `reserve()` (:208-210) denies the one named writer on the live path through the retained repositories. Admit it there
   EXACTLY as `repository.py`'s `SERVICE_WRITERS` does: `svc-commentary`, family `ANALYSIS_COMMENTARY`, on `reserve` only, tenant-bound
   (`firm == owner.firm_id`, never `global`/`opal-capital`); every other act and subject is refused as today. Test, in
   `test_commentary_draft_store.py`: `test_live_retained_put_admits_the_named_writer` (build the repositories the store Lambda builds, with
   the retained RetentionPolicy, and assert one put succeeds and a second is refused), and keep the four refusals green.
12. **S7 (package reader):** add the AMENDMENT 5 (driver) `SERVICE_READERS` entry for the `package_principal` AR-v-12 named (the worker
   measured `svc-irpt-packager`; cite the line where AR-v-12 names it), family `ANALYSIS_COMMENTARY` only, and update the pin at
   `reports/tests/test_svc_commentary.py:199` to the new two-entry map (that edit only).
13. **S8:** `test_commentary_ready_queue.py` may be updated where it pins stage `ticket` for a queue run, so a store-backed queue run ends
   `draft_stored` (driver AMENDMENT 6); a run with no store ports keeps today's behavior.

### ACCEPTANCE

### AMENDMENT 6 (issuer, 2026-10-09 ~13:1xZ) -- RE-OPENED: row IRPT_BCKEND-D2-S50 (@e091bd6984), the draft store's log group declared twice

`commentary_draft_store.tf` creates `aws_cloudwatch_log_group.commentary_draft_store` (`local.cds_log_group`), and the `yang-lambda` module
creates the same group (`modules/yang-lambda/main.tf` `aws_cloudwatch_log_group.lambda`, `retention_in_days = var.log_retention_days`). The
first apply would fail one create with ResourceAlreadyExistsException and land in part. The fix is the CTO's for the same defect, row D2-S41
(IB-pr-391 CTO half AMENDMENT 1):
13. Remove the root `aws_cloudwatch_log_group.commentary_draft_store` and its entry in the module's `depends_on`; pass `log_retention_days = 14`
    to `module "irpt_commentary_draft_store"`. Keep `local.cds_log_group` (the role's S5 statement still scopes to that group's name). Change
    nothing else.
14. New `infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store_tf.py` (parses the .tf text):
    `test_log_group_declared_once` (no `aws_cloudwatch_log_group` resource in commentary_draft_store.tf) and `test_module_carries_retention`
    (the module block sets `log_retention_days = 14`).
Base: box/dell2 at this amendment, where `ar1_t2_checks.py t13lg` reads `AR1-T13LG-FAIL absent`.

<criterion id="AR13-t-AC2" cell_refs="AR-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R1_CHECKS/ar1_t2_checks.py t13lg</invocation><expect>AR1-T13LG-OK</expect></criterion>

<criterion id="AR12-t-AC1" cell_refs="AR-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R1_CHECKS/ar1_t2_checks.py t12</invocation><expect>AR1-T12-OK</expect></criterion>
`AR12-t-AC1` -- the three named tests pass, the file is green, and `DecryptWithTheIrptKey` is gone from commentary.tf.

<criterion id="AR13-t-AC1" cell_refs="AR-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R1_CHECKS/ar1_t2_checks.py t13</invocation><expect>AR1-T13-OK</expect></criterion>
`AR13-t-AC1` -- the four named refusal tests pass and the store test file is green (dry-run at box/dell2 29125b907d: `AR1-T13-FAIL absent`).

<expected_criteria>AR12-t-AC1 AR13-t-AC1 AR13-t-AC2</expected_criteria>

Dry-run at the base (box/dell2 c5d73485ca): `AR1-T12-FAIL absent: data/transcripts/scripts/tests/test_commentary_composition_port.py` -- FAIL
as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor, LOCAL in act.** No AWS call, plan or apply, no model call; fakes only.
- **Refusal clause.** A builder refusal or an unresolvable policy ARN: leave that piece out, keep the rest, file a surprise row
  (`IRPT_ANLREQ-D2-W41-S<k>`, next unused across every document under `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/`). Never type a name or ARN.

<paths>
infra/aws/lambda/transcripts-pull/build.sh
infra/aws/terraform/transcripts/commentary.tf
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/commentary/entry.py
data/transcripts/scripts/commentary/NAMES.json
data/transcripts/scripts/tests/test_commentary_composition_port.py
data/transcripts/scripts/tests/test_commentary_live_ports.py
data/transcripts/scripts/tests/test_commentary_entry.py
data/transcripts/scripts/tests/test_commentary_lambda.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/reports/repository.py
infra/aws/lambda/investor-reporting/reports/commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store.py
infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store_tf.py
infra/aws/lambda/investor-reporting/reports/tests/test_repository.py
infra/logic/registry/reporting_policies.json
infra/aws/terraform/investor-reporting/export/commentary_draft_store.tf
infra/aws/lambda/ci/lambda-source-map.json
data/transcripts/scripts/commentary/ticket_client.py
infra/aws/lambda/investor-reporting/reports/retention.py
infra/aws/lambda/investor-reporting/reports/tests/test_svc_commentary.py
data/transcripts/scripts/tests/test_commentary_ready_queue.py
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> (round 1), cell `AR-t-12`.
<owned_cells>AR-t-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR12-t-AC1, AR13-t-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~41/IRPT_ANLREQ.TO-AR-t-12.commentary-reads-irpt-reader-persists-draft.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR12-t-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that contains it.
</proof_of_spec>

**REPORT:** the reader port and its env, the removed and added tf statements with their sources, the persist and send rule, the test names, the
check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- driven by AR-t-11's queue.
comp-iam: RUN -- 1 role read (commentary.tf at 9bd5c1f591: 5 statements + 1 grant); removes DecryptWithTheIrptKey and the composition read; adds one attachment of IRPT's invoke policy (InvokeFunction on one function).
comp-adversary: RUN -- 4 sources read (the surface file, entry.py :50/:138-183, lambda_handler.py :45-90, commentary.tf); BLIND to the commentary store and the packager's read of it (I4's consumer, ~G2). Traps: owner leaking via the firm fallback, two model calls per READY, a direct IRPT read surviving in the role, an invented store; the face fixes each.
lane: commentary workstream ~T: commentary/*, its Lambda, commentary.tf.
</preflight>

Source: CTO msgs 2341, 2460; ~P2 msg 2404; IRPT_ANLREQ decomposition round 1 cell AR-t-12 and interface I4.
