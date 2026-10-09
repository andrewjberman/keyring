# TO-AR-t-11 -- the READY message reaches the commentary Lambda (FWD-1 hop 4b, interface I3)

<to_id>IRPT_ANLREQ.TO-AR-t-11</to_id>
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

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~T (commentary) | **Decomp cell:** `AR-t-11` (`decompositions/IRPT_ANLREQ_DECOMP_R1.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AR-t-11`: "I3's queue and its subscription to the commentary Lambda; one READY yields exactly one commentary run." Interface I3 (the
decomposition's interface table): ONE closed message `queue_message("analysis_ready", {"tenant", "request_id"})`, sent once on READY by the
resident (~G2's cell `AR-g-11`). The consumer reads `ticket_id` and the report from the records. Work in your worktree; every path is relative to
its root.

Today the commentary Lambda (`data/transcripts/scripts/commentary/lambda_handler.py`, `entry.py`) expects a DynamoDB-stream-shaped READY record
(`eventName`, `NewImage.ref.request_ref` ...; `org/standards/NFRA_TRNSPT_READY_EVENT_CONTRACT.json`), and `infra/aws/terraform/transcripts/commentary.tf`
has no event source. I3 supersedes the stream for this journey.

**Build:**
1. `commentary.tf`: an SQS queue for `analysis_ready` plus its DLQ, both named by `lib/opal_naming.py name()` (record each builder call in
   `data/transcripts/scripts/commentary/NAMES.json`, read by the tf as the existing names are -- never typed; a builder refusal is a row, see
   BOUNDS); an `aws_lambda_event_source_mapping` from that queue to the commentary Lambda with `batch_size = 1`; the role gets
   `sqs:ReceiveMessage`, `sqs:DeleteMessage`, `sqs:GetQueueAttributes` on that queue only. Producer access (the resident's role SendMessage) is a
   queue-policy statement whose principal is read from the IRPT remote state, as `commentary.tf` already reads the irpt core state; if the
   resident role is not in any remote state you can cite, leave the queue policy out and file the row.
2. `lambda_handler.py`: accept an SQS event. For each record, parse the body, REBUILD it with
   `queue_message("analysis_ready", {"tenant": t, "request_id": r})` from `infra/aws/lambda/investor-reporting/_keys/keys.py:551` and require
   byte equality (the same rule as `resident_worker.py:584` for `analysis_generate`); refuse any other shape or extra field by name. Convert an
   admitted message to the entry's READY shape (`tenant`, `ref.request_ref = request_id`, `ref.report_kind = "ANALYSIS"`) and run the existing
   pipeline once. If `keys.py` cannot be imported in the commentary package, vendor nothing: import it by path the way the IRPT code does, or
   file the row.
3. `data/transcripts/scripts/tests/test_commentary_ready_queue.py` (new, LOCAL, fakes only): `test_ready_message_admitted_once` (one SQS
   record -> exactly one entry run with that tenant and request_ref); `test_malformed_or_extra_field_refused` (an extra key, a wrong kind, a
   free-text value -> refused, no entry run); `test_tf_subscribes_lambda_to_ready_queue` (commentary.tf holds an event source mapping on the
   analysis_ready queue to the commentary function with batch_size 1, names read from NAMES.json). Keep every `test_commentary_*.py` green.

### ACCEPTANCE

<criterion id="AR11-t-AC1" cell_refs="AR-t-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_ANLREQ_T2/R1_CHECKS/ar1_t2_checks.py t11</invocation><expect>AR1-T11-OK</expect></criterion>
`AR11-t-AC1` -- the three named tests pass and the file is green.

<expected_criteria>AR11-t-AC1</expected_criteria>

Dry-run at the base (box/dell2 c5d73485ca): `AR1-T11-FAIL absent: data/transcripts/scripts/tests/test_commentary_ready_queue.py` -- FAIL as
expected.

## BOUNDS

- **Grant.** The paths below, this order's file, your deliverables folder.
- **WORLD by path floor, LOCAL in act.** No AWS call, plan or apply; fakes only.
- **Refusal clause.** A builder refusal, an unimportable `keys.py`, or a producer role with no citable source: leave that piece out, keep the
  rest, file a surprise row (`IRPT_ANLREQ-D2-W41-S<k>`, next unused across every document under
  `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/`). Never type a name or ARN.

<paths>
infra/aws/terraform/transcripts/commentary.tf
data/transcripts/scripts/commentary/lambda_handler.py
data/transcripts/scripts/commentary/entry.py
data/transcripts/scripts/commentary/NAMES.json
data/transcripts/scripts/tests/test_commentary_ready_queue.py
data/transcripts/scripts/tests/test_commentary_lambda.py
data/transcripts/scripts/tests/test_commentary_live_ports.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention). Everything else named here you READ.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> (round 1), cell `AR-t-11`.
<owned_cells>AR-t-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR11-t-AC1. Instance at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~41/IRPT_ANLREQ.TO-AR-t-11.ready-queue-to-commentary.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR11-t-AC1` BEFORE the flip. Commit code first, then pin each artifact to a
commit that contains it.
</proof_of_spec>

**REPORT:** the queue and DLQ names with their builder calls, the mapping, the role and queue-policy statements, the parse rule, the test names,
the check line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the trigger is a queue message per READY, no schedule.
comp-iam: RUN -- 1 role read (commentary.tf :51-95 at 9bd5c1f591); adds 3 SQS consume actions on one queue and one producer statement on the queue policy.
comp-adversary: RUN -- 4 sources read (I3 in the decomposition, keys.py:551-579, resident_worker.py:584, lambda_handler.py); BLIND to ~G2's sender (AR-g-11, in flight). Traps: a lax parse admitting free text, two runs per READY (batch size 1 + one record -> one run), a typed queue name; the face fixes each.
lane: commentary workstream ~T (decomposition workstream table): commentary/*, its Lambda, commentary.tf.
</preflight>

Source: CTO msg 2460; IRPT_ANLREQ decomposition round 1 cell AR-t-11 and interface I3.
