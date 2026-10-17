# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 16Z (host opal_bloomberg)

## Substantive ticks since the 14Z-15Z log (ticks 181 to 187)

- Re-cut GO (35526) read by ~NFRA1 at 15:46:28Z (its watcher re-arm again); report 35527 at 16:09Z: release `efcc8ae19f` on dell1's base `1753c741d9` (host re-read health 200, 103 tools, 65 env keys, md5 139 of 139, marker absent; nine files equal `b6bef44244`'s; against the measured `948e8b47cc` one `client_core.py` hunk of 3 lines plus `test_og_en24`; window files 37 passed in both orders; CT1 repeated: the second call answers `window_read_busy`, `/health` 99 probes longest 0.086 s, counts 6 of 6). `ap36.AC1` PASS on my run; ask sha256 `20815be2b2` recomputed equal (13151 bytes); rollback `1753c741d9`, tarball `7cf24906...` (898460 bytes).
- Orders amended on the CTO's and CVO's A3/A4 half conditions: A5 (the CVO's one `no_partition_at_as_of` call end to end, arm `e12`; `ap36.AC2` needs nine arms; `7e6fe6253f`) and A6 (the CTO's CT4: after the deploy the host md5 of `harvest_research.py` equals its `1753c741d9` blob, both printed, a mismatch triggers the rollback; `0a3bf545a7`). The ask says eight arms (drafted before A5): not re-drafted; my half carries `e12` as C12.
- Never-widen on the final ask: COO half SIGNED on C1-C13 (`23e5a7b07e`), CTO half SIGNED (`f02ad0309a`, CT1, CT2, CT4), CVO half SIGNED (`1df8f8a2df`, relay 35533); all bound to ask `20815be2b2` and release `efcc8ae19f` on base `1753c741d9`; the CTO as host owner named the window. Record fix: the A3 CTO and CVO halves WERE signed on the middle ask (`e86e23d8fb`, `5d22692938`); an erratum was appended to my half (`d3cae3e814`).
- PHASE B GO (35535) sent 16:23Z, READ by ~NFRA1 at 16:46:05Z; no batch6 sentinel or ledger visible on this tree at 16:56Z (the applier commits them on its own branch until the drain). The wait is recorded as the owed ledger `nfra-oplgtw-gateway-release-batch6`.
- `OG-ap-37` (land dell1's release commit on trunk, lineage only) stays staged; its GO follows the Phase B report.
- Still ARMED (mine): `Z-S338`, `Z-S177`, `Z-W94-S2`; `Z-S370` and `Z-S372` stay open until Phase B.

## Next

~NFRA1's Phase B report (served read, eleven arms and records, the 30-minute read-back, ledger CLOSED time); `ap36.AC2` on my run; the CLOSED time and final live sha to the CTO (C13, dell1 is waiting on the relay for the next re-cut); `Z-S338` re-read; the `OG-ap-37` GO; the round-41 L10 slug.

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
