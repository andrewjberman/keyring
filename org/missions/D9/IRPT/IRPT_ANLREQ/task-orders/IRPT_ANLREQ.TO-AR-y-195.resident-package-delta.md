# TO IRPT_ANLREQ.TO-AR-y-195.resident-package-delta -- the resident package built at the live pin and at the release pin, and the delta between them

<to_id>IRPT_ANLREQ.TO-AR-y-195</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~55</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (two local tarballs outside the product tree; no AWS call)
**Decomp cell:** `AR-y-195` (`decompositions/IRPT_ANLREQ_DECOMP_R19R_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~55`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-55` (branch `wk-IRPT_ANLREQ-55`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~55 <0.9.0_WK_IRPT_ANLREQ~55@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W55-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. Scratch and throwaway worktrees go OUTSIDE the product tree and are left in place (you may not delete recursively; say where they are).

### THE CELL (`AR-y-195`, inlined) -- BUILD TWO LOCAL TARBALLS AND READ THEIR DELTA. Nothing is uploaded, installed or applied.

*What the resident rebuild would change, member by member.* The resident package is built from ONE backend pin over whole folders (`reports/build_resident_package.py`), so moving the reader members moves everything else in those folders that changed between the live pin and the release pin.

**Read first:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 3, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r19/YCHARTS_GENERATE_RELEASE_CENSUS.json` (its `resident` member), rows `IRPT_ANLREQ-D2-W51-S15`, `IRPT_BCKEND-D2-W333-S1` and `IRPT_BCKEND-D2-W328-S1`, and `infra/aws/lambda/investor-reporting/reports/build_resident_package.py` (its docstring: the arguments, the layout, `MSYS_NO_PATHCONV=1` and a Windows-form WORKTREE path on this box).

1. **Find the builder's arguments the live resident was built with.** `HOST_ROOT`, `ENROLLED_USER_ID`, `WRAPPER_SHA256`, `LIBRARY_SHA256`, `REGISTRY_ROW_PIN`: from the st32 packet and `2.0.0_SA_COO~G2`'s r10 census / release records for pin `0485393f3a` (root `/opt/irpt-resident/0485393f3a-st32`). Say where you read each; a value you cannot find is named in `not_read`, never invented. If the arguments cannot be found, STOP on this and file a BLOCKING row naming what is missing.
2. **The release pin** is `069b8f797e` (the shared head after the round-19 drains; it holds `uploads.py` @e93258c650 and `template_reader.py` @da7b3b10bc, r18.1). Say so in the record.
3. **Build both tarballs LOCALLY** with the builder (no AWS call), outside the product tree, in a throwaway worktree cut from the shared head if the builder needs a worktree: once at `0485393f3a` (the live pin) and once at `069b8f797e`, with the SAME arguments (the host root is the same string in both; the pin enters the root only on the host). Record each tarball's sha256 and member count. The builder must run twice identically (a determinism control: build the live pin twice and compare).
4. **Compute the delta** between the two tarballs: `only_in_old`, `only_in_new`, and `differing` (objects with `member`, `old_sha256`, `new_sha256`). Then `moved_by_this_release` = the two reader members (`uploads.py` and `template_reader.py`, with their pins) and `other_differing_by_owner`: every OTHER differing member grouped by the project and order that last changed it (`git log -1 --format='%h %s' <old>..<new> -- <path>`; say the project from the commit subject or the order it names; a member you cannot attribute is named as unattributed).
5. **State the three the CTO named:** is `ops/status.py` different (old and new blob), is `ycharts/research` in the new tarball and absent from the old (row W333-S1), and does the new tarball carry `IRPT_BCKEND-D2-W328-S1`'s repair (read the session code: `withAuthenticatedPage` and the stored-bundle probe; say what the new code does on a challenged probe, from the code, and whether the old differs). Say what you could not decide.
6. **Write `r19/RESIDENT_PACKAGE_DELTA.json`:** `old_pin`, `new_pin`, `builder_args_source`, `tarballs` (path, sha256, member count each), `determinism_control`, `only_in_old`, `only_in_new`, `differing`, `moved_by_this_release`, `other_differing_by_owner` (a mapping owner -> list of members), `named_by_the_cto` (the three answers of point 5), `claim`, `not_read`.
7. **In your report:** the counts, the owners whose members differ, the answer on each of the three named, and what the resident's operator must read on the host to complete the comparison.

### ACCEPTANCE

<criterion id="AR195-y-AC1" cell_refs="AR-y-195"><invocation>python C:/dev/wk-irpt-anlreq-55/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y195-delta --root C:/dev/wk-irpt-anlreq-55</invocation><expect>Y195-DELTA-OK</expect></criterion>
`AR195-y-AC1`: the record names both pins, the arguments' source, the members only in one tarball, every differing member with both hashes, the two reader members as moved, and the other differing members grouped by owner.

<criterion id="AR195-y-AC2J" cell_refs="AR-y-195" judgment="true"/>
`AR195-y-AC2J` (judgment, graded at L9, never by you): both tarballs were built by the builder with the same arguments (a determinism control), the delta is complete rather than sampled, each owner attribution was read from the log, and the three named answers come from the code.

<expected_criteria>AR195-y-AC1 AR195-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/` and this order's file (status flip only).
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R_Y.md</decomp_doc>
<owned_cells>AR-y-195</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR195-y-AC1 AR195-y-AC2J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/IRPT_ANLREQ.TO-AR-y-195.resident-package-delta.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-195`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR195-y-AC1,AR195-y-AC2J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- two local tarballs outside the product tree; nothing is uploaded, installed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (round-19 analysis section 3: the pair names every member that differs from the live resident) against the cell; the lens: a delta that samples instead of enumerating, or arguments invented for the builder. The order requires a determinism control, an attribution read from the log for each owner, and arguments whose source is named. NOT seen: the resident host itself (0 host files read; the operator reads the host).
lane: the worker's deliverables and one append to the project's investigation channel.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 ruling on the resident leg (msg 6741, section 3) as its own workstream `YR`. Base: `AR195-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order: the issuer writes the pair on the records of `AR-y-191`, `-192`, `-193` and this one, and cuts an applier order for `0.7.0_AE_CloudOps~YC2`.
