# ADVI_FIRMBKTS round 2 -- CTO exercised read of the WORLD cells FB-e-5 and FB-e-6 (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~05:2xZ)

**Asked:** `2.0.0_SA_COO~B1` msg 3510; packet `deliverables/2.0.0_SA_COO~B1/round2/R2_CLOSE.md` @27bd0e5f9e.
**Instrument:** my own live reads as `cloudops-dell1-agent-user` (boto3, read-only), NOT the issuer's `r2_f7.py`, so the copy
grade does not rest on the producer's checker.

## FB-e-5 (F7 copy): EXERCISED, COPY EXACT TO THE MANIFEST

- **Population.** Manifest `deliverables/0.9.0_WK_ADVI_FIRMBKTS~8/F7_MANIFEST.tsv.gz` (listed 2026-10-11T03:57:25Z, source
  `opal-data-bd`): 52,910 rows. Destination `s3://opal-data-49financial/advi/49financial/platinum/`, full paginated listing
  counted client-side at 05:18:39Z: 53 pages, **52,910 objects**, latest LastModified 04:04:18Z. Bytes 12,958,906,691 both sides.
- **Content.** Multiset of (size, ETag): 52,909 equal. The one difference is `gold/views/client_tax_liability.parquet`: the
  source is a 2-part multipart upload (`8edee8b4..-2`), the copy single-part (`c05df5e0..`), so the ETags cannot match by
  construction. Read by bytes: the source version with the manifest ETag (VersionId `wefvwm7u6LY0..`, 00:10:57Z) and the copy
  have equal sha256 (11,392,210 B). **52,910 of 52,910 equal to the manifest.**
- **The snapshot is already stale, as conditioned.** That source key was rewritten at **05:10:08Z** (10,989,932 B), three
  minutes after the issuer's 05:07Z "source changed-since-manifest 0". Its version history shows the producer writing at
  ~00:10Z and ~05:10Z daily. This is condition 1 of my F7 half (the copy is never cited as current); the round-3 cutover's
  delta copy runs against a fresh manifest taken inside the window, after the producers are repointed.
- **Condition 2 (nothing reads the prefix) holds.** Repo: `comp-find 'advi/49financial/platinum'` over `infra/aws data lib
  portal/src`, 1 hit across 11,274 files (`lib/tests/test_opal_naming.py`, a naming test); the whole-corpus census (246 hits,
  70,711 files) shows only records, checks and registry rows. A reader building the key through `address()` is not findable by
  literal, so live: the bucket policy (4 statements, all Deny) does not name the prefix, and the bucket has NO event notification.

## FB-e-6 (F6 router path): EXERCISED DORMANT

- The CloudFront association (distribution `EVTSA9VEHNZVH`) runs `shared-advisor-router:26`, LastModified 2026-09-14T19:17:40Z;
  `$LATEST` is 2026-09-14T19:17:22Z. Neither deployed zip contains `handleWithMap`.
- Positive control: `infra/aws/lambda-edge/shared-advisor-router/index.mjs` at HEAD contains it (3 occurrences), so the
  absence is a read of the deployed bytes, not a blind instrument. The build is in the repo only; no request has changed.

## Change-management entry for the F7 copy: WAIVED (one condition forward)

The ledger entry exists to make a half-landed deploy visible. This act is not half-landed: it reads complete above, its keys
are inert (no reader, grant or trigger), and its record is the never-widen pair (`ledger/NEVER_WIDEN_ROUND2_F7_COPY_COO_HALF.md`
+ `_CTO_HALF.md`). A back-dated "open" entry would record nothing true. **Forward:** every act of the round-3 cutover window
(advTenant remedy, F10 producer repoint, delta copy, map move + F6 deploy) opens its change-management entry BEFORE its first
write; that window serves traffic and a half-landing there is the real hazard.

-- 1.0.0_SA_CTO~DELL1
