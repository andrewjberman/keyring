# Never-widen PRODUCER half, 4.0.0_SA_CRO~DDD -- FWD-10 (b): Cottonwood carrier-value re-pull for as-of 2026-10-15

**Author:** 4.0.0_SA_CRO~DDD, 2026-10-17 ~03:2xZ. **For:** 1.0.0_SA_CTO~DELL1 (msg 7198 item 1).
**Authority:** Andrew-direct `ANDREW_DIRECT_20261017_024xZ_COTTONWOOD_CARRIER_REPULL_RUN_NOW.md` @c37856fec5 ("do the run now").
**Why:** findings ADDENDUM 2. The ~96 carrier-feed accounts are $0 in the 07:30 ET pull; a later pull carries their
values. The target is the BD Dashboard Supervised for 10/15, 530,421,988.14.

## The act, in order (each step is read before the next)

1. Start EC2 `cot-exporter` i-0643a5bee8a8feabf and probe the BD session (trigger Lambda `mode=session-check`).
2. SSM `opal-cot-bronze-run`, RunDate=2026-10-16, Table=holdings, then Table=allocations. With the 1-bday snapshot lag the
   as-of is 2026-10-15. A single-table run emits no `_BRONZE_COMPLETE` sentinel, so nothing chains on its own.
   - **READ GATE:** the new HOLDINGS_DAILY_2026-10-15 must carry non-null carrier values. All-assets total ~563.56M,
     supervised ~530.42M. If not, STOP: nothing further runs, and step 2's re-land is rolled back per key.
3. SSM `opal-cot-silver-run` for the matching date. It rewrites opal-data-cot `silver/{holdings,allocations,...}` for that
   date; its sentinel fires `cot-silver-complete`, which runs the ADVI gold chain. That chain includes B_00 with
   `--force-recent-days 14`, and C_03 with the supervised switch.
4. The MDPF mirror (opal-data-assets `blackdiamond/cottonwood/{bronze,silver}`) re-converts on the replicated bronze. If
   the event path does not re-convert, I report it and do not hand-write silver.
5. One production `mdpf-gold-lambda` run plus one publisher run.

## Keys and rollback (prior VersionIds measured 03:1xZ)

| Bucket / key | Prior VersionId |
|---|---|
| opal-data-cot forwardfill_v2/holdings/HOLDINGS_DAILY_2026-10-15.xlsx | fftnj3maKK8wbVi47nEBtYd9HIsrI8P9 |
| opal-data-cot forwardfill_v2/holdings/_complete/2026-10-15.json | qgiDC3BVLgn6cGukyxZYzPY9rNp0JlFH |
| opal-data-cot forwardfill_v2/allocations/ALLOCATIONS_DAILY_2026-10-15.xlsx | cDyVNoeOCUwAyrimau5WiXktrWkGgU_F |
| opal-data-cot silver/holdings/2026-10-15.parquet | vLppgDV8kki3yYaGIOZGvY_ofQbB5ikV |
| opal-data-cot silver/allocations/2026-10-15.parquet | usJpFmlKPKD1JZlAuduHcgKk8VnzeRpD |
| opal-data-cot gold/canonical/holdings/2026-10-15.parquet | CbBOjJTYjUNiop9YX0DDEevAapEx98S2 |
| opal-data-assets blackdiamond/cottonwood/bronze/holdings/HOLDINGS_DAILY_2026-10-15.xlsx | CYLrjkXdnOiitWjF5LcqmxG_YUdQA5ZM |
| opal-data-assets blackdiamond/cottonwood/bronze/allocations/ALLOCATIONS_DAILY_2026-10-15.xlsx | 15I351UAlxNHVcOQCj6Eo6qsGm9w7Wlw |
| opal-data-assets blackdiamond/cottonwood/silver/fact_holdings/date=2026-10-15/data.parquet | DW19611OZNH1Uc5G46TxGPCn5.RRRR4g |
| opal-data-assets blackdiamond/cottonwood/silver/fact_allocations/date=2026-10-15/data.parquet | AsAh9yg2LmPtfPx9qfeURMrrA6E5HPG2 |

**Rollback per key:** copy-object the prior VersionId onto the same key. Then re-run the ADVI gold chain and one MDPF gold
plus publisher run, which return to the 07:30-pull values. Every key above is versioned (each head returned a VersionId).

## Both branches

- **(a) The carriers come back valued.** Holdings and allocations for 10/15 gain the carrier values, about +8.86M
  supervised. Cottonwood served: MDPF ~530.42M (supervised, as-of 10/15); ADVI the same less the ~$51K canonical-collapse
  delta. Account counts do not change in holdings; allocations gains the carrier rows. 7 of them overlap COO~C1's 122
  multi-book accounts; C1 ruled that A_00 takes no portfolio_group from allocations.
- **(b) The carriers come back null again.** The READ GATE stops the run after step 2. The step-2 re-land holds the same
  content as before (nulls), so served figures do not move. The re-land is still rolled back to the prior VersionIds for
  hygiene.

## Not touched (COO~C1 condition 3)

No account_attributes partition and no A_00 code. COO~C1 gets each bronze, silver and gold run time, and took its
pre-write snapshot (msg 7200).

## Producer half: SIGNED by 4.0.0_SA_CRO~DDD. Awaiting the CTO half.
