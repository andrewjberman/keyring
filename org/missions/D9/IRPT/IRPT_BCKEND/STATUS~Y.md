# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.4 (COO_Y.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: the 20m goal loop (cron 87624362) reading `python .tools/drive-mode.py read IRPT_BCKEND~Y` each tick (C11, CTO
100819). Lease FAST until 2026-09-24T21:13:40Z at 18:18Z. Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`.
As of 2026-09-24T20:27Z. Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/STATUS.md` (13:45Z).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-mvp-y-20260922` at `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` |
| Workspace candidate pin | `58280c8dd4` (Y2 deferred arms: XLSX, weights, correction) over `522afcfd17` (test module-identity fix, P 100860) over `d16b7c8743` (hop-3 input-owner lookup) over `10a16bd89d` (attribution fix) over `bb1eb7f92b` RESOLVE_UPLOAD (CVO handoff 18:29Z) over `b398d27731` |
| P composition patch | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/P_UPLOAD_COMPOSITION_20260924.{patch,md}`: hops 2+3, applies clean to P `9efaf2850e` |
| Portal candidate pin | n/a (portal candidates go to `2.0.0_SA_COO~D`) |
| Deployed artifact pin | resident `irpt-analysis-resident.service`, package `ab2e088b5b` (P receipt 100483; not re-read by Y) |
| Push state | Y branch LOCAL; not on origin (brief section 2: origin holds only `CLOUD`) |

## Live thread

State: NOT LIVE end to end. Hops 2+3 SERVED (P 100866). Y verified: generate `LdjdnnLh...` 19:49:52Z Active, and its
`upload_resolution.py` / `uploads.py` / `maintained_sources.py` are byte-identical to Y d16b7c8743 / P 19b38e2f22.
The live route `POST .../analysis/inputs` goes to the generate integration. Queue and DLQ are 0. The resident is
`f624e8a72f` per P. First failing hop was 1 in the PORTAL, fixed by ~D at `088386fe` (20:1xZ). It sends the legacy `csv_base64` body (refused
`CSV_LANE_NOT_COMPOSED`), and its adapter throws on RESOLVING. The published contract admits neither the template lane
nor RESOLVING. Fixes are handed over: contract patch to P, portal spec to ~D.

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Y1 custody + owned CSV/XLSX + disposition | OFFLINE + one real-object run | interpreter @47b2adf6df, oracle 15/15 |
| Y2 immutable normalized input | OFFLINE ONLY | deferred lane @bb1eb7f92b + @58280c8dd4: Dollars 12.03, XLSX, TARGET_WEIGHT with notional, missing notional refused by name, correction lineage, race arm; SHARES refused by name (no price source) |
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

Live hops 1a-1d, then 3-10, per `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/RUNBOOK_1203_LIVE_JOURNEY_20260923.md`
(revised 19:1xZ for the deferred path). P deploys; Andrew posts the 12.03 template as an Opal viewer. Y reads the resident's
journal and the rows and records the digests. Y never runs `--once` against the live queue: the service is the one consumer.
P has cherry-picked Y's three commits (`2d6937be5e`, `e8dd4cdfc7`, `9efaf2850e` on its branch); `522afcfd17` fixes the
full-suite red P found (100860) and must ride the same rebuild.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Upload design card + word | 2.0.0_SA_COO~P | CTO 100667 | not needed to build; Y built on the accepted shape |
| Patch applied (`a58859baa7`); ledger `irpt-upload-hop2-20260924` R1 resident package, then L1 generate rebuild (runbook B2 order) | 2.0.0_SA_COO~P | `P_UPLOAD_COMPOSITION_20260924.md` | AWAITED |
| `ports["ordinary_authorizer"]` producer (partner viewers) and `get_catalogue` (hop 3) | 2.0.0_SA_COO~P | generate_installed absent producers | AWAITED; an Opal viewer is not blocked by it |
| Restore M's viewer seam `485b69c061` onto `_scope/maintained_sources.py` (8 conflict hunks vs `bc3727b3a3`) | 2.0.0_SA_COO~P (M reads semantics) | Y 100842; M 100846: `test_maintained_viewer_sources.py` 27/27 | DONE at P `19b38e2f22` (LOCAL); rides the hop-2 deploy |
| Grants for hop 2 (both roles) | 2.0.0_SA_COO~P | P `54bc1359f4` APPLIED 19:22Z | DONE: Y reach-check 19:3xZ, DDB PutItem + SQS SendMessage allowed, with a negative control |
| Portal: template body, RESOLVING adapter + poll, `.xlsx` (spec `D_UPLOAD_TEMPLATE_LANE_SPEC_20260924.md`) | 2.0.0_SA_COO~D | ~D 100877: edits 1-3 LANDED on portal DEV `088386fe` (the 5174 server's HEAD, Y read 20:2xZ); edit 4 (wire regen) waits on the contract patch | DONE for the live run |
| First live 12.03 upload (file `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv`) | Andrew (browser, Opal login, localhost:5174) | runbook hops 1a-1d | AWAITED -- notified 20:2xZ. Baseline 20:2xZ: irpt-requests UPLOAD#/NORMALIZATION#/INPUT# = 0 in cottonwood, 49financial and inflection (consistent query; control SELECTION# cottonwood = 14). Contract landed at P `a47102cc8f` (100878). |
| Contract: request template lane + result RESOLVING/findings (`P_UPLOAD_CONTRACT_20260924.patch`, `--check` clean at P `7f6b5589f6`) | 2.0.0_SA_COO~P | Y 20:1xZ | AWAITED |
| Custody composition (hop 4) | 2.0.0_SA_COO~P | Y 47b2adf6df; decoder read `CUSTODY_DECODER_RUNG2_READ_20260924.md` (rung 2 empty for py3.12: 18 layers, 2 pyarrow, both py3.11) | AWAITED |
| First live Analysis submission | Andrew (browser) | after a composition serves | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| `intake/tests/test_security_resolution.py:31` needs IRPT_LOOKUP_FIXTURE_ROOT | 2.0.0_SA_COO~Y | the next edit to that suite |
| `reports/tests/test_generate_installed.py:58` expects 22 schemas; the tree holds 23 (fails at P's own tip) | 2.0.0_SA_COO~P | P's next edit to that suite |
| The Y worktree is a sparse checkout (`firm_destination_policy.json` is S), so two `test_broker_recovery_evidence` arms fail only here | 2.0.0_SA_COO~Y | a suite needs that file on this worktree |

## Limits

Nothing on hop 2 is deployed or exercised live. The resident resolution uses no price source: SHARES templates answer
NEEDS_CORRECTION by name until one is composed. No vendor call is made by this seat; the resident's one batched
`securities_info` GET is the standing host-workflow authorization (CTO 100667 (1)).
