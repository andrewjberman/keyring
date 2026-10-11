# TO-YCD-e-11 -- a generation job whose message is about to be dead-lettered records FAILED with a closed cause (row D2-S49)

<to_id>IRPT_YCDGEN.TO-YCD-e-11</to_id>
<project>IRPT_YCDGEN</project>
<issued_to>0.9.0_WK_IRPT_YCDGEN~15</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `YCD-e-11` (`decompositions/IRPT_YCDGEN_DECOMP_R11.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none.

---

## WORKER FACE

### Read first

Under `infra/aws/lambda/investor-reporting/ycharts/generate/`: `resident_worker.py` `poll_once` (search `def poll_once`), and in the same file
`_end_permanently_refused`, `_end_exhausted_resolve` and `RESOLVE_MAX_RECEIVES` (the pattern to follow: a job is ended in its
own state row with a code); `durable_job.py` (`STATES`, `claim`, `put_state`, `get_state`, `release`); `resident_main.py`
(how `poll_once` is called and what it does with an exception); and `infra/aws/terraform/investor-reporting/core/sqs.tf`
(the redrive policy: `maxReceiveCount = 5`). Row `IRPT_YCDGEN-D2-S49` in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` states the finding.

### THE CELL

Measured on 2026-10-11: 8 of 8 messages in the generation dead-letter queue belong to jobs whose record still reads state
RECEIVED, and a job record has no field that says why. A job that raises on every delivery is retried by the queue, moved
to the dead-letter queue after its fifth receive, and its record never changes. Make the record say what happened.

1. In `poll_once`, for a message of kind `analysis_generate` ONLY: when `assembly.execute` raises and the envelope's
   `ApproximateReceiveCount` is at or above a new module constant `GENERATE_MAX_RECEIVES = 5` (commented with the
   Terraform file and line it mirrors), the worker writes the job's state as `FAILED` with detail
   `{"code": "DELIVERIES_EXHAUSTED", "cause": <a closed token>, "receives": <the count>}`, prints one journal line
   `IRPT_RESIDENT_JOB state=FAILED code=DELIVERIES_EXHAUSTED cause=<token> receives=<n> <request id>`, and then RE-RAISES
   the original exception unchanged.
2. `cause` is the exception's CLASS NAME when it matches `[A-Za-z][A-Za-z0-9_]{0,63}`, else `UNCLASSIFIED`. Never the
   exception's message: a message can carry a client's or a security's name.
3. The message is NOT deleted and its visibility is NOT changed by this branch. The queue still dead-letters it; this cell
   adds the record, it does not change delivery.
4. Below the limit nothing changes: the exception propagates exactly as today and no state is written.
5. A job already `READY`, `ATTENTION` or `FAILED` keeps its state. If writing the state itself raises, the ORIGINAL
   exception still propagates (the second error is printed as one line with its class name and is not raised).
6. Every other message kind (`resolve_upload`, any other) behaves byte-for-byte as today. `ReadBackPending` keeps its own
   handling: read how it leaves `poll_once` today and do not record FAILED for it unless the count is at the limit.
7. Use the store's existing claim and release (`_end_permanently_refused` shows the form). Add no new table field: the
   detail goes where `put_state` already puts a detail.
8. Tests, offline, in a NEW file `infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_dead_letter_record.py`, with fakes in the style of
   `test_resident_worker.py`: (a) at the limit the state is FAILED with the three detail keys, the journal line is printed,
   the exception is re-raised, and neither `delete_message` nor `change_message_visibility` was called by the new branch;
   (b) one below the limit nothing is written; (c) a `resolve_upload` message at the limit is untouched by the new branch;
   (d) a job already READY keeps READY; (e) a failing state write still re-raises the original exception; (f) an exception
   whose class name is not a closed token records `UNCLASSIFIED`. Keep every other test in the folder green.

Say in your report what the status route shows a caller for a FAILED job today (read the reader; do not change it).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="E11-AC1" cell_refs="YCD-e-11"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/r11_checks.py e11</invocation><expect>^R11-E11-OK</expect></criterion>

<criterion id="E11-AC2" cell_refs="YCD-e-11"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~G2/r11/r11_checks.py e11suite</invocation><expect>^R11-E11SUITE-OK</expect></criterion>

<expected_criteria>E11-AC1,E11-AC2</expected_criteria>

- AC1 imports `resident_worker`, reads `GENERATE_MAX_RECEIVES == 5`, and runs the new test file: 0 failed, at least 6
  passed. At base it FAILs (no constant, no file).
- AC2 runs the whole `ycharts/generate/tests` folder: 0 failed, 0 errors, at least 503 passed (it reads 497 at base). At
  base it FAILs on the count.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Every `.py` edit passes
  `.tools/commit-gate.sh`. This cell ships to the host only in a later resident release under its own pair.
- **Refusal clause.** If a criterion cannot be met as written, or the commit is refused because these files are another
  project's lane: stop, file a row with the refusal text, report, and do not weaken a check or force a commit.
- **Rows** are `IRPT_YCDGEN-D2-W15-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel
  file below. Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type
  a time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_YCDGEN~15" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_YCDGEN~15@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_YCDGEN~15 <0.9.0_WK_IRPT_YCDGEN~15@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_dead_letter_record.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~15/
org/missions/D9/IRPT/IRPT_YCDGEN/task-orders/IRPT_YCDGEN.TO-YCD-e-11.dead-lettered-job-states-its-failure.md
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R11.md</decomp_doc> round 11, cell `YCD-e-11`.
<owned_cells>YCD-e-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E11-AC1, E11-AC2. Instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~15/IRPT_YCDGEN.TO-YCD-e-11.dead-lettered-job-states-its-failure.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_YCDGEN.TO-YCD-e-11`.
- Validate with `python .tools/proof-of-spec-check.py <instance> E11-AC1,E11-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~13/IRPT_YCDGEN.TO-YCD-a-10.page-sentence-per-cause-no-raw-string.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the change to `poll_once`, with the lines;
- how `ReadBackPending` leaves `poll_once` and what you did about it;
- what the status route shows for a FAILED job today;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one branch of poll_once in ycharts/generate/resident_worker.py, for one message kind, at the receive limit only; it writes the job's own state row and re-raises. Below the limit and for every other kind the path is unchanged. Ships only in a later resident release under its own pair; nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the worker already writes its job row.
comp-routes: DECLARED-NOT-APPLICABLE -- no route.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read poll_once (the resolve_upload branch already ends a job at RESOLVE_MAX_RECEIVES), _end_permanently_refused and core/sqs.tf maxReceiveCount 5. Traps: deleting the message and so emptying the dead-letter queue the redrive hazard row inventories; printing an exception message that names a client; recording FAILED over READY; swallowing the original exception; counting ReadBackPending's planned retries as failures.
lane: ycharts/generate/resident_worker.py -- the resident worker; if the owned-paths gate names another project's lane the worker stops and the issuer re-points.
</preflight>

Source: CTO round-11 analysis @457305b604 section 3 item 2 and section 4 item 5; row IRPT_YCDGEN-D2-S49.
