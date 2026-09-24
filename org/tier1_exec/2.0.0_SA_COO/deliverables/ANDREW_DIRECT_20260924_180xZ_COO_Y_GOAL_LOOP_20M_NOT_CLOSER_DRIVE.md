# ANDREW-DIRECT 2026-09-24 ~18:0xZ -- COO~Y runs its goal loop at 20m, not /closer-drive

**Channel:** Andrew at the `2.0.0_SA_COO~Y` terminal (Claude session a5708842), mid-startup under blast mode.
**Receiving seat:** `2.0.0_SA_COO~Y`. **Recorded by:** `2.0.0_SA_COO~Y`, same turn.

## Verbatim

Andrew first asked:

> it should be /closer-drive , is that the same as /freeform ?]

The seat answered that the two are different (`/freeform` stands down the search rail only; `/closer-drive` is the
FAST tick body and needs a FAST lease), and that `python .tools/drive-mode.py read IRPT_BCKEND` printed
`FULL IRPT_BCKEND` at ~18:08Z, so `/closer-drive` would route to the `/canonical-drive` body. It asked whether to
request a FAST lease on IRPT_BCKEND from `1.0.0_SA_CTO`. Andrew answered:

> No you just go with your goal loop, and your 20m loop

## What it binds

- `2.0.0_SA_COO~Y` keeps the `/loop 20m` goal loop already authorized in `org/ref/LIVE_ARMS.md` (record
  `ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`), armed this session as cron `acd10798`
  (`7,27,47 * * * *`). Stop condition unchanged: `/verify` SOUND or Andrew's stand-down.
- No FAST lease is requested for IRPT_BCKEND; `/closer-drive` is not run by this seat.
- `/freeform` (authorized for the four seats by the blast-mode record) stays armed for this session's search speed.

Nothing here changes another seat's work, so no line goes to `1.0.0_SA_CTO`.

## Addendum ~18:1xZ -- "Follow CTO instruction"

`1.0.0_SA_CTO` 100813 (18:14Z) asked the seat to switch to `/closer-drive IRPT_BCKEND~Y` under a per-seat FAST lease.
Y relayed the word above to the CTO (18:16Z). Andrew then said at the Y terminal, verbatim:

> Follow CTO instruction

The CTO's latest instruction at that moment was 100819 (18:17Z), which superseded 100811-100813 on Andrew's C11 word
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_181xZ_C11_GOAL_LOOPS_READ_THE_LEASE_P_M_Y.md`):
keep the 20m goal loop and read the `IRPT_BCKEND~Y` lease at the start of every tick (FAST: `/closer-drive` item
rules; FULL: normal closer checks; HOLD: pause). The seat follows 100819: cron `acd10798` was replaced by `87624362`
(same cadence, the prompt now reads the lease first). The lease read FAST until 21:13:40Z at 18:18Z.
