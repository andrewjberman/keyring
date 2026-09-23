# Owned request reopening: bounded independent review

Reviewer `3.0.0_SA_CVO~Y`; authority
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact COO~Y005743 notice requests this review after active dates work.
Portal pin `38a3ea24412310165f0dfb09912e1997de445631`, feature ancestor628e3571.

**Bounded PASS: 9 independent controls/37 assertions, 5 focused supplied
tests/18 assertions, TypeScript noEmit PASS.** No new defect found within these
controls. All14 integrated Y1-Y7/S1-S7 criteria remain NOT_EVALUATED.

`probe_owned_reopen.test.ts` executes actual OwnedRequestHistory component
functions with manual React hook/effect storage, deferred typed API doubles and
static markup. The actual SectionBlock/RetainedSections render functions run.
`OWNED_REOPEN_38a3ea24.json` preserves exact source hashes, controls and markup;
`OWNED_REOPEN_VALIDATION_38a3ea24.json` records focused supplied output and
TypeScript return codes. Existing node_modules is junctioned into the ignored
exact-pin source snapshot; no dependency install or implementation edits.

## Measured controls

- One initial page calls list with limit25. Every selection, including the same
  ID, freshly reads the issued request before separately reading sections.
  Current-status child receives the selected issued ID, and same-ID reopen
  changes its key to reset that child. No submit function is called.
- A late request from selection A cannot trigger A's sections after B is
  selected. A late section result for A cannot replace B's current section.
- Same-ID reopen immediately clears old visible report data. A subsequent
  denied request shows the access-change message, mounts no status child, and
  does not read report sections again. A separately refused sections read
  produces the explicit unavailable message and no report body.
- Empty visible history with a continuation cursor still exposes Next page.
  The next call sends the exact cursor with limit25. List refresh clears the
  selection/report and returns to the first page with no cursor.
- Replacing the API during a pending history read ignores the earlier API's
  late page. History failure shows an actionable error, not a fabricated empty
  list. Unmounting before history/request/report completion results in zero
  post-unmount state updates under the controlled effect cleanup schedule.
- Retained sections use actual native rendering in ordinal order. UNCERTIFIED
  remains UNSUPPORTED; modeled sections keep MODELED and the actual-performance
  disclaimer. The slice is not promoted into a fabricated full report or
  disclosure document. This fixture has no numeric values, so it does not
  independently regrade numeric formatting.

## Reproduction and limitations

```powershell
$env:IRPT_PORTAL_REVIEW_ROOT='<workspace>/.runtime/codex-seats/3.0.0_SA_CVO~Y/owned-reopen-portal/38a3ea24412310165f0dfb09912e1997de445631'
$env:IRPT_PORTAL_REVIEW_OUTPUT='<absolute path>/OWNED_REOPEN_38a3ea24.json'
bun test org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_owned_reopen.test.ts
```

In that exact portal snapshot, supplied check:
`bun test src/pages/InvestorReporting/tabs/analysis/tests/owned-reopen.test.tsx`;
type check: `bun node_modules/typescript/bin/tsc --noEmit`.
Producer's wider20/81 suite is attributed, not added to this denominator.
PowerShell renders Bun stderr as NativeCommandError records even on success;
the captured native exit code is0 and actual summary is5 PASS/0 FAIL.

AnalysisTab's key includes firm ID, scope fingerprint and revision by inspection.
The full parent tree was not mounted: this is not actual browser/React lifecycle,
cross-firm tab remount or persistent reload evidence. Current status child ID/key
is exercised; its polling lifecycle is not run inside this probe. Transport,
real current authorization, retained services, deployed paths and full export
remain unproven. Exact38a3 predates8dbc's Y-DT01 display repair; this bounded
reopening PASS does not supersede the date closure's exact repair pin.

COO~Y010500 informational notice acknowledges c9e892bf9a and reports later P
backend7915bc9b2c consumed in9dbd74d2c1, portalcf77e5db consumed in096e3e3d,
with success/refusal outer schema/parser fixtures and unprojected_grant map.
Producer reports65 backend/41 portal tests plus route fixture/type checks.
These were not rerun here; no outer-contract or date-closure scope lift.
Original reopen candidate is unchanged. No ACK loop or further action needed
on that informational notice; exact named notices archived after this handoff.

No browser/vendor/cloud call, activation, deployment or push. LOCAL review only.
