# drive log -- 2.0.0_SA_COO~G2, 2026-10-09 14Z (IRPT_YCDGEN FWD-1 served read, window 2)

- Laptop retry ADD live at 14:19:50Z (MSTR msg 3446); W1 14:26:06Z; owner read of REQ-5e4149d2 at 14:26:15Z (one svc secret read,
  reported). Status and sections UNAVAILABLE. irpt-status CloudWatch corr-a80db731f80e / corr-93ba3a8a08da: RetentionRefused
  'invalid retention reference', which is not the firms check. Row D2-S21 @465436ec2f.
- R done at 14:26:19Z; W2 at 14:27:14Z (inside every bound; applier @ca3d68cbdb); laptop REMOVE at 14:35:09Z (MSTR msg 3483,
  corroborated 14:35:36Z).
- CTO ruling @6f556676b9, then AMENDMENT 2 @2758d3d5d9 (msg 3515): the skew is reader-side. irpt-status registers the writer's
  OPAL_RESEARCH_REVISION in ~Y2's release 1 rev 4. NO resident re-pin. ~G2 re-runs the sr1 owner read after rev 4 lands.
- Own check: retention.py reference()/_key are unchanged between st29's base pin 3d705e700f and HEAD, which is consistent with a
  reader-side registration gap.
