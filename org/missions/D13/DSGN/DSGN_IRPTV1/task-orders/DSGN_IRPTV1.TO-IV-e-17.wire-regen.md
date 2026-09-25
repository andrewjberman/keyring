# TO DSGN_IRPTV1.TO-IV-e-17 -- REPAIR: gen-wire renders oneOf alternatives; the wire types regenerated; the bridge types dropped

<to_id>DSGN_IRPTV1.TO-IV-e-17</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~9</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-17` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-7, FWD-5, FWD-13 | **depends_on:** IV-e-14 (chain C) | **slot:** ~9, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-17` -- the gap the FAST interval exposed. `IR/__tests__/fe-s-13/gen-wire.ts` throws
`UnrenderableSchemaError` at `AnalysisUploadRequest.schema.json#/alternatives/0` (a oneOf of object alternatives).
**(a)** Teach the generator to render a oneOf/anyOf of object alternatives as a TypeScript union, loudly (no `unknown`).
**(b)** Regenerate `IR/contracts/wire/**` from the workspace's `docs/contracts/investor-reporting/v1/` (CLOUD carries P's
template lane @aa21133b67, the OPAL_ENGINE provider @69cac32dce and the HoldingsSnapshot members @7251000daa / a73241ef66):
this project's write surface (CTO 100919, PRD v0.7), landing on P's written asks (100861, 100893). **(c)** Drop the bridge: `TemplateUploadRequest` /
`UploadState` in `IR/tabs/analysis/prospect.ts` read the generated types; the members' casts in `IR/contracts/adapt.ts`
read the generated wire fields.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE17-AC1" cell_refs="IV-e-17"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~9; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-17.gen-oneof.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: GEN-ONEOF-OK</expect></criterion>
`IVE17-AC1` -- the generator renders a planted two-alternative oneOf as a union of both object types and throws for a genuinely unrenderable schema. The test prints `VERDICT: GEN-ONEOF-OK` only when every arm holds.

<criterion id="IVE17-AC2" cell_refs="IV-e-17"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~9; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-17.regenerated.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: REGENERATED-OK</expect></criterion>
`IVE17-AC2` -- the generated AnalysisUploadRequestWire admits file_base64 + file_type, AnalysisUploadResultWire admits RESOLVING, PerformanceReport provider admits OPAL_ENGINE, HoldingsSnapshot nodes admit the four members; `bun run typecheck` is 0. The test prints `VERDICT: REGENERATED-OK` only when every arm holds.

<criterion id="IVE17-AC3" cell_refs="IV-e-17"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~9; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-17.bridge-dropped.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: BRIDGE-DROPPED-OK</expect></criterion>
`IVE17-AC3` -- prospect.ts and adapt.ts carry no `as unknown as` cast for these fields; the fe-s-13 content pin still offers 17 of 17 routes and operations. The test prints `VERDICT: BRIDGE-DROPPED-OK` only when every arm holds.

<criterion id="IVE17-AC4" cell_refs="IV-e-17" judgment="true"/>
`IVE17-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: none beyond the mechanical arms; the grader reads the regenerated diff for stray hand edits. RECORD; never self-graded.

<expected_criteria>IVE17-AC1, IVE17-AC2, IVE17-AC3, IVE17-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `13b5356fad4779b990e8e7a88636430204b30e42`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-13/gen-wire.ts
portal/src/pages/InvestorReporting/contracts/wire/
portal/src/pages/InvestorReporting/tabs/analysis/prospect.ts
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-17`.
<owned_cells>IV-e-17</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE17-AC1, IVE17-AC2, IVE17-AC3, IVE17-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~9/DSGN_IRPTV1.TO-IV-e-17.wire-regen.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE17-AC1,IVE17-AC2,IVE17-AC3,IVE17-AC4` BEFORE the flip. `IVE17-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W9-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~9, queue position 2 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 9 --portal-ref <portal_ref at the cut>`.
