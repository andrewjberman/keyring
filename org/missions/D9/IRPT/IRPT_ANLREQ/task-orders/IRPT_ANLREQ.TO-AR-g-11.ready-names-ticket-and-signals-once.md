# TO-AR-g-11 -- the resident's READY record names the ticket, and READY sends I3 once (FWD-1 hop 5)

<to_id>IRPT_ANLREQ.TO-AR-g-11</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~61</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-09</issued_date>
**AMENDMENT 2026-10-09 (2.0.0_SA_COO~G2, issuer):** <to_id> shortened to the project's form (as AR-y-11 and AR-t-*), which the
worker's proof instance names; round-close-check compares the two (2.0.0_SA_COO~Y2 msg 2745). Gate limb: none graded this modification.

<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (the Opal engine and brand) | **Decomp cell:** `AR-g-11`
(`decompositions/IRPT_ANLREQ_DECOMP_R1.md`) | **outcome_ref:** FWD-1 | **depends_on:** none to build. AR-y-11 (~Y2) writes `ticket_id`
onto the acceptance record; this cell READS it, and treats it as optional.

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md`, the "Interfaces" table, rows I2 and I3. Your cell is the
resident's half of I3.

### THE CELL

When the Opal engine finishes a request, the resident marks the job READY. From there the backend must carry on by itself: the
commentary drafts, then the package is built and attached to the ticket. **Make READY name the ticket the request belongs to, and
send ONE closed message, `analysis_ready`, so the commentary starts.**

All code is under `infra/aws/lambda/investor-reporting/ycharts/generate/`.

1. **Name the ticket on READY.** `resident_worker.py` writes READY in two places:
   - the vendor path, `ResidentGenerationWorker.run()`, around :388-391;
   - the Opal path, `run_opal(...)`, around :445-447.

   Each calls `self.store.put_state(request_id, "READY", receipt)` (`durable_job.py:138-157`, table `irpt-jobs`). The worker already
   reads the acceptance record via `DynamoAcceptance.get(tenant, request_id)` (`acceptance.py:68-71`; the worker calls it at :590).
   - When that record carries `ticket_id`, add `ticket_id` to the READY receipt (the `job_detail`) on BOTH paths.
   - When it does not, the receipt stays byte-identical to today.
   - Do not change what `put_state` requires for READY (`report_id`, `revision`, `certification_sha256`), and do not change its
     condition.
2. **Send I3 once.** After the READY write succeeds, on BOTH paths, send exactly
   `queue_message("analysis_ready", {"tenant": tenant, "request_id": request_id})`.
   - Import it from `infra/aws/lambda/investor-reporting/_keys/keys.py:551`, the same way the worker already builds `analysis_generate`
     (around :583-588).
   - Add NO other field. `ticket_id` is NOT in the message; the consumer reads it from the records (I2).
   - The send goes through an INJECTED port, the same shape as `DynamoAcceptance.dispatch(..., send, queue_url)`
     (`acceptance.py:134-157`): `send(queue_url, body)`. The live wiring passes the boto SQS `send_message`.
   - The queue URL comes from the environment variable `IRPT_ANALYSIS_READY_QUEUE_URL`. AR-t-11 (~T2) creates the queue; its name is
     wired at the release.
   - When that variable is unset or empty, READY still succeeds, nothing is sent, and the worker logs one line beginning
     `WARN: ANALYSIS_READY_QUEUE_UNSET`. This is the pre-wiring state, and it must never fail the job.
   - A send that raises must NOT undo or fail the READY write. Log one `ERROR: ANALYSIS_READY_SEND_FAILED <request_id>` line.
3. **Never twice.** The redelivery path, `ResidentAssembly.execute` around :613-628, acknowledges a job that is already READY without
   writing again. It must also send NO second `analysis_ready`.
   - If you find that "sent" must be recorded to make a lost send recoverable, do not add a new table or field. File a row and keep
     the rule: one send, after the first READY write.
4. **Test.** Add `generate/tests/test_ready_signal.py`. It is offline, with fakes only, reusing the fixtures that
   `generate/tests/test_resident_worker.py` uses for the Opal path (`opal_installed`, around :702) and the vendor READY test (:199).
   It proves:
   - (a) an Opal-path READY for a record carrying `ticket_id` writes a receipt that carries it, and sends exactly one body equal to
     `queue_message("analysis_ready", {...})`, byte for byte;
   - (b) a READY for a record WITHOUT `ticket_id` writes the receipt byte-identical to today's, and still sends one `analysis_ready`;
   - (c) with `IRPT_ANALYSIS_READY_QUEUE_URL` unset, READY is written, zero sends are made, and the WARN line is logged;
   - (d) a redelivered, already-READY job makes zero sends;
   - (e) a send that raises leaves the job READY and logs the ERROR line.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR11-g-AC1" cell_refs="AR-g-11"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py g11</invocation><expect>^AR1-G2-G11-OK</expect></criterion>

<criterion id="AR11-g-AC2" cell_refs="AR-g-11"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py regress</invocation><expect>^AR1-G2-REGRESS-OK</expect></criterion>

<expected_criteria>AR11-g-AC1,AR11-g-AC2</expected_criteria>

- **AC1:** `test_ready_signal.py` shows at least 4 passed and 0 failed. At the base it FAILs because the file is absent (issuer dry
  run).
- **AC2:** no test file in the generate or research suites is newly red against the base. Base: generate is red only in
  `test_custody_retained.py` and `test_custody_entry.py` (34 ids, custody work in flight elsewhere); research shows 165 passed. The
  issuer's dry run reads `AR1-G2-REGRESS-OK`.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no upload, no AWS calls, no installs.
- Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W61-S<k>`. File them in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`,
  using the next unused k across the document; create it if absent, in the shape of
  `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~61" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~61@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~61 <0.9.0_WK_IRPT_ANLREQ~61@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool.
  - Do not pre-`git add`.
  - Edit byte-preserving, ASCII only.
  - Use the native Grep/Glob/Read tools.
  - `resident_worker.py` sits in lane IRPT_Y_ACCESS_INTEGRATION_P. If owned-paths refuses it, commit with
    `GIT_COMMIT_AUTHOR_OVERRIDE=IRPT_Y_ACCESS_INTEGRATION_P` (audited; CTO msg 1374 precedent), that file in a commit of its own.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_ready_signal.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-11.ready-names-ticket-and-signals-once.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R1.md</decomp_doc> round 1, workstream ~G, cell `AR-g-11`.
<owned_cells>AR-g-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR11-g-AC1, AR11-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~61/IRPT_ANLREQ.TO-AR-g-11.ready-names-ticket-and-signals-once.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> AR11-g-AC1,AR11-g-AC2` BEFORE the flip to complete. Shape:
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~223/IRPT_BCKEND.TO-IB-yr-761.install-custody-factory.proof_of_spec.json`.
Commit the code first, then pin each artifact to a commit that contains it.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the two READY sites and where the send sits after each;
- the redelivery rule;
- the log lines;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one optional receipt field on the irpt-jobs READY row and one closed queue message after READY. resident_worker.py ships in the resident package (build_resident_package.py), deployed only by a later release pair; nothing deploys in this cell. With the env unset (pre-wiring) the only change is the receipt field.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added; the resident role's SendMessage on the analysis_ready queue is AR-t-11's queue-policy statement.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the message is the trigger AR-t-11 subscribes to.
comp-adversary: RUN -- the code map was read (resident_worker.py :388-391, :445-447, :583-590, :613-628; durable_job.py :138-157; acceptance.py :68-71, :134-157; keys.py :551). Traps: a ticket_id leaking into the message, a second send on redelivery, a send failure failing READY, the pre-wiring state failing jobs. Arms (a)-(e) cover each. AC1 FAILs at base; AC2 is OK at base.
lane: workstream ~G scope per the decomposition (resident_worker.py); the <paths> block IS the grant (worker_grant).
</preflight>

Source: IRPT_ANLREQ decomposition round 1 cell AR-g-11, interfaces I2 and I3 (@8412208d47); 2.0.0_SA_COO~Y2 msg 2487.
