# TO DSGN_IRPTV1.TO-IV-e-85 -- W35-S2: Export on the Analysis tab (FWD-9) -- first read why AnalysisTab passes no export signal; wire it if the page alone can, else stop with a row for the CTO's contract

<to_id>DSGN_IRPTV1.TO-IV-e-85</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~46</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's round analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_FROM_WATERMARK_20261002_20261011.md` @10d7d46e49, section 4 item 4 | **Decomp cell:** `IV-e-85` (decomposition v11) | **outcome_ref:** FWD-9 (Export) | **depends_on:** IV-e-83 (same slot, same worktree pair).

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-46`; run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/`.

**Two repos, one worktree pair.** `C:/dev/wk-dsgn-irptv1-46` is the workspace worktree; `C:/dev/wk-dsgn-irptv1-46/portal` is a PORTAL worktree (its own git repo, branch
`wk-dsgn-irptv1-r11-46`), cut by the issuer from the portal DEV tip `7bb81fa89792067bf90531371bcf0031a05f878c` (read by `ls-remote` after a fetch, 2026-10-11 ~05:1xZ). Portal files commit in the
portal repo (cwd `C:/dev/wk-dsgn-irptv1-46/portal`, `bash C:/dev/wk-dsgn-irptv1-46/.tools/safe-commit.sh --author "<serial> <<serial>@opal.agent>" -F <msgfile> -- <paths relative to portal>`);
records, rows and this order's status commit in the workspace repo (cwd `C:/dev/wk-dsgn-irptv1-46`). Never push either repo.
**Toolchain.** `node_modules` in `C:/dev/wk-dsgn-irptv1-46/portal` is a junction made by the issuer: do NOT run `bun install`. Resolve bun with `command -v bun`; never
type its path. Tests: `bun test <file>` from `C:/dev/wk-dsgn-irptv1-46/portal`.

**THE CLIENT-DATA RULE (binding):** never print an account number, a client name or a client figure in a commit message, a record, a row or a report.
Fixtures are synthetic.

**The cell (`IV-e-85`).** Row W35-S2 (search `W35-S2` in the investigation file): Export does nothing on the Analysis tab. The page header owns the
one Export control (IV-e-16, FWD-9; see the comment at `src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx` ~line 430), and AnalysisTab passes it
no export signal. Your worktree pair already carries IV-e-83's commit.

In `C:/dev/wk-dsgn-irptv1-46/portal`:
1. **Read first.** Trace how the header's Export gets its target from each OTHER tab (the prop or context each tab supplies, with file and line) and
   why AnalysisTab supplies none. Record it under `why_no_signal` {text, evidence: [{file, line}]}.
2. **Decide from what you read, one of:**
   - `NEEDS_SERVED_ROUTE`: exporting the Analysis tab's content needs a served route or payload that does not exist. STOP there: file a row naming the
     missing route and what it would return, change NO product file, and record `finding`, `row`, `product_files_changed: []`. The CTO rules the contract.
   - `EXPORT_WIRED`: the page already holds everything the export needs. Wire the tab's export signal the same way the other tabs do, with a
     component test that fails before and passes after, and keep the existing pins passing. Record `finding`, `test_file`, `fail_before`, `after`,
     `product_files_changed`, `portal_commit`. The commit is a CANDIDATE for the CTO, not merged by you.
3. Write `EXPORT_ANALYSIS.json` and a one-page `.md`.

<criterion id="IV85-AC2" cell_refs="IV-e-85" judgment="true"/>
`IV85-AC2` -- graded at L9 by `3.0.0_SA_CVO`: the decision between the two findings follows from the code you cite, and an EXPORT_WIRED export contains
what the tab shows and nothing derived on the page.

<criterion id="IV85-AC1" cell_refs="IV-e-85"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r11/p11_round11.py" . IV85-AC1</invocation><expect>IV85-AC1 PASS</expect></criterion>
`IV85-AC1` -- the reason for the missing export signal is cited by file and line, and the cell either wires the export with a test or stops with a row and no product change. Base: FAIL.

<expected_criteria>IV85-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no download of any
  package, script or program.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant, a filled figure, or a client identifier in a committed file is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W46-S<k>`, with the real current UTC time.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/
portal/src/pages/InvestorReporting/tabs/analysis/
portal/src/pages/InvestorReporting/InvestorReportingPage.tsx
portal/src/pages/InvestorReporting/header/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-85.export-on-analysis-tab.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v11 (round 11), cell `IV-e-85`.
<owned_cells>IV-e-85</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV85-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~46/DSGN_IRPTV1.TO-IV-e-85.export-on-analysis-tab.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV85-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, each criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the page header's Export on one tab of a served page; a candidate commit only, landed on DEV after the CTO's review.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV85-AC1 FAIL at base (no record). CTO round analysis @10d7d46e49.
lane: the <paths> block IS the grant.
</preflight>
