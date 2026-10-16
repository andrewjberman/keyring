# Drive log -- 2.0.0_SA_COO~MP -- NFRA_MCPORTAL -- 2026-10-16 ~09:2xZ to ~10:3xZ

Substantive ticks only. Lease: FULL. Cron `/canonical-drive NFRA_MCPORTAL once` at :17 and :47 (30m). PD HELD (CTO msg 34212). PF rounds 2, 3 and 4 MAY-CLOSE; Z-C-S40 REALIZED for today (CTO). S1 (MP-pf-4 served arm) open: limbs 1 and 2 read PASS, limb 3 (a resolved segment pair served) waits on MX-r-15.

| tick (UTC) | limb | outcome | act |
|---|---|---|---|
| ~09:4x | L7 real run (S1 served arm) | DRIVE FORWARD | ~O msg 34883: OG-ap-23 LIVE (3d5c9c8bf1, 27 of 27, mcportal pin 090b9cdc85, ledger closed 09:21:54Z). Ran pf4.served.sh: limb 1 read `descends: no` (ancestry is false by construction for a release built by taking files whole; CLAUDE.md 22a), repaired to a content comparison with a control (3 of 3 equal, old live differs 3 of 3) @d9f4ea1565; limb 2 yes; limb 3 NO: served _compute = 9 channels, 127 tools, m365 11, undeclared 92 (the PE grouping is live), 0 segments (no source_group or serves in the catalog until MX-r-15) |
| ~10:0x | preview | DRIVE FORWARD | previewed the page from ~MI's emitted catalog (blob cf7616c08e, trunk 739786b974, md5 9519ebce) through my handler's own readers: 127 of 127 tools declare a source_group; serves is list[dict] on 7 tools; 11 assets/bd tools, 9 distinct pairs; 4 Schwab helper tools carry no serves. Asked ~MI: intended per the C-GROUP amendment (serves only from rows naming the tool as read_tool), so the red gap class is the correct reading; a vendor on them is a CTO rule change |
| ~10:3x | wait | WAIT | MX-r-15 Phase A done (~MI applier ANNOUNCE fc2f9393d2); ~MI rules A-vs-B on scopes.json, then A2 (Phase B GO); target close before 13:00Z; ~MI messages me at the ledger close |

Carried to Andrew's live look (call 21d9): the four Schwab helpers read as the red "Vendor not resolved / Firm not resolved" class by contract; my recommendation is to leave it until he has seen the page.
Open: S1 limb 3 and the live 1280/390 screenshots (after MX-r-15 lands, then Andrew's signed-in look and the CVO's grade); MP-v-2 sign-in window on the CTO's word that Andrew is at the box (f0d2/21d9); the F2 re-run of the comparator (PF4.4); PD held.
