# TO IRPT_DASHBD.TO-DB-f-505 -- the FILLED-REPORT EXPORT WIRE conformed to the server's names: the page sends `filled_report_source: {source_kind: 'filled_report', client_id}` and nothing else (the server pins the VersionId, sha256 and size at submit); a three-file rename with its tests

<to_id>IRPT_DASHBD.TO-DB-f-505</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~505</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>116</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the ruling on call f50a (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_F50A_FILLED_REPORT_EXPORT_PIN_SERVER_SIDE_20261015.md`: "The portal's export wire (`~F2`) sends the client id only. No portal amendment adds pin fields.") | **Rows:** IRPT_DASHBD-D2-W505-S<k> | **Decomp cell:** `DB-f-505` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R116_F.md`) | **outcome_ref:** FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-505` (branch `wk-IRPT_DASHBD-505`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-505/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-505-portal`), cut from `cand/dell2/irpt-default-performance-report` @506a2302d74ee95d7bbcf9d3dd73ab72ef1a2c2a. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~505 <0.9.0_WK_IRPT_DASHBD~505@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~505/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up client ids only; no real id or figure anywhere. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why.** Round 115 gave the export a proposed wire for a client's filled report: `performance_source: {path: 'FILLED_REPORT', client_id}`. The server's merged code names it differently: a request body carries `filled_report_source` with `source_kind: 'filled_report'` (`infra/aws/lambda/investor-reporting/export/retained_export.py` `parse_filled_report_source`, `export/bundle.py` `FILLED_REPORT_KIND`), and the server's own freeze tests feed it `{"filled_report_source": {...}}`. The CTO ruled (call f50a) that the SERVER pins the filled object's VersionId, sha256 and size at submit, so the page sends the client only. The page must therefore send exactly `filled_report_source: {source_kind: 'filled_report', client_id}` at the top level of the submitted `wireBundle` (the place `performance_source` sits for PATH B), carry no pin field, and send no `performance_source` for a filled export.

**The cell (`DB-f-505`).**
1. **Read first.** `export/filledReportSource.ts`, `export/submit.ts` (`PerformanceSource`, `buildSubmitRequest`, its `performanceSource` argument and the body it builds), `export/ExportButton.tsx` (about lines 250-260: where `filledReportSource(clientId)` is passed as the performance source), and `__tests__/irpt-dashbd/export-filled-report.test.tsx`. Run that test file once before any edit (base: it passes).
2. **The source file.** `export/filledReportSource.ts`: `export type FilledReportSource = { readonly source_kind: 'filled_report'; readonly client_id: string }` and `export function filledReportSource(clientId: string): FilledReportSource` returning exactly `{ source_kind: 'filled_report', client_id: clientId }`. The header comment says: these are the server's own names (the two server files above), the server pins version_id, sha256 and size at submit (CTO ruling on call f50a), and the page sends the client only. The strings `FILLED_REPORT` and `path:` appear nowhere in this file.
3. **Submit.** `export/submit.ts`: `buildSubmitRequest`'s `performanceSource` argument goes back to `PerformanceSource` alone; a NEW optional last argument `filledReportSource?: FilledReportSource` puts `filled_report_source: <it>` at the top level of the submitted `wireBundle`, beside where `performance_source` sits, and never together with `performance_source`; with neither argument the body is byte-for-byte what it was before round 115.
4. **The button.** `export/ExportButton.tsx` passes `filledReportSource(clientId)` through that new argument (for a Performance export with a `clientId` and no `accountId`, as now) and passes no `performanceSource` for it.
5. **Tests.** Update `__tests__/irpt-dashbd/export-filled-report.test.tsx` to the new shape (name each assertion you change; never weaken one beyond what the new names require) and add at least 2 tests: the body's `filled_report_source` has EXACTLY the two keys `source_kind` and `client_id` (a test titled with the word `pin`: no `version_id`, `sha256` or `size` key anywhere on it), and a filled export's body carries no `performance_source` (a test titled with the word `never`). The file must hold, between its titles, the words `pin`, `never`, `source`, `submit` and `client`, and at least 10 passing tests in all.
6. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of those before (20 failed at round 115's head).
7. **Record** `BUILD_R116.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-505-portal", `base` "506a2302d74ee95d7bbcf9d3dd73ab72ef1a2c2a", `head`, `files_changed`}, `wire` {`field` "filled_report_source", `keys` (the list of its keys), `location` (words: where on the submitted body)}, `tests` {`export_pass`, `suite_before_fail`, `suite_after_fail`}, `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBF116-1-AC1" cell_refs="DB-f-505"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r116/p116_wire.py" . DBF116-1-AC1</invocation><expect>DBF116-1-AC1 PASS</expect></criterion>
`DBF116-1-AC1` -- the wire: `filledReportSource.ts` carries `source_kind`, `'filled_report'` and `filledReportSource` and neither `FILLED_REPORT` nor `path:`; `submit.ts` carries `filled_report_source` and its `performanceSource` argument no longer admits the filled source; `ExportButton.tsx` uses `filledReportSource`; the export test file has the five title words and passes with 0 failures and at least 10 tests. Base: FAIL (no `source_kind` yet).
<criterion id="DBF116-1-AC2" cell_refs="DB-f-505"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r116/p116_wire.py" . DBF116-1-AC2</invocation><expect>DBF116-1-AC2 PASS</expect></criterion>
`DBF116-1-AC2` -- bounds: the portal diff from the candidate head `506a2302` to your head is not empty and touches only the four granted files. Base: FAIL (no change).

<expected_criteria>DBF116-1-AC1,DBF116-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every other export, render and tab file, the reader, `index.tsx`, `contracts/wire/ExportBundle.ts`, every other test, and the server files named above (read only; they are another seat's).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a neighbour test outside your grant fails because of your change, file a BLOCKING row naming it and stop; do not edit it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W505-S<k>` (D2 is the device coordinate), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~505/
portal/src/pages/InvestorReporting/export/filledReportSource.ts
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/export-filled-report.test.tsx
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-505.filled-report-export-wire-the-servers-names-client-id-only.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R116_F.md</decomp_doc> round 116, workstream ~F2 (F-SHIP), cell `DB-f-505`.
<owned_cells>DB-f-505</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF116-1-AC1, DBF116-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~505/IRPT_DASHBD.TO-DB-f-505.filled-report-export-wire-the-servers-names-client-id-only.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF116-1-AC1,DBF116-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha and the changed files; the wire keys and where they sit; the test counts and the typecheck and lint results; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: portal edits on a local branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF116-1-AC1 and AC2 FAIL at base and the checker's pure helpers are exercised by its self-test (10 arms).
lane: the <paths> block IS the grant.
</preflight>
