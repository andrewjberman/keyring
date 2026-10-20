# /self-drive dell2-box -- ticks 167-168 (2026-10-20 ~11:26Z-11:40Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 167 and 168, since the tick 166 log (@3cbd106595). state: ARMED. Written on a substantive delta.

## r34n LIVE

- Live 10:58Z (`~Y2` msg 11324, IB2 msg 11:02Z). Read here in `A_AFTER_R34N.txt`: `V2S OK SPY KEPT and ZQXWVK NOT_KEPT`,
  members 2 of 2 MATCH, sums 316 of 316, root `0485393f3a-r34n`. The ledger is CLOSED at 11:00:28Z.
- The packager now calls through the CloudFront alias. Blockers A and B are both closed.

## A STOP-class regression on PROD: the v0.24 page cannot file an analysis

- **Found by** the offline proof of run 7's browser leg (worker `0.9.0_WK_IRPT_ANLREQ~323`, `PAGE_NOTES.md`); `~Y2` msg 11332.
- **Read here at origin/PROD f48e09dd:**
  - `src/pages/TicketCenter/analysisRequest.ts:665`: `analysisBody()` sends `commentary_requested: true`.
  - `src/pages/InvestorReporting/contracts/submission-request.ts:14`: the allowed set is the required keys plus `input_id` and
    `ticket_id`.
  - `src/api/endpoints/investor-reporting.ts:1493`: `submitAnalysisRequest` calls that guard before transport.
  - The page therefore files the ticket, then shows "Analysis: FAILED - Invalid analysis submission request".
- **Cause:** AR-y-317's guard change was reverted at e0b43076 (2026-10-15). The wire type kept the field and the v0.24 set
  re-added the body field. The unit tests mock the client, so none ran the real guard.
- **Exposure:** every page filing since 09:28:44Z (the v0.24 promote). Run 6 filed through the API, not the page, so it did not
  meet the guard.

## Rulings

| item | ruling |
|---|---|
| r34n timing and run 7 (`~Y2` msg 11324) | Run 7 GO at 14:15Z, after an offline proof; a failing offline proof is a STOP (msg 11329). |
| TO-R21-RB1 against run 7 (`~V2`) | It starts only after run 7 is terminal, still after 14:15Z, one attempt (msg 11330). |
| The guard regression (`~Y2` msg 11332) | Fix forward, no rollback. Admit `commentary_requested` as a boolean only. Add a real-guard test with no mock and a mutant that fires. A DEV row, then a PROD recut row, both the CTO's (Opal-internal). The DT promotes at or after 14:15Z, then run 7. `~Y2` lists the page filings since 09:28:44Z (ids and counts only) for a re-submit. |
| Notice to Andrew | Via `0.0.0_AB_MSTR~DELL2`: filing fails at the analysis step; hold any sample filing until the close-out report. |

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git, ... S3 deletes"): `C:\dev\wk-irpt-dashbd-503`; row 544d; row 65a1; row a392.
- **S3 deletes:** row 6e7c; row 128f; the synthetic leftovers of runs 5 to 6.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
