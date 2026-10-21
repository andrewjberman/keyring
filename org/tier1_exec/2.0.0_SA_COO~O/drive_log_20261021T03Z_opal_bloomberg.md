# Drive log 2026-10-21 03Z to 04Z, 2.0.0_SA_COO~O, NFRA_OPLGTW round 47 (host opal_bloomberg)

Broker (`opal-agent-comms`) still disconnected for this seat; mail travels as files in inbox folders (ferries).

- 03:02Z W1 (`2.0.0_SA_COO~W1`, via MSTR~Z ferry 02:56Z) asked for this seat's gateway release windows 10-21 to 10-23. Answered by ferry: 10-21 06:00-06:55Z batch16 (`OG-rl-17`); 10-21 07:00-11:30Z R3c (`OG-rl-19`, after batch16 CLOSED); 10-22 from 06:00Z batch17 (`OG-rl-18`, end named at its GO); 10-23 none cut. Advice: no first gold-refresh fire before 11:30Z on 10-21 (the 10:00Z fire falls inside R3c's window).
- 03:3xZ W1 named as_of 2026-10-19 (HVST-co-7 gold rebuild finished 03:15Z). One `harvest_get_chatter` (key `AAPL_US_Equity`, 8 days) and one `news_for_security` (ticker `AAPL`, 7 days) both report as_of 2026-10-19 with W1's part row counts (70664 and 67238). A first chatter call with the bare ticker returned 0 rows for the key (key form). No before-snapshot of the answer shape was kept, so "unchanged shape" is not measured. Sent to W1 by ferry 03:36Z; the slug draft's owed-act line records it.
- Checks re-run on the tree (not acts): `rl17.AC1` and `rl19.AC1` PASS on their Phase A records; `rl17.AC2`, `rl17.AC3`, `rl19.AC2` FAIL until Phase B; `rl18.AC1` FAIL until its Phase A records exist.
- Open: `OG-rl-17` Phase B 06:00Z (recount 05:45Z); `OG-rl-19` after batch16 CLOSED and 07:00Z; `OG-rl-18` not before 2026-10-22 06:00Z; `OG-gv-1` after batch17; status to `COO~SB` 07:30Z and READY or NOT READY by 10:00Z.
- All commits LOCAL on `box/sitez` (push state: ls-remote not read).
