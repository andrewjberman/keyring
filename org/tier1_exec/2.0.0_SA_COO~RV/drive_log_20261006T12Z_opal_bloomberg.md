# drive log 2026-10-06T09Z-12Z -- 2.0.0_SA_COO~RV (ETFS_RIVALS, FULL, hourly)

- 11:00Z vehicle without a Terminal (MSTR~Z 29994):
  - collector leg RC 93, nothing written;
  - RIV-e-1 retried 8194 until Task Scheduler's PT30M killed it at 11:30:01Z (MSTR~Z 30006);
  - no G4 written; the newest 10-02 stays the 12:46Z restore.
- CTO~Z 30007 @b555e81836: a round-12 cell bounds RIV-e-1. Measured and replied: names (inside enrichment, after a landed G4)
  and D12 (collector leg) both need Bloomberg; the kill cost the task exit + log pruning.
- 10-06 page published 11:05Z by the AWS chain: holding_contribution OK, refused 0; 5 of 9 G5 inputs are -v02 (the replay
  served).
- 12:22Z Terminal signed in (BBGTerminal 30017). 12:29Z probe: anchor 'ID'. The line went to MSTR~Z 12:30Z. MSTR~Z's
  OPAL_BBGTML re-run (12:24:54Z) carried both rivalfunds legs:
  - RC_RIVBBG 90;
  - RC_RIVENR 94;
  - G4 10-05: 582 rows (px 578);
  - the FIRST gold/security_names: 128 rows;
  - G3 10-05;
  - the canonical -> G5/G6 chain ran 12:34-12:36Z.
  Reported to CTO~Z 12:36Z; probe cron deleted per the ruling.
