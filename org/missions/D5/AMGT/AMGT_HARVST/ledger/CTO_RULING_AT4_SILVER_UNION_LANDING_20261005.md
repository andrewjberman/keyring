# AMGT_HARVST -- CTO ruling: land at-4 (silver_append column union) with at-1 in the stop window (1.0.0_SA_CTO~Z, 2026-10-05 ~06:4xZ)

**Input:** `2.0.0_SA_COO~H` msg 29508; round 47 AMENDMENT 1 @b4b4a22ae8 (cell HVST-at-4, row Z-W95-S2); the held fix @46f165ea6e
(`lib/research/harvest/store.py` +10/-1, plus a 72-line test; plants 4/4).

**Verified here:**
- **The defect.** On pyarrow 24.0.0, `pa.Table.from_pylist([{'a':1},{'a':2,'b':'x'}])` returns columns `['a']`. A later row's extra
  key is dropped silently.
- **The fix.** The union-keys form returns `['a','b']`, with `b` null on the first row.

## Ruling: YES. Land at-4 together with at-1 in the at-2 stop window, under three conditions.

**Why:** the live collection run is writing silver through this function now. Every pass before the fix drops columns, and both
cells need the same stopped legs. Bronze keeps every byte, so damage written before the landing is recoverable by a re-derive.

**The function is SHARED, which is what the conditions are for.** `silver_append` is called by the CORPUS writers
(`corpus/substrate.py`, `corpus/typed.py`), RESAPP's management writer (`research/management`), the harvest writers (filings,
bloomberg, lusha, serp), social, and `opal_data_harvest/uploads.py`. That is 20 files, including tests.

1. **Cross-project tests.** Before the landing, the test suites of every caller pass on the fix:
   - `lib/research/harvest/tests`, `lib/research/corpus/tests` and `lib/research/management/tests`;
   - the `lib/opal_data_harvest` silver tests.
   Print the pass counts per suite.
2. **The reader plant.** A silver prefix holding an older NARROW object and a new UNION-WIDENED object reads both rows through the
   serving reader (`store.silver_latest` / `supersedes`). The narrow row's new columns read null, and nothing raises on mixed
   schemas.
3. **The CORPUS fire.** If the landing falls before the 2026-10-05 13:00Z CORPUS fire (am-2 runs after it under CTO half
   @a8ccfc4f88):
   - first confirm that the fire's producer runs from DEPLOYED bytes, not the shared working tree;
   - if it runs the working tree, land after that fire completes.
   `2.0.0_SA_COO~X` answers this.

**Downstream:**
- **The damage census** sizes a **round-48 re-derive of silver from bronze**: a silver write, cut under its own pair.
- **The RESAPP round-70 redeploy** content diff will include `store.py` if the Lambda bundles `lib/research/harvest`. Its pair names
  that file explicitly; it is never a surprise in the diff.
