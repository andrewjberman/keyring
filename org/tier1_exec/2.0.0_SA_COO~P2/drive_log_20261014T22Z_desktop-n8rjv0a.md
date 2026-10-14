# Drive log -- 2.0.0_SA_COO~P2 -- 2026-10-14 22Z -- desktop-n8rjv0a

Project IRPT_BCKEND, workstream ~P, lease FULL. Round 197 (CTO analysis msg 7864: ship the cash rule without the CUSIP port; the port is its own release after a READ).

| time (Z) | round | what was measured | act fired |
|---|---|---|---|
| ~22:05 | 197 | pin 2 = 5fad7eaaa8 (one commit on b1d354cfc9, reverse of the port in holdings_snapshot.py), merged to trunk de08782c38; checks r197 written, dry-run at base 12 of 12 FAIL, control 12 positives, 27 negatives, 0 unexpected | issuance 70f82239a8: IB-pr-544..547 + decomposition section 189, `fanout: 2 of 2 chains, cap 8`; spawned ~389 (544) and ~392 (547) |
| ~22:20 | 197 | worker 389 report; issuer re-ran IB197-1-AC1..AC3 (PASS) and the proof check (VALID): bundle delta exactly holdings_snapshot.py, 34 of 34 closure members import under python -I per firm, closure == trace 46 of 46 | drained 52dea9de8a; 544 complete 25effde47d; spawned ~390 (545); retired account_id_hash_builder.py bd40386b7d (CTO msg 7872) |
| ~22:30 | 197 | worker 392 report; IB197-4-AC1..AC3 PASS; proof check INVALID until the two artifact pins were set to the carrying commit c611043bc2 (issuer fix 92ab8c02e8, then VALID). The READ: all 45 blanked Cottonwood sub-class values share one rule site, holdings_snapshot.py:993 (the CUSIP-keyed canonical row has no sub_asset_class; the prior path was the name-alias fallback). Options: keep_prior_sub_class (recommended), documented_correction, backfill_canonical_rows | drained 8d520aa652; 547 complete c79e2931d5 |

Waiting on: worker ~390 (IB-pr-545, built-bundle differential at pin 2), then ~391 (IB-pr-546, packet v3). Row W392-S2 (ARMED, disarm owner me) is dispositioned at round close with the 545 evidence that pin 2 changes no sub-class. Apply is NOT cut (both halves must sign v3 first). Scratch awaiting Andrew's word for a recursive delete: C:/dev/_scratch384 to _scratch387, _scratch389, _scratch392 and C:/dev/_scratchP2.
