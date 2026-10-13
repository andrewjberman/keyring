# TO IRPT_ANLREQ.TO-AR-y-193.release-build-record -- the BUILD_ONLY release build of irpt-ycharts-generate with the planned pins

<to_id>IRPT_ANLREQ.TO-AR-y-193</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-193` (`decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** AR-y-192 is merged
**NOT SPAWNED AT ISSUANCE.** The issuer spawns this order when AR-y-192 is merged, and states it in a spawn amendment. If there is none, STOP: the order was spawned too early.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### SPAWN AMENDMENT (issuer `2.0.0_SA_COO~Y2`, 2026-10-13)

`AR-y-192` is merged: drain @5743c86349 (the issuer's own run on the shared tree: `Y192-CENSUS-OK`; the two moved pins checked by the issuer against the head blobs: `uploads.py` `e93258c650` and `template_reader.py` `da7b3b10bc` both equal the head files).
The census's `planned_pin_moves` are your input: `uploads.py` `f09b802cdc` -> `e93258c650`, `template_reader.py` `3f29017cfc` -> `da7b3b10bc`; the four native members (`acceptance.py`, `submission.py`, `submission_service.py`, `durable_job.py`) are PINNED to the commits the census names
(`1eed34a8c0`, `1eed34a8c0`, `b3fc529601`, `7122afefc1`), added as staged rows, so the release moves ONLY the two reader members. `AR-y-191` is merged @069b8f797e (the scratch run shows the moved pair re-opens every pinned-stored template, and that a reader-only move refuses them: both files move together).
Nothing else in this order changes.

### THE CELL (`AR-y-193`, inlined) -- BUILD ONLY (a throwaway worktree). Nothing is uploaded, applied or pushed.

*The release BUILD of `irpt-ycharts-generate` with the planned pins, and the proof that it moves exactly the planned members.*

**Read first:** the census `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r19/YCHARTS_GENERATE_RELEASE_CENSUS.json` (its `planned_pin_moves` and `members_that_move` are your input), `infra/aws/lambda/ci/build-and-upload.sh` (the BUILD_ONLY branch near line 687; read it before you run it), the AR-y-145 build record (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/`) for the baseline package, and the act-4 ledger entry named in the census for how a throwaway worktree is used.

1. **Make the map edit as a PATCH, not on the trunk.** In a throwaway worktree OUTSIDE the product tree (cut from the current head: `git worktree add -b <name> <abs path outside the repo> HEAD`; say the path), apply the census's planned pin moves to the `irpt-ycharts-generate` entry of `infra/aws/lambda/ci/lambda-source-map.json`. Save the diff as `r19/RELEASE_MAP_PATCH.diff` in your deliverables. The trunk's map is NOT edited by this order.
2. **Build:** from that worktree run `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-ycharts-generate` (it builds after every gate and prints `BUILD_ONLY: <zip path> sha256=<base64>`; it uploads NOTHING in this mode; if you read the script and find it would upload or write to AWS in BUILD_ONLY mode, STOP and file a BLOCKING row). If a gate refuses, record the refusal and STOP; do not bypass a gate.
3. **Manifest:** for the built zip, record every member's sha256 (`member_manifest`: name -> sha256, at least 20 members). Build the BASELINE the same way from the CURRENT map without the patch (BUILD_ONLY, same worktree, patch reverted by a second throwaway worktree) and record its manifest. `actual_members_that_differ_from_baseline` = the members whose hashes differ; `planned_members_that_move` = the census's list. They must be the same set; if not, say which member differs and why (a row, not a guess).
4. **Write `r19/RELEASE_BUILD_RECORD.json`:** `package_sha256`, `baseline` (its package sha256 and manifest hash), `member_manifest`, `planned_members_that_move`, `actual_members_that_differ_from_baseline`, `patch` (the diff's path and blob), `worktrees` (the paths you made, left in place), `claim`, `not_read` (the live package: the executor compares live members at its first leg).
5. **In your report:** the package hash, whether the planned and actual member sets agree, and what the executor must read from the live package to complete the comparison.

### AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13, after the first worker's BLOCKING row `IRPT_ANLREQ-D2-W51-S16`; the worker was right and the criterion was the issuer's error)

The first run built the patch package and an UNPATCHED baseline and found six members differ, not two: the four native members (`acceptance.py`, `submission.py`, `submission_service.py`, `durable_job.py`) are PINNED in the patch to the commits the live package matches, while the
unpatched baseline carries their HEAD blobs. "Moves exactly the reader members" is true against the LIVE package, not against a map that has not yet held the natives. The baseline of the comparison must therefore be a LIVE-EQUIVALENT build. Do this:
1. Build a THIRD package, `live_equivalent`, from the SAME base commit: the current map with ONLY the four native holds applied (the same four pins as the patch) and NOT the two reader moves. (Make it in a third throwaway worktree outside the product tree, BUILD_ONLY, same command; copy each zip to a distinct file as soon as it is built, because BUILD_ONLY writes one fixed temp path: row S17.)
2. In `r19/RELEASE_BUILD_RECORD.json`: `live_equivalent_baseline` (its package sha256, member count, manifest hash and how it was built), `actual_members_that_differ_from_baseline` = the members whose hashes differ between the RELEASE package and the LIVE-EQUIVALENT baseline (expected: exactly `uploads.py` and `template_reader.py`), `differs_from_unpatched_baseline` = the six you already measured (keep them, they are the evidence for the natives), and `native_members_release_vs_census_live` unchanged. The `baseline` member may keep the unpatched baseline's description. If the release and the live-equivalent differ in any member other than the two, say which and why (a row).
3. Write in the record the BASE COMMIT of all three builds and say that the executor must build the release from a commit that carries the same members (the package depends on the commit it is built from for every member the map does not pin): name `base_commit` for the executor.
4. Re-run `y193-build` (the check now also requires `live_equivalent_baseline` and `differs_from_unpatched_baseline`), re-validate the proof (a `controls.mutant` must FIRE), flip `<status>` to `complete` only when the check prints OK and the proof is VALID, and commit as a NEW commit. Row S16 is answered by this amendment; say so in your report. Do not delete the earlier worktrees or zips.

### ACCEPTANCE

<criterion id="AR193-y-AC1" cell_refs="AR-y-193"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y193-build --root C:/dev/wk-irpt-anlreq-51</invocation><expect>Y193-BUILD-OK</expect></criterion>
`AR193-y-AC1`: the record names the package hash, a member manifest of at least 20 members, and a planned-versus-actual member set that agree.

<criterion id="AR193-y-AC2J" cell_refs="AR-y-193" judgment="true"/>
`AR193-y-AC2J` (judgment, graded at L9, never by you): nothing was uploaded or applied, the trunk's map is unedited, and the build moves exactly the members the census planned.

<expected_criteria>AR193-y-AC1 AR193-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md</decomp_doc>
<owned_cells>AR-y-193</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-193.release-build-record.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-193`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading the AR-y-145 build record and the build script's BUILD_ONLY branch: BUILD_ONLY builds after every gate and keeps the zip; nothing is uploaded; the trunk's map is not edited. The package is a local file.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading row W53-S9 against the cell; the lens: a build that ships a native unpinned member nobody meant to ship. The order compares the planned and the actual member sets. NOT seen: the live package (0 live objects read; the executor compares at its first leg).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 analysis item 1. NOT SPAWNED until `AR-y-192` is merged (its planned pin moves are this order's input). Base: `AR193-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order: the issuer writes the pair on the records of `AR-y-191`, `-192`, `-193` and cuts an applier order with a deploy-ledger entry.
