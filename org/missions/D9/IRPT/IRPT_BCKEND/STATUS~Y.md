# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` (latest read: batches 177, 178, 186)
and the fold-in `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6,
Y-H). Reviewer `3.0.0_SA_CVO` (grades pins after the fact). As of 2026-10-03T00:4xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | Y-3 + S284 journal `9bbb38f7a0` SERVED. No worktree held |
| SERVED: `irpt-status` | `h7H7KgX1FsBu4XTLqqpcMOjMnwRdeL9xlGZPwzhibcg=` since 17:04Z (M2 pool + per-thread Tables + D2 SigV4 + E7b + E6 + item 22, members at `0f70e6156e`), 1024 MB, timeout 29 s. Ledger `irpt-status-m2-d2-r1-20261002` CLOSED 4/4. Rollback: re-promote S3 `9S5jAZLr..` + memory 256 |
| SERVED: PDF route | `GET analysis/requests/{requestId}/pdf`, route `ihirb2s` on `7k3ed8px20` (integrations/8ogp332, authorizer naqxlm) since ~17:59Z. V1-b MATCH 4/4 |
| SERVED: the resident | `/opt/irpt-resident/9bbb38f7a0-st15` since 00:05:11Z (Y-3; CTO half batch 194). Rollback root `f89fc8e731-st14` |
| SERVED: `irpt-ycharts-generate` | `VZvhvWRMqD6mdaF8COT5JcUcnMxdvzCJe82Gs/9cnRk=` since ~00:09Z (Y-3). Rollback: re-promote S3 `y3LRNAoP..` (st14) -- both moves or neither |
| Stored YCharts session | **EVICTED since ~00:10Z (row S288)**: every request answers 403; the resident's refresh failed (`AUTH_FAILED:NO_AUTHENTICATED_PROBE`). Vendor traffic STOPPED. Remedy: option A at Andrew's time (asked of the CTO 00:42Z) |
| Push state | LOCAL; CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6 (CTO batch 178; Andrew-direct ~18:1xZ)

1. **BLOCKED on the session (S288):** no Analysis job can reach READY until the attended sign-in (option A). Asked of the CTO
   00:42Z for routing to Andrew. No vendor call until then.
2. **Y-3 SERVED** (ledger `irpt-y3-20261002`: U1, U2, D1, D2 closed; V1 open). Measured: IWM admitted at submission,
   identity verified 1 of 1; READY pending the session. V1-b measured S284 = `mutualFundDataUSA` (S287).
   Outcome `Y3/V1_CONTROL/OUTCOME_Y3_V1_AND_CONTROL_20261003.md`.
3. **st14 DONE** (S279 fixed; wording corrected per batch 196). Case A's READY -> Y-5 (TIMXX is gated).
4. **Y-5 packet 1 next (offline build now):** corrections ride the upload's options in the PRD's `{finding_code,
   approved_by, from_value, to_value}` shape; the user-named proxy (Case A TIMXX, Case D SGOV); design `Y45/`. Build the
   next generate artifact from a `core.autocrlf=false` checkout and compare members byte for byte (S286, batch 196).

## Queued irpt-status work

W2-06 (`include=composition`, the frozen AnalysisSubmissionRequest; CTO batch 165) and G3 (render ports for the
Analysis print, CTO batch 175).

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

- `irpt-y3-20261002`: U1, U2, D1, D2 closed; V1 open (READY pending the session re-capture).

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
