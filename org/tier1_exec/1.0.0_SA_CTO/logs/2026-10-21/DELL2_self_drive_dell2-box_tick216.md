# Self-drive dell2-box, ticks 214-216 (1.0.0_SA_CTO~DELL2)

Arming record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261015_020xZ_SELF_DRIVE_DELL2_BOX_KEEP_DRIVING_ON.md
Window: 09:57Z to 10:57Z 2026-10-21.

## IRPT_ANLREQ
- **Run 7L PASS** (IB2 msg 11981; G2 msg 11979; Y2 msg 11985):
  - The door shows TICKER_NOT_FOUND with its message, and the Overview reached READY / ATTACHED.
  - The {portfolio_name} placeholder appears on 0 of 42 pages.
  - PDF at C:/dev/andrew_samples/Opal_Overview_sample_post_r34s.pdf, sha be9b2b7bc891.
  - S220 closed (S256).
- **RULED** (msg to G2, 10:00Z):
  - A kept row left out of the figures is named on the page, ticker and reason only.
  - Page 21's six "not a readable table" lines are fixed failing-first.
  - Both go in r34t.
- **C-SWAP model leg** is on the trunk (Y2, 3dac9960e2b) and ships in r34t. RULED:
  - run names: 7M is G2's ETF Multi-Comp, 7N is Y2's BREIT Overview;
  - IAM measured by simulate: the kimi secret read is allowed (re-read here); the etf-classifications GetItem is allowed;
  - vendor Moonshot kimi-k3 with no tools / no web search; below 0.80 sets low_confidence.
- **r34t contents (G2):** typed-ETF wiring (AR-g-189), per-model as-of (AR-g-190), the exclusion line, the page-21 fix, and C-SWAP. The packet is pending.

## Completion test
NOT DONE. TCKT_VNEXT is complete; IRPT_ANLREQ is in flight.

## Acts only Andrew can do (cited)
- 65a1, 544d, a392: recursive deletion / destructive git (CLAUDE.md Agent Autonomy).
- a331: internal all-firm entitlement for an outside-domain user (entitlement beyond his grants).
- 3ffe: admin-user delete of 4 synthetic cottonwood objects. The bucket fence is never edited.
- FWD-13..15 DONE WHEN confirmation (Andrew confirms DONE WHEN at L2).
- Andrew's read of the Overview and Multi-Comp samples against YCharts.

state: ARMED

## Compiler Tools
open-calls.py list; inbox read/; aws iam simulate-principal-policy; safe-commit.sh.
