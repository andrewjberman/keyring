# Drive log -- 2.0.0_SA_COO~G1 -- MDPF_HEALGAP -- 2026-10-12 14Z-22Z (desktop-hk1uu7n)

Substantive ticks only; empty event-gated ticks (15:22Z-20:22Z) are in the runtime log.

## 2026-10-12T21:22Z -- STAGE
- Read SSM document `opal-bd-asset-dim-download`: the 22:40Z skip branch uploads to the same S3 key as the full run
  (`logs/asset-dim-download-<D>.log`), so the skip run replaces the 22:10Z log object unless the bucket is versioned.
- Wrote a gather script (scratchpad) that waits for the key's LastModified >= 22:40Z, then prints object versions, the
  log head, the trigger lambda log, rules on the trigger, instance state.

## 2026-10-12T22:22Z-22:46Z -- act-3 L4 READ and CLOSED
- 22:10Z fire: instance started 22:10:19Z, SSM sent 22:11:06Z; log version zEXhldgd.. (22:12:20Z, 208105 B): REST pull exit 0,
  bronze `assets_dim_rest/2026-10-12` 12218 rows, silver `bd_assets_dim.parquet` 12231 rows, AC1-AC3 PASS, dim rebuild exit 0.
- 22:40Z fire: first SendCommand InvalidInstanceId at 22:41:31Z (boot race), lambda async retry 22:42:32Z sent SSM;
  log version R76R0E9m.. (22:42:46Z, 2595 B): `EXISTS` bronze 2026-10-12, `SKIP-COMPLETE`; no re-download.
- Instance running 22:43:21Z, stopped (User initiated) 22:46:11Z. Bucket versioning kept both log versions.
- Ledger `healgap-r3-act3-asset-dim-reattempt-20261011`: L4 closed with the proof above; entry CLOSED (4 of 4 legs).
- Residual named: the 22:40Z first attempt depends on the async retry because the 30 s boot wait is shorter than SSM
  agent registration; the skip fire costs one extra instance start. Not changed (outside the never-widen halves).

## Open at 22:46Z
- HG-t-15 ledger L4: 2026-10-13 07:22Z tick (zero invocations of the retired 07:00Z rule).
- HG-t-10 FWD-3 exercise ledger L2-L7: 2026-10-13 10:22Z tick (induce on the sentinel target only if FBL's ack is on
  record and the target reads CLEAR).
- Round-3 L8 packet to `3.0.0_SA_CVO` after the world reads; `round-close-check` before counting the round closed.
