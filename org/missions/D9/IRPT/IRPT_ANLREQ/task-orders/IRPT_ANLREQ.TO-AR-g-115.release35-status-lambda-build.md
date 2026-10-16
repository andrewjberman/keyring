# TO-AR-g-115 -- BUILD the release-35 irpt-status Lambda package (the failure code and words) at the tooling pin (BUILD ONLY: nothing is uploaded, planned, applied or invoked; no AWS call)

<to_id>IRPT_ANLREQ.TO-AR-g-115</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~255</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-115` (`decompositions/IRPT_ANLREQ_DECOMP_R32_G.md`) |
**outcome_ref:** FWD-4 (C-HOP-FAILURE) | **depends_on:** `AR-g-111` (merged `766ec706ee`), `AR-g-113` (merged `28734e0985`); the tooling commit `90b69dcb12` (the pin). Order: CTO msgs 8907, 8971.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~255`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-255` (branch `wk-IRPT_ANLREQ-255`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~255 <0.9.0_WK_IRPT_ANLREQ~255@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W255-S<k>` (take the next free `<k>`; check the channel file for `W255` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **BUILD ONLY.** No upload, no plan, no apply, no invoke, no AWS call of any kind, no network, no push, no change to anything under `infra/`. The stage folder is OUTSIDE the repository. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-g-115`, inlined)

The issuer has written the release-35 Lambda-leg build tool and committed it at the pin (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r35/r35l_build.py`). It makes a sparse throwaway worktree detached at the pin, builds the `irpt-status` package TWICE with the repository's own builder (`infra/aws/lambda/ci/build-and-upload.sh`, `BUILD_ONLY=1`, a private TMPDIR, nothing uploaded), refuses unless the two builds are byte-identical, compares the zip's members with the issuer's offline census build at the pin and at the release-33 build pin `927337a741`, removes its throwaway worktree, and writes a record. You run it, you do not edit it. The issuer's verifier then recomputes everything without trusting the driver, and requires the CodeSha256 to equal that of the issuer's own earlier build of the same pin.

1. **Create the record's folder first** (the driver does not): `mkdir -p org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~255/r35l`. Print `git rev-parse 90b69dcb12`: it must equal the 40-hex below; if it does not, STOP and file a row. The stage folder `C:/dev/irpt-release-r35l` must not exist.
2. **Run the driver** from the worktree root (about two minutes; give the command `timeout` 590000 ms; if it is killed or fails for a reason that is not an `R35L-BUILD-BAD` line, run it ONCE more with a new, absent `--out` folder name such as `C:/dev/irpt-release-r35lb`, because the tool refuses a non-empty folder, and use that folder in the criterion):
   `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r35/r35l_build.py --pin 90b69dcb12cdfedc786966ab33d034bf14229396 --out C:/dev/irpt-release-r35l --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~255/r35l/R35L_BUILD.json`
   The last line it prints must begin `R35L-BUILD-OK`. If it prints `R35L-BUILD-BAD <why>`, file ONE row with that line and the driver's last 20 lines, change nothing, and report: do not edit a tool, do not retry with other arguments.
3. **Run the two criteria below.** Commit the record, then the proof and the status flip, as separate commits (record first). Leave the stage folder exactly as the driver made it.
4. **Report** the line the driver printed, the zip's sha256, CodeSha256 and size, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR115-g-AC1" cell_refs="AR-g-115"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g115_checks.py verify C:/dev/irpt-release-r35l org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~255/r35l/R35L_BUILD.json +TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A=</invocation><expect>^AR-G115-OK</expect></criterion>

<criterion id="AR115-g-AC2" cell_refs="AR-g-115"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g115_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~255 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-115.release35-status-lambda-build.md</invocation><expect>^AR-G115-SCOPE-OK</expect></criterion>

<expected_criteria>AR115-g-AC1,AR115-g-AC2</expected_criteria>

- AC1 recomputes, from the zip and the git objects: the zip's sha256 and CodeSha256 (base64 of the sha256); its members against the issuer's offline census build at the pin; the delta against the release-33 build (exactly 3 members: `durable_job.py`, `owned_status.py`, `status.py`); no live read claimed; and that your CodeSha256 equals the one given in the invocation (a second build of the same pin is identical). At base (no record) it FAILs.
- AC2 checks that your branch changes nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. BUILD ONLY, as above.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~255/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-115.release35-status-lambda-build.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R32_G.md</decomp_doc> round 32, workstream ~G, cell `AR-g-115`.
<owned_cells>AR-g-115</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR115-g-AC1, AR115-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~255/IRPT_ANLREQ.TO-AR-g-115.release35-status-lambda-build.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-115`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR115-g-AC1,AR115-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- BUILD ONLY: local files outside the repository (a sparse throwaway worktree that the tool creates and removes, two private TMPDIR folders, one zip) and one record under the worker's folder; nothing is uploaded, planned, applied, invoked or run on any host, and no AWS call is made (the builder's BUILD_ONLY mode reads git and the tree only). The package is applied later by a CloudOps applier under a signed never-widen pair that names the blast radius.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's trial build of this pin (CodeSha256 +TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A=, 49 members, delta 3, verifier AR-G115-OK). Traps: a zip that differs between two builds (a clock in the archive); a package that carries another seat's merged work (the delta is graded to exactly 3 members); a baseline that is not the live build (the live package is the r33 build at 927337a741, named in the tool, not the map's last_deployed_commit, which is a later test-only commit); a stage folder inside the repository; a build that uploads (the guard: BUILD_ONLY at the pin is counted before the build); a record folder that does not exist (the tool does not create it: step 1). The verifier recomputes everything independently of the driver.
</preflight>

- Cut on CTO msgs 8907 and 8971 and the issuer's trial build at the same pin. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: `AR115-g-AC1` FAILs (no record) and `AR115-g-AC2` PASSes.
- The member diff against the LIVE package is the applier's census (`infra/aws/lambda/ci/release-census.py irpt-status --pin <pin>`), which the pair requires.
