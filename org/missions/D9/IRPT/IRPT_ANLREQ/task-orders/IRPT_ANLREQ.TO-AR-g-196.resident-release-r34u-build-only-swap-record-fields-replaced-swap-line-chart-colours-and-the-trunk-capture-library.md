# TO-AR-g-196 -- BUILD ONLY: the resident release r34u (r34t plus the swap record fields, the replaced-swap line, six chart colours and the trunk capture library) as a tarball with its package sums and four host scripts

<to_id>IRPT_ANLREQ.TO-AR-g-196</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~386</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-21</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL17</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-196` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-y-497, AR-y-498, AR-g-195 (merged). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~386`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-386` (branch `wk-IRPT_ANLREQ-386`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~386 <0.9.0_WK_IRPT_ANLREQ~386@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W386-S<k>` (check the channel file for `W386` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_u_checks.py` (read it if it is a file; you cannot edit it). It computes every expected value itself, independent of your work: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-196`, inlined)

**What this cell is.** BUILD ONLY. You build the resident release r34u (the tarball, its package sums and the four host scripts) from a pin with a builder the issuer wrote and rehearsed, and prove it. Nothing is uploaded, installed, applied or run on a host; no AWS call, no network, no push, no deploy. The stage folder is OUTSIDE the repository. You write no product code and you do not edit the tools or the checker.

**Why r34u exists.** r34u packages: the swap record carries the class pair and the model's number, and a low-confidence swap's text ends with a review sentence (AR-y-497, `ycharts/research/swap_pass.py`); the Overview names every replaced swap under the left-out line (AR-y-498) and the comparison chart draws six distinct series colours (AR-g-195), both in `ycharts/research/layout_overview.py`; and THE HOST CAPTURE LIBRARY MOVES: `ycharts-host/ycharts_session.js` is taken from the trunk file `infra/aws/ec2/investor-reporting-ycharts/ycharts_session.js` (the W328-S1 WAF repair: WAF_CHALLENGE ends the run with no second sign-in; sha256 `db43e9f9744e697098120e11dd862a1348ffea05c6307f980dc24e7ea530a216`) instead of the base pin's file (`a1c2880169c5f7996cc7c5880e4fe36db90f0a2c1f5a1cd01e0d1d8153544841`), through the builder's new `--library-at-pin` flag, and the bindings' `capture.library_sha256` follows. No member is added; the registry, IAM and files-from list do not move.

**Facts (all measured by the issuer, who rehearsed this build at an earlier pin in a scratch stage).**
- Pin `d002cae9d9de62d774a7bb9333f22139309ac77c` (a full 40-hex commit on this branch's history). The files-from list at the pin is `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt`, 51 lines.
- The OLD root, the tarball running on the host: `C:/dev/irpt-release-r34t-g2/irpt-resident-0485393f3a-r34t.tar.gz`, sha256 `35a4f044c2bcae4d567c57132b833c101ab1872d9880bafd45cb0a4afe6af21d`. The r34n tarball (`C:/dev/irpt-release-r35h/irpt-resident-0485393f3a-r34n.tar.gz`, sha256 `89cad47247e6785e6b61e60112b04dfaa3cd2d5de88aef6023959692da76d899`) is also read by the builder.
- Against r34t the release moves exactly 5 members (SHA256SUMS, reports/resident_bindings.json (capture.library_sha256 and provenance.package_pin), ycharts-host/ycharts_session.js, ycharts/research/layout_overview.py, ycharts/research/swap_pass.py) and adds none: 325 members. The issuer's rehearsal tarball (at the earlier pin 1a7cfac868) has sha256 `9c5a32955524cf67dc584fa4a4d9aa3beda271879b6a7ed31b94c7d4ebb66c83`; yours differs only in the bindings' package pin and the sums (the pin is different).
- The tools: `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34u_build.py` (the builder), `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/make_scripts_r34u.py` (its host-script generator, which also restores the kept old library in the rollback), `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/build_resident_package.py` (the release builder it runs, with the new flag). Read the builder's docstring first.

**What to do.**
1. Confirm, and STOP with a BLOCKING row quoting the line if any is false: (a) `sha256sum` of the r34t and r34n tarballs prints the two values above; (b) `git cat-file -t d002cae9d9de62d774a7bb9333f22139309ac77c` prints `commit` and `git show d002cae9d9de62d774a7bb9333f22139309ac77c:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt` has 51 lines; (c) the folder `C:/dev/irpt-release-r34u-g2` does not exist; (d) the tool files above exist on disk. Never touch, create inside or delete any other folder named `irpt-release-*` or `irpt-trial-*`.
2. Create the folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~386/r68/` (the builder writes its record into it). Run from your worktree root: `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34u_build.py --pin d002cae9d9de62d774a7bb9333f22139309ac77c --out C:/dev/irpt-release-r34u-g2 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~386/r68/RESIDENT_R34U_BUILD.json`. It takes several minutes (up to 600 s): if the tool-call limit hits, run it in the background and wait for it to end. Its last line begins `R34U-BUILD-OK` or `R34U-BUILD-BAD <why>`. On BAD: file a BLOCKING row quoting the line, report, and stop (do not edit the tools).
3. Print: the tarball sha256, size and member count; the two-build identity line; the delta (changed, added, removed); the import smoke line; the gate dry-run return codes; the sha256 of each host script. Say whether the tarball's member `ycharts-host/ycharts_session.js` has sha256 `db43e9f9...` (it must).
4. Run the three criteria below (the `tree` arm needs a python with jsonschema and referencing: plain `python`, not `-I`; it runs no pytest). Write the proof instance (shape of the AR-g-194 instance `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~384/IRPT_ANLREQ.TO-AR-g-194.resident-release-r34t-build-only-typed-etf-model-dates-left-out-line-risk-tables-and-the-swap-model-leg.proof_of_spec.json`, read it from the main tree `C:/dev/ajb_workspace` if absent; its `decomp_ref` takes only doc, vintage_commit and to_ref; use the validator's enum words for artifact kinds and states): `controls.mutant` = a copy of your record with `ycharts-host/ycharts_session.js` removed from `delta_vs_r34t.changed`, which `ar_release_u_checks.py record` must refuse (run it, record the FAIL line); `controls.determinism` = `two_builds.files_compared` equals `two_builds.identical` in your record (status word `STABLE`). Validate with `python .tools/proof-of-spec-check.py <instance> AR196-g-AC1,AR196-g-AC2,AR196-g-AC3`, commit the record and the proof, then flip the order's `<status>` to `complete` (commit alone) only on VALID and three PASS.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR196-g-AC1" cell_refs="AR-g-196"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_u_checks.py record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~386/r68/RESIDENT_R34U_BUILD.json</invocation><expect>^AR-RELS-record-OK$</expect></criterion>

<criterion id="AR196-g-AC2" cell_refs="AR-g-196"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_u_checks.py tree C:/dev/irpt-release-r34u-g2/irpt-resident-0485393f3a-r34u.tar.gz d002cae9d9de62d774a7bb9333f22139309ac77c</invocation><expect>^AR-RELS-tree-OK$</expect></criterion>

<criterion id="AR196-g-AC3" cell_refs="AR-g-196"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_u_checks.py scripts C:/dev/irpt-release-r34u-g2</invocation><expect>^AR-RELS-scripts-OK$</expect></criterion>

<expected_criteria>AR196-g-AC1,AR196-g-AC2,AR196-g-AC3</expected_criteria>

- AC1: the build record's delta against the running r34t tarball is exactly the five movers (the capture library among them), nothing added or removed, the artifact on disk has the recorded sha256, size and 325 members, the bindings moved only in capture.library_sha256 and provenance, the two builds are identical, the smoke reads 87 of 87 and the gate dry runs read 0, 31, 0, 33. At base it FAILs (no record).
- AC2: the tarball read by the checker's own code: every other member equals r34t's, each mover equals the pinned source (the library from the trunk path), the registry revisions and hashes equal r34t's, the bindings carry the pin, the new library sha, 51 files-from lines, tickets_table and opal_swap_model enabled, the lazy imports import, the earlier replays still pass on the tarball's own modules, and the shipped source carries each new behavior. At base it FAILs (no tarball).
- AC3: the four host scripts exist, are ASCII, pass bash -n, name NEW r34u and OLD r34t, bind the tarball, the host script and the package sums by sha256, want the new library on the host after the install, read the old one before it, and the rollback restores the kept old library before the old root's installer. At base it FAILs (no scripts).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~386/r68/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~386/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-196.resident-release-r34u-build-only-swap-record-fields-replaced-swap-line-chart-colours-and-the-trunk-capture-library.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-196`.
<owned_cells>AR-g-196</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR196-g-AC1,AR196-g-AC2,AR196-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~386/IRPT_ANLREQ.TO-AR-g-196.resident-release-r34u-build-only-swap-record-fields-replaced-swap-line-chart-colours-and-the-trunk-capture-library.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-196`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR196-g-AC1,AR196-g-AC2,AR196-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a build in a stage folder outside the repository and one record plus a proof in the worker folder; nothing is uploaded, installed, applied or run on a host. The release itself moves five members and the host capture library, and is installed only by a later CloudOps apply under a COO+CTO never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base (no record, no tarball, no scripts); the checker was calibrated by the issuer on a rehearsal build at an earlier pin (record OK, tree OK, scripts OK) and refuses the r34t tarball offered as r34u, a record missing the library mover and the r34t stage; the rollback's library guard and restore were tested against temp files in five cases. Traps: a stage folder inside the repository, any other irpt-release folder touched, a different pin, the library taken from the base pin. NOT seen (blind): the live host; the capture library on the live YCharts path (it is unused by the Opal path).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 all FAIL (nothing built).
