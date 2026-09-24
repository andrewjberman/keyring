# IRPT Analysis (COO~Y) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE, since 2026-09-23 23:01Z; the Codex seat and its 600 s driver are retired).
Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.4; COO_Y.md and
CONTROL.md apply; CTO reviews directly (no CVO queue). Goal + loop authority:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md` @fc17929b64
(/loop 20m, stop on /verify SOUND or Andrew's stand-down). As of 2026-09-24T13:45Z. Y was paused ~06:45Z-13:00Z (a safeguards dialog; Andrew-direct batch 51 item 1: retry on the same model; MSTR found the seat working, no keys).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-mvp-y-20260922` at `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` |
| Y branch head | `47b2adf6df` (custody interpreter + oracle) over `93ec16f4fe` (resident step 1 reads the bundle; template = liveness) over `7fec957269` |
| CTO acceptance | interpreter ACCEPTED as built (100649); three exact-file integration rows granted to IRPT_Y_ACCESS_INTEGRATION_P at 47b2adf6df |
| Resident (P's receipt 100483, not re-read by Y on the host) | `irpt-analysis-resident.service` active since 09:39:24Z, package `ab2e088b5b` (Y 93ec16f4fe + tokenless transport 8576bec142 + X10 ACTIVE row), enrolled pin 1276035; ledger irpt-resident-cutover-20260924 CLOSED (C1) |
| Session | `ycharts/session/current` AWSCURRENT 02e53a44 (08:56:48Z, run 7 = sixth submission; CRO grade PASS 100466); read 13:44Z |
| Queue | irpt-generation 0 visible / 0 in flight (read 13:44Z) |
| Push state | Y commits LOCAL; origin/CLOUD 827e67ad58 (ls-remote 13:44Z); local CLOUD ahead, MSTR drains |

## Live thread

State: NOT LIVE end to end. Hops 1, 5, 6, 9, 10 closed or reachable (CRO addenda @c7126b5142 / @9a9138d4ab / @b74eb87e67):
the resident is installed and polling, the session is captured and graded, the three Analysis routes are served (batch 42),
the client flags landed on DEV (candidate 4). The first failing hop is 2 (prospect upload) or 4 (custody branch), whichever
composition lands first; both are compositions, neither is a deploy:
- Hop 2 (prospect upload): design owner P (Andrew CALL 3); direction ACCEPTED (CTO 100667) = Y's shape 2 -- the upload POST
  retains and sends ONE RESOLVE_UPLOAD to irpt-generation; the RESIDENT resolves on the host through its own session (one
  batched securities_info GET, resolution only, no prices), freezes, publishes. Y builds the resident half on P's card/word.
- Hop 4 custody branch: the ECONOMIC INTERPRETER is BUILT (Y 47b2adf6df, CTO accepted); P composes behind a ledgered
  FIRM-bucket grant plan (GetObjectVersion on opal-data-assets COT fact_holdings/fact_allocations + KMS; a parquet decoder
  reused from M's holdings runtime by ARN; IRPT_FIRM_REGISTRY; public spellings of the refusal codes).
The first live Analysis submission is Andrew's browser act on Anna's account (acc_d486fc9455d6b2aa18e13af1) on whichever
composition serves first (batch 44); Y's --once is observed on that first job.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Y1 selected custody + owned CSV/XLSX + disposition + catalogue | OFFLINE + one real-object run (custody) | interpreter @47b2adf6df: oracle 15/15, arm (e) vs P's reader, real COT objects admit Anna's 55 positions |
| Y2 immutable normalized input, corrections, reconciliation | OFFLINE ONLY | freeze_accepted_custody over real custody evidence OK; 12.03 Dollars freeze offline |
| Y3 retained acceptance, durable dispatch, idempotency, recovery | INSTALLED, not exercised | resident running (P 100483); five empty polls; no job yet |
| Y4 identity/settings/holdings readback, Overview/Comparison/Multi-Comp PDFs | NOT STARTED (live) | session graded; step 1 reads the bundle, step 2 template = liveness (93ec16f4fe) |
| Y5 extraction/certification into typed report | OFFLINE ONLY | publisher / census 195040 B |
| Y6 polling/history/reload/corrections/downloads | ROUTES SERVED, not exercised | batch 42/43 (P) |
| Y7 one reconciled full trace per required case | NOT STARTED | none |

Offline-only work grades nothing until the live thread is live.

## Write claims

None in flight on Y's branch. Next: the resident half of RESOLVE_UPLOAD, on P's design card and word (CTO 100667).

## Next proof

The first live Analysis submission on Anna's account from Andrew's browser, once a composition serves: the resident consumes the
one job (Y's --once acceptance observed there), vendor PDF, certified AnalysisReport, screen, reload/history, same-revision export,
then `RUNBOOK_1203_LIVE_JOURNEY_20260923.md` for the prospect (12.03) path once hop 2 serves.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Custody composition: CustodyBindingStore on irpt-requests, publication_for (M's HoldingsPublication), the (principal, owner) selection re-shaping, the reader over Y's two ports, grants (GetObjectVersion COT fact_holdings/fact_allocations + KMS; PutItem irpt-requests), a parquet decoder by ARN, IRPT_FIRM_REGISTRY, public refusal spellings | 2.0.0_SA_COO~P | Y 47b2adf6df (build_custody_ports); CTO 100649 items 1-6 | AWAITED behind P's ledgered FIRM-bucket plan |
| Upload composition design card (index / parse / resolve) with the RESOLVE_UPLOAD message shape | 2.0.0_SA_COO~P (Andrew CALL 3) | direction = Y shape 2 (CTO 100667) | AWAITED; Y builds the resident half on the word |
| Resident role writes on irpt-requests (UPLOAD/NORMALIZATION/INPUT) + reads on prospect_inputs / original_holdings | 2.0.0_SA_COO~P (ledgered plan) | CTO 100667 (4) | AWAITED |
| Portal upload screen handling RESOLVING | 2.0.0_SA_COO~P | CTO 100667 (4) | AWAITED |
| 49F / INF custody admission | 2.0.0_SA_COO~Y (measure) then CTO | CUSTODY_FIRM_NOT_ADMITTED stands | NOT STARTED; COT first |
| First live Analysis submission | Andrew (browser) | batch 44 (b) | after a composition serves |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| intake/tests/test_security_resolution.py:31 needs IRPT_LOOKUP_FIXTURE_ROOT (pre-existing; fails alone) | 2.0.0_SA_COO~Y | the next edit to that suite |
| `comp-blast freeze_parsed_portfolio` NOT-FOUND over 28,307 nodes (MSTR 99629/99630) | 2.0.0_SA_COO~Y | a graph question arises for that name |

## Limits

Not proven: installed service, live login/session recovery, real vendor PDF contents, browser E2E, all-firm
publication, holdings readback beyond upload echo, the units/variants/corrections/export matrix. Reserved gates still
ahead: the shared Terraform apply on the ycharts root (P, never-widen), the first automated sign-in (approved under
6fc3f5f785 as the standing host workflow; agent ad hoc vendor calls stay prohibited), and any shared-branch push
(0.0.0_AB_MSTR). No acceptance ID is PASS until the CTO grades a pinned live trace.
