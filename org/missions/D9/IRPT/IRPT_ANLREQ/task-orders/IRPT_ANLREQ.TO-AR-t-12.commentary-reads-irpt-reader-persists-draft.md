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
   READY for the same pair finds the existing draft and does NOT call the model again. The live port raises `NO_COMMENTARY_STORE` until the
   store is fixed (the issuer asks the driver for I4's store; do not invent one). After a successful persist, send
   `queue_message("commentary_ready", {"tenant": t, "request_id": r})` exactly once through an injected `send` port.
3. `commentary.tf`: REMOVE `DecryptWithTheIrptKey`, the irpt core remote-state data source if nothing else uses it, the composition env names
   and the conditional `ReadTheRetainedComposition`; ADD the `COMPOSITION_READ_FUNCTION` env and an `aws_iam_role_policy_attachment` of IRPT's
   invoke policy, its ARN resolved by a data source on the builder name (never typed). `NAMES.json`: replace the `composition` key with
   `composition_read` (builder call + name).
4. `data/transcripts/scripts/tests/test_commentary_composition_port.py` (new, fakes only):
   `test_live_port_invokes_irpt_reader_with_tenant_and_request_ref` (a fake lambda client receives exactly those two keys and the builder name);
   `test_owner_never_read` (a composition carrying `owner` yields no owner value anywhere in the request or ticket context; firm == tenant);
   `test_draft_persisted_then_one_commentary_ready` (one persist, then exactly one send; a second READY for the same pair makes no model call and
   no second send). Update `test_commentary_live_ports.py` for the removed and added names. Keep every `test_commentary_*.py` green.

### ACCEPTANCE

<criterion id="AR12-t-AC1" cell_refs="AR-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R1_CHECKS/ar1_t2_checks.py t12</invocation><expect>AR1-T12-OK</expect></criterion>
`AR12-t-AC1` -- the three named tests pass, the file is green, and `DecryptWithTheIrptKey` is gone from commentary.tf.

<expected_criteria>AR12-t-AC1</expected_criteria>

Dry-run at the base (box/dell2 c5d73485ca): `AR1-T12-FAIL absent: data/transcripts/scripts/tests/test_commentary_composition_port.py` -- FAIL
as expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor, LOCAL in act.** No AWS call, plan or apply, no model call; fakes only.
- **Refusal clause.** A builder refusal or an unresolvable policy ARN: leave that piece out, keep the rest, file a surprise row
  (`IRPT_ANLREQ-D2-W41-S<k>`, next unused across every document under `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/`). Never type a name or ARN.

<paths>
infra/aws/terraform/transcripts/commentary.tf
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/commentary/entry.py
data/transcripts/scripts/commentary/NAMES.json
data/transcripts/scripts/tests/test_commentary_composition_port.py
data/transcripts/scripts/tests/test_commentary_live_ports.py
data/transcripts/scripts/tests/test_commentary_entry.py
data/transcripts/scripts/tests/test_commentary_lambda.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> (round 1), cell `AR-t-12`.
<owned_cells>AR-t-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR12-t-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~41/IRPT_ANLREQ.TO-AR-t-12.commentary-reads-irpt-reader-persists-draft.proof_of_spec.json`,
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
