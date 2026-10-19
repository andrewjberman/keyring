# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 142-143 (2026-10-18 23:37Z to 2026-10-19 00:3xZ)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Root cause of tonight's seat deaths and failed spawns: the commit limit is nearly exhausted

**Measured 00:3xZ (Win32_OperatingSystem, Get-Process):**
- Commit free is **1,682 MB of 81,363 MB**, while physical free is 35,326 MB of 64,979 MB.
- Total private memory is 60,351 MB.
- **11 `bplus64` (Bloomberg Terminal) processes hold 34,969 MB private.** All were started 2026-10-17 22:44 local. Each has a working
  set under 100 MB, so the memory is reserved, not used.
- `wintrv` holds 2,596 MB.

**Why this explains what happened (an inference from the mechanism, not separately proven per event):**
- **Seats crashed when an allocation failed.** Dead since 20:48Z: 2.0.0_SA_COO~O, 4.0.0_SA_CRO~Z, 3.0.0_SA_CVO~Z, 0.0.0_AB_MSTR~Z and
  2.0.0_SA_COO~MI. For COO~O (20:48:58Z), CRO~Z (22:37:32Z) and CVO~Z (22:47:19Z), the spawn logs read `EXIT rc=-1073740791`
  (0xC0000409).
- **New processes could not start.** No MSTR spawn since 23:22Z wrote a spawn log, so each failed before the wrapper's START line.
  This continued after the console session read Active at 23:37Z, so the disconnected desktop was not the only cause.
- **Alive claude.exe** (5, each parent's serial read): 0.0.3_BG_BBGTerminal 10896, 1.0.0_SA_CTO~Z 5716,
  0.7.0_AE_CloudOps~NFRA1 15864, 0.7.0_AE_CloudOps~MDPF1 37156, 2.0.0_SA_COO~O 31796.

**Act:**
- Asked 0.0.3_BG_BBGTerminal, which owns the Terminal, to recycle the `bplus64` set by its own procedure. It is to say at once if
  Andrew must sign in again; he is at the console.
- `integrations/bloomberg/READ_HERE.md` was read for a restart procedure first, and it holds none.
- Re-spawning CVO~Z, CRO~Z and MSTR~Z waits on the commit headroom. A spawn now would fail the same way.

## Other

- 23:37Z: the operator reconnected the console (`query user`: session 1 Active). The reconnect act row stays open until the seats are
  back.
- Two messages to MSTR~Z are unread (35829 OFFER-EXHAUSTED, 35830 QUEUED): it has no live process.

## Open calls

- 0 forks.
- 5 open `act` rows, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew), 5b35, and the console reconnect (6b13).

## Compiler Tools

| tool | used for | result |
|---|---|---|
| Win32_OperatingSystem | commit headroom | 1,682 of 81,363 MB free |
| Get-Process by PrivateMemorySize64 | commit holders | bplus64 x11 = 34,969 MB |
| Win32_Process parent command lines | live seat census | 5 claude.exe, serials read |
| .runtime/spawn-logs + agent-spawn-audit.log | spawn failures | 0 logs for 4 spawns since 23:22Z |
