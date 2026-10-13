# TO IRPT_ANLREQ.TO-AR-y-199.resident-recipe-and-delta -- st32's full assembly recipe recovered, rebuilt, and the delta redone

<to_id>IRPT_ANLREQ.TO-AR-y-199</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~55</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-199` (`decompositions/IRPT_ANLREQ_DECOMP_R19R3_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

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

### THE CELL (`AR-y-199`, inlined) -- RECOVER THE RECIPE, REBUILD, REDO THE DELTA. Nothing is uploaded, installed or applied.

*A resident release must be built the way st32 was built, or it loses live members.* The builder alone makes 184 members; the live st32 root has 326.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_PACKAGE_DELTA.json` (the round-19 delta of the BUILDER ALONE; its members `live_tar_fidelity`, `builder_args_source`, `tarballs`), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/INSTALL_SEMANTICS_SCRATCH_PROOF.json` (the install proof: the host script `resident_host_install_0485393f3a-st32.sh`, lines 9, 20, 23, 42, 95, 112; the 143 absent members by name), the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` sections 3 and 4, and YC2's records: `org/tier2_senior/0.7.0_AE_CloudOps~YC2/deliverables/irpt_ycdgen_st32/` (`D2_V1_INSTALL_20261011.txt`, `P1_PRE_READ_20261011.txt`, the proof instance), `.../irpt_ycdgen_st31/`, `.../irpt_ycdgen_st30/`, and `2.0.0_SA_COO~G2`'s st32 packet and r10 census (find them under `org/missions/D9/IRPT/IRPT_YCDGEN/` from the install proof's `installer_lines_read` and the delta's `builder_args_source`).

1. **Recover the recipe.** From those records (and the scripts they name: tar assembly, the wrapper, the library, `install_st32.sh`, `resident_host_install_*.sh`), write down EVERY step that produced st32's tarball: the builder call and its arguments, anything added AFTER the builder (the `ycharts-host/` files, fixtures, `docs/contracts/` schemas, `_gate/gate.py`, `data/firm_registry.json`, `intake/fixtures/`, `ycharts/research` extras), where each added file came from (a repo path at a pin, a host path, a generated file), and what the host adds after extraction (pydeps; SHA256SUMS). Quote file and line for each step. A step you cannot find is named in `not_read` as MISSING; never invent one.
2. **Run the recipe at st32's pin `0485393f3a`** locally (outside the product tree; MSYS_NO_PATHCONV=1 and Windows-form paths as the builder says), and compare the result with the live st32 root's 326 members by NAME and by CONTENT: use the recorded member list and hashes (the delta's `live_tar_fidelity`, the install proof's names, the st32 packet's SHA256SUMS if recorded). Report `members_total`, `matched_by_name`, `matched_by_content`, `unmatched_names`, and `host_origin_names` (members that exist only on the host: pydeps, host-generated files; name them, do not fabricate bytes), and `pass` = true ONLY if every member that CAN be produced locally matches by name and content and every one that cannot is a named host-origin member. If you cannot make it pass, STOP, set `pass` false, file a BLOCKING row with the unmatched names and what is missing (and what you would ask YC2), and do NOT build the release pin.
3. **Only if `pass` is true:** build the RELEASE pin `069b8f797e` with the SAME recipe and arguments; then redo the delta against the st32 build: `only_in_old`, `only_in_new`, `differing` (member, both sha256), `moved_by_this_release` (the two reader members), and `other_differing_by_owner` (as in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_PACKAGE_DELTA.json`, plus any member the recipe adds that the builder alone did not). Say the removed members count (it must be 0 for the host-created members the recipe carries).
4. **Write `r19/RESIDENT_RECIPE_AND_DELTA.json`:** `recipe_source` (the files and lines read), `recipe_steps` (ordered, each with its source), `st32_rebuild` (the object of point 2), `release_build` (tarball paths, sha256, member counts, determinism control), `delta` (the object of point 3), `named_by_the_cto` (status.py, ycharts/research, W328-S1 as before), `claim`, `not_read`.
5. **In your report:** the recipe in one paragraph, the st32 rebuild result first, then (only if it passed) the redone delta counts and the owners; what YC2 must be asked if the records are not enough.

### ACCEPTANCE

<criterion id="AR199-y-AC1" cell_refs="AR-y-199"><invocation>python C:/dev/wk-irpt-anlreq-55/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y199-recipe --root C:/dev/wk-irpt-anlreq-55</invocation><expect>Y199-RECIPE-OK</expect></criterion>
`AR199-y-AC1`: the record names the recipe's source and steps, the st32 rebuild PASSES by name and content (host-origin members named), and the delta is redone with the recipe.

<criterion id="AR199-y-AC2J" cell_refs="AR-y-199" judgment="true"/>
`AR199-y-AC2J` (judgment, graded at L9, never by you): each recipe step is quoted from a record, the st32 rebuild really compares content and not only names, a host-origin member is named rather than fabricated, and the release pin was built only after the st32 rebuild passed.

<expected_criteria>AR199-y-AC1 AR199-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R3_Y.md</decomp_doc>
<owned_cells>AR-y-199</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/IRPT_ANLREQ.TO-AR-y-199.resident-recipe-and-delta.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-199`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- local tarballs and scratch folders outside the product tree; nothing is uploaded, installed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's confirmation (msg 6767: the recipe rebuilds st32's 326 members by name and content before it builds the release pin) against the cell; the lens: a recipe that matches names but not bytes, or a host-origin member invented to make the count agree. The order requires a content comparison, named host-origin members and a stop if the rebuild does not pass. NOT seen: the host's real root (0 host files read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 6767 as workstream `YR` round 3. Base: `AR199-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
