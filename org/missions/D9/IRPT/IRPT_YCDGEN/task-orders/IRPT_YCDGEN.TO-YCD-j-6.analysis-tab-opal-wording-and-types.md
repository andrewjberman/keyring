# IRPT_YCDGEN task order -- `YCD-j-6` -- ROUND 6 (THREAD): THE ANALYSIS TAB'S WORDING AND TYPES FOR THE OPAL FORM: NO VENDOR HEADINGS, METHOD AND COVERAGE SHOWN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6B.md</decomp_doc>
<owned_cells>YCD-j-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-j-6.analysis-tab-opal-wording-and-types</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~4</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-j-6` -- the analysis tab's wording and types for the opal form: no vendor headings, method and coverage shown (hops 8 Open (page wording); FWD-1)
- `portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx`, `contracts/index.ts`, `contracts/wire/index.ts`, `contracts/wire/consumed.ts`, `contracts/wire/responses.ts` and `api/endpoints/investor-reporting.ts` (all under `portal/src/pages/InvestorReporting/`): R10.
- `portal/scripts/native-sections-opal-exercise.mjs` (new): takes one argument and prints one RESULT line. `opal` renders NativeSections to static markup for an invented OPAL_ENGINE section list and checks R10 (a) and (b) (`RESULT: opal PASS`); `v1` renders a v1 list and checks its headings and wording are unchanged (`RESULT: v1 PASS`); `typecheck` runs `tsc -b --noEmit` in the portal (`RESULT: typecheck PASS` only on exit 0).
- The portal is a git submodule: your worktree has a nested portal worktree cut from e-6's portal branch; commit the `portal/...` files INSIDE it. No colour or layout change beyond the added method and coverage text (the portal colour law binds).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R10 The Analysis tab speaks the Opal form (PRD FWD-1 ACCEPT; C-BRAND).** For a section list whose report has `provider: OPAL_ENGINE`, `tabs/analysis/NativeSections.tsx` (a) prints each section's `method` and `coverage` beside its value or its NOT_AVAILABLE reason; (b) does NOT print the headings 'Certified sections', 'Extraction validation:' or 'Vendor attribution:', nor the text 'no source coordinate stated for this section'; it prints the report's `computation_validation` status where the v1 view prints the extraction validation. The typed contracts and the response wire types name the Opal members so the adapter's wider unions are the declared types, not casts. A report with no `provider` or `provider: YCHARTS` renders exactly as before. Source: worker row IRPT_YCDGEN-W2-S14 (measured: NativeSections.tsx, contracts/index.ts, wire/index.ts, wire/consumed.ts 64-65, wire/responses.ts 162-166 and api/endpoints/investor-reporting.ts 1093 and 1188 still speak the v1 vendor wording and types). Your base is e-6's portal commit (the adapter that returns `OpalReportSection`).

**R4 The v2 form of AnalysisReport** (IRPT_BCKEND PRD v0.28 item 29, `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` section ADDENDUM v0.28). One contract with a `provider` member: `YCHARTS` carries exactly the v1 members. `OPAL_ENGINE` carries `request_ref`, `disclosures` and `release` as v1 and, in place of the vendor members: `opal_artifact` (`sha256`, `byte_length`, `generated_at`, `run_record_key`); `effective_inputs` with `holdings_fingerprint`, `settings`, `inputs_as_of` and no `read_back`; sections with `section_id`, `section_type`, `units`, `as_of_date`, `status` (`VALUE` or `NOT_AVAILABLE`), `reason`, `method`, `coverage`, `page` optional; `computation_validation` (`status`, `checks_run`, `checks_failed`, `notes`). Under `OPAL_ENGINE` the vendor members (`vendor_artifact`, `read_back`, `extraction_validation`) are ABSENT, never null and never defaulted; a consumer that needs one rejects the document. `NOT_AVAILABLE` carries a null value and a `reason` from the closed set in R2. v1 and its schema `_contracts/AnalysisReport.schema.json` (pinned @62301f71e0) are untouched.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: worker row IRPT_YCDGEN-W2-S14 in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md`; e-6's adapter in `contracts/adapt.ts` (`adaptAnalysisReport`, `adaptAnalysisReportSlice`, `OpalReportSection`) and its wire type in `contracts/wire/AnalysisReport.ts`; `tabs/analysis/NativeSections.tsx`; and e-6's exercise script `portal/scripts/adapt-analysis-report-opal-exercise.mjs` (read only: how it loads the adapter under bun).
- Baseline (measured by the issuer on unedited portal DEV): `bun test src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/tabs/analysis` is 40 pass, 11 fail BEFORE any edit (route table, response envelope and content pins). Your edit must not change those counts: 40 pass and 11 fail, the same 11. Do not try to fix them.
- Portal dev builds use port 5174 only; this cell needs no dev server. This is a product-file change: it lands on DEV through the issuer after the CTO's review, never by you.
- Encoding: ASCII only in code; no client figure and no secret in any committed file.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W4-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/NativeSections.tsx
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/contracts/wire/index.ts
portal/src/pages/InvestorReporting/contracts/wire/consumed.ts
portal/src/pages/InvestorReporting/contracts/wire/responses.ts
portal/src/pages/InvestorReporting/api/endpoints/investor-reporting.ts
portal/scripts/native-sections-opal-exercise.mjs
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- an Opal section list renders with method and coverage shown and none of the v1 vendor headings
- **AC2** -- a v1 section list renders with its headings and wording unchanged
- **AC3** -- the portal typechecks with zero errors, run through the exercise script

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-j-6"><invocation>bun portal/scripts/native-sections-opal-exercise.mjs opal</invocation><expect>^RESULT: opal PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-j-6"><invocation>bun portal/scripts/native-sections-opal-exercise.mjs v1</invocation><expect>^RESULT: v1 PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-j-6"><invocation>bun portal/scripts/native-sections-opal-exercise.mjs typecheck</invocation><expect>^RESULT: typecheck PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~4/IRPT_YCDGEN.TO-YCD-j-6.analysis-tab-opal-wording-and-types.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-j-6.analysis-tab-opal-wording-and-types`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~4`, first order; addendum B cell (decomposition IRPT_YCDGEN_DECOMP_R6B.md), cut by the issuer to disarm worker row W2-S14, which breaks the Opal page Andrew opens; stacked on e-6's UNLANDED portal commit 81bbeba2 (branch wk-IRPT_YCDGEN-67-portal), so e-6 and j-6 land on portal DEV together after the CTO's review. Portal submodule cell. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-05 ~23:3xZ):** worker 0.9.0_WK_IRPT_YCDGEN~4 workspace @c123fcc251 merged 1785e50b03 (proof and rows); the PORTAL candidate is commit cd3924d5 on portal branch wk-IRPT_YCDGEN-70-portal, stacked on e-6's 81bbeba2, and is NOT LANDED (product files: lands on portal DEV with e-6 after 1.0.0_SA_CTO's review). j-6.AC1-AC3 PASS at the worker (opal 22 of 22 legs, v1 13 of 13, typecheck exit 0), instance VALID; the portal test baseline holds (40 pass, 11 fail, the same 11 names as unedited DEV); a v1 render compared byte-identical against 81bbeba2. Row W2-S14 DISARMED by this cell. Rows W4-S7 (the endpoints client the order named at `portal/src/pages/InvestorReporting/api/endpoints/investor-reporting.ts` is really `portal/src/api/endpoints/investor-reporting.ts`; the order's path was the issuer's error, the file is unedited, lines 1093 and 1188 still declare `send<AnalysisReportWire,...>` and typecheck through the wider union) and W4-S8 (adapt.ts sets no `provider`, so the tab recognises the Opal form from `provider` or from every section being an Opal section, and an Opal report with zero sections would render the v1 wording; `consumed.ts` is GENERATED and the hand-added WIRE_CONSUMED_OPAL_FIELDS would drop on regeneration) are INERT for FWD-1 (the Overview has sections) and are carried to the CTO as portal-contract items.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6B_ARTIFACTS</workstream>
<slot>~4</slot>
<fabric>laptop</fabric>
