# TO DSGN_IRPTV1.TO-IV-e-92 -- test hygiene: bun resolved from the environment, the S60 press test off React's private dispatcher, and F47-AC6 -- three things, one cell

<to_id>DSGN_IRPTV1.TO-IV-e-92</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~49</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-13 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_13_20261011.md` @72e8e2bb59, section 4 item 5 | **Decomp cell:** `IV-e-92` (decomposition v14) | **outcome_ref:** FWD-1 (the suite bar) | **depends_on:** IV-e-89 (same slot, same worktree pair).

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

**The cell (`IV-e-92`).** Your worktree pair already carries IV-e-89's candidate commit; do not touch it.

In `C:/dev/wk-dsgn-irptv1-49/portal`:
1. **bun from the environment** (row `DSGN_IRPTV1-D2-W43-S1`; CLAUDE.md: derive, do not hardcode). Six baseline ids fail because a test spawns bun at
   a path under another user's profile. Find every hardcoded bun path in the Investor Reporting tests and their helpers, and resolve bun from the
   environment (the running executable, `process.execPath`, or PATH), with one shared helper if several tests need it. Record `bun`
   {hardcoded_paths_left (a count over the test tree, with the pattern and the denominator), source: [{file, line}], ids_fixed}.
2. **The press test** (`__tests__/dsgn-irptv1/upload-press-did-you-mean.test.tsx`). The CTO ruled (analysis section 2 item 3): tests press through
   the public surface, never React's internals: the testing library the portal already has in `package.json` if one is there, else a native DOM
   click inside `act`. FIRST state which the repository supports, from `package.json` and the installed `node_modules`: `TESTING_LIBRARY`,
   `NATIVE_ACT` (a DOM implementation is installed and `react-dom` can render into it under bun test), or `NEITHER`. The issuer's read of
   `package.json` at this commit found `react` and `react-dom` and no testing library and no DOM implementation named; verify it, including
   transitive installs. `NEITHER` means: do NOT add a dependency (that is a download and a CTO word), leave the test as it is, file a row that says
   what is missing, and record `press` {supports: "NEITHER", rewritten: false, row}. Otherwise rewrite the test to the supported way, show it still
   catches the two mutants (the handler fills nothing; the handler fills another ticker), and record `press` {supports, rewritten: true,
   uses_private_internals: false, mutants}.
3. **F47-AC6** (`fe-s-47/no-status-reason.test.ts`, "the reach, by subtraction over the committed tree"), recorded fixed on 2026-10-03 and red again
   (rows S56, S57 and `DSGN_IRPTV1-D2-W43-S3`). Run it alone, read which member of its subtraction is uncovered and which commit brought it, and
   either fix the test's subject (a product or test file in your grant) or, if the assertion is what is stale, ask its retirement: `f47` {outcome:
   FIXED or RULING_ASKED, reason, evidence}. F47-AC7 in the same file: say whether the same cause explains it.
4. The suite run of the baseline note; `TEST_HYGIENE.json` {bun, press, f47, product_files_changed, portal_commit, suite_after}.

<criterion id="IV92-AC1" cell_refs="IV-e-92"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r14/p14_round14.py" . IV92-AC1</invocation><expect>IV92-AC1 PASS</expect></criterion>
`IV92-AC1` -- no hardcoded bun path is left, the press test is rewritten or its missing support is rowed, F47-AC6 is fixed or its ruling asked, with no new failing id. Base: FAIL.

<expected_criteria>IV92-AC1</expected_criteria>

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
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-92.bun-env-press-f47.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v14 (round 14), cell `IV-e-92`.
<owned_cells>IV-e-92</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV92-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~49/DSGN_IRPTV1.TO-IV-e-92.bun-env-press-f47.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV92-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, the criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: test files and test helpers; a product file changes only if F47-AC6's subject is one, and then it is a candidate.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no served route is changed by this cell; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV92-AC1 FAIL at base (no record). CTO ROUND-13 ANALYSIS @72e8e2bb59.
lane: the <paths> block IS the grant.
</preflight>
