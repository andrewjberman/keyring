# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (latest read: batches 177, 178, 186)
and the fold-in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6,
Y-H). Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-03T05:0xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | Y-4 enrichment merged `d82ba47e4e`; packet `f53e219188` (blob `703359ad2a`), CTO half asked 05:03Z. No worktree held |
| SERVED: `irpt-status` | `6VQejBfsI/P3mfAVSFjLt/ythlcxXxi12cy9hxXhKNg=` since 04:28Z (W2-06 `include=composition`; CTO half batch 204); ledger `irpt-status-w206-20261003` CLOSED 3/3. Rollback: re-promote S3 `wXzz3_gh..` (`h7H7KgX1..`) |
| SERVED: PDF route | `GET analysis/requests/{requestId}/pdf`, route `ihirb2s` on `7k3ed8px20` since 2026-10-02 ~17:59Z |
| SERVED: the resident | `/opt/irpt-resident/828c37c6f7-st17` since 03:04:34Z (Y-4; CTO half batch 199). Rollback root `34088050e0-st16` |
| SERVED: `irpt-ycharts-generate` | `fD2R6OFrT2N086C9Go3e1aA9RKZCP/vfnZCaHCloJTs=` since 03:02Z (Y-4). Rollback: re-promote S3 `oew.wOPK..` (Y-5, `aug0YyWc..`) -- with the resident, all or none |
| SERVED: runner role | Sid `ReadTheEstateKimiKey` (GetSecretValue on `astn/kimi/api-key-*`) since 02:58Z (Y-4 D3) |
| Stored YCharts session | **EVICTED since 2026-10-03 ~00:10Z (row S288)**: every request answers 403. Vendor traffic STOPPED. Remedy: option A at Andrew's time |
| Push state | LOCAL; CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6 (CTO batch 178; Andrew-direct 2026-10-02 ~18:1xZ)

1. **BLOCKED on the session (S288):** no Analysis job can reach READY until the attended sign-in (option A). No vendor
   call until then.
2. **Y-3 SERVED** (ledger `irpt-y3-20261002`: V1 open). IWM admitted and verified; READY waits on the session.
3. **Y-5 packet 1 SERVED** 02:0xZ (ledger `irpt-y5-20261003`: V1 open). V1 = Case A TIMXX -> SGOV and Case D with proxies,
   after Y-3's READY.
4. **Y-4 SERVED** 03:05Z (ledger `irpt-y4-20261003`: U1, U2, D3, D1, D2 closed; V1 open). V1 = the typo file (APPL ->
   AAPL), recording the check gate's elapsed seconds (CTO 104515). Its enrichment (gate total 240 s; Resource
   `astn/kimi/api-key-??????`) is merged `d82ba47e4e` and PACKETED (`Y4E/`, ledger `irpt-y4e-20261003`: U2 closed),
   CTO half asked.
5. After option A, in order: Y-3 READY, Y-5 V1, Y-4 V1, then Y-2 and Y-6.

## Queued work

- W2-06 SERVED (above). Next: G3 (render ports for the Analysis print, CTO batch 175).
- Y-5 packet 2 (the Kimi swap) waits on the web-search QA receipt (`KIMI_WEB_SEARCH_UNVERIFIED` stands).

## Rows this lane holds

| Row | State |
|---|---|
| S279 | DISARMED by S283 (st14 V1 run 3) |
| S284 | OPEN, BLOCKING, ARMED: TIMXX gated -- MEASURED `mutualFundDataUSA` (S287); remedy Y-5 proxy |
| S285 / S288 | the 403s are the evicted session (S288, BLOCKING): option A |
| S286 | CVO: generate bundles carry CRLF members; build from autocrlf=false (mine) |
| S282 | test_generate_installed pins 24 schemas (25 since hop 11's contract); owner `2.0.0_SA_COO~P` |
| S277 | DISARMED S270 (history list <= 6.6 s server time after M2) |
| S263, S253, S231, W94-S2, W91-S1, W92-S1 | for the CVO to close (unchanged) |
| S261 | E7 superseded by E7b (served); for the CVO to close |
| S230 | the resident's own sign-in meets a CAPTCHA; only Andrew's sign-in (option A) restores a session |
| W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

- `irpt-y3-20261002`: V1 open (READY pending the session re-capture).
- `irpt-y5-20261003`: V1 open (after Y-3's READY).
- `irpt-y4-20261003`: V1 open (after option A).
- `irpt-y4e-20261003`: U2 closed; D3, D2 wait on the CTO half; V1 after them.

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/lambda/investor-reporting/intake/{security_resolution,portfolio,resolution_broker}.py`
and their tests; `infra/aws/ec2/investor-reporting-ycharts/**`; `docs/contracts/investor-reporting/v1/routes.json`;
`infra/aws/lambda/investor-reporting/ops/owned_requests.py`; the rows of `irpt-status` and `irpt-ycharts-generate` in
`infra/aws/lambda/ci/lambda-source-map.json`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; this file.

## Parked, each with its owner and the condition that un-parks it

- A deterministic ROWS_UNVERIFIED (a stray row) is still retried four times at 60 s. Owner this seat; un-parks if a
  stray-row refusal recurs after st14 (st14 names its cause in the journal).
- The api root's `CHANGELOG.json` entries for routes `bh7ynom` and `ihirb2s`: outside this seat's surface. Un-parks with
  an exact-file grant or that lane's next entry.
- `record-terraform-deploy.sh investor-reporting` is not run per packet: it stamps every function as deployed at HEAD.
- The node of `ycharts/session/tests/test_host_capture.py` that needs a POSIX host; `test_composition_admission` errors
  only in a combined run (13 of 13 alone). Owner this seat.

## Limits

No fund-holding upload has normalized live. No Comparison or Target Weight report on served code; no real client file
has reached READY. The laptop clock is ~3 s behind AWS (w32time stopped): grade expiries on AWS's Date header.

## Standing directives (carried)

- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` in a worktree.
- A password or cookie is read BY NAME into memory and never printed; an output is read for values before commit.
- Vendor egress only on Andrew's words, each use inside a packet with both halves; a CAPTCHA is Andrew's act.
- A served move needs both never-widen halves; read safe-merge's exit code and tree-check line on every merge.
- A drained worktree is removed the same turn (Andrew-direct ~20:3xZ).
