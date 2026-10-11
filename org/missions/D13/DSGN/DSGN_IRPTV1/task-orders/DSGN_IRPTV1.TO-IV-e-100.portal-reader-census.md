# TO DSGN_IRPTV1.TO-IV-e-100 -- the census of portal readers of irpt-status routes, at PROD and at DEV: reader, key policy per level, and whether release 5's answer passes -- read-only

<to_id>DSGN_IRPTV1.TO-IV-e-100</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~56</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 4872 (2026-10-11 ~12:02Z): "One read-only cell, at the portal's PROD commit 37aa1247ee and again at DEV's tip ... For every irpt-status route the portal reads: the reader function with its file and line; its key policy at each level it checks, EXACT (an unknown key refuses) or TOLERANT; and, against release 5's answer for that route, PASS or the member that refuses. Denominator printed ... Two that must not be skipped. The sections reader, which will meet retained_ref ... And the single-request reader ... Any route whose PROD reader would refuse release 5's answer joins the history reader's PROD push." It is section 4 of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release5/NEVER_WIDEN_PAIR_ANLREQ_RELEASE5_RERELEASE_IRPT_STATUS.md` | **Decomp cell:** `IV-e-100` (decomposition v20) | **outcome_ref:** FWD-1 (the page reads what the service serves) | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-55` (branch `wk-dsgn-irptv1-r19-55`); run everything from its root unless a step says the
portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~56/`. `C:/dev/wk-dsgn-irptv1-55/portal` is a
PORTAL worktree (its own git repo). **This cell is READ-ONLY: you change no portal file and no workspace file outside your folder, the
surprise channel and this order's status line.** `portal/node_modules` is a junction: never write under it, never remove it, no `bun install`.

**Why.** A service release (irpt-status release 5) went live with new members on its answers; the portal's history reader admitted an exact
key set and refused every answer; the release was rolled back after 61 minutes. Nobody had listed which portal readers read that service and
how strictly. This cell is that list, so the re-release is signed on a measured consumer set.

**The cell (`IV-e-100`).**

1. **The denominator, both sides, printed with how you got it.**
   - `routes_served`: every route the irpt-status function serves. Read it from the function's own dispatch in the workspace
     (`infra/aws/lambda/investor-reporting/`: find the handler the Terraform names for `irpt-status`; start from
     `infra/aws/terraform/investor-reporting/` and the handler's route table), NOT from memory and not from the portal.
   - `routes_read_by_portal`: of those, the ones a portal client method calls (the route table and client in
     `portal/src/api/endpoints/investor-reporting.ts`). A served route no portal method calls is listed under `not_read_by_portal` with the
     search that showed it.
2. **Release 5's answer per route** (`release5_answer_source`). Release 5 is rolled back and you make NO live call. Read what it serves from
   the handler source at the release's source pins and from the release's own records:
   `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/task_orders/IRPT_ANLREQ.TO-APPLY-Y5.irpt-status-release5-dell2.md`, the pair under
   `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release5/`, and the laptop's after-read results it cites. Per route: which
   members release 5 ADDS or changes against the previous build, with the file and line that emits each, and the contract's line for it under
   `docs/contracts/investor-reporting/v1/`. Known so far, for you to confirm and complete, not to assume: `retained_ref` on the report
   sections read; `client_id`, `client_claim`, `unreadable_rows` on the history read; an OPAL_ENGINE branch of the section-date census.
   A route release 5 does not change is stated as unchanged, with how you know.
3. **Per route the portal reads: the reader and its key policy.** The reader function, file and line; then for EACH LEVEL it checks (the
   envelope, the `data` document, each nested object or row it validates): `EXACT` (an unknown key refuses) or `TOLERANT` (an unknown key is
   ignored or carried), with the line that shows it (`levels`: [{level, policy, evidence}]). A level the reader does not check at all is
   TOLERANT by absence: say so.
4. **PASS or the member that refuses, at TWO commits.** At the portal's PROD commit `37aa1247ee` and at DEV's tip (your portal worktree's
   HEAD after `git fetch origin DEV` and a fast-forward merge; record both hashes in `commits`): would this reader accept release 5's answer
   for its route? `at_prod` and `at_dev`: {result: PASS / REFUSES / NOT_ESTABLISHED, member (the first member that refuses), how, reason}.
   Read the PROD reader with `git -C portal show 37aa1247ee:<path>`; do not check PROD out over your worktree. Where you can, PROVE a result
   by running the reader on a body: a bun probe script kept OUTSIDE both worktrees that imports the reader from a path (for PROD, export the
   needed files at that commit into a scratch folder outside the repo with `git archive` or `git show`), feeds it a body built from the
   producer's own fixture or from the handler's emitted shape, wrapped as
   `{contract_version, operation, firm_id, data, unprojected_grant: {count: 0, denominator: 1, kinds: {}}}`, with a control that passes and a
   control that refuses. Where you only read the code, `how` says "read, not run".
5. **Two that must not be skipped** (`must_not_skip`: {sections_read, single_request_read}, each the route's name as your rows spell it):
   the report SECTIONS reader, which will meet `retained_ref` and, for an OPAL_ENGINE report, `computation_validation` where it expects
   `extraction_validation` (rows IRPT_YCDGEN-W2-S13 and IRPT_YCDGEN-W6-S4 in
   `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`: read them); and the SINGLE-REQUEST reader
   (`readOwnedRequest`), which shares its row check with history and has no `persist_inputs`.
6. **`joins_prod_push`**: exactly the routes whose `at_prod.result` is REFUSES. For each, one line on what the reader would need to admit
   (not built here). `product_files_changed: []`, `s3_or_live_calls: 0`.

<criterion id="IV100-AC1" cell_refs="IV-e-100"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_round20.py" . IV100-AC1</invocation><expect>IV100-AC1 PASS</expect></criterion>
`IV100-AC1` -- every served route the portal reads has its reader, its key policy per level, and a result at PROD and at DEV, over a printed denominator, with the sections and single-request readers included. Base: FAIL.

<criterion id="IV100-AC2" cell_refs="IV-e-100"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r20/p20_round20.py" . IV100-AC2</invocation><expect>IV100-AC2 PASS</expect></criterion>
`IV100-AC2` -- the routes that join the PROD push are exactly those whose PROD reader refuses, every unestablished result has its reason, and nothing was changed or called live. Base: FAIL.

<expected_criteria>IV100-AC1,IV100-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. No portal file is changed or committed.
- **No live call.** No request to any served route, no AWS call, no vendor call, no secret read, no deploy, no push, no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W56-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content. Write no client name, account id or figure.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~56/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-100.portal-reader-census.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v20 (round 20), cell `IV-e-100`.
<owned_cells>IV-e-100</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV100-AC1,IV100-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~56/DSGN_IRPTV1.TO-IV-e-100.portal-reader-census.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV100-AC1,IV100-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the denominator both ways with how you got it; ONE table, a row per route the portal reads: reader (file:line), key policy per level, release 5's change on that route, result at PROD and at DEV with the refusing member, and whether it was run or read; the routes that join the PROD push and what each reader would need to admit; the two must-not-skip readers in a sentence each; everything NOT_ESTABLISHED and why; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only cell; it IS the consumer census a blast read of the re-release needs.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the cell reads the served routes from the function's own dispatch and prints that denominator.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; both criteria FAIL at base (no record).
lane: the <paths> block IS the grant.
</preflight>
