# 2.0.0_SA_COO~H drive log -- 2026-09-30 12:3xZ-14:0xZ (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron bf9d159b). Lease: FULL. Round 29, L6/L7.

## The round-28 analysis and the round-29 issuance

- **~12:36Z -- the analysis arrived:** `ROUND_ANALYSIS.round28.md` @`c907537920` (msg 27139, acked). Round 29 is 3 cells.
- **~12:5xZ -- ONE issuance** @`201bc76e9b`, decomp section 41:
  - `ab-1`: live wsj reach from `timestamp`, the `p-2` test re-pointed, the hold seed;
  - `ab-2`: the mention rebuild, under a pair;
  - `ab-3`: backfill batch 1, 10 names x {bbg, wsj}, under a pair.
- **Issuer ruling on `Z-W76-S1`:** a wsj backfill now bound-stops at the floor (a paging change, stated in the order).

## ab-1 and ab-2

- **`ab-1` dispatched** to `~81` in `wk-hvst-r29-81`.
- **`ab-2` signing (~13:2xZ):** the serializing dry run is 1 put, 379 rows, 44,376 bytes, reproduced. KEPT 358, NEW 21 (all on
  the 11 story ids), GONE 0. The predecessor diff since `062354Z` is `91b74a9047` only, which touches the daily builder.
- **Found at signing (row `Z-S46`, ARMED against `ab-3`):**
  - 9 of the 11 story ids' Lenovo pairs are 2015-2019. bbg search is relevance-ordered, and a backfill fetches dated
    pre-floor hits.
  - `ab-1` AMENDMENT 1 stops those fetches.
  - `ab-2`'s AC2 is scoped to the page floor.
  - Committed @`9548acfffb`. The CTO signed @`8522f36154`.
- **`ab-1` phase A reported:** AC1 17 passed, AC2 `NETWORK CALLS MADE: 0`, AC3 271 passed (253 at base, 0 regressed). The seed
  row is `held` for 2026-09-30.
  - Rows `Z-W81-S1` and `S2` are ruled inside `Z-W76-S1`.
  - Resuming the worker failed ("No transcript found"), so a fresh `~81` instance carries AMENDMENT 1.
- **`ab-2` act (~13:46Z):** `part-20260930T134616Z`, 379 rows, 44,376 bytes. Drained @`a9c5fc9ea8`. On the trunk AC1 and AC2
  PASS; the day route lists 2 of 2 in-window pairs. Complete @`df1fa5d0aa`.

## Andrew-direct via the CTO (msg 27155, ~13:03Z)

The word: a stored token first, a 429 is not expiry, backoff; barrons and ft move into scope; re-arm the schedule after batch 1;
remove `wk-hvst-r24..r28` with branches kept.

- **The addendum:** three NEW order files were REFUSED by `to-pipeline-gate` (ONE ISSUER PER ROUND). Re-cut @`094fcb2a4a`
  (decomp section 42):
  - `ab-1` AMENDMENT 2 carries `C-HV-TRUST-TOKEN`;
  - `ab-3` AMENDMENT 1 adds the Lenovo barrons and ft jobs and phase B (the schedule).
- **Worktree removal, authorized** by Andrew's "recs approved for all", card 2:
  - census: 26 worktrees, all merged into CLOUD, 0 tracked-dirty; untracked `.scratch/` only (commit-message scratch);
  - removal is running (12 left at 14:02Z); branches are kept.

## Slips

- A peer's `index.lock` and a peer merge refused two of my commits. Both were retried clean; nothing was lost.
