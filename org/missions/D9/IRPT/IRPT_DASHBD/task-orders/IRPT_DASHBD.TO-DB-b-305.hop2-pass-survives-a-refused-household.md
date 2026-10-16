# TO IRPT_DASHBD.TO-DB-b-305 -- the HOP-2 PASS survives a household the reader refuses (worker row IRPT_DASHBD-D2-W243-S1): `run_filled_report` also catches `publisher.PublishRefused` raised by the READER, records the client as refused and goes on (round 149)

<to_id>IRPT_DASHBD.TO-DB-b-305</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~245</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>FILLEDPASS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** FILLEDPASS, round 149 | **Ordered by:** worker 243's row `IRPT_DASHBD-D2-W243-S1` (ARMED, disarm owner `2.0.0_SA_COO~D2`) on the drained cell `DB-b-302` (merge `aec0df87fc`): the reader raises `publisher.PublishRefused` for a household it cannot compose, but `run_filled_report` catches only `NotYetAvailable` around the reader, so one such household would end the whole pass once the switch is on | **Decomp cell:** `DB-b-305` (decomposition section 165).

**Risk class WORLD** is the floor of the path (`infra/`): one handler function and tests in a branch; no Terraform command, no AWS call, no push. The switch stays OFF.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-245` (branch `wk-IRPT_DASHBD-245`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~245/`. Never push; never commit the workspace `portal` gitlink. Counts, dates, hashes and words only in the repo, a row, a commit message or your report; use synthetic ids in tests. **Before every commit, scan what you stage for a client figure and for long identifier runs; the commit gate's client-data list is absent on this box, so that scan is yours.** **Commit order: the artifact first, then the proof instance, then the status flip to complete as the LAST commit.** Tool calls that carry a backslash-r or backslash-n escape inside a shell heredoc can be altered in transit: write patch scripts to a file with the Write tool and run them.

**The cell (`DB-b-305`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p173_filled_pass_refused.py` (your three criteria); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py`, the function `run_filled_report` (first `FILLED-REPORT-A` block).
2. **The edit (ONE function).** In `run_filled_report`, the `try` that calls `reader(firm, cid)` gets a second `except publisher.PublishRefused:` clause, placed after the `except NotYetAvailable:` clause, that appends `cid` to `out["refused"]` and continues to the next client. Update the function's docstring to say that a household the reader refuses, like a document the publisher refuses, is recorded as refused and not written. Nothing else in the function changes, and NO other byte of `handler.py` or any other file changes (a bare `except Exception` is a defect: an unexpected failure must still propagate). Write the file as bytes with LF.
3. **Tests.** Add at least THREE tests, in `reporting-publish/tests/test_filled_report_reader.py` or `test_filled_report_publish.py`, whose names contain `reader_refused`: a refused household is recorded in `refused` and the pass writes the other clients; it is not counted as `not_available`; the switch off reads nothing. All existing tests keep passing.
4. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p173_filled_pass_refused.py" . DB173-1-AC1`, then AC2, then AC3. (A base-relative clause of the checker reads the file against commit `aec0df87fc`.)
5. **Record** `RD_FILLED_PASS_FACTS_R149.json` in your folder with EXACTLY these fields: `function_changed` ("run_filled_report"); `clause_added` (one sentence); `tests_added` (the new test names); `words` (one paragraph, 80 to 1800 characters: what changed and why, and what is NOT proven: nothing was deployed, the switch is off, the reader's id-space match with the directory is unmeasured).

<criterion id="DB173-1-AC1" cell_refs="DB-b-305"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p173_filled_pass_refused.py" . DB173-1-AC1</invocation><expect>DB173-1-AC1 PASS</expect></criterion>
`DB173-1-AC1` -- `handler.py` differs from the base only inside `run_filled_report`, which now catches `PublishRefused` around the reader as well as around the publish; `publisher.py` and `locals.tf` are byte-identical to the base. Base: FAIL.
<criterion id="DB173-1-AC2" cell_refs="DB-b-305"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p173_filled_pass_refused.py" . DB173-1-AC2</invocation><expect>DB173-1-AC2 PASS</expect></criterion>
`DB173-1-AC2` -- behaviour: a reader refusal is recorded in `refused` and the pass writes the clients after it; `NotYetAvailable` still records `not_available`; an unexpected exception still propagates; the switch off reads and writes nothing; a document the publisher refuses is still counted refused. Base: FAIL.
<criterion id="DB173-1-AC3" cell_refs="DB-b-305"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p173_filled_pass_refused.py" . DB173-1-AC3</invocation><expect>DB173-1-AC3 PASS</expect></criterion>
`DB173-1-AC3` -- at least three NEW tests carry `reader_refused` in their name and both filled-report test files pass under pytest. Base: FAIL.

<expected_criteria>DB173-1-AC1,DB173-1-AC2,DB173-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no Terraform command, no push. Writes: the one handler, the test files and your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W245-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`) and BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output: a refused commit leaves your edit uncommitted and blocks every other seat's merge. ASCII only in anything you write.

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_reader.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_filled_report_publish.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~245/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-305.hop2-pass-survives-a-refused-household.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 165 (round 149, workstream FILLEDPASS), cell `DB-b-305`.
<owned_cells>DB-b-305</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB173-1-AC1, DB173-1-AC2, DB173-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~245/IRPT_DASHBD.TO-DB-b-305.hop2-pass-survives-a-refused-household.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB173-1-AC1,DB173-1-AC2,DB173-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the clause added in one line; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one handler function and tests in a branch; no plan, no apply, nothing deployed; the switch is off.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: nothing is applied in this cell; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the issuer ran them on a reference tree (green) and on three single-fault mutants of the handler and one diff mutant (all red).
lane: the <paths> block IS the grant.
</preflight>
