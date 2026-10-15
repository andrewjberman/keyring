# S3 cost anomaly 2026-10-11..14 (DataTransfer-Out $67.99) -- which bucket, prefix, workload, why

**Author:** 4.0.0_SA_CRO (laptop). **Measured:** 2026-10-15 05:3xZ-06:2xZ. **Ask:** 1.0.0_SA_CTO msg 109339 (relay via
muse, bus 600e9b14, "said to be from Andrew; unconfirmed"). Research only: read-only AWS (Cost Explorer, the CUR parquet
copied to scratch, CloudWatch, CloudTrail via an Athena SELECT on the existing `cloudtrail_forensics.ct_use1` table,
`s3 ls`, describe/get calls). No service, bucket, trail or schedule was changed.
**Repo paths** are relative to `file:///C:/Users/AndrewBerman/Desktop/ajb_workspace/`. Code read at `box/laptop`.

## Conclusion

1. **Bucket: `opal-data-harvest`, 72% of the window's egress.** 541 GB of the 755 GB that left S3 on 10-11..10-14, and
   941 GB since 10-05, from an 8.0 GB bucket (60,953 objects). The bucket is being re-read 12-30 times a day.
2. **Workload: the AMGT_HARVST collection runner on site Z** (Windows task "Opal Data Harvest - Continuous Cycle",
   `lib/opal_data_harvest`), INFERRED (see Evidence law). **Why:** two code paths re-read an entire silver prefix on
   every call: `store.silver_latest()` lists and GETs "every part-*.parquet" under the source's silver table
   (`lib/research/harvest/store.py:373-397`), and it is called (a) by `silver_append` on every append
   (`store.py:431-440`) and (b) by `harvest_grammar.watermark()` once per (security, publisher) job
   (`lib/opal_data_harvest/harvest_grammar.py:140-153`, docstring: "a full per-(source,table) scan"). A bbg cycle is 242
   pairs (`AMGT_HARVST/.../round85/bz11_reads.out`), so one cycle re-reads the 0.21 GB bbg article silver about 242
   times, about 50 GB, before any append. The read is quadratic in what is stored, which is why egress has climbed
   since 10-02.
3. **Second bucket: `opal-data-bd`, 143 GB in the window (72.6 GB on 10-14, 52.6 GB on 10-12).** CloudTrail names the
   reader: IAM user `cloudops-dell1-agent-user` from `108.242.96.89` (the dell1 box), Boto3, prefixes `gold/entities`
   (10-12 09-13Z) and `silver/prices` (10-14 01-03Z). That is dell1 agent work (ADVI/MDPF checks reading bd gold and
   silver), MEASURED.
4. **Third: `opal-data-assets`, 53 GB in the window** (29.6 GB on 10-11 at 02-04Z and 18Z). US-daytime bursts; agent
   work on a box. No CloudTrail data events on that bucket, so the principal is UNREAD.
5. **No tie to the `/api/general/mdpf` edge gate.** The gate closed 23:06Z 10-14; the egress runs 10-07 onward, around
   the clock. CloudFront's own egress is 0.2-0.6 GB a day and an S3-origin fetch by CloudFront is not billed as S3
   DataTransfer-Out. CloudTrail shows no CloudFront or anonymous reader.
6. **Requests-Tier1 ($2.14):** the request storm is a different bucket, `opal-313476888478-globgrph`: 2.29M requests
   on 10-14 (vs 0.12-0.29M a day before), 145 GB downloaded on 10-14 and 72 GB in the first 6 hours of 10-15, in
   bursts at 00Z, 05Z and 12Z, but only 0.5 GB of it is egress, so the reader is in-VPC (Trino/Nessie/serving on the
   `opal-globgrph` ECS cluster, or the nightly producers). Not the $67.99; about $1-2 a day of requests. Reader UNREAD.

## Numbers (MEASURED)

**Cost Explorer, S3, daily (`ce get-cost-and-usage`, SERVICE = Amazon Simple Storage Service, by USAGE_TYPE):**

| day | DataTransfer-Out-Bytes | GB | Requests-Tier1 | Requests-Tier2 |
|---|---|---|---|---|
| 10-09 | $19.90 | 221.1 | $3.81 | $0.83 |
| 10-10 | $0.98 | 10.9 | $1.12 | $0.20 |
| 10-11 | $25.50 | 283.4 | $3.62 | $1.16 |
| 10-12 | $16.41 | 182.3 | $2.35 | $0.61 |
| 10-13 | $9.43 | 104.8 | $2.06 | $0.54 |
| 10-14 | $16.65 | 185.0 | $2.21 | $1.36 |

By OPERATION the egress is GetObject (279.6 / 180.3 / 103.1 / 182.9 GB on the four days); ListBucket is 1.4-3.5 GB a day.

**Per bucket, from the hourly Cost and Usage Report** (`s3://opal-cur-313476888478/cur/opal-cur/opal-cur/year=2026/month=10/opal-cur-00001.snappy.parquet`,
5.9 MB, delivered 2026-10-14 22:25Z, usage through 10-14 21:00Z; `line_item_resource_id` is the bucket). GB of
`DataTransfer-Out-Bytes`:

| day | opal-data-harvest | opal-data-assets | opal-data-bd | other | TOTAL GB | USD |
|---|---|---|---|---|---|---|
| 10-01 | 54.7 | 29.8 | 0.8 | 6.2 | 91.5 | 0.00 (free tier) |
| 10-02 | 80.4 | 4.4 | 0.9 | 5.6 | 91.3 | 7.5 |
| 10-05 | 61.9 | 2.5 | 0.1 | 3.9 | 68.4 | 6.2 |
| 10-07 | 112.8 | 54.5 | 15.3 | 11.8 | 194.5 | 17.5 |
| 10-08 | 42.2 | 51.7 | 8.1 | 4.1 | 106.2 | 9.6 |
| 10-09 | 149.9 | 40.7 | 15.4 | 15.2 | 221.1 | 19.9 |
| 10-10 | 10.6 | 0.1 | 0.0 | 0.2 | 10.9 | 1.0 |
| 10-11 | 242.5 | 29.6 | 4.0 | 7.2 | 283.4 | 25.5 |
| 10-12 | 127.0 | 0.8 | 52.6 | 1.9 | 182.3 | 16.4 |
| 10-13 | 77.8 | 9.6 | 13.7 | 3.7 | 104.8 | 9.4 |
| 10-14 (to 21Z) | 93.4 | 13.0 | 72.6 | 6.0 | 185.0 | 16.6 |

Window 10-11..10-14: **755.4 GB, $67.99** (equals the ask's figure). "other" is opal-data-49financial (2-3 GB/day),
opal-data-cot, opal-data-inf, opal-data-etfs, opal-data-portal-v2, opal-data-cottonwood, opal-data-inflection and
the globgrph bucket (0.1-0.5 GB/day each). The harvest bucket's CUR tags: `macro=AMGT`, `project=AMGT_RESAPP`.

**opal-data-harvest egress by hour (GB, UTC), the shape of the workload:**

| hour | 10-11 | 10-12 | 10-13 | 10-14 |
|---|---|---|---|---|
| 00-04 | 5.2 5.5 7.4 26.0 4.7 | 25.8 7.4 7.2 5.9 5.4 | 0 0 0 0 0 | 4.5 4.6 4.5 4.1 4.5 |
| 05-09 | 5.8 4.9 4.9 6.7 7.5 | 6.8 6.2 3.5 4.5 6.3 | 0.5 4.6 3.9 3.3 3.9 | 5.9 5.2 4.3 2.5 4.0 |
| 10-14 | 5.8 6.2 6.3 31.7 4.8 | 5.7 5.2 4.9 4.7 3.3 | 4.0 4.1 4.0 4.4 3.7 | 2.1 4.5 4.3 4.7 4.3 |
| 15-19 | 3.8 5.5 5.2 5.1 20.0 | 4.5 4.5 4.6 4.3 4.4 | 4.3 3.9 3.3 4.4 4.8 | 4.1 2.7 3.7 3.7 3.9 |
| 20-23 | 18.2 32.7 5.5 12.8 | 1.7 0 0 0 | 4.3 4.5 6.1 5.8 | 6.7 4.5 (report ends 21Z) |

A steady 4-6 GB every hour, around the clock, from 10-11 00Z, with an 8-hour gap 10-12 21Z to 10-13 05Z, plus
20-33 GB bursts on 10-11 (03Z, 13Z, 19-21Z) and 10-12 00Z. Before 10-11 the hourly shape was US-daytime bursts
(10-07 and 10-09 at 17-22Z), consistent with interactive agent work plus the runner's earlier, smaller cycles.

**The bucket is small.** CloudWatch `BucketSizeBytes` 8.0 GB, `NumberOfObjects` 60,953 (10-14). One full listing
(59,467 objects, 7.97 GB) by prefix:

| GB | objects | prefix |
|---|---|---|
| 2.98 | 8,152 | bloomberg/harvest/bronze |
| 1.41 | 1,543 | wsj/harvest/bronze |
| 0.88 | 30,611 | seeking-alpha/harvest/bronze |
| 0.75 | 2,134 | derived/model_block |
| 0.50 | 4,631 | amgt/harvest/bronze |
| 0.37 | 2,951 | seeking-alpha/harvest/silver |
| 0.31 | 774 | barrons/harvest/bronze |
| 0.30 | 2,825 | amgt/harvest/gold |
| 0.21 | 749 | bloomberg/harvest/silver |
| 0.13 | 421 | wsj/harvest/silver |

**opal-data-bd, CloudTrail data events** (Athena, `cloudtrail_forensics.ct_use1`, dt 2026/10/12 and 2026/10/14,
GetObject on bucketName opal-data-bd, grouped by hour, principal, IP, prefix; query id
`47a6771b-8749-47e1-9b22-0db018b9a5d6`, 0.24 GB scanned):
- `cloudops-dell1-agent-user` from `108.242.96.89` (Boto3 1.43): 10-12 09-13Z `gold/entities` 3,802 + 11,500 +
  15,172 + 7,589 GETs; 10-14 01-03Z `silver/prices` 2,125 + 5,650 + 971 GETs, plus `forwardfill_v2/unrealized` (aws-cli).
  These hours are exactly the CUR egress hours for bd (10-12 09-13Z: 4.8/2.4/15.3/18.8/10.4 GB; 10-14 01-03Z:
  20.4/42.3/6.3 GB).
- `bd-exporter-ec2-role` from `172.31.12.5` (in-VPC EC2, the bd gold runner): 58k GETs per run on `gold/canonical` at
  00Z and 05Z. In-region, not egress.
- No CloudFront, no anonymous, no foreign principal.

**opal-313476888478-globgrph request metrics** (the only bucket with S3 request metrics, `FilterId=EntireBucket`):
BytesDownloaded 5-8 GB/day 10-01..10-12, 15.8 GB 10-13, 145.1 GB 10-14, 72.1 GB 10-15 00-06Z; GetRequests 147k
(11Z), 354k (12Z), 184k (23Z) on 10-14 and 142k (05Z) on 10-15 against a 470/hour baseline. ECS tasks
`globgrph-trino`, `globgrph-nessie`, `globgrph-serving` have run since September (no restart). Nightly producers:
derive-runner 02Z, stitch 03Z, cse 03:30Z, comp-learns 04Z, fedobs 04:30Z. The 00Z/05Z/12Z bursts match none of them.

**Instruments that could not answer:**
- Cost Explorer resource-level granularity is not enabled (AccessDenied; payer-account setting).
- CloudTrail S3 data events are logged for `opal-data-49financial`, `opal-data-bd`, `opal-data-cot`, `opal-data-inf`
  only (trail `opal-organization-trail`), not for `opal-data-harvest`, `opal-data-assets` or the globgrph bucket.
- Server access logging is on for `opal-data-security` and `opal-security-evidence` only (41 buckets read).
- Storage Lens is the free default dashboard (no activity metrics). Athena has no recent query history in either
  workgroup.
- The site Z and dell box task states are UNREAD from this laptop.

## Evidence law on the harvest attribution

The bucket, the bytes and the hours are MEASURED (CUR). The reader is INFERRED, on four legs: (1) the only continuous
off-AWS process that reads harvest silver is the site Z runner (`install-cycle-schedule.ps1`, AtLogOn, no end;
re-pinned 10-14 00:09Z with `-RefreshOnce`, `round85/bz10_register.out`), and its bbg cycle ran 18:58Z-23:53Z on 10-13
and from 00:09Z on 10-14 (`bz11_reads.out`), the hours the steady read is present; (2) the egress is around the clock,
which no interactive agent produces; (3) the code mechanism above makes a cycle's read volume tens of GB on a 0.21 GB
prefix; (4) the two prefixes the mechanism reads, `*/harvest/silver/article` and `*/harvest/silver/listing_hit`, are
the ones that have grown since 10-02 (`HVST-ai-5` 10-02, `HVST-at-1` 10-05 changed the append cadence, not the
full-scan read). What would prove it: one hour of S3 data events on `opal-data-harvest`, or the runner's own per-cycle
S3 call count (`.runtime/harvest-cycle/state` on site Z). Lambda readers of the same prefixes (chatter axis, freshness
snapshot, scoped API) are in-region and do not bill as DataTransfer-Out.

## GAPS

| # | Surface | What is missing | Proposed fix | Project |
|---|---|---|---|---|
| E1 | `store.silver_latest()` full-prefix scan on every `silver_append` and every `watermark()` | A 0.21 GB prefix is re-read about 242 times per bbg cycle; egress is quadratic in stored parts. ~$50 of the $68. | Cache the silver index per cycle (one scan per (source, table) per cycle, not per pair), or keep a per-source manifest object (record_key -> part) so append and watermark read one small object. Compaction of parts is the second half. | AMGT_HARVST |
| E2 | Site Z runner egress is invisible | No S3 data events, no access logs, no request metrics on `opal-data-harvest`; attribution took the CUR plus inference. | Add `opal-data-harvest` to the trail's ReadOnly data-event selector, or enable request metrics (`PutBucketMetricsConfiguration`) on the bucket. The runner should also print S3 GET count and bytes per cycle into its cycle record. | AMGT_HARVST |
| E3 | dell1 bulk reads of `opal-data-bd` (`gold/entities`, `silver/prices`) | 143 GB in four days from one IAM user; each read was a full-table pull by an agent check script. | Agent checks that need a whole table run in-region (the bd gold EC2 or a Lambda), or read the served platinum object instead of silver/gold. | ADVI (dell1 CTO to place) |
| E4 | `opal-data-assets` reads | 53 GB in window, 200 GB since 10-05; no data events, so the reader is unknown. | Same instrument as E2 for `opal-data-assets`. | MDPF_CANON or NFRA (CTO to place) |
| E5 | globgrph request storm | 2.29M requests/day since 10-14 11Z, in-VPC, reader unknown. | Request metrics are already on; add a per-prefix filter (`warehouse/`, `stitch/`) and read `AllRequests` by prefix for one day to name it. | NFRA_CLDGRPH |
| E6 | Cost attribution instrument | Resource-level Cost Explorer is off; the CUR parquet had to be copied and parsed by hand. | Create the Glue/Athena table the CUR already ships a template for (`cur/opal-cur/crawler-cfn.yml`, `opal-cur-create-table.sql`), so a per-bucket per-hour question is one SELECT. | NFRA (CTO to place) |

## Commands (all read-only)

- `aws ce get-cost-and-usage --time-period Start=2026-10-01,End=2026-10-16 --granularity DAILY --metrics UnblendedCost UsageQuantity --filter '{SERVICE=Amazon Simple Storage Service}' --group-by Type=DIMENSION,Key=USAGE_TYPE` (and `Key=OPERATION`).
- `aws ce get-cost-and-usage-with-resources ...` -> AccessDeniedException (opt-in feature).
- `aws s3 cp s3://opal-cur-313476888478/cur/opal-cur/opal-cur/year=2026/month=10/opal-cur-00001.snappy.parquet <scratch>` then pandas pivot on `line_item_resource_id` x day/hour for `line_item_usage_type ~ DataTransfer-Out-Bytes`, `line_item_product_code = AmazonS3`.
- `aws cloudwatch list-metrics --namespace AWS/S3 --metric-name BytesDownloaded` (1 bucket); `get-metric-statistics` BytesDownloaded/GetRequests on `opal-313476888478-globgrph`, period 86400 and 3600; `BucketSizeBytes`/`NumberOfObjects` on `opal-data-harvest`.
- `aws cloudtrail describe-trails`, `get-event-selectors`, `get-trail-status`; `aws athena start-query-execution --work-group opal_mcp --query-execution-context Database=cloudtrail_forensics --result-configuration OutputLocation=s3://opal-mcp-athena-results/cro-egress-20261015/` with the GetObject GROUP BY above; `get-query-results`.
- `aws cloudfront list-distributions`; `get-metric-statistics` AWS/CloudFront BytesDownloaded for EVTSA9VEHNZVH.
- `aws s3 ls s3://opal-data-harvest/ --recursive` (one listing, aggregated locally); `s3api get-bucket-logging` on 41 buckets; `comp-find --corpus aws '.' S3_BUCKET --all` (41 buckets); `comp-trigger --list`; `ecs describe-clusters/list-services/list-tasks/describe-tasks opal-globgrph`; `scheduler get-schedule`; `glue get-tables`/`get-table`.
