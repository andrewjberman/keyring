# IRPT_YCDGEN task order -- `YCD-p-6` -- ROUND 6 (THREAD): THE ANALYSIS TAB SENDS THE PICKED CLIENT'S OWN FIRM, NEVER AN EMPTY ONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6I.md</decomp_doc>
<owned_cells>YCD-p-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-p-6.analysis-tab-sends-picked-clients-firm</to_id>
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

### `YCD-p-6` -- the analysis tab sends the picked client's own firm, never an empty one (hops 8 Open (page wiring); FWD-1)
- `portal/src/pages/InvestorReporting/index.tsx` and `portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx`: R17.
- `portal/scripts/global-tenant-exercise.mjs` (new): takes one argument and prints one RESULT line. `global` drives the code path for a Global principal who picks a client whose firm is `cottonwood` and checks that BOTH the catalogue read and the submit carry `cottonwood` as the selected tenant (`RESULT: global PASS`); `refuse` drives the same path with no tenant and checks that no catalogue read is made, the submit is refused, and the page text says why in plain words (`RESULT: refuse PASS`); `typecheck` runs `tsc -b --noEmit` in the portal (`RESULT: typecheck PASS` only on exit 0).
- The portal is a git submodule: your worktree has a nested portal worktree cut from j-6's portal branch (commit cd3924d5); commit the `portal/...` files INSIDE it. No colour or layout change (the portal colour law binds).

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R17 The tenant sent with the catalogue read and the submit is the picked client's own firm.** For a principal in Global scope who has picked a client, `selectedScopeRef.selectedTenant` (`portal/src/pages/InvestorReporting/index.tsx`, around lines 222-228) is the firm tenant of that client's entry: the `firm.tenant` of the global firm context whose `verifiedRequestFirm.firmId` equals the picked row's `entry.firmId`; never empty, never the principal's own tenant. `GenerateComposer` (a) does not read the catalogue when it holds no tenant (`fetchCatalogue(scopeRef.selectedTenant)`, around lines 226-238) and (b) refuses to submit with no tenant and says on the page why, in plain words with no internal code. A single-firm (non-Global) context behaves exactly as before. Why (measured 2026-10-06 ~13:03Z): a Global principal picked a Cottonwood client and pressed Generate; the intake logged a catalogue read with no firm (`BucketUnmapped`) and the page showed 'Needs attention'. `tabs/analysis/ProspectComposer.tsx` lines 160-161 already carry the same guard (item 89) and are the pattern to follow.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `portal/src/pages/InvestorReporting/index.tsx` (`AuthenticatedWorkspace`, `SelectionWorkspace`, `selectedScope`, `selectedScopeRef`), `portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx` (`fetchCatalogue` use, `onGenerate`, how the submit takes its tenant), `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx` lines 150-170 (the guard to copy), and `portal/src/pages/InvestorReporting/contracts/adapt.ts` around line 751 (`registry_tenant` is optional on the wire).
- Do not guess the cause: measure it first in the exercise script (print, for a Global principal who picked a client, what `selectedScope.registryTenant` and the global firm's `tenant` hold), then fix the one place it is lost. Record what you measured in your report.
- The firm selector showing Global after a client is picked is expected for a Global principal; do not change that.
- Baseline (measured by the issuer on unedited portal DEV): `bun test src/pages/InvestorReporting/__tests__/fe-s-13 src/pages/InvestorReporting/tabs/analysis` is 40 pass, 11 fail BEFORE any edit. Your edit must not change those counts: 40 pass and 11 fail, the same 11. Do not try to fix them. State the counts after your edit in your report.
- Portal dev builds use port 5174 only; this cell needs no dev server. This is a product-file change: it lands on DEV through the issuer after the CTO's review, never by you.
- Encoding: ASCII only in code; no client figure and no secret in any committed file.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W2-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx
portal/scripts/global-tenant-exercise.mjs
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a Global principal who picks a Cottonwood client sends cottonwood on both the catalogue read and the submit
- **AC2** -- with no tenant the composer reads no catalogue, refuses to submit and says why in plain words
- **AC3** -- the portal typechecks with zero errors, run through the exercise script

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-p-6"><invocation>bun portal/scripts/global-tenant-exercise.mjs global</invocation><expect>^RESULT: global PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-p-6"><invocation>bun portal/scripts/global-tenant-exercise.mjs refuse</invocation><expect>^RESULT: refuse PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-p-6"><invocation>bun portal/scripts/global-tenant-exercise.mjs typecheck</invocation><expect>^RESULT: typecheck PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~2/IRPT_YCDGEN.TO-YCD-p-6.analysis-tab-sends-picked-clients-firm.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-p-6.analysis-tab-sends-picked-clients-firm`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~2`, first order; addendum I cell (decomposition IRPT_YCDGEN_DECOMP_R6I.md), cut on CTO ruling msg 105563 after the F1 walk of 2026-10-06 ~13:03Z; stacked on j-6's UNLANDED portal commit cd3924d5 (branch wk-IRPT_YCDGEN-70-portal), so e-6, j-6 and this cell land on portal DEV together after the CTO's review. Portal submodule cell. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-06 ~14:2xZ):** worker 0.9.0_WK_IRPT_YCDGEN~2 workspace @19937bf72e merged 83df582608 (proof and row W2-S16); the PORTAL candidate is commit e107538d on portal branch wk-IRPT_YCDGEN-81-portal, stacked on j-6's cd3924d5, and is NOT LANDED (product files: lands on portal DEV with e-6 and j-6 after 1.0.0_SA_CTO's review). p-6.AC1-AC3 PASS at the worker and re-run by the issuer in the worktree (global 11 of 11 checks, refuse 6 of 6, typecheck exit 0); the portal test baseline holds (40 pass, 11 fail; the worker did not run the unedited tree, so 'the same 11' rests on the counts). The worker's measurement: on the served-wire fixture the picked client's scope already holds its firm; the empty tenant comes from the composer's mount-time read and submit made with the bootstrap scopeRef that has no selectedTenant. The live wire of the 13:03Z walk was not read, so the fix is proven against the fixture, not yet against Andrew's live click (that is F1's retry).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6I_GLOBAL_TENANT</workstream>
<slot>~2</slot>
<fabric>laptop</fabric>
