# bd 49F source-download un-freeze — P0 LONG-POLE resolved (06-29 -> 06-30 -> 07-01)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE
**serial:** 0.6.0_AE_PartnerETL | **window:** 2026-07-02 ~14:25Z -> ~18:15Z | **1 commit:** f1f530b2e

## Summary

Andrew-direct P0 LONG-POLE: bd 49F source-download FROZEN @06-29 (gold ran daily on stale
06-29 source; served header data_as_of stuck 06-29). Diagnosed, un-froze end-to-end to the BD
frontier (07-01), served-confirmed on content, closed by CVO (VERIFIED-GREEN) + COO (ACCEPTED).

## Root cause (grounded, Rule 22 — source + live + independent-solver)

The FEED boxes' embedded Playwright login (runner.ts UI-export on bd-transactions/bd-allocations)
is DEAD: SS&C email-OTP MFA times out the 30s nav to bd3.bdreporting.com. NOT a BD-source pause
(custodian data existed) — our bot couldn't authenticate. Evidence: live SSM logs
`s3://opal-data-bd/logs/{realized,transaction,allocation,fees}-download-2026-07-01.log` all fail
"Phase 1: Login -> TimeoutError forURL bd3.bdreporting.com"; compproof solver B-02
(`org/modules/graph/compproof/solver_results_full.json`) concurred; portal probe = 302/UP.
0.7.0~A refined: the DEDICATED auto-login box (i-0fa1846f, bd_49f_auto_login.js) WORKS + mints the
`.bd.identity` cookie nightly (00:00Z); only the feed boxes' OWN login is dead. NOTE: the SSM
`opal-bd-*-download` "Success" status was a FALSE-ADVANCE (exit-0 masks the internal login failure
— never-trust-rc=0; same detection-gap class CVO banked vs inf no-read-key + schwab schedule-fired).

## The fix (Phase-0 of the CVO bd-49f migration brief; NO Andrew action)

The stored `.bd.identity` (SM `blackdiamond/49f/session`, captured_at 2026-07-02T00:02:11Z, box-
minted by i-0fa1846f) was LIVE — probed `GET /datamining/auth/token` -> 200. So NO re-capture.
Bypassed the dead login via the proven REST pull `data/cot/scripts/bronze/cot_bronze_ingest.py`
firm-bound to bd (`BD_S3_BUCKET=opal-data-bd BD_FIRM_ID=49f BD_SESSION_SECRET_ID=blackdiamond/49f/
session BD_BASE=https://bd3.bdreporting.com`; `_assert_firm_separation` fail-closed guard PASSED).

## Deployment sequence (produce-to-served, both legs)

1. Sharp test (Rule 22, CVO bar): pulled allocations 06-30 no-land -> Timestamps **End Date 6/30**,
   32,688 rows = DATA genuinely advanced, not just token=200.
2. 06-30 bronze: REST-pulled + landed forwardfill_v2/{realized,unrealized,transactions,allocations}.
   **transactions 14-day window ERRORs on BD (2x, too heavy) -> used a 3-day window (06/27..06/30);
   End Date still 06-30.**
3. 06-30 silver: allocations via ProcessAllocationFiles (S3-trigger); realized/unrealized/
   transactions via the merge single-file process functions run LOCALLY (merge manifest is
   EC2-local ephemeral -> full merge reprocesses-all/slow; single-file avoids it). All 4 @06-30.
4. Fired `bd-price-update(06-30)` (boto3, 202) -> silver/prices/2026-06-30.parquet ->
   GoldLayerPricesTrigger -> bd-gold-trigger `start_instances` -> gold runner i-01003b035d2988dfb
   booted -> gold_dispatch A_00..D_04 -> served.
5. 06-30 served flipped 16:20Z; runner auto-stopped 16:39Z (post-dispatch recon 16:35Z ->
   `shutdown -h +2`).
6. 07-01 leg (required — MDPF 49F @07-01, else surfaces diverge): pre-staged 07-01 inert bronze
   while 06-30 gold ran; on runner=stopped, landed allocations 07-01 + fired price-update(07-01)
   -> booted 07-01 dispatch -> served flipped **17:51:02Z** (my hard ETA was ~17:50Z).

## Verification (grounded on SERVED content, not mtime — the frozen-but-fresh trap)

- `platinum/firm/header_metrics.json`: data_as_of **06-29 -> 06-30 -> 07-01**; final AUA
  **$1,830,739,641.89**, 2915 clients / 6237 accts (SANE; ~-0.5% DoD = market move, NOT a widen).
- `platinum/firm/dashboard.json`: data_as_of 07-01. ADVI 49F == MDPF 49F @07-01 (consistency MET).
- SEV1 (CVO): `platinum/firm/advisor_nna_canonical.json` (gzipped) data_as_of=**07-01**, gen
  18:03Z — D_00f DID run (dispatch tail 18:04Z, late in GROUP_D); NO partial-surface staleness.
- CVO = VERIFIED-GREEN + no never-widen; COO = ACCEPTED + independently comp-freshness-grounded.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| pipescript | `advi-bd` | PASS | mapped the bd estate (feed EC2s, ProcessAllocationFiles/GoldLayerPricesTrigger, gold runner) |
| comp-freshness | `chain bd` | PASS(read) | grounded the freeze frontier (silver realized FAIL@06-29, gold A_00 FAIL@06-29) |
| comp-which | routing q's | PARTIAL | near-tie router; used it to confirm no tool fit before rail-checked raw aws/grep |
| comp-grep/comp-glob | login/writer/dispatch locates | PASS | found bd3-login refs, D_04 header writer, gold_dispatch.sh |

What worked: comp-freshness cleanly localized the freeze to the silver source layer; pipescript
gave the whole event-chain wiring (S3 triggers). What failed: n/a. Gap: much of the run was
rail-checked raw `aws` (EC2 describe / SSM get-command-invocation / S3 cascade-transition
tracking / content data_as_of) — comp-freshness gives a static chain verdict, not per-object
cascade/dispatch-progression/liveness. A `comp-gold-run <instance>` (stage checkpoints + ETA +
served-flip watch) would have replaced ~10 rail-checked aws calls — coverage-gap candidate.

## Current State (zero-context handoff)

- bd 49F source-download UN-FROZEN end-to-end: silver {allocations,realized,unrealized,
  transactions} + gold + served all @07-01 (BD frontier; 07-02 = T-0, unpublished).
- Deploy-ledger `org/critical_paths/change_management/20260702T1437Z_bd-49f-source-unfreeze-rest-backfill_deploy_completion.md` CLOSED + committed (f1f530b2e).
- gold runner i-01003b035d2988dfb: was running the 07-01 dispatch tail at session log time (D_00f
  ran 18:04Z); auto-shuts-down after its recon.
- 0.7.0~A CLEARED to fire the kill-cookie resilience VERIFY-GATE (my REST pulls done; cookie out
  of my critical path).

## Next Steps

- **[0.6.0_AE_PartnerETL]** (me) DURABLE feed-repoint = ADVI_BDAPIMIG.P1.ae-productionize-runner:
  repoint the scheduled feed pull OFF the dead runner.ts UI-export ONTO the cookie-REST pull
  (`cot_bronze_ingest` firm-bound bd) so the ~daily auto-pull self-heals WITHOUT a manual backfill
  — else the freeze RECURS at the next scheduled feed run. Fold the transactions 14-day-window
  chunking (BD errors on the heavy query) into it.
- **[0.7.0_AE_CloudOps~A]** login-box (i-0fa1846f) durability + the kill-cookie resilience gate.
- **[0.4.0_DS_ClientPlatform]** D_00.portal_aggregates.py:748-749 NNA period window keyed off
  run-date `today`, not `data_as_of` (nna_mtd/qtd=0 across a boundary during a lag) — routed
  162632Z, non-blocking.
- **[2.0.0_SA_COO]** folding all non-blocking follow-ups (txn chunking, fees separate-infra REST,
  nna bug, feed-repoint, D_00f ordering-window) into ADVI_ETLFIX WS-2 (bd source resilience).
- **fees** frozen by the same dead login but SEPARATE infra (bronze/fees/, Fees_OpalCapital_Daily
  template, not in cot_bronze_ingest's table set) + not-AUA-critical — own REST-template follow-up.

## Blockers
None. P0 resolved + closed by CVO+COO. The durable-recurrence-prevention (feed-repoint) is a
follow-on TO, not a blocker on the resolved un-freeze.
