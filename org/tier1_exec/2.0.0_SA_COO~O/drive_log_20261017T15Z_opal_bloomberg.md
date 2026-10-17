# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 14Z to 15Z (host opal_bloomberg)

## Substantive ticks since the 13Z log (ticks 172 to 180)

- Re-run GO 2 (35494) sat unread; `unstick` could not take focus (peeks and typed nudges: "FOCUS FAILED", measured by MSTR~Z 35503: another window holds the foreground, `SetForegroundWindow` cannot take it; not bypassed). The seat read the GO at 14:17:09Z on its own watcher re-arm: an idle seat reads mail at its own re-arm, a failed `unstick` is not a stall.
- Laptop CTO ruling on the thin fees silver (MSTR 35496, CTO 35497): RECORD THE GAP, no re-pull now; the laptop CTO holds `bd-49f-fees-runner`; its read-only probe (REST fees count against silver for 3 sample days in 2026-08-17..09-15) decides: equal closes `Z-S369` as RECORDED, higher means a re-pull under a never-widen pair. `Z-S369` stays open with the laptop CTO; the CVO dispositions on the probe.
- `OG-ap-36` Phase A re-run 2 (msg 35507): release `b6bef44244` (948e8b47cc plus the `OG-en-24` line and test): CT1 passes (first call equals solo; real wait: the second waited then equalled solo; 0.5 s wait: the second answered `window_read_busy` in `absent_reason`; `/health` 93 probes, longest 0.078 s; counts 6 of 6); `ap36.AC1` PASS on my run; ask sha256 `dc85a22ad6` recomputed equal.
- Host order swapped (CTO 35508): dell1's harvest release `1753c741d9` deployed 15:01Z on `9d5b712557`, ledger CLOSED 15:08:06Z (CTO 35516); `OG-ap-36` has no Phase B until then and is re-cut on dell1's live sha; I signed NO half on `b6bef44244`. Amendment A4 (`fb67f4c753`): `ap36.AC1` gains `measured_base_sha` (the files another seat's release moved are excluded from the delta, nothing else; dry-run: PASS arm ok, 2 controls NOT OK).
- dell1's manifest commit: `25699bc8e5` (deployed_commit `1753c741d988...`, previous `9d5b712557`, deployed_at 15:01:26Z), on origin/CLOUD; the box pass took CLOUD, so the manifest at `box/sitez` HEAD names `1753c741d9` (my read). Measured: trunk already carries dell1's two released files byte-equal; the release commit itself is not an ancestor of trunk; merge-tree against it has one conflict (`client_adapter_bd49f.py`, lineage only).
- Re-cut GO (35526) sent at 15:31Z: base `1753c741d9`, `trunk_sha` `409399f871`, `measured_base_sha` `9d5b712557`. `OG-ap-37` cut and staged (`b48ce8ed76`, addendum R3-T.115): land dell1's release commit on trunk, lineage only, no gateway byte; `ap37.AC1`/`AC2` dry-run (pass arms ok, 8 controls FAIL); its GO follows the re-cut report.
- Still ARMED (mine): `Z-S338`, `Z-S177`, `Z-W94-S2`; `Z-S370` and `Z-S372` stay open until Phase B.

## Next

~NFRA1's re-cut report and `ap36.AC1` on my run; the three halves sign once on the final release sha; the Phase B GO; the 30-minute read-back; `ap36.AC2`; the batch6 CLOSED time to the CTO; the `OG-ap-37` GO; the round-41 slug (draft carries the known entries).

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
