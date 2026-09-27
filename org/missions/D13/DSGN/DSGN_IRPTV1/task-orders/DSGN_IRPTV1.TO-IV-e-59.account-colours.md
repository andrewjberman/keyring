# TO DSGN_IRPTV1.TO-IV-e-59 -- No two slices share a colour; no hue means both a model and an asset class (UIR-25, UIR-46, UIR-37)

<to_id>DSGN_IRPTV1.TO-IV-e-59</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~38</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>complete</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-59` (decomp v8) | **outcome_ref:** FWD-12, FWD-13 | **depends_on:** none | **slot:** ~38, queue position 1 of 3

---

## WORKER FACE

### THE CELL

`IV-e-59` -- Rows (verbatim, PRD v0.16): UIR-25 "No two slices in one chart share a colour." UIR-46 "As UIR-25." UIR-37 "No hue means both a model and an asset class; every Opal model draws its canonical colour."

On Holdings, the account-level pie gives all three account slices the same teal (window 9, w9c). `tabs/holdings/DrillTree.tsx`
`drillSliceColor` :286-290 sends ACCOUNT nodes to `modelSliceColor` :267-269, then `colorForSlice` :312-315, which uses the MODEL
palette's name match and hash; slice data is built at :504-507. `src/lib/modelPortfolioColors.ts` `getModelColor` :192-223 (partial
match, then an `EXTENDED_MODEL_COLORS` hash :143-150); the teal `#14b8a6` is the 50/50 INT/LT model colour (:69). Also involved:
`tabs/holdings/palette.ts` and `src/lib/chartColors.ts` `ASSET_CLASS` (:115). Commodities is `PALETTE.green900` (CTO 101681).

**Build:** Account slices draw from an ACCOUNT palette (a new ordered list in `tabs/holdings/palette.ts`) assigned by the slice's position
among its siblings, so no two slices in one chart share a colour. That palette shares no hue with any Opal model's canonical colour or
any `ASSET_CLASS` colour (UIR-37). Model slices keep their canonical colours; asset-class slices keep `ASSET_CLASS`. Do not edit
`src/lib/modelPortfolioColors.ts` or `src/lib/chartColors.ts` (read only).

**Environment:** the portal worktree is based on local DEV `3f76cdb2` (round 7 drained). Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

### ACCEPTANCE

<criterion id="IVE59-AC1" cell_refs="IV-e-59"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-38/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-59.slice-colours.test.ts 2>&1 | tail -15</invocation><expect>VERDICT: SLICE-COLOURS-OK</expect></criterion>
<criterion id="IVE59-AC2" cell_refs="IV-e-59" judgment="true"/>
`IVE59-AC2` -- judgment: UIR-25/46/37 read on the running page (round-8 walk), graded by 3.0.0_SA_CVO at L9. Record it in your instance as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

Each mechanical criterion prints its expect string only when every arm holds. AC1 arms: a three-account level gets three distinct colours; a 12-sibling level gets 12 distinct colours; no account colour equals any model canonical colour or any ASSET_CLASS colour; control: model and asset-class slices keep their colours.

<expected_criteria>IVE59-AC1, IVE59-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/palette.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-59.slice-colours.test.ts
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-59`.
<owned_cells>IV-e-59</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE59-AC1, IVE59-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-59.account-colours.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE59-AC1,IVE59-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W38-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~38, queue position 1 of 3; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 38 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).
