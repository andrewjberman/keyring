# TO IRPT_ANLREQ.TO-AR-y-295.fwd1-consolidated-release-census -- READ the FWD-1 consolidated release: which served packages carry which changed members, the live start state of each, and the order the legs must move in

<to_id>IRPT_ANLREQ.TO-AR-y-295</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~113</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>28</round>
<workstream>YS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-295` (`decompositions/IRPT_ANLREQ_DECOMP_R28A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~113`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-113` (branch `wk-IRPT_ANLREQ-113`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~113 <0.9.0_WK_IRPT_ANLREQ~113@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W113-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-295`, inlined) -- READ. Nothing is changed, built, uploaded, applied or called except live AWS get/describe/list reads of the named resources.

*The FWD-1 cells drained since the last releases are, on the trunk: `AR-y-245` (the upload's price date defaults to the previous trading day; `intake/portfolio.py`, `intake/uploads.py`, the calendar member `lib/trading_calendar.py` if the package carries it), `AR-y-280` (the ticket service SUBMIT-FORM takes an analysis request), `AR-y-281` (a client-human's own-firm LIST), `AR-y-284` (the ticket service PACKAGE records the request id once), `AR-y-285` (the packager sends the request id; `ycharts/research/opal_packager.py`), `AR-y-291` (the registry identity port; `ycharts/generate/resident_worker.py` and `intake/security_resolution.py`), `AR-y-292` (the yfinance history checker; `intake/yfinance_check.py`, not yet wired by the resident), `AR-y-293` (the KEPT state and its three words; `intake/portfolio.py`, `intake/security_resolution.py`, `intake/uploads.py` and the `ops/status.py` words table), and the folded template reader r19.3 (`intake/template_reader.py`, commit `55d1755d39`). The CTO folded r19.3 into one FWD-1 consolidated release (msg 7264). Before the issuer writes the never-widen pair and cuts the build and apply orders, the release must be COUNTED: each changed member, every served package that carries it (N writers), the live start state of each package, and the order the legs must move in. Known so far (read, do not trust): the ticket service is the Lambda `opal-ticket-api` (`infra/aws/lambda/ticket_center`); the status envelope is `irpt-status` (`infra/aws/lambda/investor-reporting/ops`); the packager runs in the resident (`reports/resident_installed.py` :326-341, :425-433) and is NOT in `lambda-source-map.json`; release 19 and 21 moved the reader in the resident and in `irpt-ycharts-generate`; row `IRPT_ANLREQ-D2-W109-S2` (ARMED, the issuer's): the packager released before the ticket service's `AR-y-284` leg gets a 400 on every attach.*

1. **Read first:** `infra/aws/lambda/ci/lambda-source-map.json` (every function entry that carries any of the members above: `source_dir`, `files`, `staged_from` with each member's `pin`, `packaged_as`, `sha256`, `artifact_sha256`, `deployed_code_sha256`), the release-21 pair `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release21/NEVER_WIDEN_PAIR_ANLREQ_RELEASE21_READER_R193_TWO_LEG.md` (its sections 1 to 3 are the shape the issuer will write for this release), the release census records `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/UPLOAD_DOOR_RELEASE_CENSUS.json` and `.../0.9.0_WK_IRPT_ANLREQ~5*/r19/YCHARTS_GENERATE_RELEASE_CENSUS.json` (find the second by name with `Glob`), and the records of the cells above: `.../deliverables/0.9.0_WK_IRPT_ANLREQ~<n>/r2*/*.json` for `AR-y-245`, `-280`, `-281`, `-284`, `-285`, `-291`, `-292`, `-293` (find each cell's record folder from its order file under `org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/`; each record's `release_needs` member is the author's own list: copy it, do not trust it).
2. **The changed members.** For each served package that could carry a FWD-1 member (the ticket service, `irpt-ycharts-generate`, the upload door and intake poller packages in the map, `irpt-status`, and the resident), list the members that differ between the commit or bytes the package was LAST BUILT from and the trunk HEAD: `git diff --name-only <last-built pin>..HEAD -- <the package's source folder>` for each pin the map names (state the pin, the diff command and the number of paths in its output, printed beside the list; a zero is a count, not an absence). Restrict the release list to the members the FWD-1 cells above changed; every OTHER differing member is listed apart as `unrelated_drift` with its count and NOT proposed to move (the release moves what the cells changed and what they import, nothing else; if a changed member imports a name another member lacks, record the minimum extra member and say why: a finding for the CTO, never a silent widening).
3. **Writers.** For every member in the release list, name every served package that carries it (the Lambdas by map entry, the resident by its builder's rule) and print N. A member carried by one package moves in one leg; a member carried by several moves in each, and the record says whether those legs must be one window.
4. **The live start state** of every package that will move, from live READ-ONLY calls only (`aws lambda get-function-configuration --function-name <name>`: `CodeSha256`, `CodeSize`, `LastModified`; `aws s3api list-object-versions --prefix <key>` for the artifact key: latest version and the count of versions; use the `.tools/aws` shim). Print each result beside the map's `deployed_code_sha256`; a mismatch is a finding (the map is stale or someone released). For the resident, read the host's installed root name from the last release record (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release21/` and the ledger entries it cites) and say it was NOT read live (the applier's step 0 reads it).
5. **Order and gates.** From the cells' records and the rows `W109-S2`, `W108-S4`, `W108-S5`, `W107-S3`, `W106-S2`, state for each pair of legs whether a mixed state (one leg moved, the other not) is safe in each direction, with the evidence (a test, a code line, or `INFERRED`). The known constraint: the packager (resident) must follow the ticket service's `AR-y-284` leg. Also state: which `irpt-status` words the new finding codes need and in which leg; what `AR-y-245`'s calendar member needs (is `lib/trading_calendar.py` in each package that carries `intake/portfolio.py`?); whether `AR-y-292`'s checker is imported by anything yet (if not, shipping it is dead code until the resident wires it: say which seat owns the wiring and that it is not in this release).
6. **The legs.** Propose the legs: for each, the package, the members that move, the builder and how it is run without uploading (`BUILD_ONLY=1` for the Lambda builder; the resident's recipe by the release-19/21 method), the OWNING applier lane (read the round-14/15 compile and the release records: name what you read, never guess), the ledger slug shape, and the rollback artifact that exists today (the previous version id or tarball, with its hash read from a record or `INFERRED`).
7. **Write `r28/FWD1_RELEASE_CENSUS.json`:** `cells` (the eight cell ids with the commit that drained each and the record path read), `packages` (objects: `name`, `kind` (lambda or resident), `source_folder`, `last_built_pin`, `diff_command`, `diff_path_count`, `members_in_release` (member, old blob sha256 or pin, head blob sha256, cells that changed it), `unrelated_drift` (count and a list of at most 10), `live` (CodeSha256, CodeSize, LastModified, artifact key latest version, map `deployed_code_sha256`, `matches_map` true/false/null), `missing_imports`), `member_writers` (object: member -> list of packages, with `n`), `order_constraints` (objects: `before`, `after`, `why`, `evidence`), `status_words_leg`, `calendar_member`, `checker_wiring`, `legs` (objects: `leg`, `package`, `members`, `builder`, `applier_lane`, `ledger_slug`, `rollback`), `claim`, `not_read`.
8. **In your report:** the legs in order with the members each moves, every N greater than 1, every finding (stale map, missing import, mismatch of the live state), and what only the applier's step 0 can read.

### ACCEPTANCE

<criterion id="AR295-y-AC1" cell_refs="AR-y-295"><invocation>python C:/dev/wk-irpt-anlreq-113/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y295-census --root C:/dev/wk-irpt-anlreq-113</invocation><expect>Y295-CENSUS-OK</expect></criterion>
`AR295-y-AC1`: the record names the eight FWD-1 cells with their drain commits, every package that could carry a changed member with its diff command and path count, the changed members with their writers (N printed), the live start state of every Lambda that will move read beside the map, the ordering constraints with evidence, and the proposed legs with applier lane and rollback.

<criterion id="AR295-y-AC2J" cell_refs="AR-y-295" judgment="true"/>
`AR295-y-AC2J` (judgment, graded at L9, never by you): the release list is exactly what the cells changed and what they import (nothing else is proposed to move, the unrelated drift is listed apart), every served package that carries a changed member is named, the live states were read and compared with the map, the order constraints are evidenced or marked INFERRED, and nothing was changed, built, uploaded or applied.

<expected_criteria>AR295-y-AC1 AR295-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~113/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R28A_Y.md</decomp_doc>
<owned_cells>AR-y-295</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~113/IRPT_ANLREQ.TO-AR-y-295.fwd1-consolidated-release-census.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-295`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR295-y-AC1,AR295-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- READ-only live AWS get/describe/list calls on the named Lambdas and artifact keys; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the release-19 and release-21 census records and the cells' own `release_needs` against the cell; the lens: a package that carries a changed member and is missing from the list, a member listed as moving that no cell changed, a map entry taken for the live state. The order requires every package named with its diff command and path count, the live reads printed beside the map, and the unrelated drift listed apart. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut for the FWD-1 consolidated release (the CTO's msg 7264 folded r19.3 into it; the cells AR-y-245, -280, -281, -284, -285, -291, -292, -293 are drained) as workstream `YS` round 28. The result feeds the never-widen pair, the build cells and the apply orders. Base: `AR295-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
