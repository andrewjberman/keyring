# TO IRPT_ANLREQ.TO-AR-y-398.synthetic-commentary-e2e-run-specification-read -- READ ONLY: from the code and the earlier run records, specify the fresh synthetic commentary end-to-end run (CTO ruling addendum 1, msg 10652): the submit call, the actor's auth, the polls, the timings and the delete inventory, with a file:line for every answer

<to_id>IRPT_ANLREQ.TO-AR-y-398</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~293</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ59</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (read-only; one record file and optional surprise rows)
**Decomp cell:** `AR-y-398` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the ticket's commentary PDF opens) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~293`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-293` (branch `wk-IRPT_ANLREQ-293`), provisioned by the issuer from the current branch (sparse). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~293 <0.9.0_WK_IRPT_ANLREQ~293@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. A row id has the form `IRPT_ANLREQ-D2-W293-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions). No non-ASCII in what you add.
- **READ ONLY.** You change no source file, run no AWS call, no network call, no deploy. You write ONE record file and, if you find something odd off the task, rows. Read code with the Read, Grep and Glob tools (a named folder or file, never a blind search of the repository) and `git show HEAD:<path>`; cite every answer as `<path>:<line>` read from the file at HEAD of your worktree (print the line, do not recall it).

### THE CELL (AR-y-398, inlined)

*Context.* The CTO ruled (msg 10652, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/1.0.0_SA_CTO~DELL2/RULING_COMMENTARY_GAP_TWO_CAUSES_20261017.md` ADDENDUM 1) that ONE fresh synthetic request with `commentary_requested: true` and a live synthetic actor is run through the resident, the drafter and the packager, ending at a read of the commentary route `GET /api/scoped/investor-reporting/analysis/requests/{requestId}/commentary-pdf`. The portal never sets `commentary_requested` (the wire type is `portal/src/pages/InvestorReporting/contracts/wire/AnalysisSubmissionRequest.ts:23`), so the run must file the request by an HTTP call that carries the field. Earlier synthetic runs (windows 4 and 5, orders `org/tier2_senior/0.7.0_AE_CloudOps~IB2/task_orders/IRPT_ANLREQ.TO-RUN-FWD1.fwd1-staff-filing-window4-ib2.md` and `...window5-ib2.md`) file through the Ticket Center UI with a browser driver (`fwd1_driver.mjs`, its folder is named in the window-5 order) after minting a synthetic staff user and advisor (`0.9.0_WK_IRPT_ANLREQ~167/test_fwd1_mint.py` and `0.9.0_WK_IRPT_ANLREQ~172/fwd1_advisor.py` under `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/`; the mint scripts' exact paths are in those orders). The backend that admits the field is `infra/aws/lambda/investor-reporting/ycharts/generate/submission.py` and `acceptance.py`; the Lambda route table is `infra/aws/lambda/investor-reporting/ops/entry.py` (about lines 230-260) and the packager chain is as in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~292/r51/TRACE_COMMENTARY_PDF_RETENTION.md`.

*Questions. Answer each in ONE line of the record, labelled `U1` to `U6`, each line holding at least one `<file>.<ext>:<line>` citation (py, ts, tsx, mjs or md):*
- `U1` THE SUBMIT CALL: the method and path of the route that files an Analysis Request, and every body key the validator admits or requires (name each, with `commentary_requested`), where the holdings come from (the upload route and the `input_id` it returns, and the upload's body keys), and which other calls the portal makes between login and the submit; cite the portal endpoint module and the Lambda validator.
- `U2` THE ACTOR AND ITS AUTH: how a synthetic staff user is minted today (the script name and function) and how a script (not a browser) obtains the credential the API accepts for that user (cookie, bearer, or header name, and the login route and body keys); do NOT print or read any secret value, name only the fields.
- `U3` THE POLLS: the reads that show each hop done, in order: the job row state READY, the request item's `commentary_ref`, the draft artifact, the `commentary_ready` message, the PDF artifact under family YCHARTS_OPAL_REPORT with logical id `<request id>-commentary-<sha256>`, and the route answer; for each the table, key shape and the closed field to read.
- `U4` THE DELETE INVENTORY: every object one run creates (user and partner rows, upload, request item, job row, artifact index items and their blobs, queue messages, ticket) and for each how it is removed (the existing script and function, or a gap with no remover); list the gaps plainly.
- `U5` THE INPUTS: the minimal valid holdings bytes and body for a request that the resident will render (take them from the window-5 order's step 5 holdings and the driver's submit), and whether `ticket_id` is required for `send_ready_if_ticketed` to fire (`ycharts/generate/resident_worker.py:247-258`) and how a synthetic ticket id is made.
- `U6` THE TIMINGS: the observed duration of each hop in the window-4 record (upload, accept, resident render to READY, the drafter, the packager poll) and the poll intervals in the code (`resident_main.py` loop wait, the packager's `VisibilityTimeout`), so a poll budget can be stated; if the window-4 record carries no timing for a hop, write `NOT READ` for that hop.

Anything you cannot answer from the code is written `U<k> NOT READ <what is missing>`; a guess is a defect. Write no secret, bearer, password, email beyond the `@opal.invalid` synthetic pattern, or client data.

---

## ACCEPTANCE

Record file: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~293/r52/E2E_RUN_SPECIFICATION.md` (create the folder). It holds a first line `# specification` and then exactly the six lines `U1` to `U6`, each starting at column 0 with its label and a space, each answer on that single line.

<criterion id="AR398-y-AC1" cell_refs="AR-y-398"><invocation>grep -c -E "^U[1-6] " org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~293/r52/E2E_RUN_SPECIFICATION.md</invocation><expect>^6$</expect></criterion>
<criterion id="AR398-y-AC2" cell_refs="AR-y-398"><invocation>grep -c -E "^U[1-6] .*[A-Za-z_0-9]+\.(py|ts|tsx|mjs|md):[0-9]+" org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~293/r52/E2E_RUN_SPECIFICATION.md</invocation><expect>^[5-6]$</expect></criterion>

`AR398-y-AC1`: the six labelled answers exist; at base the record is absent and it FAILS. `AR398-y-AC2`: at least five of the six lines carry a `file:line` citation (a line written `NOT READ` may carry none); at base it FAILS.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~293/IRPT_ANLREQ.TO-AR-y-398.synthetic-commentary-e2e-run-specification-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-398`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR398-y-AC1,AR398-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-398</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, the deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~293/`, this order's file (status line only) and the surprise investigation file are the only places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~293/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-398.synthetic-commentary-e2e-run-specification-read.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of code and run records and one record file; nothing is built, uploaded, planned, applied, invoked or called.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- a citation recalled instead of read (each line is printed from the file), a guess written as a finding (NOT READ is the honest answer), a secret or password copied into the record (forbidden: field names only), a route inferred from a test's mock instead of the route table. NOT seen (blind): the live system; denominator: six questions, two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (msg 10652) so the issuer can write the never-widen pair and the IB2 run order from a specification, not from memory. Base: the record is absent, so `AR398-y-AC1` and `AR398-y-AC2` FAIL as expected. After the worker: the issuer checks the citations, writes the COO half of the pair (synthetic only, outside the band, one actor kept until the route read, the packager journal line in the receipt, delete list with keys), sends the CTO the packet blob, and cuts `TO-RUN-COMMENTARY-E2E` to `0.7.0_AE_CloudOps~IB2`.
