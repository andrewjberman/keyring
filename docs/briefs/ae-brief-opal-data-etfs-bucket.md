# AE Brief — Import `opal-data-etfs` into shared-infra Terraform

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-15
**Audience:** 0.7.0_AE_CloudOps (shared-infra owner)
**Type:** S3 bucket adoption — bucket already exists, needs `terraform import`

---

## Summary

A new S3 bucket, **`opal-data-etfs`**, was created out-of-band (`aws s3 mb`, 2026-05-15,
us-east-1) for an ETF net-assets daily data series. It started as an off-the-books
pilot; Andrew has confirmed it is needed and directed that it be brought under
**shared-infra Terraform management**. This brief is the turnkey handoff — DS cannot
run terraform or edit `infra/aws/terraform/` (lane boundary), so AE owns execution.

The bucket **already exists with data in it** (296 objects), so this is an
`import`-then-`plan`-to-0-diff operation, not a fresh `apply`.

## What the bucket is

| | |
|---|---|
| Bucket | `opal-data-etfs` |
| Region | `us-east-1` |
| Purpose | Daily net-assets series for TrueShares ETFs (DIVZ, IDVZ) — NAV, market price, shares outstanding, net assets. Silver-tier daily parquet. |
| Producer | `etf_netassets_watch/etf_probe.py` (daily, Windows Task Scheduler 6 PM) + `backfill.py` (one-time history). Off-the-books today; see "Follow-ups". |
| Current contents | 296 objects — see layout below |

Layout (mirrors the BD silver tier — `silver/transactions/` + `silver/nna_timeseries.parquet`):

```
opal-data-etfs/
  silver/netassets/<YYYY-MM-DD>.parquet   293 per-day partition files (2025-05-30 .. 2026-05-15)
  silver/netassets_daily.parquet          consolidated daily series
  snapshots/snapshot_<YYYY-MM-DD>.json    per-run JSON snapshots
  etf_history.csv                         live-probe operational journal
```

## Current AWS-side state (already applied by `aws s3 mb` defaults)

- **SSE:** `AES256` (AWS default on new buckets) — confirmed via `get-bucket-encryption`.
- **Public access block:** all 4 flags `true` (AWS default) — confirmed via `get-public-access-block`.
- **Versioning:** not enabled.

Because SSE + PAB already match the shared-infra standard, importing those resources
should yield a **0-diff plan**.

## Action — add to `infra/aws/terraform/shared-infra/s3.tf`

Append this block (matches the existing pattern in that file — `opalinvest_portal`,
`ci_staging`, etc.):

```hcl
# ---------------------------------------------------------------------
# opal-data-etfs -- ETF net-assets daily series (TrueShares DIVZ / IDVZ:
# NAV, market price, shares, net assets). Silver-tier daily parquet,
# produced by the etf_netassets probe + backfill. Standalone data bucket
# -- no dedicated pipeline module, so it lives here per Andrew directive
# 2026-05-15.
# ---------------------------------------------------------------------

resource "aws_s3_bucket" "opal_data_etfs" {
  bucket = "opal-data-etfs"
  tags   = { Name = "opal-data-etfs" }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "opal_data_etfs" {
  bucket = aws_s3_bucket.opal_data_etfs.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "opal_data_etfs" {
  bucket                  = aws_s3_bucket.opal_data_etfs.id
  block_public_acls       = true
  ignore_public_acls      = true
  block_public_policy     = true
  restrict_public_buckets = true
}
```

> **Note on the `s3.tf` header comment.** That file says pipeline-specific data
> buckets stay in their pipeline modules. `opal-data-etfs` is a data bucket, but it
> has **no pipeline module** (it is a lightweight probe, not a full pipeline) and
> Andrew explicitly directed shared-infra. Recommend AE either accept this as the
> pragmatic home or lightly amend the header comment. Versioning was left out to
> match the majority pattern in `s3.tf`; enable it (like `analytics_dashboard`) if
> AE judges a data bucket warrants it — that would be a normal `apply`, not import.

## Import sequence

`export MSYS_NO_PATHCONV=1` first (Git Bash). From `infra/aws/terraform/shared-infra/`:

```bash
.tools/terraform.exe import aws_s3_bucket.opal_data_etfs opal-data-etfs
.tools/terraform.exe import aws_s3_bucket_server_side_encryption_configuration.opal_data_etfs opal-data-etfs
.tools/terraform.exe import aws_s3_bucket_public_access_block.opal_data_etfs opal-data-etfs
```

## Deploy sequence (per CLAUDE.md deployment rules)

1. Add the block to `s3.tf`.
2. Run the 3 `terraform import` commands above.
3. `terraform plan` — **expect 0-diff** (resources adopt existing AWS state).
4. `git commit` the `s3.tf` change (+ this brief if not already committed).
5. `terraform apply` — confirm 0-diff.
6. Tag: latest is `shared-infra-v1.10.0` → `git tag -a shared-infra-v1.11.0 -m "adopt opal-data-etfs bucket"` (verify with `git tag -l "shared-infra-v*" | sort -V | tail`).
7. `git push --follow-tags`.

## IAM

No IAM change required right now — the probe runs on Andrew's local machine using
local AWS credentials, which already have `s3:PutObject` on the bucket (the 296
objects uploaded successfully). **If** the probe is ever migrated to a Lambda/EC2
runner, that runner's role will need `s3:PutObject` / `s3:GetObject` /
`s3:ListBucket` on `opal-data-etfs` — out of scope for this brief.

## Verification

- `terraform plan` is 0-diff after import + apply.
- `aws s3 ls s3://opal-data-etfs/ --recursive | wc -l` still shows the object count (import does not touch data).
- `terraform state list | grep opal_data_etfs` shows the 3 resources.

## Follow-ups (not AE scope — flagging for routing)

- The `etf_netassets_watch/` probe scripts + `run_daily.cmd` are not yet committed
  (were off-the-books). Now that the bucket is going official, they should be
  committed to a sensible home and the work likely registered as a tracked project.
  That is a DS + COO call, separate from this Terraform brief.
