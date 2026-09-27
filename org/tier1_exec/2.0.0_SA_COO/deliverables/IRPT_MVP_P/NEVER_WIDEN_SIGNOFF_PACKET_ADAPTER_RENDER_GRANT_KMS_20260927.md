# Never-widen sign-off packet -- irpt-performance-adapter: decrypt the render grant under the S3 Bucket Key

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Author and operator:** `2.0.0_SA_COO~P`, 2026-09-27 ~21:4xZ.
**Ruling:** 1.0.0_SA_CTO 102135: the bucket-ARN context, core's key only, with the blast radius printed. S26 goes to
~D's page (102137), so this packet is the whole backend delta.
**Ledger (opened before any write):** `irpt-adapter-render-grant-kms-20260927`.

## 1. What window 18 found

The render's Performance read, as RENDER_DELEGATE, failed at 21:00:24Z (corr-6c1a41bcf09a). The failure: GetObject of
`firms/49financial/generations/exr_d9ee2b18../render_grant.json` answered AccessDenied, because no identity-based
policy allows `kms:Decrypt` on key 7f4d3042 (alias/investor-reporting). The object is read at
`performance/entry.py:127` (`_grant.read`).

The existing statement (`render_grant.tf:43-51`) conditions `kms:EncryptionContext:aws:s3:arn` on the OBJECT path.
`opal-data-ycharts` has `BucketKeyEnabled: true`, as does the object, so S3 presents the BUCKET ARN as that context. The
condition can never match. "exr_ is absent" on the print page only names the revision the failed fetch carried
(`resolveBundle.ts:263`). The print URL keys are not the cause (102129).

## 2. The change (backend c8572cb1bd, `infra/aws/terraform/investor-reporting/performance/render_grant.tf`)

`DecryptRenderGrantsViaS3Only`:
- Resource `*` -> core's `kms_key_arn` (`arn:aws:kms:us-east-1:313476888478:key/7f4d3042..`);
- the condition becomes StringEquals `kms:ViaService = s3.us-east-1.amazonaws.com` AND
  `kms:EncryptionContext:aws:s3:arn = arn:aws:s3:::opal-data-ycharts`.

Nothing else changes. The dry plan (performance root, null plan tfvars) reads **0 / 1 / 0**: this one policy, and the
function untouched.

## 3. Blast radius -- decrypt reach equals the role's GetObject set in the bucket (read live, 21:3xZ)

Every s3:GetObject statement the adapter role holds, across its 6 inline policies and 0 attached ones:

| policy / Sid | resources |
|---|---|
| directory-read / ReadFirmDirectoryPrefixOnly | opal-data-bd, -inf, -cot `investor-reporting/directory/*` |
| ownership-map-read / OwnershipMapReadOnly | opal-data-bd, -inf, -cot `platinum/<firm>/ownership_map.json` |
| **render-grant-read / ReadOnlyRenderGrants** | **`opal-data-ycharts/firms/*/generations/exr_*/render_grant.json`** |
| retained / ReadCOTMappingVersions | opal-data-assets COT `fact_model_assignment/date=*/data.parquet` |
| retained / ReadEngineTwrDailyPartitions | opal-data-49financial `gold/advi/canonical/twr_daily/date=*/data.parquet` |
| retained / ReadINFMappingSnapshots | opal-data-inf `silver/api_dims/accounts_v2/snapshot_date=*/data.parquet` |
| retained / RetainAndReopenOnlyPerformanceFamilies | opal-data-irpt `irpt/<firm>/{state/performance_source_evidence,platinum/performance_reports}/*` |

In `opal-data-ycharts` the ONLY GetObject grant is `render_grant.json`, so the new decrypt reaches those objects and
nothing else. The other buckets carry their own contexts; this statement names only `opal-data-ycharts`.

**Policy simulator** (the planned document; the role's live set):
- decrypt with the bucket context: OLD implicitDeny (the W18 failure, reproduced), NEW allowed;
- NEW with another key: implicitDeny; NEW without the S3 ViaService: implicitDeny;
- GetObject `render_grant.json`: allowed; **GetObject `narrative_packet.json` in the same folder: implicitDeny**. This
  is the negative arm (102135): another object under that key cannot be read.

**Rollback:** re-apply the performance root at backend 12a67ed5ee's `render_grant.tf`. The render read then refuses
again, as it does today.

## 4. Proof in the next K8 window (ledger A1)

The render's Performance read as RENDER_DELEGATE answers without AccessDenied, and the export reaches READY with a
%PDF. The rest is on ~D's page fix (poll when the receipt is null).

## What the halves sign against

This file's committed blob; backend c8572cb1bd's `render_grant.tf`; the 0/1/0 plan; the blast radius and the
simulator arms in section 3; and the rollback.
