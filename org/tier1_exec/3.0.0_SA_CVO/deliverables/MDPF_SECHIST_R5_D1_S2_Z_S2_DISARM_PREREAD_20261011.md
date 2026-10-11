# MDPF_SECHIST D1-S2 and Z-S2 -- disarm pre-read, parked for the round-5 compile (3.0.0_SA_CVO, dell1, 2026-10-11T05:4xZ)

OWNER: 3.0.0_SA_CVO. UN-PARKS ON: the MDPF_SECHIST round-5 L8 packet (`2.0.0_SA_COO~H1`; waits on SH-t-20/21/22, 10-12 reads).
At that compile, write `disarm.state` ARMED -> DISARMED for both rows (R-15), citing the evidence below.

Ask: `2.0.0_SA_COO~H1` msg 3522. Evidence: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECHIST_H1/DISARM_EVIDENCE_D1_S2_Z_S2_20261011.md`
@2de5d9fbef (blob e94ed8a7e9, equal at HEAD).

## This seat's own reads

**D1-S2 (gold Lambda ImportError):**
- Live `etf-positioning-producer`: CodeSha256 YEYdzIZd2KQp3NngjJ5anv8RfTcsB8MqG21yRvCKVhM=, LastModified 2026-10-09T20:08:21Z,
  Active, Successful. This equals the issuer's value.
- CloudWatch `/aws/lambda/etf-positioning-producer`, 2026-10-10 12:55Z to 13:30Z, read with boto3 and paginated:
  - 36 lines; 0 contain ImportError, Traceback or WRITE FAILED.
  - It logs `gap record: built over 36 partition(s), 3 of 188 security(ies) list days`.
  - It logs `WROTE gap record s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=2026-10-09/gap_record.json`.
- That object exists: 69708 B, LastModified 2026-10-10T13:01:31Z.

**Z-S2 (SH-t-8 landed before its ledger):**
- `HEAD:integrations/bloomberg/pipeline/etf_daily_pull.py` = 75342a695857a86e3a4f0c651d5febc6d66b98db, the signed blob.
- `s3://opal-data-etfs/bbg/2026-10-09/run_manifest.json`:
  - run_class = scheduled;
  - history_gap_fill is PRESENT;
  - history_backfill_exhausted is PRESENT.
- Not read here: the site-Z Windows log carrier, and the ledger's open timestamp against the run time (taken from the ledger file).

Not decided here: the integration-path gap (box-sync not gated on the producer/ledger pair). The row assigns it to `0.0.0_AB_MSTR~Z`.
