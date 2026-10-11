# TO IRPT_BCKEND.TO-IB-pr-426 -- irpt-ycharts-generate rebuilt from ONE merged commit: candidate map, a census of every member that moves against live, replay, never-widen packet (BUILD ONLY)

<to_id>IRPT_BCKEND.TO-IB-pr-426</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~285</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>124</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msgs 4621 and 4657 (row IRPT_ANLREQ-D2-S39; the issuer's live-bytes read `deliverables/2.0.0_SA_COO~P2/checks/r122/LIVE_BYTES_irpt-ycharts-generate_READ_20261011.md` @2cef0485fd) | **Decomp cell:** `IB-pr-426` (decomposition section 117) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-285/` (bash `/c/dev/wk-irpt-bckend-285`). Work only there. **BUILD ONLY plus AWS reads: no upload, apply
or deploy; no product source edit; no vendor call.**

**The state.** Live `irpt-ycharts-generate` is `tdpterTMfJlWXjnoAQCwil+wN/Jf8Q/yLjGxTk7yUkk=` (release 6b, 2026-10-09, pin `66207bce7d`).
Read by the issuer: all 104 members of the live package match a commit; 88 are staged from 12 different pins in
`infra/aws/lambda/ci/lambda-source-map.json`; 23 staged members and 3 native ones (`acceptance.py`, `durable_job.py`,
`submission_service.py`) are older than the tree at HEAD. The CTO ruled one re-pin of the WHOLE entry to ONE merged commit, a fresh
build, and a census of everything that moves.

**Build:**
1. **One pin.** The pin is the commit your worktree was cut from (`git rev-parse HEAD` before your first commit). It contains the
   restoration of `performance/` (`c267b71edb`). EVERY member of the function, staged or native, is taken from that one commit.
2. **Candidate map.** Do NOT edit the real source map. Write `candidate_source_map.json` in your deliverables folder: the real map
   with ONLY the `irpt-ycharts-generate` entry changed, every `staged_from` row re-pinned to the one pin with its sha256 recomputed
   from `git show`. Model: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~278/` (`make_candidate_map.py`,
   `make_census_416.py`, `signature_closure_attr.py`, `method_call_limb_416.py`, `replay/`, and its packet
   `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-416.md`). Copy and adapt; leave that folder untouched.
3. **Build twice** with `BAU_SOURCE_MAP_OVERRIDE=<candidate> BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh
   investor-reporting irpt-ycharts-generate`, with `TMPDIR` set to scratch outside the worktree. Byte-identical or stop. The name,
   attribute and method closure limbs each read 0 on the built zip. Run the build in YOUR worktree, never the shared one: the build
   checks pinned members out and restores them, and a failed restore there prints only a WARN (row IRPT_BCKEND-D2-S72). After each
   build run `git status --short` and report anything it left changed.
4. **Census** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~285/IB124-1_generate_census.json`:
   `{function, pin, built_sha256, built_twice_identical, live_before, rollback_version, members_live, members_built,
   member_count_note, built_signature_mismatched, built_attribute_mismatched, built_method_mismatched,
   moved_members:[{member, repo_path, live_sha, built_sha, old_pin, owning_commits:[...], class:"served"|"inert", one_line}],
   added_members:[...], removed_members:[...]}`.
   - `live_before` is the live CodeSha256 you read; `rollback_version` is the S3 version of
     `s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip` whose `content-sha256` equals it.
   - `moved_members` is EVERY member whose bytes differ between the live package and the built one. `owning_commits` are the commits
     between the member's live blob and its built blob on that path.
   - `class`: `served` if the change can alter any answer, record or call the function makes (a handler, a code path a route
     reaches, a schema the function validates or writes, a registry or policy file it reads at runtime); `inert` only if you can say
     why it cannot (for example a module with no call site in this package, a comment-only or test-only change). `one_line` gives the
     reason in one sentence. When unsure, it is `served`.
   - `acceptance.py` and `submission_service.py` must BOTH be in `moved_members`: read
     `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release5/GENERATE_MEMBER_CENSUS_AR-y-37_FOR_IRPT_BCKEND.md`; one
     without the other raises a `TypeError` on every submission.
5. **Replay** `IB124-1_replay.json`, `{arms:[{name, verdict, negative_control, members:[...], detail}]}`: live zip against built zip,
   offline, in-memory fakes, every route of the function plus the binding cases in IB-pr-416's form; every verdict `identical` or
   `expected-diff`; at least one negative control; every `served` member is named in the `members` list of at least one arm that
   exercises it. An arm you cannot build for a served member is a row and a stop, not an `inert` relabel.
6. **Packet** `NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-426.md`, in IB-pr-416's form: live and built sha256; the rollback version; EVERY moved
   member with its owning commits and its served / inert line; Branch A (source-map entry landed first, then build, then the
   module's Terraform path) and Branch B (redeploy the rollback version, re-read at apply); an after-read proposed for each served
   change (for the acceptance pair, the one `2.0.0_SA_COO~Y2`'s census suggests); the function's role, routes, layers and
   environment as unchanged, read from Terraform; what is NOT exercised. Do NOT write which ratified outcome each change serves: the
   issuer reads the ENDPOINT against your census before any half is written.
   Also state for the record step that the real map's `artifact_sha256`, `deployed_code_sha256`, `last_deployed_at` and
   `deploy_ledger` for this entry are one release behind (they name the build release 6b replaced).

<criterion id="IB124-1-AC1" cell_refs="IB-pr-426"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r124/p124_cells.py" . IB124-1-AC1</invocation><expect>IB124-1-AC1 PASS</expect></criterion>
<criterion id="IB124-1-AC2" cell_refs="IB-pr-426"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r124/p124_cells.py" . IB124-1-AC2</invocation><expect>IB124-1-AC2 PASS</expect></criterion>
<criterion id="IB124-1-AC3" cell_refs="IB-pr-426"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r124/p124_cells.py" . IB124-1-AC3</invocation><expect>IB124-1-AC3 PASS</expect></criterion>

<expected_criteria>IB124-1-AC1, IB124-1-AC2, IB124-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. BUILD ONLY plus AWS reads through the `.tools/aws` shim.
- **Do not edit product source or the real source map.** If the one-commit tree does not build, or a closure limb reads above 0,
  stop, file a row and report; do not pin a member back to make it pass.
- **No vendor call** (the function refuses one without a per-use sentence in its environment; do not supply it).
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row and report. Never weaken a check; do not edit
  `p124_cells.py`.
- **Client data:** counts, sha256 and reason codes only in committed files. Extracted zips stay OUTSIDE the worktree and are deleted
  file by file at the end; report what remains.
- **Row ids** are `IRPT_BCKEND-D2-W285-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; check the id is free just before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~285" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~285@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~285 <0.9.0_WK_IRPT_BCKEND~285@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~285/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-426.ycharts-generate-one-tree-rebuild.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 117 (round 124, workstream ~P), cell `IB-pr-426`.
<owned_cells>IB-pr-426</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB124-1-AC1, IB124-1-AC2, IB124-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~285/IRPT_BCKEND.TO-IB-pr-426.ycharts-generate-one-tree-rebuild.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the pin; the built sha256 and the rollback version; the count of moved members with the served /
inert split; each served member with its one line; the closure limb counts; the replay's arm count and any expected-diff arms; what
`git status --short` read after each build; each criterion's last line; the proof checker's result; any row ids; what scratch remains.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; a build-only cell, nothing uploaded or applied; the cell's own census is the blast read of the later release (every member that moves against live), graded by IB124-1-AC1.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the packet states the role as unchanged from Terraform.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p124_cells.py dry-run at base box/dell2 on dell2 2026-10-11 ~10:5xZ: AC1 FAIL, AC2 FAIL, AC3 FAIL (no census); commit-gate clean.
lane: the <paths> block IS the grant; IRPT_BCKEND releases irpt-ycharts-generate by CTO ruling (msg 4621).
</preflight>
