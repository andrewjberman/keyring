# TO DSGN_IRPTV1.TO-IV-e-72 -- Holdings charts at any account count (UIC-10/12/13)

<to_id>DSGN_IRPTV1.TO-IV-e-72</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~38</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>superseded</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E7 | **Decomp cell:** `IV-e-72` (decomp v9) | **outcome_ref:** FWD-2, FWD-14, FWD-19, FWD-21, FWD-23 | **depends_on:** IV-e-71 (same slot) | **slot:** ~38, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-72` -- Rows (acceptance lines verbatim, PRD v0.18): UIC-10 "Labels never overlap: small slices move to the legend (or a leader line)."; UIC-12 "A negative account is shown as a separate, labelled line (never as a pie slice), and the pie's shares sum to the positive total it states."; UIC-13 "Every account is reachable from Over what (a 'show all' or a scroll affordance); no row is clipped."

File:line facts: `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md` rows UIC-10/12/13 (DrillTree.tsx renderInsideLabel :162-186 labels every slice; donutRows :562 keeps negative accounts; slices.ts buildSliceRows :583; IdentityCard.tsx account list :560-589 inside Panel overflow-hidden :497).

**Build:** Small slices move to the legend (no overlapping labels); a negative account is a separate labelled line, never a slice, and the pie's shares sum to the positive total; every account is reachable from OVER WHAT (no clipped row).

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE72-AC1" cell_refs="IV-e-72"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-38/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-72.holdings-any-count.test.tsx 2>&1 | tail -20</invocation><expect>VERDICT: HOLDINGS-ANY-COUNT-OK</expect></criterion>
`IVE72-AC1` -- the built behaviour: one arm per UIC row on a fixture with 11+ accounts and one negative account; control: a 3-account fixture renders as today. Print `VERDICT: HOLDINGS-ANY-COUNT-OK` only when every arm holds.
<criterion id="IVE72-AC2" cell_refs="IV-e-72" judgment="true"/>
`IVE72-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<expected_criteria>IVE72-AC1, IVE72-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/DrillTree.tsx
portal/src/pages/InvestorReporting/tabs/holdings/slices.ts
portal/src/pages/InvestorReporting/tabs/holdings/SliceTable.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-72.holdings-any-count.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-72`.
<owned_cells>IV-e-72</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE72-AC1, IVE72-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~38/DSGN_IRPTV1.TO-IV-e-72.holdings-any-count.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE72-AC1,IVE72-AC2` BEFORE the flip.
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

Seating: slot ~38, queue position 3 of 3; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 38 --path <abs> --portal-ref <DEV at seating>`.

**Issuer close (2.0.0_SA_COO~D, 2026-09-28 ~17:5xZ):** SUPERSEDED by FAST lease, drive-mode.log line 16 (ARM DSGN_IRPTV1 17:47:43Z, CTO msg 102388, placement @1d443e50db on Andrew-direct 17:3xZ record @229b3fd184). No worker was seated and no build exists for this cell; its rows move verbatim to the FAST next-list in org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md, built by 2.0.0_SA_COO~D under /closer-drive and graded by the CVO after the fact.
