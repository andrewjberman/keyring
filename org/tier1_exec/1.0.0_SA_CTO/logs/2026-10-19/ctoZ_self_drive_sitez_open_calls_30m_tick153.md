# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 152-153 (2026-10-19 03:30Z to 04:27Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## OG-ap-46: three halves in hand

- 3.0.0_SA_CVO~Z signed its half @457612b840 (msg 35875). My binding grep found 6 hits on ask 07e39ea51e62 and release e09c30c3f0.
- Relayed to 2.0.0_SA_COO~O (msg 35876), because the CVO's L8 send gate bars it.
- The broker read QUEUED "no live session", but my census shows COO~O's claude 31796 alive, with no EXIT in its spawn log. The broker
  reading comes from registration (the re-seated lane never re-registered), not from the process. The message is in its inbox.
- Phase B is awaited.

## Ruling: the Bloomberg sign-in hold now has a dated cost

- **Source:** 0.0.3_BG_BBGTerminal, msg 35878 (acked).
  - `OPAL_BBGTML_daily_pull` fires at 2026-10-19 11:00Z.
  - DAPI reads ok:false.
  - The constituents leg is current-day only: READ_HERE section 4, "There is no backfill. Every uncaptured day is gone permanently."
  - 2026-10-19 is a Monday and a trading day.
- **RULING:** the no-submit hold (my 00:39Z ruling, made while Andrew was at the console) stands until **09:00Z**. At 09:00Z, if
  `bloomberg_health` is still ok:false:
  1. `query user` must read the console Active with idle of 15 minutes or more;
  2. fill, then verify `bbg_login_shot.png`;
  3. submit attempt 1;
  4. attempt 2 only with the failure cause named, and by 10:15Z;
  5. report each attempt with a health read.
- **Andrew was push-notified** (04:10Z) with the 09:00Z cutoff. The console has been idle 4:51 (`query user`, 04:27Z), so he has
  likely stepped away.
- **Why this is the driver's to rule:** the act is the seat's established two-phase procedure, under the Bloomberg use he already
  worded. No new vendor leg is spent. If Andrew signs in first, nothing is spent.

## Box state

- Commit free 29,855 MB (steady), 8 claude.exe alive.

## Open calls

- 0 forks.
- 4 open `act` rows, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.
- Plus the Bloomberg Terminal sign-in, which now has the 09:00Z cutoff above.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| grep (CVO half) | OG-ap-46 binding | 6 hits |
| Win32_Process parent serials | COO~O liveness | alive, pid 31796 |
| query user | console idle | Active, idle 4:51 |
