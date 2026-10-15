# TO IRPT_DASHBD.TO-DB-f-602 -- the ASSET-CLASS WINDOW VIEW MODEL and its SECTION (FWD-3): a pure model that turns one account's class rows (the `account_class_daily` contract's columns) into each class's contribution over a window, the mix at its two dates, the sum check and the one sentence; and a section component that prints it; NEW files only on a branch cut from PROD, not mounted

<to_id>IRPT_DASHBD.TO-DB-f-602</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~602</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the parallelization ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, Move 2: `~F2` takes FWD-3 "new portal tab sections plus their gold readers", not the default-report files) | **Rows:** IRPT_DASHBD-D2-W602-S<k> | **Decomp cell:** `DB-f-602` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R119_F.md`) | **outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-602` (branch `wk-IRPT_DASHBD-602`); run everything from its root unless a step says the portal. `C:/dev/wk-irpt-dashbd-602/portal` is a PORTAL worktree (its own git repo, branch `wk-IRPT_DASHBD-602-portal`), cut from `origin/PROD` @e0e69da7766d87719571d7e6c0ccf59bf65fcae9 (the last PROD release; this feature is separate from the default-report branch and carries only its own commits). Portal files commit in the portal repo with plain git and your author line (`0.9.0_WK_IRPT_DASHBD~602 <0.9.0_WK_IRPT_DASHBD~602@opal.agent>`); your folder, rows and this order's status commit in the workspace repo with `.tools/safe-commit.sh`. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~602/`. Never push either repo; never commit the workspace `portal` gitlink. `node_modules` is a LINK to the main portal checkout's real install: no `bun install`, no package change, never delete it. Resolve bun with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a file with no uncommitted work of yours. Made-up ids and figures only; no real account id or client figure anywhere. All portal paths below are under `portal/src/pages/InvestorReporting/`. Portal colour law (`portal/CLAUDE.md`, `portal/DESIGN.md`): the canvas is light `#F4F6FA`, containers are white panels with a 1px `#C4CBDB` hairline, ink is navy `#163372`; light text or ghost-white fills are ILLEGAL outside the one band; use the existing panel and token idioms of the neighbouring `tabs/reporting/` components and render nothing that reads light-on-light.

**Why.** FWD-3: a person says in one sentence which class drove the window and how the mix moved, without reading a table; the classes add up to the account; unclassified holdings show as their own class and are never folded away. The gold table `account_class_daily` (`org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json`) holds, per account, per trading day and per class: `market_value_eod` (the class's end-of-day value; the classes of one account-day sum to the account's value) and `class_return_daily` (the class's CONTRIBUTION to the account's daily total return: `(MV_c,t - MV_c,t-1 - NF_c,t) / V_(t-1)`; null whenever `coverage` is not `MEASURED`), with `coverage` one of `MEASURED`, `ACCOUNT_RETURN_NOT_MEASURABLE`, `POSITIONS_PARTITION_ABSENT`, `CLASS_VALUES_DO_NOT_SUM_TO_ACCOUNT`, `LINKED_VALUATION_CHAIN`, `TRADE_FLOW_UNREADABLE`, and `asset_class` one of `cash`, `fixed_income`, `equity`, `structured`, `alternatives`, `commodities`, `unclassified`. A served path for these rows does not exist yet (another cell, `DB-f-601`, maps it), so this cell builds what needs no server: the pure model and the section over rows of exactly that shape. Nothing is mounted, requested or served.

**The cell (`DB-f-602`).**
1. **Read first.** `tabs/holdings/assetClass.ts` (the class vocabulary, the order Cash, Fixed Income, Equity, Structured, Alternatives, Commodities then Unclassified, and the colors: import from it, never copy; it is read-only), `tabs/reporting/PerformanceHeadline.tsx` and `tabs/reporting/AccountsTable.tsx` (the style of a Performance-tab section and its panel idiom), `format.ts` (percent and dollar formatters: reuse), and two existing `__tests__/irpt-dashbd/` tests (`bun:test`, `renderToStaticMarkup`, no server, no network). Run `bun test src/pages/InvestorReporting/__tests__/irpt-dashbd` once before any edit (base: record the failing-test count).
2. **The model** `tabs/reporting/classes/classWindowModel.ts` (NEW). Export `type ClassDailyRow = { account_id: string; business_date: string; asset_class: string; market_value_eod: number; class_return_daily: number | null; coverage: string }`, `buildClassWindowModel(input)` and `classSentence(model)`. The input is `{ rows: readonly ClassDailyRow[]; start: string; end: string; accountValues?: readonly { business_date: string; market_value_eod: number }[] }` (all rows are ONE account's; `start` is the window's opening anchor date, the mix date it opens on; `end` its last date). Rules, all pure (no clock, no DOM):
   - The window's days are the trading days `d` present in the rows with `start < d <= end`. The mix is taken at `start` and at `end` (rows must exist on both dates, else the result is NOT_MEASURED with reason `WINDOW_NOT_COVERED`).
   - A day is measured only when EVERY row of that day has `coverage` `MEASURED` and a non-null `class_return_daily`. If any window day or any of the two mix dates is not measured, the model is `{ kind: 'NOT_MEASURED', reason, words }` where `reason` is the first non-`MEASURED` coverage value met (in date order, then enum order), or `WINDOW_NOT_COVERED`; `words` is one plain sentence per reason in client-safe English that names no code, no table and no vendor (for example "Asset-class performance is not available for this period: the account's return could not be measured on some days."); never a figure beside it.
   - Otherwise `{ kind: 'MEASURED', window: {start, end}, accountReturnPct, classes, sentence, checks }`. The account's daily return on a day is `r_t` = the sum over classes of `class_return_daily`; the account's window return is `Π(1 + r_t) - 1` (as a percent). A class's contribution over the window is `sum over days of C_(t-1) * contribution_c,t`, where `C_(t-1) = Π over earlier window days of (1 + r_s)`, `C = 1` before the first day (so the classes' contributions add up to the account's window return EXACTLY; this is the sum rule). `classes` is one line per class that is non-zero in value at either mix date or has a non-zero contribution, in the class order, with: `asset_class`, `label` (from `assetClass.ts`; `unclassified` reads "Unclassified"), `startWeightPct` and `endWeightPct` (the class's share of the account's value at each mix date), `weightChangePp` (end minus start), `contributionPp` (percentage points), all rounded for display only in the component, never in the model. `unclassified` is a class like any other: listed whenever non-zero, never merged into another class, never dropped.
   - `checks`: `{ contributionsSumToReturn: boolean (the sum of `contributionPp` equals `accountReturnPct` within 1e-9), valuesSumToAccount: boolean | null }` where the second compares, at each mix date, the sum of the classes' `market_value_eod` with `accountValues` when given (within 0.01) and is `null` when not given; if `accountValues` is given and a mix date does not sum, the model is NOT_MEASURED with reason `CLASS_VALUES_DO_NOT_SUM_TO_ACCOUNT` (the classes must add up to the account or nothing prints).
   - `classSentence(model)`: for MEASURED: "<Driver> drove the window, adding <x.xx> points to the account's <y.yy>% return. <Mover> rose|fell from <a.a>% to <b.b>% of the account." where the driver is the class with the largest absolute `contributionPp` and the mover the class with the largest absolute `weightChangePp`; when the largest absolute weight change is under 0.05 points the second sentence is "The mix barely moved."; a driver or mover that is `unclassified` is named "Unclassified holdings" (never skipped); a negative contribution reads "taking <x.xx> points off" instead of "adding"; for NOT_MEASURED the sentence is the model's `words`.
3. **The section** `tabs/reporting/classes/AssetClassSection.tsx` (NEW): `AssetClassSection({ model }: { model: ClassWindowModel })` renders, inside the panel idiom of the neighbouring components, `data-slot="asset-class-section"`, a heading "How each asset class performed", the SENTENCE first (one `<p data-slot="asset-class-sentence">`), then a table in the class order (class with its color swatch from `assetClass.ts`, share at the start, share at the end, change in points, points added to the return) and a footnote "The classes add up to the account's return." (MEASURED only). NOT_MEASURED renders the heading and the model's `words` and NO table and NO figure. Every figure is formatted by the existing formatters or a local percent-points formatter with one decimal for shares and two for points; a `unclassified` row is labelled "Unclassified" and sits last; no clock.
4. **Tests** (NEW files only; `bun:test`; made-up rows):
   - `__tests__/irpt-dashbd/class-window-model.test.ts`, at least 10 tests whose titles contain, between them, the words `contribution` (a hand-computed three-class, four-day window: each class's contribution, the account return), `mix` (the weights at the two dates), `sum` (the contributions sum to the account return exactly; the class values sum to the account at each date; a planted mismatch gives NOT_MEASURED `CLASS_VALUES_DO_NOT_SUM_TO_ACCOUNT`), `unclassified` (listed when non-zero, last in the order, never merged; named "Unclassified holdings" as driver), `window` (only days after `start` up to `end`; a window that does not cover both mix dates is `WINDOW_NOT_COVERED`), `coverage` (one non-MEASURED row makes the whole window NOT_MEASURED with that reason and no figure) and `sentence` (the driver and the mover, "barely moved", a negative driver). Use at least one fixture whose answer you compute BY HAND in a comment, not by the model.
   - `__tests__/irpt-dashbd/class-section.test.tsx`, at least 6 tests whose titles contain, between them, the words `section` (the slot and the heading), `table` (rows in the class order), `sentence` (first, and equal to `classSentence(model)`), `absent` (a NOT_MEASURED model prints its words, no table and no digit of a figure), `unclassified` (its row last and labelled) and `not measured` and `order` (cash before fixed income before equity ... before unclassified).
   - ONE temporary mutant you make and revert yourself: change the contribution weighting so that `C_(t-1)` is dropped (a plain sum of daily contributions), show at least two model tests fail, then `git checkout --` the file. The final head holds only the new files.
5. **Gates, once, after your last portal commit:** from the portal worktree `bun run typecheck` and `bun run lint` (0 errors each) and `bun test src/pages/InvestorReporting`: the failing-test names after must be a subset of those before. Do not use `test.todo` (this portal's typecheck refuses it).
6. **Record** `BUILD_R119.json` in your folder with exactly: `portal` {`branch` "wk-IRPT_DASHBD-602-portal", `base` "e0e69da7766d87719571d7e6c0ccf59bf65fcae9", `head`, `files_changed`}, `model_exports` (the list of exported names), `rules_pinned` (a list of words, one per rule of step 2 you pinned by a test), `tests` {`model_pass`, `section_pass`, `suite_before_fail`, `suite_after_fail`}, `mutant_failed_tests` (the integer), `typecheck_rc`, `lint_errors`, `pushed` false, `deployed` false.

<criterion id="DBF119-1-AC1" cell_refs="DB-f-602"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r119/p119_fwd3.py" . DBF119-1-AC1</invocation><expect>DBF119-1-AC1 PASS</expect></criterion>
`DBF119-1-AC1` -- `class-window-model.test.ts` carries titles with the seven words `contribution`, `mix`, `sum`, `unclassified`, `window`, `coverage` and `sentence`, and `bun test` on it passes with 0 failures and at least 10 tests. Base: FAIL (no file).
<criterion id="DBF119-1-AC2" cell_refs="DB-f-602"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r119/p119_fwd3.py" . DBF119-1-AC2</invocation><expect>DBF119-1-AC2 PASS</expect></criterion>
`DBF119-1-AC2` -- `class-section.test.tsx` carries titles with the seven words `section`, `table`, `sentence`, `absent`, `unclassified`, `not measured` and `order`, and `bun test` on it passes with 0 failures and at least 6 tests. Base: FAIL (no file).
<criterion id="DBF119-1-AC3" cell_refs="DB-f-602"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r119/p119_fwd3.py" . DBF119-1-AC3</invocation><expect>DBF119-1-AC3 PASS</expect></criterion>
`DBF119-1-AC3` -- bounds: the portal diff from the PROD release `e0e69da7` to your head holds at least one new file under `tabs/reporting/classes/` and touches only files under that folder and the two new test files. Base: FAIL (no new file).

<expected_criteria>DBF119-1-AC1,DBF119-1-AC2,DBF119-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `tabs/holdings/assetClass.ts`, every existing `tabs/reporting/` file (including `ReportingTab.tsx`: the mount is the issuer's hookup and is not part of this cell), every other portal file, the contract, every existing test, the issuer's check.
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no `bun install`, no package change.
- **Inert means inert.** Nothing imports the new files outside their own tests: the section is not mounted and nothing requests the rows.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a rule of step 2 contradicts the contract's columns or cannot be pinned by a hand-computed test, file a BLOCKING row naming the rule and stop on it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W602-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~602/
portal/src/pages/InvestorReporting/tabs/reporting/classes/
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/class-window-model.test.ts
portal/src/pages/InvestorReporting/__tests__/irpt-dashbd/class-section.test.tsx
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-602.class-window-view-model-and-section-new-files-not-mounted.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R119_F.md</decomp_doc> round 119, workstream ~F2 (F-SHIP), cell `DB-f-602`.
<owned_cells>DB-f-602</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF119-1-AC1, DBF119-1-AC2, DBF119-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~602/IRPT_DASHBD.TO-DB-f-602.class-window-view-model-and-section-new-files-not-mounted.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF119-1-AC1,DBF119-1-AC2,DBF119-1-AC3` BEFORE the flip (one comma-separated argument); pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the portal head sha and the new files; the exported names; the rules each test pins; the mutant's failing-test count; the test counts and the typecheck and lint results; anything off-task (as row ids). Made-up values only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: new portal files on a local branch; nothing is mounted, wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the rows' served path is cell DB-f-601's question.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF119-1-AC1 to AC3 FAIL at base and the checker's pure helpers are exercised by its self-test (10 arms).
lane: the <paths> block IS the grant.
</preflight>
