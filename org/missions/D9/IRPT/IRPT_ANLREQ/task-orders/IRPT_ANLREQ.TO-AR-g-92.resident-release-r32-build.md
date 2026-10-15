# TO-AR-g-92 -- BUILD the release-32 resident tarball and its four host scripts at the pin of the last merged ENGINE cell (BUILD ONLY: nothing is uploaded, installed, applied or run on a host)

<to_id>IRPT_ANLREQ.TO-AR-g-92</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~197</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-92` (`decompositions/IRPT_ANLREQ_DECOMP_R21_G.md`) |
**outcome_ref:** FWD-1 run 3 | **depends_on:** every ENGINE source cell, merged; the last is `AR-g-95` at `26d720a980`.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~197`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-197` (branch `wk-IRPT_ANLREQ-197`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~197 <0.9.0_WK_IRPT_ANLREQ~197@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W197-S<k>` (take the next free `<k>`; check the channel file for `W197` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **BUILD ONLY.** No upload, no install, no apply, no invoke, no AWS call of any kind, no network, no push, no change to anything under `infra/`. The stage folder is OUTSIDE the repository. Scratch outside the product tree. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-g-92`, inlined)

The issuer has written the tools of the release-32 build and committed them (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/`): the builder (derived from the production one, with three added flags), the packer, the clock wrapper, the files-from list, the script generator and the driver `r32_build.py`. The driver builds twice under one fixed clock and compares, packs once, diffs against the release-31 tarball, derives the four host scripts from the release-31 set, runs `bash -n` on each, dry-runs the two sha256 gates and writes the record. It refuses unless every tool on disk equals the same tool at the pin. You run it, you do not edit it. The issuer's verifier then recomputes everything without trusting the driver.

1. **Run the driver** from the worktree root (it takes a few minutes; give it `timeout 900`; it needs `C:/dev/irpt-release-r31/` on this box, which holds the release-31 tarball):
   `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r32/r32_build.py --pin 26d720a980ba7792e87141e2bd97a5781f8bb190 --out C:/dev/irpt-release-r32 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~197/r32/RESIDENT_R32_BUILD.json`
   (Before you run it, print `git rev-parse 26d720a980`: it must equal the 40-hex above. If it does not, STOP and file a row.) The last line it prints must begin `R32-BUILD-OK`. If it prints `R32-BUILD-BAD <why>`, file ONE row with that line and the driver's last 20 lines, change nothing, and report: do not edit a tool, do not retry with other arguments.
2. **Run the two criteria below.** Commit the record, then the proof and the status flip, as separate commits (record first). Leave the stage folder `C:/dev/irpt-release-r32` exactly as the driver made it.
3. **Report** the line the driver printed, the tarball's sha256 and size, the four script names with their sha256, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR92-g-AC1" cell_refs="AR-g-92"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g92_checks.py verify C:/dev/irpt-release-r32 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~197/r32/RESIDENT_R32_BUILD.json</invocation><expect>^AR-G92-OK</expect></criterion>

<criterion id="AR92-g-AC2" cell_refs="AR-g-92"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g92_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~197 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-92.resident-release-r32-build.md</invocation><expect>^AR-G92-SCOPE-OK</expect></criterion>

<expected_criteria>AR92-g-AC1,AR92-g-AC2</expected_criteria>

- AC1 recomputes, from the tarball, the release-31 tarball and the git objects at the pin: the artifact hash; the delta (exactly 15 members changed and 11 added, none removed, 284 identical); every changed or added member against `git show <pin>:<path>`; the bindings (the three added keys, the pins verified by the installer's own loader, pricing off); the producer list (exactly andrew and `fwd1-staff-r41b@opal.invalid`); the two builds identical; no credential-shaped text; each host script (ASCII, `bash -n`, the pins, the fail-closed guards, one member check per changed or added member); and the two sha256 gates. At base (no record) it FAILs. It takes about a minute.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changes nothing under `infra/` and nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. BUILD ONLY, as above.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~197/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-92.resident-release-r32-build.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21_G.md</decomp_doc> round 21, workstream ~G, cell `AR-g-92`.
<owned_cells>AR-g-92</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR92-g-AC1, AR92-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~197/IRPT_ANLREQ.TO-AR-g-92.resident-release-r32-build.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-92`.
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR92-g-AC1,AR92-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- BUILD ONLY: local files outside the repository and one record under the worker's folder; nothing is uploaded, installed, applied, invoked or run on a host. The release is applied later by a CloudOps applier under a signed never-widen pair that names the blast radius (producer list, per-variant map selection, commentary revision, pricing shipped off).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by a trial build at an earlier pin and the verifier run on it (it passed). Traps: a tool on disk that is not the tool at the pin; a member in the tarball that no merged cell changed (a foreign change since the r31 pin: the export bundle schema, filled-named-accounts and lib/opal_naming.py of other lanes are NOT in the files-from list, and the delta must still be exactly 15 and 11); two builds that differ; a script that pins the wrong tarball or does not refuse a wrong running root; a gate that passes a one-byte change; a credential-shaped string in a changed member or script; anything written under infra/ or outside the stage folder. The verifier recomputes all of it independently of the driver.
</preflight>

- Cut on the issuer's trial build at `cbf05a6afa` (310 members, 14 changed, 11 added, verifier OK; AR-g-95 later made intake/uploads.py the 15th changed member (amendment 1, after worker 197 row W197-S1)) and the CTO's rulings (msgs 8568, 8630, 8647, 8658). Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: `AR92-g-AC1` FAILs (no record) and `AR92-g-AC2` PASSes.
- Fixed pin: `26d720a980` is `AR-g-95`'s merge. Every file the files-from list takes was last changed by an ANLREQ worker (checked by `git log c4c2afe896..26d720a980` per file, 20 authors, all of this project).
