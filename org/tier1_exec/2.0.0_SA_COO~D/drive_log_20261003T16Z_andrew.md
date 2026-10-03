# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 16Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 16:0xZ-16:1xZ | IRPT_DASHBD B1 (the P-2 window, CTO 104632, Andrew "1 yes today"; 0.0.0_AB_MSTR 104636) | B1: P-3 + P-6 on DEV when ~P calls it | B1 staged: origin/DEV 525c9404 merged into `coo-d-p3-client-summary`, then 426761e4 (iv-e-162 read-only cast); ~P told 161323Z | DRIVE FORWARD |
| 16:1xZ-16:3xZ | DSGN_REBRND (FAST; product changes held off DEV until B2) | the CVO's census after S14 (b296ae47c1) | the regime's `?? 50` sites fixed on the held branch `coo-d-regime-readings` @3a842221 | DRIVE FORWARD |

## B1 staged

- Download was already on DEV (item 93), so B1 is P-3 and P-6 from the held branch.
- The branch tip had failed `bun run typecheck` since b847c9f0: iv-e-162 wrote a readonly wire field. Fixed in the
  test (426761e4); no production file changed. That miss was this seat's, at the b847c9f0 pin.
- Measured: typecheck rc=0. The branch's five tests pass 9 of 9.
- Full suite: DEV head 905 pass / 63 fail / 18 errors; the branch 910 / 63 / 18. The same 57 named tests fail in
  both. Both runs used worktrees outside the workspace, which adds path failures (`Desktop\docs\...` ENOENT) to both.
- The landing path is `git push origin HEAD:DEV` from the branch worktree. The gate reads the refspec and admits it
  under this seat's FAST lease. The main portal tree carries another writer's uncommitted wire edits, and a
  fast-forward there would collide with them.
- After B1 lands, 0.0.0_AB_MSTR gets the DEV head sha.

## Regime readings (held)

- MarketRegimeIndicator, MarketRegimeModal, FearGreedModal: a missing reading reads "Not published" in neutral ink,
  with no marker, never 50.
- Pin regime-no-reading. Four negative controls:
  - the modal at DEV;
  - the indicator's signals starting at 50;
  - a single reading ranked as 50;
  - the indicator at DEV, failing only on the missing markers.
- Real run: a build served with fixtures, looked at; "Not published" measures 6.95:1 on the band. The served regime
  JSON answers 401 without sign-in.
- HELD until B2 is measured: the promote carries DEV head, and this change is not graded yet.

## Open

- B1 lands on ~P's call; B2 is 0.0.0_AB_MSTR's.
- From the CVO's grade b296ae47c1: tests for the untested wiring (MarketPerformance `failed`, Positioning
  `loadFailed`, HoldingsTab). These are tests only, so they could land before B2, but they wait to keep B2's delta
  small.
