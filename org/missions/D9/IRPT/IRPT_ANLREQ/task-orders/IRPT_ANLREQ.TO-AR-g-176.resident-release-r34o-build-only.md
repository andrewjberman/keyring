# TO-AR-g-176 -- BUILD ONLY: the resident release r34o (FWD-10 Core, the audit wiring, the Overview price pages) as a tarball with its package sums and four host scripts

<to_id>IRPT_ANLREQ.TO-AR-g-176</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~332</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-176` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-y-469 of 2.0.0_SA_COO~Y2 (the audit wiring) and this issuer's AR-g-171 to 175 (FWD-10), all merged on the pin's history. Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~332`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-332` (branch `wk-IRPT_ANLREQ-332`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~332 <0.9.0_WK_IRPT_ANLREQ~332@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W332-S<k>` (check the channel file for `W332` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_checks.py` (read it if it is a file; you cannot edit it). It computes every expected value itself, independent of your work: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-176`, inlined)

**What this cell is.** BUILD ONLY. You build the resident release r34o (the tarball, its package sums and the four host scripts) from a pin with a builder the issuer wrote and rehearsed, and prove it. Nothing is uploaded, installed, applied or run on a host; no AWS call, no network, no push, no deploy. The stage folder is OUTSIDE the repository. You write no product code and you do not edit the tools or the checker.

**Facts (all measured by the issuer, who rehearsed this exact build at this pin in a scratch stage).**
- Pin `3f1961ceab12c934b2510e2047589351ba3539e6` (a full 40-hex commit on this branch's history). The files-from list at the pin is `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt`, 47 lines.
- The OLD root, the tarball running on the host: `C:/dev/irpt-release-r35h/irpt-resident-0485393f3a-r34n.tar.gz`, sha256 `89cad47247e6785e6b61e60112b04dfaa3cd2d5de88aef6023959692da76d899`.
- The release moves 11 members (SHA256SUMS, lib/trading_calendar.py, ops/owned_report.py, reports/resident_bindings.json, reports/resident_installed.py, ycharts/generate/resident_worker.py, ycharts/generate/ticket_confirmation.py, ycharts/research/layout_overview.py, ycharts/research/opal_packager.py, ycharts/research/opal_producer.py, ycharts/research/overview_map.json) and adds 6 (_contracts/AnalysisAudit.v1.schema.json, reports/analysis_audit.py, ycharts/generate/ticket_audit_source.py, ycharts/research/comparables.py, ycharts/research/model_code_map.json, ycharts/research/model_source.py): 323 members. The issuer's rehearsal tarball sha256 is `c1e3ab21de0511e951c0e727f3d358c1ecfb94fc5f0078963ced2f97cb359b2a` (builds are held to a fixed clock, so yours should equal it).
- The tools: `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34o_build.py` (the builder), `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/make_scripts_r34o.py` (its host-script generator), and the builder's own inputs in the same folder. Read the builder's docstring first.

**What to do.**
1. Confirm, and STOP with a BLOCKING row quoting the line if any is false: (a) `sha256sum C:/dev/irpt-release-r35h/irpt-resident-0485393f3a-r34n.tar.gz` prints the sha256 above; (b) `git cat-file -t 3f1961ceab12c934b2510e2047589351ba3539e6` prints `commit` and `git show 3f1961ceab12c934b2510e2047589351ba3539e6:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt` has 47 lines; (c) the folder `C:/dev/irpt-release-r34o-g2` does not exist; (d) both tool files above exist on disk. Never touch, create inside or delete any other folder named `irpt-release-*` or `irpt-trial-*`.
2. Run from your worktree root: `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34o_build.py --pin 3f1961ceab12c934b2510e2047589351ba3539e6 --out C:/dev/irpt-release-r34o-g2 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~332/r61/RESIDENT_R34O_BUILD.json`. It takes several minutes (up to 600 s): if the tool-call limit hits, run it in the background and wait for it to end. Its last line begins `R34O-BUILD-OK` or `R34O-BUILD-BAD <why>`. On BAD: file a BLOCKING row quoting the line, report, and stop (do not edit the tools).
3. Print: the tarball sha256, size and member count; the two-build identity line; the delta (changed, added, removed); the import smoke line; the gate dry-run return codes; the sha256 of each host script. State whether the tarball sha256 equals the rehearsal's above (a difference is not a failure of this cell: file an OBSERVATION row with both values).
4. Run the three criteria below. Write the proof instance (shape of the AR-y-450 instance in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/`, read it first; `git show HEAD:<path>` if absent): `controls.mutant` = a copy of your record with one name removed from `delta_vs_r34n.changed`, which `ar_release_checks.py record` must refuse (run it, record the FAIL line); `controls.determinism` = `two_builds.files_compared` equals `two_builds.identical` in your record. Validate with `python .tools/proof-of-spec-check.py <instance> AR176-g-AC1,AR176-g-AC2,AR176-g-AC3`, commit the record and the proof, then flip the order's `<status>` to `complete` (commit alone) only on VALID and three PASS.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR176-g-AC1" cell_refs="AR-g-176"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_checks.py record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~332/r61/RESIDENT_R34O_BUILD.json</invocation><expect>^AR-REL-record-OK$</expect></criterion>

<criterion id="AR176-g-AC2" cell_refs="AR-g-176"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_checks.py tree C:/dev/irpt-release-r34o-g2/irpt-resident-0485393f3a-r34o.tar.gz 3f1961ceab12c934b2510e2047589351ba3539e6</invocation><expect>^AR-REL-tree-OK$</expect></criterion>

<criterion id="AR176-g-AC3" cell_refs="AR-g-176"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_checks.py scripts C:/dev/irpt-release-r34o-g2</invocation><expect>^AR-REL-scripts-OK$</expect></criterion>

<expected_criteria>AR176-g-AC1,AR176-g-AC2,AR176-g-AC3</expected_criteria>

- AC1: the build record's delta against the running r34n tarball is exactly the 11 movers and 6 additions, the artifact on disk has the recorded sha256, size and 323 members, the bindings moved only in the Overview map pin and the provenance, the two builds are identical, the import smoke reads 86 of 86 and the gate dry runs read 0, 31, 0, 33. At base it FAILs (no record).
- AC2: the tarball read by the checker's own code: every member shared with r34n equals r34n except the movers, each mover and addition equals `git show` of the pinned source, the lazy imports the smoke cannot see import in a fresh interpreter, and the bindings carry the pin. At base it FAILs (no tarball).
- AC3: the four host scripts exist, are ASCII, pass bash -n, name NEW r34o and OLD r34n, bind the tarball, the host script and the package sums by sha256, and carry one member check per mover or addition. At base it FAILs (no scripts).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~332/r61/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~332/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-176.resident-release-r34o-build-only.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-176`.
<owned_cells>AR-g-176</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR176-g-AC1,AR176-g-AC2,AR176-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~332/IRPT_ANLREQ.TO-AR-g-176.resident-release-r34o-build-only.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-176`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR176-g-AC1,AR176-g-AC2,AR176-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a build in a stage folder outside the repository and one record plus a proof in the worker folder; nothing is uploaded, installed, applied or run on a host. The release itself moves 11 resident package members and adds 6 only when a later CloudOps apply installs it under a COO+CTO never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base (no record, no tarball, no scripts); the checker was calibrated by the issuer on a rehearsal build at this pin (record OK, tree OK, scripts OK) and refuses a mutant (a one-byte host script; a record missing a mover; the r34n tarball itself; a wrong pin). Traps: a stage folder inside the repository, any other irpt-release folder touched, a different pin than the one named, the lazy imports the smoke cannot see. NOT seen (blind): the live host and the live objects.
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 all FAIL (nothing built).
