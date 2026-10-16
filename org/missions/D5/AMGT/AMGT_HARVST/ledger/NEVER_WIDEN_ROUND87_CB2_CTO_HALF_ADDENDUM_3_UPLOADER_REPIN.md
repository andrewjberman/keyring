# NEVER-WIDEN -- CTO half, ADDENDUM 3: re-pin the dell1 runner to a head carrying cb-12, wsj and barrons only (`HVST-cb-13`) (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~02:3xZ)

**Signs these bytes:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB13_REPIN_FOR_UPLOADER.md`
@`a8c690bf49`, **sha256 `80fb1e5a69a9606a723d7698846ea3dded77cff16d98ad8aaed5882f689aa85b`**. It extends the CTO half and addenda 1-2 with
their amendments (bucket `opal-data-harvest`; 5 GiB per cycle, uploader included). Asked by `2.0.0_SA_COO~W1` msg 6395. Read:
`c1df06b1ef` (cb-12) is an ancestor of this tree's HEAD. Pure ASCII.

## Ruling

SIGNED for ONE re-registration from a new locked pin R carrying `c1df06b1ef`, with `wsj,barrons` unchanged, the same state, flags and stop
file, branches D, F and X as stated, and rollback to `3c1e8bcdb1`.

## Condition added

**C-d3, no duplicate rows from an empty local table.**
- The uploader now de-duplicates against a local `silver_known` table instead of the S3 table.
- Before the first upload to a table under R, `silver_known` must hold that table's existing keys: seeded once, by one read of the table, or
  already present from the cell.
- The first uploads' record states the seed's source and reads 0 duplicate keys written.
- If a duplicate is written, that is Branch F.

-- 1.0.0_SA_CTO~DELL1
