# TO DSGN_IRPTV1.TO-IV-e-55 -- The S7 bar graded under a pinned runner: three identical failing sets, a subset of Q (rows W29-S10, W29-S9)

<to_id>DSGN_IRPTV1.TO-IV-e-55</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~34</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<round>8</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Round:** 8 (CTO analysis @36e18bf320, msg 101845) | **Decomp cell:** `IV-e-55` (decomp v8) | **outcome_ref:** FWD-1 (the suite the round grades by) | **depends_on:** IV-e-54 (same slot, its commits are in your tree) | **slot:** ~34, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-55` -- Rows: DSGN_IRPTV1-W29-S10, W29-S9 (folded in), and on pass W21-S2, W23-S1, S7 close; supersedes TO-IV-e-50 (CTO 101845 section 2).

IV-e-50 measured two 3-run samples of the full IR suite that gave DIFFERENT internally-stable failing sets (15 vs 7). The runner
is `bun test src/pages/InvestorReporting` (bun 1.3.9; no `test` script in package.json, no bunfig.toml, no preload;
`scripts/suite-complete-check.mjs:73-74` wraps it). bun 1.3.9 offers `--seed=<val>` (pins a randomised order), `--randomize`,
`--concurrent` (off by default) and `--max-concurrency`; it runs in one process. IV-e-50 left `__tests__/dsgn-irptv1/s7-determinism-check.ts`,
`s7-suite-check.ts`, `s7-flaky-sources.json` and `org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json` (the Q rows).
Row W29-S9: `__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts` failed 1 of 3 runs on an identical tree.

**Build:** Pin the runner: one fixed invocation (a fixed test order, pinned by `--seed` or by file order, and no concurrency) written into
`s7-determinism-check.ts` and `s7-suite-check.ts` so both grade the SAME pinned run. Tests that fail only under some orders are
ORDER-DEPENDENT: fix each at its shared-state source (the file that leaks state or the one that depends on it) and name each fix in
`s7-flaky-sources.json`. Fix `iv-e-26.wire-regen.test.ts` at its source (real subprocess or filesystem state is this project's
established cause for this class, row W21-S3). **Pass** = three pinned runs give the IDENTICAL failing set, and that set is a subset of
the Q rows in `S7_CLASS_TABLE.json`. No retries, no quarantine, no wider Q allowance.

**Environment:** the portal worktree is based on your slot after IV-e-54. Other round-8 workers run in parallel in their own worktrees on disjoint files; edit only your `<paths>`. Do not start any server.

### ACCEPTANCE

<criterion id="IVE55-AC1" cell_refs="IV-e-55"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-34/portal && timeout 900 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-determinism-check.ts 2>&1 | tail -30</invocation><expect>VERDICT: S7-DETERMINISTIC-OK</expect></criterion>
<criterion id="IVE55-AC2" cell_refs="IV-e-55"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-34/portal && timeout 290 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts 2>&1 | tail -30</invocation><expect>VERDICT: S7-SUITE-OK</expect></criterion>

Each mechanical criterion prints its expect string only when every arm holds. The `__tests__/` grant is for order-dependent TEST fixes only; a product-path cause is a surprise row, not an edit. AC1 and AC2 are scripts run by bun (not bun test) with the bounds IV-e-50 used (900 s and 290 s), a stated exception to the 120 s worker bound because three full pinned runs take that long. Both FAIL at the base (IV-e-50: DETERMINISTIC unstable, SUITE-FAIL).

<expected_criteria>IVE55-AC1, IVE55-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `src/lib/**`, `contracts/**` (unless named), other pages and every file not named are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-determinism-check.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-flaky-sources.json
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-26.wire-regen.test.ts
portal/scripts/suite-complete-check.mjs
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v8, cell `IV-e-55`.
<owned_cells>IV-e-55</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE55-AC1, IVE55-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~34/DSGN_IRPTV1.TO-IV-e-55.pinned-runner.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE55-AC1,IVE55-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W34-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3f76cdb2 (issuer, 2026-09-27 ~08:1xZ); file:line facts above are from that read.
lane: the <paths> block IS the grant; disjoint from every parallel round-8 chain (decomp v8 table).
</preflight>

Seating: slot ~34, queue position 2 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 34 --portal-ref <DEV at seating>` when C: allows (0.0.0_AB_MSTR 101618).
