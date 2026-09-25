# TO DSGN_IRPTV1.TO-IV-e-15 -- FWD-17: a marked sample of each tab before a client is chosen

<to_id>DSGN_IRPTV1.TO-IV-e-15</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~10</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>complete</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-15` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-17 | **depends_on:** -- (chain D head) | **slot:** ~10, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-15` -- PRD v0.6 candidate C23. `IR/tabs/TabShell.tsx` today renders a one-line "select a client" box for
Performance and Holdings. Replace it with `IR/tabs/SampleView.tsx` (new): for each tab, the eye-catching components (a
headline, one chart, one card) rendered from a built-in SAMPLE data set clearly marked "Sample" on every component, with ONE
prompt to choose a client. No sample value may equal a real client's number: build the sample from round numbers, never
from a fixture file of real data.

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE15-AC1" cell_refs="IV-e-15"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-15.sample-performance.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SAMPLE-PERFORMANCE-OK</expect></criterion>
`IVE15-AC1` -- with no selection the Performance tab renders the sample headline and chart, each marked Sample, and exactly one choose-a-client prompt. The test prints `VERDICT: SAMPLE-PERFORMANCE-OK` only when every arm holds.

<criterion id="IVE15-AC2" cell_refs="IV-e-15"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-15.sample-holdings.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SAMPLE-HOLDINGS-OK</expect></criterion>
`IVE15-AC2` -- with no selection the Holdings tab renders the sample hero and map, each marked Sample, and exactly one prompt. The test prints `VERDICT: SAMPLE-HOLDINGS-OK` only when every arm holds.

<criterion id="IVE15-AC3" cell_refs="IV-e-15"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~10; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-15.sample-provenance.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: SAMPLE-NOT-REAL-OK</expect></criterion>
`IVE15-AC3` -- every sample figure comes from SampleView's own constant (no fixture import); the markup carries the word Sample on each sample component. The test prints `VERDICT: SAMPLE-NOT-REAL-OK` only when every arm holds.

<criterion id="IVE15-AC4" cell_refs="IV-e-15" judgment="true"/>
`IVE15-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: an advisor landing with no client sees what each tab will show, and nothing could be mistaken for a real client's numbers (FWD-17 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE15-AC1, IVE15-AC2, IVE15-AC3, IVE15-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/tabs/SampleView.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-15`.
<owned_cells>IV-e-15</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE15-AC1, IVE15-AC2, IVE15-AC3, IVE15-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~10/DSGN_IRPTV1.TO-IV-e-15.sample-view.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE15-AC1,IVE15-AC2,IVE15-AC3,IVE15-AC4` BEFORE the flip. `IVE15-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W10-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~10, queue position 1 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 10 --portal-ref <portal_ref at the cut>`.
