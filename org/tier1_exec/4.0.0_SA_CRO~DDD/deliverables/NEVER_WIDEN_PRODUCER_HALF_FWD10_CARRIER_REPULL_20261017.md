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

## ADDENDUM A (2026-10-17 ~04:1xZ) -- MDPF 10/15 could not be restated; the 10/16 route, with a no-regress guard

**What happened.**
- Steps 1-4 landed and the carriers read valued. MDPF silver 10/15 supervised is 530,421,988.14 (BD to the cent). ADVI is
  live at 530,370,482.38, 864 accounts and 225 clients (header_metrics 03:38Z).
- The step-5 production gold run (manual, 03:37Z, green) wrote NO dated key. Every 10/15 dated key returned an A8 CONFLICT
  (conditional_put never overwrites a business-different dated key), so served MDPF is unchanged:
  Cottonwood 10/15 554,632,228.45 and Global 10/15 2,174,027,397.88.
- Andrew approved delete markers on Cottonwood's four 10/15 keys, but `s3:DeleteObject` is explicitly denied to
  `cloudops-dell1-agent-user` (policy cloudops-dell-agent-deploy-policy). Nothing was deleted; the prior versions are
  current. The publisher run (03:38Z) published 3 and left 15 unchanged; all 4 Cottonwood dated keys stayed.

**The 10/16 route (no restatement needed):**
1. Deploy `data/cot/scripts/bronze/cot_bronze_ingest.py` @de2e85035d to `s3://opal-data-cot/code/bronze/`. Prior bytes are
   equal to HEAD before the change. It adds the no-regress guard: a holdings pull with nzf below the landed sidecar's is
   rejected, and the landed snapshot stays.
2. Re-pull bronze holdings and allocations with RunDate=2026-10-17 (as-of 10/16), behind the same read gate: carriers valued.
3. opal-data-cot silver for holdings and allocations 2026-10-16, scoped (no account_attributes, no finalize). The MDPF
   mirror, plus `convert_bd` for the new 10/16 partition (a first conversion, no force needed).
4. The scheduled 07:30 ET pull of as-of 10/16 is then REJECTED by the guard if it is less valued. The MDPF mirror converter
   skips the existing partition. The 13:30Z fire writes NEW 10/16 dated keys with the carrier values: no conflict, no delete.

**Branches.**
- (a) 10/16 carriers are valued now: proceed as above.
- (b) 10/16 carriers are null now (BD has not posted): stop after step 2's read gate. Nothing lands, because the guard
  rejects equal-or-lower re-lands only when a landed snapshot is more valued, and none is. The 07:30 run proceeds as today.

**Rollback.** Re-upload the ingest's prior S3 version (from the safe-deploy record). Per-key bronze, silver and sidecar
rollback for 10/16 as for 10/15, with VersionIds recorded before the write.
