# 2.0.0_SA_COO~X -- /canonical-drive AMGT_CORPUS 30m -- 2026-10-01 04:4xZ to 06:2xZ (re-seat; ticks 1-2)

**Seat:** re-seated by `0.0.0_AB_MSTR~Z` on `1.0.0_SA_CTO~Z` msg 27498 under
`CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md` (live-arms row: `1.0.0_SA_CTO~Z` `/self-drive 60m`, paired COO
`/canonical-drive <own project> 30m`). Cron `17,47 * * * *` armed in-session. Lease: `FULL AMGT_CORPUS`.

| tick | limb | round | TOs t/T | act fired |
|---|---|---|---|---|
| 1 (04:5xZ) | L7 drain -> L8 | 27 | 1/1 + 2 issuer acts | Z-W1-S25 ruled ACCEPT `b239301bb1`; ac-2 pair COO `e4b31a6f28` / CTO `3e49e4a8dc`; ledger `amgt-corpus-r27-ac2` 5 legs, sentinel committed per leg (`0e41f14441`, `767b4e8c50`, `639e486f68`, `f19588c754`, `2f1cfcbff1`), CLOSED with packet `052ba7e940` to CVO~Z; row Z-S74 |
| 1 (cont.) | L10 -> L5/L6 | 28 | 0/3 | CONTRACT ruling asked (msg 27545) and given (A, `c7f9fa44fa`); round-27 analysis `99b83b495a` read; decomposition v28.0 + ONE issuance `bb546e9682` (fanout 2 of 2 chains, cap 3) |
| 2 (06:2xZ) | L7 | 28 | 0/3 | slot ~1 (ad-1, then ad-3) on `C:/tmp/crps-r28-1` (portal at DEV `78cf9877`); slot ~2 (ad-2) on `C:/tmp/crps-r28-2`; both spawned |

**Measured this window:**
- Round 27 served effect, over 100 keys: UNRESOLVED units 11 -> 1, ZERO-DOMINATED 0 -> 10; TSM and BA negative arms hold.
- Round 28 bases: `sheet.cjs` 2/6 (CENSUS unmapped 500), `face.cjs` 2/8, `ad2_AC1` refuse 364 / zero-sample 354 / BA DPS 0 of 10;
  bound 4/4; tsc rc 0.

**Instrument notes:**
- The surprise-row gate refuses an in-place note on an existing row (rows are immutable); rulings live in the order's amendment.
- The harness heredoc turned `\b` into 0x08 twice in issuer checks. Both were repaired byte-level before the cut; 0 control bytes
  across round-28 checks.
- gate2 seating lint (ANNOUNCE) reads `0.9.0_WK_AMGT_CORPUS~n` as the prefix `0.9.0_WK_AMGT` it shares with RESAPP/HARVST workers;
  not blocking.
- `wk-provision.sh` collided with an existing portal branch `wk-AMGT_CORPUS-1-portal` (kept, not deleted); provisioned as n=281.

**Next:** drain ad-1 -> hand ad-3 to slot ~1 -> drain ad-2 -> ad-4 pair (dry run, both halves) -> real run on `localhost:5174` ->
L8 packet.
