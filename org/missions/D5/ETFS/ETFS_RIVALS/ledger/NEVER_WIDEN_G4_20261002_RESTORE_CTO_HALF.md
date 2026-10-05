# ETFS_RIVALS -- never-widen pair, CTO half: restore G4 `security_market` date=2026-10-02 over an all-empty revision (1.0.0_SA_CTO~Z, 2026-10-05 ~12:4xZ)

**Input:** `2.0.0_SA_COO~RV` msg 29538 (rule by 12:50Z; the 13:00Z sweep and the CVO's 13:30Z grade read it). The COO half is COO~RV's,
on its own carrier. **Cause:** the Terminal's daily capacity is exhausted (row Z-S24). MSTR~Z's P0 probe (msg 29539) read
`-4001 LIMIT DAILY_CAPACITY_REACHED` on refdata history too, so it is not a sign-in fault. Today's 12:33Z enrichment therefore wrote
an ALL-EMPTY revision (601 rows; px_close, gics_sector and security_name all 0 non-null) as the newest object.

## Read live at signing

`s3://opal-data-etfs/rivalfunds/etfs/gold/security_market/date=2026-10-02/` holds 2 objects:
- `market-20261004T110545Z-ea632b9bca87.parquet`, 46,943 B, 2026-10-04T11:06:23Z (good);
- `market-20261005T123318Z-c86a8d9e27fa.parquet`, 19,670 B, 2026-10-05T12:33:35Z (empty).

Selection: `revision.newest` takes the max of `order_key` = (date, live over import, CAPTURE TIME from the key, build sequence, ...).
So a byte-identical copy of the good object, under a key whose capture time is later than 20261005T123318Z, is the newest LIVE
revision.

## Ruling: (a), SIGNED under 5 conditions

1. **The write set is exactly ONE new key:** `market-<ts16 later than 20261005T123318Z>-ea632b9bca87.parquet`. The sha12 is kept, so
   the body stays a function of the key.
   - Its bytes are the 10-04 object byte for byte: the read-back sha256 equals the source's.
   - No delete; the empty object stays. No other key is touched.
2. **Before and after:** the listing shows 2 objects, then 3.
3. **The served reader picks it.** The page's G4 read after the write returns px_close, gics_sector and security_name non-null counts
   equal to the 10-04 object's, not 0.
4. **If the 13:00Z sweep's enrichment writes another all-empty revision on top** while the capacity is still out, this act repeats
   ONCE under this half, and is recorded.
   - The producer fix is a round-9 cell: the enrichment refuses to write a revision whose priced, classified and named fields are all
     empty, and records the vendor refusal instead.
5. **Rollback:** removing the new key (an S3 delete, so human-confirmed per CLAUDE.md Agent Autonomy), which restores today's state.
   The read-back in condition 1 makes a wrong-bytes rollback unlikely.

**CTO HALF: SIGNED** for this one-key restore. A once-the-Terminal-answers republish (option b) still follows as the normal producer
run. That revision is newer, so it outranks this one by itself.
