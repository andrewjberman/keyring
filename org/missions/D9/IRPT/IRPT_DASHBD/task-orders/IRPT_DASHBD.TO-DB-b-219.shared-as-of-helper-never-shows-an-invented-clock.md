# TO IRPT_DASHBD.TO-DB-b-219 -- the SHARED AS-OF HELPER NEVER SHOWS AN INVENTED CLOCK: a date-only as-of prints its date words and no time on every page that uses the shared helpers; a clock prints only when the source supplied a real timestamp; one candidate branch in the portal, never pushed

<to_id>IRPT_DASHBD.TO-DB-b-219</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~176</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>110</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-110 ANALYSIS section 1 (row "The shared as-of fix") and section 2 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_110_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W176-S<k> (start at S1) | **Decomp cell:** `DB-b-219` (decomposition section 112) | **outcome_ref:** Andrew's P1 of 2026-10-14 (the CTO's frame for round 110); no FWD id is claimed | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-176` (branch `wk-IRPT_DASHBD-176`); run everything from its root unless a step says the portal. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~176/`. `C:/dev/wk-irpt-dashbd-176/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-176-portal`), cut from the last PROD release `6a5926fc` (never from DEV: the branch must carry only its own commits). Portal files commit in the portal repo with plain git and your author line; records, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. **Never push either repo, never create or push a `cand/` branch, never commit the workspace `portal` gitlink**: the issuer names the candidate branch at your tip and registers its approval row. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. This cell touches NO client data and reads none.

**Why.** Andrew read an as-of on a page as "as of 5 PM ET, October 14" at 2:37 PM that same day. The portal's shared date helpers turn a date-only as-of (`YYYY-MM-DD`, no time of day in the source) into an instant at 5 PM Eastern and then print that clock, so every footer and header on the pages that use them tells the reader a time the data never had. The rule, ruled by the CTO: **a date-only value never shows an invented clock; a clock prints only when the source supplies a real timestamp.** The fix is ONE change in the shared helpers, so every page that uses them gets it; it is a client-facing candidate, so Andrew approves it before it reaches DEV (not your concern: you only build the branch).

**The cell (`DB-b-219`).** Read these first, in the portal worktree, and print each file's line count: `src/lib/dateUtils.ts` (the helpers `create5pmETDate`, `parseDataAsOf`, `getCanonicalAsOfDate`, `formatDataAsOfDisplay`, `formatPanelTimestamp`, and the private `formatDateWithOrdinal`), `src/components/DataAsOf.tsx` (the private `formatDataAsOfCompact`, which also builds its own 5 PM instant, and `DataAsOfCompact`), `src/ui/components/panels/PanelFooter.tsx`, and the tests `src/lib/__tests__/create5pm-et.test.ts`, `src/pages/Positioning/panels/footer-date-format.test.ts`, `src/pages/Positioning/shared/PageEnd.test.tsx`, `src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-45.face-batch.test.tsx`.

1. **The rule in `src/lib/dateUtils.ts`.** `formatPanelTimestamp(timestamp, dataAsOf, frequency)`: when `timestamp` is a real, parseable timestamp, it prints exactly what it prints now (`"October 14th, 2026, 2:37p ET"`); when only a full date `YYYY-MM-DD` is available, it prints the ordinal date words and NO clock (`"October 14th, 2026"`) and must not call `create5pmETDate` for that path. The `YYYY-MM`, `YYYY`, `frequency` `monthly` and `annually` outputs do not change. `formatDataAsOfDisplay(dataAsOf, { includeTime: true })` on a full date prints `"October 14, 2026"` (the no-time words) because its input carries no time. **`create5pmETDate`, `parseDataAsOf` and `getCanonicalAsOfDate` KEEP returning the 5 PM instant**: it is the calculation instant (stale-data tests, day counts, period resolution) and no display reads it. Update their doc comments to say it is for calculation only and is never a display value.
2. **The rule in `src/components/DataAsOf.tsx`.** `formatDataAsOfCompact` on a full date prints `"Oct 14, 2026"` with `includeTime` true or false; delete the private 5 PM instant it builds (`utcHour`). Keep the `includeTime` prop accepted (it has no effect on a date-only value) and export `formatDataAsOfCompact` by name so a test can call it. Fix the two doc comments that say it shows "5:00 PM ET".
3. **Two pages build their own fake clock and hand it to the footer as if it were a source timestamp:** `src/pages/Macroeconomics/tabs/VolatilityTab.tsx` (about line 705, a `T17:00:00` string with a guessed offset) and `src/pages/Valuation/tabs/RiskPremiumTab.tsx` (about line 218, `T17:00:00-05:00`). Change each to hand the footer the date only (pass the date as `dataAsOf`, leave `timestamp` null/undefined), the minimum edit that stops the invention.
4. **Callers.** Every other caller keeps working unchanged; a caller that today strips the invented clock with a regex (`src/pages/SecurityAnalysis/components/LeadPanel.tsx`, `src/pages/SecurityAnalysis/dateWords.ts`, `src/pages/InvestorReporting/format.ts`) becomes a no-op strip: do NOT edit those files unless a test of theirs fails. Caller classes at the PROD release, for your census (print the denominator): 32 tracked files under `src/` reference `create5pmETDate`, `formatPanelTimestamp`, `DataAsOfCompact`, `formatDataAsOfDisplay`, `parseDataAsOf` or `getCanonicalAsOfDate`; 5 of them are tests or a harness, 2 are the definitions, so **25 are caller files**. DATE-ONLY callers (pass `null`/`undefined` and a date): `ModelPortfolios.tsx`, `CategoryViewTree.tsx`, `ModelPortfolioModal.tsx`, `ui/components/PageEnd.tsx`, `Positioning/tabs/HoldingsTab.tsx`, `Positioning/panels/PositioningSummary.tsx`, `SecurityAnalysis/dateWords.ts`, `SecurityAnalysis/components/LeadPanel.tsx`, `InvestorReporting/format.ts`. MIXED callers (a manifest `timestamp` when present, else its `data_as_of`): `PanelFooter.tsx`, `IndexPerformanceModal.tsx`, `MarketRegimeModal.tsx`, `RSIModal.tsx`, `MacroTimeSeriesModal.tsx`; a manifest timestamp is the SOURCE's own and keeps printing its clock. REAL-TIMESTAMP callers: the four `AdvisorIntelligence/_partners/*/index.tsx` pages (`generated_at`), `SecurityAnalysis/components/ThesisCards.tsx`. COMPACT component: `Attribution/components/AssetAllocationSummary.tsx`. The rest use the calculation helpers only. Count your own run of the census by those classes and record the three integers.
5. **Tests.** (a) NEW file `src/lib/__tests__/as-of-no-invented-clock.test.ts`, which prints `VERDICT: ASOF-NO-INVENTED-CLOCK-OK` when every case holds and a FAIL verdict line with the failures otherwise. Its cases, each asserted exactly: `formatPanelTimestamp(null, d)` and `formatPanelTimestamp(undefined, d)` for `2026-10-03`, `2026-01-09`, `2026-03-08`, `2026-11-01` write `October 3rd, 2026`, `January 9th, 2026`, `March 8th, 2026`, `November 1st, 2026` (no colon, no `ET`); a real timestamp `2026-10-14T14:37:00-04:00` writes `October 14th, 2026, 2:37p ET` and `2026-01-09T17:00:00-05:00` writes `January 9th, 2026, 5:00p ET` (a source clock still prints); `('2026-01', monthly)` writes `January 2026` and `('2026', annually)` writes `2026`; `formatDataAsOfDisplay('2026-10-14', { includeTime: true })` writes `October 14, 2026`; `formatDataAsOfCompact('2026-10-14', true)` and the same call with false write `Oct 14, 2026`; `DataAsOfCompact` rendered with `react-dom/server` `renderToStaticMarkup` on `2026-10-14` holds no colon and no `ET`; the calculation helpers are unchanged (`create5pmETDate(2026, 10, 3).toISOString()` is `2026-10-03T21:00:00.000Z`, and `parseDataAsOf('2026-10-14').date` is the 21:00:00Z instant). **The negative case:** with `setSystemTime(new Date('2026-10-14T18:37:00Z'))` from `bun:test` (2:37 PM Eastern on the day) a value dated `2026-10-14` writes `October 14th, 2026` with no clock, and the same with the system time at `2026-10-14T22:30:00Z` (after 5 PM): the words do not depend on the reading time; restore the real clock after. (b) Re-pin `src/lib/__tests__/create5pm-et.test.ts`: it still asserts that `create5pmETDate` returns 5 PM New York in every runtime zone (keep every `getUTCHours` assertion), and its footer clause now asserts the DATE words only for a date-only input and `5:00p ET` only for a real timestamp built from the same date; update its header comment. Edit `footer-date-format.test.ts`, `PageEnd.test.tsx` and `iv-e-45.face-batch.test.tsx` only if one fails, and only by the minimum edit, named in your report. (c) ONE temporary mutant: put the invented clock back in `formatPanelTimestamp`'s date-only path; the new test must fail; revert it with `git checkout -- <file>`.
6. **Gates.** In the portal: `bun run lint` and `bun run typecheck` after your last commit (0 errors); the whole-scope suite once before any edit as the base and once after (`bun test` from the portal, output to `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~176/`), `new_failing_ids` []. Commit the portal work on `wk-IRPT_DASHBD-176-portal` as one or more commits.
7. **Record** `ASOF_R110.json` in your folder: `portal` {`branch` "wk-IRPT_DASHBD-176-portal", `commit` (the tip), `files_changed` (portal-relative paths)}, `callers` {`files_scanned`, `date_only_callers`, `real_timestamp_callers`} (integers from your census), `tests` {`new_file`, `mutant_failed` true, `lint_errors`, `typecheck_errors`, `suite_before`, `suite_after` {`new_failing_ids`}}, `pushed` false, `deployed` false, `reads` (the page-level reads you did, in words). Counts, paths and words only.

**Issuer amendment (row `W176-S1`): one golden is re-pinned.** The byte-for-byte golden `portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-120.golden/model_portfolios_mount.before.html` (read by `iv-e-120.total-base-in-the-card.test.tsx` test (b)) holds the invented clock in the ModelPortfolios footer ("September 29th, 2026, 5:00p ET"). That one footer sentence is the behaviour this order removes, so the golden is now in your grant for exactly that edit: change ONLY the date sentence in that file to the date-only words your fix prints ("September 29th, 2026"), nothing else in the file, and leave `iv-e-120.total-base-in-the-card.test.tsx` itself untouched. Name this edit in your report with the others. Then re-run the whole-scope suite: `new_failing_ids` must be [] and DB110-4-AC3 must read PASS.

<criterion id="DB110-4-AC1" cell_refs="DB-b-219"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_asof.py" . DB110-4-AC1</invocation><expect>DB110-4-AC1 PASS</expect></criterion>
`DB110-4-AC1` -- the new test file exists and holds the required cases (including the before-5-PM negative case under `setSystemTime`), and `bun test` on it passes under TZ=UTC and under TZ=America/Los_Angeles, printing its verdict line. Base: FAIL (no test file).
<criterion id="DB110-4-AC2" cell_refs="DB-b-219"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_asof.py" . DB110-4-AC2</invocation><expect>DB110-4-AC2 PASS</expect></criterion>
`DB110-4-AC2` -- the old pin of the invented clock is gone (`create5pm-et.test.ts` no longer asserts `endsWith(', 5:00p ET')` on a date-only footer and still asserts the 5 PM instant), and the four neighbour test files (`create5pm-et`, `footer-date-format`, `PageEnd`, `iv-e-45.face-batch`) pass together. Base: FAIL (the old pin stands).
<criterion id="DB110-4-AC3" cell_refs="DB-b-219"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r110/p110_asof.py" . DB110-4-AC3</invocation><expect>DB110-4-AC3 PASS</expect></criterion>
`DB110-4-AC3` -- no product file under `portal/src` builds its own `17:00:00` timestamp; `formatPanelTimestamp` makes no 5 PM instant for display; `DataAsOf.tsx` builds none; and `ASOF_R110.json` is complete: a portal commit on `wk-IRPT_DASHBD-176-portal` descending from the PROD release `6a5926fc`, files under `src/`, the caller census (at least 25 files), a failing mutant, lint 0, typecheck 0, no new failing test, pushed false, deployed false. Base: FAIL (no record; two pages build a 17:00 string).

<expected_criteria>DB110-4-AC1,DB110-4-AC2,DB110-4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every caller listed in step 4 except where a step names it, the issuer's check files and every file outside `portal/src/`.
- **No push, no deploy, no candidate branch.** No portal or workspace push, no `cand/` branch, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Scope.** One shared change. A page-specific string edit beyond steps 3 and 4 is out of scope: if you find another page that builds its own clock, file a row naming the file and line and keep going.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the checker's convention, not the code, is wrong, file a BLOCKING row naming the clause and stop on it. Never weaken an assertion of an existing test beyond the minimum edit the new behaviour requires, and name each such edit. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W176-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~176/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-219.shared-as-of-helper-never-shows-an-invented-clock.md
portal/src/lib/dateUtils.ts
portal/src/components/DataAsOf.tsx
portal/src/lib/__tests__/create5pm-et.test.ts
portal/src/lib/__tests__/as-of-no-invented-clock.test.ts
portal/src/pages/Macroeconomics/tabs/VolatilityTab.tsx
portal/src/pages/Valuation/tabs/RiskPremiumTab.tsx
portal/src/pages/Positioning/panels/footer-date-format.test.ts
portal/src/pages/Positioning/shared/PageEnd.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-45.face-batch.test.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-120.golden/model_portfolios_mount.before.html
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 112 (round 110), cell `DB-b-219`.
<owned_cells>DB-b-219</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB110-4-AC1, DB110-4-AC2, DB110-4-AC3 (all mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~176/IRPT_DASHBD.TO-DB-b-219.shared-as-of-helper-never-shows-an-invented-clock.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB110-4-AC1` (and the other two) BEFORE the status flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the three caller integers and the files by class that you counted; the exact sentence a date-only footer prints now beside the one it printed before; which existing tests you edited (name each and say why); whether the mutant failed the new test and which case caught it; lint, typecheck and the suite before and after; the portal tip commit; any row ids (including any other page that builds its own clock). Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a shared date-words helper and two page footers in a portal branch that is never pushed; nothing is wired, served or deployed here (the issuer registers the candidate for approval separately).
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB110-4-AC1, AC2 and AC3 FAIL at base (no test file, the old pin stands, no record), and the worker's temporary mutant is the difference control for AC1.
lane: the <paths> block IS the grant.
</preflight>
