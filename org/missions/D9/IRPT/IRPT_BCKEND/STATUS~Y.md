# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Mode FAST: lease `IRPT_BCKEND~Y` (renewed by the loop; read each tick).
Loop `/canonical-drive IRPT_BCKEND`. Way forward: CTO rulings in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/RULINGS.md` and the fold-in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_FOLD_IN_IRPT_THREE_BRIEFS_20261002.md` section 2 (Y-1..Y-6, Y-H); run order
CTO 104634 ("Y-3 READY, then Y-5 V1, then Y-4 V1, one at a time and spaced"; then Y-2 and Y-6). Reviewer `3.0.0_SA_CVO`
(grades pins after the fact). As of 2026-10-05T10:5xZ.

## Pins

| What | Value |
|---|---|
| CLOUD (local) | IRPT_YCDGEN round 4 drained `0bdc75c6c2`, L8 packet `742b4665df` (rows S7/S8 `d666b782c3`). No worktree held by this seat |
| SERVED: `irpt-ycharts-generate` | `uFTONal/RhfoETes4rqJ4xRjJV4d2/nv3OlwuR9AXCQ=` (Y5D). Source map recorded at 3a14a49f48, parity (S320 `40417a1b8c`) |
| SERVED: the resident | `/opt/irpt-resident/3f29017cfc-st21` since 02:01:04Z 2026-10-04. Rollback root `136ee09e9f-st20` |
| SERVED: `irpt-status` | `jhGc2J4Q5EesJgnLq8EzdE5ErrZLbyqnJ8m00R7CgdE=` since 04:18:20Z 2026-10-05 (S326: history newest first; carries S318). Rollback S3 version `jVkDK9v6..` (`XPta1UMJ..`) |
| SERVED: research principal | `irpt-cot-ycharts-research-role` (Put/Get on Cottonwood's two research tables), assumed by the runner role (CTO batch 239) |
| Stored YCharts session | LIVE. Budget measured: 6 requests a window with 660 s between windows (rows IRPT_YCDGEN-S6, S7; five windows on 2026-10-05, no challenge) |
| Push state | LOCAL; origin CLOUD is pushed by `0.0.0_AB_MSTR` only |

## Live thread -- fold-in Y-1..Y-6

1. **Y-3 READY** 2026-10-03 17:03:14Z (a CSV upload with ULT + IWM).
2. **Y-5 READY** 2026-10-04 02:28:20Z (REQ-a618aa83; TIMXX named SGOV). Its page row now reads READY with its date basis
   (S318 closed, V1 00:13Z 2026-10-05).
3. **Y-4 READY** 2026-10-04 03:18:02Z (REQ-0d97252f; the typo file; check gate 15.6 s). Ledger closed.
4. **Y-2 READY** 2026-10-05 01:37:07Z (REQ-c1b53772; the easy file, SGOV, Opal Ultra Long-Term; ~D's page run). Its
   row now lists first in the history (S326, served 04:18Z).
5. **Y-6** (~D, 5 cases x 2 from the page, one at a time):
   - run 1 REQ-777d7546 READY 05:18:26Z (page 18.2 min; open to sections 2.0 s);
   - run 2 REQ-14fe69cf READY (page 06:58:51Z, 17.9 min; open to sections 1.4 s);
   - run 3 REQ-724a493e READY 07:38:14Z server-side (18m40s). The page lost the row from 07:27Z on portal 0edab95f;
     server-side the row is position 0 of 33 (page-side miss, ~D reading its screenshot);
   - run 4 REQ-1352d8c1 READY 08:41:43Z; runs 5-6 (Multi-Comp) READY 09:40:23Z and 10:07:22Z, each read-back
     WAF-challenged and absorbed by the release (`Y6/Y6_BACKEND_SUMMARY.md`);
   - runs 7-10 are next. This seat records each run's backend states (`IRPT_MVP_Y/Y6/`, @0d980ceca5) and writes
     the Y-6 evidence at the end.

## IRPT_YCDGEN (this seat issues; FULL lease)

- Round 4 graded (CVO @d6f334c003): m-4.AC3 FAIL narrowly; FWD-2 not realized (a changed request).
- Round 5 issued `2f901c0a21` from the CTO's round-4 analysis (FWD-6 binds the Overview at 12 requests):
  - r-5 (~1): runner plan cap 12, request hash, lookup;
  - p-5 (~2): budgeted map, six statistics wired;
  - h-5 (~3): Opal-held census;
  - m-5 (~4): map residuals;
  - w-5 (~2, join after p-5 and h-5).
  Workers run in SPARSE worktrees `wk-ycdgen-r5-1..4` (disk full).
- Close acts: E4 (indexed level-series run, then the identical request after today's close); E6 (the budgeted
  Overview live, link to Andrew).

## Queued work

- Y-5 packet 2 (the Kimi swap): HELD by CTO batch 218.
- **Submit-to-READY is mostly a fixed wait.**
  - Y-6 runs 1-3 each spend 15m07s in `READ_BACK_LEASE_TTL_S = 900` (`ycharts/generate/recipe.py:688`, CTO batch 97
    item 4) after one `calculating` read-back.
  - The firewall window is bounded to (122, 660] s: 122 s was challenged (batch 97), and 660 s was clean in 5 of 5 windows
    on 2026-10-05.
  - Next, after Y-6 (never between its runs): measure the window with research probes, then a never-widen packet to cut
    the release to it (about 4+ minutes saved a job). The value is the CTO's (batch 97).

## Rows this lane holds

| Row | State |
|---|---|
| S318 / S321 | DISARMED by S325 (irpt-status serves the pinned-boilerplate proof) |
| S326 | CLOSED (V1 by ~D's page check); disarmed by S329 |
| S284 | DISARMED by S327 (the user-named proxy proven by Y-5 and Y-2; the entitlement stays Andrew's vendor call) |
| S320 | closed (recorder run, parity) |
| S288 | DISARMED by S306 |
| S296, S286, S230, S282 | unchanged (see their rows) |
| S263, S253, S261, S231, W94-S2, W91-S1, W92-S1, W91-S2, W92-S4, W88-S2 | unchanged |

## Ledgers this seat holds open

None open. Closed: `irpt-s326-history-20261005`, `irpt-y4-20261003`,
`irpt-ycdgen-grant-20261004` (V1 superseded), `irpt-ycdgen-principal-20261004`, `irpt-s318-boilerplate-20261004`.

## Write claims

`infra/aws/lambda/investor-reporting/ycharts/**`; `infra/aws/lambda/investor-reporting/intake/{security_resolution,portfolio,resolution_broker}.py`
and their tests; `infra/aws/lambda/investor-reporting/ops/{owned_requests,prospect_dates}.py` and their tests;
`infra/aws/ec2/investor-reporting-ycharts/**`; `infra/aws/terraform/investor-reporting/ycharts/resident.tf`;
`docs/contracts/investor-reporting/v1/routes.json`; the rows of `irpt-status` and `irpt-ycharts-generate` in
`infra/aws/lambda/ci/lambda-source-map.json`; `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/**`; this file.

## Parked, each with its owner and the condition that un-parks it

- C: is full (1.7 GB free at 10:5xZ). Twelve merged worktrees of ~P and ~M hold ~30 GB. Owner 0.0.0_AB_MSTR (asked
  10:34Z); un-parks when space returns. Until then this seat's workers use sparse worktrees.

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
