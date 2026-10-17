# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 11Z (host opal_bloomberg)

## Substantive ticks since the 10Z log (ticks 154 to 161)

- NUDGE (tick 154): the `OG-ap-36` Phase A GO (35466) sat unread because ~NFRA1's inbox watcher was re-armed after the message landed (the shape of the earlier A2 GO); peek, one typed prompt, READ at 10:38:56Z.
- RECORD REPAIR (tick 157): git showed the CVO had already written the `Z-S312`, `Z-S336` clocks and the `Z-S356`, `Z-S358` dispositions; my "pending" in the 10Z log came from a stale note. Corrected (`87c596ada7`).
- `OG-ap-36` Phase A STOPPED (msg 35467, row `Z-S370`): on the candidate release `e45922ef75` (seven files from trunk, byte-equal) two host measurements failed: (e) the event loop starved 1 to 3.9 s during a page (limit 1 s; the live code held it 29.8 s), (a) median chain growth 27.7 MB per page (limit 20; the live code 18.3 in the same run, a median of three sawtooth differences). Passed: plateau +34.5 MB, first page 20.8 s against 29.7 s live, 4 of 4 pages equal row for row.
- RULING (tick 158): the limits are NOT relaxed. Inferred cause from the code: `typed_scope.py:155` converts the whole partition (`to_pylist`, `json.dumps`, `json.loads`) and `_read_partitions` filters to the account afterwards. Cut `OG-en-23` (`557b841548`, addendum R3-T.113, workstream `ENRICH-R41-Q`): `Ctx.read_account_rows` applies the 49F fence and the account test in arrow and converts only the account's rows, returning the same total and excluded counts; a non-string id column takes the old path. `OG-ap-36` amended A1 (re-run Phase A on the new trunk, eight files, six-page chain with the live code's six beside it).
- `OG-en-23` built by worker `~137`, drained `83c8c75f83`: my runs named tests 3 of 3, eleven-file window set 39 of 39 both orders, four-file set 12 of 12 both orders, `py_compile` ok, proof VALID; the commit-time client-data list was absent on this device, so I scanned the merged diff by text (0 long digit runs, 0 e-mails) and recorded that as the weaker check in ruling row `Z-S371` (`caa3177748`). Worker `~137`'s `tests/test_og_en22.py` edit: the fixture serves the bytes the new path loads; no assertion changed.
- Phase A RE-RUN GO (35469) sent to ~NFRA1 naming trunk_sha `caa31777489e84243b0f09dc02191132a7656b93`; at 12:00Z it is not yet read (the peek showed ~NFRA1 idle at input with its watcher armed before the message).
- Still ARMED (mine): `Z-S338`, `Z-S177`, `Z-W94-S2`. `Z-S370` stays open until the re-run passes. `Z-S369` was carried by MSTR~Z (READ 10:24:19Z).

## Next

The Phase A re-run report and `ap36.AC1` on my run; the three halves; the Phase B GO; the 30-minute read-back; the round-41 slug (draft committed `a4dd5853cf`).

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
