# TO-YCD-d-15 -- the worker sends `analysis_ready` only for a request filed under a ticket

<to_id>IRPT_YCDGEN.TO-YCD-d-15</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~17</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-d-15` (`decompositions/IRPT_YCDGEN_DECOMP_R15.md`, AMENDMENT 1) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## 0.9.0_WK_IRPT_YCDGEN~17 FACE

### Read first

`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`: the function `send_ready` (search `def send_ready`), the method `mark_ready` (search
`def mark_ready`) and `signal_ready`, and the READY branch of the job's execution that re-sends when the job has no
`i3_sent_at` (search `"i3_sent_at" not in previous`). `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal.py` and
`infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_resend.py` (how those two sends are tested today, and their fakes).

### THE CELL

Today, when a generation job reaches READY, the worker sends one `analysis_ready` message whether or not the request was
filed under a ticket. Downstream of that message a commentary draft is started with an outside model, and for a request
with no ticket the result can never be attached to anything. Stop the chain at its first step.

1. **The rule:** `analysis_ready` is sent ONLY when the accepted request record carries a `ticket_id` that is a non-empty
   string. With no ticket, nothing is sent, and one journal line is printed:
   `IRPT_RESIDENT_READY_SIGNAL skipped=NO_TICKET <request id>`.
2. **Both send sites obey it:** the send after the READY write in `mark_ready`, and the re-send in the READY branch for a
   job that has no `i3_sent_at`. Read at each site where the ticket is known (the accepted record is in hand at both; the
   READY receipt also carries `ticket_id` when the record did). Put the decision in ONE place that both sites call.
3. **A skipped send records nothing as sent:** `i3_sent_at` is NOT written for a skipped request (it was not sent). The
   re-send branch must therefore not loop into a send for it: the same rule skips it again, with the same journal line.
4. **Everything else is unchanged:** the READY write, its receipt (which names the ticket when there is one), the release
   of the request, the behaviour when the queue URL is unset (the existing `ANALYSIS_READY_QUEUE_UNSET` warning), and the
   send itself for a request WITH a ticket, byte for byte.
5. The worker does not read the ticket and learns nothing about its type: it has no ticket port and must not gain one.
6. **Tests, offline, in a NEW file** `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_ticket_gate.py`, with the fakes of the two files
   above. Five groups, each a function whose name starts with the letter shown:
   - `test_a_`: a record WITH a ticket: one send, to the bound URL, and `i3_sent_at` is marked (as today).
   - `test_b_`: a record with NO `ticket_id`: 0 sends, `i3_sent_at` not marked, the skip line printed once.
   - `test_c_`: a `ticket_id` that is empty, whitespace or not a string: 0 sends, the skip line.
   - `test_d_`: the re-send branch (READY, no `i3_sent_at`) for a ticketless request: 0 sends on each of two deliveries.
   - `test_e_`: the re-send branch for a request WITH a ticket and no `i3_sent_at`: one send (as today).
   Update `test_ready_signal.py` and `test_ready_resend.py` only where a case there now needs a ticket to keep its
   meaning; say which in your report. Keep every other test in the folder green.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="D15-AC1" cell_refs="YCD-d-15"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r15/r15_checks.py d15</invocation><expect>^R15-D15-OK</expect></criterion>

<criterion id="D15-AC2" cell_refs="YCD-d-15"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r15/r15_checks.py d15suite</invocation><expect>^R15-D15SUITE-OK</expect></criterion>

<expected_criteria>D15-AC1,D15-AC2</expected_criteria>

- AC1 requires the new test file with all five groups and runs it: 0 failed, at least 5 passed. At base it FAILs (no file).
- AC2 runs the whole `ycharts/generate/tests` folder: 0 failed, 0 errors, at least 512 passed (507 at base, plus the five
  groups). At base it FAILs on the count. It takes about two minutes.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Every `.py` edit passes
  `.tools/commit-gate.sh`. This cell ships to the host only in a later resident release under its own pair.
- **Refusal clause.** If a criterion cannot be met as written, or the commit is refused because these files are another
  project's lane: stop, file a row with the refusal text, report, and do not weaken a check or force a commit.
- **Rows** are `IRPT_YCDGEN-D2-W17-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel
  file below. `class` is `OBSERVATION` or `BLOCKING`, nothing else. Each row's `surfaced_at` is the output of
  `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type a time. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~17" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~17@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~17 <0.9.0_WK_IRPT_YCDGEN~17@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_ticket_gate.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_resend.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~17/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-d-15.analysis-ready-is-sent-only-for-a-request-filed-under-a-ticket.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R15.md</decomp_doc> round 15, cell `YCD-d-15`.
<owned_cells>YCD-d-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: D15-AC1, D15-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~17/IRPT_YCDGEN.TO-YCD-d-15.analysis-ready-is-sent-only-for-a-request-filed-under-a-ticket.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-d-15`.
- Each criterion's `output_evidence` BEGINS with the check's own OK line. `artifacts_produced.commit_or_etag` is the hash of
  your code commit, never a placeholder: commit the code first, then write the proof.
- Validate with `python .tools/proof-of-spec-check.py <instance> D15-AC1,D15-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~16/IRPT_YCDGEN.TO-YCD-d-13.worker-stamps-cause-claim-measured.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the one place the rule lives, with its lines, and the two call sites;
- which existing tests you changed and why;
- whether the Opal path's READY (an Opal-produced report) goes through the same `mark_ready`, by reading;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- the two sites in ycharts/generate/resident_worker.py that send analysis_ready (mark_ready after the READY write; the READY branch re-send). The send is dormant on the host today: st32's bindings carry no analysis_ready_queue_url (V1 read 0), so no behaviour on the running host changes until a later release binds it. Consumer of the message: outlook-global-commentary-draft-lambda. Ships only in a later resident release under its own pair; nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read send_ready (lines 163-186 at HEAD), mark_ready (318-328), the READY branch (lines 657-675) and the 2 existing test files of the send; denominator: 2 send sites in the worker (native search of the file for send_ready( gives the definition and 2 calls). NOT seen: whether the Opal path's READY uses the same mark_ready (the order asks the worker to say). Traps: marking i3_sent_at for a send that did not happen; a re-send loop for a ticketless READY job; reading the ticket; changing the send for a request that has a ticket.
lane: ycharts/generate/resident_worker.py -- the resident worker; if the owned-paths gate names another project's lane the worker stops and the issuer re-points.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` msg 5727 (the cell FIRST: the chain stops for a request with no ticket before analysis_ready is
sent; tests assert the drafter is not called); this seat's packet `r15/NEVER_WIDEN_PACKET_THE_BINDING_PART1_20261011.md`
@4fdc20b233 section 2.2.
