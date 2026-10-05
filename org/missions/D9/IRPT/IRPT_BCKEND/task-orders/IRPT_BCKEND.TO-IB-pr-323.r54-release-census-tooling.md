# TO IRPT_BCKEND.TO-IB-pr-323 -- the r54 release census tooling: BUILD_ONLY for build-and-upload.sh, and a member-by-member census of a built zip against the live bundle (CTO half condition 2)

<to_id>IRPT_BCKEND.TO-IB-pr-323</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~126</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>54</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO's CTO half for release r54
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_IRPT_BCKEND_RELEASE_R54_20261005.md` @f342ba6664, msg 105191), condition 2:
"Per-function census of built zip vs live bundle, every changed member attributed to 317, 320, 321 or 322. An unattributed change is
a rider and drops the function." | **Decomp cell:** `IB-pr-323` (decomposition section 48) | **outcome_ref:** FWD-8 |
**depends_on:** none. The risk is WORLD because the cell edits a script under infra/. The cell makes NO S3 upload and deploys nothing.

---

## WORKER FACE

**Why.** `infra/aws/lambda/ci/build-and-upload.sh` builds a deterministic zip at `${TMPDIR:-/tmp}/lambda-artifact-<fn>.zip`
(`:350`, zip built near `:563`). It then always uploads it to the artifact bucket and updates `lambda-source-map.json`. The release
needs the zip BEFORE any upload, so a rider can drop a function without touching S3.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-126`; run everything from its root.

1. **`BUILD_ONLY=1`** in `build-and-upload.sh`:
   - every pre-build gate still runs, and the zip is built exactly as now;
   - then the script prints `BUILD_ONLY: <zip path> sha256=<base64>` and skips the upload, the head-object verify and the
     source-map update;
   - the zip is kept, and the script exits 0;
   - without `BUILD_ONLY`, nothing changes.
2. **`infra/aws/lambda/ci/tests/test_build_only.sh`**, modeled on `test_sha_handoff.sh`. Under `BUILD_ONLY=1` with a stub `aws` on
   PATH that fails loudly if called, it shows that:
   - the zip exists;
   - no aws call was made;
   - `lambda-source-map.json` is byte-identical before and after.

   Use a tiny fixture pipeline, or a real small function, so no real upload is reachable. It prints `PASS` lines and exits 0.
3. **`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~126/release_census.py`**:
   - `census <built.zip> <live.zip>` lists every member as `added`, `removed`, `changed` (sha256 differs) or unchanged;
   - each added, removed or changed member is `attributed` to an order id by a rules file (path pattern to order id) passed with
     `--rules <json>`, or else marked `RIDER`;
   - it writes JSON (`members`, `counts`, `riders`) and exits 1 when any RIDER exists;
   - `fetch-live <function>` downloads the live bundle with boto3 `lambda.get_function(...)['Code']['Location']`, a read only, to
     a path you name;
   - it never prints a URL with a signature in it.
4. **`.../~126/tests/test_release_census.py`**: at least 5 offline pytest tests on synthetic zips:
   - added;
   - removed;
   - changed;
   - an attributed change passes (exit 0);
   - an unattributed change is a RIDER (exit 1).

   The words `RIDER`, `attributed`, `added`, `removed` and `changed` appear in the file.

<criterion id="IB54-1-AC1" cell_refs="IB-pr-323"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r54/p54_release_census.py" . IB54-1-AC1</invocation><expect>IB54-1-AC1 PASS</expect></criterion>
`IB54-1-AC1` -- `test_build_only.sh` exits 0 with at least 3 PASS lines (zip built, no aws call, source map unchanged). Base: FAIL.

<criterion id="IB54-1-AC2" cell_refs="IB-pr-323"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r54/p54_release_census.py" . IB54-1-AC2</invocation><expect>IB54-1-AC2 PASS</expect></criterion>
`IB54-1-AC2` -- the census tests pass, at least 5, naming RIDER, attributed, added, removed and changed. Base: FAIL.

<criterion id="IB54-1-AC3" cell_refs="IB-pr-323"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r54/p54_release_census.py" . IB54-1-AC3</invocation><expect>IB54-1-AC3 PASS</expect></criterion>
`IB54-1-AC3` -- a GUARD: your commits touch only the grant, and never terraform or `lambda-source-map.json`. Base: PASS.

<expected_criteria>IB54-1-AC1,IB54-1-AC2,IB54-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** NO S3 upload, no Lambda update, no terraform. `fetch-live` (a `get_function` read) may be exercised once on one function
  to prove it works; the census tests themselves are offline.
- **Refusal clause.** Any upload or source-map change is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/build-and-upload.sh
infra/aws/lambda/ci/tests/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~126/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-323.r54-release-census-tooling.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 48 (round 54, workstream ~P), cell `IB-pr-323`.
<owned_cells>IB-pr-323</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB54-1-AC1, IB54-1-AC2, IB54-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~126/IRPT_BCKEND.TO-IB-pr-323.r54-release-census-tooling.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB54-1-AC1,IB54-1-AC2,IB54-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the BUILD_ONLY output line format, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the build script gains an opt-in BUILD_ONLY branch; the default path is unchanged; 0 served bytes move; no upload.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes; fetch-live is a get_function read.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB54-1-AC1 base FAIL (no test), IB54-1-AC2 base FAIL (no census tests), IB54-1-AC3 base PASS (guard), dry-run at base f58728dde1 2026-10-05 ~06:4xZ.
lane: the <paths> block IS the grant.
</preflight>
