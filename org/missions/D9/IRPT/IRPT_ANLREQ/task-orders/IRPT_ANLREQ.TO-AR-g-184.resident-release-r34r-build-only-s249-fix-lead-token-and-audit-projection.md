# TO-AR-g-184 -- BUILD ONLY: the resident release r34r (r34q plus the S249 comparison-path fix, the retained-line lead token and the audit source projection) as a tarball with its package sums and four host scripts

<to_id>IRPT_ANLREQ.TO-AR-g-184</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~357</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>60</round>
<workstream>~GREL7</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-184` (`decompositions/IRPT_ANLREQ_DECOMP_R60_G.md`) |
**outcome_ref:** FWD-10 (PRD v0.25 @b83ce81b5b, C-MODEL-SOURCE; CTO msg 11442, ruling R1) | **depends_on:** AR-g-182, AR-g-183 (merged) and Y2's AR-y-487 (trunk 11fb915f82d). Nothing is deployed by this cell.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~357`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-357` (branch `wk-IRPT_ANLREQ-357`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~357 <0.9.0_WK_IRPT_ANLREQ~357@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W357-S<k>` (check the channel file for `W357` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Do NOT run `git sparse-checkout`.
- **The checker** is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_r_checks.py` (read it if it is a file; you cannot edit it). It computes every expected value itself, independent of your work: if your result and the checker's differ, re-read the cell text before you doubt the checker, and if you still believe the checker is wrong file a BLOCKING row quoting both results, and stop on that criterion.

### THE CELL (`AR-g-184`, inlined)

**What this cell is.** BUILD ONLY. You build the resident release r34r (the tarball, its package sums and the four host scripts) from a pin with a builder the issuer wrote and rehearsed, and prove it. Nothing is uploaded, installed, applied or run on a host; no AWS call, no network, no push, no deploy. The stage folder is OUTSIDE the repository. You write no product code and you do not edit the tools or the checker.

**Why r34r exists.** Run 7I (a Multi-Comp filing on the r34q resident) passed admission and then stopped: the resident's Opal comparison path built the vendor upload it never uses (RecipeRefused, row S249) and read key/label/ticker fields the retained catalogue entries do not carry. r34r packages the fixes (cells AR-g-182 and AR-g-183, merged `6422a8dc359` and `c02fdd2fd64`): `ycharts/generate/frozen_worker.py` (`prepare(upload=False)`, `comparison_keys`), `ycharts/generate/resident_worker.py` (`_opal_comparables` on the real catalogue shape), `ycharts/generate/resident_main.py` (the retained line carries `lead=<token>` for our own Refused/Attention classes), and 2.0.0_SA_COO~Y2's `ycharts/generate/ticket_audit_source.py` (plain-name projection, trunk `11fb915f82d`). The registry file and the `tickets_table` binding are r34q's and do not move.

**Facts (all measured by the issuer, who rehearsed this exact build at this pin in a scratch stage).**
- Pin `32bb8d5a673d3e0dd3c6efc933b7f0db5206533a` (a full 40-hex commit on this branch's history). The files-from list at the pin is `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt`, 50 lines (r34q's 49 plus `frozen_worker.py`, which the packaged tree carried from the base pin).
- The OLD root, the tarball running on the host: `C:/dev/irpt-release-r34q-g2/irpt-resident-0485393f3a-r34q.tar.gz`, sha256 `f757171891f3924458123168abe2ccbba87d4b5bc12821cfa0f59b0f38b9266b`. The r34n tarball (`C:/dev/irpt-release-r35h/irpt-resident-0485393f3a-r34n.tar.gz`, sha256 `89cad47247e6785e6b61e60112b04dfaa3cd2d5de88aef6023959692da76d899`) is also read by the builder.
- Against r34q the release moves exactly 6 members (SHA256SUMS, reports/resident_bindings.json (provenance only), ycharts/generate/frozen_worker.py, ycharts/generate/resident_main.py, ycharts/generate/resident_worker.py, ycharts/generate/ticket_audit_source.py) and adds none: 323 members. The issuer's rehearsal tarball sha256 is `77ec08f5a591de5584abb71787eb74c86bcbd3167416f2b411befc750140b828` (builds are held to a fixed clock, so yours should equal it).
- The tools: `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34r_build.py` (the builder), `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/make_scripts_r34r.py` (its host-script generator), `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/build_resident_package.py` (the release builder it runs). Read the builder's docstring first.

**What to do.**
1. Confirm, and STOP with a BLOCKING row quoting the line if any is false: (a) `sha256sum` of the r34q and r34n tarballs prints the two values above; (b) `git cat-file -t 32bb8d5a673d3e0dd3c6efc933b7f0db5206533a` prints `commit` and `git show 32bb8d5a673d3e0dd3c6efc933b7f0db5206533a:org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/files_from_r34.txt` has 50 lines; (c) the folder `C:/dev/irpt-release-r34r-g2` does not exist; (d) the tool files above exist on disk. Never touch, create inside or delete any other folder named `irpt-release-*` or `irpt-trial-*`.
2. Run from your worktree root: `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34r_build.py --pin 32bb8d5a673d3e0dd3c6efc933b7f0db5206533a --out C:/dev/irpt-release-r34r-g2 --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~357/r65/RESIDENT_R34R_BUILD.json`. It takes several minutes (up to 600 s): if the tool-call limit hits, run it in the background and wait for it to end. Its last line begins `R34R-BUILD-OK` or `R34R-BUILD-BAD <why>`. On BAD: file a BLOCKING row quoting the line, report, and stop (do not edit the tools).
3. Print: the tarball sha256, size and member count; the two-build identity line; the delta (changed, added, removed); the import smoke line; the gate dry-run return codes; the sha256 of each host script. State whether the tarball sha256 equals the rehearsal's above (a difference is not a failure of this cell: file an OBSERVATION row with both values).
4. Run the three criteria below (the `tree` arm needs a python with jsonschema and referencing: plain `python`, not `-I`; it runs no pytest). Write the proof instance (shape of the AR-g-181 instance `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~354/IRPT_ANLREQ.TO-AR-g-181.resident-release-r34q-build-only-s245-fix-tickets-table-and-the-audit-revision.proof_of_spec.json`, read it from the main tree `C:/dev/ajb_workspace` if absent; its `decomp_ref` takes only doc, vintage_commit and to_ref): `controls.mutant` = a copy of your record with `ycharts/generate/resident_main.py` removed from `delta_vs_r34q.changed`, which `ar_release_r_checks.py record` must refuse (run it, record the FAIL line); `controls.determinism` = `two_builds.files_compared` equals `two_builds.identical` in your record. Validate with `python .tools/proof-of-spec-check.py <instance> AR184-g-AC1,AR184-g-AC2,AR184-g-AC3`, commit the record and the proof, then flip the order's `<status>` to `complete` (commit alone) only on VALID and three PASS.


### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR184-g-AC1" cell_refs="AR-g-184"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_r_checks.py record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~357/r65/RESIDENT_R34R_BUILD.json</invocation><expect>^AR-RELR-record-OK$</expect></criterion>

<criterion id="AR184-g-AC2" cell_refs="AR-g-184"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_r_checks.py tree C:/dev/irpt-release-r34r-g2/irpt-resident-0485393f3a-r34r.tar.gz 32bb8d5a673d3e0dd3c6efc933b7f0db5206533a</invocation><expect>^AR-RELR-tree-OK$</expect></criterion>

<criterion id="AR184-g-AC3" cell_refs="AR-g-184"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_release_r_checks.py scripts C:/dev/irpt-release-r34r-g2</invocation><expect>^AR-RELR-scripts-OK$</expect></criterion>

<expected_criteria>AR184-g-AC1,AR184-g-AC2,AR184-g-AC3</expected_criteria>

- AC1: the build record's delta against the running r34q tarball is exactly the six movers, nothing added or removed, the artifact on disk has the recorded sha256, size and 323 members, the bindings moved only in provenance, the two builds are identical, the smoke reads 86 of 86 and the gate dry runs read 0, 31, 0, 33. At base it FAILs (no record).
- AC2: the tarball read by the checker's own code: every other member equals r34q's, each mover equals the pinned source, the registry revisions and hashes equal r34q's, the bindings carry the pin, 50 files-from lines and tickets_table, the lazy imports import, the admission replay passes, and the tarball's own extracted modules pass the frozen-read, comparables and retained-line checks. At base it FAILs (no tarball).
- AC3: the four host scripts exist, are ASCII, pass bash -n, name NEW r34r and OLD r34q, bind the tarball, the host script and the package sums by sha256, and carry one member check per mover. At base it FAILs (no scripts).

## BOUNDS

- **Grant.** The `<paths>` block only. Every other file is read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~357/r65/
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~357/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-184.resident-release-r34r-build-only-s249-fix-lead-token-and-audit-projection.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R60_G.md</decomp_doc> round 60, workstream ~G, cell `AR-g-184`.
<owned_cells>AR-g-184</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR184-g-AC1,AR184-g-AC2,AR184-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~357/IRPT_ANLREQ.TO-AR-g-184.resident-release-r34r-build-only-s249-fix-lead-token-and-audit-projection.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-184`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the code and tests first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's RESULT line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR184-g-AC1,AR184-g-AC2,AR184-g-AC3` BEFORE the flip to complete. Flip the order's `<status>` to complete ONLY if all three criteria PASS.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~308/IRPT_ANLREQ.TO-AR-g-170.producer-guard-held-price-layout-and-stale-tests.proof_of_spec.json` (read it from the main tree `C:/dev/ajb_workspace` if absent in your sparse worktree).
</proof_of_spec>

**REPORT (final message):** the commit hashes, the three criterion outputs (the RESULT lines), and any row filed.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- a build in a stage folder outside the repository and one record plus a proof in the worker folder; nothing is uploaded, installed, applied or run on a host. The release itself moves six members and is installed only by a later CloudOps apply under a COO+CTO never-widen pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache key or TTL is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- the criteria were dry-run at the base from the invocations above: all three criteria FAIL at base (no record, no tarball, no scripts); the checker was calibrated by the issuer on a rehearsal build at this pin (record OK, tree OK, scripts OK) and refuses the r34q tarball offered as r34r (delta empty, four movers not the pinned source, bindings unmoved, the extracted frozen-read check fails). Traps: a stage folder inside the repository, any other irpt-release folder touched, a different pin. NOT seen (blind): the live host and the live Opal producer's reads of the two model objects (the next filing reads them).
</preflight>

- Cut by the issuer inside its own decomposition (R60) on the CTO's order to decompose and issue FWD-10 as one round (msg 11442). Base: AC1, AC2 and AC3 all FAIL (nothing built).
