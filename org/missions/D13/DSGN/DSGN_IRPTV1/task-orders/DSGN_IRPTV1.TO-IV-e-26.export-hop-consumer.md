# TO DSGN_IRPTV1.TO-IV-e-26 -- FWD-9: the export hop's consumer side on P's written specs -- submit-export's data-less QUEUED/RUNNING answer; the print URL's selection and window

<to_id>DSGN_IRPTV1.TO-IV-e-26</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~16</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-25</issued_date>
<status>complete</status>
<round>4</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-26` (decomp v4 @d4add46f46) | **outcome_ref:** FWD-9 | **depends_on:** -- (chain 5) | **slot:** ~16, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-26` -- two written interface specs from the export producer `2.0.0_SA_COO~P`, landing on this project's consumer-side
surface (CTO 100919: `contracts/**`, wire included, is this project's; `portal/src/api/**` stays P's and is NOT in your grant).

**(a) submit-export (P 100960; schema `docs/contracts/investor-reporting/v1/responses/submit-export.response.schema.json`,
ruling R2).** While `status.state` is QUEUED or RUNNING the response may omit `data`; the export id then travels in
`status.operation.revision`. In every other state `data` (the ExportReceipt) is still required. Regenerate
`IR/contracts/wire/**` by running `IR/__tests__/fe-s-13/gen-wire.ts` (run it; do not edit it) and make `IR/export/submit.ts`
accept the data-less QUEUED/RUNNING answer, returning the export id from `status.operation.revision`; any other state
without `data` refuses by name.
**(b) The print URL (P 100987; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/EXPORT_HOP_DESIGN_CARD_20260924.md`
section B2-URL, READ it).** The render host opens `/investor-reporting/print?...&selection=<sel_>&start=&end=`. Today
`IR/render/PrintEntry.tsx` -> `IR/export/resolveBundle.ts` -> `getPerformanceReport` passes no accountSetId (it throws "An
accepted account selection is required") and sends start = end = businessAsOf. Make PrintEntry read `selection`, `start` and
`end` from the URL and resolveBundle pass them to `getPerformanceReport`; a missing one refuses by naming it, and no request
is made.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

**Environment (every cell):** the portal worktree is based on DEV `8242412d` (round 3 merged). Each criterion's test file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. The header's accepted selection reaches tab bodies through `IR/header/HeaderSelectionContext.ts` (wrap a render in `HeaderSelectionContext.Provider` to exercise it). Do not start any server: dev builds run on port 5174 only, and 5174 serves the main checkout, not your worktree.

### ACCEPTANCE

<criterion id="IVE26-AC1" cell_refs="IV-e-26"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~16; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.submit-data-optional.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SUBMIT-QUEUED-OK</expect></criterion>
`IVE26-AC1` -- submit.ts, fed a QUEUED and a RUNNING answer without `data`, returns the export id from status.operation.revision; fed a READY answer without `data`, refuses by name. The test prints `VERDICT: SUBMIT-QUEUED-OK` only when every arm holds.

<criterion id="IVE26-AC2" cell_refs="IV-e-26"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~16; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.print-url.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: PRINT-URL-OK</expect></criterion>
`IVE26-AC2` -- PrintEntry's URL parse plus resolveBundle, with a recording stub api, call getPerformanceReport once with accountSetId = the URL selection and the window = the URL start/end; with each one of the three missing in turn, no call is made and the refusal names the missing one. The test prints `VERDICT: PRINT-URL-OK` only when every arm holds.

<criterion id="IVE26-AC3" cell_refs="IV-e-26"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~16; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: WIRE-REGEN-OK</expect></criterion>
`IVE26-AC3` -- running gen-wire.ts leaves `IR/contracts/wire/**` byte-identical to the committed files (the regeneration is committed), the submit-export response type has `data` optional, and the fe-s-13 content pin still offers 17 of 17 operations. The test prints `VERDICT: WIRE-REGEN-OK` only when every arm holds.

<criterion id="IVE26-AC4" cell_refs="IV-e-26" judgment="true"/>
`IVE26-AC4` -- graded at the round-4 drain by `2.0.0_SA_COO~D` on the signed-in trace (IRPT_BCKEND principal IB-rtf-3, else Andrew's walk on `localhost:5174`), per CTO 100991 -- never the CVO: an advisor exports a Performance report and the printed page shows that client's window, or the refusal names what is missing (FWD-9 ACCEPT; the served route answers NOT_READY until P's B1 lands, graded from the live refusal). RECORD; never self-graded.

<expected_criteria>IVE26-AC1, IVE26-AC2, IVE26-AC3, IVE26-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` are
  OUT unless named below; the reference pages (`pages/ModelPortfolios/**`, `pages/Positioning/**`, `pages/Philosophy/**`,
  `pages/CapitalMarketAssumptions/**`) are read and copied from, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `8242412dde9a3ef807e118f648242cf24ffe2981`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (the naming-gate rule; row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/contracts/wire/
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/export/resolveBundle.ts
portal/src/pages/InvestorReporting/render/PrintEntry.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v4 @d4add46f46, cell `IV-e-26`.
<owned_cells>IV-e-26</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE26-AC1, IVE26-AC2, IVE26-AC3, IVE26-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~16/DSGN_IRPTV1.TO-IV-e-26.export-hop-consumer.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE26-AC1,IVE26-AC2,IVE26-AC3,IVE26-AC4` BEFORE the flip. `IVE26-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `2.0.0_SA_COO~D`'s drain trace (CTO 100991).
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W16-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v4 section 5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v4 -- every write path measured at portal DEV 8242412d at the cut (decomp v4 section 5).
lane: the <paths> block IS the grant; the write sets are pairwise disjoint (decomp v4 section 2).
</preflight>

Seating: slot ~16, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 16 --portal-ref 8242412dde9a3ef807e118f648242cf24ffe2981`.
