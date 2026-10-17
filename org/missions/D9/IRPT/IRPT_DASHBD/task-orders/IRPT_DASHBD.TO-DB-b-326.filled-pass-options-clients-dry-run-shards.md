# TO IRPT_DASHBD.TO-DB-b-326 -- the CODE of the filled-report switch-on pair (IB-pr-551 hop 2, CTO msg 10295): the filled-report pass takes optional scoping -- `clients`, `dry_run`, `shard`/`shards` -- so the first pass is proven on ONE client and a dry run before it is run whole; absent, the pass is exactly what it is today (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-326</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~257</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>FILLPASS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's ruling msg 10295 (2.0.0_SA_COO~D2 issues the filled-report switch-on pair; the switch is an environment variable on `irpt-49f-reporting-publish-lambda`, in this seat's root) and S2's grade `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/GRADE_IB_pr_616_STEP_6_AND_IB_pr_618_20261017.md` (hops 3 and 4 live; the switch OFF; no `filled_report.json` exists) | **Decomp cell:** `DB-b-326` (decomposition section 185).

**Why this cell exists.** Today `filled_report_fire` with the switch ON writes a filled document for EVERY directory client in one synchronous invoke (about 4,000 households, a 300 s function) with no subset, no dry run and no shard. A first pass of a client-facing document set must be provable on one client, and must fit the function's limits. The options mirror the summaries pass (`clients`, `dry_run`, `shard`/`shards`, the stable `shard_of` hash).

**Risk class WORLD** is the floor of the path (`infra/`): one source file and a new test file in a branch. No Terraform command, no AWS call, no push. Nothing is deployed and the switch stays OFF.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-257` (branch `wk-IRPT_DASHBD-257`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~257/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report; use synthetic ids and marker strings only. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the proof instance, then the status flip to complete as the LAST commit.** Write patch scripts to a file with the Write tool and run them (a backslash escape inside a shell heredoc can be altered in transit).

**The cell (`DB-b-326`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p192_filled_pass_options.py` (your three criteria) and the issuer's REFERENCE DIFF `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/reads/DB326_REFERENCE.patch` (`handler.py` and one new test file, already green against the checker); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` between `# BEGIN FILLED-REPORT-A` and `# END FILLED-REPORT-A` (`run_filled_report`, `filled_report_fire`), `run_summaries` and `_summaries_requested` (the pattern the options follow) and `tests/test_filled_report_publish.py` (the test style).
2. **Apply the reference diff** (`git apply` from your worktree root, then read every hunk): `handler.py` gains, INSIDE the FILLED-REPORT-A block only, `_filled_options(event)` (validates `clients`, `dry_run`, `shard`/`shards` BEFORE any read) and a new `filled_report_fire(event, context=None, s3=None, directory=None)` (switch OFF returns at once whatever the options; otherwise it narrows the directory clients by `clients` then by `shard_of`, puts nothing when `dry_run`, marks a dry run and a shard in the response, and keeps the one `put_object`). The new test file `reporting-publish/tests/test_filled_report_pass_options.py` is part of the diff. If a hunk does not apply, or you think the reference is wrong, file a BLOCKING row and stop on it.
3. **Nothing else changes:** no other source file, no other test, no Terraform, no environment variable.
4. **Run the checks yourself before the record**, from the MAIN tree's copy of the checker, by absolute path, against your worktree as the root: `python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p192_filled_pass_options.py" C:/dev/wk-irpt-dashbd-257 DB192-1-AC1`, then AC2, then AC3 (AC3 runs the whole reporting-publish test directory, about 5 seconds). Run `ruff check` on both files first.

<criterion id="DB192-1-AC1" cell_refs="DB-b-326"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p192_filled_pass_options.py" C:/dev/wk-irpt-dashbd-257 DB192-1-AC1</invocation><expect>DB192-1-AC1 PASS</expect></criterion>
`DB192-1-AC1` -- the diff: only `handler.py` (inside the FILLED-REPORT-A block, nothing outside it) and the new test file changed; at most 20 lines removed and 80 added; one `put_object`; nothing printed, logged or deleted. Base: FAIL.
<criterion id="DB192-1-AC2" cell_refs="DB-b-326"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p192_filled_pass_options.py" C:/dev/wk-irpt-dashbd-257 DB192-1-AC2</invocation><expect>DB192-1-AC2 PASS</expect></criterion>
`DB192-1-AC2` -- behaviour on the real `filled_report_fire`: default unchanged (every directory client written once, the response keys unchanged); a named subset once each; a dry run reads and validates and writes nothing; seven shards write every client exactly once; clients and shards intersect; malformed options refused with no read or write; the switch OFF returns at once. Base: FAIL.
<criterion id="DB192-1-AC3" cell_refs="DB-b-326"><invocation>python -I "C:/dev/ajb_workspace/org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p192_filled_pass_options.py" C:/dev/wk-irpt-dashbd-257 DB192-1-AC3</invocation><expect>DB192-1-AC3 PASS</expect></criterion>
`DB192-1-AC3` -- at least six NEW tests carry `options` in their name and the whole `reporting-publish/tests` directory passes. Base: FAIL.

<expected_criteria>DB192-1-AC1,DB192-1-AC2,DB192-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: `handler.py`, the new test file and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W257-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_pass_options.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~257/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-326.filled-pass-options-clients-dry-run-shards.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 185 (round 150, workstream FILLPASS), cell `DB-b-326`.
<owned_cells>DB-b-326</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB192-1-AC1, DB192-1-AC2, DB192-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~257/IRPT_DASHBD.TO-DB-b-326.filled-pass-options-clients-dry-run-shards.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB192-1-AC1,DB192-1-AC2,DB192-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the number of new tests; what is NOT proven (nothing deployed; the reader against the real partition inside the function's memory and time was not run). Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one source file and a new test file in a branch; no plan, no apply, nothing deployed; the switch stays OFF.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green, the reference diff is committed beside the checker) and on single-fault mutants (all red).
lane: the <paths> block IS the grant.
</preflight>
