# IRPT_YCDGEN task order -- `YCD-q-6` -- ROUND 6 (THREAD): THE PROSPECT CARD NAMES THE FIRM IT IS FOR, THE FIRM DROPDOWN LISTS REAL OPTIONS, AND THE STAGED UPLOAD SURVIVES A REMOUNT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6J.md</decomp_doc>
<owned_cells>YCD-q-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-q-6.prospect-card-names-its-firm</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~3</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-q-6` -- the prospect card names the firm it is for, the firm dropdown lists real options, and the staged upload survives a remount (hops 8 Open (page wiring); FWD-1)
- `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`, `portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx`, `portal/src/pages/InvestorReporting/tabs/analysis/stagedProspect.ts` (new), `portal/src/pages/InvestorReporting/header/FirmDropdown.tsx` and `portal/src/pages/InvestorReporting/index.tsx`: R18.
- `portal/scripts/prospect-firm-exercise.mjs` (new): takes one argument and prints one RESULT line. `firm` drives the Prospect card for an internal principal with NO client picked: with Cottonwood chosen on the card, the upload request and the submit request both carry `cottonwood` as the selected tenant, and with no firm chosen the card sends nothing and shows its plain-words refusal (`RESULT: firm PASS` only when both hold); `dropdown` builds the Firm dropdown's options for an internal principal after a single firm has been chosen and checks the options are Global plus every catalogue firm and that the value is one of them (`RESULT: dropdown PASS`); `remount` stages a file and a review result, remounts the composer as a client pick or tab switch does, checks both are still there, then checks a change of the card's firm clears them (`RESULT: remount PASS`).
- The portal is a git submodule: your worktree has a nested portal worktree cut from p-6's portal branch (commit e107538d); commit the `portal/...` files INSIDE it. No colour or layout change beyond the added firm control and its refusal text (the portal colour law binds).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R18 The Prospect card names its firm.** (a) For an internal (Opal) principal the Prospect card shows a firm choice (the real firm options, from the same catalogue the Firm dropdown uses); it is preselected to the Firm dropdown's firm when that is not Global, and the card refuses to upload, saying in plain words why, while no firm is chosen. The chosen firm's tenant is sent as `selected_tenant` on the upload (`analysis-input-upload`), on the submit (`analysis-requests`) and on the comparison catalogue read; for a single-firm principal the card behaves exactly as before. (b) The Firm dropdown lists Global plus every firm of the catalogue at all times, so the selected value is always one of its options and it never shows 'Global (All)' while the page is single-firm. (c) A staged file and its review result are held in memory above the keyed composer (a module-level store in the new `stagedProspect.ts`, never browser storage, never serialised) so a client pick or a tab switch does not discard them; a change of the card's firm or the explicit choice of a different file clears them. Client data never leaves memory. Why (measured 2026-10-06): the no-client upload sent no `selected_tenant` (`header/search.ts:420-426` `scopeRefFrom` never sets it; `AnalysisTab.tsx:266`), the server refuses an owner firm of `global` or `opal-capital` (`intake/uploads.py:170-177`), the dropdown's options come from `globalContext?.firms ?? []` (`index.tsx:351`) which is empty once a firm is chosen, and `ProspectComposer` is keyed on `firmId:scopeFingerprint:revision` (`AnalysisTab.tsx:265`) under a tab keyed on the whole scope (`TabShell.tsx:165`).

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` (state, `upload()` at about 235-260, `selectedTenant` prop at about 77, the item-89 guard at about 160), `portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx` (lines 60-66 and 258-270), `portal/src/pages/InvestorReporting/index.tsx` (lines 92-127 and 340-355), `portal/src/pages/InvestorReporting/header/FirmDropdown.tsx` (lines 78-102), `portal/src/pages/InvestorReporting/header/firm.ts` and `portal/src/pages/InvestorReporting/header/search.ts` (`scopeRefFrom`), and the route table in `portal/src/api/endpoints/investor-reporting.ts` (about 205-232).
- The catalogue of firms the Firm dropdown needs already exists: the query at `index.tsx:96-102` (enabled only while `firmId === 'global'`; make it available for the whole session) returns the Global context whose `firms[].tenant` are the firm tenants; display names come from `firmDisplayNameFor`. The Global firm option's id is `GLOBAL_FIRM_OPTION.id`.
- The firm sent must be a registry tenant such as `cottonwood` (the same value the picked-client path sends, `selected_tenant=cottonwood`), never an opaque firm id.
- Staged file bytes are client data: keep them in memory only, in the new store; no `localStorage`, `sessionStorage`, IndexedDB, query cache, console print or serialisation.
- The picked-client path (GenerateComposer, p-6) and the single-firm principal path must behave exactly as before; do not change `GenerateComposer.tsx`.
- Do not guess: measure each defect first in the exercise script (print what the card sends today with no client picked), and say what you measured in your report.
- Baseline (measured by the issuer): `bun test src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/tabs/analysis`, run from the portal directory of a worktree, is 40 pass and 11 fail BEFORE your edit, the same 11 at the base. Your edit must not change those counts. State them after your edit.
- Portal dev builds use port 5174 only and it is already held by another seat; do NOT start a dev server. This is a product-file change: it lands on DEV through the issuer after the CTO's review, never by you.
- Encoding: ASCII only in code; no client figure and no secret in any committed file.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W3-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx
portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx
portal/src/pages/InvestorReporting/tabs/analysis/stagedProspect.ts
portal/src/pages/InvestorReporting/header/FirmDropdown.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/scripts/prospect-firm-exercise.mjs
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the Prospect card with no client picked sends the chosen firm on the upload and the submit, and with no firm chosen sends nothing and says why
- **AC2** -- after a single firm is chosen the Firm dropdown still lists Global plus every catalogue firm and its value is one of them
- **AC3** -- a staged file and its review result survive a remount and are cleared by a change of firm

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-q-6"><invocation>bun portal/scripts/prospect-firm-exercise.mjs firm</invocation><expect>^RESULT: firm PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-q-6"><invocation>bun portal/scripts/prospect-firm-exercise.mjs dropdown</invocation><expect>^RESULT: dropdown PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-q-6"><invocation>bun portal/scripts/prospect-firm-exercise.mjs remount</invocation><expect>^RESULT: remount PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~3/IRPT_YCDGEN.TO-YCD-q-6.prospect-card-names-its-firm.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-q-6.prospect-card-names-its-firm`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~3`, first order; addendum J cell (decomposition IRPT_YCDGEN_DECOMP_R6J.md), cut on CTO ruling msg 105720 and Andrew-direct 2026-10-06 (the Prospect card asks for a firm because it is produced for a given firm inherently); stacked on p-6's UNLANDED portal commit e107538d (branch wk-IRPT_YCDGEN-81-portal), so e-6, j-6, p-6 and this cell land on portal DEV together after the CTO's review. The issuer also runs the portal typecheck and the bun baseline at the drain. Portal submodule cell. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~G2, 2026-10-07 ~07:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~3 @215c317f77 (proof + rows W3-S19, W3-S20, W3-S21) merged to CLOUD by safe-merge @710c9129ab; proof-of-spec-check VALID (rc=0) at HEAD. AC1-AC3 PASS were re-run by 2.0.0_SA_COO~Y at the worker's worktree (handoff @217963b67d). The portal code is commit 643b6ddd on portal branch wk-IRPT_YCDGEN-82-portal (on origin); it is UNLANDED on portal DEV, and that landing is a CTO product-file review, not this order.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6J_PROSPECT_FIRM</workstream>
<slot>~3</slot>
<fabric>laptop</fabric>
