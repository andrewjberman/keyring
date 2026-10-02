# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (latest read: batches 177, 178, 186)
and the fold-in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6,
Y-H). Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-03T00:0xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | st14 `f89fc8e731`; Y-3 + S284 journal `9bbb38f7a0` (NOT served); generate repin merge `2209801a3f`. No worktree held |
| SERVED: `irpt-status` | `h7H7KgX1FsBu4XTLqqpcMOjMnwRdeL9xlGZPwzhibcg=` since 17:04Z (M2 pool + per-thread Tables + D2 SigV4 + E7b + E6 + item 22, members at `0f70e6156e`), 1024 MB, timeout 29 s. Ledger `irpt-status-m2-d2-r1-20261002` CLOSED 4/4. Rollback: re-promote S3 `9S5jAZLr..` + memory 256 |
| SERVED: PDF route | `GET analysis/requests/{requestId}/pdf`, route `ihirb2s` on `7k3ed8px20` (integrations/8ogp332, authorizer naqxlm) since ~17:59Z. V1-b MATCH 4/4 |
| SERVED: the resident | `/opt/irpt-resident/f89fc8e731-st14` since 22:13:00Z (st14; CTO half batch 188). Rollback root `c657a5966d-st13` on the host |
| SERVED: `irpt-ycharts-generate` | `wjSX3zZo..` (st14) since ~22:18Z. **UPLOADED, NOT APPLIED:** version `jFLj0wX5..` (`VZvhvWRM..`, Y-3 at `9bbb38f7a0`) is the key's LATEST -- no untargeted apply of the ycharts root until Y-3's D1 |
| UPLOADED, NOT INSTALLED | resident tar `irpt-resident-9bbb38f7a0-st15.tar.gz` (`af49e702..`) and its script (`1a282fd4..`) |
| Stored YCharts session | `ycharts/session/current` fence 23, captured 09:45:43Z; its `aws-waf-token` is from that sign-in |
| Push state | LOCAL; CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6 (CTO batch 178; Andrew-direct ~18:1xZ)

1. **st14 DONE**: ledger `irpt-st14-20261002` CLOSED @0b3816f0b7. V1 closed on Case A run 3 (CTO batch 192): one read, no WAF,
   the fund row attributed, one row named (100, TIMXX). S283 disarms S279. TIMXX is unusable on the account (row S284,
   INFERRED entitlement-gated) -> Case A's READY moves to Y-5 (user-named proxy). No entitlement spend unless Andrew asks.
2. **Y-3 + S284 journal: packet `Y3/NEVER_WIDEN_SIGNOFF_PACKET_Y3_20261002.md` (blob 8bebf7ea86), CTO half ASKED 23:56Z.**
   Ledger `irpt-y3-20261002`: U1, U2 closed; D1, D2, V1 open. V1-a ULT+IWM Multi-Comp on the 12.03 file; V1-b AAPL+TIMXX
   upload-only measures S284 (`gated=`). One job at a time, >= 10 min apart, solo gate; a first-read WAF challenge stops.
3. **Then Y-4/Y-5** (design `Y45/Y45_DESIGN_CHECK_AND_SWAP_GATES_20261002.md` @22c39d8977): packet 1 = check gate + correction
   revision + user-named proxy (Case A's TIMXX, Case D's SGOV); packet 2 = Kimi swap after the web-search QA. Then Y-2, Y-6.
4. **Y-H** works on real HARs (`backend_join.py`); ~D's harness `yh-submit-case.mjs` sends `selected_tenant` (portal DEV 39aa21c2).

## Queued irpt-status work

W2-06 (`include=composition`, the frozen AnalysisSubmissionRequest; CTO batch 165) and G3 (render ports for the
Analysis print, CTO batch 175).

## Rows this lane holds

| Row | State |
|---|---|
| S279 | DISARMED by S283 (st14 V1 run 3) |
| S284 | OPEN, BLOCKING, ARMED: TIMXX entitlement-gated (INFERRED); measured by Y-3's V1-b; remedy Y-5 proxy |
| S282 | test_generate_installed pins 24 schemas (25 since hop 11's contract); owner `2.0.0_SA_COO~P` |
| S277 | DISARMED S270 (history list <= 6.6 s server time after M2) |
| S263, S253, S231, W94-S2, W91-S1, W92-S1 | for the CVO to close (unchanged) |
| S261 | E7 superseded by E7b (served); for the CVO to close |
| S230 | the resident's own sign-in meets a CAPTCHA; only Andrew's sign-in (option A) restores a session |
| W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

- `irpt-y3-20261002`: U1, U2 closed; D1, D2, V1 open (CTO half asked).

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
