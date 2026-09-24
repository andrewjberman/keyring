# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.4 (COO_Y.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: the 20m goal loop (cron 87624362) reading `python .tools/drive-mode.py read IRPT_BCKEND~Y` each tick (C11, CTO
100819). Lease FAST until 2026-09-24T21:13:40Z at 18:18Z. Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`.
As of 2026-09-24T18:47Z. Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/STATUS.md` (13:45Z).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-mvp-y-20260922` at `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` |
| Workspace candidate pin | `10a16bd89d` (attribution fix for ordinary viewers) over `bb1eb7f92b` RESOLVE_UPLOAD both halves (CVO handoff 18:29Z) over `b398d27731` |
| P composition patch | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/P_UPLOAD_COMPOSITION_20260924.{patch,md}`: applies clean to P `aa3aabe2ca` |
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
| Y2 immutable normalized input | OFFLINE ONLY | 12.03 Dollars freeze offline; deferred path @bb1eb7f92b (RESOLVING -> resident -> NORMALIZED 12.03, race arm, NEEDS_CORRECTION by name) |
| Y3 acceptance, dispatch, recovery | INSTALLED, not exercised | P 100483 |
| Y4 vendor PDFs (3 variants) | NOT STARTED live | session graded |
| Y5 certified typed report | OFFLINE ONLY | publisher |
| Y6 polling/history/reload/downloads | ROUTES SERVED, not exercised | P batch 42/43 |
| Y7 reconciled full trace per case | NOT STARTED | none |

## Write claims

None in flight. RESOLVE_UPLOAD landed @bb1eb7f92b and @10a16bd89d. The patch for P's `reports/generate_installed.py` was
written in scratch worktree `C:/Users/AndrewBerman/Desktop/irpt-y-pcompose-20260924` (branch `y-scratch-pcompose-20260924`,
never committed, never pushed). Y makes no commit on P's branch.

## Next proof

Live hop 2: once P composes the Lambda half and the resident grants (Y 100823), Andrew's browser posts the 12.03 template.
The POST answers RESOLVING, and the resident's journal shows one `IRPT_RESIDENT_POLL handled=1`. The re-POST then answers
NORMALIZED 12.03. Next build item while that waits: the hop-3 composition patch (`ports["uploads"]`,
`load_prospect_owner`, the prospect branch of `RoutedSubmissionService`), in the same form. The 49F/INF measurements are done;
admission is P's composition act (CTO 100711).

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Upload design card + word | 2.0.0_SA_COO~P | CTO 100667 | not needed to build; Y built on the accepted shape |
| Apply the hop-2 patch + cherry-pick bb1eb7f92b, 10a16bd89d; rebuild/deploy generate + resident | 2.0.0_SA_COO~P | `P_UPLOAD_COMPOSITION_20260924.md` | AWAITED |
| `ports["ordinary_authorizer"]` producer (partner viewers) and `get_catalogue` (hop 3) | 2.0.0_SA_COO~P | generate_installed absent producers | AWAITED; an Opal viewer is not blocked by it |
| Resident role grants: irpt-requests UPLOAD#/NORMALIZATION#/INPUT#; S3 original_holdings get, prospect_inputs put | 2.0.0_SA_COO~P (ledgered) | CTO 100667 (4), msg 100823 | AWAITED |
| Portal upload screen polling RESOLVING by re-POST | 2.0.0_SA_COO~D | Y interface 18:29Z | AWAITED |
| Custody composition (hop 4) | 2.0.0_SA_COO~P | Y 47b2adf6df | AWAITED |
| First live Analysis submission | Andrew (browser) | after a composition serves | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `intake/tests/test_security_resolution.py:31` needs IRPT_LOOKUP_FIXTURE_ROOT | 2.0.0_SA_COO~Y | the next edit to that suite |
| `reports/tests/test_generate_installed.py:58` expects 22 schemas; the tree holds 23 (fails at P's own tip) | 2.0.0_SA_COO~P | P's next edit to that suite |

## Limits

Nothing on hop 2 is deployed or exercised live. The resident resolution uses no price source: SHARES templates answer
NEEDS_CORRECTION by name until one is composed. No vendor call is made by this seat; the resident's one batched
`securities_info` GET is the standing host-workflow authorization (CTO 100667 (1)).
