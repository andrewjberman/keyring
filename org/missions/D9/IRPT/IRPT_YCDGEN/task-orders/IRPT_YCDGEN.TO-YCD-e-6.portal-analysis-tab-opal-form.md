# IRPT_YCDGEN task order -- `YCD-e-6` -- ROUND 6 (THREAD): THE ANALYSIS TAB'S WIRE TYPE AND ADAPTER FOR THE OPAL FORM

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6.md</decomp_doc>
<owned_cells>YCD-e-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-e-6.portal-analysis-tab-opal-form</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~2</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-e-6` -- the analysis tab's wire type and adapter for the opal form (hops 8 Open (page); FWD-1)
- `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` and `contracts/adapt.ts` (`adaptAnalysisReport`, `AnalysisReportSliceView`, `adaptAnalysisReportSlice`): accept the OPAL_ENGINE form (R4); sections render from `status`, `method` and `coverage`; a NOT_AVAILABLE section shows its reason; the Opal form never reads `vendor_artifact`.
- `portal/scripts/adapt-analysis-report-opal-exercise.mjs` (new): takes one argument and prints one RESULT line: `opal` runs the adapter on an invented OPAL_ENGINE document (`RESULT: opal PASS`), `v1` runs it on a v1 document (`RESULT: v1 PASS`), `typecheck` runs `tsc -b --noEmit` in the portal and prints `RESULT: typecheck PASS` only on exit 0.
- No visual change beyond the sections the form adds. The portal is a git submodule on branch DEV: the issuer cuts you a worktree of the portal repo; commit there.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R4 The v2 form of AnalysisReport** (IRPT_BCKEND PRD v0.28 item 29, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` section ADDENDUM v0.28). One contract with a `provider` member: `YCHARTS` carries exactly the v1 members. `OPAL_ENGINE` carries `request_ref`, `disclosures` and `release` as v1 and, in place of the vendor members: `opal_artifact` (`sha256`, `byte_length`, `generated_at`, `run_record_key`); `effective_inputs` with `holdings_fingerprint`, `settings`, `inputs_as_of` and no `read_back`; sections with `section_id`, `section_type`, `units`, `as_of_date`, `status` (`VALUE` or `NOT_AVAILABLE`), `reason`, `method`, `coverage`, `page` optional; `computation_validation` (`status`, `checks_run`, `checks_failed`, `notes`). Under `OPAL_ENGINE` the vendor members (`vendor_artifact`, `read_back`, `extraction_validation`) are ABSENT, never null and never defaulted; a consumer that needs one rejects the document. `NOT_AVAILABLE` carries a null value and a `reason` from the closed set in R2. v1 and its schema `_contracts/AnalysisReport.schema.json` (pinned @62301f71e0) are untouched.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `wire/AnalysisReport.ts` (`vendor_artifact` 19, `read_back` 26), `wire/consumed.ts` 64-65, `adapt.ts` (950-957, 974, 1309, 1317, 1639-1652), `tabs/analysis/NativeSections.tsx`, and the PerformanceReport precedent `wire/PerformanceReport.ts` (line 15, `provider`). The portal colour law (`/frontend-dev`) binds any markup; add none unless a section needs it.
- Portal dev builds use port 5174 only. This cell needs no dev server.
- This is a product-file change: it lands on DEV through the issuer after the CTO's review, never by you.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W2-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/scripts/adapt-analysis-report-opal-exercise.mjs
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the exercise script reads an OPAL_ENGINE document through the adapter without touching vendor_artifact
- **AC2** -- the exercise script reads a v1 document through the adapter unchanged
- **AC3** -- the portal typechecks with zero errors, run through the exercise script

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-e-6"><invocation>bun portal/scripts/adapt-analysis-report-opal-exercise.mjs opal</invocation><expect>^RESULT: opal PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-e-6"><invocation>bun portal/scripts/adapt-analysis-report-opal-exercise.mjs v1</invocation><expect>^RESULT: v1 PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-e-6"><invocation>bun portal/scripts/adapt-analysis-report-opal-exercise.mjs typecheck</invocation><expect>^RESULT: typecheck PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-e-6.portal-analysis-tab-opal-form.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-e-6.portal-analysis-tab-opal-form`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~2`, third order; starts after c-6 is merged. Portal submodule cell: the issuer cuts the portal worktree and lands DEV after the CTO's review (product file). Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~23:0xZ):** worker 0.9.0_WK_IRPT_YCDGEN~2 workspace @8b5fa963da merged 2b01d10976 (proof and rows); the PORTAL candidate is commit 81bbeba2 on portal branch wk-IRPT_YCDGEN-67-portal (cut from portal DEV @481b3bcc5f) and is NOT LANDED: it touches product files, so it lands on portal DEV only after 1.0.0_SA_CTO's review, together with cell YCD-j-6 (stacked on it). e-6.AC1-AC3 PASS at the worker (opal 25 of 25 legs, v1 13 of 13, typecheck exit 0); instance VALID (the portal commit hash reads UNRESOLVED-HERE, announced, because it is a portal-repo hash). Row W2-S14 -> DISARMED by cell YCD-j-6. Row W2-S15 (11 of 51 portal tests red) is a PRE-EXISTING baseline: the issuer measured the same 40 pass, 11 fail on unedited portal DEV (`bun test src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/tabs/analysis`), so it is not this cell's regression; owner none in this round, carried to the CTO.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~2</slot>
<fabric>laptop</fabric>
