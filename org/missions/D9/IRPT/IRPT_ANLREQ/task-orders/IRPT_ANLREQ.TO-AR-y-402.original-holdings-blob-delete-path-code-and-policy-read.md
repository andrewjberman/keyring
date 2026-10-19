# TO IRPT_ANLREQ.TO-AR-y-402.original-holdings-blob-delete-path-code-and-policy-read -- READ ONLY: which principal, if any, the application deletes objects under irpt/<firm>/state/original_holdings/ with (code and policy only), and whether a re-post of the same upload lands on the same ART- key

<to_id>IRPT_ANLREQ.TO-AR-y-402</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~295</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ63</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (read-only; one record file and optional surprise rows)
**Decomp cell:** `AR-y-402` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none (CTO msg 10668, item 2)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~295`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-295` (branch `wk-IRPT_ANLREQ-295`), provisioned by the issuer from the current branch (sparse). First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~295 <0.9.0_WK_IRPT_ANLREQ~295@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. A row id has the form `IRPT_ANLREQ-D2-W295-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions). No non-ASCII in what you add.
- **READ ONLY.** You change no source file, run no AWS call, no network call, no deploy. You write ONE record file and, if you find something odd off the task, rows. Read code and Terraform with the Read, Grep and Glob tools (a named folder or file at a time, never a blind search of the whole repository) and `git show HEAD:<path>`; cite every answer as `<path>:<line>` read from the file at HEAD of your worktree (print the line, do not recall it).

### THE CELL (AR-y-402, inlined)

*Context.* A synthetic run (IB2, order `org/tier2_senior/0.7.0_AE_CloudOps~IB2/task_orders/IRPT_ANLREQ.TO-RUN-COMMENTARY-E2E-2.fresh-synthetic-commentary-end-to-end-with-advisor-ib2.md`, receipt dir `org/tier2_senior/0.7.0_AE_CloudOps~IB2/deliverables/irpt_anlreq_commentary_e2e2/`, file `LEFTOVER.txt`) uploaded one 118-byte holdings CSV through `POST /api/scoped/investor-reporting/analysis/inputs` and could not delete the stored original afterwards: `AccessDenied` on `s3:DeleteObject` for the key `irpt/49financial/state/original_holdings/ART-<id>/<file>.csv` for IB2's principal. The blob is written by the upload door (`infra/aws/lambda/investor-reporting/intake/uploads.py`, the `artifacts.put` at about :398 for the original and :468 for the normalized portfolio) into the retained-artifact repository (`infra/aws/lambda/investor-reporting/reports/repository.py` `ArtifactRepository.put` from about :397, retention bookkeeping in `reports/retention.py`, composition in `reports/composition.py:50-58`). The artifact id is the repository's own binding: `repository.py:390-395` `_binding(owner, family, logical_id)` returns `"ART-" + digest({owner, family, logical_id})`. The S3 key shape comes from `lib/opal_naming.py` (about :2650-2665, per worker 292's trace). The Terraform roots are under `infra/aws/terraform/investor-reporting/` (for example `ops/iam.tf` lines 74-89 grant the status Lambda read of this family; `intake/iam.tf` lines 10-37 is the intake poller's grant and says it has no `s3:DeleteObject`; the roots that grant the upload door's and the resident's roles are to be found by Grep over named subfolders).

*Questions. Answer each in ONE line of the record, labelled `W1` to `W5`, each line holding at least one `<file>.<ext>:<line>` citation (py, tf, md):*
- `W1` THE WRITER: which Lambda or role writes the original-holdings object (the function and the role name or Terraform resource), and the S3 actions its policy grants on the key prefix `irpt/<firm>/state/original_holdings/*` (cite the policy statement and its actions; names only).
- `W2` THE DELETER IN CODE: every place the application's code deletes an S3 object or object version of any retained-artifact family (a `delete_object`, `delete_objects` or a version delete), or says it never does; cite the line or the sentence that says so, and name the module that would do it for a retention expiry (`reports/retention.py` or other).
- `W3` THE DELETER IN POLICY: every Terraform resource that grants `s3:DeleteObject` or `s3:DeleteObjectVersion` on the bucket or this prefix to any role, and every S3 lifecycle rule (`aws_s3_bucket_lifecycle_configuration`) that expires objects under it, with the role or rule name and its prefix/age; if none is found in the roots read, write `NOT FOUND in <the folders read>` with the list of folders read as the denominator (a zero without a denominator is invalid).
- `W4` THE SAME KEY: whether a second identical upload POST (same upload token, same body) lands on the same `ART-` key: from `uploads.py` and `repository.py:390-395`, what the logical id of the original-holdings object is made of (the inputs to the digest) and whether those inputs are identical for an identical re-post, and what the repository does when an object with that id already exists (the conditional-put or return-existing path, with the line).
- `W5` THE ANSWER: one clause each for (a) the principal the application itself deletes this prefix with, or `NONE FOUND`; (b) whether a synthetic blob is therefore deletable by any existing path, or is a standing leftover until a retention or lifecycle rule (named, or `NONE FOUND`) removes it.

Anything you cannot answer from the code is written `W<k> NOT READ <what is missing>`; a guess is a defect. Write no secret and no client data.

---

## ACCEPTANCE

Record file: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/r54/ORIGINAL_HOLDINGS_DELETE_PATH.md` (create the folder). It holds a first line `# delete path` and then exactly the five lines `W1` to `W5`, each starting at column 0 with its label and a space, each answer on that single line.

<criterion id="AR402-y-AC1" cell_refs="AR-y-402"><invocation>grep -c -E "^W[1-5] " org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/r54/ORIGINAL_HOLDINGS_DELETE_PATH.md</invocation><expect>^5$</expect></criterion>
<criterion id="AR402-y-AC2" cell_refs="AR-y-402"><invocation>grep -c -E "^W[1-5] .*[A-Za-z_0-9]+\.(py|tf|md|json):[0-9]+" org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/r54/ORIGINAL_HOLDINGS_DELETE_PATH.md</invocation><expect>^[4-5]$</expect></criterion>

`AR402-y-AC1`: the five labelled answers exist; at base the record is absent and it FAILS. `AR402-y-AC2`: at least four of the five lines carry a `file:line` citation; at base it FAILS.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/IRPT_ANLREQ.TO-AR-y-402.original-holdings-blob-delete-path-code-and-policy-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-402`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR402-y-AC1,AR402-y-AC2"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-402</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, the deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/`, this order's file (status line only) and the surprise investigation file are the only places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~295/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-402.original-holdings-blob-delete-path-code-and-policy-read.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of code and Terraform and one record file; nothing is built, uploaded, planned, applied, invoked or called.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call; the policy is read from Terraform source only.
comp-adversary: RUN -- a policy recalled instead of read (each line printed from the file), a zero written without the folders read (invalid), a lifecycle rule inferred from a bucket name, an IAM statement read from a different root than the one that creates the role, a guess written as a finding (NOT READ is the honest answer). NOT seen (blind): the live bucket policy and the applied IAM; denominator: five questions, two criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 10668 item 2 (read which principal the application deletes that prefix with, code and policy only; print whether the third upload lands on the same ART- key). Feeds the third run's step D (the existing path, or a surprise row with an owner). No IAM change. Base: the record is absent, so `AR402-y-AC1` and `AR402-y-AC2` FAIL as expected.
