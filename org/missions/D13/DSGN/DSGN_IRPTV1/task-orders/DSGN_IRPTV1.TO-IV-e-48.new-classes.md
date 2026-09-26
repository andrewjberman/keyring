# TO DSGN_IRPTV1.TO-IV-e-48 -- C34: the Investor Reporting page maps UIR-50's structured and commodities classes, labelled and coloured

<to_id>DSGN_IRPTV1.TO-IV-e-48</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~31</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 (C34, UIR-50, FWD-23) | **Decomp cell:** `IV-e-48` (decomp v7 addendum 3; PRD C34) | **outcome_ref:** FWD-23, FWD-12/13 (O7) | **depends_on:** 2.0.0_SA_COO~P's contract enum (CLOUD d3c5467ce1 + ae32ac98d7, landed) | **slot:** ~31, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-48` -- PRD C34: UIR-50's portal half. Andrew's rule: a security the ETF Classifier tags keeps that class. The producer contract now
admits `structured` and `commodities` (the HoldingsSnapshot `asset_class` enum is equity, fixed_income, alternatives, structured,
commodities, cash, other, unclassified: `docs/contracts/investor-reporting/v1/`, CLOUD d3c5467ce1). No value is written yet: the data
producer (2.0.0_SA_COO~M) writes them only after this cell drains. Today the page folds them to "Unclassified":

- the generated wire union `contracts/wire/HoldingsSnapshot.ts` :104 lacks both values: regenerate the wire from the contract with the
  existing generator `__tests__/fe-s-13/gen-wire.ts` (run it; do not edit it) -- never hand-edit a generated file;
- `contracts/index.ts` :797 `assetClass?: 'equity' | 'fixedIncome' | 'alternatives' | 'cash' | 'unclassified' | 'other'`;
- `contracts/adapt.ts` `ASSET_CLASS_FOR_WIRE` :983 and :1005 (`?? 'unclassified'`);
- `tabs/holdings/assetClass.ts` `CLASS_FOR_SERVED` :36-43. `HoldingAssetClass` and `ASSET_CLASS_COLOR` already carry 'Structured' and
  'Commodities' with `ASSET_CLASS.structured` / `ASSET_CLASS.commodities` colours (:15-22).

**Build:** a served `structured` or `commodities` node renders as "Structured" / "Commodities" with its own colour everywhere the page
shows an asset class, never "Unclassified". Each colour is distinct from every other class colour and from every model colour
(`src/lib/modelPortfolioColors.ts`, read only): if an existing colour collides, file a surprise row naming both (the colour pass is
TO-IV-e-43's, later in round 7) rather than editing `src/lib`. Every other class maps exactly as today. The contract is the producer's:
the consumer admits exactly the contract's values and nothing more (CTO 101449's rule).

**Environment:** the portal worktree is based on DEV `6757223a`; the workspace worktree carries ~P's contract commit. Round-7 chains run in
parallel over other files (none of yours). The test file does not exist at the base: write it against a synthetic in-memory snapshot
(no real client figure, no firm token in the file). Do not start any server.

### ACCEPTANCE

<criterion id="IVE48-AC1" cell_refs="IV-e-48"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-31/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~31; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-48.new-classes.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: NEW-CLASSES-OK</expect></criterion>
`IVE48-AC1` -- the built behaviour with its control: a snapshot whose security nodes carry `structured` and `commodities` adapts to those
classes and renders "Structured" / "Commodities" with colours distinct from every other class and model colour; the generated wire union
equals the contract's enum; a snapshot with only today's classes adapts exactly as the base code does. Prints `VERDICT: NEW-CLASSES-OK`
only when every arm holds.

<criterion id="IVE48-AC2" cell_refs="IV-e-48" judgment="true"/>
`IVE48-AC2` -- graded at L9 by `3.0.0_SA_CVO` once ~M writes the values: a holdings view of a client holding a tagged structured or
commodities security shows its class by name and colour. RECORD; never self-graded.

<expected_criteria>IVE48-AC1, IVE48-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/public-status.ts`, `src/lib/**`,
  the generator and every other file are READ, never edited. A needed edit outside the grant is a surprise row, not an edit.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/contracts/wire/
portal/src/pages/InvestorReporting/contracts/index.ts
portal/src/pages/InvestorReporting/contracts/adapt.ts
portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-48.new-classes.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 3, cell `IV-e-48`.
<owned_cells>IV-e-48</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE48-AC1, IVE48-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~31/DSGN_IRPTV1.TO-IV-e-48.new-classes.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE48-AC1,IVE48-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W31-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 6757223a: contracts/index.ts :797, adapt.ts :983/:1005, wire/HoldingsSnapshot.ts :104, assetClass.ts :15-43; the contract enum at CLOUD d3c5467ce1 (~P 101600).
lane: the <paths> block IS the grant; disjoint from every running chain (S, P, H, slot ~30) and from IV-e-35 (tests and fixtures only). assetClass.ts is also TO-IV-e-43's (chain Z, which starts after this drains).
</preflight>

Seating: slot ~31, queue position 1 of 1; trigger per the agreed order (~D 101557, ~M 101576): ~P's enum landed -> C34 -> ~M writes values.
