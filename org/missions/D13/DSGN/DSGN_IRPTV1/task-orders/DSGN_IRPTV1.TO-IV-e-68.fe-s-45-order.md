# TO DSGN_IRPTV1.TO-IV-e-68 -- fe-s-45 order dependence fixed and named; one pinned 3-run sample meets the bar (W34-S1)

<to_id>DSGN_IRPTV1.TO-IV-e-68</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~34</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E9 | **Decomp cell:** `IV-e-68` (decomp v9) | **outcome_ref:** -- (the suite the round grades by) | **depends_on:** none | **slot:** ~34, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-68` -- Rows: see below.

Row W34-S1: `__tests__/fe-s-45/residuals.test.ts` fails intermittently under the pinned runner IV-e-55 built (`__tests__/dsgn-irptv1/s7-determinism-check.ts`, `s7-suite-check.ts`; Q rows in `org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json`). CTO C-S60 (analysis section 2): the FIRST pinned sample is the grade; S7, W21-S2, W23-S1 and W29-S10 close only when fe-s-45's order dependence is FIXED and named and ONE pinned 3-run sample meets the bar (identical failing set, a subset of Q). A re-run that happens to pass is not a fix.

**Build:** Find the shared state fe-s-45/residuals.test.ts depends on (its dev-server / OS-process watch driver `__tests__/fe-s-45/dev-script-writes.mjs`, ports, temp dirs, or state another file leaves), fix it at the source, name the fix in `s7-flaky-sources.json`, and prove it with the pinned checks. No retries, no quarantine, no wider Q.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE68-AC1" cell_refs="IV-e-68"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-34/portal && timeout 900 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-determinism-check.ts 2>&1 | tail -20</invocation><expect>VERDICT: S7-DETERMINISTIC-OK</expect></criterion>
<criterion id="IVE68-AC2" cell_refs="IV-e-68"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-34/portal && timeout 290 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts 2>&1 | tail -20</invocation><expect>VERDICT: S7-SUITE-OK</expect></criterion>
Both are scripts run by bun (not bun test), with the bounds IV-e-55 used, a stated exception to the 120 s worker bound.

<expected_criteria>IVE68-AC1, IVE68-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-45/
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-determinism-check.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-flaky-sources.json
portal/scripts/dev-live.mjs
org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-68`.
<owned_cells>IV-e-68</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE68-AC1, IVE68-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~34/DSGN_IRPTV1.TO-IV-e-68.fe-s-45-order.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE68-AC1,IVE68-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W34-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3b98939b (org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md, @51ec23d744); CTO analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md @071e09aa18.
lane: the <paths> block IS the grant; disjoint from every parallel round-9 chain (decomp v9 table).
</preflight>

Seating: slot ~34, queue position 1 of 1; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 34 --path <abs> --portal-ref <DEV at seating>`.
