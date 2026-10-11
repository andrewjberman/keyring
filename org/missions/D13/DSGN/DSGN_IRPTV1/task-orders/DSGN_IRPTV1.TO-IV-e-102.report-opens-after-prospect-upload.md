# TO DSGN_IRPTV1.TO-IV-e-102 -- the report can be opened after a Prospect upload -- a rendered read FIRST, then the fix only if the read says so; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-102</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~57</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 rulings msg 4924 ("Hop 12's two new rows ... to 2.0.0_SA_COO~D2 as page cells") and msg 4958 with its IRPT_YCDGEN ROUND-12 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_12_20261011.md` @71a14ece46, section 2 ("They go ahead of the wire-folder regeneration. When both are on DEV I ask Andrew for the sitting.") | **Row:** IRPT_YCDGEN-D2-W14-S2 (INFERRED from a portal comment, not measured) | **Decomp cell:** `IV-e-102` (decomposition v21) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** IV-e-101 (the same worktree pair).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-57` (branch `wk-dsgn-irptv1-r21-57`); run everything from its root unless a step says the
portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~57/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-57/portal` is a PORTAL worktree (its own git repo, branch `wk-dsgn-irptv1-r21-57`) at the commit your
spawn prompt names. Portal files commit in the portal repo with plain git and your author line; records, screenshots, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`portal/node_modules` is a JUNCTION to another worktree's install: never write or delete under it, never remove it, no `bun install`, no
package change. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with
`git checkout -- <file>` on a file that has no uncommitted work of yours.

Read first: the journey read's hop 12 (`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~14/JOURNEY_READ_YCD-a-11.md`), the row named above in
`org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`, and portal law before touching visual code: `portal/CLAUDE.md` ("Color law") and
`portal/DESIGN.md` (C1 to C12).

**What is claimed, and it is only inferred.** After a Prospect upload and Generate (no client picked in the header), the one surface that
opens the report, "Your analysis requests", mounts only when the header holds a client (`tabs/analysis/AnalysisTab.tsx` near lines 397-409),
so the user's own report may have nowhere to open from. Nobody has rendered it.

**The cell (`IV-e-102`).**

1. **MEASURE FIRST, rendered, before any edit.** Build the portal and render the Analysis tab with NO client in the header, in the state
   after a Prospect upload has been generated (synthetic fixtures: the owner's history answer holds one request). Does "Your analysis
   requests" (or any surface that opens that report) mount? `measured`: {opener_mounts_without_client (true or false), how: "RENDERED",
   evidence (a PNG in your folder), what_you_saw}. Also read the code and state the exact condition that decides the mount, with file and line.
2. **If it DOES mount:** the inference was wrong. `outcome: "NOT_A_DEFECT"`, no product file changes, and your record says what the comment
   that misled the read actually guards. Stop there.
3. **If it does NOT mount:** fix it, minimally. A user who generated a report from a Prospect upload can open THEIR OWN requests without
   picking a client: the opener mounts for the prospect owner and lists that owner's requests through the SAME history read the page already
   makes (no new request shape, no new route, no change to what any reader accepts). What a picked client sees is unchanged. If mounting it
   without a client would show one owner another owner's requests, or needs a change to what the service returns, STOP with a row
   (`outcome: "STOPPED"`). On a fix: a rendered test (with no header client, after a generate, the opener is present and opens the report;
   with a header client, today's behaviour) and one temporary mutant (the old mount condition restored) that makes it fail; `after`
   {opener_mounts_without_client: true, evidence (a PNG)}; `outcome: "FIXED"`.
4. `bun run typecheck` 0 errors. One whole-scope run before any edit and one after: `suite_after`; `product_files_changed` ([] unless
   FIXED); `portal_commit` (your last portal commit, or your base if you committed nothing in the portal).

<criterion id="IV102-AC1" cell_refs="IV-e-102"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r21/p21_round21.py" . IV102-AC1</invocation><expect>IV102-AC1 PASS</expect></criterion>
`IV102-AC1` -- the opener's mount with no client in the header is measured on the rendered page, and the outcome agrees with that measurement. Base: FAIL.

<criterion id="IV102-AC2" cell_refs="IV-e-102"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r21/p21_round21.py" . IV102-AC2</invocation><expect>IV102-AC2 PASS</expect></criterion>
`IV102-AC2` -- a fix carries a test, a failing mutant and a rendered after-read; no fix carries no product change; typecheck is clean and no new id fails. Base: FAIL.

<expected_criteria>IV102-AC1,IV102-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Looking at it.** Screenshots come from a BUILD (`bun run build`, then `node scripts/ui-smoke.mjs <route> <out.png> --dist <built dir>
  --fixtures <f.json>`). If `ui-smoke` cannot reach the state, a driver that copies its recipe is accepted (the earlier one is
  `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~53/holdings-face-driver.mjs`): name the instrument in the record. Fixture bodies are
  synthetic: no real client name, account number or figure. READ every PNG: `LOC` matches the route, `CANVAS` reads `rgb(244, 246, 250)`.
  The built folder is never committed. Never fake a screenshot; if a state cannot be reached, say exactly where it stops.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W57-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~57/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-102.report-opens-after-prospect-upload.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v21 (round 21), cell `IV-e-102`.
<owned_cells>IV-e-102</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV102-AC1,IV102-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~57/DSGN_IRPTV1.TO-IV-e-102.report-opens-after-prospect-upload.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV102-AC1,IV102-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line, what the rendered read showed and the exact mount condition (file and line), the outcome and why, on a fix the portal commits, the test, its mutant and the after-read, on no fix what the misleading comment guards, typecheck, `product_files_changed`, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one mount condition on a client-facing page, measured before it is touched; the candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record). The defect itself is another lane's code read at portal dbeb6764ea, not rendered and not re-read by the issuer beyond the lines quoted in the WORKER FACE.
lane: the <paths> block IS the grant.
</preflight>
