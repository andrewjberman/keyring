# TO DSGN_IRPTV1.TO-IV-e-101 -- an Opal report opened on the page prints no vendor wording -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-101</to_id>
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

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 rulings msg 4924 ("Hop 12's two new rows ... to 2.0.0_SA_COO~D2 as page cells") and msg 4958 with its IRPT_YCDGEN ROUND-12 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_12_20261011.md` @71a14ece46, section 2 ("They go ahead of the wire-folder regeneration. When both are on DEV I ask Andrew for the sitting.") | **Row:** IRPT_YCDGEN-D2-W14-S1 (related: IRPT_YCDGEN-W4-S8) | **Decomp cell:** `IV-e-101` (decomposition v21) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** none (its own portal worktree).

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

**What is wrong.** The page that opens a retained report draws EVERY report with the vendor's wording. `RetainedSections` in
`portal/src/pages/InvestorReporting/tabs/analysis/OwnedRequestHistory.tsx` (near line 151) prints, under "Technical details",
`Extraction validation: ...` from `report.extractionValidation` for any report (read by the issuer at portal 73806e29), and the section
blocks print a "Vendor attribution:" line (`NativeSections.tsx` near 105 and 186-190, as the journey read cites them). An OPAL_ENGINE report
is computed by Opal: it has no vendor and no extraction. A census of the portal's readers today says the sections adapter already branches
on `provider` and reads `computation_validation` for an Opal report (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~56/READER_CENSUS.json`,
row DSGN_IRPTV1-D2-W56-S1), while IRPT_YCDGEN-W4-S8 says the adapter sets no provider on the VIEW. Both may be true: establish it first.

**The cell (`IV-e-101`).**

1. **How does the page know?** Read the sections adapter (`contracts/adapt.ts`, `adaptAnalysisReportSlice`) and the view type: is the
   report's provider carried to the view, and where? `provider_known`: {how, file, line}. If the view does not carry it, carry it from the
   wire member the adapter ALREADY reads (no new request, no new wire member). If the wire answer gives no way to tell an Opal report from a
   vendor one, STOP with a row.
2. **The words.** For an OPAL_ENGINE report the page prints NO word "vendor" and NO word "extraction" anywhere in the opened report:
   - the validation line under Technical details reads `Computation validation: ...`, with the same value rule as today (CERTIFIED, else
     the reason code, else "Not stated"), drawn from the Opal form's validation member;
   - the per-section attribution line reads `Source: Opal Capital Analysis` (the words the page's own footers already print), never
     "Vendor attribution:";
   - any other vendor-worded string in the opened-report surface (find them: state the search) is treated the same way or listed.
   For a VENDOR report every string stays EXACTLY as it is today: record `vendor_before` (the two strings at your base) and `wording.vendor`
   (after), and they must be equal. Record `wording.opal` {attribution, validation}.
3. **A test** under the scope's `__tests__/dsgn-irptv1/`: renders `RetainedSections` (or the surface that hosts it) with an Opal report and
   asserts the rendered TEXT carries the Opal words and neither "vendor" nor "extraction" (case-insensitive); renders a vendor report and
   asserts today's words. One temporary mutant (the vendor wording restored for Opal) makes it fail. `test` {id, passes, mutant {what, failed}}.
4. **Look at it.** Two screenshots at least, saved in your folder: an opened OPAL report and an opened VENDOR report. `screenshots`
   [{state, path, canvas}] with the word "opal" or "vendor" in each state.
5. `bun run typecheck` 0 errors (never bare `tsc --noEmit`). One whole-scope run before any edit (your base) and one after: `suite_after`
   {failed, fixed_ids, new_failing_ids}; existing tests that pinned the vendor wording on an Opal report are brought to the new rule and
   listed with before and after; `product_files_changed`; `portal_commit`.

<criterion id="IV101-AC1" cell_refs="IV-e-101"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r21/p21_round21.py" . IV101-AC1</invocation><expect>IV101-AC1 PASS</expect></criterion>
`IV101-AC1` -- an Opal report reads its own words with no vendor or extraction word, a vendor report is unchanged, a test holds it and a mutant breaks it. Base: FAIL.

<criterion id="IV101-AC2" cell_refs="IV-e-101"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r21/p21_round21.py" . IV101-AC2</invocation><expect>IV101-AC2 PASS</expect></criterion>
`IV101-AC2` -- an opened Opal report and an opened vendor report are screenshotted from a build on the light canvas, typecheck is clean and no new id fails. Base: FAIL.

<expected_criteria>IV101-AC1,IV101-AC2</expected_criteria>

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
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-101.opal-report-no-vendor-wording.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v21 (round 21), cell `IV-e-101`.
<owned_cells>IV-e-101</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV101-AC1,IV101-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~57/DSGN_IRPTV1.TO-IV-e-101.opal-report-no-vendor-wording.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV101-AC1,IV101-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the portal commit hashes in order, each criterion's last line, how the page knows the provider (file and line), every vendor-worded string you found on the opened-report surface and what each reads for an Opal report now, the vendor report's strings before and after, the test and its mutant, each screenshot with what it shows, typecheck, every existing test updated, `product_files_changed`, `suite_after`, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; wording on one surface of a client-facing page; a vendor report is pinned unchanged; the candidate with its screenshots is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record). The defect itself is another lane's code read at portal dbeb6764ea, not rendered and not re-read by the issuer beyond the lines quoted in the WORKER FACE.
lane: the <paths> block IS the grant.
</preflight>
