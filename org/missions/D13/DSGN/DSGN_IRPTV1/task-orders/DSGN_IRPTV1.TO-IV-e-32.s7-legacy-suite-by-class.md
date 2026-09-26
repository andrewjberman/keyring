# TO DSGN_IRPTV1.TO-IV-e-32 -- S7: every legacy failing test takes one class (Retired / Regression / Harness / Query) and is dispositioned by it

<to_id>DSGN_IRPTV1.TO-IV-e-32</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~21</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<round>5</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.8 @31a61d0466 | **Decomp cell:** `IV-e-32` (decomp v5) | **outcome_ref:** FWD-11 (the suite as the body contract), S7 | **depends_on:** IV-e-31 (chain 1, position 2: this batch cell runs last) | **slot:** ~21, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-32` -- row `DSGN_IRPTV1-S7` (OPEN, ARMED; REMEDIATION_v2 @36eb3c9492), ruled BY CLASS in the CTO's round-4 analysis
(ledger/ROUND_ANALYSIS.round4.md @61cd39d895, section 2 -- READ IT, it is the rule). At the base, `bun test src/pages/InvestorReporting`
fails about 80 tests across about 36 files, all under `IR/__tests__/fe-s-*` plus a few others (measure it yourself first: the list
you measure at the base, after IV-e-31 lands on this worktree, is the denominator).

Give EVERY failing test exactly ONE class and act by it:
- **R -- RETIRED:** it asserts behaviour a PRD amendment retired or changed (account chips on the header, FWD-2 v0.6; the drawer or
  truncated menu, FWD-3 v0.6; the left rail or request history, FWD-7/8 v0.6; method, lineage, basis, denominator or provenance in
  the footer, FWD-5/6 v0.8; an "UNAVAILABLE" string on a body, FWD-15; the retired `render/performance/Summary.tsx` block).
  Re-scope the assertion to the current ENDPOINT (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_DSGN_IRPTV1_20260924.md`)
  or delete it; the row names the retiring FWD and PRD version.
- **G -- REGRESSION:** it asserts behaviour the current ENDPOINT still requires, and fails. Fix the CODE; never the test.
- **H -- HARNESS:** it fails for an environment reason (fixture paths resolved from a worktree, missing browser APIs, timing,
  a generator that rewrites committed files in place -- e.g. IVE26-AC3's wire regen). Fix the harness; the assertion stays.
- **Q -- QUERY:** it cannot be classed from the PRD. At most 5; leave it failing, one line each for the CTO.

Record every test in `org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json`: {"base": "<portal sha you measured at>", "base_failures": <N>, "rows": [{"file": ..., "test":
<full test name>, "class": "R|G|H|Q", "retired_by": "FWD-n vX.Y" (R only), "action": <one line>, "query": <one line, Q only>}]}.

**The rules:** the FE derives nothing; colour is keyed by the served code or class, never a label substring or a guess; a test is never edited to pass (a REGRESSION is fixed in the code).

**Environment:** the portal worktree is based on DEV `1e02be40` (= origin DEV, PROD 36a37afc plus site-Z work outside InvestorReporting). Each criterion's check file does not exist at the base: you write it from the criterion's text, and it prints the VERDICT only when every arm holds. Do not start any server (dev builds run on port 5174 only, serving the main checkout). `IVE32-AC2` runs the IR suite (about 2 minutes); it is `.ts`, not `.test.ts`, so the suite never collects it.

### ACCEPTANCE

<criterion id="IVE32-AC1" cell_refs="IV-e-32"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-21/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~21; timeout 290 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-table-check.ts 2>&1 | tail -25</invocation><expect>VERDICT: S7-TABLE-OK</expect></criterion>
`IVE32-AC1` -- reading `org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json` (resolved from the portal root as `../org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json`): `rows` has exactly `base_failures` entries, each with a class in R/G/H/Q; every R row names `retired_by` as "FWD-<n> v<x.y>"; at most 5 Q rows each carry a `query`; no (file, test) pair repeats. It prints `VERDICT: S7-TABLE-OK` only when every arm holds.

<criterion id="IVE32-AC2" cell_refs="IV-e-32"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-21/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~21; timeout 290 /c/Users/AndrewBerman/.bun/bin/bun src/pages/InvestorReporting/__tests__/dsgn-irptv1/s7-suite-check.ts 2>&1 | tail -25</invocation><expect>VERDICT: S7-SUITE-OK</expect></criterion>
`IVE32-AC2` -- running `bun test src/pages/InvestorReporting` as a child process, the set of failing tests equals exactly the table's Q rows (matched by file and full test name), and the pass count is printed. It prints `VERDICT: S7-SUITE-OK` only when every arm holds.

<expected_criteria>IVE32-AC1, IVE32-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**` and `api/**` edits are
  OUT unless a REGRESSION fix (S7 class G) needs them, and then only under `portal/src/pages/InvestorReporting/`; `src/lib/**` is read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (row W3-S2); never type a firm token in a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/ledger/S7_CLASS_TABLE.json
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v5, cell `IV-e-32`.
<owned_cells>IV-e-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE32-AC1, IVE32-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~21/DSGN_IRPTV1.TO-IV-e-32.s7-legacy-suite-by-class.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE32-AC1,IVE32-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W21-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched (decomp v5).
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v5 -- the write paths measured at portal DEV 1e02be40 (DrillTree.tsx:241/:277 label fallback live; 78 failing tests in 36 files under InvestorReporting at 4d6c8aaa's suite run).
lane: the <paths> block IS the grant; one chain, so the batch cell's wide grant follows the narrow one on the same worktree.
</preflight>

Seating: slot ~21, queue position 2 of 2; worktree pair provisioned by
`.tools/wk-provision.sh provision DSGN_IRPTV1 21 --portal-ref 1e02be40eca4cb0f9ce4c0cc77a6ac510fe6ae11`.
