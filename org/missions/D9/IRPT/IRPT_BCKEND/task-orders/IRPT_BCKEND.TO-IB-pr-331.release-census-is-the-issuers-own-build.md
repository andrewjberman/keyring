# TO IRPT_BCKEND.TO-IB-pr-331 -- the release census is derived by the issuer's own build against live, never from a worker-written census (row S337)

<to_id>IRPT_BCKEND.TO-IB-pr-331</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~134</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>61</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** laptop (project placement; seat on dell2) | **Ordered by:** `1.0.0_SA_CTO~DELL2` round analysis rounds 47-60,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_47_60_20261007.md` @e363a194ed section 5, item E-P3 |
**Risk:** declared at the L6 floor its `<paths>` imply (an `infra/` path floors at WORLD, spine v3.19); the analysis's own class for E-P3 is in its section 5 | **Decomp cell:** `IB-pr-331` (decomposition section 54) | **outcome_ref:** row S337 census half (release tooling) | **depends_on:** none.

---

## WORKER FACE

**The defect (row IRPT_BCKEND-S337).** IB-pr-324's census (a worker-written `R56_REPIN_CENSUS.json`) reported
`irpt-ycharts-generate` with 4 changed members; the issuer's own re-census at merged HEAD f36a8cdefd (BUILD_ONLY vs the live zip from
`get-function`) read **19** changed (the 4 re-pinned members plus 15 under fixtures/templates). The rule: a release census is re-derived
by a build at the pin against the live zip, never read from a worker's file. Prior art to read (not to import): the IB-pr-323 tool
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~126/release_census.py`.

**What you build** (your worktree is `C:/dev/wk-irpt-bckend-134`; run everything from its root):

1. **`infra/aws/lambda/ci/release-census.py`** (new): `python infra/aws/lambda/ci/release-census.py <function> --pin <commit>` builds the function's zip as the builder
   would at `<pin>` (BUILD_ONLY semantics: the source map at the pin, `files[]` from the source_dir at the pin, `staged_from` members by
   their pins), fetches the LIVE zip by `aws lambda get-function --function-name <function>` `Code.Location` (read-only), and diffs member
   by member (name + sha256). It prints one line per changed/added/removed member and ends with `changed_members=<N>`. It must finish in
   under 120 s: materialize members with `git show <pin>:<path>` into a temp dir rather than checking out a worktree. It reads no
   `*CENSUS*.json` file. Run it from `.tools/aws` or `aws` on PATH (the `.tools/aws` shim exists in this repo).
2. **`infra/aws/lambda/ci/tests/test_release_census.py`** (new, offline, no AWS): build a fixture zip pair and show the diff logic reports a changed
   member, an added member and a **planted extra file** (the word `planted` appears in that test's name).
3. Run it once on `irpt-ycharts-generate --pin f36a8cdefd` and put the full output in your deliverables folder. The issuer's figure is
   19; if yours differs, report both and the members that differ, and file a row (do not tune the tool to the number).

<criterion id="IB61-3-AC1" cell_refs="IB-pr-331"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-3-AC1</invocation><expect>IB61-3-AC1 PASS</expect></criterion>
`IB61-3-AC1` -- the offline tests pass, including a planted extra file, and the tool names no census .json. Base: FAIL (no tool).

<criterion id="IB61-3-AC2" cell_refs="IB-pr-331"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-3-AC2</invocation><expect>IB61-3-AC2 PASS</expect></criterion>
`IB61-3-AC2` -- release-census.py irpt-ycharts-generate --pin f36a8cdefd prints changed_members=19. Base: FAIL (no tool).

<criterion id="IB61-G-134" cell_refs="IB-pr-331"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r61/p61_cells.py" . IB61-G-134</invocation><expect>IB61-G-134 PASS</expect></criterion>
`IB61-G-134` -- a GUARD: your commits touch only your grant. Base: PASS.

<expected_criteria>IB61-3-AC1,IB61-3-AC2,IB61-G-134</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, and nothing else.
- **HOLD (laptop `1.0.0_SA_CTO` ruling A, 2026-10-07 08:5xZ):** nothing you produce, land or grade may carry a date before 2024-01-01
  through `lib/trading_calendar.py` on this box. Use 2026 dates in every test and fixture.
- **No vendor call, ever.** No call off Opal infrastructure.
- **A test that fails for a reason you did not cause** is a surprise row and a stop on that criterion, never an edit to another test.
- Every invocation finishes inside 120 s; scope it so it does.
- **Refusal clause.** Any AWS call other than read-only `lambda get-function` / `get-function-configuration`, or an edit to the builder or the map, is a defect: stop and file a row.

<paths>
infra/aws/lambda/ci/release-census.py
infra/aws/lambda/ci/tests/test_release_census.py
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~134/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-331.release-census-is-the-issuers-own-build.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 54 (round 61, workstream ~P), cell `IB-pr-331`.
<owned_cells>IB-pr-331</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB61-3-AC1, IB61-3-AC2, IB61-G-134. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~134/IRPT_BCKEND.TO-IB-pr-331.release-census-is-the-issuers-own-build.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IB61-3-AC1,IB61-3-AC2,IB61-G-134` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message gives the commit hashes, each criterion's last line, any suite's last line, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- nothing is deployed by this order; any release is the issuer's after the drain.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS permission is added.
comp-routes: DECLARED-NOT-APPLICABLE -- no route or CloudFront behaviour changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- every criterion dry-run at base 6e462d3499 2026-10-07 ~09:0xZ: build checks FAIL, guards PASS (p61_cells.py).
lane: the <paths> block IS the grant.
</preflight>
