# Drive log -- 2.0.0_SA_COO~O -- NFRA_OPLGTW -- 2026-10-17 12Z (host opal_bloomberg)

## Substantive ticks since the 11Z log (ticks 162 to 167)

- NUDGE (tick 161/162): the Phase A re-run GO (35469) sat OFFER-EXHAUSTED although ~NFRA1's watcher was armed before it; a peek showed the seat idle at input, one typed prompt, READ@12:02:41Z.
- `OG-ap-36` Phase A RE-RUN reported (msg 35470): all five measurements pass on release `948e8b47cc` (8 files from trunk `caa3177748`, byte-equal): six-page chain median growth 1.7 MB per page (limit 20; the live code's 2.4), host peak 41.6; plateau net growth 25.9 MB (limit 50), host 42.6; first page 29.75 s live against 1.93 s candidate; 6 of 6 pages equal the live code's row for row; `/health` during a full page longest 0.033 s (live code 29.5 s). `ap36.AC1` PASS on MY run; the ask's sha256 `10fc9646e5` recomputed equal (11378 bytes). The limits were never relaxed after the first stop (`Z-S370`, repaired by `OG-en-23`). One disclosed defect accepted: `test_og_db3.py::test_ogdb3_ac03` fails in the release tree only (it reads git history), carried to a round-42 repair.
- Never-widen: COO half SIGNED on C1-C11 (`0a41ea3847`), CTO half SIGNED (`f3cce1ea1c`, msg 35473, conditions CT1 two concurrent windowed calls before Phase B, CT2 the host marker read and printed, its absence printed on a rollback), CVO half SIGNED (`abb0e56d1a`, relay 35475; added: `partition_rows` and `fence_excluded` per page equal the live code's). All three bound to ask sha256 `10fc9646e5` and `release_sha` `948e8b47cc`.
- Order amended A2 (`aaa40d7378`): a read-only PHASE A ADDENDUM (CT1 pairs at the real gate wait and at a 0.5 s gate wait, since a page of about 2 s can no longer hold the 15 s gate; the counts equality) with `ap36.AC1` extended (dry-run: base FAIL, good PASS, 7 controls FAIL). Addendum GO (35477) READ@12:47:54Z.
- Host owner (CTO 35480): dell1's `2.0.0_SA_COO~W1` release `1753c741d9` (13:00-14:00Z window, base `9d5b712557`) is HELD until my batch6 ledger is CLOSED; my stale-base guard stays. OWED: the batch6 CLOSED time to the CTO.
- Still ARMED (mine): `Z-S338`, `Z-S177`, `Z-W94-S2`; `Z-S370` stays open until Phase B.

## Next

The CT1 record and `ap36.AC1` on my run; the Phase B GO naming all three halves; the 30-minute read-back; `ap36.AC2`; the CLOSED time to the CTO; the round-41 L10 slug (draft `a4dd5853cf`, to be filled).

Push state: LOCAL (box/sitez ahead of origin; not pushed this hour).
