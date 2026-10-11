# TO-YCD-a-16 -- the worker sends `analysis_ready` only for a ticketed request whose record says commentary was asked for

<to_id>IRPT_YCDGEN.TO-YCD-a-16</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~18</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>16</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-a-16` (`decompositions/IRPT_YCDGEN_DECOMP_R16.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## 0.9.0_WK_IRPT_YCDGEN~18 FACE

### Read first

`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`: the function `send_ready_if_ticketed` (search `def send_ready_if_ticketed`) and its two
callers (`signal_ready`, and the READY branch under `"i3_sent_at" not in previous`).
`infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_ticket_gate.py` (the tests of that function and their fakes), `test_ready_signal.py` and
`test_ready_resend.py`. The contract: `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md`, the section headed
`ADDENDUM v0.13` (search `commentary_requested`).

### THE CELL

Today the worker sends `analysis_ready` for any request filed under a ticket. The contract now says a request states
whether commentary was asked for, in a member of its accepted record named `commentary_requested`, and a draft is started
only then. Add that second condition to the ONE rule that exists.

1. **The rule, in `send_ready_if_ticketed`:** send only when the accepted record carries a `ticket_id` that is a non-empty
   string AND `commentary_requested` is EXACTLY the boolean `True` (`record.get("commentary_requested") is True`). The
   string `"true"`, the number `1`, any other truthy value, `False`, `None` and an absent member all send NOTHING.
2. **Two skip lines, so the journal says which condition failed.** The ticket check comes first and keeps its line
   unchanged: `IRPT_RESIDENT_READY_SIGNAL skipped=NO_TICKET <request id>`. A ticketed request that did not ask prints
   `IRPT_RESIDENT_READY_SIGNAL skipped=COMMENTARY_NOT_REQUESTED <request id>`. Exactly one line per skipped call.
3. As before: a skipped send marks no `i3_sent_at`; the re-send branch skips the same way on every delivery; `send_ready`
   itself, the READY write and its receipt are untouched. Rename the function if its name no longer says what it does,
   and keep ONE rule that both sites call.
4. The worker does NOT write `commentary_requested` anywhere: not into the READY receipt, not into the message. It reads
   it from the accepted record and nothing else. It gains no ticket read.
5. **Tests, offline, in a NEW file** `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_commentary_gate.py`, with the fakes of the ticket-gate
   file. Five groups, each a function whose name starts with the letters shown:
   - `test_a_`: ticket id present and `commentary_requested` True: one send, `i3_sent_at` marked.
   - `test_b_`: ticket id present and the member ABSENT: 0 sends, not marked, the COMMENTARY_NOT_REQUESTED line once.
   - `test_c_`: ticket id present and the member `False`, `"true"`, `1`, `"yes"` or `None`: 0 sends each.
   - `test_d_`: NO ticket id and the member True: 0 sends, and the line printed is NO_TICKET (the first condition).
   - `test_e_`: the re-send branch (READY, no `i3_sent_at`): a ticketed request without the member sends nothing on two
     deliveries; with it True, one send.
   Update `test_ready_signal_ticket_gate.py`, `test_ready_signal.py` and `test_ready_resend.py` only where a case that
   expects a send now needs the member to keep its meaning; say which in your report. Keep every other test green.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="A16-AC1" cell_refs="YCD-a-16"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r16/r16_checks.py a16</invocation><expect>^R16-A16-OK</expect></criterion>

<criterion id="A16-AC2" cell_refs="YCD-a-16"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r16/r16_checks.py a16suite</invocation><expect>^R16-A16SUITE-OK</expect></criterion>

<expected_criteria>A16-AC1,A16-AC2</expected_criteria>

- AC1 requires the new test file with all five groups and runs it: 0 failed, at least 5 passed. At base it FAILs (no file).
- AC2 runs the whole `ycharts/generate/tests` folder: 0 failed, 0 errors, at least 527 passed (522 at base, plus the five
  groups). At base it FAILs on the count. It takes about two and a half minutes. If the honest count after your change is
  below 527 with 0 failed, do not pad tests and do not edit the checks file: file a row with the count and report it.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Every `.py` edit passes
  `.tools/commit-gate.sh`. This cell ships to the host only in a later resident release under its own pair.
- **Not yours:** the submission's closed set and acceptance copying the member (`submission.py`, `acceptance.py`, the
  schema) are another cell's. Do not edit them; your tests build the accepted record directly.
- **Refusal clause.** If a criterion cannot be met as written, or the commit is refused because these files are another
  project's lane: stop, file a row with the refusal text, report, and do not weaken a check or force a commit.
- **Rows** are `IRPT_YCDGEN-D2-W18-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel
  file below. `class` is `OBSERVATION` or `BLOCKING`, nothing else. Each row's `surfaced_at` is the output of
  `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type a time. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~18" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~18@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~18 <0.9.0_WK_IRPT_YCDGEN~18@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_commentary_gate.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_ticket_gate.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_resend.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~18/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-a-16.analysis-ready-needs-a-ticket-and-commentary-requested-true.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R16.md</decomp_doc> round 16, cell `YCD-a-16`.
<owned_cells>YCD-a-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: A16-AC1, A16-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~18/IRPT_YCDGEN.TO-YCD-a-16.analysis-ready-needs-a-ticket-and-commentary-requested-true.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-a-16`.
- Each criterion's `output_evidence` BEGINS with the check's own OK line. `artifacts_produced.commit_or_etag` is the hash of
  your code commit, never a placeholder: commit the code first, then write the proof.
- Validate with `python .tools/proof-of-spec-check.py <instance> A16-AC1,A16-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~17/IRPT_YCDGEN.TO-YCD-d-15.analysis-ready-is-sent-only-for-a-request-filed-under-a-ticket.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the rule's lines as they now read, and the two skip lines;
- which existing tests you changed and why;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one function in ycharts/generate/resident_worker.py, send_ready_if_ticketed, and its 2 callers. The send is dormant on the host: st32's bindings carry no analysis_ready_queue_url, and the function is not even in st32 (merged after its pin). Consumer of the message: outlook-global-commentary-draft-lambda. Ships only in a later resident release under its own pair; nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read send_ready_if_ticketed and its 2 call sites at HEAD, the 15 tests of the ticket gate, and PRD ADDENDUM v0.13; denominator: 1 rule, 2 callers, 0 writers of commentary_requested in the tree today (the addendum's own token census reads 0). NOT seen: the cell that makes acceptance copy the member, which is not built, so no accepted record carries it and after this cell EVERY request sends nothing; that is the intended order (the gate first, the producer of the fact second). Traps: truthiness in place of `is True`; the worker copying the member into the receipt or the message; a third state for an absent member; losing the NO_TICKET line.
lane: ycharts/generate/resident_worker.py -- the resident worker; if the owned-paths gate names another project's lane the worker stops and the issuer re-points.
</preflight>

Source: `1.0.0_SA_CTO~DELL2` round-16 analysis @1dd909d19d section 3 item 1 and msg 5830 ("cut the worker's second
condition now"); PRD ADDENDUM v0.13 @39c807e066, ratified-text half signed by `3.0.0_SA_CVO` @6f8aeb03b7.
