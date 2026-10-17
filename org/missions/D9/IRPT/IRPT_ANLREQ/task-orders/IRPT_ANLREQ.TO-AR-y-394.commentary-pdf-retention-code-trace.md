# TO IRPT_ANLREQ.TO-AR-y-394.commentary-pdf-retention-code-trace -- READ ONLY: trace in the code why the resident's commentary PDF is retained for no request (0 of 206, 210 and 33 artifact items), from the commentary-ready trigger to the retention write, with a file:line for every answer

<to_id>IRPT_ANLREQ.TO-AR-y-394</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~292</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ55</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (read-only code trace; one record file and optional surprise rows)
**Decomp cell:** `AR-y-394` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the ticket's commentary PDF opens) | **depends_on:** none (CTO msg 10630 ruled it top priority)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~292`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-292` (branch `wk-IRPT_ANLREQ-292`), provisioned by the issuer from the current branch (sparse). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~292 <0.9.0_WK_IRPT_ANLREQ~292@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. The workspace may show ` M portal` and a modified `.parquet` fixture: never commit either. A row id has the form `IRPT_ANLREQ-D2-W292-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `INVESTIGATION_v1.md` (0 deletions). No non-ASCII in what you add. Commit the record, then validate (below).
- **READ ONLY.** You change no source file, run no AWS call, no network call, no deploy, no test that writes outside the worktree. You write ONE record file and, if you find something odd off the task, rows. Read code with the Read, Grep and Glob tools and `git show HEAD:<path>`; cite every answer as `<path>:<line>` read from the file at HEAD of your worktree (print the line, do not recall it).

### THE CELL (`AR-y-394`, inlined)

*Context.* The irpt-status Lambda now reads a request's `commentary_ref` and resolves the commentary PDF at `ops/owned_report.py:335-379` (`OwnedAnalysisReader.commentary_pdf`) as the artifact of family `YCHARTS_OPAL_REPORT` whose logical id is `<request id>-commentary-<sha256>` (`owned_report.py:119-124`; the artifact id is `repository.py:390-395` `_binding(owner, family, logical_id)`). The issuer's live reads found NO such artifact for any request: 0 matched of 206, 210 and 33 artifact items in the three tenants. The PDF is meant to be rendered and retained by `ycharts/research/opal_producer.py` (`commentary_logical_id` at :372, `produce_package` at :377, `produce_commentary_pdf` at :430, the `artifacts.put` retention at about :417 and :461), called from `ycharts/research/opal_packager.py` (`handle_commentary_ready`; the call `produce(request_ref, tenant, stores, commentary, commentary_sha256=commentary_sha)` at about :199; `live_retained_package` at :240-262), which runs in the resident host: `ycharts/generate/resident_worker.py` and `reports/resident_installed.py`. The commentary DRAFT is stored by `reports/commentary_draft_store.py` (the draft artifact is family `ANALYSIS_COMMENTARY`, logical id = the request id; the `commentary_ref` sibling attribute {artifact_id, sha256, version_id} is set once on the request item).

*Questions. Answer each in ONE line of the record, labelled `T1` to `T6`, each line holding at least one `<file>.py:<line>` citation:*
- `T1` WHAT TRIGGERS the packager's commentary path: the message kind or poll that calls `handle_commentary_ready`, and which component enqueues it (name the sender function and the queue or table it uses).
- `T2` WHERE the commentary text and `commentary_sha256` come from inside `handle_commentary_ready`, and how they relate to the stored `commentary_ref.sha256` (equal, or different) so the logical id the producer writes under equals the one the route reads.
- `T3` WHICH STORE the PDF is written to: `stores["artifacts"]` (the repository: table, S3 key shape) or the `stores["objects"]` branch (the S3 key shape, which bucket env name); and which of the two the resident's wiring (`resident_worker.py`, `resident_installed.py`) actually injects.
- `T4` EVERY condition before the write that returns, skips or raises (each early `return`, `raise`, disabled flag or env switch on that path), one entry each, with its line.
- `T5` WHICH RELEASE of the resident carries this path: the function map or tarball record that stages `opal_packager.py`, `opal_producer.py` and the draft store into the resident (name the file and the pin or the staged_from row), and whether the staged pins include the artifacts-port branch of `produce_package`.
- `T6` Whether the commentary-ready trigger of T1 is ever sent for a READY analysis request in the code's own flow (name the line where a READY job leads to the send), or only after a step this flow does not take.

Anything you cannot answer from the code is written `T<k> NOT READ <what is missing>`; a guess is a defect. Do not write any client data, ticket text or bearer.

---

## ACCEPTANCE

Record file: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~292/r51/TRACE_COMMENTARY_PDF_RETENTION.md` (create the folder). It holds a first line `# trace` and then exactly the six lines `T1` to `T6`, each starting at column 0 with its label and a space.

<criterion id="AR394-y-AC1" cell_refs="AR-y-394"><invocation>grep -c -E "^T[1-6] " org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~292/r51/TRACE_COMMENTARY_PDF_RETENTION.md</invocation><expect>^6$</expect></criterion>
<criterion id="AR394-y-AC2" cell_refs="AR-y-394"><invocation>grep -c -E "^T[1-6] .*[A-Za-z_]+\.py:[0-9]+" org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~292/r51/TRACE_COMMENTARY_PDF_RETENTION.md</invocation><expect>^[56]$</expect></criterion>

`AR394-y-AC1`: the six labelled answers exist; at base the record is absent and it FAILS. `AR394-y-AC2`: at least five of the six lines carry a `file.py:line` citation (a line written `NOT READ` may carry none); at base it FAILS.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~292/IRPT_ANLREQ.TO-AR-y-394.commentary-pdf-retention-code-trace.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-394`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR394-y-AC1,AR394-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-394</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, the deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~292/`, this order's file (status line only) and the surprise investigation file are the only places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~292/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-394.commentary-pdf-retention-code-trace.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of code and one record file; nothing is built, uploaded, planned, applied or invoked.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call.
comp-adversary: RUN -- a citation recalled instead of read (each line is printed from the file), a guess written as a finding (NOT READ is the honest answer), a read of the wrong release (the worktree's HEAD is the trunk; T5 names the staged pins separately), client data copied into the record (forbidden). NOT seen (blind): the live resident host and any live table; denominator: six questions, two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (msg 10630, top priority) after the issuer's live reads (row `IRPT_ANLREQ-D2-S207`). The issuer does the live half in parallel (the READY request's item, job row, queue and log counts). The answer feeds a possible WORLD fix cell with its own pair. Base: the record is absent, so `AR394-y-AC1` and `AR394-y-AC2` FAIL as expected.
