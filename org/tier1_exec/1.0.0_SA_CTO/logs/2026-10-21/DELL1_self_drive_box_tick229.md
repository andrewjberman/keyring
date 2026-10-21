# DELL1 self-drive box -- tick 229, 2026-10-21 ~09:18Z (delta: the first backfill day LANDED; the lander's trading-day rule)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 09:18Z. Acked since tick 228: 9044, 9046.
- open_calls.json: 163 rows, 4 OPEN: 89c9 and ea86 (Andrew's); 3bc7 and 5013 done or withdrawn, held CROSS-BOX by the tool. The
  per-firm Groups act for Andrew stands (ruling @4c536cb554).

## Acts and rulings
- **The first backfill day landed** (run 5, 08:56Z, puller profile, one sign-in; read by me from the bucket at 09:05Z): four objects
  under `fidelity/alongside/bronze/{balance,position,prices,security}/20261016/` (1,223,747 / 30,326,543 / 645,722 / 655,578 B),
  content date Friday 2026-10-16, from the 2026-10-19 export folder. `account.txt` and `transact.txt` did not land; the run ended
  `TargetClosedError` with `stop.reason none`. Row D1-S18 (NFRA1 @11a02ca6a45).
  - **Ruled** (09:06Z): the record names why each missing file did not land (never a silent zero); an exception is the stop reason
    with its day. P1 cut both as FT-s-7 REPAIR 9 (`--skip-files` for transact, which never answered in three runs on two clients and
    whose history comes by the per-account route; closed @f0bf1360b08).
- **Why account.txt failed** (P1 9044): its as-of column is the CALENDAR day before the export (Saturday 2026-10-17), and the
  lander refuses a non-trading day; the same would bite every Monday's daily pull from 2026-10-26. **Ruled** (09:09Z): a file's
  landing date is the last trading day on or before its content as-of, from `lib/trading_calendar.py` (the one frontier), both
  dates in the run record (`content_as_of` measured, `landed_under` derived); `split.py` uses the same rule so firm files never
  land under a weekend. P1 cut it as FU-s-4 REPAIR 2 (@7ac44b0bf3c, worker ~2).
  - The 90 s per-file cap did not fire in 461 s on transact: P1 measured the timer starts before the fetch and covers headers and
    body; the browser call itself hung, so the fault is outside the fetch and skipping is the bounded answer.
- **Run 6** near 10:50Z, after the three scheduled fires (09:45, 10:15, 10:45Z) on the puller profile.
- **AMGT_HARVST:** no change; W1 at 60m until 2026-10-22 09:30Z.

## Scope state
- **NFRA_FIDUPL:** FT-s-11, FT-s-8, FU-s-4 (REPAIR 2), FU-s-11, FU-x-1 pending. 33 objects under `fidelity/alongside/bronze/` (10
  data: 6 for 20261019 and 4 for 20261016; 23 run records). Rules ENABLED; first fire 09:45Z. Backfill earliest LANDED date:
  2026-10-16 for balance, position, prices and security; none yet for account and transact. No firm prefix; the "split to firms"
  half stays UNREACHABLE until Groups exist (Andrew's act).
- **AMGT_HARVST:** round 100, co-7 stage 7 pending.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **Per-firm account Groups in Wealthscape:** create one Group per firm, or say the word for a seat to (ruling @4c536cb554).
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** a back-dated export profile, only if the wizard's date field cannot be automated on the backfill (CRO 8916).

## Compiler Tools
- `list-objects-v2` (every data object with its date prefix); `s3 cp` of the backfill record (counts and dates only).
