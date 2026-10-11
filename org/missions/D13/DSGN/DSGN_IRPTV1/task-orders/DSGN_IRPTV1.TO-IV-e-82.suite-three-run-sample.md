# TO DSGN_IRPTV1.TO-IV-e-82 -- one pinned three-run sample of the Investor Reporting suite at the portal DEV tip: the three failing SETS by test id, whether they are identical, and each failing id ruled once

<to_id>DSGN_IRPTV1.TO-IV-e-82</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~43</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_FROM_WATERMARK_20261002_20261011.md` @10d7d46e49, section 4 item 1 | **Decomp cell:** `IV-e-82` (decomposition v11) | **outcome_ref:** FWD-1 (the suite bar every page outcome is graded behind) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-43`; run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-43` is the workspace worktree; `C:/dev/wk-dsgn-irptv1-43/portal` is a PORTAL worktree (its own git repo, branch
`wk-dsgn-irptv1-r11-43`), cut by the issuer from the portal DEV tip `7bb81fa89792067bf90531371bcf0031a05f878c` (read by `ls-remote` after a fetch, 2026-10-11 ~05:1xZ). Portal files commit in the
portal repo (cwd `C:/dev/wk-dsgn-irptv1-43/portal`, `bash C:/dev/wk-dsgn-irptv1-43/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <paths relative to portal>`);
records, rows and this order's status commit in the workspace repo (cwd `C:/dev/wk-dsgn-irptv1-43`). Never push either repo.
**Toolchain.** `node_modules` in `C:/dev/wk-dsgn-irptv1-43/portal` is a junction made by the issuer: do NOT run `bun install`. Resolve bun with `command -v bun`; never
type its path. Tests: `bun test <file>` from `C:/dev/wk-dsgn-irptv1-43/portal`.

**THE CLIENT-DATA RULE (binding):** never print an account number, a client name or a client figure in a commit message, a record, a row or a report.
Fixtures are synthetic.

**The cell (`IV-e-82`).** No count from this suite is citable today: rows S7, W21-S2, W23-S1, W29-S10 and W34-S1 each quote a different number of failures.
The CTO ruled the bar (analysis section 3, W29-S10): **the bar is the failing SET, not a count.** Read the five rows in
`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md` (search each id) before you run anything.

In `C:/dev/wk-dsgn-irptv1-43/portal`:
1. Confirm `git rev-parse HEAD` equals `7bb81fa89792067bf90531371bcf0031a05f878c`, and record the `ls-remote` read the issuer made (sha and time) under `ls_remote`. Do not re-fetch.
2. Run the WHOLE Investor Reporting test scope three times, one after another, never in parallel: `bun test src/pages/InvestorReporting` (370 test
   files at this commit; print the count you see). Capture each run's full output to a file OUTSIDE both repos. Use a timeout that fits a full run and
   say how long each took. A run that crashes or times out is not a run: say so and stop with a row.
3. From each run's own output take the failing test ids (file path plus full test name), the pass, fail and skip counts. Record `SUITE_SAMPLE.json`
   {dev_tip, ls_remote: {sha, read_at}, command, test_files, runs: [{commit, duration_s, passed, failed, skipped, failing_ids}], identical}.
4. **Identical sets:** rule each failing id ONCE under `rulings`: {id, ruling, row, basis}. `REGRESSION` (it should pass at this commit and does not),
   `KNOWN-LEGACY` (named in an existing row: give the row id) or `FLAKE` (say what makes it one: it cannot be FLAKE on three identical failures unless
   you show the nondeterminism). The ruling is a PROPOSAL the reviewer grades; give the evidence for each.
   **Sets that differ:** record `differing_ids` (the union minus the intersection), write NO rulings, and file a row: the differing ids are the finding.
5. A one-page `SUITE_SAMPLE.md` beside it: for each of the five rows, whether this sample closes it or re-states it, and why.

<criterion id="IV82-AC1" cell_refs="IV-e-82"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r11/p11_round11.py" . IV82-AC1</invocation><expect>IV82-AC1 PASS</expect></criterion>
`IV82-AC1` -- three full runs at the DEV tip are recorded by failing test id, the identical flag follows from the sets, and every failing id is ruled once or the differing ids are named. Base: FAIL.

<expected_criteria>IV82-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no download of any
  package, script or program.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant, a filled figure, or a client identifier in a committed file is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W43-S<k>`, with the real current UTC time.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-82.suite-three-run-sample.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v11 (round 11), cell `IV-e-82`.
<owned_cells>IV-e-82</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV82-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/DSGN_IRPTV1.TO-IV-e-82.suite-three-run-sample.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV82-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, each criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only test sample; no product, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV82-AC1 FAIL at base (no record). CTO round analysis @10d7d46e49.
lane: the <paths> block IS the grant.
</preflight>
