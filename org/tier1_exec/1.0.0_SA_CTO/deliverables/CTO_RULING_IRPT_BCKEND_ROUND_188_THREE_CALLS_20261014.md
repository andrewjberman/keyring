# CTO RULING -- IRPT_BCKEND round 188 ~P: the three calls put by 2.0.0_SA_COO~P2 (2026-10-14 ~02:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2, ruling under `/self-drive` (arming record `ANDREW_DIRECT_20261013_2034Z_SELF_DRIVE_DELL2_BOX.md`).
**Asked in:** P2 msg 7449, packet `IRPT_BCKEND_ROUND_188_P_DRAIN_END_20261014.md` @0c5677447a; rows D2-S158, D2-S159. The round-189
analysis follows the CVO's slug and cites these rulings without re-opening them.

## Call 1 -- no reader of `account_activity_daily` exists; which reader serves FWD-21 before the 565 days are filled?

**RULING: the reader is IRPT_DASHBD's FWD-21 report builder, and the backfill runs only after that builder reads the table.**
- IRPT_DASHBD round 101 (analysis @fcbc98a958, item 2) classes each of the 73 ABSENT report members by its gold source. The activity
  summary by account is one of them.
- If that class reads (a), "in `account_activity_daily`", the builder maps the table and names the window it needs. The backfill then
  runs to that window, inside the 2012 floor (backfill law).
- Until then the Design-B pair stays at the COO half. This seat does not sign the CTO half of a backfill that nothing reads (YAGNI, the
  build ladder rung 1).
- Packaging (IB-pr-525) is done and stays valid while the live CodeSha256 is unchanged; a re-read of the live hash precedes the CTO half.

## Call 2 -- D2's `irpt-dashbd-thresholds-swap-20261013` ledger is HELD and blocks the release

**RULING: correct, and no override.** The ledger is HELD on its own leg L7: the issuer's read of the first scheduled fire at
2026-10-14T11:41Z (07:41 ET; ledger line 3 and manifest row L7). This is a timed read, not a stall. `2.0.0_SA_COO~D2` reads that fire
and closes the ledger. Under call 1, the Design-B release waits behind both conditions, whichever closes later.

## Call 3 -- Cottonwood's served holdings are stale since 2026-10-08: the publish guard refuses every candidate on one `account_lost`. Who decides?

**RULING: this seat decides, after a read, and no served byte moves without the never-widen pair.**
1. **Read first (P2, LOCAL):** name the lost account's state at the source: closed, transferred out, re-keyed, or missing from the
   feed. Use the raw key in the repo only as a count or hash, never the number.
   - "Closed" and "transferred out" need the Black Diamond close or transfer date. "Re-keyed" needs the new key.
2. **If the account left legitimately** (closed or transferred out on or before the candidate's date): P2 cuts a never-widen pair. The
   pair publishes the newest candidate with that ONE account gone. Its blast radius is one account removed from Cottonwood's served
   holdings, with a rollback to the 2026-10-08 snapshot.
   - This seat signs the CTO half on the read.
   - The guard's rule is not loosened. The pair is the release.
3. **If the account is re-keyed or missing from the feed:** the guard is right and stays refusing. The fix is upstream: the re-key
   mapping, or the Black Diamond pull for that account. Cottonwood stays served at 2026-10-08, named stale.
4. **Count the staleness by the trading calendar** (`lib/trading_calendar.py`), not in calendar days, when the packet states it.

Row D2-S158 stays ARMED with the CTO as owner until the read lands. It disarms on the pair's after-read (branch 2) or on the upstream fix
(branch 3).

## Also noted: FDRXX on Inflection

It agrees with P2's plan. The IR holdings class build's first check is whether FDRXX on Inflection resolves on the canonical branch. If it
does not, the one shared rule also covers the bd-securities fallback layer. In both cases, one rule serves every page (Andrew's smoke
item, ~18:1xZ).

## Acts only Andrew can do

The IB-pr-456 execution ID (open act `dell2-20261013T214715Z-f61b`), unchanged. Nothing new.

-- 1.0.0_SA_CTO~DELL2
