# TO-AR-g-21 -- READY records `i3_sent_at` after the I3 send; a redelivery that finds READY unsent sends again (row D2-W61-S1)

<to_id>IRPT_ANLREQ.TO-AR-g-21</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~64</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G | **Decomp cell:** `AR-g-21` (`decompositions/IRPT_ANLREQ_DECOMP_R2.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (AR-g-11 is merged).

---

## WORKER FACE

### THE CELL

Round 1 made READY send ONE closed message, `analysis_ready` (I3), after the READY write
(`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`: `mark_ready`, then `signal_ready`).

Row IRPT_ANLREQ-D2-W61-S1 found the gap: a process death between the READY write and the send loses the signal forever. The
redelivery branch (`ResidentAssembly.execute`, around :648, `if previous["state"] == "READY":`) re-binds the report and returns,
and nothing records whether the send happened.

**Record the send, and re-send from redelivery when it is missing.**

1. **The record.** Work in `infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py`, `DynamoGenerationStore`, table
   `irpt-jobs`, key `{tenant, job}`. It already has `_update` (:120), `get_state` (:132) and `put_state` (:138).
   - Add `mark_i3_sent(job_id, at)`: ONE conditional update that sets a TOP-LEVEL attribute `i3_sent_at` (an ISO-8601 UTC string),
     only when `state = READY` and `attribute_not_exists(i3_sent_at)`.
   - A second call is a no-op that returns normally: catch the conditional failure only when the row already carries
     `i3_sent_at`; any other failure raises.
   - Do NOT put it inside `job_detail`: the READY receipt's bytes stay as round 1 left them.
   - `get_state` exposes `i3_sent_at` when present.
2. **Write the marker only after a successful send.** In `signal_ready`, call `store.mark_i3_sent(...)` only after `send(...)`
   returns.
   - Unset queue (`WARN: ANALYSIS_READY_QUEUE_UNSET`) or a failed send (`ERROR: ANALYSIS_READY_SEND_FAILED`): no marker.
   - A failure of the marker write itself logs one `ERROR: ANALYSIS_READY_MARK_FAILED <request_id>` and never undoes READY.
3. **Re-send on redelivery.** In the redelivery READY branch, after the existing binding check passes and before it returns: if
   `previous` carries no `i3_sent_at`, run the same `signal_ready` path once (send, then mark).
   - A READY row that already carries `i3_sent_at` sends nothing (round 1's rule, kept).
   - Build the worker's `signal_ready` access however is smallest. The assembly already holds `ready_send`, and the queue URL comes
     from `IRPT_ANALYSIS_READY_QUEUE_URL`, set by AR-g-13's factory.
4. **Test.** Add `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_resend.py`, offline with fakes. Reuse the
   fixtures of `tests/test_ready_signal.py` (round 1). It must prove:
   - (a) a successful READY send writes `i3_sent_at`, exactly once;
   - (b) KILL BETWEEN WRITE AND SEND: make the send step raise a `BaseException` subclass (a simulated process death) after the
     READY write. The row is READY with no `i3_sent_at`. A redelivery then sends exactly one `analysis_ready`, byte-equal to
     `queue_message("analysis_ready", {...})`, and writes `i3_sent_at`;
   - (c) a redelivery of a READY row that carries `i3_sent_at` sends nothing;
   - (d) a failed send leaves no marker, and the next redelivery sends;
   - (e) `mark_i3_sent` twice is one write and no error.

   Keep `tests/test_ready_signal.py` green.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR21-g-AC1" cell_refs="AR-g-21"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py g21</invocation><expect>^AR1-G2-G21-OK</expect></criterion>

<criterion id="AR21-g-AC2" cell_refs="AR-g-21"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py regress</invocation><expect>^AR1-G2-REGRESS-OK</expect></criterion>

<expected_criteria>AR21-g-AC1,AR21-g-AC2</expected_criteria>

- AC1: at least 4 passed and 0 failed. At base it FAILs because the file is absent (issuer dry run).
- AC2: no file newly red. The base red set is the two custody files plus `research/tests/test_opal_packager.py`; AR-g-22 repairs the
  latter. Allow at least 600 s.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS calls, no installs. Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W64-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of
  `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~64" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~64@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~64 <0.9.0_WK_IRPT_ANLREQ~64@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/durable_job.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_resend.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~64/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-21.ready-records-i3-sent-and-redelivery-resends.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md</decomp_doc> round 2, workstream ~G, cell `AR-g-21`.
<owned_cells>AR-g-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR21-g-AC1, AR21-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~64/IRPT_ANLREQ.TO-AR-g-21.ready-records-i3-sent-and-redelivery-resends.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-21`.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR21-g-AC1,AR21-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/IRPT_ANLREQ.TO-AR-g-11.ready-names-ticket-and-signals-once.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the `mark_i3_sent` condition;
- where the re-send sits in the redelivery branch;
- the kill-test mechanism;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one new top-level attribute on irpt-jobs READY rows (conditional, set once); the READY receipt bytes are unchanged; the redelivery branch gains one guarded send. Ships in the resident release (AR-g-23); nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- the resident role already updates irpt-jobs (put_state); no new permission.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read resident_worker.py :290-325 (mark_ready/signal_ready, merged @716a635999) and :640-662 (the redelivery READY branch); durable_job.py :120-157. Traps: the marker written before the send (arm b), a second send on a marked row (arm c), the marker placed inside the receipt (bounded), a marker failure undoing READY.
lane: ~G (resident_worker.py, durable_job.py per the decomposition).
</preflight>

Source: IRPT_ANLREQ decomposition round 2 cell AR-g-21 (@cff0872f0f, 2.0.0_SA_COO~Y2 msg 2780); row IRPT_ANLREQ-D2-W61-S1.
