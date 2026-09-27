# TO DSGN_IRPTV1.TO-IV-e-71 -- The strategy drill names the account with the header tail and mask; ALL CATEGORIES draws no one-slice pie (UIR-32/34/49)

<to_id>DSGN_IRPTV1.TO-IV-e-71</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~38</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E2 | **Decomp cell:** `IV-e-71` (decomp v9) | **outcome_ref:** FWD-14, FWD-6 | **depends_on:** IV-e-70 (same slot) | **slot:** ~38, queue position 2 of 3

---

## WORKER FACE

### THE CELL

`IV-e-71` -- Rows (acceptance lines verbatim, PRD v0.18): UIR-32 "The breadcrumb names the account, the account and its strategy show the same tail, and one masking style is used."; UIR-34 "A level with one child shows no pie (or shows the next level down)."; UIR-49 "As UIR-31 and UIR-32."

The round-8 grade (CVO, window 18) left UIR-32/34/49 FAIL: a strategy drill does not name the account with the same tail and mask as the header (one mask form everywhere), and the ALL CATEGORIES card draws a one-slice pie. The ALL CATEGORIES card is the SHARED component `portal/src/components/CategoryViewTree.tsx` (:947, also used by src/pages/ModelPortfolios.tsx); breadcrumb and labels: `tabs/holdings/DrillTree.tsx` Breadcrumbs, `tabs/holdings/slices.ts` maskedLabelFor.

**Build:** One mask form everywhere (the header's `****1234 / TYPE`), in the drill breadcrumb and strategy levels. CategoryViewTree's one-slice pie is suppressed through an ADDITIVE prop the IR page passes (Model Portfolios' rendering unchanged).

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE71-AC1" cell_refs="IV-e-71"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-38/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-71.drill-mask.test.tsx 2>&1 | tail -20</invocation><expect>VERDICT: DRILL-MASK-ONE-SLICE-OK</expect></criterion>
`IVE71-AC1` -- the built behaviour: (a) a strategy drill's breadcrumb carries the header's masked account label; (b) the ALL CATEGORIES card with one category renders no pie on the IR page; control: CategoryViewTree without the new prop renders as today. Print `VERDICT: DRILL-MASK-ONE-SLICE-OK` only when every arm holds.
<criterion id="IVE71-AC2" cell_refs="IV-e-71" judgment="true"/>
`IVE71-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<expected_criteria>IVE71-AC1, IVE71-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/components/CategoryViewTree.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-71.drill-mask.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-71`.
<owned_cells>IV-e-71</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE71-AC1, IVE71-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-71.drill-mask-one-slice.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE71-AC1,IVE71-AC2` BEFORE the flip.
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

Seating: slot ~38, queue position 2 of 3; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 38 --path <abs> --portal-ref <DEV at seating>`.
