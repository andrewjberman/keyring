# TO IRPT_ANLREQ.TO-AR-y-200.resident-two-member-release -- the resident release that moves only the reader members, built with st32's recipe and proved in a scratch tree

<to_id>IRPT_ANLREQ.TO-AR-y-200</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~55</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-200` (`decompositions/IRPT_ANLREQ_DECOMP_R19R4_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

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

### THE CELL (`AR-y-200`, inlined) -- BUILD THE TWO-MEMBER RESIDENT RELEASE AND PROVE IT IN A SCRATCH TREE. Nothing is uploaded, installed or applied.

*The release moves the reader and nothing else.* The Lambda's release moves exactly `uploads.py` and `template_reader.py` (AR-y-193); the resident's must too, built the way st32 was built.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_RECIPE_AND_DELTA.json` (the recovered recipe: `recipe_steps`, the clock-held control, `st32_rebuild`, the removed-members note; its evidence folder `r19/recipe_evidence/` holds the scripts that rebuilt st32), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/INSTALL_SEMANTICS_SCRATCH_PROOF.json` (the host script's lines: a NEW root per pin, bindings, SHA256SUMS regenerated on the host, the refusals at lines 42 and 95, the rollback at line 112), the CTO's rulings `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 4 items 4 and 5 (msgs 6760 and 6770: `extract.py` and every other member stay at st32 bytes; `SECTION_BOUNDS` stays OFF), and `AR-y-193`'s record `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r19/RELEASE_BUILD_RECORD.json` (the Lambda's two-member release).

1. **Make the build input.** In a throwaway worktree OUTSIDE the product tree cut at st32's pin `0485393f3a`, replace `infra/aws/lambda/investor-reporting/intake/uploads.py` and `.../intake/template_reader.py` with their blobs at the release pin `069b8f797e` (the same blobs the Lambda release moves: `uploads.py` @e93258c650, `template_reader.py` @da7b3b10bc) and make ONE local scratch commit there (never pushed). Say its hash.
2. **Find what must move with them.** The new `uploads.py` and `template_reader.py` import other members. Import each in the scratch package (step 3) and record every ImportError or missing name; if a member must move for them to import, add the MINIMUM set from the release pin, name each with the reason (the import line), and re-run. The CTO's rule: the reader members and what imports them; nothing else.
3. **Build with the SAME recipe** as the st32 rebuild (same builder blob `e1e58c2d`, the recorded arguments, the clock held to the recorded `generated_at`), with the scratch commit as the pin source for the package files (the census pin, the opal map, the extra members and the ycharts-host files stay exactly as the st32 recipe takes them). Record the tarball path and sha256.
4. **Delta against the st32 rebuild** (from AR-y-199): `differing`, `only_in_old`, `only_in_new`, `removed_members_count`. Expected: the two reader members, plus the generated `reports/resident_bindings.json` and `SHA256SUMS` (say what changed inside the bindings: provenance and, if the root name changes, HOST_ROOT), plus any member of the minimal import set. ANY other difference is a finding: explain it or fix the build input.
5. **Root naming.** The host script creates `$R/$NEW` from the tarball; the bindings carry the host root path. State, from the host script and the bindings, what `NEW` must be for the bindings to point at the new root, whether the build must therefore be made with a new HOST_ROOT (and what that changes: the bindings only), and what the rollback line 112 re-installs. Build the tarball with the HOST_ROOT the release would use: propose one name (e.g. `/opt/irpt-resident/0485393f3a-r19`) and say why; the pair names it.
6. **Prove the reader's tests on that build in a scratch tree.** Extract the tarball to a scratch folder outside the tree, copy the test files of the named tests from the release pin (the tarball carries no tests), and run them against the extracted package modules with `PYTHONPATH` set to the package root: at least `tests/test_stored_input_contract.py`, `tests/test_template_reader.py`, `tests/test_template_account_totals.py`, `tests/test_template_uploads.py`, `tests/test_correction_words.py` and `tests/test_deferred_resolution.py` of `intake`. Report `named_tests`, `passed`, `failed`, `skipped`, and the denominator; every failure is explained one by one (a test that needs a member the package does not carry, because the test file is the head's, is NOT a pass; say which). If a reader test fails because a member is at st32 bytes, that member goes to the minimal import set or the finding goes to the CTO: do NOT widen the release silently.
7. **Write `r19/RESIDENT_TWO_MEMBER_RELEASE.json`:** `base_pin`, `scratch_commit`, `recipe_args_source`, `minimal_import_set` (a list; possibly empty), `delta_vs_st32_rebuild` (`differing` as objects with `member`, `old_sha256`, `new_sha256`, `reason`; `only_in_old`; `only_in_new`; `removed_members_count`), `tests` (`named_tests`, `passed`, `failed`, `skipped`, `denominator`, `failures_explained`), `tarball` (path, sha256, member count, determinism control), `root_naming`, `claim`, `not_read`.
8. **In your report:** the delta in one line, the tests, the root naming, anything beyond the two readers that had to move and why.

### ACCEPTANCE

<criterion id="AR200-y-AC1" cell_refs="AR-y-200"><invocation>python C:/dev/wk-irpt-anlreq-55/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y200-two --root C:/dev/wk-irpt-anlreq-55</invocation><expect>Y200-TWO-OK</expect></criterion>
`AR200-y-AC1`: the build differs from the st32 rebuild only in the two reader members, the generated bindings and SHA256SUMS, and any named minimal import set; it removes nothing; and the reader's named tests pass on it.

<criterion id="AR200-y-AC2J" cell_refs="AR-y-200" judgment="true"/>
`AR200-y-AC2J` (judgment, graded at L9, never by you): the tests were run against the extracted package (not the repository), the import set is minimal and each member in it is justified by an import line, and the root naming is read from the host script and the bindings.

<expected_criteria>AR200-y-AC1 AR200-y-AC2J</expected_criteria>

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-13, after the CTO's msg 6778 and the signed pair).** `AR200-y-AC1` now accepts the two failures the CTO ACCEPTED as named limits in the one two-leg pair -- S26 (`test_the_readers_output_on_the_fixtures_is_pinned_to_its_version`: the nine csv and xlsx fixtures are not packaged; 5 of 5 pass with them restored) and S25 (`test_correction_words_are_the_envelopes_words`: the held `ops/status.py` lacks 24 words the release `uploads.py` declares) -- provided each is in `tests.failures_explained` and `tests.failed` equals the number explained; any other failure still fails. The check is `ar19_checks.py y200-two`; the issuer's run prints `Y200-TWO-OK` on the worker's record. The worker's proof instance recorded AC1 as FAIL at the time; that row is left as the worker wrote it and the compile packet carries this amendment for the L9 grade. The release this order built was applied under the signed pair (resident 0485393f3a-r19, 2026-10-13T06:09:33Z). Gate limb that graded this amendment: none stated by the gate (the issuer amends its own order's criteria; the CTO reads it at the round-20 analysis).

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R4_Y.md</decomp_doc>
<owned_cells>AR-y-200</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/IRPT_ANLREQ.TO-AR-y-200.resident-two-member-release.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-200`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a local tarball and scratch folders outside the product tree; nothing is uploaded, installed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's hold (msg 6770: the release moves only the reader members and what imports them, proven by the reader's tests in a scratch tree) against the cell; the lens: tests run against the repository instead of the package, or a member quietly widened to make a test pass. The order requires the tests to run against the extracted package, a minimal import set with the import line for each member, and a stop-and-report if a reader test needs another member. NOT seen: the host (0 host files read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's msg 6770 (section 4 item 5) as workstream `YR` round 4. Base: `AR200-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
