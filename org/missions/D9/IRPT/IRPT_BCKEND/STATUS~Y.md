# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` and the fold-in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6, Y-H); run order
CTO 104634 ("Y-3 READY, then Y-5 V1, then Y-4 V1, one at a time and spaced"; then Y-2 and Y-6). Reviewer `3.0.0_SA_CVO`
(grades pins after the fact). As of 2026-10-05T04:3xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | S326 served `e805bb727a`; IRPT_YCDGEN round 3 L8 `22f9a0b8c0`. No worktree held by this seat |
| SERVED: `irpt-ycharts-generate` | `uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ=` (Y5D). Source map recorded at 3a14a49f48, parity (S320 `40417a1b8c`) |
| SERVED: the resident | `/opt/irpt-resident/3f29017cfc-st21` since 02:01:04Z 2026-10-04. Rollback root `136ee09e9f-st20` |
| SERVED: `irpt-status` | `jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE=` since 04:18:20Z 2026-10-05 (S326: history newest first; carries S318). Rollback S3 version `jVkDK9v6..` (`XPta1UMJ..`) |
| SERVED: research principal | `irpt-cot-ycharts-research-role` (Put/Get on Cottonwood's two research tables), assumed by the runner role (CTO batch 239) |
| Stored YCharts session | LIVE at fence 25; research runs 2-3 met a WAF challenge on one request shape only (row IRPT_YCDGEN-S3) |
| Push state | LOCAL; origin CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6

1. **Y-3 READY** 2026-10-03 17:03:14Z (a CSV upload with ULT + IWM).
2. **Y-5 READY** 2026-10-04 02:28:20Z (REQ-a618aa83; TIMXX named SGOV). Its page row now reads READY with its date basis
   (S318 closed, V1 00:13Z 2026-10-05).
3. **Y-4 READY** 2026-10-04 03:18:02Z (REQ-0d97252f; the typo file; check gate 15.6 s). Ledger closed.
4. **Y-2 READY** 2026-10-05 01:37:07Z (REQ-c1b53772; the easy file, SGOV, Opal Ultra Long-Term; ~D's page run). Its
   row now lists first in the history (S326, served 04:18Z).
5. Then Y-6 (each case twice in a row, from the page, timings recorded).

## IRPT_YCDGEN (this seat issues; FULL lease)

- Round 1 graded by the CVO (FWD-1 realized on Andrew's open; his open not yet confirmed).
- Round 2 (E2-E5) was issued `4182c82353`, drained (r-2 `988a62c350`, c-2 `14254f9b70`, m-2 `9cfc9da211`) and closed
  live: YCD-R2-20261004T2315Z-A/B.
  - FWD-2 reads false/false against the bootstrap run.
  - Both OTHER_ENDPOINT routes answer 200 for a model portfolio.
- L8 packet `fda2a4e8c7`, READ by the CVO at 23:23:49Z.
- Next: the CVO's L9 (m-2.AC4, c-2.AC3), then the CTO's round-2 analysis.

## Queued work

- Y-5 packet 2 (the Kimi swap): HELD by CTO batch 218.
- The Y jobs spend ~15 min in the 900 s read-back release after one `calculating` answer; IRPT_YCDGEN FWD-6 measures
  YCharts' real calculation time.

## Rows this lane holds

| Row | State |
|---|---|
| S318 / S321 | DISARMED by S325 (irpt-status serves the pinned-boilerplate proof) |
| S326 | served (history newest first); V1 closes on ~D's page check |
| S284 | DISARMED by S327 (the user-named proxy proven by Y-5 and Y-2; the entitlement stays Andrew's vendor call) |
| S320 | closed (recorder run, parity) |
| S288 | DISARMED by S306 |
| S296, S286, S230, S282 | unchanged (see their rows) |
| S263, S253, S261, S231, W94-S2, W91-S1, W92-S1, W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

`irpt-s326-history-20261005`: U1 and D1 closed, V1 open (~D's page check). Closed: `irpt-y4-20261003`,
`irpt-ycdgen-grant-20261004` (V1 superseded), `irpt-ycdgen-principal-20261004`, `irpt-s318-boilerplate-20261004`.

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/lambda/investor-reporting/intake/{security_resolution,portfolio,resolution_broker}.py`
and their tests; `infra/aws/lambda/investor-reporting/ops/{owned_requests,prospect_dates}.py` and their tests;
`infra/aws/ec2/investor-reporting-ycharts/**`; `infra/aws/terraform/investor-reporting/ycharts/resident.tf`;
`docs/contracts/investor-reporting/v1/routes.json`; the rows of `irpt-status` and `irpt-ycharts-generate` in
`infra/aws/lambda/ci/lambda-source-map.json`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; this file.

## Parked, each with its owner and the condition that un-parks it

- Login and session secret ARNs keep `-*` in the runner role. Owner this seat; un-parks on a CTO ruling.
- The recorder's CHANGELOG entries for irpt-ycharts-generate (S320) and irpt-status (S318) are `2.0.0_SA_COO~P`'s lane,
  handed over as patches. The S320 entry was committed by ~P; S318's un-parks when ~P commits it.
- An uncommitted `irpt-holdings` artifact_sha256 edit in the shared source map is another seat's. It was left untouched.
- Andrew's HAR file `C:\Users\AndrewBerman\Downloads\ycharts.comalyss.har` (outside the repo): its deletion is Andrew's
  (asked); recorded by sha256 and size only.
- The worktree `C:/Users/AndrewBerman/Desktop/wk-ycdgen-2` (round-1 slot ~2; branch merged) holds an untracked `.scratch/`.
  Owner this seat; un-parks on a look at its contents.
- A deterministic ROWS_UNVERIFIED is still retried four times at 60 s. Owner this seat; un-parks if a stray-row refusal
  recurs.
