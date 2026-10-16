# TO IRPT_DASHBD.TO-DB-c-30 -- round 150: the page's series mirror takes on series contract 0.3.3 (the optional names history_scope_claim and history_scope_basis); portal edit in seriesContract.ts only; no deploy, no push

<to_id>IRPT_DASHBD.TO-DB-c-30</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~421</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's msg 9056 ("bring the portal series mirror to the contract, with iv-e-124 green on the merged tree") and the CTO's rulings on row S113 (msgs 9226 and 9227); `~D2`'s series contract 0.3.3 is on trunk (`40476cbde7`) | **Rows:**  IRPT_DASHBD-D2-W421-S<k> | **Decomp cell:** `DB-c-30` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 19) | **outcome_ref:** FWD-10 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-421`); run everything from its root unless a step says the portal. Its nested `portal/` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-421-portal`) cut from the portal commit `34a6baf8657bb166676dc3b8c3eec97ee8d3e585` (portal DEV, the round-148 merge). Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~421 <0.9.0_WK_IRPT_DASHBD~421@opal.agent>`; set it for that repo with the environment variables `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME`, `GIT_COMMITTER_EMAIL`, since the portal repo holds no identity); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh` (never `--no-verify`). Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~421/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. Made-up values only; no AWS call, no network. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why.** The series contract is the page's seam: the pin test `__tests__/dsgn-irptv1/iv-e-124.series-contract.test.ts` reads `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` and fails when the page's key lists differ from it. The contract now reads 0.3.3 (`~D2`, round 149, the CTO's msg 9226/9227: `history_scope` is derived per account): `series.optional` is `class_value`, `class_weight`, `class_names`, `unreported_trading_days`, `unreported_trading_days_basis`, `income_claim`, `history_scope_claim`, `history_scope_basis` (eight names). The page mirror (`dashboard/seriesContract.ts`) lists six, so `iv-e-124` is red on trunk.

**The cell (`DB-c-30`).**
1. **Read first.** `dashboard/seriesContract.ts` and `__tests__/dsgn-irptv1/iv-e-124.series-contract.test.ts`, and the contract file's `series.optional`, `series.fields.history_scope_claim`, `series.fields.history_scope_basis` and `history_scope_rule`. Run once, before any edit, `bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-124.series-contract.test.ts` from the portal worktree and record that it fails (base).
2. **The mirror.** In `dashboard/seriesContract.ts` only: `SERIES_OPTIONAL` becomes exactly the contract's eight `series.optional` names, in the contract's order; `SeriesDocument` gains `readonly history_scope_claim?: string` and `readonly history_scope_basis?: string`, each with a one-line comment (the claim words `inferred` and the basis text name how `history_scope` was derived; the page prints nothing for them in this cell). Do not make either required; do not change `SERIES_REQUIRED`, `SERIES_ARRAY_KEYS`, `MANIFEST_REQUIRED` or any reader function.
3. **Tests and fixtures.** `iv-e-124` must pass after the edit; `__tests__/irpt-dashbd/fwd10-unreported-days.test.tsx` must still pass. If `iv-e-124` fails for a reason that comes from this change inside the test itself, update ONLY that assertion and record the edit. Do NOT regenerate or edit the fixtures.
4. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` (rc 0; prove it can fail first with one deliberate error you revert) and `bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-124.series-contract.test.ts src/pages/InvestorReporting/__tests__/irpt-dashbd/fwd10-unreported-days.test.tsx`.
5. **Record** `BUILD_R150.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-421-portal", `base` "34a6baf8657bb166676dc3b8c3eec97ee8d3e585", `head`, `files_changed` (a list of paths)}, `optional_names` (the eight names as the file lists them), `existing_tests_edited` (a list of paths, empty when none), `tests` {`parity_pass`, `unreported_pass`, `base_parity_failed`}, `typecheck_rc`, `pushed` false, `deployed` false.

<criterion id="DBC151-1-AC1" cell_refs="DB-c-30"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r150/p151_bcw.py" . DBC151-1-AC1</invocation><expect>DBC151-1-AC1 PASS</expect></criterion>
`DBC151-1-AC1` -- `SERIES_OPTIONAL` in `dashboard/seriesContract.ts` equals the contract's `series.optional` in order (eight names, contract 0.3.3); `SeriesDocument` declares `history_scope_claim?: string` and `history_scope_basis?: string`; `bun test` on `iv-e-124` and the round-147 `fwd10-unreported-days` test passes with 0 failures. Base: FAIL (six-name list).

<criterion id="DBC151-1-AC2" cell_refs="DB-c-30"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r150/p151_bcw.py" . DBC151-1-AC2</invocation><expect>DBC151-1-AC2 PASS</expect></criterion>
`DBC151-1-AC2` -- the difference control and the bounds: with `dashboard/seriesContract.ts` temporarily put back to its base version by the checker, `iv-e-124` FAILS, and after the checker restores it the file is byte-identical to the worker's head; the portal diff from the base to the head touches only `dashboard/seriesContract.ts` and the two test folders, and not `DashboardPerformance.tsx`. Base: FAIL (no change; the control also refuses to run on a main checkout).

<expected_criteria>DBC151-1-AC1, DBC151-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other source file, `DashboardPerformance.tsx`, the fixtures' generator, the contract files, the checkers.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W421-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh` (never `--no-verify`); run its gates in the background and wait for them. ASCII only in anything you write. Leave this order's `<status>` as it is; the issuer flips it.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~421/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-30.page-mirror-takes-on-series-contract-033.md
portal/src/pages/InvestorReporting/dashboard/seriesContract.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 19, cell `DB-c-30`.
<owned_cells>DB-c-30</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC151-1-AC1, DBC151-1-AC2. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~421/IRPT_DASHBD.TO-DB-c-30.page-mirror-takes-on-series-contract-033.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC151-1-AC1,DBC151-1-AC2` BEFORE you report (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha; the eight optional names; the typecheck result; any existing test you edited; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a one-file portal edit on a worker branch; nothing is pushed, deployed, planned or written to any service.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched; the change reaches DEV by the portal merge-forward law, not by this order.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is read or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC151-1-AC2 plants its own difference control (the base file put back).
</preflight>
