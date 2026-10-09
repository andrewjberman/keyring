# TO-AR-y-21 -- the release-1 packet: staged rows carry AR-y-11 and the contract that admits it

<to_id>IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~2</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~Y | **Decomp cell:** `AR-y-21` (`decompositions/IRPT_ANLREQ_DECOMP_R2.md`)

---

## WORKER FACE

### THE CELL

`AR-y-11` (drained @3ad7526e06) taught the analysis submission to carry `ticket_id` and taught the published request contract to admit it.
Two served functions still package the OLD bytes of those files through `infra/aws/lambda/ci/lambda-source-map.json` `staged_from` rows. **Re-pin
exactly three rows to a pin whose blob equals HEAD's**:

| function | `repo_path` | today's pin |
|---|---|---|
| `irpt-status` | `infra/aws/lambda/investor-reporting/ycharts/generate/submission.py` | `80a79a7462` |
| `irpt-status` | `infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py` | `80a79a7462` |
| `irpt-ycharts-generate` | `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json` | `3f29017cfc` |

- Each new `pin` is the full 40-char sha of a commit whose blob of that path equals HEAD's: the last commit touching it.
  `git log -1 --format=%H -- <path>` gives it.
- Each `sha256` is the hex sha256 of that blob, in the existing format.
- Change nothing else in those rows, and no other row. Edit the JSON byte-preserving: keep its indentation and line endings, and replace
  only the two values per row.
- If AC2 or AC3 then fails because a commit now ships split or a name is missing, STOP and file a row. Do not re-pin further rows to
  chase it.
- Report `python infra/aws/lambda/ci/release-census.py irpt-status --pin HEAD` and the same for `irpt-ycharts-generate`, with every changed
  member listed. This is informational; the release pair grades it.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR21-y-AC1" cell_refs="AR-y-21"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/ar21_cells.py . AR21-y-AC1</invocation><expect>AR21-y-AC1 PASS</expect></criterion>

<criterion id="AR21-y-AC2" cell_refs="AR-y-21"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/ar21_cells.py . AR21-y-AC2</invocation><expect>AR21-y-AC2 PASS</expect></criterion>

<criterion id="AR21-y-AC3" cell_refs="AR-y-21"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r2/ar21_cells.py . AR21-y-AC3</invocation><expect>AR21-y-AC3 PASS</expect></criterion>

<expected_criteria>AR21-y-AC1,AR21-y-AC2,AR21-y-AC3</expected_criteria>

**Issuer's base run at box/dell2 HEAD:**
- AC1: FAIL, 3 of 3 rows lag;
- AC2: PASS, split=0 for both functions;
- AC3: PASS, irpt-status missing=0 of 111 and irpt-ycharts-generate missing=0 of 299.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no upload (BUILD_ONLY only, inside AC3), no terraform, no AWS calls.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W2-S<k>`, in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, one `## <id> -- <title>`
  header plus a ```json block per row (the file's existing format). Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Before the issuer drains,** run `bash .tools/safe-merge.sh box/dell2` INSIDE your worktree and resolve any channel conflict there
  (box/dell2's file plus your own row blocks appended whole).
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~2" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~2@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~2 <0.9.0_WK_IRPT_ANLREQ~2@opal.agent>" -F <msgfile> -- <paths>`.
  Write the message file with the Write tool (a Windows path); no pre-`git add`; ASCII only; use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~2/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R2.md</decomp_doc> round 2, workstream ~Y, cell `AR-y-21`.
<owned_cells>AR-y-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR21-y-AC1, AR21-y-AC2, AR21-y-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~2/IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows.proof_of_spec.json`. Its `to_id` is the FULL id
`IRPT_ANLREQ.TO-AR-y-21.release1-staged-rows`. Validate with `python .tools/proof-of-spec-check.py <instance> AR21-y-AC1,AR21-y-AC2,AR21-y-AC3` BEFORE the
flip to complete. Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~1/IRPT_ANLREQ.TO-AR-y-11.analysis-carries-ticket-id.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the three new pins and sha256 values;
- both census outputs;
- the commit hashes and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- three staged rows in two functions (irpt-status: 2; irpt-ycharts-generate: 1); the blobs carry AR-y-11 (ticket_id admitted, persisted, contract) and nothing else of theirs moves; nothing deploys in this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added or changed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or authorizer change.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched.
comp-adversary: RUN -- AC1 at base FAILs (3 of 3 lag); AC2 and AC3 PASS at base and refuse a split commit or a missing name the re-pin introduces.
lane: the <paths> block IS the grant (worker_grant).
</preflight>
