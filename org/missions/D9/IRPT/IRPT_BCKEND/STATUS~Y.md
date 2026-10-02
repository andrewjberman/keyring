# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (read 23:06Z, until 23:33:47Z, renewed by the loop).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (latest read: batches 177, 178, 186)
and the fold-in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6,
Y-H). Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-02T23:0xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | st14 `f89fc8e731`; Y-3 merged `ce035e9387` (code `bb255c4cb2`, NOT served). No worktree held |
| SERVED: `irpt-status` | `h7H7KgX1FsBu4XTLqqpcMOjMnwRdeL9xlGZPwzhibcg=` since 17:04Z (M2 pool + per-thread Tables + D2 SigV4 + E7b + E6 + item 22, members at `0f70e6156e`), 1024 MB, timeout 29 s. Ledger `irpt-status-m2-d2-r1-20261002` CLOSED 4/4. Rollback: re-promote S3 `9S5jAZLr..` + memory 256 |
| SERVED: PDF route | `GET analysis/requests/{requestId}/pdf`, route `ihirb2s` on `7k3ed8px20` (integrations/8ogp332, authorizer naqxlm) since ~17:59Z. V1-b MATCH 4/4 |
| SERVED: the resident | `/opt/irpt-resident/f89fc8e731-st14` since 22:13:00Z (st14; CTO half batch 188). Rollback root `c657a5966d-st13` on the host |
| SERVED: `irpt-ycharts-generate` | `wjSX3zZoFu2EUintXwZVESW+ac8F+bdRHSWm+YfpmgA=` since ~22:18Z (st14 at `f89fc8e731`). Rollback: re-promote S3 `rtq1e9oT..` (code `E+FqSWwE..`) -- roll back BOTH st14 moves or neither |
| Stored YCharts session | `ycharts/session/current` fence 23, captured 09:45:43Z; its `aws-waf-token` is from that sign-in |
| Push state | LOCAL; CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6 (CTO batch 178; Andrew-direct ~18:1xZ: YCharts approved for cases A, B, C, D and the typo file, one at a time, queue empty)

1. **st14 SERVED** (ledger `irpt-st14-20261002`: U1, U2, D1, D2 closed; **V1 open**). V1 = Y-1 Case A from the page.
   Run 1 (22:25Z) never reached a lookup: the page's `POST analysis/inputs` carried no `selected_tenant`, so the Lambda
   refused the walker's home firm (`IdRefused`, page defect). Sent to `2.0.0_SA_COO~D` (22:35Z) with this seat's word to
   rerun once fixed on DEV. On the rerun: arm the resident journal watch, then `backend_join.py <har> <out> --journal`.
   PASS: `IRPT_RESIDENT_RESOLVE_FUNDS matched=1`, NORMALIZED with `M:TIMXX`, first lookup unchallenged, then READY.
2. **Y-B baselines diverged** -> row S279 (fund ticker fails the whole upload), fixed by st14. Vendor traffic paused since
   19:48Z except V1 (cause named @483cbd3ea5).
3. **Y-3 BUILT and MERGED** (`bb255c4cb2`, merge `ce035e9387`; design `IRPT_MVP_Y/Y3/`): a named ETF as a comparison key,
   identity-checked on the resident before the first mutation. Packet after st14's V1 (generate + resident at one
   commit); the CTO said no PRD half re-opens (batch 189). IB-yr-261 superseded @cab30cf41d.
4. Then Y-2 (Case B, page 2.1 by ~D), Y-4/Y-5 (wire both gates, ruling 5; Case D's proxy SGOV), Y-6 (each case twice).

## Queued irpt-status work

W2-06 (`include=composition`, the frozen AnalysisSubmissionRequest; CTO batch 165) and G3 (render ports for the
Analysis print, CTO batch 175).

## Rows this lane holds

| Row | State |
|---|---|
| S279 | OPEN, BLOCKING, ARMED: fund tickers fail the whole upload. st14 SERVED 22:18Z; disarms on Case A's fund row resolving (V1) |
| S282 | test_generate_installed pins 24 schemas (25 since hop 11's contract); owner `2.0.0_SA_COO~P` |
| S277 | DISARMED S270 (history list <= 6.6 s server time after M2) |
| S263, S253, S231, W94-S2, W91-S1, W92-S1 | for the CVO to close (unchanged) |
| S261 | E7 superseded by E7b (served); for the CVO to close |
| S230 | the resident's own sign-in meets a CAPTCHA; only Andrew's sign-in (option A) restores a session |
| W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

- `irpt-st14-20261002`: U1, U2, D1, D2 closed; V1 (Case A from the page) open.

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
