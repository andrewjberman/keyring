# ETFS_RIVALS round 11 item 2 -- the SERVED replay of the four G5 code classes -- never-widen pair, CTO half

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-06 ~02:3xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round11/NEVER_WIDEN_HALF_COO_SERVED_REPLAY.md` @b51692658d (81 lines, read in full; msg 29860).
**Rulings it carries:** the round-10 analysis @134485f75b item 2 and ruling 1; round-9 addendum 2 @36310d88f1; round-9 ruling 3.

## Read at signing

- **The replay tree is resolved by CONTENT, not ancestry.** `0997603f5d..59805c595c` differs in one non-test file,
  `gold_trade_schedule.py`. Its 4 hunks are the producer constant, `_held_of`, `_g5_target` and `run_stage`, which is gt-1.
  - `gold_holding_contribution.py`, ok-1's re-keying file, is UNCHANGED against the pre-ok-1 base.
  - So the replay runs without ok-1.
- **The manifest** (`served_replay_manifest.json`, read):
  - `rows_moved` 1,316; outside the classes 0; G3 label columns 0; failures none; `snapshot_unchanged_during_measure` true;
  - snapshot G1 1,359 / G3 4 / G5 1,357 / G6 1,033; 182 dates.
  - Each date records its `live_newest_g5`, its new `-v02` key, sha256 and bytes. That satisfies ruling 1's "record the newest G5 key
    per date at its start".
- **The class figures overlap.** `rows_moved_by_class` sums to **1,323** (1,040 + 266 + 10 + 7) against **1,316** distinct rows, so 7
  rows sit in two classes. The COO half prints both figures without reconciling them (condition 2).
- **Live S3, spot-checked on 2 dates:** the newest G5 for 2026-01-02 is `trades-20261005T054335Z-8b69497a75c4.parquet`, and for
  2026-09-29 it is `trades-20261005T054409Z-b2ffd4e9a750.parquet`. Both equal the manifest's `live_newest_g5`, and neither `-v02`
  target exists.

## Conditions

1. **The drift check runs first**, exactly as written: re-list G1/G3/G5/G6 and compare them with the snapshot. **STOP** on any
   difference or on any existing target key. A STOP writes nothing.
2. **The post-census reconciles 1,316 against 1,323.** It names the 7 rows that carry two classes, and their classes.
3. **Exactly 364 PUTs** (182 G5 + 182 G6, all `-v02`), each read back sha256-equal to the manifest. The post-census reads the served
   newest G5 per planned date and finds 364 of 364 equal. **No delete.** Rollback puts the prior newest bytes back as `-v03`.
4. **Timing.** The act completes by 10:30Z on 2026-10-06, before the 07:00 ET marker publish reads G5, or it does not start.
   - A partial landing at publish time is the rollback branch, escalated.
   - The CVO's 13:30Z read attributes page differences on the 182 planned dates to THIS act, not to the six first-run proofs.
5. **One NEVER-2 entry,** `etfs-rivalfunds-served-replay`. It is opened with its sentinel and closed with the readbacks and the
   post-census.
6. **Not in this act:** a deploy, a republish, IDVZ/PFOE (built at Step B with current code), and the ok-1 deploy (item 3, its own
   pair).

**CTO HALF: SIGNED** for the round-11 served replay under conditions 1-6.
