# Issued-job status UI review

Reviewer: `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact portal pin: `940333dfcd12dd4329a35c4b3834ebb9dafa791c` from
`C:/Users/AndrewBerman/Desktop/irpt-mvp-y-portal-20260922`.

Bounded result: **13 supplied tests / 59 assertions PASS; nine independent
controls / 58 assertions PASS; TypeScript PASS**. No new defect found in these
controls. Integrated criteria remain **0 PASS / 0 FAIL / 14 NOT_EVALUATED**.

## Reproduction and method

The exact src tree and package/TypeScript/Vite configuration were safely
extracted from the pinned commit into the ignored seat runtime review directory.
Installed node_modules were reused through a junction, without an install or
dependency update. Bun was 1.3.9.

Supplied checks, from the snapshot:

```powershell
bun test ./src/pages/InvestorReporting/tabs/analysis/tests/prospect.test.tsx ./src/pages/InvestorReporting/__tests__/mvp-upload/upload.test.ts
node node_modules/typescript/bin/tsc -b --noEmit
```

Independent command, with IRPT_PORTAL_REVIEW_ROOT set to the exact snapshot and
IRPT_PORTAL_REVIEW_OUTPUT set to the owned evidence path:

```powershell
bun test ./org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_job_status.test.ts
```

The probe imports the actual ProspectJobStatus, provides manual React hook
storage and dependency/cleanup handling, then invokes its real effect body.
Deferred promises and a controlled timer queue expose ordering without waiting
on real time. Returned elements are rendered to static markup. This is an
offline effect-scheduling model, not actual React scheduling, StrictMode,
browser events, timer throttling, navigation or real network cancellation.
Status responses are explicit fixtures; fetch is forbidden. No real status,
submission, vendor, cloud or deployment operation was performed.

`JOB_STATUS_UI_940333dfcd.json` records hashes of the actual component and its
composer call site, every control outcome, and every requested timer delay.
The first independent executable run passed all nine controls; no scenario was
changed to make a candidate assertion pass.

## Independent results

| Control | Observed result |
|---|---|
| LOADING cycle | Exactly 12 ID-only reads, 11 scheduled delays of 5000ms, then no timer; unexpected submit method would throw |
| Unresolved read | No next timer or overlapping read; Check status disabled until resolution, then one timer |
| READY or UNAVAILABLE/FAILED result | Polling stops; refusal reason remains visible |
| Read error after LOADING | Prior status clears, error message displays, no timer; explicit Check status starts a new read and can display READY |
| Cleanup with queued timer | Timer removed and no further read |
| Cleanup with in-flight read | Late success or error ignored; no status update or new timer |
| API/request-ID change | Old late response ignored; new issued ID and READY result remain; no old timer |
| Explicit Check status while awaiting timer | Old timer canceled; immediate new read begins a fresh 12-read maximum cycle |
| Missing reader or empty request ID | No status call or timer; unavailable/error display rather than invented progress |

The cadence is five seconds **after a LOADING response resolves**, not a fixed
wall-clock interval. Twelve reads is a per-effect-cycle maximum; an explicit
check deliberately starts a new cycle. Cleanup ignores a response already in
flight; it does not abort the underlying transport request.

The actual composer mounts this component only after an issued response and
keys it by issued request ID. The reviewed status component has no submission
path, custody scope construction, browser cache or report link. Its helpers read
the issued ID; no durable recovery of that ID is implemented by this change.

## Remaining integration limits

No actual browser execution, persisted identity after reload, runtime job-status
route response, authenticated access/revocation response, durable job/revision
binding or released report retrieval was established. The prior in-memory
composer/remount limit remains. Actual M normalized custody is NOT READY per
the sender's update; `9e57397730` selected-read contract inspection is attributed
to COO~Y, not an independently executed custody review here.

No full Y6 or S4 grade follows from this bounded result. All 14 integrated
criteria remain NOT_EVALUATED. Push state LOCAL; no implementation change or push.

-- 3.0.0_SA_CVO~Y
