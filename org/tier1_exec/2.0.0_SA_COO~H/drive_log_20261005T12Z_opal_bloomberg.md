# drive log -- 2.0.0_SA_COO~H -- 2026-10-05 T05Z-T12Z (opal_bloomberg)

Loop `/canonical-drive AMGT_HARVST 30m`; lease FULL. Andrew-direct @b023b75324: no ft until he returns; the rest proceed.

**Closed decisions this window**
- **Round 46:** drained @e51fb4ddac on CTO @7cd62976f1 (Z-S86: run on; batched upload in round 47; separate barrons root refused).
- **Round 47:** issued @c9b2e03ed2 (section 60).
  - at-1, the batched listing upload: worker ~95; prefix reads 100 -> 1; 84 s -> 0.9 s; rows identical.
  - Amendment 1 @b4b4a22ae8 cuts at-4: the `silver_append` column union. Row Z-W95-S2: pyarrow from_pylist takes columns from the
    first row, confirmed.
  - The damage census reads 0 of 2,373 served article rows since round 45.
- **The landing:** at-1 + at-4 LANDED @23baacf0e1 on CTO @08580b1fd6 + ADDENDUM @ff4e31bcd0.
  - Suites: harvest 342, management 142, collector 655, corpus 475 + 1 pre-existing failure identical on CLOUD.
  - bbg and wsj stopped by stop files and resumed 07:25:46Z from their own checkpoints.
  - sa's driver exited on an unhandled upload TimeoutExpired (row Z-S87) and was resumed 07:57:37Z. Its 92 stranded objects
    uploaded in ONE batched pass.
- **bbg:** stopped on bot_check (403, BBY) 08:4xZ. CTO AMENDMENT 1 @441a9f05a6 allows ONE --clear-stop after the cooldown, issued
  08:49:45Z. No challenge since.

| leg (12:35Z) | concluded of 191 |
|---|---|
| sa | 6 |
| barrons | 0 (queued behind sa) |
| ft | 0 (held, Andrew-direct) |
| bbg | 28 |
| wsj | 60 |

DECLARED SET: EMPTY. at-3 (the per-leg report) is due at the round-47 drain.
