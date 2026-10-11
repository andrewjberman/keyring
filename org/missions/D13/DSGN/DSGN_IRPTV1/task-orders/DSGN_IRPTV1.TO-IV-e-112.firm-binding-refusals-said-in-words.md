# TO DSGN_IRPTV1.TO-IV-e-112 -- the reads the walk saw refused with FIRM_BINDING: which face each feeds, and that face says the refusal in words -- a product change; candidate to the CTO

<to_id>DSGN_IRPTV1.TO-IV-e-112</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~62</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 ruling msg 5562 (2026-10-11 ~18:27Z) on the laptop's rendered walk (`org/tier1_exec/4.0.0_SA_CRO/deliverables/XB_C5CE_IRPT_DEV_WALK_RESULT_20261011.md`): "S22 first ... And the face says the refusal in words." | **Rows:** DSGN_IRPTV1-D2-S22 | **Decomp cell:** `IV-e-112` (decomposition v26) | **outcome_ref:** FWD-1 (the Performance hop's faces) | **depends_on:** none; FIRST on the slot (it may be what Andrew meets when he sits).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is a real local install that another worktree junctions to: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~62/`) is your base for `new_failing_ids`.

**What was seen (row D2-S22).** In the laptop's rendered walk of the page against the SERVED backend (the result file named above, face
9; read it whole first), every `/api/` answer was HTTP 200, and inside them `reporting/<account>/manifest` and
`reporting/client/<client>/summary` answered UNAVAILABLE with reason `FIRM_BINDING`, three times, as a staff sign-in (internal, role
admin). Nothing on any face said so, and which face those reads feed was not seen. Whether a firm was selected in the header when they
were refused is being asked of the walker and is NOT known; do not assume it.

**The cell (`IV-e-112`).**
1. **Trace each read to its face.** The summary read is `dashboard/reportingRead.ts` (`reportingSummaryPath`); find the manifest
   read's reader and EVERY other reader of the `reporting/` routes the client's route table declares
   (`src/api/endpoints/investor-reporting.ts`, `IR_ROUTE_TABLE`). For each: `reads`: [{route, reader {file, line}, feeds_face (which
   visible part of which tab), on_refusal_before (exactly what the face shows today when the answer is UNAVAILABLE with FIRM_BINDING:
   nothing, a spinner, an empty panel, words), on_refusal_after}]. Establish `on_refusal_before` by a rendered test or by reading the
   code path to the JSX, and say which.
2. **The face says the refusal in words.** Wherever a face is silent or blank on that refusal, it states it in a sentence a principal
   can act on, using the page's EXISTING refusal vocabulary and component (read how the Performance refusal and `FirmDropdown.tsx`'s
   FIRM_BINDING note are worded; the page's named reason codes are generated in `render/Page.tsx`: do not hand-edit a generated region
   and do not invent a reason code). The sentence says what is not shown and why in plain words (the selected firm does not cover this
   client or account), and names no internal code on the face. No new request; no retry loop; no change to which firm is sent.
3. **A rendered test** under `__tests__/dsgn-irptv1/` for each face you change (the answer UNAVAILABLE with FIRM_BINDING -> the words
   are on the face), one temporary mutant. A screenshot from a build with a synthetic fixture that answers those routes with the
   refusal (`scripts/ui-smoke.mjs` now has `--type` and `--option` to pick a client; or the fixed driver in the ~58 folder), read by you.
4. `lint_errors`, `typecheck_errors`, `suite_after`, `product_files_changed`, `portal_commit`. Record `FIRM_BINDING_FACES.json`.

<criterion id="IV112-AC1" cell_refs="IV-e-112"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r26/p26_round26.py" . IV112-AC1</invocation><expect>IV112-AC1 PASS</expect></criterion>
`IV112-AC1` -- each refused reporting read is traced to its reader and its face, every such face states the refusal in words, a rendered test holds it with a failing mutant, and a screenshot was read. Base: FAIL.

<expected_criteria>IV112-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Every portal commit is followed by `bun run lint` and `bun run typecheck`**; a lint ERROR is fixed before you report (the count goes in
  the record as `lint_errors`, and typecheck's as `typecheck_errors`).
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W62-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-112.firm-binding-refusals-said-in-words.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v26 (round 26), cell `IV-e-112`.
<owned_cells>IV-e-112</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV112-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~62/DSGN_IRPTV1.TO-IV-e-112.firm-binding-refusals-said-in-words.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV112-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; ONE table: route, reader file:line, the face it feeds, what the face showed on the refusal before, what it says now; the test and its mutant; what the screenshot shows; `product_files_changed`; lint, typecheck and suite; the portal commit; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; sentences on faces that were silent on a refusal, on the page's existing refusal component; no request, route or contract change. The candidate is read by the CTO before DEV.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
