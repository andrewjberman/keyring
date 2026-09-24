# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.4 (COO_Y.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: the 20m goal loop (cron 87624362) reading `python .tools/drive-mode.py read IRPT_BCKEND~Y` each tick (C11, CTO
100819). Lease FAST until 2026-09-24T21:13:40Z at 18:18Z. Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`.
As of 2026-09-24T18:25Z. Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/STATUS.md` (13:45Z).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-mvp-y-20260922` at `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` |
| Workspace candidate pin | `b398d27731` (custody interpreter, CTO-accepted); RESOLVE_UPLOAD item in flight |
| Portal candidate pin | n/a (portal candidates go to `2.0.0_SA_COO~D`) |
| Deployed artifact pin | resident `irpt-analysis-resident.service`, package `ab2e088b5b` (P receipt 100483; not re-read by Y) |
| Push state | Y branch LOCAL; not on origin (brief section 2: origin holds only `CLOUD`) |

## Live thread

State: NOT LIVE end to end. Hops 1, 5, 6, 9, 10 are closed or reachable (CRO addenda). First failing hop: 2 (prospect
upload) or 4 (custody branch), whichever composition serves first. Hop 2 is the item below.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Y1 custody + owned CSV/XLSX + disposition | OFFLINE + one real-object run | interpreter @47b2adf6df, oracle 15/15 |
| Y2 immutable normalized input | OFFLINE ONLY | 12.03 Dollars freeze offline |
| Y3 acceptance, dispatch, recovery | INSTALLED, not exercised | P 100483 |
| Y4 vendor PDFs (3 variants) | NOT STARTED live | session graded |
| Y5 certified typed report | OFFLINE ONLY | publisher |
| Y6 polling/history/reload/downloads | ROUTES SERVED, not exercised | P batch 42/43 |
| Y7 reconciled full trace per case | NOT STARTED | none |

## Write claims

Item: the resident half of RESOLVE_UPLOAD (CTO 100667 shape 2), plus the upload service's deferred half, which P's own
docstring (`reports/generate_installed.py`) names Y's surface:
- `infra/aws/lambda/investor-reporting/intake/uploads.py::UploadService` (deferred mode, `resolve_deferred`)
- `infra/aws/lambda/investor-reporting/intake/upload_resolution.py` (new: message, conditional state adapter, service builders)
- `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py::ResidentAssembly.execute` (`resolve_upload` kind)
- their tests under `intake/tests/` and `ycharts/generate/tests/`

## Next proof

Offline: a template upload answers RESOLVING, and the resident resolves it through a replayed `securities_info` response to
NORMALIZED 12.03. The run also covers the race arm (a lost conditional flip returns the retained winner) and a named
NEEDS_CORRECTION. Live: Andrew's browser submission once P composes the Lambda half and grants the resident its writes.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Upload design card + word | 2.0.0_SA_COO~P | CTO 100667 | AWAITED; Y builds on the accepted shape now |
| Lambda composition of the deferred service (send port + table) in `generate_installed.py` | 2.0.0_SA_COO~P | the item's pin | AWAITED |
| Resident role writes on irpt-requests (UPLOAD/NORMALIZATION/INPUT) + S3 prospect prefixes | 2.0.0_SA_COO~P (ledgered) | CTO 100667 (4) | AWAITED |
| Portal upload screen handling RESOLVING | 2.0.0_SA_COO~D | CTO 100744 | AWAITED |
| Custody composition (hop 4) | 2.0.0_SA_COO~P | Y 47b2adf6df | AWAITED |
| First live Analysis submission | Andrew (browser) | after a composition serves | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `intake/tests/test_security_resolution.py:31` needs IRPT_LOOKUP_FIXTURE_ROOT | 2.0.0_SA_COO~Y | the next edit to that suite |

## Limits

Nothing on hop 2 is deployed or exercised live. The resident resolution uses no price source: SHARES templates answer
NEEDS_CORRECTION by name until one is composed. No vendor call is made by this seat; the resident's one batched
`securities_info` GET is the standing host-workflow authorization (CTO 100667 (1)).
