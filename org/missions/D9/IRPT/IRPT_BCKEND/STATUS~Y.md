# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` and the fold-in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6, Y-H); run order
CTO 104634 ("Y-3 READY, then Y-5 V1, then Y-4 V1, one at a time and spaced"). Reviewer `3.0.0_SA_CVO` (grades pins after
the fact). As of 2026-10-04T02:3xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | Y-5 READY + 4 ledgers closed `1afe081ac4`; YCDGEN round 1 drained `c1d672f636`; the research grant packet `6b76e61d62`. No worktree held |
| SERVED: `irpt-ycharts-generate` | `uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ=` since ~01:5xZ 2026-10-04 (Y5D: bind at cents). Rollback S3 `31clJjOm..` (`FgZcBjJu..`) with the resident, all or none |
| SERVED: the resident | `/opt/irpt-resident/3f29017cfc-st21` since 02:01:04Z 2026-10-04. Rollback root `136ee09e9f-st20` |
| SERVED: `irpt-status` | `hC6PramtsshP40jo3OJ91k4qxlHndylJWxHLIjIdw/E=` (G3 + W2-06) |
| SERVED: runner role | Kimi key via one carrier; login and session ARNs keep `-*` (parked). Pending: `KeepYChartsResearchAnswersAndRunRecords` (IRPT_YCDGEN; packet at the CTO) |
| Stored YCharts session | LIVE at fence 25 since the HAR seed (S288 disarm row S315; the remediation clock is the CVO's) |
| Push state | LOCAL; origin CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6

1. **Y-3 READY** 2026-10-03 17:03:14Z (closed).
2. **Y-5 READY** 2026-10-04 02:28:20Z: REQ-a618aa83 (TIMXX named SGOV on the page; RPT-ffe60035). Three defects found and
   served on the way (y5v finding value, y5c cents upload, y5d bind at cents; row S316). Ledgers closed.
3. **Y-4 V1 (next):** the typo file -- accept AAPL for APPL and name SGOV for TIMXX. `2.0.0_SA_COO~D` asked for a
   `typoAccept` driver case and one live run (02:32Z).
4. Then Y-2 and Y-6.

## IRPT_YCDGEN (this seat issues; FULL lease)

Round 1 (the thread, FWD-1) merged and drained `c1d672f636`: keeper + X10 row, runner inside the served lease, the
Overview map (249 elements, 12 calls), the Opal-branded layout (real Chromium). The close's one live run waits on the runner
role's research grant (ledger irpt-ycdgen-grant-20261004; packet blob `01c8a35f8d` at the CTO). Then the L8 compile to the
CVO (m-1.AC2 is its judgment criterion).

## Queued work

- Y-5 packet 2 (the Kimi swap): HELD by CTO batch 218 (YAGNI: the user-named proxy serves Case D). Findings
  `Y5P2/KIMI_WEB_SEARCH_QA_FINDINGS_20261003.md`.
- G3 arm 3, the live wiring, is E4's.
- The Y-5 jobs spend ~15 min in the 900 s read-back release after one `calculating` answer
  (`RESEARCH/Y3_JOB_TIME_BREAKDOWN_MEASURED_20261003.md`); IRPT_YCDGEN FWD-6 measures YCharts' real calculation time.

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

- `irpt-y4-20261003`: apply legs proven, V1 open (the typo run).
- `irpt-ycdgen-grant-20261004`: D1 and V1 open (the research grant; packet at the CTO).

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
