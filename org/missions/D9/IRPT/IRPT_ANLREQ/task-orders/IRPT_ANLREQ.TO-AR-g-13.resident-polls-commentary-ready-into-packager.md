# TO-AR-g-13 -- the resident polls I4 (commentary_ready) into the packager, and its runtime wires I3 and I4 (FWD-1 hops 7-8, the poll)

<to_id>IRPT_ANLREQ.TO-AR-g-13.resident-polls-commentary-ready-into-packager</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~63</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G-I4POLL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G-I4POLL (the poll half AMENDMENT 4 added after ~G's round-1 issuance) | **Decomp cell:** `AR-g-12` (the poll half, assigned to ~G2 by
decomposition AMENDMENT 4, @e124f00985) | **outcome_ref:** FWD-1 | **depends_on:** AR-g-11 and AR-g-12. Both are merged on box/dell2
(@716a635999, @bfba3fdd4b).

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md`:
- the "Interfaces" table, rows I3 and I4;
- AMENDMENT 4: ~T2 adds the `commentary_ready` queue beside `analysis_ready` in `commentary.tf`, with send granted to the commentary
  role and receive to the resident role; ~G2 wires the resident's poll into AR-g-12's handler.

### THE CELL

AR-g-12 built the packager:
- `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`, `handle_commentary_ready(body, ports)`;
- its live ports: `live_attach` and `live_ticket_package` raise `PACKAGER_PRINCIPAL_UNSET`, and `live_read_artifact` raises
  `COMMENTARY_READER_UNWIRED`;
- `opal_producer.produce_package`.

AR-g-11 made READY send I3 through `ResidentGenerationWorker(ready_send=...)`. The queue URL comes from the environment variable
`IRPT_ANALYSIS_READY_QUEUE_URL`.

Nothing on the resident host yet RECEIVES I4, and nothing installed hands the worker its I3 URL. **Wire both into the resident's
runtime, so a deployed resident packages every request whose commentary is ready.**

1. **Bindings** (`infra/aws/lambda/investor-reporting/reports/resident_installed.py`, `load_bindings`; `REQUIRED` at :44, the
   `queue_url` check at :86). Admit TWO OPTIONAL keys: `analysis_ready_queue_url` and `commentary_ready_queue_url`.
   - Each, when present, must start with `https://sqs.`, exactly as `queue_url` does.
   - Absent is the pre-wiring state. It must load exactly as today.
   - Never type a queue name or URL: the release writes them from ~T2's queues.
2. **The factory** (`build_resident_runtime`, :274-344).
   - When `analysis_ready_queue_url` is bound, hand the assembly
     `ready_send = lambda url, body: clients["sqs"].send_message(QueueUrl=url, MessageBody=body)`.
   - Make the bound URL the one AR-g-11's `signal_ready` reads: set `IRPT_ANALYSIS_READY_QUEUE_URL` for the process from the binding,
     or change `signal_ready` to take the URL from the assembly. Choose ONE and keep the other path's WARN behaviour.
   - When `commentary_ready_queue_url` is bound, also return `package_queue_url` and `packager`, where `packager` is a callable
     `body -> outcome`. It is `handle_commentary_ready` with the LIVE ports, built from the same clients, `acceptance`,
     `stores.artifacts`, `opal_stores` and the jobs table the factory already builds.
3. **The loop** (`infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py`; the runtime check at :45-47; the loop at
   :52-63).
   - Admit the runtime with or without the two extra keys; any other key set still refuses `INSTALLED_RESIDENT_RUNTIME_REQUIRED`.
   - When `package_queue_url` is present, each loop iteration runs ONE short poll of it after `poll_once`, through a new
     `poll_package_once(*, sqs, queue_url, packager)` in `resident_worker.py`:
     - `WaitTimeSeconds` 1, `MaxNumberOfMessages` 1, `VisibilityTimeout` 900;
     - the same 4096-byte and duplicate-field refusals as `poll_once`.
   - The poll deletes a message ONLY on a terminal outcome: attached, already attached, or a named refusal of the message itself
     (wrong kind, extra or missing field, not closed).
   - The poll KEEPS the message (no delete) when the outcome is `PACKAGER_PRINCIPAL_UNSET`, `COMMENTARY_READER_UNWIRED`, or any other
     exception. Redelivery and ~T2's DLQ own it then.
   - Each outcome prints one line: `IRPT_RESIDENT_PACKAGE outcome=<code>`, with a closed code only and never a ref value.
   - A package-poll exception must not stop the generation loop; it reuses `retained_reason`.
4. **Test.** Add `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_package_poll.py`. It is offline, with a fake SQS and
   a fake packager. It proves:
   - (a) a terminal outcome deletes the message;
   - (b) `PACKAGER_PRINCIPAL_UNSET` keeps it;
   - (c) a malformed body is refused and deleted, with the packager not called;
   - (d) `build_resident_runtime` with neither optional binding returns exactly `{assembly, sqs, queue_url}`, as today. Use its
     `clients=` and `clock=` offline controls; reuse the offline bindings fixture its existing tests use, if any.
   - (e) with both bindings, the runtime carries `package_queue_url` and `packager`, and a READY send goes to the bound
     `analysis_ready` URL;
   - (f) `resident_main` admits both runtime shapes and refuses an unknown key.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR13-g-AC1" cell_refs="AR-g-12"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py g13</invocation><expect>^AR1-G2-G13-OK</expect></criterion>

<criterion id="AR13-g-AC2" cell_refs="AR-g-12"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py regress</invocation><expect>^AR1-G2-REGRESS-OK</expect></criterion>

<expected_criteria>AR13-g-AC1,AR13-g-AC2</expected_criteria>

- AC1: at least 5 passed and 0 failed. At the base it FAILs because the file is absent (issuer dry run).
- AC2: no test file in the generate or research suites is newly red against the base. The base red set is the two custody files.
  The regress run takes about 150 s; give it at least 600 s.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no upload, no AWS calls, no installs.
- Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W63-S<k>`. File them in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`.
  - APPEND a new `## <id>` heading plus a fenced json block at the END of the file.
  - Never edit an existing block.
  - Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~63" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~63@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~63 <0.9.0_WK_IRPT_ANLREQ~63@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool.
  - Do not pre-`git add`.
  - Edit byte-preserving, ASCII only.
  - Use the native Grep/Glob/Read tools.
- **Lane overrides.** `reports/resident_installed.py` is outside ~G's written scope; AMENDMENT 4 assigns this wiring to ~G2. If
  owned-paths refuses a file, commit that file alone with `GIT_COMMIT_AUTHOR_OVERRIDE=<the lane the refusal names>` (audited), and
  name it in your report.

<paths>
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_package_poll.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~63/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-13.resident-polls-commentary-ready-into-packager.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> round 1, workstream ~G, cell `AR-g-12` (poll half, AMENDMENT 4).
<owned_cells>AR-g-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR13-g-AC1, AR13-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~63/IRPT_ANLREQ.TO-AR-g-13.resident-polls-commentary-ready-into-packager.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR13-g-AC1,AR13-g-AC2` BEFORE the flip to complete. Shape:
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~62/IRPT_ANLREQ.TO-AR-g-12.package-pdf-with-commentary-and-attach.proof_of_spec.json`.
Commit the code first, then pin each artifact to a commit that contains it.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the two bindings and where they are read;
- how the I3 URL reaches `signal_ready`;
- the delete/keep rule per outcome;
- any lane override;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two optional bindings, two optional runtime keys and one short poll per loop iteration; with neither binding the runtime and loop are unchanged (arm d). Ships in the resident package by a later release pair, after ~T2's queues exist; nothing deploys in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the resident role's SendMessage on analysis_ready and ReceiveMessage/DeleteMessage on commentary_ready are ~T2's queue-policy statements (AMENDMENT 4); no permission here.
comp-schedule: DECLARED-NOT-APPLICABLE -- driven by the resident's own loop and the I4 queue.
comp-adversary: RUN -- read resident_main.py (70 lines), resident_worker.py poll_once :787-840, resident_installed.py :44, :86, :274-344. Traps: the package poll starving generation (WaitTimeSeconds 1), deleting a message whose live port is unwired (arm b), refs in log lines, a typed queue URL, a changed runtime contract with no binding (arm d).
lane: ~G per AMENDMENT 4 (the resident's poll); resident_installed.py by the audited override if refused.
</preflight>

Source: IRPT_ANLREQ decomposition round 1 AMENDMENT 4 (@e124f00985, 2.0.0_SA_COO~Y2 msg 2542); AR-g-11 @716a635999 and AR-g-12 @bfba3fdd4b, drained by 2.0.0_SA_COO~G2.
