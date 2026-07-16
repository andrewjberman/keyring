# P0 INGESTION CENSUS -- THE BASELINE READ (2026-07-16 ~04:50Z, 1.0.0_SA_CTO)

**Authority: Andrew-direct verbatim x2 (CTO terminal ~04:4x-05:0xZ):** (1) *"If we do not have
at least July 14 if not July 15 in every single bronze and silver bucket at parity, then
ingestion is not programmatic, and that is P0 fix required immediately."* (2) *"I want all of
this routed immediately p0. Need backfill first and incremental pulls scheduled henceforth,
make it so."*

Instrument: full two-layer key listing per channel (66,874 keys), date tokens extracted, bar =
07-14 minimum / 07-15 target, BOTH layers, EVERY channel. Acceptance re-run uses this same script.

| channel | layer | max_date | 07-14 | 07-15 | n_keys | verdict |
|---|---|---|---|---|---|---|
| blackdiamond/49f | bronze | 2026-07-15 | YES | YES | 12 | PASS |
| blackdiamond/49f | silver | 2026-07-14 | YES | no | 2 | PASS |
| blackdiamond/cottonwood | bronze | 2026-07-16 | YES | YES | 319 | PASS |
| blackdiamond/cottonwood | silver | 2026-07-16 | YES | YES | 518 | PASS |
| eclipse/inflection | bronze | 2026-07-10 | no | no | 624 | FAIL |
| eclipse/inflection | silver | 2026-07-10 | no | no | 192 | FAIL |
| orion/inflection | bronze | 2026-07-16 | no | no | 4644 | FAIL |
| orion/inflection | silver | 2026-07-16 | no | no | 4644 | FAIL |
| pathfinder | bronze | 2026-07-15 | no | YES | 2 | PASS |
| pathfinder | silver | 2026-07-15 | no | YES | 4 | PASS |
| schwab/08242234 | bronze | 2026-07-14 | YES | no | 6246 | PASS (T-1 pattern; 07-15 lands ~09:46Z) |
| schwab/08242234 | silver | 2026-07-14 | YES | no | 7619 | PASS (T-1 pattern; 07-15 lands ~09:46Z) |
| schwab/08335338 | bronze | 2026-07-14 | YES | no | 6959 | PASS (T-1 pattern; 07-15 lands ~09:46Z) |
| schwab/08335338 | silver | 2026-07-14 | YES | no | 8452 | PASS (T-1 pattern; 07-15 lands ~09:46Z) |
| smartx | bronze | 2026-07-15 | YES | YES | 26349 | PASS |
| smartx | silver | 2026-07-15 | YES | YES | 13 | PASS |
| trueshares | bronze | 2026-07-15 | no | YES | 2 | PASS |
| trueshares | silver | 2026-07-15 | no | YES | 2 | PASS |

**FAILS**: eclipse (both layers dead at 07-10) · orion (07-11..07-15 hole both layers; revived
only via tonight's window run) · bd49f SILVER (07-14 vs its bronze 07-15 -- parity lag).
**Work packages** (routed 05:02-05:04Z): WP1 eclipse [0.7.0+~B] · WP2 orion hole [same] · WP3
bd49f silver [~B] · WP4 smartx scheduler [0.7.0] · WP5 wsb_49f feeder backfill+scheduler [0.5.0
+CTO scoping] · WP6 ETF history [0.5.0, P1]. Task #15. Notes: events do NOT retro-fire on
backfilled keys (dated conversions required); the gold chokepoint is NOT needed for bronze+silver
(mirror+event path proven on orion 07-16 tonight); INF gold daily-release = separate co-sign.
