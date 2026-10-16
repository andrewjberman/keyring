# TO-AR-g-103 -- BUILD the release-33 Lambda packages (irpt-ycharts-generate and irpt-status) at the pin of the release-33 source merge (BUILD ONLY: nothing is uploaded, planned, applied or invoked; no AWS call)

<to_id>IRPT_ANLREQ.TO-AR-g-103</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~204</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-103` (`decompositions/IRPT_ANLREQ_DECOMP_R26_G.md`) |
**outcome_ref:** FWD-1 run 3 | **depends_on:** `AR-g-102` (merged `927337a741`, the pin). Order: CTO msg 8658.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~204`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-204` (branch `wk-IRPT_ANLREQ-204`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~204 <0.9.0_WK_IRPT_ANLREQ~204@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W204-S<k>` (take the next free `<k>`; check the channel file for `W204` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **BUILD ONLY.** No upload, no plan, no apply, no invoke, no AWS call of any kind, no network, no push, no change to anything under `infra/`. The stage folder is OUTSIDE the repository. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-g-103`, inlined)

The issuer has written the release-33 build tool and committed it (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r33/r33_build.py`). It makes a sparse throwaway worktree detached at the pin, builds each of the two packages TWICE with the repository's own builder (`infra/aws/lambda/ci/build-and-upload.sh`, `BUILD_ONLY=1`, a private TMPDIR, nothing uploaded), refuses unless the two builds of each are byte-identical, compares each zip's members with the issuer's offline census build at the pin and at each function's baseline commit, removes its throwaway worktree, and writes a record. You run it, you do not edit it. The issuer's verifier then recomputes everything without trusting the driver, and requires the two CodeSha256 values to equal those of the issuer's own earlier build of the same pin.

1. **Run the driver** from the worktree root (it takes about 5.5 minutes: give the command `timeout` 590000 ms; if it is killed or fails for a reason that is not a `R33-BUILD-BAD` line, run it ONCE more with a new, absent `--out` folder name such as `C:/dev/irpt-release-r33b`, because the tool refuses a non-empty folder):
   `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r33/r33_build.py --pin 927337a741f40a83e7daa9e09154436a813b05dd --out C:/dev/irpt-release-r33 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~204/r33/R33_BUILD.json`
   (Before you run it, print `git rev-parse 927337a741`: it must equal the 40-hex above. If it does not, STOP and file a row.) The last line it prints must begin `R33-BUILD-OK`. If it prints `R33-BUILD-BAD <why>`, file ONE row with that line and the driver's last 20 lines, change nothing, and report: do not edit a tool, do not retry with other arguments.
2. **Run the two criteria below.** Commit the record, then the proof and the status flip, as separate commits (record first). Leave the stage folder exactly as the driver made it.
3. **Report** the line the driver printed, each zip's sha256, CodeSha256 and size, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR103-g-AC1" cell_refs="AR-g-103"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g103_checks.py verify C:/dev/irpt-release-r33 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~204/r33/R33_BUILD.json kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE= OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss=</invocation><expect>^AR-G103-OK</expect></criterion>

<criterion id="AR103-g-AC2" cell_refs="AR-g-103"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g103_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~204 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-103.release33-lambda-build.md</invocation><expect>^AR-G103-SCOPE-OK</expect></criterion>

<expected_criteria>AR103-g-AC1,AR103-g-AC2</expected_criteria>

- AC1 recomputes, from the two zips and the git objects: each zip's sha256 and CodeSha256 (base64 of the sha256); its members against the issuer's offline census build at the pin; the delta against each function's baseline build (exactly 8 members of `irpt-ycharts-generate`: `acceptance.py`, `generate_installed.py`, `normalized_input.py`, `portfolio.py`, `prospect_submission.py`, `submission_service.py`, `ticket_confirmation.py`, `uploads.py`; exactly `status.py` of `irpt-status`); no live read claimed; and that your two CodeSha256 values equal the two given in the invocation (a second build of the same pin is identical). At base (no record) it FAILs.
- AC2 checks that your branch changes nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. BUILD ONLY, as above.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~204/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-103.release33-lambda-build.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R26_G.md</decomp_doc> round 26, workstream ~G, cell `AR-g-103`.
<owned_cells>AR-g-103</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR103-g-AC1, AR103-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~204/IRPT_ANLREQ.TO-AR-g-103.release33-lambda-build.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-103`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR103-g-AC1,AR103-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- BUILD ONLY: local files outside the repository (a sparse throwaway worktree that the tool creates and removes, four private TMPDIR folders, two zips) and one record under the worker's folder; nothing is uploaded, planned, applied, invoked or run on any host, and no AWS call is made (the builder's BUILD_ONLY mode reads git and the tree only). The packages are applied later by a CloudOps applier under a signed never-widen pair that names the blast radius.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by two trial builds of this pin by the issuer (a full checkout and a sparse one: the same two CodeSha256 values) and the verifier run on them with six negative controls (a tampered zip, a record claiming a live read, a wrong member table, a wrong pin, builds_identical false, a delta field with a member removed: each FAILs). Traps: a zip that differs between two builds (a clock in the archive); a package that carries another seat's merged work (the delta is graded to exactly 8 and 1 members); a baseline that is not the live build (irpt-status's map entry names the last commit touching the source dir, not its build commit: the tool uses the release-31 map commit af51e37a29 and the verifier names it); a stage folder inside the repository; a build that uploads (the guard: BUILD_ONLY at the pin is counted before the build). The verifier recomputes everything independently of the driver.
</preflight>

- Cut on CTO msg 8658 and the issuer's trial builds at the same pin (full: 3m25s to build the worktree plus four builds; sparse: 5m23s in all; both give `kxOEgpbspky10PYWQ28y0+7V2UXG28whJ2riMa4CkTE=` for `irpt-ycharts-generate` and `OOez8YSmE22btOqx28/fJdK9sxGNDGAumU5pMJ++6Ss=` for `irpt-status`). Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: `AR103-g-AC1` FAILs (no record) and `AR103-g-AC2` PASSes.
- The member diff against the LIVE package is the applier's census (`release-census.py <function> --pin <pin>`), which the pair requires.
