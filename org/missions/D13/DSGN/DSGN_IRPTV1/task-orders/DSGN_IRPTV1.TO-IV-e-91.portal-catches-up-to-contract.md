# TO DSGN_IRPTV1.TO-IV-e-91 -- the portal half catches up to the contract: the 18 failing ids whose contract files are ahead of the portal's routes table, envelopes and content pins -- the portal moves; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-91</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~49</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-13 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_13_20261011.md` @72e8e2bb59, section 4 item 4 | **Decomp cell:** `IV-e-91` (decomposition v14) | **outcome_ref:** FWD-1, FWD-9, FWD-11 (the wire the page reads) | **depends_on:** IV-e-92 (same slot, same worktree pair).

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

**The cell (`IV-e-91`).** Row `DSGN_IRPTV1-D2-W43-S2`: 18 baseline ids (fe-s-13 routes, content-pins, producer-fixtures, request-corpus; fe-s-14 header,
envelope, published-map; fe-s-57 carry; mvp-selection) fail because the contract files they read from the WORKSPACE tree (`docs/contracts`, `lib`)
are ahead of the portal half. The CTO ruled (analysis section 3): **the portal moves. The contract is the ratified side.** The portal's routes
table, envelopes and content pins catch up, and the record names both commits. Your worktree pair already carries IV-e-89's and IV-e-92's commits.

In `C:/dev/wk-dsgn-irptv1-49`:
1. List the 18 ids from the baseline (the rulings whose `row` is `DSGN_IRPTV1-D2-W43-S2`). Run each failing file alone and read its own error:
   which contract member the portal lacks or spells differently. Group the 18 by cause; print the denominator.
2. For each cause, move the PORTAL: the routes table, the envelope types, the content pins or fixtures, to what the contract at your workspace
   commit says. Never edit a contract file, and never weaken a test to pass. A cause where the portal is right and the contract is what moved
   wrongly is a row, not a fix; list its ids under `not_fixed` with the reason.
3. A change that alters what a served page sends or reads (a route path, a request member) is stated one by one in the record under
   `wire_changes` [{what, before, after, source}]: the CTO reads that list before DEV.
4. The suite run of the baseline note; `CONTRACT_CATCHUP.json` {causes: [{cause, ids, fix}], wire_changes, not_fixed, workspace_commit (the
   box/dell2 commit your contract files are read at), portal_commit, product_files_changed, suite_after}. The portal commit is a CANDIDATE.

<criterion id="IV91-AC1" cell_refs="IV-e-91"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r14/p14_round14.py" . IV91-AC1</invocation><expect>IV91-AC1 PASS</expect></criterion>
`IV91-AC1` -- every contract-family id is fixed or reasoned, with no new failing id, and the record names both commits and every wire change. Base: FAIL.

<expected_criteria>IV91-AC1</expected_criteria>

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
portal/src/api/endpoints/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-91.portal-catches-up-to-contract.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v14 (round 14), cell `IV-e-91`.
<owned_cells>IV-e-91</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV91-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~49/DSGN_IRPTV1.TO-IV-e-91.portal-catches-up-to-contract.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV91-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes in each repo, the criterion's last line, what you measured, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the portal's Investor Reporting wire (routes table, envelopes, pins) moves to the ratified contract; a candidate commit only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no served route is changed by this cell; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched; nothing is deployed.
comp-adversary: RUN -- IV91-AC1 FAIL at base (no record). CTO ROUND-13 ANALYSIS @72e8e2bb59.
lane: the <paths> block IS the grant.
</preflight>
