# TO DSGN_IRPTV1.TO-IV-e-70 -- Asset-class colours keep a named distance from every Opal model colour; distinct account colours at 4+ accounts (UIR-37, UIC-11)

<to_id>DSGN_IRPTV1.TO-IV-e-70</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~38</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E4 | **Decomp cell:** `IV-e-70` (decomp v9) | **outcome_ref:** FWD-12, FWD-13, FWD-21 | **depends_on:** none | **slot:** ~38, queue position 1 of 3

---

## WORKER FACE

### THE CELL

`IV-e-70` -- Rows (acceptance lines verbatim, PRD v0.18): UIR-37 "No hue means both a model and an asset class; every Opal model draws its canonical colour."; UIC-11 "Adjacent slices are distinguishable at a glance (a palette with enough separation for 11+ accounts)."

CTO ruling UIR-37 (analysis section 2): the Opal MODEL colours are fixed (FWD-12: each model wears the colour it wears on Model Portfolios); the ASSET-CLASS palette yields. `src/lib/modelPortfolioColors.ts` stays read-only. UIC-11: the account palette (`tabs/holdings/palette.ts` ACCOUNT_PALETTE :40-55, 14 greys) is not distinguishable at 11+ accounts.

**Build:** Change `src/lib/chartColors.ts` ASSET_CLASS entries whose hue sits within a stated distance of any Opal model colour (state the distance rule, e.g. CIEDE2000 dE < N, in the file). List every other page that consumes the changed entries in your result (the change reaches them consistently). Give the account palette enough separation for 11+ accounts, sharing no hue with a model or asset-class colour. Add a test that FAILS when any asset-class colour falls within the distance of a model colour.

**Amendment 1 (issuer ruling, 2026-09-28 ~13:2xZ, on row W38-S4):** the ASSET_CLASS registry carries a second STANDING invariant that
this cell must also keep: `ASSET_CLASS.commodities` (green900, CTO 101649/101681, cells IV-e-49/IV-e-51) clears CIEDE2000 dE00 >= 20 from
every other MIX_PIE, ASSET_CLASS and model-primary colour, re-measured live by
`src/pages/AdvisorIntelligence/__tests__/iv-e-49.commodities-distance.test.ts` and `iv-e-51.commodities-chromatic.test.ts`. Under UIR-37
the asset-class palette yields to the MODEL colours only; it does not yield commodities' ratified colour. So pick the moved entries
(fixedIncome and any other) to satisfy BOTH bars at once -- a hue outside the green family is allowed. `ASSET_CLASS.commodities` and both
AdvisorIntelligence tests are read and run, never edited.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE70-AC1" cell_refs="IV-e-70"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-38/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-70.model-class-colour.test.ts 2>&1 | tail -20</invocation><expect>VERDICT: MODEL-VS-CLASS-COLOUR-OK</expect></criterion>
`IVE70-AC1` -- the built behaviour: (a) no ASSET_CLASS colour within the stated distance of any model colour (the test fails if one is moved back); (b) 12 sibling accounts get 12 distinguishable colours, none a model or class colour; control: model colours byte-identical to modelPortfolioColors.ts. Print `VERDICT: MODEL-VS-CLASS-COLOUR-OK` only when every arm holds.
<criterion id="IVE70-AC2" cell_refs="IV-e-70" judgment="true"/>
`IVE70-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<criterion id="IVE70-AC3" cell_refs="IV-e-70"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/AdvisorIntelligence/__tests__/iv-e-49.commodities-distance.test.ts ./src/pages/AdvisorIntelligence/__tests__/iv-e-51.commodities-chromatic.test.ts 2>&1 | tail -6</invocation><expect>0 fail</expect></criterion>
`IVE70-AC3` -- control (amendment 1): the two ratified commodities tests pass UNEDITED against the changed registry. At the base they pass;
with fixedIncome at green700 they fail 2 of 8 (row W38-S4).

<expected_criteria>IVE70-AC1, IVE70-AC2, IVE70-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/lib/chartColors.ts
portal/src/pages/InvestorReporting/tabs/holdings/palette.ts
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-70.model-class-colour.test.ts
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-70`.
<owned_cells>IV-e-70</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE70-AC1, IVE70-AC2, IVE70-AC3. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-70.model-vs-class-colour.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE70-AC1,IVE70-AC2,IVE70-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W38-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3b98939b (org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md, @51ec23d744); CTO analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md @071e09aa18.
lane: the <paths> block IS the grant; disjoint from every parallel round-9 chain (decomp v9 table).
</preflight>

Seating: slot ~38, queue position 1 of 3; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 38 --path <abs> --portal-ref <DEV at seating>`.
