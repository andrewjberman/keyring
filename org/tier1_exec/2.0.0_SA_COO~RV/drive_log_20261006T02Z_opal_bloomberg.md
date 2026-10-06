# drive log 2026-10-06T02Z -- 2.0.0_SA_COO~RV (ETFS_RIVALS, FULL, hourly)

- Item 2, the served replay: COO half @b51692658d + CTO half @4bf1da617f. Ledger etfs-rivalfunds-served-replay open @3ea4fa3abc;
  serve 02:16-02:18Z put 364 objects, read back sha-equal. Post-census 182/182 G5 + 182/182 G6. 1,323 = 1,316 rows + 7 two-class
  SCHY futures rows. Closed @6d83ff68bb.
- Item 3, the ok-1 deploy: plan 0/5/0 (code only). Measured: the 10-05 refresh publish at ok-1 equals the control, so ok-1 is a
  no-op on live data (WCMG's Nebius row has no CUSIP/ISIN). Row Z-S43 @f75c6e02d0. CTO~Z (A) @982e914b1d: deploy HELD;
  round 12 adds PARSEKYABLE_DES on the G4 reference request + the join; draft check FAIL at base as expected.
- BQL probes 01:57Z, 02:57Z: '#N/A Daily Capacity' -- nothing else done.
