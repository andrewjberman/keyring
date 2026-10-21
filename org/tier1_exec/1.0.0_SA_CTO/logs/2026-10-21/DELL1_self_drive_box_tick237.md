# DELL1 self-drive box -- ticks 236-237, 2026-10-21 ~12:48-13:19Z (hour floor; the Historical route ruled; the 120-day cap probe ruled on Andrew's question)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 13:19Z. Acked since tick 235: 9083, 9090.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **Probe 2 done** (P1 9083, record @bfeb73497a8): the read-only walk (warmed profile, sign-in 12:07:46Z, logout 204/400, nothing
  saved): the Historical Prices & Positions export takes ONE date per request, reach today-120 to yesterday, file types positions,
  balances, prices only (POST `/ssc/importexport/wc/channel/export/v1/historicalExport.json`, keys known); accounts, securities and
  transactions have no historical export there; a one-off Group-filtered export cannot be made without a SAVED profile.
  - **Ruled** (12:22Z): YES to ONE live Historical request (10/15/2026, the existing saved profile, positions and prices, nothing
    saved) landed by content date; the Historical wizard IS the backfill route for positions, balances and prices (earliest about
    2026-06-23 at the observed reach), walked backward on trading days under the caps; no profile is saved by a seat, so a
    Group-filtered export (a Group plus a profile) stays Andrew's act.
- **The CRO's reports for ms** (@2447db85574 depth, @3f3d7374576 theory and plan on Andrew-direct bus 356885a0; @e46553e7eb7): three
  surfaces (standing export 3 days; Historical ~120 days for three file types; per-account transactions months); accounts and
  securities current-snapshot only; no step needs Andrew within reach.
- **Andrew's question, the 120-day cap** (CRO 9090): UI-observed, never POSTed. **Ruled** (12:50Z): probe it NOW in the same session
  as the live request: historicalDate at today-150, -180, -270, -365, -730, classified SERVED / EMPTY / REFUSED with the exact text;
  the first REFUSED is the proven cap, anything SERVED lands; per-account transactions stepped back year by year; depth stated
  "at least 120 days, cap unproven" until measured. Runs now because the split is blocked on Andrew's Groups.
- **Quiet asks:** 12:05Z (answered 12:07Z: the walk had just started) and 13:05Z (no answer at 13:19Z; no project commit since
  12:21Z). `get_agent_status(2.0.0_SA_COO~P1)` at 13:19Z: LIVE (0 s, PID 8160) with FOUR unread inbox files since 12:21Z (my 12:22Z
  and 12:50Z rulings, the CRO's 9090, my 13:05Z ask): the live-and-deaf shape. **Act:** asked `0.0.0_AB_MSTR~DELL1` to `/unstick` P1 by
  serial now (the @2138a1f383 fix) and report the console; the Historical request and cap probe wait on it.
- **AMGT_HARVST:** no change; W1 at 60m until 2026-10-22 09:30Z.

## Scope state
- **NFRA_FIDUPL:** FT-s-8, FU-s-11, FU-x-1 pending. 46 objects under `fidelity/alongside/bronze/` (17 data; 29 run records). Rules
  ENABLED, the scheduler proven; the first real fire tomorrow 09:45Z. Deliverable 1: scheduled, enabled, proven; the per-firm SPLIT
  UNREACHABLE until Groups exist (Andrew's act). Deliverable 2: the standing export's earliest date named (2026-10-16 x5,
  2026-10-19 transact); the Historical route and the cap probe pending their first run.
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape** (and the saved export profile a Group-filtered export needs): create them, or say the
  word for a seat to (ruling @4c536cb554; probe 2 record @bfeb73497a8).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a hand-recorded HAR of the Historical wizard, only if an agent walk is refused at the password step (not needed
  so far: the 12:07Z walk passed).

## Compiler Tools
- `git show` of the CRO's plan and P1's records; `list-objects-v2` (counts only); `get_agent_status` (P1).
