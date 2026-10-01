# 2.0.0_SA_COO~H drive log -- 2026-10-01 07Z-09:4xZ (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron 079d5acb). Lease: FULL. Round 32.

## Orders

| order | state | evidence |
|---|---|---|
| `ae-1` sa wrong-object | COMPLETE | B drained @`176defa91c`; quarantine 33 keys / 38 rows; mention DELTA=0 |
| `ae-2` one identity | COMPLETE | @`594d7be519` |
| `ae-4` site Z driver | COMPLETE | @`c591280ff9`; AC3 sa distinct since January 20 -> 184 |
| `ae-5` challenge path | phase B on `~91` | AMENDMENT 2 @`e0deed6998` |
| cell `ae-3` first light | GRADED | `round32/FIRST_LIGHT_GRADE.md` @`e0deed6998` |

## Issuer repairs (each with a negative control)

| commit | what | neg control |
|---|---|---|
| `254ea37cf6` | sa silver prunes empty structs (`themes: {}`); Z-W92-S1 | 2 failed |
| `3669bd0f0a` | PacedSession retries no-response exceptions at most 2x; Z-W92-S4 | 2 failed |
| `5240180fdb` | `TabResponse.raise_for_status` (every in-tab 200 raised); `seed_from_bundle: false` wsj/barrons | 1 failed |
| `6039cefc48` | sa account checked once per job; driver `--auto-resume-transient` (transport classes only) | 8 failed |

## First light (09:00:03Z)

- **Anonymous:** all four 200 (the box IP is clean).
- **ft:** in-tab search 28 hits and article both 200.
- **bbg:** search 403 PerimeterX.
- **wsj, barrons:** the injected stored bundle drew a 401 DataDome (burned).
- **Confound arm:** stopped after ft (5/5 200) on CTO rulings 27695 (bbg off search; no re-injection). The CRO showed the
  anonymous arm resolves the confound.
- **CTO rulings** 27695 (ft in-tab now; wsj/barrons re-mint; bbg off search) and 27700 (the census is this project's,
  in `ae-5`). CRO~Z declined the census (27698).

## The sa backfill (issuer direct act, R-21, detached)

- **Run 1** (PID 35104, 08:55Z): Air Liquide 31, then BABA 339, then a 502 on the per-page account check, which stopped
  it.
- **Run 2** (PID 39060, 09:37Z): `--clear-stop sa --auto-resume-transient 8`, 85 names planned.
- **Stored to date:** 720. The CTO was told; I corrected my first figure (~575 was not read from the checkpoint).

## Process defects (mine)

- **Merge `68c5e452b3` committed without its 9 files** (safe-merge exit 5). My remedy checkout then left 8 paths staged on
  the shared index for ~5 min and blocked peers (COO~O 27628). I unstaged and apologised; the worker re-landed the files
  @`fe9e397c5d`, merged @`b082af5f47`.
- **The first detached launch** failed on path quoting; no job ran.
