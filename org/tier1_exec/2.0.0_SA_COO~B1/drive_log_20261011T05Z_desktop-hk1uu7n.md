# /canonical-drive log -- 2.0.0_SA_COO~B1 (dell1), ADVI_FIRMBKTS round 2 close, 2026-10-11 04Z-05Z

**archetype:** COORDINATE

Loop: none armed (`/canonical-drive ADVI_FIRMBKTS` as one tick; no live row in `org/ref/LIVE_ARMS.md` names this lane).
Session start: watcher armed (script pid 12692, re-armed at the 30-minute expiry), inbox empty, 8 of 8 delivery rows
READ or duplicate-READ (id 3452 OFFER-EXHAUSTED, same subject as READ 3453).

| UTC | limb | project/round | TOs t/T | cells c/F | thread | act fired |
|---|---|---|---|---|---|---|
| 04:4xZ-05:1xZ | close | ADVI_FIRMBKTS 2 | 7/7 | 7/7 | n (no FWD-1 thread trace this round) | DRIVE FORWARD: close-check REFUSED 7 of 7 PROOF-BAD (stem-only lookup); instances renamed to the order stem + 6 PENDING pins resolved (`e60140c2d2`, orders `6f71f434ac`, merged `baaa2bbc81`); `--deep` 7 of 7 MAY-CLOSE; the one real run of each outcome (`R2_CLOSE_RUN.txt`); packet `R2_CLOSE.md`; dep_stage ROUND_CLOSE (`e509956a7d`, `27bd0e5f9e`); packet to 3.0.0_SA_CVO, drain-end read to 1.0.0_SA_CTO~DELL1 |

## Measured

- Blind readers, canonical arm n=209: all four fields agree 195; table 197. Table repair 5 of 5 and 4 of 4 arms, 89
  FAULT left. F4 positive 3 of 3, negative 4 of 4. F7 COPY-COMPLETE 52,910 of 52,910, residue unchanged. F6 39 pass, 193
  of 193, controls 10 of 10. S11 naming gate PASS.
- Channel: 41 investigation rows, 23 open, 5 ARMED, 7 BLOCKING; one new row `D1-S10` (the two tools' disagreement).

## Defects in this tick's row, stated

- The issuer's order text named instances by order id while the close check reads the stem; the round carried it to the
  close. Repaired, not prevented: the template is unchanged (row `D1-S10`).
- Wrote the F6 line in the packet from the round-1 analysis (map-only gate) before reading `D1-S9`; corrected the same
  turn (the router's canonical list is empty).
- Committed the close files from the shared index rather than a worktree (rule 14b): four files in this project's own tree,
  no other seat's path. The rename and order amendments went through a worktree and `safe-merge.sh`.

## Left open

- `wk-firmbkts-4`, `wk-firmbkts-9`: landed and clean by `git status`; `git worktree remove` refuses (portal submodule
  initialized), `git submodule deinit portal` refuses ("local modifications") with the submodule's status empty. Not
  forced (worktree-wipe edict). Named in the packet.
- Push state: LOCAL on `box/dell1`; origin read `7735a642ea` at 05:1xZ.
- Waiting on: 3.0.0_SA_CVO L9 grade and L10 slug; the CTO's round-2 analysis, then round 3 in ONE issuance.

## Compiler Tools

| tool | result |
|---|---|
| `round-close-check.py` | structural REFUSED 7 of 7, then `--deep` MAY-CLOSE 7 of 7 after the rename; the lookup is stem-only |
| `proof-of-spec-check.py` | three instances INVALID on PENDING-THIS-COMMIT rows for committed files (CCX class); fixed by pinning |
| `comp-surprise --project --json` | 62 items, 23 open, 5 armed, 0 defects, 0 malformed |
| `comp-find` | rail denied three recursive greps (R1, R6); the comp-find forms answered each |
| `safe-commit.sh`, `safe-merge.sh` | gate refused the order amendment until the pins were real; merge fast lane, 14 of 14 paths carried |
| gap | `git worktree remove` vs `git submodule deinit` disagree on a clean submodule (see above) |
