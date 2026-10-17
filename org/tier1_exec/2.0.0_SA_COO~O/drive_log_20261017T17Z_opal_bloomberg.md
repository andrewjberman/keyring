# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 17Z to 18Z (host opal_bloomberg)

## Substantive ticks since the 16Z log (ticks 188 to 190)

- `OG-ap-36` Phase B (applier msg 35538): release `efcc8ae19f` LIVE at 17:06Z on dell1's base `1753c741d9` (base guard equal, marker equal to the release sha, host md5 139 of 139, `harvest_research.py` md5 equal to its `1753c741d9` blob, nine arms true, no ask trigger; the manifest at `box/sitez` HEAD now reads `efcc8ae19f7e`, deployed_at 17:06:00Z).
- INCIDENT (row `Z-S375`, ARMED, disarm owner this seat): the applier's unguarded 27-tool harness took the 1.8 GB host out of memory at 17:21Z through `etfs_compare_peers` (a module byte-equal on both refs and importing no changed file): the gateway was killed once (back in 3 s, health 200) and eight system daemons (restored; `chronyd` unsynchronised until it polls). Under a hard guard the same call raises MemoryError, so the served read is 26 of 27. Any caller can still trigger it.
- CTO decision 35541 (and 35540): grade 26 of 27 with the exception named and the row open; NO further probe on the live host; this seat cuts the fix cells now. CVO condition (35544, adopted 35546): the second read-back prints `chronyc tracking` (Leap status Normal, synchronised) and `systemctl --failed` (0 units) before the ledger closes; the record's wording on the 27th tool is a trigger set aside by ruling, not one that stayed clear.
- Order amendments: A7 (`1b6c2a878d`): `ap36.AC2` accepts 26 of 27 ONLY with `per_tool_exception` [`etfs_compare_peers`] and `exception_row` `Z-S375`; A8 (`1da9da739c`): `host_clock` Normal and synchronised, `systemd_failed_units` 0; both dry-run (accepted shapes OK, every other shape NO). Ruling and A8 sent to ~NFRA1.
- Repair cells cut: `OG-en-25` (`typed_scope.read_parquet` refuses a FILTERED table over a 64 MB in-memory cap before any Python conversion, protecting every typed reader; `etfs_compare_peers` reads its peer tables with Arrow filters and takes the available values from an Arrow `unique`; a fresh-process heap test) and `OG-un-1` (`MemoryHigh=1200M`, `MemoryMax=1400M`, `OOMScoreAdjust=300` on `deploy/opal-gateway.service`), commit `6784006a1f`, addendum R3-T.116, workstream `ENRICH-R41-T`, 2 of 2 chains cap 8; base checks FAIL as expected; workers `~139` and `~140` spawned. The cause is a code reading (whole-table `to_pylist` after only a compressed-size cap, the class `OG-en-23` fixed for the 49F window), INFERRED; the host measures it in the fix release's Phase A under a hard guard.
- Still ARMED (mine): `Z-S375` (new), `Z-S338`, `Z-S177`, `Z-W94-S2`; `Z-S370` and `Z-S372` close with the batch6 ledger. `OG-ap-37` stays staged.

## Next

Workers `~139` and `~140`: read the diffs, drain, re-run the checks; ~NFRA1's second read-back and the ledger CLOSED time (the clock and failed-unit print first); `ap36.AC2` on my run; the CLOSED time and final live sha to the CTO (C13); `Z-S338` re-read; the `OG-ap-37` GO; the fix release's order (its own never-widen); the round-41 slug (draft carries the known entries; round 42 gets `Z-S375` first).

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
