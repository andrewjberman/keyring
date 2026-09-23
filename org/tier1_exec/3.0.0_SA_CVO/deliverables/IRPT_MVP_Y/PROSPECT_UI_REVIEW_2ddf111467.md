# Bounded prospect UI review

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Portal pin: `2ddf111467348c4c81ae28e0c0b8aa80e1239152`, repository
`C:/Users/AndrewBerman/Desktop/irpt-mvp-y-portal-20260922`.

Bounded result: supplied **11/11 tests, 50 assertions PASS**; independent
**9/9 controls, 57 assertions PASS**; `tsc -b --noEmit` **PASS**. No new defect
found within these controls. This does not grade integrated acceptance:
**0 PASS / 0 FAIL / 14 NOT_EVALUATED** remains unchanged.

## What was executed

Source was archived from the exact portal commit into the ignored seat runtime
review directory. Installed dependencies were reused through a junction; no
package install or dependency update. Bun version was 1.3.9. The initial full
archive extraction stopped at an unrelated absolute symlink under etl; no tests
ran on that partial extraction. The retry extracted only the pinned src tree,
package.json, TypeScript configs and vite.config.ts with the safe tar data filter.
That completed and all checks below ran against that snapshot.

Supplied commands, from the pinned snapshot:

```powershell
bun test ./src/pages/InvestorReporting/tabs/analysis/tests/prospect.test.tsx ./src/pages/InvestorReporting/__tests__/mvp-upload/upload.test.ts
node node_modules/typescript/bin/tsc -b --noEmit
```

The six prospect tests and five shared upload tests passed. The shared tests
include response identity/hash binding and NO-HANDLER/zero-transport refusal.
This consumes the checked-in producer fixture; it does not regenerate a guarded
backend response or independently repeat P's complete R-P09 retest.

Independent command, from the main workspace, with environment variables set to
the pinned runtime snapshot and the owned evidence JSON output path:

```powershell
bun test ./org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_prospect_ui.test.ts
```

`probe_prospect_ui.test.ts` imports the actual ProspectComposer and LiveClient.
It provides manual useState/useRef storage through the installed React dispatcher,
calls actual returned handlers and renders their returned tree to static markup.
This exercises handler logic but does not model React scheduling, DOM events,
focus, browser file controls, remount integration, or real browser rendering.
All submission/upload successes use explicit callbacks; LiveClient's no-handler
test supplies a transport counter and records zero transport. Fetch is forbidden
by the probe. No vendor, cloud or deployment operations were performed.

## Independent controls

| Control | Observed result |
|---|---|
| Ambiguous upload and repeated same-tick handler | One initial API call; in-flight controls disabled; retry serializes the identical body/token and exact large-cent CSV bytes |
| Explicit refresh, followed by ambiguous response | Old review/generate panel cleared; new token carries the previous input ID; subsequent retry carries exactly that refresh body |
| Ambiguous analysis submission | Same request ID/body on retry; one argument with no custody scope; input ID only, null client/snapshot, empty accounts/comparisons, Overview |
| Deliberate report title edit | New request identity with the new title, preserving the normalized input |
| Successful analysis | Issued request/stage shown; acceptance button disabled; copy distinguishes acceptance from later generation/verification |
| Correction and valuation option edit | Correction reason shown, no Generate action; deliberate currency correction creates a new upload token with declared USD |
| Competing file reads | Later selection remains the chosen filename and bytes after the earlier read completes |
| Presentation strings and row bound | `9007199254740993.01` remains exact in markup; 101 source rows explicitly show only 100; ROW99 present and ROW100 absent |
| NO-HANDLER and remount limits | LiveClient upload/retry makes zero transport calls; a new component state loses the earlier attempt and, after selecting the same file, creates a new token |

The table groups related observations; the executable has exactly nine controls.
The presentation test deliberately changes the supplied response in a callback;
it tests display formatting only, not response-envelope or artifact hash validity.
Evidence JSON `PROSPECT_UI_2ddf111467.json` contains source hashes and each exact
control name/outcome. No tests were changed after a failing candidate assertion;
the first executable independent run passed all nine controls. Bun did not emit
the JSON through the initial process-exit hook, so the evidence writer moved to
afterAll and the unchanged scenarios were rerun. These runs are not double-counted.

## Boundaries and peer evidence

The retry guarantee is in-memory only. Actual React remount is not simulated;
fresh hook storage demonstrates loss of request state. AnalysisTab keys this
composer by firm/scope/revision, so persistent recovery and identity retention
across actual navigation, reload and scope changes remain integration obligations.
The visible source table caps at 100 rows with an explicit count and no pagination
in this component. This is not proof of complete per-row interactive review.
Only Overview is selectable here; comparison builders are not a rendered selector.

No route handler, authenticated runtime composition, actual M resolver, vendor
upload/readback/create, polling/history recovery or released report/export was
proved. Source hashes and offline type checks do not establish those behaviors.
All 14 integrated criteria remain NOT_EVALUATED, including Y6 reload/reopen.

Exact CVO~P notice 20260922T233240Z reports **R-P09 CLOSED** in peer review
`65a3aedf72`, portal `c86a5eb5`, backend `5add22ca9f`: regenerated guarded
responses/hash/schema and 24 supplied plus 11 unchanged assertions PASS.
Reference: `IRPT_MVP_P/UPLOAD_CONTRACT_RETEST_C86A.md`. This closure remains
peer-attributed; these counts are not folded into Y's tests. NO-HANDLER and
zero-transport limits remain unchanged.

The COO~Y notice separately reports backend `090c819803` canonical
tenant_firm_id/revision1/immutable acceptance identity repair and 45 tests plus
24 subtests PASS, consumed by P. That is producer-attributed information, not
an independently executed backend review in this portal task.

Push state LOCAL. No implementation files changed and no push performed.

-- 3.0.0_SA_CVO~Y
