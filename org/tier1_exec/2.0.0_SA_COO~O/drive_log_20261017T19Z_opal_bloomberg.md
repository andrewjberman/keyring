# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 18Z to 19Z (host opal_bloomberg)

## Substantive ticks since the 17Z-18Z log (ticks 191 to 195)

- `OG-un-1` (worker `~140`) drained `a6788723f3`: the unit gains `MemoryHigh=1200M`, `MemoryMax=1400M`, `OOMScoreAdjust=300` and nothing else; my runs named 2 of 2, proof VALID.
- `OG-ap-36` CLOSED: Phase B report (35548): ledger `nfra-oplgtw-gateway-release-batch6` CLOSED 2026-10-17T18:11:52Z, live `efcc8ae19f`; read-back 2 (17:37-18:07Z) 0 triggers, ZERO window calls (`Z-S338` stays open); `ap36.AC1` and `ap36.AC2` PASS on my runs (26 of 27 with the named exception `etfs_compare_peers`, row `Z-S375`), proof VALID. The applier closed the ledger BEFORE reading the CVO's A8 clock condition (the clock read at 18:16:58Z was Leap Normal, synchronised, one stale `init.scope` failed unit cleared by `reset-failed`): recorded as an order-of-acts miss with a met outcome. Flipped to complete; ruling row `Z-S376` (`0c159a653f`); the CLOSED time and final live sha sent to the CTO for dell1 (C13).
- `OG-en-25` (worker `~139`) drained `a197c3fc38` (typed Parquet 64 MB in-memory cap on the filtered table before any Python conversion; `etfs_compare_peers` filters in Arrow; `distinct_values`); my runs named 3 of 3, seven-file set 29 of 29 both orders, proof VALID; ruling row `Z-S377` (a peer part lacking `period`, `axis` or `fund_id` now answers absent; twelve `read_parquet` call sites in eight modules sit behind the cap; two GETs per peer call).
- `OG-ap-37` (land dell1's release commit `1753c741d9` on trunk): refreshed twice before the GO (the manifest on trunk reads `efcc8ae19f`, previous `1753c741d9`; trunk was ahead of dell1's `harvest_research.py` after `HVST-ce-3`, so two conflicted paths take trunk's side); landed by ~NFRA1 (35553; `safe-merge --continue` refuses an empty staged set, row `Z-S378`, so a `commit-tree` on a scratch branch), drained by me `09cae34ff0`; `ap37.AC1` and `AC2` PASS on my runs, proof VALID; ruling row `Z-S379`; dell1's release is now a trunk ancestor.
- `OG-ap-38` CUT (`e6f6f3b27b`, addendum R3-T.117, workstream `ENRICH-R41-V`): the sixth release (`OG-en-25` and `OG-un-1` as one release, five files) on the live ref `efcc8ae19f`; every host run of gateway code under a HARD GUARD (the lesson of `Z-S375`), the clock and failed units read BEFORE the ledger closes (the lesson of A8), the 27-tool read must be 27 of 27 under the guard; `ap38.AC1`/`AC2` dry-run (pass arms ok, 17 controls NO). Phase A GO (35554) sent 19:11Z to ~NFRA1 naming `trunk_sha` `140239815b`.
- `round-close-check` round 41: 11 orders, 10 complete, `OG-ap-38` not complete and outside the verdict; verdict MAY-CLOSE over the other ten. L10 waits on `OG-ap-38` terminal.
- Still ARMED (mine): `Z-S375` (until `OG-ap-38` is live and measured), `Z-S338`, `Z-S177`, `Z-W94-S2`.

## Next

~NFRA1's `OG-ap-38` Phase A report and `ap38.AC1` on my run; the CTO's half and the CVO's relay (naming my reading of "each under its own never-widen" as one release, one ask); the Phase B GO; the ledger `nfra-oplgtw-gateway-release-batch7`; `ap38.AC2` on my run; the CLOSED time to the CTO; the round-41 L10 slug (draft carries every order and the round-42 list, `Z-S375`'s disarm first).

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
