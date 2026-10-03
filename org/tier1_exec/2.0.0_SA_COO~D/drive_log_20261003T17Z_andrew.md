# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 17Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 17:0xZ-17:2xZ | DSGN_REBRND (FAST, held) | row W3-S5, /factor-tilts | one state for a failed or empty load, held branch `coo-d-regime-readings` @cc1d7cc6 | DRIVE FORWARD |
| 17:3xZ-17:5xZ | DSGN_IRPTV1 (FAST re-armed to 19:48Z on Andrew's presence) | Andrew-direct: two Holdings changes before the push | change 1, the /portfolios canon for Models / SMAs / Client, LANDED portal `e862b0c4` (push output 525c9404..e862b0c4) | DRIVE FORWARD |
| 17:5xZ-18:0xZ | IRPT_BCKEND Y-5 (~Y 104651) | the Aproxy case | added to yh-submit-case.mjs and run on fixtures; the live run held | DRIVE FORWARD |

## Andrew-direct, change 1

- Words (~17:3xZ, with screenshots of /portfolios and the Holdings tab): "the portfolios page is the canonical design
  and color which we should adhere to for the investor-reporting holdings view as it pertains to top level asset
  taxonomy (models/smas/client)".
- Cause: the Holdings card keyed its SMA peer by the display word `SMAs`; the shared CategoryViewTree keys by `SMA`.
  SMAs therefore missed its colour, mark, order and line.
- The fix keys the card's peers canonically (DrillTree.tsx only). Pin holdings-l0-canon; the DEV file fails it exactly
  as the screenshot showed (Models, Client, SMAs; #60a5fa; shapes; no line). iv-e-92 re-keyed.
- Suites (IR, components, ModelPortfolios): every one of the 49 failing names also fails at DEV head.
- The lease had lapsed to FULL at 17:4xZ. It was re-armed at the same surface as the last ARM line, because Andrew is
  present and directing.
- Live walk `20261003T175211Z` (local, not committed). The UI-walker ARM and DISARMED were sent to 0.0.0_AB_MSTR. The
  client's accounts are Models-only, so the live card shows the lilac Models tile; no served account in the walk
  carried SMAs or Client.
- Left as is, and said to Andrew: exact amounts (the tab's `exactAmounts`) against /portfolios' abbreviations.
- Change 2: awaiting Andrew's words. B2 waits: 0.0.0_AB_MSTR gets the DEV head only after change 2 and B1 are on DEV.

## Other

- 0.0.0_AB_MSTR 104664 (Andrew-direct ~17:3xZ, release any quarantine): this seat holds none; acked, no reply owed.
- UI-walker: site Z held it at 17:09Z, released it at 17:23Z, and holds it again from 17:58Z (104669).
- ~Y's Aproxy live run is held for two reasons: the walker is held, and Andrew's "further data collection after
  review". ~Y was asked to re-confirm (18:00Z).
- ~P's window is at leg A7 (d67450e8c2); B1 lands on its call.
