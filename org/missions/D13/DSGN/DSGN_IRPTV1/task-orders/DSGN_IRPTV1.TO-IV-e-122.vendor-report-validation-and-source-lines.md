# TO DSGN_IRPTV1.TO-IV-e-122 -- the vendor report's face carries a validation line and a source line, read from the wire's extraction_validation and its vendor; an Opal report is unchanged -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-122</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~70</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6625 (2026-10-12 ~22:03Z), section 1 row D2-S21: "A page cell: the face carries the validation line and the source line from the four validation keys already on the wire." (Carried unbuilt since round 30, msg 6344 item 3.) | **Rows:** D2-S21 | **Decomp cell:** `IV-e-122` (decomposition v31) | **outcome_ref:** FWD-1 of IRPT_YCDGEN, served on this project's page | **depends_on:** none (portal DEV 183860bac055 is the base).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-70` (branch `wk-dsgn-irptv1-r31-70`); run everything from its root unless a step says the
portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~70/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-70/portal` is a PORTAL worktree (its own git repo) at portal DEV `183860bac055`. Do not amend or revert anything
committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the
workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` here is a LINK to the
main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run,
then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file that has no uncommitted work of yours. ONE whole-scope
run before any edit (`bun test src/pages/InvestorReporting`, output to a file under
`C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~70/`) is your base for `new_failing_ids`; the issuer measured it at this base as
1203 pass, 27 skip, 1 fail (F14-AC3, a diff check against DEV 1f3ce9f0, a known base failure).

**What is wrong.** On a served vendor-kind analysis report (104 section cards) the laptop walk read the word "validation" once, inside a closed Technical
details, and "Source:" zero times in the opened dialog (the issuer's row D2-S21 in
`org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`, search the row id). The titles and units were repaired by IV-e-115 and
IV-e-116 and IV-e-118. The wire carries the report's validation: `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` lines 79-84 give
`extraction_validation` as exactly four members, `status` (`CERTIFIED` | `UNCERTIFIED` | `FAILED`), `checks_run` (number), `checks_failed` (number) and
`notes` (optional string or null); the portal's reader is `AnalysisReport.extractionValidation` in `contracts/` (read how `adapt.ts` maps it:
`validated`, `reasonCode`, `unconfirmedValueCount` appear in `tabs/analysis/NativeSections.tsx` lines 11-86). An Opal report's face already prints
`OPAL_SECTION_SOURCE_WORDS` ('Source: Opal Capital Analysis', `NativeSections.tsx` near line 60). Read that file's header comment first: it says what the face
prints for each report kind and why.

**The cell (`IV-e-122`).**
1. **The validation line.** On a vendor-kind report the face (the opened report, outside any closed `<details>`) carries ONE plain sentence from the four
   keys: what the producer's check found, in words a reader without the system's vocabulary understands (no `CERTIFIED` / `UNCERTIFIED` token, no check
   count without its meaning: for example how many checks were run and how many did not pass; say `notes` when it is present, as given). Read how the page
   words other statuses (`wordedRefusalFor`, `dashboard/coverageWords.ts`, the Technical-details wording; read only) and match the register; choose the
   wording once, in one constant, and say it. `validation_line` {on_face true, inside_closed_details false, keys_read ["status","checks_run","checks_failed","notes"]}.
2. **The source line.** The same face carries a source line for a vendor-kind report, shaped like the Opal one ('Source: ...'), naming the vendor the report came
   from. Read the vendor from the wire (`vendor_artifact` and the vendor view `header/vendorDisplayNames.generated.ts` that the Holdings footers already use through
   `holdingsFooterSource`); if the wire names no vendor for the report, the line says the fixed plain words for "a vendor's report" and you file a row saying
   the wire lacks it; never invent a vendor. `source_line` {on_face true, from "<the wire member or file you read it from>"}.
3. **An Opal report is unchanged.** Its face, its source line and its validation wording stay byte-for-byte as before (a rendered comparison of one synthetic
   Opal report before and after). `opal_report_unchanged` true.
4. **The test and the suite.** One rendered test `__tests__/dsgn-irptv1/iv-e-122.vendor-validation-and-source.test.tsx` (a vendor report prints both lines on its
   face and not inside a closed details; the same report with `checks_failed` above 0 reads differently from one with 0; an Opal report prints neither new
   line), one temporary mutant (move the validation sentence back inside the closed details) that the test catches, then reverted. Re-golden an existing test only
   where it asserts a face this change moves, and say which. `suite_base`, `suite_after` {pass, skip, fail, new_failing_ids}, `lint_errors`, `typecheck_errors`
   (run `bun run lint` and `bun run typecheck` after your last portal commit), `product_files_changed`, `portal_commit` (40 hex), and a screenshot of an opened
   synthetic vendor report showing both lines, read by you. Record everything in `VALIDATION_SOURCE_LINES.json` with the keys named in the criterion below.

<criterion id="IV122-AC1" cell_refs="IV-e-122"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r31/p31_round31.py" . IV122-AC1</invocation><expect>IV122-AC1 PASS</expect></criterion>
`IV122-AC1` -- a vendor report's face carries its validation line from the four extraction_validation members and its source line, both outside a closed details, an Opal report is unchanged, a rendered test and a mutant hold it, and a screenshot was read. Base: FAIL (no record).

<expected_criteria>IV122-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `contracts/wire/` (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`, which this order does not call for) and the files the other two cells of this round name.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
  A dev server is allowed only for your own screenshot, on a port other than 5174, started from YOUR worktree and stopped when you finish.
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order
  did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W70-S<k>`, with the real current UTC time; append as BYTES, never re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~70/
portal/src/pages/InvestorReporting/tabs/analysis/
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/vendorSectionNames.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-122.*
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-122.vendor-report-validation-and-source-lines.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v31 (round 31), cell `IV-e-122`.
<owned_cells>IV-e-122</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV122-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~70/DSGN_IRPTV1.TO-IV-e-122.vendor-report-validation-and-source-lines.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV122-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the two sentences the face prints and where each is read from; what the wire does and does
not carry for the vendor; the Opal-report comparison; the test and its mutant; lint, typecheck, and the suite before and after; what the screenshot shows; and
any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; two sentences are added to a vendor-kind report's face. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
