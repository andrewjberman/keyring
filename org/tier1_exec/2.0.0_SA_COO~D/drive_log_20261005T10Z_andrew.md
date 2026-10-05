# Drive log -- 2.0.0_SA_COO~D, 2026-10-05 09:4xZ-15:2xZ (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 09:4xZ-10:1xZ | DSGN_IRPTV1 Y-6 runs 5-6 | live thread | Cproxy #1 REQ-e7af8e8a: 19.5 min, 20.8 s, 104 cards. Cproxy #2 REQ-01c90366: 18.7 min, 10.3 s. Both READY; no row miss with no builds running | DRIVE FORWARD |
| 10:1xZ-10:3xZ | DSGN_REBRND R4-3 part 3 batch 2 | FWD-13 | 72 white hover overlays onto the band rung (DEV 31510397) | LANDED, then FAILED its grade (below) |
| 10:4xZ-14:3xZ | DSGN_IRPTV1 Y-6 run 7 | live thread | Dproxy #1 took five attempts. 1: a local-proxy 500. 2: the stale case named the Y-5 tickers (fixed with the `'*'` wildcard). 3: a cold dev server after its restart (restarted on ~Y's advice, then warmed). 4: a 4.5-min resolve past the 4-min wait (waits now 8 min). 5: submitted REQ-6eaec4e9, which ended ATTENTION in the backend (YCharts session evicted twice, ~Y 105312). Every attempt disarmed with a refused login | DRIVE FORWARD; runs 8-10 HELD |
| 12:3xZ-14:5xZ | DSGN_REBRND row S22 (CVO ARMED) | FWD-13 | 3.0.0_SA_CVO graded batch 2 FAIL: inks not paired (Excel 9.13 -> 1.64; negatives 4.7 -> 3.3). Revert f1cdccd7 is byte-exact with autocrlf off. BUY/SELL fixed (cab2b039). The CVO's re-walk DISARMED it (105296); disarm row S23, CLOUD cb65948b69. The PROD hold lifts | RULED |
| 12:xZ-13:5xZ | shared index | hygiene | Two failed safe-commits (a scratch file swept by the temp cleanup; another seat's index.lock) left 2 paths staged, holding ~Y's merge. Unstaged, then committed as 1994a8ed20 | fixed (a defect of this seat's) |

## Open

- Y-6 runs 8-10 held until ~Y says the YCharts session is live.
- Batch 2's redo needs the stronger walk: every hover-styled element, every text descendant, modals open.
- tmp/yh-submit (2.0 GB of local HARs and shots): removal on MSTR's or Andrew's word, after Y-6.
