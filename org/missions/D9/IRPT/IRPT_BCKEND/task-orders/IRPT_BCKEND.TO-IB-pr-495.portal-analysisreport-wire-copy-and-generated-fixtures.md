# TO IRPT_BCKEND.TO-IB-pr-495 -- the portal's AnalysisReport wire copy and generated fixtures carry the extractor's section form (row DSGN_IRPTV1-D2-W63-S1, the follow-up)

<to_id>IRPT_BCKEND.TO-IB-pr-495</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~346</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>170</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's DSGN_IRPTV1 ROUND-31 ANALYSIS section 1 (row D2-W63-S1: "the page's fixtures are re-derived after") and ROUND-33 ANALYSIS section 2 | **Decomp cell:** `IB-pr-495` (decomposition section 162) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-495` (inlined):** the producer's contract fixtures now send the extractor's section form (merged: `IB-pr-491`: `section_id` `2.annualized_return.c1`, `section_type` `2`, `value` 7.12, `units` `pct`). The portal still carries the OLD section (`section_type` `annualized_return`, `units` `DECIMAL_FRACTION`) in its wire copy and in the fixtures generated from it: `portal/src/pages/InvestorReporting/fixtures/wire/AnalysisReport.valid.json` is the consumer's mirror of the producer's file, and `fixtures/smoke/*.json`, `fixtures/fe-s-15/job.*.json` and several `__tests__/*` fixture files are written by `__tests__/fe-s-13/gen-all.ts`, `gen-corpus.ts`, `gen-wire.ts`, `gen-consumed.ts` and `__tests__/fe-s-15/gen-fixtures.ts`, `__tests__/fe-s-18/gen-fixtures.ts` from that copy, so a hand edit of a generated file would be undone by the next regeneration. Re-derive them. You work in the PORTAL repo (your worktree's `portal/` directory, a worktree of the portal repo with `node_modules` linked; bun is on PATH). This is a candidate for portal DEV; its PROD rides Andrew's held promote.

**Steps:**
1. Copy the producer's section into the portal wire copy: in `portal/src/pages/InvestorReporting/fixtures/wire/AnalysisReport.valid.json` set `instance.sections` to equal `instance.sections` of `infra/aws/lambda/investor-reporting/_contracts/fixtures/AnalysisReport.valid.json` in your workspace root (the parent of `portal/`).
2. Find which generator writes each file that still carries the old tokens (`grep` the generators for the wire copy's path; run each generator the way its header or its test says, from the portal directory) and regenerate. A file that no generator writes and that still carries the old tokens is hand-written: change its `section_type`/`units`/`value`/`section_id` to the same extractor form (section_id `2.annualized_return.c1`, section_type `2`, value 7.12, units `pct`).
3. Tests that assert the old tokens or the old printed words (`iv-e-101`, `iv-e-105`, `iv-e-106`, `iv-e-102.prospect-open.domrun.tsx`, `iv-e-115`, `iv-e-122` under `src/pages/InvestorReporting/__tests__/dsgn-irptv1/`) are updated to the new tokens ONLY where they assert the fixture's value; a test that asserts a RENDERED word keeps its assertion and you re-read what the page now prints (the vendor section prints through the page's upper-case unit map and a code that prints itself); do not weaken a test, report a printed word that changes.
4. The two test fixture files `src/pages/InvestorReporting/__tests__/fe-s-32/holdings-no-answer.json` and `__tests__/fe-s-74/fixtures/one-bad-key.json` carry the old section too: same extractor form.

**Do NOT** edit any product file under `src/` outside `src/pages/InvestorReporting/fixtures/` and `src/pages/InvestorReporting/__tests__/`, any generator's logic, `package.json` or lockfiles; run no `bun install`; push nothing.

**Criteria (run each under `timeout 120` from your WORKSPACE root, the parent of `portal/`, record the output and exit code verbatim):**

<criterion id="IB170-4-AC1" cell_refs="IB-pr-495"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-4-AC1</invocation><expect>IB170-4-AC1 PASS</expect></criterion>
<criterion id="IB170-4-AC2" cell_refs="IB-pr-495"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-4-AC2</invocation><expect>IB170-4-AC2 PASS</expect></criterion>
<criterion id="IB170-4-AC3" cell_refs="IB-pr-495"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r170/p170_cells.py" . IB170-4-AC3</invocation><expect>IB170-4-AC3 PASS</expect></criterion>

<expected_criteria>IB170-4-AC1, IB170-4-AC2, IB170-4-AC3</expected_criteria>

What the checks grade: AC1 no `.json`, `.ts` or `.tsx` file under the portal's `fixtures/` folder or the two named test fixture files carries `annualized_return` or `DECIMAL_FRACTION` (at base 29 files do); AC2 the five token-citing tests (`iv-e-101.opal-report-words`, `iv-e-105.opal-document-words`, `iv-e-106.sections-retained-ref`, `iv-e-115.vendor-section-names-units`, `iv-e-122.vendor-validation-and-source`) pass under `bun test` (21 pass, 0 fail at base: a bound); AC3 the portal wire copy's `sections` equal the producer fixture's. Do not edit the checks. Your own drain-level work (the whole `bun test src/pages/InvestorReporting`) is the issuer's at the merge; run it ONCE at the end and report its pass and fail counts against a base run you take FIRST.

## BOUNDS

- **Grant:** the `paths` block and nothing else. Portal repo: only `src/pages/InvestorReporting/fixtures/` and `src/pages/InvestorReporting/__tests__/`. No product code, no generator logic, no dependency change.
- **Refusal clause:** STOP, file a row, change nothing more, if a generator cannot be run without a network or a secret, if regenerating changes a figure other than the section's, or if a test cannot be updated without weakening it.
- **Commit** in BOTH repos per your definition: the workspace commit (the deliverables, the order flip, the rows) with `.tools/safe-commit.sh`, and the portal commit with plain `git -C portal commit` (same author and committer values, message file from the Write tool outside the worktree); ASCII only; do not push; never stage the workspace's `portal` gitlink.
- **Row ids** are `IRPT_BCKEND-D2-W346-S<k>` (the next free `k`). Report once, under 150 words.

<paths>
portal/src/pages/InvestorReporting/fixtures/
portal/src/pages/InvestorReporting/__tests__/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~346/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-495.portal-analysisreport-wire-copy-and-generated-fixtures.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 162 (round 170, workstream ~P), cell `IB-pr-495`.
<owned_cells>IB-pr-495</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB170-4-AC1, IB170-4-AC2, IB170-4-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~346/IRPT_BCKEND.TO-IB-pr-495.portal-analysisreport-wire-copy-and-generated-fixtures.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- test fixtures and tests of one portal page; no product file, no served artifact; the candidate lands on portal DEV through the CTO review lane, PROD rides the held promote `dell1-e7f2`. No live DSGN_IRPTV1 order names these files (the issuer read the non-complete orders' paths: all superseded).
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p170_cells.py dry-run at base on dell2 2026-10-13 ~02:2xZ: IB170-4 AC1 FAIL (29 files carry the old tokens), AC2 PASS (a bound: 21 pass, 0 fail), AC3 FAIL (the wire copy's section differs from the producer's). Not run: a positive control for AC1 and AC3.
lane: the paths block IS the grant; worker slot ~346 of IRPT_BCKEND, a portal worktree pair. Class LOCAL.
</preflight>
