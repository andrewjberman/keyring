# TO DSGN_IRPTV1.TO-IV-e-89 -- F40-AC5: the portal's calendar agrees with lib/trading_calendar.py day by day -- the portal takes its fallback from the one frontier, never a second copy; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-89</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~49</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-13 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_13_20261011.md` @72e8e2bb59, section 4 item 2 | **Decomp cell:** `IV-e-89` (decomposition v14) | **outcome_ref:** FWD-5, FWD-20 (a day labelled on a served page) | **depends_on:** none (first on slot ~49).

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-49`; run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~49/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-49` is the workspace worktree; `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo, branch
`wk-dsgn-irptv1-r14-49`), cut by the issuer from the portal DEV tip `1cd1cf252eae0eee0d67cba4bde31630a71f975c`. Portal files commit in the portal repo with plain git and your author line
(`git -c user.name="<serial>" -c user.email="<serial>@opal.agent" commit -F <msgfile> -- <paths>`; the workspace safe-commit fails inside the portal
repo on this box); records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never
commit the workspace `portal` gitlink. `node_modules` is a junction: do NOT run `bun install`; resolve bun with `command -v bun`.
**The suite baseline** is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json`: at portal `7bb81fa8` the Investor Reporting scope fails the same 43 ids in three runs, and the same 43 at
`1cd1cf25`. After your change run the whole scope ONCE (`bun test src/pages/InvestorReporting`, about 100 seconds, output to a file outside both
repos) and record `suite_after` {failed, fixed_ids, new_failing_ids} against those 43, by test id. A new failing id is yours to fix or to report.

**The cell (`IV-e-89`).** Test `fe-s-40/window.test.ts :: F40-AC5 -- the portal calendar agrees with lib/trading_calendar.py, day by day` fails 3 of 3
(row `DSGN_IRPTV1-D2-W43-S3`; the sample's error text names calendar fallback years 2010 against 2024). The CTO ruled (analysis section 3): a portal
calendar that disagrees with `lib/trading_calendar.py` can mislabel a day on a served page; **the portal takes its fallback from the one frontier,
never a second copy.**

In `C:/dev/wk-dsgn-irptv1-49/portal`:
1. Run the test alone and read its failure: which years or days disagree, and where the portal's calendar data comes from (the file it ships, how it
   was generated, what the test re-derives from `lib/trading_calendar.py` in the workspace worktree). Record what you find with file and line.
2. Fix the portal side so its calendar is DERIVED from the one frontier (`lib/trading_calendar.py`, read through whatever generation step the
   repository already has for it), not maintained as a second hand-edited copy. If the repository has a generator, run it and commit its output;
   if the portal's copy is hand-kept, replace it by a generated artifact with the command that regenerates it stated in a comment and in your
   record. Do NOT edit `lib/trading_calendar.py` (it is the frontier and it is not in your grant): if the frontier itself is what is wrong, stop
   with a row.
3. `F40-AC5` passes. The other calendar-reading tests in `fe-s-40/` still pass. Then the suite run of the baseline note.
4. Record `CALENDAR_FIX.json` {cause {text, evidence: [{file, line}]}, one_frontier {text, source: {file, line}}, regenerate_command,
   product_files_changed, portal_commit, suite_after}. The portal commit is a CANDIDATE for the CTO.

## AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-11 ~07:2xZ): the portal base moved before the cut

Your portal worktree is at DEV tip `ab697ba120a6452bdcb634038d8114b88f18e4a9`, not `1cd1cf25`: one Model Portfolios commit landed on DEV after the
issuance (two files outside Investor Reporting). `1cd1cf25` is its ancestor. The suite baseline is unchanged in meaning; if your first full run at
this base fails an id outside the 43 BEFORE any edit of yours, record it under `base_new_failing_ids` and do not count it against your change.

Gate limb: none graded this modification (to-pipeline-gate LIMB 6 fires on a newly added order only; `<placeholders>` is NONE).

<criterion id="IV89-AC1" cell_refs="IV-e-89"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r14/p14_round14.py" . IV89-AC1</invocation><expect>IV89-AC1 PASS</expect></criterion>
`IV89-AC1` -- F40-AC5 passes with no new failing id, and the record names the single frontier the portal's calendar is derived from. Base: FAIL.

<expected_criteria>IV89-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no download of any
  package, script or program, no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W49-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~49/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~49/
portal/src/pages/InvestorReporting/
portal/scripts/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-89.calendar-one-frontier.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v14 (round 14), cell `IV-e-89`.
<owned_cells>IV-e-89</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV89-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~49/DSGN_IRPTV1.TO-IV-e-89.calendar-one-frontier.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV89-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, the criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the portal's trading-calendar data read by served pages; a candidate commit only, landed on DEV after the CTO's review.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no served route is changed by this cell; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV89-AC1 FAIL at base (no record). CTO ROUND-13 ANALYSIS @72e8e2bb59.
lane: the <paths> block IS the grant.
</preflight>
