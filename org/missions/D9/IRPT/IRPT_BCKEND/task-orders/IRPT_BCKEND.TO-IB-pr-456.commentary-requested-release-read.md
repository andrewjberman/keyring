# TO IRPT_BCKEND.TO-IB-pr-456 -- BUILD ONLY plus AWS reads: the release read for `commentary_requested` -- every function that packages it, what would move in each, every reader of the accepted record

<to_id>IRPT_BCKEND.TO-IB-pr-456</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~312</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>152</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 5863 ("one cell then its release pair ... the pair names every reader of the accepted record with one read through each, and shows a submission WITHOUT the member is accepted exactly as today") | **Decomp cell:** `IB-pr-456` (decomposition section 144) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-312/` (bash `/c/dev/wk-irpt-bckend-312`). Work only there. **BUILD ONLY plus AWS reads: no upload, no
apply, no deploy, no edit of the real source map, no product source edit, no vendor call, no invoke.** State your base first:
`git rev-parse HEAD` before your first commit is `base_commit`; it contains IB-pr-455 (merged @0322231fc8).

**The state.** IB-pr-455 changed three members in the tree: `infra/aws/lambda/investor-reporting/ycharts/generate/submission.py`
(the closed set admits the optional boolean `commentary_requested`), `.../generate/acceptance.py` (the accepted record carries
it only when sent) and `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json`. Nothing is released. The
worker half that READS the member (`resident_worker.py`: `analysis_ready` only with a ticket id AND the member exactly true)
is merged and dormant. The order of release is SERVICE FIRST: this half, then the form. Before any release is designed, this
cell reads what a release would move.

**Functions.** `infra/aws/lambda/ci/lambda-source-map.json` pins each function's members, many through `staged_from` rows at
their own commits. IB-pr-455's worker named four entries that package `submission.py` or `acceptance.py`: `irpt-status`,
`irpt-commentary-draft-store-lambda`, `irpt-commentary-composition-read-lambda` and `irpt-ycharts-generate` (which stages the
whole `ycharts/generate` directory), and one unnamed entry near map line 4030 that packages the schema as
`contracts/AnalysisSubmissionRequest.schema.json`. That list is a lead, not a denominator. **Find them by subtraction**
(`source_map_census`): parse the whole map, count every function entry (`entries_scanned`), and place each as packaging or not
packaging any of the three members, by `files[]`, by `staged_from` (a file or a directory that contains one), and by
`source_dir`; state `how_found`. Every entry that packages one is a function of this read.

**For each function** (model and tools: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~285/`, the one-tree
rebuild of `irpt-ycharts-generate`, and its model `.../0.9.0_WK_IRPT_BCKEND~278/`: `make_candidate_map.py`, the census, the
closure limbs, `replay/`, the packets; copy and adapt into YOUR folder, leave theirs untouched):
1. **Live:** `lambda get-function-configuration` (through `.tools/aws`): `live_code_sha256`, `live_read_at_utc`; download the
   live package once (`get-function`, the link used once and never written) to scratch OUTSIDE the worktree; the rollback
   version: the S3 version of the function's artifact key (`artifact_s3_bucket` / `artifact_s3_key` from its map entry) whose
   content sha256 equals the live digest (`rollback_version_id`), or why none is found.
2. **Candidate map** (`candidate_source_map.json` in your folder; NEVER the real map): the real map with, in this function's
   entry, ONLY the rows that pin one of the three members re-pinned to `base_commit` with their sha256 recomputed from
   `git show`. This is the MINIMAL release: nothing else in the entry is touched.
3. **Build twice** with `BAU_SOURCE_MAP_OVERRIDE=<candidate> BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh
   investor-reporting <function>`, `TMPDIR` in scratch outside the worktree, in YOUR worktree only (the build checks pinned
   members out and restores them; run `git status --short` after each and report anything left changed). Byte-identical, or
   say why. `build:{outcome: BUILT|DID_NOT_BUILD, built_sha256, built_twice_identical, why}`. A function whose minimal
   candidate does not build is recorded `DID_NOT_BUILD` with the builder's refusal; do not pin anything else to make it pass.
4. **What moves** (`moved_members`): EVERY member whose bytes differ between the live package and the built one: `member`,
   `repo_path`, `live_sha`, `built_sha`, `owning_commits` (the commits between the member's live blob and its built blob on that
   path), `class` (`served` if it can alter any answer, record or call; `inert` only with a stated reason; unsure is `served`),
   `one_line`, and `is_one_of_the_three`. `changed_members_packaged`: for each of the three, `moves`, `not_packaged` or
   `packaged_and_does_not_move`. `riders`: the moved members that are NOT one of the three, in the same order. Note that one
   of the three may itself carry EARLIER unreleased commits (its `owning_commits` then hold more than IB-pr-455's): list every
   owning commit and say in `one_line` which are not IB-pr-455's. `added_members`, `removed_members`.
5. **`minimal_release`:** `ONLY_THE_CHANGED_MEMBERS_MOVE`, `RIDERS_MOVE_WITH_THEM` or `CANNOT_BE_BUILT_ALONE`.

**Entanglements** (`entanglements`, a list, one sentence each with its evidence): any HELD or unreleased work a release here
would carry or collide with. Known to the issuer: `irpt-ycharts-generate`'s one-tree rebuild (IB-pr-426, merged, NOT applied;
its apply waits on the CTO's word) and its census's statement that `acceptance.py` and `submission_service.py` must move
together or every submission raises a `TypeError` (read
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release5/GENERATE_MEMBER_CENSUS_AR-y-37_FOR_IRPT_BCKEND.md` and
the ~285 census): say whether that holds for each function at this base. Do not resolve an entanglement; state it.

**Readers of the accepted record, at YOUR base** (`readers_of_the_accepted_record_at_base`): IB-pr-453 counted 50 readers
(`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~309/IB149-1_commentary_asked_member.json`) at an OLDER base
that lacked the worker gate (row `IRPT_BCKEND-D2-S99`). Re-count at `base_commit` by the same subtraction (every file naming
`DynamoAcceptance`, `analysis#`, `.acceptance` or the record; each placed as reader, writer or neither): `readers` (each:
`reader`, `code_line`, `kind`, `function_or_surface` = the Lambda function or host process that runs it, and
`read_the_pair_makes_through_it` = the ONE read, named exactly, that would show after a release that this reader still reads a
record with and without the member: an existing route and what to look at, or an offline arm where no route reaches it),
`production_readers` (the count excluding tests), `difference_from_ib_pr_453` (readers added or gone, with why).

**Replay** (`replay.arms`, offline, in-memory fakes, live zip against built zip, in IB-pr-416's form): for each BUILT function
that accepts or reads a submission: a submission WITHOUT the member is accepted and recorded identically by live and built
(`submission_without_the_member: true`, verdict `identical`); a submission WITH it is refused by live and accepted by built
(`expected-diff`); a wrong-typed member is refused by both; a record without the member read through each reader the function
holds reads identically; one or more arms are a `negative_control`. An arm you cannot build is listed in `not_exercised` with
its reason, never relabelled.

**Packet** `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-456.md`, in IB-pr-416's form: per function the live and built digests, the rollback
version, EVERY moved member with its owning commits and served / inert line, the riders, Branch A (map entry landed first,
then build, then the module's Terraform path) and Branch B (redeploy the rollback version, re-read at apply), the after-read
proposed through each reader, the entanglements, what is NOT exercised. Do NOT write which ratified outcome each change
serves, and do NOT recommend an order of release among the functions: the issuer reads the ENDPOINT against your census.

**AMENDMENT 1 (2026-10-11 ~22:0xZ, issuer, on CTO msg 5904), before any spawn.** Two things go in the packet and in the json.
(a) **`after_read_with_no_vendor_call`** for `irpt-ycharts-generate`. The CTO's half on IB-pr-426
(`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/NEVER_WIDEN_IB_pr_426_YCHARTS_GENERATE_ONE_TREE_ENDPOINT_READ_AND_COO_HALF.md`
names it; find the CTO's half beside the commit 87d92b7c3b with `git show --stat 87d92b7c3b`) forbids an apply while the resident's
vendor session is signed out, because its first after-read was ONE VENDOR GENERATION. The vendor path is stopped, so that
condition blocks the function indefinitely. PROPOSE, from the code, the after-read that replaces it with NO vendor call: a
submission accepted and read back, WITH and WITHOUT the member (name the exact routes, what is read back and through which
reader), and an Opal-producer job if one is needed to exercise the function past acceptance (say whether one is needed and
what it reaches). Then list, by route and code path, WHAT OF THAT FUNCTION STAYS UNEXERCISED under that after-read
(`stays_unexercised`: every route or branch that only a vendor generation reaches, each with its file:line). Write it as text
the CTO rules on; do not say the old condition is lifted. Shape: `after_read_with_no_vendor_call:{steps:[{step, route_or_call,
what_is_read_back, through_which_reader}], opal_producer_job_needed (true/false/null), why, stays_unexercised:[{what,
code_line, why_only_a_vendor_generation_reaches_it}]}`.
(b) **The replay fact as a branch:** a replay of the same request id with a DIFFERENT `commentary_requested` (or with the member
added or dropped) is REFUSED `CHANGED_INPUTS_SAME_REQUEST_ID`, because `browser_sha256` is the digest of the validated
submission. Add a replay arm that shows it on the built package (`name` containing `same_request_id_different_member`,
verdict `expected-diff` against live where live refuses the member outright; say exactly what each side answers), and state
it in the packet as a branch of the release with what a caller sees.
IB152-1-AC3 does not grade (a) or (b) mechanically; the issuer reads them at the drain.

**Output:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~312/IB152-1_release_read.json` with
`{base_commit, source_map_census:{entries_scanned, entries_packaging_a_changed_member, how_found}, functions:[{function,
live_code_sha256, live_read_at_utc, rollback_version_id, rollback_version_absent_reason, build:{...}, moved_members:[...],
changed_members_packaged:{"submission.py":..., "acceptance.py":..., "AnalysisSubmissionRequest.schema.json":...}, riders:[...],
added_members, removed_members, minimal_release}], entanglements:[...], readers_of_the_accepted_record_at_base:{...},
replay:{arms:[...]}, not_exercised:[...], uploads_made:0, applies_made:0, real_source_map_edits:0, product_source_edits:0,
vendor_calls_made:0}`; your scripts; the candidate maps; the packet.

<criterion id="IB152-1-AC1" cell_refs="IB-pr-456"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r152/p152_cells.py" . IB152-1-AC1</invocation><expect>IB152-1-AC1 PASS</expect></criterion>
<criterion id="IB152-1-AC2" cell_refs="IB-pr-456"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r152/p152_cells.py" . IB152-1-AC2</invocation><expect>IB152-1-AC2 PASS</expect></criterion>
<criterion id="IB152-1-AC3" cell_refs="IB-pr-456"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r152/p152_cells.py" . IB152-1-AC3</invocation><expect>IB152-1-AC3 PASS</expect></criterion>

<expected_criteria>IB152-1-AC1, IB152-1-AC2, IB152-1-AC3</expected_criteria>

The checks grade the denominators, the arithmetic of riders against moved members, the replay's required arms and the five
zeros. Which functions build alone, what rides, and how many readers there are is UNMEASURED by the issuer.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. BUILD ONLY plus AWS reads through the `.tools/aws` shim.
- **Do not edit product source or the real source map.** If a minimal candidate does not build, or a closure limb reads above
  0, record it; do not pin another member to make it pass.
- **No vendor call**, no invoke of any function.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit
  `p152_cells.py`.
- **Client data:** counts, sha256 and reason codes only in committed files. Extracted packages stay OUTSIDE the worktree and
  are deleted file by file at the end; a package is data: never run or import anything from it except through the replay
  harness's own loader, as IB-pr-416's does.
- **Row ids** are `IRPT_BCKEND-D2-W312-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or
  `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~312" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~312@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~312 <0.9.0_WK_IRPT_BCKEND~312@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~312/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-456.commentary-requested-release-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 144 (round 152, workstream ~P), cell `IB-pr-456`.
<owned_cells>IB-pr-456</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB152-1-AC1, IB152-1-AC2, IB152-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~312/IRPT_BCKEND.TO-IB-pr-456.commentary-requested-release-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the map census and the functions found; per function the live and built digests,
the rollback version, the moved members, the riders and the minimal-release word; the entanglements; the readers at base and
the difference from IB-pr-453; the replay arms; what is not exercised; each criterion's last line; the proof checker's result;
`git status --short` after the builds; commit hashes; any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; this cell IS the blast-radius read of the release (every function packaging the changed members, every moved member, every reader of the accepted record); it builds in a worktree and uploads nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the reads are get-function, get-function-configuration and the artifact key's version reads the earlier build cells made.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p152_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~21:5xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no file); commit-gate clean. The four function names are IB-pr-455's worker's lead and are stated as a lead; the face orders a subtraction over the whole map. The issuer's own knowledge of the entanglement with IB-pr-426 (its COO half @e8a6b947bd, the CTO half @87d92b7c3b with conditions) is on the face. The reader census of IB-pr-453 is named stale (row IRPT_BCKEND-D2-S99) and re-counted here.
lane: the <paths> block IS the grant. WORLD: live function reads and package builds; nothing uploaded, applied or released. No apply order follows without a signed pair.
</preflight>
