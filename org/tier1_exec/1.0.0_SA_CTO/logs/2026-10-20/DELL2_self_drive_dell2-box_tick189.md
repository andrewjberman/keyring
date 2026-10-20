# /self-drive dell2-box -- ticks 187-189 (2026-10-20 ~20:27Z-21:56Z), 1.0.0_SA_CTO~DELL2, cadence 30m

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md`.
**Covers:** ticks 187 to 189, since the tick 186 log (@5031d3d083). state: ARMED.

## Andrew at the desk (~20:3xZ)

- He asked what he could look at, then whether we were ready to run the test.
- **Answered:**
  - the walk form is live on PROD;
  - filing works through to the 4 attachments;
  - opening the two PDFs waits on the r37 irpt-status release;
  - `~Y2`'s ETA was given as an estimate, not a measurement.

## r37 irpt-status: the two PDF routes

- **CTO half SIGNED @3f1961ceab** on `~Y2`'s packet (blob f0a152fd55, sha256 f47c8a08).
  - Read here: the live CodeSha `274dl2bC...` equals R0.
  - `owned_report.py` is the only non-test mover; AR-y-470 and AR-y-472 are as ruled.
- **LIVE at 21:33:49Z.** Read here: CodeSha `B4R0dZqB...` equals the packet.
- **IB2 `A_AFTER_R37.txt`:** G1 to G6 hold; the Overview route went from NOT_FOUND to a download link on an older request.
- **Next:** run 7d (GO by `~Y2`) reads both routes live.

## r34o: FWD-10 comparison, audit wiring, Overview price pages

- **CTO half SIGNED @4e5f63eba0** on `~G2`'s packet (blob bb2bf1ec4b, sha256 95c3615b).
- **Precondition:** no apply until run 7d is terminal.
- **Movers accepted:**
  - the price pages are covered by the v0.25 supersession of XA-2064 for FWD-10, and are merged work, not new performance work;
  - the `trading_calendar` change is additive.
- **FWD-9:** Andrew's sample is one Overview filed after r34o, because r34o changes the Overview.

## Cross-box: closed (laptop CTO msg 110026)

- Andrew "Yes go ahead": the stray Scope key is deleted, and the inf mirror catch-up is clean (laptop record a7852b5b44).
- The Scope feed's re-point to `opal-data-inf` is still owed by IRPT_BCKEND; the feed stays frozen.

## Acts only Andrew can do

- **Row a331** (an entitlement): the outside-domain users row in TCKT_VNEXT-D2-S53, which carries the internal firm id.
- **Recursive deletions and discards of uncommitted files** (CLAUDE.md, Agent Autonomy: "Human confirmation ONLY for:
  recursive deletion, destructive git"): `C:\dev\wk-irpt-dashbd-503`; row 544d; row 65a1; row a392.

## Completion test

NOT DONE. The dell2-box scope is a keep-driving scope; it ends on Andrew's stand-down word.

state: ARMED
