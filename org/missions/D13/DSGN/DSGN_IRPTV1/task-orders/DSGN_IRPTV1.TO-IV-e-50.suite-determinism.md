# TO DSGN_IRPTV1.TO-IV-e-50 -- the harness cell: the Investor Reporting suite is deterministic (3 identical full runs) and only the table's Q rows fail (CTO 101651, disarms W23-S1)

<to_id>DSGN_IRPTV1.TO-IV-e-50</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~29</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.16 @f3026103f0 | **Decomp cell:** `IV-e-50` (decomp v7 addendum 5) | **outcome_ref:** FWD-11 (the suite as the body contract), S7 | **depends_on:** IV-e-35 (merged), IV-e-45 (same slot, queue) | **slot:** ~29, queue position 3 of 3

---

## WORKER FACE

### THE CELL

`IV-e-50` -- 1.0.0_SA_CTO's ruling 101651 on TO-IV-e-35 (merged as a strict improvement, 31 -> 16 failing): row
`DSGN_IRPTV1-W23-S1` is disarmed into THIS cell. Its bar, verbatim in substance:

- **The Investor Reporting suite is deterministic:** 3 consecutive full runs of `bun test src/pages/InvestorReporting` give IDENTICAL
  pass/fail sets. No retries, no quarantine, no skip added to hide a test, and no raised Q cap (at most 5 Q rows, table
  `org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json`).
- **The first criterion names W21-S3's flaky files by the shared-state source that makes them flaky** (timers, module caches,
  fixtures, ordering, or another named source), one line per file, and each source is removed at its root.
- **The "only Q rows fail" bar** (`src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts`, unchanged in its assertion) now lives here.

**Known inputs:** rows `DSGN_IRPTV1-W21-S3` (fe-s-33/39/46 run-to-run flakiness) and `DSGN_IRPTV1-W23-S1` (the flakiness spans at least 9
files; 13 failures outside the Q rows at IV-e-35's close), both in `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md`; IV-e-35's result
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~23/s7-residual.result.md`; the class rule (R retire with the retiring FWD named, G fix the
code, H fix the harness or fixture with the assertion unchanged, Q leave failing with one line for the CTO) in
`org/missions/D13/DSGN/DSGN_IRPTV1/ledger/ROUND_ANALYSIS.round4.md` section 2. `contracts/public-status.ts` stays producer-faithful (CTO 101449): never loosen it.

**Environment:** this slot's portal worktree carries every round-7 cell once IV-e-43 and IV-e-45 are done on it; that is your base.
Re-measure the failing set yourself first (3 full runs): it is your denominator. A full run takes about 150-220 s. Do not start any
server.

### ACCEPTANCE

<criterion id="IVE50-AC1" cell_refs="IV-e-50"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-29/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~29; timeout 900 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-determinism-check.ts 2>&1 | tail -30</invocation><expect>VERDICT: S7-DETERMINISTIC-OK</expect></criterion>
`IVE50-AC1` -- a new check file: it runs `bun test src/pages/InvestorReporting` 3 times in a row as child processes (JUnit output, the
pattern `s7-suite-check.ts` uses), prints each run's pass count and failing set, and prints `VERDICT: S7-DETERMINISTIC-OK` only when the
three failing sets are identical. It also reads `src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-flaky-sources.json` (written by you: one entry per W21-S3 / W23-S1 flaky file
with its shared-state source and the commit that removed it) and fails if any entry lacks a source or a removing commit.

<criterion id="IVE50-AC2" cell_refs="IV-e-50"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-29/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~29; timeout 290 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts 2>&1 | tail -25</invocation><expect>VERDICT: S7-SUITE-OK</expect></criterion>
`IVE50-AC2` -- IV-e-32's own instrument, unchanged in its assertion: the failing set equals exactly the table's Q rows.

<expected_criteria>IVE50-AC1, IVE50-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Product code, `contracts/public-status.ts`,
  `src/lib/**` and every other page are READ, never edited: a flakiness source in product code is a surprise row and a Q line, not an
  edit. The workspace `portal` gitlink is NOT yours: never stage or commit it.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (row W3-S2); never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/__tests__/fe-s-*
portal/src/pages/InvestorReporting/__tests__/m-overlay/
portal/src/pages/InvestorReporting/__tests__/m-selection/
portal/src/pages/InvestorReporting/__tests__/mvp-selection/
portal/src/pages/InvestorReporting/__tests__/mvp-upload/
portal/src/pages/InvestorReporting/__tests__/submission-request.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-17.regenerated.test.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-table-check.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-determinism-check.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-flaky-sources.json
portal/src/pages/InvestorReporting/fixtures/
portal/src/pages/InvestorReporting/render/fixtures/
org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7 addendum 5, cell `IV-e-50`.
<owned_cells>IV-e-50</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE50-AC1, IVE50-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~29/DSGN_IRPTV1.TO-IV-e-50.suite-determinism.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE50-AC1,IVE50-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W29-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- measured at local portal DEV 9c45800b: 887 pass / 16 fail (the drain's suite run after chains S/P/H/T); rows W21-S3 and W23-S1 name the flaky files.
lane: the <paths> block IS the grant (tests, fixtures, the class table, the channel); queued on slot ~29 after IV-e-45 so it measures the final round-7 DEV.
</preflight>

Seating: slot ~29, queue position 3 of 3 (after IV-e-43 and IV-e-45), no new worktree.
