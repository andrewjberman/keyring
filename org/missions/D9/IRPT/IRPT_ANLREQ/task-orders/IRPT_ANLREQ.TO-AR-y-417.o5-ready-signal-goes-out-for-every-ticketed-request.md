# TO IRPT_ANLREQ.TO-AR-y-417.o5-ready-signal-goes-out-for-every-ticketed-request -- O5: the resident sends analysis_ready for every request that carries a ticket, whether or not commentary was requested (resident_worker.py send_ready_if_ticketed), so the packager is reached on every run

<to_id>IRPT_ANLREQ.TO-AR-y-417.o5-ready-signal-goes-out-for-every-ticketed-request</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~311</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ77</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-417` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the four attachments reach the ticket), C-PACKAGER | **depends_on:** PRD v0.24 (C-PACKAGER: triggered by READY, never by the commentary flag); ~G2 note S10 (the trigger is resident_worker.py:254); a resident release (r34m) follows and is its own pair

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~311`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-311` (branch `wk-IRPT_ANLREQ-311`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~311 <0.9.0_WK_IRPT_ANLREQ~311@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W311-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-417`, inlined)

*Context.* `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py`, `send_ready_if_ticketed(store, ready_send, request_id, record)` (about lines 242-254): it sends `analysis_ready` (through `send_ready`) only when the accepted record carries a non-empty string `ticket_id` AND `record.get("commentary_requested") is True`; otherwise it prints `IRPT_RESIDENT_READY_SIGNAL skipped=NO_TICKET <id>` (checked first) or `IRPT_RESIDENT_READY_SIGNAL skipped=COMMENTARY_NOT_REQUESTED <id>` and sends nothing. The packager (`ycharts/research/opal_packager.py`, `handle_commentary_ready`) is reached only downstream of that signal, so a request filed without commentary is never packaged: no ticket has carried a package since 2026-10-10 (CRO gap G7; ticket TCK-20261017-5af976ff holds a COMPLETE report and its upload, neither attached). The PRD v0.24 ratified text: C-PACKAGER is triggered by READY, never by the commentary flag; the form now always requests commentary (AR-y-416), but a request that arrives without the flag (an older client, a retry) must still be packaged.

*The change (ONE function and its docstring).* In `send_ready_if_ticketed` remove the `commentary_requested` condition: a record with a non-empty string `ticket_id` ALWAYS reaches `send_ready`, whatever `commentary_requested` is (True, False or absent). The NO_TICKET skip is unchanged and still checked first. The `COMMENTARY_NOT_REQUESTED` journal literal is no longer printed by this function (delete it; keep `NO_TICKET`). Change nothing else in the file and no other file under `infra/aws/lambda/investor-reporting/` except the tests named below. The `commentary_requested` MEMBER of the request contract is untouched (`test_commentary_requested_member.py` must stay green): this cell changes the trigger rule only. A commentary failure withholding the other three attachments (the brief's O5 second sentence) is NOT done here: it needs the ticket service's package contract (all four refs in one attach, `opal_packager._attach`) and is raised separately; do not touch the packager.

*The tests.* `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_commentary_gate.py` pins the old gate (five mentions): change it so each test pins the new rule, keeping its names and intent (a test that asserted "no signal when commentary is not requested" now asserts the signal IS sent for `False` and for an absent member). Add the new file `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_on_ready.py` with EXACTLY five tests: (1) ticketed + `commentary_requested` True -> sent; (2) ticketed + False -> sent; (3) ticketed + member absent -> sent; (4) no ticket (absent, empty and whitespace-only, as one parametrized or three asserts) -> NOT sent and the journal line names `NO_TICKET`; (5) the journal never prints `COMMENTARY_NOT_REQUESTED`. Read `test_ready_signal.py` for the fake store and `ready_send` style.

*What to do.* (1) Baseline: `cd infra/aws/lambda/investor-reporting/ && python -m pytest ycharts/generate/tests/test_ready_signal.py ycharts/generate/tests/test_ready_signal_commentary_gate.py ycharts/generate/tests/test_commentary_requested_member.py -q --color=no -p no:cacheprovider`; print it. (2) Write the new tests, run them against the UNCHANGED code (tests 2 and 3 must fail: the difference control). (3) Make the change and update the gate tests; run the three baseline files plus the new file; print the lines. `controls.mutant` = the new file run against a copy of `resident_worker.py` with the `commentary_requested` condition restored (tests 2 and 3 FAIL). (4) Write `check_o5_bound.py` (below) and the proof instance.

You also write `check_o5_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~311/` (ruff clean, stdlib only): it takes the branch point `git merge-base HEAD box/dell2`, keeps the changed paths NOT under `org/`, and prints `O5-BOUND-OK files=<n>` only when they are exactly `resident_worker.py`, `test_ready_signal_commentary_gate.py` and `test_ready_signal_on_ready.py` (n=3) AND, comparing `ast.dump` of every top-level definition of `resident_worker.py` at the branch point and at HEAD, only `send_ready_if_ticketed` differs; otherwise `O5-BOUND-BAD <what>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR417-y-AC1" cell_refs="AR-y-417"><invocation>cd infra/aws/lambda/investor-reporting/ && python -m pytest ycharts/generate/tests/test_ready_signal_on_ready.py -q --color=no -p no:cacheprovider</invocation><expect>5 passed</expect></criterion>
<criterion id="AR417-y-AC2" cell_refs="AR-y-417"><invocation>cd infra/aws/lambda/investor-reporting/ && python -m pytest ycharts/generate/tests/test_ready_signal.py ycharts/generate/tests/test_ready_signal_commentary_gate.py ycharts/generate/tests/test_commentary_requested_member.py -q --color=no -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
<criterion id="AR417-y-AC3" cell_refs="AR-y-417"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~311/check_o5_bound.py</invocation><expect>O5-BOUND-OK files=3</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~311/IRPT_ANLREQ.TO-AR-y-417.o5-ready-signal-goes-out-for-every-ticketed-request.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-417.o5-ready-signal-goes-out-for-every-ticketed-request`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR417-y-AC1,AR417-y-AC2,AR417-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-417</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_commentary_gate.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal_on_ready.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~311/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-417.o5-ready-signal-goes-out-for-every-ticketed-request.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- one function of the resident worker and its tests; nothing is deployed; the resident release (r34m: a build order, a never-widen pair and an IB2 install) is a later act.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading `send_ready_if_ticketed`, the three ready-signal test files and the PRD C-PACKAGER text against this cell; the lens: a test weakened to pass (tests 2 and 3 fail against the old rule), the packager or its payload touched (the bound check allows exactly three files and one definition), the request contract member removed (test_commentary_requested_member must stay green), the NO_TICKET skip lost (test 4). NOT seen (blind): the live resident, the commentary drafter queue and the ticket service; denominator: three criteria; AC2 PASSES at the base (a control).
</preflight>
