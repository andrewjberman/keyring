# TO IRPT_DASHBD.TO-DB-f-801 -- the CLASS-SERIES READER: one new portal file that fetches an account's `class_series` document (route `GET .../reporting/{account_id}/class_series`) and turns its columnar shape into the `ClassDailyRow` rows the round-119 class model reads, plus its tests; new files only, not mounted, nothing served

<to_id>IRPT_DASHBD.TO-DB-f-801</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~801</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>121</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, open call 3596 (msg 8826: "(3) ~F2 builds only the reader and the tab") with the shape and name from `2.0.0_SA_COO~D2` (msg 8846) and the route key from `2.0.0_SA_COO~S2` (msg 8848: `which=class_series`) | **Rows:** IRPT_DASHBD-D2-W801-S<k> | **Decomp cell:** `DB-f-801` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R121_F.md`) | **outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-801` (branch `wk-IRPT_DASHBD-801`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-801/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-801-portal`), cut from the class candidate `cand/dell2/irpt-asset-class-performance` @7fa808c949fbe5d9c9d4ea1aea3aa3006be7d2e8. Do not amend or revert anything already committed there. Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~801 <0.9.0_WK_IRPT_DASHBD~801@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~801/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up ids and figures only. All portal paths below are under `portal/src/pages/InvestorReporting/`.

**Why.** FWD-3 (asset-class performance and mix). The class model and section exist (round 119; `tabs/reporting/classes/classWindowModel.ts`, `AssetClassSection.tsx`): the model reads `ClassDailyRow[]` (one row per account, date and class). The data will arrive as ONE columnar document per account, which `2.0.0_SA_COO~D2` will publish as `class_series.json.gz` beside `series.json.gz`, served by the existing route with `which=class_series`. Nothing is served yet and `~D2`'s contract file (section `class_object`, version 0.4.0) is not committed, so this cell builds against the SHAPE `~D2` named, and the reader refuses anything that does not match it. The reader is not mounted anywhere.

**The shape (as `~D2` named it; one JSON object).** `account_id` (string), `firm` (string), `as_of` (string, ISO date), `method_version` (string), `schema_version` (string), `date` (array of ISO date strings, ascending), `class_names` (array of strings, the gold class names in gold enum order), `coverage` (array of strings, one per date), `market_value_eod` (object: class name to an array of numbers aligned to `date`), `class_return_daily` (object: class name to an array of numbers or null aligned to `date`; null on a day whose coverage is not `MEASURED`). Every per-day array has the length of `date`; index `i` is the same business date in every array.

**The cell (`DB-f-801`).**
1. **Read first.** `dashboard/reportingRead.ts` (`REPORTING_READ_BASE`, `reportingReadPath`, `FetchJson`, `liveFetchJson`, how the existing readers turn an envelope refusal or a bad body into an `absent` answer), `tabs/reporting/classes/classWindowModel.ts` (`ClassDailyRow`, its field names), and the report reader in the candidate `cand/dell2/irpt-default-performance-report` (`dashboard/report/reportRead.ts`, via `git -C portal show cand/dell2/irpt-default-performance-report:src/pages/InvestorReporting/dashboard/report/reportRead.ts`) as the pattern for a reader. Run `bun test src/pages/InvestorReporting/__tests__/irpt-dashbd/class-window-model.test.ts` once before any edit.
2. **ONE new source file** `tabs/reporting/classes/classSeriesRead.ts` exporting: (a) `classSeriesPath(accountId, selectedTenant?)` returning `${REPORTING_READ_BASE}/<encoded account>/class_series` with `?selected_tenant=<encoded>` only when a tenant is given; (b) a pure `classSeriesToRows(doc: unknown)` returning `{ accountId, asOf, methodVersion, rows: ClassDailyRow[] } | null`: `null` (never a partial result) unless the document matches the shape above exactly (every required key present with its type, every per-day array the length of `date`, every class in `class_names` present in both objects, dates strictly ascending), otherwise one `ClassDailyRow` per date and class in `class_names` order with `account_id`, `business_date`, `asset_class` (the class name as given), `market_value_eod`, `class_return_daily` (number or null) and `coverage` (that date's coverage string); (c) `readClassSeries(accountId, selectedTenant?, fetchJson = liveFetchJson)` returning `{ kind: 'served', ...the conversion } | { kind: 'absent', reason: string | null }`, where an envelope refusal (`ok: false`, its public reason code) or a rejected fetch gives `absent` with that code (or `null`), and a body `classSeriesToRows` refuses gives `absent` with the reason `CLASS_SERIES_UNREADABLE`. No clock, no DOM, no mount, no import of the tab, the section or `ReportingTab`; only `reportingRead.ts` and the model's type. ASCII only. A class name outside the model's seven stays a row (the model decides what to print).
3. **ONE new test file** `__tests__/irpt-dashbd/class-series-read.test.ts`, made-up ids and numbers, at least 8 tests whose titles together contain the words `path`, `columnar`, `rows`, `absent`, `null`, `misaligned`, `unreadable` and `tenant`: the path with and without a tenant; a good document converts to the expected rows (count = dates x classes, the order, the null return preserved on a non-MEASURED day); a misaligned array (one array shorter than `date`) gives `null`; a missing key and a wrong type give `null`; dates not ascending give `null`; an envelope refusal gives `absent` with its code; a rejected fetch gives `absent`; an unreadable body gives `absent` with `CLASS_SERIES_UNREADABLE`. Use an injected fake `fetchJson`; never the network.
4. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of those before.
5. **Mutant** (temporary, reverted): make `classSeriesToRows` skip the length check; at least one test must fail. Say which.
6. **Record** `BUILD_R121.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-801-portal", `base` "7fa808c949fbe5d9c9d4ea1aea3aa3006be7d2e8", `head`, `files_changed`}, `tests` {`reader_pass`, `suite_before_fail`, `suite_after_fail`}, `mutant_failed_tests` (a number), `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBF121-1-AC1" cell_refs="DB-f-801"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r121/p121_reader.py" . DBF121-1-AC1</invocation><expect>DBF121-1-AC1 PASS</expect></criterion>
`DBF121-1-AC1` -- `class-series-read.test.ts` carries titles with the eight words `path`, `columnar`, `rows`, `absent`, `null`, `misaligned`, `unreadable` and `tenant`, and `bun test` on it passes with 0 failures and at least 8 tests. Base: FAIL (no file).
<criterion id="DBF121-1-AC2" cell_refs="DB-f-801"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r121/p121_reader.py" . DBF121-1-AC2</invocation><expect>DBF121-1-AC2 PASS</expect></criterion>
`DBF121-1-AC2` -- bounds: the portal diff from the class candidate head `7fa808c9` to your head is exactly the two new files (`classSeriesRead.ts` and `class-series-read.test.ts`) and nothing else. Base: FAIL (no change).

<expected_criteria>DBF121-1-AC1,DBF121-1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every source file, every other test, the model and the section, the contract, the issuer's check.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change. The reader is NOT mounted: do not edit `ReportingTab.tsx` or any importer.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the shape above conflicts with the model's row type, report it as a row and keep to this order.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W801-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~801/
portal/src/pages/InvestorReporting/tabs/reporting/classes/classSeriesRead.ts
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/class-series-read.test.ts
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-801.class-series-reader-columnar-document-to-class-rows-not-mounted.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R121_F.md</decomp_doc> round 121, workstream ~F2 (F-SHIP), cell `DB-f-801`.
<owned_cells>DB-f-801</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF121-1-AC1, DBF121-1-AC2 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~801/IRPT_DASHBD.TO-DB-f-801.class-series-reader-columnar-document-to-class-rows-not-mounted.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF121-1-AC1,DBF121-1-AC2` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha; the exported names; the test counts, the mutant result and the typecheck and lint results; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: two new files on a local portal branch; nothing is wired, mounted, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the reader names the route ~S2 will serve and requests nothing.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF121-1-AC1 and AC2 FAIL at base and the checker's pure helpers are exercised by its self-test (7 arms).
lane: the <paths> block IS the grant.
</preflight>
