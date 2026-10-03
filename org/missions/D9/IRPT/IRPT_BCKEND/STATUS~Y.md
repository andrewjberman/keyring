# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (latest read: batches 177, 178, 186)
and the fold-in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6,
Y-H). Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-03T06:3xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | G3 SERVED, evidence `6cbe9144e7`. No worktree held |
| SERVED: `irpt-status` | `hC6PramtsshP40jo3OJ91k4qxlHndylJWxHLIjIdw/E=` since 06:28:49Z (G3 render-grant ports + `IRPT_EVIDENCE_BUCKET`; W2-06 since 04:28Z). Policy `irpt-status-render-grant-read-policy` (I1). Rollback: re-promote S3 `4CQOSM..` (`6VQejBfs..`), drop the variable, delete the policy |
| SERVED: PDF route | `GET analysis/requests/{requestId}/pdf`, route `ihirb2s` on `7k3ed8px20` since 2026-10-02 ~17:59Z |
| SERVED: the resident | `/opt/irpt-resident/a6f6e7165e-st18` since 05:52:20Z (Y-4 enrichment: gate total 240 s; CTO half batch 209). Rollback root `828c37c6f7-st17` |
| SERVED: `irpt-ycharts-generate` | `fD2R6OFrT2N086C9Go3e1aA9RKZCP/vfnZCaHCloJTs=` since 03:02Z (Y-4). Rollback: re-promote S3 `oew.wOPK..` (Y-5, `aug0YyWc..`) -- with the resident, all or none |
| SERVED: runner role | the estate Kimi secret through ONE carrier (`local.kimi_secret_arn` = `api-key-??????`, both statements) since 05:5xZ; a sibling name reads implicitDeny. Login and session ARNs keep `-*` (parked for a ruling) |
| Stored YCharts session | **EVICTED since 2026-10-03 ~00:10Z (row S288)**: every request answers 403. Vendor traffic STOPPED. Remedy: option A at Andrew's time |
| Push state | LOCAL; CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6 (CTO batch 178; Andrew-direct 2026-10-02 ~18:1xZ)

1. **BLOCKED on the session (S288):** no Analysis job can reach READY until the attended sign-in (option A). No vendor
   call until then.
2. **Y-3 SERVED** (ledger `irpt-y3-20261002`: V1 open). IWM admitted and verified; READY waits on the session.
3. **Y-5 packet 1 SERVED** 02:0xZ (ledger `irpt-y5-20261003`: V1 open). V1 = Case A TIMXX -> SGOV and Case D with proxies,
   after Y-3's READY.
4. **Y-4 SERVED** 03:05Z (ledger `irpt-y4-20261003`: U1, U2, D3, D1, D2 closed; V1 open). V1 = the typo file (APPL ->
   AAPL), recording the check gate's elapsed seconds (CTO 104515; the journal field `elapsed_s=` is installed). Its
   enrichment is SERVED (ledger `irpt-y4e2-20261003` closed; the first try `irpt-y4e-20261003` rolled back on its own
   stop -- a second statement granted the same name).
5. After option A, in order: Y-3 READY, Y-5 V1, Y-4 V1, then Y-2 and Y-6.

## Queued work

- G3 SERVED 06:28Z (CTO half batch 212). V1 arm 1: 18 of 18 non-render reads equal. Arm 2 (a foreign render token
  refused) is `2.0.0_SA_COO~P`'s (told 06:32Z). Arm 3 rides E4's first Analysis export.
- Y-2 needs no backend change: AnalysisSubmissionRequest admits `input_id` with variant `comparison` and one key; Y-3's
  V1-a measured the upload + comparison path admitted. Y-2 is the live run after option A.
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
- `irpt-status-g3-20261003`: U1, I1, D1 closed; V1 open (arm 2 `~P`, arm 3 at E4).

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
