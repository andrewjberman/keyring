# TO IRPT_ANLREQ.TO-AR-y-196.resident-install-semantics -- overlay or replace: the resident installer's semantics proved on a scratch install

<to_id>IRPT_ANLREQ.TO-AR-y-196</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~55</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-196` (`decompositions/IRPT_ANLREQ_DECOMP_R19R2_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~55`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-55` (branch `wk-IRPT_ANLREQ-55`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~55 <0.9.0_WK_IRPT_ANLREQ~55@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W55-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-196`, inlined) -- READ AND SCRATCH-INSTALL. Nothing is installed on a host.

*Does a resident release REPLACE the package or OVERLAY it?* The builder produces 182 members and the live resident has 298: 116 live members come from elsewhere (pydeps merged on the host, `ycharts-host/`, a different schemas layout, `SHA256SUMS`). If a release deletes them, it is not this pair's, and it STOPS (CTO, section 4).

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 4 point 1, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_PACKAGE_DELTA.json` (members `live_tar_fidelity`, `what_the_operator_reads_on_the_host`, `not_read`), `infra/aws/lambda/investor-reporting/ycharts/generate/install-resident.sh` (the installer; read it all), the st32 install script and packet for pin `0485393f3a` (`install_st32.sh`; find it from the delta record's `builder_args_source` and from `2.0.0_SA_COO~G2`'s r10 census), and `infra/aws/lambda/investor-reporting/reports/build_resident_package.py` (its docstring: pydeps are merged into package_root ON THE HOST; SHA256SUMS is generated on the host).

1. **Read the installer line by line** and quote, with line numbers, every step that touches the package root: where the tarball is extracted, whether the extraction target is a NEW directory named for the pin or an existing one, whether anything is removed (`rm`, `--delete`, `--overwrite`, `mv`, a symlink swap), what is copied from the previous root into the new one (pydeps, `ycharts-host/`, bindings), when `SHA256SUMS` is generated, and what it does while the service is active. Say which of OVERLAY (new files over the existing root; nothing removed), REPLACE (the root is emptied or the old tree removed first) or NEW_ROOT_COPY (a new directory per pin, the live members copied or linked in from the old root) it is, and the line that proves it.
2. **Scratch install proof.** In a folder OUTSIDE the product tree (leave it, say where): make a live-shaped package = the OLD tarball from the delta record's `tarballs` (`C:/dev/ar195-55-tarballs/`, the live-pin build; if missing, rebuild it with the recorded arguments) extracted, PLUS 116 dummy files named like the unbuilt live members (use the delta record's `live_tar_fidelity` for their names; if it lists fewer, say so and use what it lists). Then perform the installer's extraction and copy steps for the NEW tarball (the release-pin build) against that scratch root, executing the SAME commands the installer runs (you may not run `systemctl`, `sudo` or anything on a host; run only the file operations, with the host paths replaced by the scratch paths, and say exactly which lines you ran). Print the member list before and after and the denominators: members before, after, the unbuilt members before and after, members added, members removed, members whose bytes changed.
3. **Write `r19/INSTALL_SEMANTICS_SCRATCH_PROOF.json`:** `install_mode` (`OVERLAY`, `REPLACE` or `NEW_ROOT_COPY`), `installer_lines_read` (objects: `file`, `line`, `quote`), `scratch` (path and how it was made), `commands_run` (the exact lines), `before_member_count`, `after_member_count`, `unbuilt_members_before`, `unbuilt_members_after`, `members_added`, `members_removed`, `members_changed`, `claim`, `not_read` (the host itself: nothing about the host's state beyond the recorded install is claimed).
4. **In your report:** the mode and the line that proves it, the before/after denominators, and whether any unbuilt member is lost; if the mode is REPLACE, say so first.

### ACCEPTANCE

<criterion id="AR196-y-AC1" cell_refs="AR-y-196"><invocation>python C:/dev/wk-irpt-anlreq-55/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y196-install --root C:/dev/wk-irpt-anlreq-55</invocation><expect>Y196-INSTALL-OK</expect></criterion>
`AR196-y-AC1`: the record names the install mode (OVERLAY, REPLACE or NEW_ROOT_COPY), the installer lines read, the scratch proof's before and after counts and the unbuilt members before and after.

<criterion id="AR196-y-AC2J" cell_refs="AR-y-196" judgment="true"/>
`AR196-y-AC2J` (judgment, graded at L9, never by you): the mode is proved by the installer's own commands run on a live-shaped scratch root with denominators, not by reading alone, and a lost unbuilt member would have been reported.

<expected_criteria>AR196-y-AC1 AR196-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R2_Y.md</decomp_doc>
<owned_cells>AR-y-196</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/IRPT_ANLREQ.TO-AR-y-196.resident-install-semantics.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-196`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- scratch folders outside the product tree; the installer's file operations only, with host paths replaced; nothing is installed on a host or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (round-19 analysis section 4 point 1: prove overlay or replace with a scratch install, denominator printed) against the cell; the lens: a scratch install that does not run the installer's own commands. The order requires the exact commands, before and after member lists and denominators. NOT seen: the host's real package (0 host files read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 analysis section 4 point 1. Base: `AR196-y-AC1` FAIL as expected (no record).
