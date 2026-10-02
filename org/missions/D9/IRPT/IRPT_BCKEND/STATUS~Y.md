# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (read 21:41Z, until 22:07:04Z, renewed by the loop).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (latest read: batches 177, 178, 186)
and the fold-in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6,
Y-H). Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-02T21:4xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | st14 merged `f89fc8e731` (code `de5e0c6878`); generate row repin merged `f1cede95dd`. No worktree held |
| SERVED: `irpt-status` | `h7H7KgX1FsBu4XTLqqpcMOjMnwRdeL9xlGZPwzhibcg=` since 17:04Z (M2 pool + per-thread Tables + D2 SigV4 + E7b + E6 + item 22, members at `0f70e6156e`), 1024 MB, timeout 29 s. Ledger `irpt-status-m2-d2-r1-20261002` CLOSED 4/4. Rollback: re-promote S3 `9S5jAZLr..` + memory 256 |
| SERVED: PDF route | `GET analysis/requests/{requestId}/pdf`, route `ihirb2s` on `7k3ed8px20` (integrations/8ogp332, authorizer naqxlm) since ~17:59Z. V1-b MATCH 4/4 |
| SERVED: the resident | `/opt/irpt-resident/c657a5966d-st13` (st13). st14 tar uploaded, NOT installed |
| SERVED: `irpt-ycharts-generate` | `E+FqSWwETrwJ9Gd1..`. **UPLOADED, NOT APPLIED:** version `y3LRNAoPvGmdWYZSNb5moyTiEDvo8055` (sha `wjSX3zZo..`, st14 at `f89fc8e731`) is the key's LATEST: no untargeted apply of the ycharts root until st14's D1 |
| Stored YCharts session | `ycharts/session/current` fence 23, captured 09:45:43Z; its `aws-waf-token` is from that sign-in |
| Push state | LOCAL; CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6 (CTO batch 178; Andrew-direct ~18:1xZ: YCharts approved for cases A, B, C, D and the typo file, one at a time, queue empty)

1. **Y-B baselines DONE, diverged** (`IRPT_MVP_Y/YB_BASELINES/OUTCOME_YB_AND_WAF_CAUSE_20261002.md` @483cbd3ea5): typo and
   Case D both end NEEDS_CORRECTION with ONE file-level RESOLVE_RETRY_EXHAUSTED. Cause: a fund ticker (TIMXX, FBIFX)
   fails classify_batch for the whole batch -- row **S279** (BLOCKING, this seat). Brief 2 item 4.1 is real.
2. **st14 = S279's fix, BUILT, MERGED, offline-proven** (`de5e0c6878`): the "M:<ticker>" fund row answers the bare
   ticker its display id names; the portfolio sends YCharts that id; a bad fund row refuses THAT row by name; the
   journal names the refusing check. CTO batch 186: proven offline first (done; 16 tests, negative control 17 of 19
   fail on HEAD). **Packet next**: resident (st13 -> st14) + `irpt-ycharts-generate` (both carry the intake modules;
   `uploads.py:450` replays a frozen input on the Lambda). Ledger `irpt-st14-20261002`: U1, U2 closed; D1, D2, V1 open.
3. **Vendor traffic PAUSED** since 19:48Z (five WAF challenges). Cause named (outcome file section 2): the bisect's
   retry burst on a ten-hour-old WAF token. Resume after st14: one job at a time, >= 10 min apart, Y-1 first; a
   first-read challenge stops traffic and is reported (remedy: the attended sign-in, option A, at Andrew's time).
4. **Y-H**: `live_walk/backend_join.py` published to `2.0.0_SA_COO~D` (@44da23a117); ~D's harness
   `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/yh/yh-submit-case.mjs` (b6e3b75e56) is ready.
   ~D runs Case A when st14 serves and the queue is empty (msg 104401) -- this seat tells ~D.
5. Then Y-2/Y-3 (comparisons with an upload; a ticker such as IWM as a comparison key, ruling 4 -- name the CONTRACTS
   row if its meaning changes), Y-4/Y-5 (wire the check and swap gates, ruling 5; Case D's proxy SGOV), Y-6 (each case
   twice).

## Queued irpt-status work

W2-06 (`include=composition`, the frozen AnalysisSubmissionRequest; CTO batch 165) and G3 (render ports for the
Analysis print, CTO batch 175).

## Rows this lane holds

| Row | State |
|---|---|
| S279 | OPEN, BLOCKING, ARMED: fund tickers fail the whole upload. Disarms on st14 served + Case A's fund row resolving |
| S277 | DISARMED S270 (history list <= 6.6 s server time after M2) |
| S263, S253, S231, W94-S2, W91-S1, W92-S1 | for the CVO to close (unchanged) |
| S261 | E7 superseded by E7b (served); for the CVO to close |
| S230 | the resident's own sign-in meets a CAPTCHA; only Andrew's sign-in (option A) restores a session |
| W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

- `irpt-st14-20261002`: U1, U2 closed; D1 (generate targeted apply), D2 (resident install), V1 (Case A first lookup).

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
