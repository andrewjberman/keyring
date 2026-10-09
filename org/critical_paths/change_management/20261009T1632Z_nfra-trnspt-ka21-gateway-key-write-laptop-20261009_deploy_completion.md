# Deploy Completion Record
**Date opened:** 2026-10-09T16:32:57.435334+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT ka21 gateway key-write statement at pin 95a62b9f29fdff643344667b82e5364203e3c002 carrying b74b1e45bd (pair COO 6791d6ebc2 + CTO ad98587dfa)
**Authored by:** 0.7.0_AE_CloudOps~TRL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| PRECHECK | verify | the opal-gateway runtime role's S3 write reach into opal-data-transcripts | every policy attached to the role enumerated (managed + inline) with the statement denominator printed; each S3 write statement and the probe ARNs it matches; the verdict reached by SUBTRACTION, with a planted-statement control proving the matcher fires on a wildcard |  | OPEN |
| APPLY | activation | aws_kms_key.transcripts | safe-apply from a saved plan showing ONE in-place key-policy update whose ONLY difference is the added GatewayWritesTranscripts statement; the five live statements byte-identical; full key diff printed in this entry |  | OPEN |
| AFTER | verify | the live transcripts key policy | six Sids read back, GatewayWritesTranscripts carrying both conditions (kms:ViaService s3.us-east-1 and kms:EncryptionContext:aws:s3:arn = the bucket), no kms:Decrypt granted; AC1's invocation run as the order states it |  | OPEN |

## Log

- 20261009T163257Z OPENED by 0.7.0_AE_CloudOps~TRL with 3 leg(s)
