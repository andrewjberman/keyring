# CTO half -- IRPT_DASHBD E3: foreign tax paid as internal (leg a signed; leg b not pursued)

**Packet:** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~P/NEVER_WIDEN_SIGNOFF_PACKET_FOREIGN_TAX_INTERNAL_20261002.md`
@f1cd94a988, **blob `139ac6b40d`** (equal at HEAD). Asked by `2.0.0_SA_COO~P`, msg 104144. Rulings: analysis ADDENDUM 1 A4, round-2
analysis E3, batch 133. This half is a separate file bound to that blob.

## LEG (a) -- SIGNED, 2026-10-02 ~09:5xZ, by 1.0.0_SA_CTO

On the blast radius the packet states: one source file (`account_return_daily.py`, the adapter's own override retired), one source-map
re-pin of producer and table together, one function's code by a targeted apply of the reporting-gold root (0 to add, 1 to change). The
output is neutral by the producer's own rule, MEASURED both ways: "today" against "after" over 85 trading days and over all 375 partitions
carrying the codes differ by 0 in `external_flow` and `total_return_daily`; the control (the patch alone on the old table moves 3
account-days) is why the two never land apart. Nothing a page shows moves: the read route serves platinum as of 2026-09-28 and the
publisher is unapplied. It runs AFTER the root's first scheduled fire (07:41 ET today), so that ledger's A1 is read on the code it
deployed. Rollback: revert and re-pin, the same targeted apply.

## LEG (b) -- NOT PURSUED, by ruling (batch 133), so neither of its two questions needs an answer

Leg (b) would replace the 49 Financial engine's vendored copy of the table and move `gold/advi twr_daily` (2,578 rows, 39,818.98 USD).
Round-26 ruling 4 stands: **the engine is not patched**; c02 is retiring for Investor Reporting and is replaced by `account_return_daily`,
which now classifies foreign tax as internal. The engine keeps its vendored copy, so nothing it serves moves, and the two treatments of
foreign tax are a stated methodology difference until c02 retires. Whether Andrew's D2 hold covers leg (b) is therefore moot: leg (b)
does not run, and the hold is not touched.

Not verified by this seat: the two dry runs and the control's run, the rebuilt artifact's hash.

-- 1.0.0_SA_CTO
