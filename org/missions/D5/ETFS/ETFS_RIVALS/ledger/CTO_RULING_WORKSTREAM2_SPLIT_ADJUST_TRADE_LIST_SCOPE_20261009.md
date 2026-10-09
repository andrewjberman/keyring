# CTO ruling -- ETFS_RIVALS WORKSTREAM 2, released NOW: split-adjusted history + dramatic-move lookup; the trade list scoped to the toggle

**Ruled by:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~05:2xZ, on `2.0.0_SA_COO~V1` msg 1758. **Andrew's words and measurements:**
`deliverables/2.0.0_SA_COO~V1/ANDREW_DIRECT_20261009_051xZ_UI_COMMENTS_TKOMY_CLOSE_AND_TRADE_LIST_SCOPE.md` @9d08dd64d4. He asked for
this as work "you can go pursue in the interim", so it runs now and does not wait for round 29.

## Placement

Rule 27: a workstream is a scope, not a round. Round 28 stays frozen on its three acts (the aw-1 deploy, the tc-1 merge, the
switch-on). **Workstream 2** is issued by `2.0.0_SA_COO~V1` (one project, one issuer) as its own issuance, with a write surface
disjoint from those acts. Each item is a build cell with at most three mechanical criteria.

1. **WS2-a, split-adjusted series** (comment 1, items 1-2).
   - Every price series the page draws is adjusted for share-count corporate actions, from STORED corporate-action rows: the dialog
     curve, the holding-implied points, the trade-marker prices and any return read from closes.
   - The factor and its source row are recorded with the series, and the dialog says when a series is adjusted.
   - Proof: TKOMY's 30d curve on a served page reads continuous across 2026-10-07, with the factor 15 read from a row, never typed.
2. **WS2-b, the missing action and the dramatic-move lookup** (comment 1, items 3-4).
   - A stored close past 3x, or below one third, of the prior stored close triggers a web search for that security's corporate action
     on that date (egress is open, law 4d77a9c3ea).
   - A split, reverse split or merger found with its ratio is stored as a corporate-action row carrying its source URL and
     `claim: inferred`, never `measured`.
   - Found nothing: the point is a gap with its reason, never drawn.
   - The gap behind it: the stored actions hold no TKOMY row. If the fix is a Bloomberg field the enrichment leg does not request
     today, that request is a Bloomberg draw and goes through MDPF_DEMQUE's queue as a quoted request.
3. **WS2-c, trade list scoped to the toggle** (comment 2).
   - The dialog's trade list shows only the toggle's window (30, 90 or 365 days), behind a closed disclosure.
   - Its heading names that window, and "Trades in the Last 365 Days" never shows on 30d.

## Guards (a criterion of EVERY workstream-2 order)

1. **No deploy before round 28's reads.** Nothing deploys a rivalfunds Lambda, the gateway or the page, and nothing writes a served
   rivalfunds key, before both round-28 J1 reads are taken: tw-1 at the 11:00Z vehicle run and aw-1 at the 13:00Z sweep. Merged code
   does not reach those runs; only a deploy would.
2. **Disjoint write surface.** No edit to `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py`, which is tc-1's and the round-29
   reader cell's. A cell that finds it must edit that file files a row and stops.
3. **Deploys and served writes go under their own never-widen pair** (this seat's half plus the COO's). The corporate-action rows from
   WS2-b are a served write. The vehicle is a site-Z producer, so any change its run imports also needs `1.0.0_SA_CTO~Z`'s half.

The round-29 pre-draft (`ledger/ROUND_ANALYSIS.round29.PREDRAFT.md`) is unchanged: WS2 is not in it.
