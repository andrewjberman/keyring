# IRPT_YCDGEN task order -- `YCD-v-6` -- ROUND 6 (THREAD): THE ANALYSISREPORT WIRE TYPE IS GENERATED FROM V2

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6L.md</decomp_doc>
<owned_cells>YCD-v-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-v-6.analysisreport-wire-type-is-generated-from-v2</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~6</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a portal type and consumer change; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the gap was measured by the u-6 proof instance c73a029dc3 and row IRPT_YCDGEN-D2-W6-S1
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT) -- the Analysis report made in house, Opal-branded, with no YCharts call. Work ONLY in the worktree
your spawn line names; every path below is relative to that root. No vendor call, no AWS call, no deploy.

**RULES THAT BIND THIS ORDER (verbatim, from the dell2 CTO and Andrew):**
- "Never `bun install`. Provision a worktree only with `wk-provision.sh --node-modules link` (it links C:\dev\ajb_workspace\portal\node_modules, the kit tree) or `none`. The rest of 106215 stands: bun only inside a portal tree holding node_modules, always --no-install, no registry-reaching probe."
- "research browsing only when necessary; no packages, no installs, no file fetched onto the box."

## 1. YOUR CELL (inlined from decomposition R6L revision 1.1)

### `YCD-v-6` -- the committed AnalysisReport wire type IS the generator's output from v2 (portal consumer hop; FWD-1)
Your previous order YCD-u-6 moved the generator's AnalysisReport source to the served v2 schema (portal dc88c4f7). Its AC2 failed
because the committed `portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts` is HAND-SHAPED: `export interface
AnalysisReportWire` with an optional `provider`, plus hand-added `AnalysisSectionNotAvailableReason`, `AnalysisReportOpalSectionWire`,
`AnalysisReportOpalWire`, `AnalysisReportAnyWire`; the generator emits one union `AnalysisReportWire = {YCHARTS} | {OPAL_ENGINE}`.
The producer defines and the consumer conforms (gen-wire.ts header), so the CONSUMERS move, not the schema or the generator.
- Regenerate `contracts/wire/AnalysisReport.ts` with the changed generator so the committed file IS its output (render only that
  file; do not rewrite any other file under `contracts/wire/`).
- Migrate every portal consumer of the hand-added names or of the interface shape to the generated union, keeping each consumer's
  behaviour. Known readers: `contracts/adapt.ts`, `contracts/index.ts`, `src/api/endpoints/investor-reporting.ts`,
  `__tests__/mvp-selection/coverage.test.ts`; find the rest with a search whose denominator you print. Where a consumer needs a
  narrowed type, derive it from the generated union (`Extract<AnalysisReportWire, {provider: 'OPAL_ENGINE'}>`, indexed access) in
  the consumer's own file, never in `contracts/wire/`.
- Commit inside the portal submodule (branch wk-IRPT_YCDGEN-6-portal) first, then the submodule pointer in the outer worktree.
- AMENDMENT 1 (issuer ruling on row IRPT_YCDGEN-D2-W6-S3): your first proof instance (94a0e10d39) measured that
  `renderModule` in `portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts` emits `export interface X {..} | {..}`
  for a union body (it picks `interface` whenever the body starts with `{` and ends with `}`), which is not TypeScript. Fix THAT
  rule only: a body that is a top-level union renders as `export type X = ...`; every other contract's output stays byte-equal
  (prove it: render all contracts before and after your edit to a temp dir and diff; only AnalysisReport may change). Regenerate
  `contracts/wire/AnalysisReport.ts`. Then edit `contracts/wire/index.ts` and `contracts/wire/responses.ts` ONLY where they name
  the hand-added AnalysisReport types, so they reference the generated union (other lines of those two files are another
  workstream's; leave them byte-equal). Never run a test or command that writes into the real `contracts/wire/` other than your
  own edits (the iv-e-26 test calls `generate()`: run the suite only in temp copies, as your v6_checks.py now does).

## 2. THE CONTRACT YOU BUILD AGAINST

**R20 The committed AnalysisReport wire type IS the generator's output from v2.** The committed file equals the generated one
(header excluded), every consumer reads the generated union, the portal typechecks, and its InvestorReporting tests pass as they did.

## 3. WHAT YOU NEED TO KNOW

- `u6_checks.py regen` (your previous order's script, path below) already compares generated vs committed bodies; reuse it.
- Typecheck and tests: from inside `portal/`, `bun --no-install` only. Read `portal/package.json` for the script names.
- If a consumer cannot keep its behaviour on the generated union, file a row naming the consumer and the line; do not edit a schema,
  the generator, or any other contract's file to force it.
- ASCII only in new text. No client figure and no secret in any committed file.

## 4. SURFACES AND BOUNDS

NEVER: a vendor call, any AWS call, a deploy, a `bun install`, a package fetch, a schema edit, a gen-wire.ts edit beyond the union rule above. A check you cannot
satisfy inside your `<paths>` is a surprise row appended to
`org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `IRPT_YCDGEN-D2-W6-S<k>`, next unused k;
`fabric` "dell2"; `surfaced_at` the real UTC time).

<paths>
portal
portal/src/pages/InvestorReporting/contracts/wire/AnalysisReport.ts
portal/src/pages/InvestorReporting/contracts/wire/index.ts
portal/src/pages/InvestorReporting/contracts/wire/responses.ts
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/api/endpoints/investor-reporting.ts
portal/src/pages/InvestorReporting/__tests__/mvp-selection/coverage.test.ts
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/v6_checks.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/IRPT_YCDGEN.TO-YCD-v-6.analysisreport-wire-type-is-generated-from-v2.proof_of_spec.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the generator's AnalysisReport body equals the committed one (header excluded)
- **AC2** -- the portal typecheck passes with the migrated consumers
- **AC3** -- every portal InvestorReporting test that passes at d1b21c97 still passes

`v6_checks.py` (new): one argument (`typecheck` or `tests`), one RESULT line; `tests` runs the InvestorReporting test set at portal
d1b21c97 and at your HEAD and passes only when nothing green there is red here (print both counts).

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-v-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/u6_checks.py regen</invocation><expect>^RESULT: regen PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-v-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/v6_checks.py typecheck</invocation><expect>^RESULT: typecheck PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-v-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/v6_checks.py tests</invocation><expect>^RESULT: tests PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Commit, then write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~6/IRPT_YCDGEN.TO-YCD-v-6.analysisreport-wire-type-is-generated-from-v2.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-v-6.analysisreport-wire-type-is-generated-from-v2`, check it with
`python .tools/proof-of-spec-check.py <instance>`, and commit it. Report once: each criterion's verdict line with the output above it;
consumers migrated (with the search denominator); files written; rows filed. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~G2):** decomposition R6L revision 1.1, cut on the u-6 proof instance c73a029dc3 (AC2 FAIL, row
D2-W6-S1). Keeps CTO~DELL2 ruling msg 1250's AC2 intact: this cell makes the committed type the generated one, then u-6's AC2 is
re-run. Chain `~6`, same worker and worktree (C:/dev/wk-ycdgen-u6), after u-6's generator edit. fanout: 1 of 1 chain, cap 8. Risk
SERVED: portal product files change; nothing deploys; the candidate goes to 1.0.0_SA_CTO~DELL2 before portal DEV.

<round>6</round>
<workstream>R6L_ANALYSISREPORT_WIRE</workstream>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
**AMENDMENT 1 2026-10-08 (2.0.0_SA_COO~G2, issuer):** ruling on row IRPT_YCDGEN-D2-W6-S3 (ARMED, disarm owner this seat): the
generator's union rendering is a defect inside this decomposition; paths granted: gen-wire.ts (the union rule only, other contracts
byte-equal), contracts/wire/index.ts and responses.ts (only the AnalysisReport names). Criteria unchanged. This amendment is the
disarm: the portal branch is not drained until AC2 and AC3 pass. Gate limb: none graded this modification (modified order; no
placeholders). u-6 stays open until its AC2 is re-run on the fixed generator.

<status>complete</status>
