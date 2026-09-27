# TO DSGN_IRPTV1.TO-IV-e-35 -- the S7 residual: the Investor Reporting suite fails ONLY the table's Q rows (W21-S2 disarm; CTO 101449)

<to_id>DSGN_IRPTV1.TO-IV-e-35</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~23</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>superseded</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.12 @0953f5b5d9 | **Decomp cell:** `IV-e-35` (decomp v6, addendum 1) | **outcome_ref:** FWD-11 (the suite as the body contract), S7 | **depends_on:** IV-e-32 (merged, DEV 8b36968e) | **slot:** ~23, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-35` -- the residual of row `DSGN_IRPTV1-S7`, carried by 1.0.0_SA_CTO's ruling 101449 ("the bar moves; it is not lowered"). IV-e-32
classed all 79 base failures (`org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json`: R4, G2, H69, Q4) and repaired one shared bug family; at portal DEV `8b36968e` the full suite
reads 855 pass / 32 fail, the 32 under `IR/__tests__/` in 19 files (measure it yourself first; that list is your denominator). Row
`DSGN_IRPTV1-W21-S2` (BLOCKING) names this residual; you disarm it.

**The rule is the CTO's round-4 analysis section 2** (`org/missions/D13/DSGN/DSGN_IRPTV1/ledger/ROUND_ANALYSIS.round4.md`) plus ruling 101449:
- Each still-failing test takes ONE class: **R** (asserts retired behaviour: re-scope or delete, naming the retiring FWD and PRD version),
  **G** (the current ENDPOINT requires it: fix the CODE), **H** (environment or fixture: fix the harness or the fixture, assertion unchanged),
  **Q** (cannot be classed from the PRD: leave failing, one line for the CTO; the TOTAL Q across the table stays at most 5).
- **101449:** `contracts/public-status.ts` stays at its producer-faithful bytes: `state` and `public_reason_code` are REQUIRED and the code is a
  non-null `^[A-Z0-9_]+$` string (`PublicStatusEnvelope.schema.json:27-33, :223-226`). A test that fed a state-less or null-code status is
  re-classed **H** (fix the fixture to a contract-legal shape) or **R** (the retired shape), NEVER G, and never loosen the consumer.
- The known families (IV-e-32's result, `deliverables/0.9.0_WK_DSGN_IRPTV1~21/s7-legacy-suite-by-class.result.md` on CLOUD): the
  `requirePublicStatus` business_date obligation on intentionally dateless status fixtures; two render/adapter questions; fe-s-33/39/46
  run-to-run flakiness (row W21-S3: make them deterministic, class H); the fe-s-41 schema fix vs fe-s-46's DEV-diff purity rule (row
  W21-S1: rule it by re-pointing fe-s-46's baseline to the post-S7 commit, class H, naming why); `iv-e-17.regenerated.test.ts` regenerating
  `contracts/wire/**` IN PLACE (a suite run rewrites 25 files with LF endings: regenerate into a temp dir and compare, class H).
- Update `org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json` in place: every row's final class and action; rows you move keep their id; the table's `base` stays IV-e-32's.

**Environment:** the portal worktree is based on DEV `8b36968e` (round 5 merged). Round 6's IV-e-34 runs in parallel on slot ~22 with
`IR/__tests__/dsgn-irptv1/` (except `iv-e-17.regenerated.test.ts`), `tabs/`, `header/`, `index.tsx` and `export/`: do not edit those.
Do not start any server.

### ACCEPTANCE

<criterion id="IVE35-AC1" cell_refs="IV-e-35"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-23/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~23; timeout 290 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts 2>&1 | tail -25</invocation><expect>VERDICT: S7-SUITE-OK</expect></criterion>
`IVE35-AC1` -- IV-e-32's own AC2 instrument (`src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts`, unchanged in its assertion): running `bun test src/pages/InvestorReporting`,
the set of failing tests equals exactly the table's Q rows (matched by file and full test name), and the pass count is printed. It prints
`VERDICT: S7-SUITE-OK` only when every arm holds.

<criterion id="IVE35-AC2" cell_refs="IV-e-35"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-23/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~23; timeout 290 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-table-check.ts 2>&1 | tail -25</invocation><expect>VERDICT: S7-TABLE-OK</expect></criterion>
`IVE35-AC2` -- the updated table still validates (`src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-table-check.ts`: rows equal base_failures, each class in R/G/H/Q, R rows name
`retired_by`, at most 5 Q each with a query, no (file, test) repeats) and `git diff 8b36968e -- src/pages/InvestorReporting/contracts/public-status.ts`
is empty. It prints `VERDICT: S7-TABLE-OK` only when every arm holds (the public-status arm may live in a small added assertion in the
same check file).

<expected_criteria>IVE35-AC1, IVE35-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/public-status.ts`, `tabs/**`,
  `header/**`, `index.tsx`, `export/**` and every other page are OUT; `src/lib/**` is read, never edited. A true class-G code fix outside
  the grant is a surprise row and a Q, not an edit.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `8b36968e09a816da9c8245be8ec10790c5faf74d`). Commit through `.tools/safe-commit.sh`.
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
portal/src/pages/InvestorReporting/fixtures/
portal/src/pages/InvestorReporting/render/fixtures/
org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v6 addendum 1, cell `IV-e-35`.
<owned_cells>IV-e-35</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE35-AC1, IVE35-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~23/DSGN_IRPTV1.TO-IV-e-35.s7-residual.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE35-AC1,IVE35-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W23-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- measured at portal DEV 8b36968e: 855 pass / 32 fail in 19 files (the suite log of the round-5 drain).
lane: the <paths> block IS the grant; disjoint from IV-e-34's (slot ~22) except none -- iv-e-17.regenerated.test.ts and s7-table-check.ts are named singly.
</preflight>

Seating: slot ~23, queue position 1 of 1; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 23 --portal-ref 8b36968e09a816da9c8245be8ec10790c5faf74d`.

**Issuer close (2.0.0_SA_COO~D, 2026-09-27 ~00:5xZ, on CTO 101651):** SUPERSEDED, not complete. IVE35-AC2 PASS; IVE35-AC1 FAIL (15 failing: 13 outside the Q rows, flakiness across at least 9 files). Merged as a strict improvement (31 -> 16 failing on DEV 9c0cff2f); row W23-S1 disarmed by the ruling into ONE harness cell whose bar is a deterministic suite (3 consecutive full runs, identical pass/fail sets, no retries, no quarantine, no raised Q cap); the 'only Q rows fail' bar moves there.
