# Drive log -- 2.0.0_SA_COO~F2 -- IRPT_DASHBD F-SHIP (the idle hours 09Z-16Z, 2026-10-15)

Every F-SHIP round (114-118) is closed and slugged; the only acts of these hours were seam probes and a registration record, all committed (`ee359d687f`, `16ec8e1fdf`, `31c164f492`, row `D2-S70` at `3ba6251d8c`). One summary, not one entry per tick.

## What the ticks found (ticks 14-26)
- 09Z-10Z: `open-calls.py add --kind approval --check-only` read OK at the candidate head 65f2e543 (30 commits): registration is ready (`CANDIDATE_REGISTRATION_READY_F_SHIP.md`); PROD moved to c3b21a40 (7 MDPF_CANON commits, none under InvestorReporting/); a trial merge-tree of the candidate is clean.
- 08Z: the page's export wire matches the merged submit handler (`export/entry.py` `_page_pins_dropped`, `retained_export.py` `parse_filled_report_source`): no row.
- 11Z-16Z: no FREE option (`/next-calls --drive`): the serve path's deploy legs (hops 2-4, ~P2's pair) wait on the first cloud write of 49F's `filled_report_values` gold; hop 1 was applied 11:49:38Z and its first scheduled fire is 2026-10-16 about 11:41Z (~D2's round-129 drain-end packet line 27; the CTO's round-124 analysis: "applied, not proven"). Row D2-S70 (the filled route ignores `version_id`) is unanswered by ~P2. Call a252 is Andrew's and not the DEV sample's gate.
- The dated WAIT: `unblock.py tick --wait-until 2026-10-16T12:00:00Z --owner 2.0.0_SA_COO~D2` (WAITING DATED, empty count 0). The first attempt with owner ~P2 read "owner-not-live" and counted one empty tick; ~P2 was LIVE by `get_live_agents`, so that read was a tool quirk.
- 12Z and 15Z: no commit-worthy act.

## State
- Candidate `cand/dell2/irpt-default-performance-report` = portal 65f2e543 (30 commits over origin/PROD 5d646418; current PROD c3b21a40): local, not pushed, not registered.
- Push state: origin/box/dell2 carried my commits through `ee359d687f` at the last read (ls-remote 09:2xZ); later commits LOCAL until the next box-sync.
- Next: 2026-10-16 ~12:00Z re-check (hop 1's first fire, ~P2's pair, S70); then the first real run on DEV, the re-cut onto the current PROD and the registration.
