# NFRA_OPLGTW task order -- `OG-dq-1` -- READ ONLY: who drained `opal-assets-silver-dlq` on 2026-10-09 15:39Z-16:17Z, and what it holds now (E7)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-dq-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-dq-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~57</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- reads only; nothing scheduled is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reads under the operator's own identity; no role or policy changes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is 1.0.0_SA_CTO~Z's round-33 analysis @2672b8d28a row Z-S77 ruling: read-only first; enabling SQS data-event logging is NOT in this cell.
EGRESS CLASS, declared: NONE beyond Opal's own AWS (read APIs).
</preflight>

## 1. THE CELL -- `OG-dq-1` (decomposition addendum R3-T.42, E7)

Row Z-S77: six held RPS messages left the shared converter DLQ `opal-assets-silver-dlq` between 15:39Z and 16:17Z on
2026-10-09, by an unknown actor. It was not OG-bh-1 (that driver reads depth only), and not the 12:15Z sweep (outside the
window). A second, unknown DLQ consumer would silently eat other masters' failures. Name it from the planes that exist:

1. **CloudTrail** (`lookup-events`, the window +-30 min): every management event naming the queue (`PurgeQueue`,
   `SetQueueAttributes`, `StartMessageMoveTask`, `ListMessageMoveTasks`, event-source-mapping calls). Record the events
   and the count read. Data events (`ReceiveMessage`/`DeleteMessage`) are not logged: say so, never infer them.
2. **Event-source mappings**: `lambda list-event-source-mappings --event-source-arn <queue arn>`. Record every mapping,
   its function and its state, plus any redrive (`StartMessageMoveTask`) history on the queue.
3. **CloudWatch**, per minute over the window: `NumberOfMessagesReceived`, `NumberOfMessagesDeleted`,
   `ApproximateNumberOfMessagesVisible`.
4. **The current messages**: read them with `receive-message --visibility-timeout 0 --max-number-of-messages 10`,
   repeated until the depth is covered. This DLQ has no further redrive, so a receive moves nothing. Delete NOTHING.
   Record the count and each message's source key (bucket/key). No message body beyond its key.
5. Write `W/DQ1_READ.json` with keys:
   - `cloudtrail_events`, `cloudtrail_events_denominator`;
   - `event_source_mappings`, `event_source_mappings_denominator`;
   - `metrics`;
   - `current_messages` (`count`, `sources`);
   - `actor`: `verdict` "named" or "unnamed", plus `evidence`.

   "named" only if a plane above shows it. Otherwise "unnamed", with what logging would name it next. That is the
   CTO's call to cut, not yours.

## 2. BOUNDS

- READ ONLY. No delete, purge, redrive, attribute change, logging change or mapping change.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~57/`. Rows: id `NFRA_OPLGTW-Z-W57-S<k>`, fabric
`site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`. AWS through the repo shim `bash .tools/aws`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-dq-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r34/checks/dq1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)planes present .*actor (named|unnamed).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: every plane read with its denominator, and the actor verdict stated with evidence.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-dq-1.dlq-drain-actor-read.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> AC1 --governing-order <this order>`, flip the ONE `<status>` tag to
`complete` only if AC1 PASSES, and report once. Your next order (OG-bd-1) follows on this same slot.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 34, E7. First on slot ~57.
- Pre-cut: dq1.AC1 base FAIL as expected (DQ1_READ.json absent).

<status>complete</status>
<round>34</round>
<slot>~57</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
