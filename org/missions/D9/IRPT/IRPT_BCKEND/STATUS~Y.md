# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` and the fold-in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6, Y-H); run order
CTO 104634 ("Y-3 READY, then Y-5 V1, then Y-4 V1, one at a time and spaced"). Reviewer `3.0.0_SA_CVO` (grades pins after
the fact). As of 2026-10-03T18:0xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | Y-3 READY evidence `ee801b0505`, its ledger closed `284667acb5`; Andrew-direct egress record `ce20ca6854`; Y-3 timing `f6d8202ce4`. No worktree held |
| SERVED: `irpt-status` | `hC6PramtsshP40jo3OJ91k4qxlHndylJWxHLIjIdw/E=` since 06:28:49Z (G3 + W2-06). Rollback: re-promote S3 `4CQOSM..` (`6VQejBfs..`), drop the variable, delete the policy |
| SERVED: PDF route | `GET analysis/requests/{requestId}/pdf`, route `ihirb2s` on `7k3ed8px20` |
| SERVED: the resident | `/opt/irpt-resident/a6f6e7165e-st18` since 05:52:20Z. Rollback root `828c37c6f7-st17` |
| SERVED: `irpt-ycharts-generate` | `fD2R6OFrT2N086C9Go3e1aA9RKZCP/vfnZCaHCloJTs=` since 03:02Z. Rollback: S3 `oew.wOPK..` with the resident, all or none |
| SERVED: runner role | the estate Kimi secret through ONE carrier (`local.kimi_secret_arn`); login and session ARNs keep `-*` (parked) |
| Stored YCharts session | **LIVE** since 16:3xZ at fence 25 (AWSCURRENT `6190de31`, captured_by `irpt-ycharts-har-seed`), seeded from Andrew's HAR with no sign-in; S288 disarmed by S306. Shared with Andrew's browser (S233). aws-waf-token expiry ~epoch 1791390810; the server-side ycsessionid expiry is unknown |
| Push state | LOCAL; origin CLOUD `a714df4d7f` (ls-remote read 17:3xZ); CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6

1. **Y-3 READY** 17:03:14Z: REQ-329a5618 (Multi, ULT + IWM, Cottonwood), report RPT-c8c4037a. Ledger
   `irpt-y3-20261002` CLOSED. Measured: 15 m 06 s of its 17 m 43 s is our 900 s read-back release after one
   `calculating` answer (`IRPT_MVP_Y/RESEARCH/Y3_JOB_TIME_BREAKDOWN_MEASURED_20261003.md`).
2. **Y-5 V1 (next):** Case A with TIMXX -> SGOV from the page. `2.0.0_SA_COO~D` added case `Aproxy` to
   `yh-submit-case.mjs`; it passes on fixtures (104671). The live run is HELD by ~D on: (a) site Z holding the UI-walker
   account (MSTR 104669); (b) whether Andrew's ~17:3xZ "We will discuss internally on how to proceed with further data
   collection after review" covers a YCharts Analysis run. (b) is ASKED of Andrew at this terminal ~18:0xZ.
3. **Y-4 V1** after Y-5: the typo file. The driver's `typo` case has no accept step, and the file also holds TIMXX, so READY
   needs the AAPL accept AND TIMXX -> SGOV: the next ask to ~D after Aproxy runs.
4. Then Y-2 (the page's Case B; the easy file holds TIMXX too) and Y-6.

## New project (not this lane's build): YCharts direct-API generation, Opal-branded

Andrew-direct ~17:0xZ, request `IRPT_MVP_Y/RESEARCH/CRO_REQUEST_YCHARTS_DIRECT_GENERATION_20261003.md`. L1 brief
`docs/briefs/irpt-ycharts-direct-generation-opal-branded-brief-20261003.md` @8dc32668e1 (4.0.0_SA_CRO). L2
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_IRPT_YCHARTS_DIRECT_GENERATION_20261003.md` @c3f2fb4bb3 waits on
Andrew confirming its seven DONE WHEN lines. Andrew ~17:3xZ (`ce20ca6854`): YCharts egress whitelisted for this seat and
its agents; subscription cleared for use.

## Queued work

- Y-5 packet 2 (the Kimi swap): HELD by CTO batch 218 (YAGNI: the user-named proxy serves Case D). Findings
  `Y5P2/KIMI_WEB_SEARCH_QA_FINDINGS_20261003.md`.
- G3 arm 3, the live wiring, is E4's.

## Rows this lane holds

| Row | State |
|---|---|
| S288 | DISARMED by S306 (the session restored from Andrew's HAR) |
| S284 | OPEN, BLOCKING, ARMED: TIMXX gated (`mutualFundDataUSA`, S287); remedy the Y-5 proxy, proven live by Y-5 V1 |
| S296 | OBSERVATION, INERT (history UNEXPECTED) |
| S286 | CVO: generate bundles carry CRLF members; build from autocrlf=false (mine) |
| S230 | the resident's own sign-in meets a CAPTCHA; only Andrew restores a session (now by HAR seed or sign-in) |
| S282 | test_generate_installed schema pin; owner `2.0.0_SA_COO~P` |
| S263, S253, S261, S231, W94-S2, W91-S1, W92-S1 | for the CVO to close (unchanged) |
| W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

- `irpt-y5-20261003` and `irpt-y4-20261003`: apply legs proven, V1 open, not held (released after the session restore).

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/lambda/investor-reporting/intake/{security_resolution,portfolio,resolution_broker}.py`
and their tests; `infra/aws/ec2/investor-reporting-ycharts/**`; `docs/contracts/investor-reporting/v1/routes.json`;
`infra/aws/lambda/investor-reporting/ops/owned_requests.py`; the rows of `irpt-status` and `irpt-ycharts-generate` in
`infra/aws/lambda/ci/lambda-source-map.json`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; this file.

## Parked, each with its owner and the condition that un-parks it

- Login and session secret ARNs keep `-*` in the runner role. Owner this seat; un-parks on a CTO ruling.
- The iam.tf comment in `ycharts/iam.tf`: `2.0.0_SA_COO~P`'s lane; un-parks with that lane's next edit.
- Andrew's HAR file `C:\Users\AndrewBerman\Downloads\ycharts.comalyss.har` (outside the repo): its deletion is Andrew's
  (asked); recorded by sha256 and size only.
- A deterministic ROWS_UNVERIFIED is still retried four times at 60 s. Owner this seat; un-parks if a stray-row refusal
  recurs.
- The api root's `CHANGELOG.json` entries for routes `bh7ynom` and `ihirb2s`: outside this seat's surface.

## Limits

No fund-holding upload has normalized live (Y-5 V1 is the first). No Comparison report on served code from a client file;
Y-3's Multi READY used window 15's Dollars CSV. The laptop clock is ~3 s behind AWS: grade expiries on AWS's Date header.

## Standing directives (carried)

- Andrew-direct ~17:3xZ (site Z, MSTR 104662): no data-engineering change without his explicit directive; this seat
  holds no quarantine.
- No firm id typed in code or JSON; run `.tools/naming-gate.py --diff <diff> --enforce` in a worktree.
- A password or cookie is read BY NAME into memory and never printed; an output is read for values before commit.
- YCharts runs one at a time with the queue empty; a CAPTCHA or sign-in is Andrew's act.
- A served move needs both never-widen halves; read safe-merge's exit code and tree-check line on every merge.
- A drained worktree is removed the same turn.
