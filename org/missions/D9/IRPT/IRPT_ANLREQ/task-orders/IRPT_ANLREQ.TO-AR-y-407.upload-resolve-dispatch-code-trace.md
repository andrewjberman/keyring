# TO IRPT_ANLREQ.TO-AR-y-407.upload-resolve-dispatch-code-trace -- READ ONLY: trace in the code how a RESOLVING upload becomes NORMALIZED (the dispatch from the upload door, the queue, the resident handler, the journal literal), so the issuer can say why five identical re-posts over 20 s answered RESOLVING with no resolve line in the resident journal

<to_id>IRPT_ANLREQ.TO-AR-y-407</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~298</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ67</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (read-only; one record file and optional surprise rows)
**Decomp cell:** `AR-y-407` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (CTO ruling ADDENDUM 4, msg 10731)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~298`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-298` (branch `wk-IRPT_ANLREQ-298`), provisioned by the issuer from the current branch (sparse). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~298 <0.9.0_WK_IRPT_ANLREQ~298@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture: never commit it. A row id has the form `IRPT_ANLREQ-D2-W298-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions) and give each row the class OBSERVATION. No non-ASCII in what you add.
- **READ ONLY.** You change no source file, run no AWS call, no network call, no deploy. You write ONE record file and, if you find something odd off the task, rows. Read code with the Read, Grep and Glob tools (a named folder or file at a time, never a blind search of the whole repository) and `git show HEAD:<path>`; cite every answer as `<path>:<line>` read from the file at HEAD of your worktree (print the line, do not recall it).

### THE CELL (AR-y-407, inlined)

*Context.* A synthetic run (IB2, order `org/tier2_senior/0.7.0_AE_CloudOps~IB2/task_orders/IRPT_ANLREQ.TO-RUN-COMMENTARY-E2E-3.fresh-synthetic-commentary-end-to-end-resolving-repost-ib2.md`, receipt `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e3/A_E2E3.txt`) posted one upload and re-posted the identical request four more times, 3 s apart; all five answers were `RESOLVING`, no `input_id`, and the resident journal showed no line naming a resolve step. The run reused an earlier run's (deleted) upload token. Window 4 (2026-10-16) also showed 45 resident POLL lines and no RESOLVE (surprise investigation lines 22817-22823 of `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`). The door side is `infra/aws/lambda/investor-reporting/intake/uploads.py`: the upload POST publishes a `RESOLVING` row (about lines 486-516) and dispatches one request to resolve it (`_dispatch`, the guard `self.request_resolution is not None` at about :528); an identical re-post of a RESOLVING row answers `RESOLVING` and re-dispatches only after `REDRIVE_SECONDS` since `dispatched_at` (:526-533); the resident half is `resolve_deferred` (about :546-). The resident's loop is `infra/aws/lambda/investor-reporting/ycharts/generate/resident_main.py` and `resident_worker.py` (a generation queue poll, `poll_once`, the `IRPT_RESIDENT_POLL` literal, a `_end_exhausted_resolve` helper at about :1080); the queue wiring and the resolve request port are in `infra/aws/lambda/investor-reporting/ycharts/generate/entry.py` and the Lambda that serves the upload route (`intake/upload_entry.py`), and the upload resolution state is `intake/upload_resolution.py` (`RESOLVING`, `REDRIVE_SECONDS`, `NORMALIZED`).

*Questions. Answer each in ONE line of the record, labelled `X1` to `X6`, each line holding at least one `<file>.<ext>:<line>` citation (py, tf, md):*
- `X1` THE DISPATCH: what `_dispatch` does at the upload door (the message, the queue or function it sends to, the env name or port that carries the target, the line where `request_resolution` is set for the deployed Lambda and what it is set to; and the condition under which it is None).
- `X2` THE REDRIVE: from `_answer` (about :518-533), exactly when a re-post re-dispatches (the `REDRIVE_SECONDS` value, what `dispatched_at` holds right after the first post) and therefore how many dispatches five posts over 20 s cause.
- `X3` THE CONSUMER: which process receives the resolve request and where (the queue name or the function), its message kind literal, and the line where it calls `resolve_deferred` or the equivalent; whether that consumer is the resident host's loop, a Lambda, or something else, and its journal or log literal for a resolved or refused upload (the exact string it prints).
- `X4` THE FRESH-TOKEN KEY: how the upload id and the resolution row key are derived (the inputs; cite `uploads.py:371` and the row key lines), and what a re-use of a DELETED token does (the row is absent: does the door create a new RESOLVING row and dispatch, or does something refuse or skip); so whether run 3's token reuse could have suppressed the dispatch, from the code.
- `X5` THE TERRAFORM WIRING: the queue, event source mapping, environment variable and IAM statement that connect X1 to X3 in Terraform (cite the `.tf` files under `infra/aws/terraform/investor-reporting/`), and which of them the code needs to be set for a dispatch to arrive.
- `X6` THE POSITIVE CONTROL SPEC: the exact literal strings and queue or table the issuer must count in the live resident journal and queue for Andrew's 13:43Z filing (the `IRPT_RESIDENT_POLL` handled=N line, the resolve literal from X3, any `retained_for_retry` literal on the resolve path), and which table row (key shape, state field) proves a resolved upload, so a live read-only order can be written from this line alone.

Anything you cannot answer from the code is written `X<k> NOT READ <what is missing>`; a guess is a defect. Write no secret and no client data.

---

## ACCEPTANCE

Record file: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~298/r56/RESOLVE_PATH_TRACE.md` (create the folder). It holds a first line `# resolve path` and then exactly the six lines `X1` to `X6`, each starting at column 0 with its label and a space, each answer on that single line.

<criterion id="AR407-y-AC1" cell_refs="AR-y-407"><invocation>grep -c -E "^X[1-6] " org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~298/r56/RESOLVE_PATH_TRACE.md</invocation><expect>^6$</expect></criterion>
<criterion id="AR407-y-AC2" cell_refs="AR-y-407"><invocation>grep -c -E "^X[1-6] .*[A-Za-z_0-9]+\.(py|tf|md):[0-9]+" org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~298/r56/RESOLVE_PATH_TRACE.md</invocation><expect>^[5-6]$</expect></criterion>

`AR407-y-AC1`: the six labelled answers exist; at base the record is absent and it FAILS. `AR407-y-AC2`: at least five of the six lines carry a `file:line` citation; at base it FAILS. After the record, run each grep once more on a copy with the X4 line removed (AC1 must then read 5) as the mutant control, and run AC1 twice for determinism.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~298/IRPT_ANLREQ.TO-AR-y-407.upload-resolve-dispatch-code-trace.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-407`. Copy its shape from `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/IRPT_ANLREQ.TO-AR-y-402.original-holdings-blob-delete-path-code-and-policy-read.proof_of_spec.json` (it needs `controls.mutant` FIRED-AS-EXPECTED and `controls.determinism` STABLE, both really run). Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> "AR407-y-AC1,AR407-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-407</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~298/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-407.upload-resolve-dispatch-code-trace.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of code and Terraform and one record file; nothing is built, uploaded, planned, applied, invoked or called.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; policy is read from Terraform source only.
comp-adversary: RUN -- a literal recalled instead of read (each string is printed from the file), a zero written without the folders read (invalid), a guess written as a finding (NOT READ is the honest answer), a test's mock read as the production wiring (cite the deployed module and the .tf), run 3's token reuse taken as the cause without X4's code reading. NOT seen (blind): the live queue, the live journal and the applied environment; denominator: six questions, two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ADDENDUM 4 (msg 10731): trace the resolve dispatch for a fresh token, and give the positive control for Andrew's 13:43Z filing; a fresh-token run 4 follows under a pair addendum. The issuer's own omission: the run 3 order did not require a fresh upload token, so IB2 reused run 2's. Base: the record is absent, so `AR407-y-AC1` and `AR407-y-AC2` FAIL as expected.
