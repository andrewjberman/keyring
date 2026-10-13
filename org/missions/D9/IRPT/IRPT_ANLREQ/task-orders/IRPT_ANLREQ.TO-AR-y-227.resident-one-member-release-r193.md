# TO IRPT_ANLREQ.TO-AR-y-227.resident-one-member-release-r193 -- the resident release that moves only template_reader.py, built from the release-19 tarball and proved in a scratch tree

<to_id>IRPT_ANLREQ.TO-AR-y-227</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~71</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-227` (`decompositions/IRPT_ANLREQ_DECOMP_R21R_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~71`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-71` (branch `wk-IRPT_ANLREQ-71`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~71 <0.9.0_WK_IRPT_ANLREQ~71@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W71-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-227`, inlined) -- BUILD THE ONE-MEMBER RESIDENT RELEASE AND PROVE IT IN A SCRATCH TREE. Nothing is uploaded, installed or applied.

*Release 19 installed the resident root `0485393f3a-r19` (tarball `irpt-resident-0485393f3a-r19.tar.gz`, sha256 `84df6479655c07ae6000af40404e53eb056b4c403aa9134bbe9c1521317d497a`, staged at `C:/dev/irpt-release-r19/`) with the reader r18.1. This release moves ONE member: `intake/template_reader.py` (r19.3, the trunk head's blob). `intake/uploads.py` stays at `176682cb1545435eec084376b3c37a578ca70d05f9ad5a376c0f2275f62b05ea`, the bytes the r19 root already holds. The CTO's rule since release 19: the reader members and what imports them; nothing else.*

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_TWO_MEMBER_RELEASE.json` (the method you repeat: the scratch commit at st32's pin, the recipe arguments, the clock-held control, the delta, the tests, the root naming; its sibling files in that folder hold the scripts), `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_RECIPE_AND_DELTA.json` (the recovered recipe) and the host script of release 19, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release19/resident_host_install_0485393f3a-r19.sh` (sha256 `8b53be1328f9ed20827e0118aee9c1b1b402d66b25d82a434275b1c83cfa57f0`).

1. **Make the build input.** As AR-y-200 step 1, but with ONE replaced member: in a throwaway worktree OUTSIDE the product tree cut at st32's pin `0485393f3a`, replace `infra/aws/lambda/investor-reporting/intake/uploads.py` with its blob at the r19 release pin `069b8f797e` (as AR-y-200 did; the bytes must hash to `176682cb...` -- check) and `intake/template_reader.py` with the HEAD blob of your worktree (READER_VERSION `irpt-template-reader.r19.3`), and make ONE local scratch commit (never pushed). Say its hash and both sha256.
2. **Build with the SAME recipe** as AR-y-200 (same builder blob, the recorded arguments, the clock held to the recorded `generated_at`), with the scratch commit as the pin source. Use the new HOST_ROOT `/opt/irpt-resident/0485393f3a-r193` (rollback root is the running `0485393f3a-r19`). Record the tarball path and sha256, and the determinism control (two builds: 298 of 298 files identical by name and sha256; the `tar.gz` hashes may differ by the gzip clock, so the SHIPPED FILE is the control).
3. **Delta against the release-19 tarball** (`C:/dev/irpt-release-r19/irpt-resident-0485393f3a-r19.tar.gz`; check its sha256 first, extract to a scratch folder): `differing`, `only_in_old`, `only_in_new`, `removed_members_count`. Expected: EXACTLY `intake/template_reader.py`, `reports/resident_bindings.json` (only the root name and `provenance.member_overrides`; say what changed inside) and `SHA256SUMS`; nothing else. If the new reader imports a name another member lacks, record the ImportError and the MINIMUM member that must move with the import line (a finding for the CTO: do not widen silently).
4. **Host script.** Copy the r19 host script to `r21/resident_host_install_0485393f3a-r193.sh` in your deliverable folder and change ONLY the lines that name the release (`NEW`, `OLD` (= `0485393f3a-r19`), `WANT_TAR`, the member checks for `template_reader.py`, `written_by`, `ledger` and the header comment); print a `diff` of the two scripts and the sha256 of yours. Its 17 member-check hashes must equal the new tarball's members (compute and say so).
5. **Prove the reader's tests on the build, in a scratch tree.** As AR-y-200 step 6: extract the tarball outside the tree, copy the test files from your worktree (the tarball carries none), run the named tests against the extracted package with `PYTHONPATH` set to the package root: `tests/test_stored_input_contract.py`, `tests/test_template_reader.py`, `tests/test_template_account_totals.py`, `tests/test_template_uploads.py`, `tests/test_correction_words.py`, `tests/test_deferred_resolution.py`, `tests/test_account_value_backstop.py` of `intake`. Report `named_tests`, `passed`, `failed`, `skipped`, `denominator`; explain each failure one by one (the two the CTO already accepted -- the nine fixtures not packaged, S26, and the 24 correction words the held `status.py` lacks, S25 -- are named as such; any other failure is a finding).
6. **Write `r21/RESIDENT_ONE_MEMBER_RELEASE.json`:** `base_tarball` {`path`, `sha256`}, `scratch_commit`, `delta_vs_r19_tarball` (`differing` as objects `member`, `old_sha256`, `new_sha256`, `reason`; `only_in_old`; `only_in_new`; `removed_members_count`), `tarball` (path, sha256, member count, determinism control), `root_naming` (`NEW`, `OLD`, what the bindings carry), `host_script` (path, sha256, `lines_changed`, `member_checks_equal_tarball` true or false), `tests` (`named_tests`, `passed`, `failed`, `skipped`, `denominator`, `failures_explained`), `claim`, `not_read`.
7. **In your report:** the delta in one line, the tarball sha256, the tests, the host script's changed lines.

### ACCEPTANCE

<criterion id="AR227-y-AC1" cell_refs="AR-y-227"><invocation>python C:/dev/wk-irpt-anlreq-71/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y227-resident --root C:/dev/wk-irpt-anlreq-71</invocation><expect>Y227-RESIDENT-OK</expect></criterion>
`AR227-y-AC1`: the build is the release-19 tarball with exactly `template_reader.py`, the bindings and the sums changed, adds and removes no member, carries a 64-hex tarball digest and a host script digest, and the reader's tests pass on it except the two CTO-accepted, explained failures.

<criterion id="AR227-y-AC2J" cell_refs="AR-y-227" judgment="true"/>
`AR227-y-AC2J` (judgment, graded at L9, never by you): the base tarball was the release-19 file (its sha256 checked, not recalled), the tests ran against the extracted package and not the repository, the host script differs from release 19's only in the lines that name the release, and nothing was uploaded, installed or applied.

<expected_criteria>AR227-y-AC1 AR227-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~71/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else. The tarball and scratch folders stay OUTSIDE the product tree (say where); `C:/dev/irpt-release-r19/` is read, not written.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R21R_Y.md</decomp_doc>
<owned_cells>AR-y-227</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~71/IRPT_ANLREQ.TO-AR-y-227.resident-one-member-release-r193.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-227`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR227-y-AC1,AR227-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a local tarball and scratch folders outside the product tree; nothing is uploaded, installed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's hold (the release moves only the reader and what imports it, proven by the reader's tests in a scratch tree) against the cell; the lens: tests run against the repository instead of the package, a base tarball taken from a record, or a member quietly widened to make a test pass. The order requires the base file's sha256, the tests against the extracted package, and a stop-and-report if the reader needs another member. NOT seen: the host (0 host files read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-21 analysis section 3 item 4 as workstream `YR` round 14. Base: `AR227-y-AC1` FAIL as expected (no record).
- The PAIR and the APPLY are not this order.
