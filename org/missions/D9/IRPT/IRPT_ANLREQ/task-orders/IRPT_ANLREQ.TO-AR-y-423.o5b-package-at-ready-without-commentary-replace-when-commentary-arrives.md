# TO IRPT_ANLREQ.TO-AR-y-423.o5b-package-at-ready-without-commentary-replace-when-commentary-arrives -- O5, packager half: at READY the resident attaches the package WITHOUT the commentary (pdf_ref and commentary_ref both null); when the commentary is ready it REPLACES that package with all four refs; a failure of either step is recorded as the PACKAGER hop failure and never withholds the READY

<to_id>IRPT_ANLREQ.TO-AR-y-423.o5b-package-at-ready-without-commentary-replace-when-commentary-arrives</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~313</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ81</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the path floor | **Decomp cell:** `AR-y-423` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the attachments reach the ticket; a commentary failure withholds nothing), FWD-4 (the ticket names the failed step), C-PACKAGER | **depends_on:** AR-y-417 (merged b8e34d819af); TCKT_VNEXT.TO-R20-LM7 (the ticket service accepts pdf_ref and commentary_ref both null; read org/missions/D7/TCKT/TCKT_VNEXT/task-orders/TCKT_VNEXT.TO-R20-LM7.package-accepts-commentary-ref-null-and-the-page-reads-it-as-not-available.md at HEAD); CTO msgs 11065, 11068, 11078; both halves ship in ONE release

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~313`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-313` (branch `wk-IRPT_ANLREQ-313`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~313 <0.9.0_WK_IRPT_ANLREQ~313@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W313-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-423`, inlined)

*Context.* The ticket service's package route (`infra/aws/lambda/ticket_center` is not yours; read `infra/aws/lambda/ticket_center/lambda_function.py` lines about 1800-1900 at HEAD, read-only): a first package is stored with `attached_at`; a second POST must send `prior_attached_at` equal to the stored `attached_at` to REPLACE it, otherwise 409 `PACKAGE_ALREADY_ATTACHED` with the stored package's four pointers and `attached_at` in the answer. After TCKT_VNEXT.TO-R20-LM7 the route accepts `pdf_ref` and `commentary_ref` BOTH null (both keys present, together only; one null beside one set is 400); `report_ref` stays required; `original_ref` may be null for a custody-lane request. TODAY the packager (`infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`) is reached only by `handle_commentary_ready` (a `commentary_ready` queue message): one attach with all four refs, so a request whose commentary is slow or fails is never packaged (CRO gap G7). `send_ready_if_ticketed` (AR-y-417, merged) now sends `analysis_ready` for every ticketed request. The resident builds its packager in `infra/aws/lambda/investor-reporting/reports/resident_installed.py` (`make_packager`, about line 449: a `ports` dict, `_record_packager_failure` writing the job row's hop failure `PACKAGER` with code `PACKAGER_REFUSED` or `PACKAGER_FAILED`, and the `packager(body)` closure returned) and constructs the generation assembly with `ready_send=ready_send` (about line 581); `ResidentAssembly.__init__` (`infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py` about line 629, `ready_send=None`) passes it to `ResidentGenerationWorker.__init__` (about line 261) which calls `send_ready_if_ticketed` in `signal_ready` (about line 402) and again at about line 746.

*The change (FOUR places; the cell's own new names).*
1. **`opal_packager.py`.** (a) `_attach` accepts `commentary_wire=None` and `ref=None` and then sends `"pdf_ref": None, "commentary_ref": None` (BOTH keys present, together; a mixed pair is a refusal `PACKAGE_PARTIAL_PAIR`); the existing full call is byte-identical in its payload. (b) A NEW `handle_ready(tenant, request_id, ports)` for a request at READY: read the acceptance record (`TICKET_ID_ABSENT` if no string ticket id), the job at READY (`JOB_NOT_READY`) for `report_id` as `handle_commentary_ready` does (reuse its reads and the original-ref rule `ORIGINAL_REF_ABSENT`), compute `_revision(record)`, and attach `{report_ref, pdf_ref: None, original_ref, commentary_ref: None, firm, request_id, request_revision}`; return `{"outcome": "ATTACHED_WITHOUT_COMMENTARY" | "ALREADY_ATTACHED", ...}`. It reads NO commentary and renders NO PDF. (c) In `live_ticket_ports.attach`'s `conflict` handling: on a 409 `PACKAGE_ALREADY_ATTACHED` read the stored package from the answer: if the stored pair is both null and the payload's pair is both set (a FULL package arriving over a partial one), re-POST ONCE with `prior_attached_at` = the answer's `attached_at` (the replace) and return that answer; if the stored pair is both set and the payload's is null (a late READY retry after the full package), do NOT downgrade: return `{"already_attached": True}`; if the four pointers are equal return `{"already_attached": True}` as today; anything else is the existing `ATTACH_CONFLICT:PACKAGE_ALREADY_ATTACHED_OTHER`. `handle_commentary_ready` is otherwise unchanged.
2. **`resident_worker.py`.** `ResidentGenerationWorker.__init__` and `ResidentAssembly.__init__` gain `ready_package=None` (passed through exactly as `ready_send` is). A module-level `package_on_ready(ready_package, tenant, request_id, record)`: nothing when `ready_package` is None or the record has no string `ticket_id`; otherwise calls `ready_package(tenant, request_id)` inside `try/except Exception` and prints `IRPT_RESIDENT_PACKAGE_READY outcome=<closed code>` on success or `IRPT_RESIDENT_PACKAGE_READY retained_for_retry <exception class name>` on failure; it NEVER raises and never touches the READY state. It is called AFTER `send_ready_if_ticketed` at BOTH sites (`signal_ready` and the second site), with `self.store.tenant`.
3. **`resident_installed.py`.** In `make_packager`, build `ready_packager(tenant, request_id)` from the same `ports`: on success `opal_packager.handle_ready(tenant, request_id, ports)`; on any exception record the hop failure exactly as `_record_packager_failure` does (hop `PACKAGER`, code `PACKAGER_REFUSED` or `PACKAGER_FAILED`; factor the recording so the two closures share it, the message-based one unchanged in behaviour) and re-raise. Return the `packager` closure as today and attach the new callable to it as `packager.ready_package = ready_packager` (the factory's return type and every caller stay valid). At the assembly construction (about line 581) pass `ready_package=getattr(packager, "ready_package", None)` where the packager exists, None otherwise. The resident runtime's closed key set in `resident_main.py` does NOT change.
4. Nothing else moves: no other function, no ticket-service file, no queue, no binding, no IAM.

*The tests.* (a) NEW `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager_ready.py`, EXACTLY seven tests (fakes in the style of `test_opal_packager.py` and `test_packager_live_ports.py`): (1) `handle_ready` attaches a payload carrying `report_ref`, `original_ref`, `firm`, `request_id`, `request_revision` and BOTH `pdf_ref` and `commentary_ref` as None with both keys present, and renders nothing; (2) no ticket id -> `PackagerRefused` `TICKET_ID_ABSENT`; (3) a job not at READY -> `JOB_NOT_READY`; (4) a custody-lane record with no original attaches with `original_ref` None, a prospect record with no original is refused `ORIGINAL_REF_ABSENT`; (5) the live attach port, stored package partial and payload FULL: the fake HTTP sees two POSTs, the second carrying `prior_attached_at` equal to the 409 answer's `attached_at`, and the outcome is an attach; (6) stored FULL and payload partial: ONE POST only, `already_attached`; (7) stored partial and an identical partial payload: ONE POST only, `already_attached`. (b) NEW `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_package_on_ready.py`, EXACTLY four tests: (1) a READY with a ticket calls `ready_package(tenant, request_id)` once, after the analysis_ready send; (2) no ticket -> not called; (3) `ready_package` raising leaves the READY state written, prints the `retained_for_retry` line and raises nothing; (4) `ready_package` None -> nothing, behaviour identical to today.

*What to do.* (1) Read the five files; baseline the criterion AR423-y-AC2's command and print it. (2) Write both test files, run them against the UNCHANGED code (they must fail: the difference control). (3) Make the change; run the new files (`11 passed`) and AC2 (no failure). `controls.mutant` = the seven packager tests against a copy of `opal_packager.py` WITHOUT change (c) (tests 5 and 6 FAIL). (4) Write `check_o5b_bound.py` (below) and the proof instance; flip on VALID with all three PASS.

You also write `check_o5b_bound.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~313/` (ruff clean, stdlib only): it takes the branch point `git merge-base HEAD box/dell2`, keeps the changed paths NOT under `org/`, and prints `O5B-BOUND-OK files=5` only when they are exactly the three product files and the two new test files named above; otherwise `O5B-BOUND-BAD <paths>` and a non-zero exit.

---

## ACCEPTANCE

<criterion id="AR423-y-AC1" cell_refs="AR-y-423"><invocation>cd infra/aws/lambda/investor-reporting/ && python -m pytest ycharts/research/tests/test_opal_packager_ready.py ycharts/generate/tests/test_package_on_ready.py -q --color=no -p no:cacheprovider</invocation><expect>11 passed</expect></criterion>
<criterion id="AR423-y-AC2" cell_refs="AR-y-423"><invocation>cd infra/aws/lambda/investor-reporting/ && python -m pytest ycharts/research/tests/test_opal_packager.py ycharts/research/tests/test_opal_packager_request_id.py ycharts/research/tests/test_packager_live_ports.py ycharts/research/tests/test_packager_i7.py ycharts/generate/tests/test_package_poll.py ycharts/generate/tests/test_ready_signal.py ycharts/generate/tests/test_ready_signal_on_ready.py ycharts/generate/tests/test_resident_worker.py reports/tests/test_resident_installed.py reports/tests/test_resident_packager_binding.py -q --color=no -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
<criterion id="AR423-y-AC3" cell_refs="AR-y-423"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~313/check_o5b_bound.py</invocation><expect>O5B-BOUND-OK files=5</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~313/IRPT_ANLREQ.TO-AR-y-423.o5b-package-at-ready-without-commentary-replace-when-commentary-arrives.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-423.o5b-package-at-ready-without-commentary-replace-when-commentary-arrives`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR423-y-AC1,AR423-y-AC2,AR423-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-423</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager_ready.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_package_on_ready.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~313/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-423.o5b-package-at-ready-without-commentary-replace-when-commentary-arrives.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- three modules of the resident package and two new test files; nothing is deployed; the resident release (r34m: a build order, a never-widen pair and an IB2 install) and the ticket-service release of TCKT_VNEXT.TO-R20-LM7 ship together later, each under its own signed pair.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading `opal_packager.py`, `make_packager`, the assembly and worker constructors, the ticket service's package route and the CTO rulings (msgs 11065 and 11078) against this cell; the lens: a downgrade of a full package by a late READY retry (test 6), a replace without `prior_attached_at` (test 5), a half-null pair sent (refused PACKAGE_PARTIAL_PAIR), the READY state undone or an exception escaping the worker (test 3 of the worker file), the runtime key set changed (it does not), the packager hop failure not recorded for the new path (the shared recorder). NOT seen (blind): the live ticket service before R20-LM7 lands, the live queue and the resident host; the release order is the contract: this packager must not reach PROD before the service accepts the null pair; denominator: three criteria.
</preflight>
