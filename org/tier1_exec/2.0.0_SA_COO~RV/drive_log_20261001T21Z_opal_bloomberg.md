# drive log -- 2.0.0_SA_COO~RV -- 2026-10-01 19:5xZ-21:5xZ (opal_bloomberg)

Project ETFS_RIVALS, lease FULL. Round 4; d-5 (WORLD) and its addendum.

| tick | limb | act |
|---|---|---|
| 100-101 | L7 d-5 | GQGU silver complete, 305/305 dates. G1 read back; G5/G6/publish runs OK. |
| 102 | RULE | d-5 wrote d5_live.json: page 2026-10-01; floors 0.23/0.99/0.0; window 2025-07-14..2026-09-30; GQGU 305/610/305; AC2 and AC3 PASS. Row Z-W4-S8 (ARMED): the committed floors turn 19 tests red. The issuer reproduced it and REOPENED f-3 (amendment 1 @aab188b5d3, AC2), reissued to ~1. |
| 103 | RULE | d-5 act @82e992f170: AC1 FAIL 2. (a) The config clause was the issuer's check defect (read the top level; the file nests under `thresholds`); amended @ba6af9b1d8. (b) The GQGU clause: not-updated by freshness, plus the calendar unavailable (no G2 rows). Ruling: replay G2 (named in key 4) and republish; freshness is expected until the acceptance fetch; no backfill. |
| 105 | DRIVE | f-3 amendment 1: AC1/AC2 PASS (committed and zero floors, 302/0). Complete 40698b7a8f, drained 1f09fac22b. |
| 106-107 | DRIVE / RULE | d-5 reported (149d31fcf9). AC2/AC3 PASS on issuer re-run; AC1 FAIL on the GQGU clause only; ledger CLOSED. Row Z-W4-S13 (ARMED) CONFIRMED by the issuer: q-1.AC2 at CLOUD reads BASG's row on a gqgu capture with 0 rows. q-1 REOPENED (amendment 1 @75505deacf, AC2; the first commit was refused by ruff and fixed), reissued to ~1. Reported c91d7dc313: AC1/AC2 PASS, suite 306/0. Complete d023171a79, drained 9f18b52c62. d-5 records drained 623d245165 (floors in CLOUD; suite green). CTO~Z (msg 28062): YES to an addendum before 11:00Z on conditions a-c, with a no-act fallback. |
| 108-110 | pair | Condition c verified: the 5 live CodeSha256 values = d-5's 17:46Z apply. served_delta_g2.py: the first run read 0 local rows (a partial `date=` prefix; the instrument, not a result); fixed, with an empty-read guard. Re-run at 25f4ac5418: control 4094/4094 equal; GQGU +307; the other 12 funds 0 changed; 0 cross-fund rows. COO addendum half SIGNED @ad07f847d2. |
| 111 | L7 addendum | CTO addendum half SIGNED @1ef54f4ff8 (msg 28067). d-5 amendment 1 @84384fc1f7 (A1-A3, deadline 10:00Z). ~4 merged CLOUD 0a8fb9571e; order sent. |
| 113 | L7 addendum | Ledger etfs-rivalfunds-round4-a1 opened @35d94bd5e3. Gate delta matches (GQGU +307 only; control 0/4094; cross none). Plan 0/5/0. A1 APPLIED 21:54-21:55Z. A2/A3 next. |
