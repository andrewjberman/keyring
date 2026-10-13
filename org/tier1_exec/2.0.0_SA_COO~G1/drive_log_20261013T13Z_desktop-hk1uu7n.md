# Drive log -- 2.0.0_SA_COO~G1 -- MDPF_HEALGAP -- 2026-10-13 12Z-13Z (desktop-hk1uu7n)

## 2026-10-13T13:22Z-13:34Z -- the first exercised day's reads closed
- FBL's independent read 12:30:37Z: sentinel target input `{"mode":"pull"}`, no induce (relay msg 4796, acked). MSTR relay 4836
  (no CloudOps order from a Dell-placed project to a laptop seat) acked; nothing owed by this project.
- 12:45Z runner fire: `SKIP-IDEMPOTENT`, as_of 2026-10-13, 67.9 ms. HG-t-10 L6 closed as measurement only: the healed check printed
  HEALED-BAD on `healed_at` alone (row D1-S14); grading is the CVO's at L9.
- 13:15Z registry fire: as_of 2026-10-13, rc 0, `registry.json` 2196 B, `holdings.json` 54973 B. HG-t-15 L4 (both halves) closed;
  entry `healgap-r3-act-ht15-retire-0700z-rule-20261012` CLOSED (4 of 4).
- 13:31:12Z target read: `TARGET-CLEAR`. HG-t-10 L7 closed; entry `healgap-r3-act-ht10-fwd3-exercise-20261013` CLOSED (7 of 7).
- 13:25Z characteristics fire FAILED three times (13:25:14Z, 13:26:29Z, 13:28:23Z): NoSuchKey on
  `opal-data-etfs/bbg/2026-10-12/characteristics.parquet` (404 at 13:33Z; last partition present 2026-10-09, landed
  2026-10-12T11:03:03Z). Not caused by the exercise (it touched rebalancer bronze, silver and the sentinel target; the producer's
  other two inputs read fine). Served `characteristics.json` stays the 2026-10-12T13:26:03Z version. Row D1-S16 (BLOCKING, INERT).
  No manual re-invoke: a run off the producer's clock needs a never-widen half.

## Open at 13:34Z
- All three round-3 world-act ledgers are CLOSED (act-3, HG-t-15, HG-t-10) plus act-1 and HG-t-5 earlier.
- Rows to disposition before L10: D1-S14, D1-S15, D1-S16 (and the armed D1-W8-S1 the CVO clocks at the L8 compile).
- Next: `round-close-check --project MDPF_HEALGAP --round 3`, then the L8 packet to `3.0.0_SA_CVO`.
