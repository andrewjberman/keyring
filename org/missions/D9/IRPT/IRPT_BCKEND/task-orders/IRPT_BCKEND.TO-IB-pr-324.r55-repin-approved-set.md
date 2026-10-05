# TO IRPT_BCKEND.TO-IB-pr-324 -- apply the approved r55 re-pin set to lambda-source-map.json, with a BUILD_ONLY census and an import smoke per function (CTO batch 260)

<to_id>IRPT_BCKEND.TO-IB-pr-324</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~127</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-10-05</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>56</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULINGS batch 260 @7bd2946ccd (msg 105242), "r55 re-pin set APPROVED;
cut the one cell", with its conditions: an import smoke per function on the built bundle; the census attribution rule stands;
irpt-status stays 2.0.0_SA_COO~Y's deploy lane; the release returns as a plan for halves | **Decomp cell:** `IB-pr-324` (decomposition
section 49) | **outcome_ref:** FWD-8 | **depends_on:** IB-pr-323 (merged; BUILD_ONLY + release_census.py). The risk is WORLD because the
cell edits a deploy carrier under infra/. It uploads and deploys nothing.

---

## WORKER FACE

**The input.** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/REPIN_PLAN_R55.json`. Its `proposal` maps each function to
`repin` (member basenames to move), `held_rider` and `held_dependency` (members that must NOT move). `pairs` gives each
(function, member) its current pin and the commits since. The approved set is exactly the `repin` lists:
- 49f-reporting-read and status: four members each;
- export-render: schema, entry, loaders and served;
- directory-search and holdings: loaders.

Your worktree is `C:/Users/AndrewBerman/Desktop/wk-irpt-bckend-127`; run everything from its root. `MAP` =
`infra/aws/lambda/ci/lambda-source-map.json`.

1. **Re-pin.** For each (function, member) in a `repin` list, move that `staged_from` row's `pin` to the plan's `head` commit.
   Update every hash the row carries for the member (the build verifies `sha256` per staged member; recompute it from
   `git show <head>:<repo_path>` exactly as `build-and-upload.sh`'s staging step does). Touch no other row, and no pin in
   `held_rider` or `held_dependency`.
2. **Census + import smoke** per function with a repin, written to
   `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~127/R56_REPIN_CENSUS.json` as
   `{"functions": {fn: {...}}}`:
   - Build with `BUILD_ONLY=1 bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting <fn>`. It never uploads.
   - Fetch live with `python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~126/release_census.py fetch-live <fn>`.
   - Census both with that tool. For every added, removed or changed member, record `name`, `status` and `order`: the order id
     whose commits produced the change (IB-pr-317, -320, -321 or -322; read `git log <old pin>..<head> -- <path>`).
     Unattributed members go in `riders`.
   - **Import smoke:** unzip the BUILD_ONLY bundle to a temp dir, and in a fresh subprocess with that dir first on sys.path,
     `import` every top-level `.py` module. Record `import_smoke: {modules: N, import_errors: [{module, error}]}`. Only
     ImportError/ModuleNotFoundError count. Record other import-time exceptions under `other_errors` without failing.
   - Delete the temp zips and dirs after each function, because disk is tight.
3. If a function shows a rider or an import error, do NOT widen the set. Revert that function's pins to base, keep it in the
   census with its finding, and file a row naming it.

<criterion id="IB56-1-AC1" cell_refs="IB-pr-324"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r56/p56_repin.py" . IB56-1-AC1</invocation><expect>IB56-1-AC1 PASS</expect></criterion>
`IB56-1-AC1` -- every approved pin is moved to HEAD content, and every other pin is unchanged. Base: FAIL.

<criterion id="IB56-1-AC2" cell_refs="IB-pr-324"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r56/p56_repin.py" . IB56-1-AC2</invocation><expect>IB56-1-AC2 PASS</expect></criterion>
`IB56-1-AC2` -- the census attributes every changed member to IB-pr-317/320/321/322, with no riders. Base: FAIL.

<criterion id="IB56-1-AC3" cell_refs="IB-pr-324"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r56/p56_repin.py" . IB56-1-AC3</invocation><expect>IB56-1-AC3 PASS</expect></criterion>
`IB56-1-AC3` -- every function's bundle imports with no ImportError. Base: FAIL.

<expected_criteria>IB56-1-AC1,IB56-1-AC2,IB56-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below.
- **AWS:** `get_function` reads only (fetch-live). NO upload, NO terraform, NO deploy.
- **Refusal clause.** A pin outside the approved set, or any upload, is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~127/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-324.r55-repin-approved-set.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 49 (round 56, workstream ~P), cell `IB-pr-324`.
<owned_cells>IB-pr-324</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB56-1-AC1, IB56-1-AC2, IB56-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~127/IRPT_BCKEND.TO-IB-pr-324.r55-repin-approved-set.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB56-1-AC1,IB56-1-AC2,IB56-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, the pins moved per function, the census per
function (changed members and their orders), the import-smoke counts, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- staged_from pins in the source map for 5 functions; 0 served bytes move (no upload or deploy); the release returns as a plan for halves.
comp-iam: DECLARED-NOT-APPLICABLE -- no role changes.
comp-routes: DECLARED-NOT-APPLICABLE -- no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- IB56-1-AC1 base FAIL (no pin moved), IB56-1-AC2 base FAIL (no census), IB56-1-AC3 base FAIL (no smoke), dry-run at base fc30e2ca85 2026-10-05 ~12:1xZ.
lane: the <paths> block IS the grant.
</preflight>
