# TO IRPT_BCKEND.TO-IB-pr-381 -- count every writer of the served directory; make the runner carry source-removed entries; read the previous state from the served directory; package IB-pr-380 + IB-pr-381 as ONE release

<to_id>IRPT_BCKEND.TO-IB-pr-381</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~189</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>open</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>93</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** CTO ruling msg 1988 on rows D2-W188-S1, S2, S3 | **Decomp cell:** `IB-pr-381`
(decomposition section 86) | **outcome_ref:** FWD-7 (directory READY at all 3 firms) | **depends_on:** IB-pr-380 (complete, P 8953eccfca,
drained @3ff1ed35fa). **Deadline:** the ONE release (380 + 381) is live before cottonwood goes OVER_AGE on 2026-10-12, so in practice by
Friday 2026-10-09's close.

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-irpt-bckend-189` (branch `wk-IRPT_BCKEND-189`; it already carries IB-pr-380's code). Work, build and commit
only there. `L` = `infra/aws/lambda/investor-reporting`, `G` = `data/assets/scripts/gold/investor_reporting`. Paths below are relative to
the worktree. Keep scratch outside the worktree.

**What exists.** IB-pr-380 (P `8953eccfca`) put the CTO's rule into `L/directory/refresh.py`: an entry absent from both the build and the
source snapshot is carried as TERMINATED (date in `termination.effective_date` plus a `capability_facts` marker `source_removed_on=...`).
An entry in the source but missing from the build stays REFRESH_FAILED. Its rows (in
`org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`) name what still blocks the outcome:
- **D2-W188-S1:** `G/directory_runner.py` emits no `source_client_ids`, and it writes `directory.json` and `latest.json`
  (`land()`, ~line 872). Without it, the rule is fail-closed and no reader sees a carried entry.
- **D2-W188-S2:** inflection's last READY manifest (2026-09-25) is outside the 10-trading-day previous-state window, so a fire on or after
  2026-10-09 goes READY with a false 294 additions and `terminated_count` 0.
- **D2-W188-S3:** no contract change. The CTO accepted `effective_date` + the `capability_facts` marker.

**Your cell, in this order. AWS READS and BUILD_ONLY only: no upload, apply or deploy.**
1. **(a) FIRST: count the writers.** Find every writer of `investor-reporting/directory/<as_of>/directory.json` and
   `investor-reporting/directory/latest.json` in the firm buckets: code paths (runner, refresh, any other), the schedules and functions
   that run them, and the live evidence (object versions and LastModified of latest.json per firm, matched to runs).
   - Explain how inflection's served directory reads as_of 2026-10-08 after the 2026-10-08 refresh returned REFRESH_FAILED.
   - Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~189/IB93-1_directory_writers.json`:
     `{writer_count, writers: [{name, kind, evidence}], served_inflection_1008_explained}`.
   - If a writer exists that this order cannot make honour the rule (outside `<paths>`), STOP after (a): file a row naming it, and
     report.
2. **(b) The runner** emits `source_client_ids` (the keys the source snapshot holds, in the same key space as `ids.client_id` /
   `ids.relationship_id`). It lands the previous served directory's source-removed entries as TERMINATED, exactly as refresh.py's rule
   decides, so the landed `directory.json` carries them.
   - Tests in `G/tests/test_directory_runner_terminated.py`, with names containing `terminated_carry_forward` (at least 2):
     - an entry absent from both the build and the source is landed TERMINATED;
     - an entry in the source but missing from the build is NOT carried.
   - The whole `G/tests` suite passes.
3. **(c) The previous state is the served directory** (latest.json and its directory.json), not a READY manifest inside the walk window.
   - Tests in `L/directory/tests/test_refresh_previous_state_served.py`, names containing `previous_state_served` (at least 2):
     - a fire whose last READY manifest is outside the window still compares against the served directory, so no false additions;
     - with no served directory, it falls back to today's behaviour.
   - The whole `L/directory/tests` suite passes.
4. **Real-case replay** through the BUILT release (offline: built runner + built refresh, real inputs read from AWS), written to
   `.../0.9.0_WK_IRPT_BCKEND~189/IB93-1_release_replay.json` as `{pin, firms: {inflection: {built: {reason_code, terminated_count,
   carried_in_landed}, live: {reason_code}, fire_20261009: {previous_found, false_additions}}, cottonwood: {built: {...}, live: {...}}}}`.
   Opaque ids only.
5. **Package the ONE release.** Commit the code; that commit is pin P. Then:
   - Run `python infra/aws/lambda/ci/release-census.py irpt-directory-refresh --pin P`, plus any other function whose members changed.
   - For the runner bundle (`investor-reporting.tar.gz`, `irpt_runner_bundle_uri` in
     `infra/aws/terraform/investor-reporting/directory/schedule.tf`), name its build and deploy path. The deploy is the applier's.
   - BUILD_ONLY each from a clean tree. Record pins, members and built sha256s in
     `.../0.9.0_WK_IRPT_BCKEND~189/IB93-1_release_census.json`.
6. **Packet** `.../0.9.0_WK_IRPT_BCKEND~189/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-380_381.md`, modelled on
   `deliverables/0.9.0_WK_IRPT_BCKEND~178/NEVER_WIDEN_SIGNOFF_PACKET_IB-pr-370.md`. It must contain:
   - P;
   - every writer from (a), by name;
   - the built sha256s;
   - Branch A, and Branch B: refresh rollback to live `RbpsijC23XVUFPE0W34Gr/xqtDil94xYRqDuuZlaYx8=` (S3 version
     `Ntv3Br2YU3utvESdPFCiTMkVVatmyzxY`, re-read live), plus the runner bundle's live object version;
   - the replay arm for the applier (rerun step 4 before the ledger);
   - the after-read: a driven refresh READY at all 3 firms, read at each manifest's own as_of, with `terminated_count` 1 at inflection
     and cottonwood and 0 at 49financial, and the carried entry present in the served directory.

<criterion id="IB93-1-AC1" cell_refs="IB-pr-381"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r93/p93_cells.py" . IB93-1-AC1</invocation><expect>IB93-1-AC1 PASS</expect></criterion>
`IB93-1-AC1` -- the writers file counts and names every writer of the served directory, with evidence, and explains the served 10-08.
Base: FAIL.

<criterion id="IB93-1-AC2" cell_refs="IB-pr-381"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r93/p93_cells.py" . IB93-1-AC2</invocation><expect>IB93-1-AC2 PASS</expect></criterion>
`IB93-1-AC2` -- the runner `terminated_carry_forward` tests and the refresh `previous_state_served` tests pass, as do both suites whole.
Base: FAIL.

<criterion id="IB93-1-AC3" cell_refs="IB-pr-381"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r93/p93_cells.py" . IB93-1-AC3</invocation><expect>IB93-1-AC3 PASS</expect></criterion>
`IB93-1-AC3` -- on both firms' real inputs, the built release is READY with `terminated_count` 1 and the entry carried in the landed
directory, and live is REFRESH_FAILED. Inflection's 10-09 fire finds its previous state. The packet names P, every writer, the rollback
sha and both branches. Base: FAIL.

<expected_criteria>IB93-1-AC1, IB93-1-AC2, IB93-1-AC3</expected_criteria>

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No upload, apply or deploy. AWS reads only.
- **Client data:** opaque ids only in committed files; raw extracts stay in scratch outside the worktree and are deleted after.
- **Every `.py` edit passes `.tools/commit-gate.sh`**; safe-commit runs it.
- **Refusal clause:** if a criterion cannot be met as written, stop, file a row, and report. Never weaken a check, a test or the rule.
- **Row ids** are `IRPT_BCKEND-D2-W189-S<k>`; `surfaced_at` is the real time. Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~189" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~189@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~189 <0.9.0_WK_IRPT_BCKEND~189@opal.agent>" -F <msgfile> -- <paths>`.
  Do NOT pre-`git add`. Write the message file with the Write tool.
- **Search:** raw recursive grep/find in Bash is gated; use the native Grep/Glob/Read tools. **ASCII only.**

<paths>
infra/aws/lambda/investor-reporting/directory/
infra/aws/lambda/ci/lambda-source-map.json
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/tests/test_directory_runner_terminated.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-381.directory-writers-runner-carry-and-served-previous-state.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~189/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 86 (round 93, workstream ~P), cell `IB-pr-381`.
<owned_cells>IB-pr-381</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB93-1-AC1, IB93-1-AC2, IB93-1-AC3. The instance goes at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~189/IRPT_BCKEND.TO-IB-pr-381.directory-writers-runner-carry-and-served-previous-state.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message, give the writer count and names, P, the built sha256s, the commit hashes, each criterion's last line,
the replay outcomes per firm, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- IB-pr-380 P 8953eccfca (refresh rule, fail-closed without source_client_ids); directory_runner.py land() writes directory.json + latest.json (~872); runner bundle s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz via schedule.tf irpt_runner_bundle_uri; served inflection as_of 2026-10-08 after a REFRESH_FAILED 10-08 refresh (diagnosis IB91-1) -- a second writer until (a) proves otherwise (CTO msg 1988).
comp-iam: DECLARED-NOT-APPLICABLE -- reads under the seat's existing roles; no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: (a) READS the schedules; none is changed by this cell.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p93_cells.py dry-run at base 41efe788d3 on dell2 2026-10-09 ~00:4xZ: AC1, AC2, AC3 FAIL (no writers file; runner `-k terminated_carry_forward` selects 0 of 342; no replay or packet); 0 control bytes; ruff clean.
lane: the <paths> block IS the grant; directory/ is ~P's; directory_runner.py is IRPT_BCKEND's runner (gold script; its bundle deploy is routed to the applier with the pair).
</preflight>
