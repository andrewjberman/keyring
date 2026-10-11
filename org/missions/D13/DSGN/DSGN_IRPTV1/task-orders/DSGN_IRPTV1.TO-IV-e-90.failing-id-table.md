# TO DSGN_IRPTV1.TO-IV-e-90 -- the 43-id table: every failing id of the suite sample is a REGRESSION with an owner and a cell, or an assertion whose RETIREMENT is asked with its reason -- KNOWN-LEGACY is not a class

<to_id>DSGN_IRPTV1.TO-IV-e-90</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~50</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-13 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_13_20261011.md` @72e8e2bb59, section 4 item 3 | **Decomp cell:** `IV-e-90` (decomposition v14) | **outcome_ref:** FWD-1 (the suite bar) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-50`; run everything from its root unless a step says the portal. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~50/`.

**The cell (`IV-e-90`).** The reviewer refused the 14 KNOWN-LEGACY labels of the suite sample, and the CTO tightened the bar to match (analysis section
2 item 2): a failing test is one of two things, a REGRESSION with an owner, or an assertion RETIRED by a ruling that is cited. "Known" is not a
third class. This cell writes the one table the CTO rules from. It is read-only.

In `C:/dev/wk-dsgn-irptv1-50`:
1. The 43 ids and their proposed rulings are in the baseline record
   `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~43/SUITE_SAMPLE.json` (and `SUITE_SAMPLE.md` beside it). The run logs are
   outside the repo under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~43/`: read each id's own error text there.
2. For EACH id read the test (portal code by content: `git -C C:/dev/ajb_workspace/portal show 1cd1cf252eae0eee0d67cba4bde31630a71f975c:<path>`),
   the rows the sample cites for it (Grep the id's row in `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`),
   and any ruling in the reviewer's files (`surprise-channel/adjudications/`, `remediations/`) or the two CTO analyses of 2026-10-11 that already
   decides it. Then one of:
   - `REGRESSION_OWNED`: {owner (a seat or a project lane), cell (an existing order id of round 14: IV-e-89 the calendar, IV-e-91 the contract
     catch-up, IV-e-92 bun / press / F47; or `UNCUT` with the one-line cell it needs), cause};
   - `RETIREMENT_ASKED`: {assertion_retired (what the test asserts that should no longer hold), reason, ruling_cited (the ruling that already
     retires it, by path and line) or `asks_ruling: true`}.
   Nothing else. An id whose cause you cannot read is `REGRESSION_OWNED` with `cell: UNCUT` and the question that cell answers.
3. `FAILING_ID_TABLE.json` {baseline, rows: [...]} and a one-page `.md` with the table grouped by disposition, and the counts.

<criterion id="IV90-AC1" cell_refs="IV-e-90"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r14/p14_round14.py" . IV90-AC1</invocation><expect>IV90-AC1 PASS</expect></criterion>
`IV90-AC1` -- all 43 ids carry one of the two dispositions with its owner and cell or its reason and the assertion retired. Base: FAIL.

<expected_criteria>IV90-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no vendor call, no secret read, no `bun install`, no download of any
  package, script or program, no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W50-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~50/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~50/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-90.failing-id-table.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v14 (round 14), cell `IV-e-90`.
<owned_cells>IV-e-90</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV90-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~50/DSGN_IRPTV1.TO-IV-e-90.failing-id-table.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV90-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, the criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only table; no product, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no served route is changed by this cell; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV90-AC1 FAIL at base (no record). CTO ROUND-13 ANALYSIS @72e8e2bb59.
lane: the <paths> block IS the grant.
</preflight>
