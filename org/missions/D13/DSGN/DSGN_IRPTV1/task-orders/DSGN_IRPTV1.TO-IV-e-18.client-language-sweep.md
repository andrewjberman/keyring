# TO DSGN_IRPTV1.TO-IV-e-18 -- JOIN 1 -- FWD-15 + FWD-11: client language on every body; the census with its retained-facts control

<to_id>DSGN_IRPTV1.TO-IV-e-18</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~11</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>3</round>
<risk>LOCAL</risk>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-18` (decomp v3 @2af10e4cd0) | **outcome_ref:** FWD-15, FWD-11 | **depends_on:** chains A, B, C, D landed | **slot:** ~11, queue position 1 of 3

---

## WORKER FACE

### THE CELL

`IV-e-18` -- PRD candidates C20 + C14, provisioned off DEV's tip after chains A-D land. Move off every tab body
into disclosures: the status band's state word and reason code (`OK [code not defined by the v1 contract]`; wrap
`IR/tabs/reporting/AnswerStatus.tsx` at its mounts, never edit it), the "Basis:" chip, the firm-attribution chip
(`IR/global/FirmAttribution.tsx`, a ruled touch), the accounts table's "PERIOD:" labels, and any `sel_`/`acc_`/revision
string. Re-scope `IR/__tests__/fe-s-5/fields.test.ts` to the PRD (account ids never print; formatted currency and the header
help tip count as reached), citing CTO 100865. Build a DOM census over the three bodies at 1440 with the disclosures as the
positive control (every moved fact found there).

**The rules:** the FE derives nothing -- every figure is a wire fact; "not supplied", never zero; ids never print; a fact moves to a disclosure, it does not vanish; colour is keyed by code or served class, never a label substring or a guess; DESIGN.md governs (C1-C12).

### ACCEPTANCE

<criterion id="IVE18-AC1" cell_refs="IV-e-18"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-18.census.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: BODIES-CLEAN</expect></criterion>
`IVE18-AC1` -- over Performance, Holdings and Analysis bodies: zero state tokens, reason codes, revisions, `sel_`/`acc_` ids (printed per body with the denominator of text nodes scanned). The test prints `VERDICT: BODIES-CLEAN` only when every arm holds.

<criterion id="IVE18-AC2" cell_refs="IV-e-18"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-18.retained.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: FACTS-RETAINED</expect></criterion>
`IVE18-AC2` -- every fact the census removed is found in a disclosure (help tip, popover, row hover) -- printed fact by fact. The test prints `VERDICT: FACTS-RETAINED` only when every arm holds.

<criterion id="IVE18-AC3" cell_refs="IV-e-18"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~11; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-18.fields-rescope.test.ts 2>&1 | tail -25</invocation><expect>VERDICT: FIELDS-RESCOPED-OK</expect></criterion>
`IVE18-AC3` -- fe-s-5/fields passes on its three firm fixtures under the re-scoped rule, and its re-scope cites CTO 100865. The test prints `VERDICT: FIELDS-RESCOPED-OK` only when every arm holds.

<criterion id="IVE18-AC4" cell_refs="IV-e-18" judgment="true"/>
`IVE18-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the real run on `localhost:5174` (main portal checkout) the COO takes at the drain: an advisor reads every heading and label on a real client's page and asks no engineer what one means (FWD-15 ACCEPT). RECORD; never self-graded.

<expected_criteria>IVE18-AC1, IVE18-AC2, IVE18-AC3, IVE18-AC4</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/reporting/
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/global/FirmAttribution.tsx
portal/src/pages/InvestorReporting/__tests__/fe-s-5/fields.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v3 @2af10e4cd0, cell `IV-e-18`.
<owned_cells>IV-e-18</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE18-AC1, IVE18-AC2, IVE18-AC3, IVE18-AC4. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~11/DSGN_IRPTV1.TO-IV-e-18.client-language-sweep.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE18-AC1,IVE18-AC2,IVE18-AC3,IVE18-AC4` BEFORE the flip. `IVE18-AC4` recorded
`UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W11-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v3 as the gate register (decomp section 5); this cell owes none of its four entries.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v3 on PRD v0.6 (10/10 commits verified; 12 paths, 11 stable, 1 flagged -> F1).
lane: the <paths> block IS the grant; ruled touches are named in decomp v3 section 2.
</preflight>

Seating: slot ~11, queue position 1 of 3; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 11 --portal-ref <portal_ref at the cut>`.
