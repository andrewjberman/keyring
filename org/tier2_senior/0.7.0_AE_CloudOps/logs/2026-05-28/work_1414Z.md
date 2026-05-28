# /work work-cycle:0003 — opal-data-imo SSE disposition (2026-05-28 ~1414Z)

**Agent:** 0.7.0_AE_CloudOps~A
**Tick class:** SENIOR_DISPATCH disposition (substantive; decision artifact, no apply)
**Trigger:** COO /drive 1416Z [AWARENESS] — DS~C found opal-data-imo bucket-default = AES256, not SSE-KMS as PRD v0.5 §3.1 reads.

## Verified state
- Live: `aws s3api get-bucket-encryption opal-data-imo` = AES256, BucketKeyEnabled=false, no bucket policy.
- TF: s3.tf:29-33 `aws_s3_bucket_server_side_encryption_configuration.imo_data` sse_algorithm=AES256. Matches live.

## Disposition = (b)
Per-object KMS-on-write is CORRECT and the ONLY mechanism for the PRD per-prefix split.

**Key finding (reusable):** S3 bucket-default-encryption (PutBucketEncryption) is **bucket-WIDE — there is no per-prefix default.** You cannot set "KMS for silver/linkedin-scrape/*, AES256 for web-scrape/*" as a bucket default. PRD §3.1's "amend bucket SSE → aws:kms for the KMS-scope prefixes" is therefore not implementable as a bucket-default; the AES256 default is CORRECT for the non-PII majority. Per-prefix PII-KMS is achievable only via per-object SSE-KMS-on-write (DS~C's LiveS3Writer) ± a bucket policy.

DS~C's pattern (find-insure-data-key KMS per-object on PII-prefix writes) is the intent-honoring + only-viable mechanism. NOT a defect — a PRD wording gap.

## Recommendations (both non-urgent)
1. PRD §3.1 reword (CTO ask sent): bucket-default stays AES256; PII prefixes get SSE-KMS via per-object-write ± bucket policy.
2. Optional defense-in-depth (me, POST-.024-run): bucket policy denying s3:PutObject to the 5 PII prefixes without aws:kms+find-insure-data-key. Deferred so it can't gate DS~C's LIVE .024 demo-day writes; will test condition vs DS~C's actual write headers + plan→safe-apply→0-diff.

## Routing
Disposition → COO; CC CTO (PRD reword) + DS~C (pattern-correct reassurance). No apply, no TF change this tick.

## Posture
Back to standby. Optional enforcement-policy queued behind .024 active-write-window-close signal.
