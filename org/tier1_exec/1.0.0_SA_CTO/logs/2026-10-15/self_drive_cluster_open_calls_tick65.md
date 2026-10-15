# self-drive cluster open calls -- tick 65 (2026-10-15 ~01:5xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 60m   cron: 6ca5a587   ticks covered: 65

## Measurements this tick

- Cluster list, read ~01:56Z: boxes=4, read=4, absent=none; open=18 (fork 0, act 17, approval 1), closed=199.
- Changes since tick 64:
  - CLOSED dell1 `a196`. It was superseded by `f411`, the Global AUA Trend with the Custom Models roll-forward, and by `c397`
    (its DEV resolution). Both closed on Andrew's word at dell1 ~01:xxZ: "trend looks good, custom roll-forward, then PROD"
    (`ANDREW_DIRECT_20261015_01xxZ_COO_D1_TREND_LOOKS_GOOD_CUSTOM_ROLLFORWARD_THEN_PROD.md`).
  - NEW dell2 `53cb` (act): a recursive delete of eight worker and issuer scratch directories outside the repo
    (`C:/dev/_scratch384`..`_scratch392`, `_scratchP2`; IRPT_BCKEND rounds 192-197). Some hold client-derived bundle extracts.
    Recursive deletion is Andrew's word.
- **The MDPF edge gate ledger:** still OPEN at L5, under the hold and the extension to 07:00Z
  (`RULING_20261015_012xZ_EDGE_GATE_HOLD_NO_ROLLBACK_WINDOW_EXTENDED.md` @916f09fb81).
- **Other changes this hour:**
  - COMM_ASSIST CA-k-4 CTO half SIGNED @2c942a35b1, with the apply after the spend-limit reset.
  - The inf-gold-freshness-guard 2027 closures are owned by ADVI_FIRMBKTS, due before 2026-12-31.
  - Laptop disk: ctlpln-97 removed (+3.7G).

## Calls this tick

- None for this seat. `53cb` is Andrew's (recursive delete); REC yes, because the scratch holds client-derived extracts that
  gate nothing.

## Acts only Andrew can do

- Laptop: `3717` (spend limit); `7841`; `8f2b`, `44eb`, `e435`; G4; the DSGN_RBNDV2 endpoint.
- dell2: approval `2402`; `53cb` (new); `f61b`, `a252`, `2106`, `e260`.
- Site Z: `21d9`, `def4`/`3b41`, `a519`, `21c5`/`8ed7`/`f0d2`.
