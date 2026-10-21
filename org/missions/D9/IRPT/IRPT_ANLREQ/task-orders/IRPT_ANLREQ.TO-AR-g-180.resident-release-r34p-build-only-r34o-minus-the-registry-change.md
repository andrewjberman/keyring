# TO-AR-g-180 -- BUILD ONLY: the resident release r34p (r34o without the registry change) as a tarball with its package sums and four host scripts

<to_id>IRPT_ANLREQ.TO-AR-g-180</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~336</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL4</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-180` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** the r34o stage (AR-g-178) and the CTO ruling (msg 11639). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~336`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-336` (branch `wk-IRPT_ANLREQ-336`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~336 <0.9.0_WK_IRPT_ANLREQ~336@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W336-S<k>` (check the channel file for `W336` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_p_checks.py` (read it if it is a file; you cannot edit it). It computes every expected value itself, independent of your work: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-180`, inlined)

**What this cell is.** BUILD ONLY. You build the resident release r34p (the tarball, its package sums and the four host scripts) from a pin with a builder the issuer wrote and rehearsed, and prove it. Nothing is uploaded, installed, applied or run on a host; no AWS call, no network, no push, no deploy. The stage folder is OUTSIDE the repository. You write no product code and you do not edit the tools or the checker.

**Why r34p exists.** r34o (running on the host since 23:12Z) added the ANALYSIS_AUDIT family to the packaged registry file `infra/logic/registry/reporting_policies.json`. That moved the policy hash of the revisions `irpt-anlreq-x10-v1` and `irpt-dashbd-x10-v1`, and the retention check refuses any row whose stored hash differs from the current hash of its revision (run 7e: RetentionRefused). CTO ruling (msg 11639): r34p = r34o minus the registry change; a revision that has rows is never edited.

**Facts (all measured by the issuer, who rehearsed this exact build at this pin in a scratch stage).**
- Pin `919bb891fa72dd706493f094c9b4412503fcf42a` (a full 40-hex commit on this branch's history). The files-from list at the pin is `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt`, 47 lines (r34o's 48 without the registry file).
- The OLD root, the tarball running on the host: `C:/dev/irpt-release-r34o-g3/irpt-resident-0485393f3a-r34o.tar.gz`, sha256 `df070b09230f1e2dd1068291f6fe1f7e2078413dae6ea263b95242e09e25670b`. The r34n tarball (`C:/dev/irpt-release-r35h/irpt-resident-0485393f3a-r34n.tar.gz`, sha256 `89cad47247e6785e6b61e60112b04dfaa3cd2d5de88aef6023959692da76d899`) is also read by the builder: the packaged registry must be byte-equal to r34n's.
- Against r34o the release moves exactly 3 members (SHA256SUMS, infra/logic/registry/reporting_policies.json, reports/resident_bindings.json) and adds none: 323 members. The issuer's rehearsal tarball sha256 is `4991c7bcba0f01cb47b06bfa8c4e30f3fe47a6cbd6e9b9f479d1d39b77b49ea4` (builds are held to a fixed clock, so yours should equal it).
- The tools: `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34p_build.py` (the builder), `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/make_scripts_r34p.py` (its host-script generator). Read the builder's docstring first.

**What to do.**
1. Confirm, and STOP with a BLOCKING row quoting the line if any is false: (a) `sha256sum` of the r34o and r34n tarballs prints the two values above; (b) `git cat-file -t 919bb891fa72dd706493f094c9b4412503fcf42a` prints `commit` and `git show 919bb891fa72dd706493f094c9b4412503fcf42a:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt` has 47 lines; (c) the folder `C:/dev/irpt-release-r34p-g2` does not exist; (d) both tool files above exist on disk. Never touch, create inside or delete any other folder named `irpt-release-*` or `irpt-trial-*`.
2. Run from your worktree root: `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34p_build.py --pin 919bb891fa72dd706493f094c9b4412503fcf42a --out C:/dev/irpt-release-r34p-g2 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~336/r63/RESIDENT_R34P_BUILD.json`. It takes several minutes (up to 600 s): if the tool-call limit hits, run it in the background and wait for it to end. Its last line begins `R34P-BUILD-OK` or `R34P-BUILD-BAD <why>`. On BAD: file a BLOCKING row quoting the line, report, and stop (do not edit the tools).
3. Print: the tarball sha256, size and member count; the two-build identity line; the delta (changed, added, removed); the import smoke line; the gate dry-run return codes; the sha256 of each host script. State whether the tarball sha256 equals the rehearsal's above (a difference is not a failure of this cell: file an OBSERVATION row with both values).
4. Run the three criteria below. Write the proof instance (shape of the AR-g-178 instance in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~334/`, read it first with `git show HEAD:<path>` if absent; its `decomp_ref` takes only doc, vintage_commit and to_ref): `controls.mutant` = a copy of your record with `reports/resident_bindings.json` removed from `delta_vs_r34o.changed`, which `ar_release_p_checks.py record` must refuse (run it, record the FAIL line); `controls.determinism` = `two_builds.files_compared` equals `two_builds.identical` in your record. Validate with `python .tools/proof-of-spec-check.py <instance> AR180-g-AC1,AR180-g-AC2,AR180-g-AC3`, commit the record and the proof, then flip the order's `<status>` to `complete` (commit alone) only on VALID and three PASS.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR180-g-AC1" cell_refs="AR-g-180"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_p_checks.py record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~336/r63/RESIDENT_R34P_BUILD.json</invocation><expect>^AR-RELP-record-OK$</expect></criterion>

<criterion id="AR180-g-AC2" cell_refs="AR-g-180"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_p_checks.py tree C:/dev/irpt-release-r34p-g2/irpt-resident-0485393f3a-r34p.tar.gz 919bb891fa72dd706493f094c9b4412503fcf42a</invocation><expect>^AR-RELP-tree-OK$</expect></criterion>

<criterion id="AR180-g-AC3" cell_refs="AR-g-180"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_p_checks.py scripts C:/dev/irpt-release-r34p-g2</invocation><expect>^AR-RELP-scripts-OK$</expect></criterion>

<expected_criteria>AR180-g-AC1,AR180-g-AC2,AR180-g-AC3</expected_criteria>

- AC1: the build record's delta against the running r34o tarball is exactly SHA256SUMS, the registry file and the bindings, nothing added or removed, the artifact on disk has the recorded sha256, size and 323 members, the bindings moved only in provenance, the two builds are identical, the smoke reads 86 of 86 and the gate dry runs read 0, 31, 0, 33. At base it FAILs (no record).
- AC2: the tarball read by the checker's own code: every other member equals r34o's, the registry file is byte-equal to r34n's, every reporting policy revision has the same policy_sha256 as in r34n, the lazy imports import, the bindings carry the pin and 47 files-from lines. At base it FAILs (no tarball).
- AC3: the four host scripts exist, are ASCII, pass bash -n, name NEW r34p and OLD r34o, bind the tarball, the host script and the package sums by sha256, and carry one member check per mover (three) and one member entry. At base it FAILs (no scripts).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~336/r63/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~336/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-180.resident-release-r34p-build-only-r34o-minus-the-registry-change.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-180`.
<owned_cells>AR-g-180</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR180-g-AC1,AR180-g-AC2,AR180-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~336/IRPT_ANLREQ.TO-AR-g-180.resident-release-r34p-build-only-r34o-minus-the-registry-change.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-180`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR180-g-AC1,AR180-g-AC2,AR180-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a build in a stage folder outside the repository and one record plus a proof in the worker folder; nothing is uploaded, installed, applied or run on a host. The release itself restores one registry file to its r34n bytes and moves the bindings provenance only when a later CloudOps apply installs it under a COO+CTO never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base (no record, no tarball, no scripts); the checker was calibrated by the issuer on a rehearsal build at this pin (record OK, tree OK, scripts OK) and refuses the r34o tarball offered as r34p (delta empty, registry not r34n's, bindings unmoved, policy hashes of irpt-anlreq-x10-v1 and irpt-dashbd-x10-v1 differ). Traps: a stage folder inside the repository, any other irpt-release folder touched, a different pin, the registry file not byte-equal to r34n's. NOT seen (blind): the live host and the live retention rows (the census is a separate read).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 all FAIL (nothing built).
