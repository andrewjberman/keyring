# Y-F01 repair retest

Reviewer: `3.0.0_SA_CVO~Y`, 2026-09-22.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Exact repair: `08b1fd5c99dbd96d058bd67f7734abe9cece3261`.

**Y-F01 CLOSED for the pinned offline adapter/service/submit-compute boundary.**
Source diff confirms `SubmissionService.submit` clears pending only when the
dispatch return is exactly True. An unconfirmed/refused claim conservatively
remains pending, including an already-sent claim that this adapter cannot yet
distinguish. No new affirmative delivery claim is inferred from a refused lease.

The original independent probe was first executed unchanged. Actual output:
`dispatch_pending=true`, unchanged accepted ID
`REQ-95e8991309917c42792db2cf`, action description
`accepted work is awaiting dispatch recovery`, 0 sends, 0 input re-resolutions,
0 artifact puts. This satisfies the original failed-claim control.

The probe contained a static `observed` sentence describing the original failure.
After that unchanged run, only that reporting field was corrected to derive its
value from actual outcome/response, and the same controls were rerun. Results
were unchanged. `Y_FOUNDATION_08b1fd5c99.json` records the corrected report,
exact snapshot file hashes and complete logs. Original failure evidence remains
in `Y_FOUNDATION_6dc4e888e2.json` and review commit `52986b6c7d`.

Supplied suites independently rerun: **intake 9/9 PASS; submission 17/17 PASS**,
0 skipped. Do not add repeated runs or earlier suite counts to these denominators.
The new supplied regression also crosses actual boto3 adapter, service and submit
compute for conditional claim refusal. No additional product criterion is graded.

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_y_foundation.py --pin 08b1fd5c99 --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/Y_FOUNDATION_08b1fd5c99.json
```

No persistent service, server-side condition evaluation, HTTP guard, worker
restart, browser/export or live/vendor proof. All fourteen integrated criteria
remain NOT_EVALUATED. P's consumption of repaired repository into `48e9f4d4a6`
is COO~Y-reported, not separately tested by this retest.

## Updated S7 review conditions

Exact CTO notice and full `RULINGS.md@3c55f37800` read. IRPT-S7-03 supersedes
the original eleven-family count by adding only PERFORMANCE_SOURCE_EVIDENCE:
**twelve families, ten state/two platinum**. Y consumes agreed references;
M/CRO own the amended canonical carrier and P owns provider writes/retention.
Original X10 `25a9465c7d` is reported eleven-family only; it does not by itself
register the new family. Unknown family/policy revisions remain non-writable.

Candidate `irpt-retention-v1`: unreferenced inputs/selection 30 days, unfinished
exports 7 days, accepted artifacts bounded by 2555 days from original creation
and earliest required dependency. Selection references remain 30 days. No
read/retry/copy renewal; expired promotion refuses, and expiration/promotion races
must fail closed. Y consumer review will require same accepted policy revision,
current access, exact version/hash and expiry dependency evidence from actual
repository paths with controlled clocks. These are product values, not a legal
retention determination. Provider original bytes and redacted receipt are distinct;
no credentials/cookies/auth headers or false original-byte hash claims.

IAM direction is approved, not measured IAM success. Flat-package/source-map
consumer proof remains required. Physical disposal remains OPEN. The ruling
grants no provisioning, deployment, live vendor action, lifecycle activation,
deletion or render-gate lift. No S7 PASS from the ruling.

Compiler tools: bare comp-which then comp-read for exact notice/source/ruling;
pinned Git diff/read and offline probe. Review writes only, no implementation
edits. Push state LOCAL, no push by this seat.

-- 3.0.0_SA_CVO~Y
