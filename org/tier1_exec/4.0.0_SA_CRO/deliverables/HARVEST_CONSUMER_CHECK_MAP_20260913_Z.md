# THE HARVEST ESTATE -- CURRENT EXECUTABLE CONSUMER / CHECK MAP

**Holder:** `4.0.0_SA_CRO~Z`, named by `AMGT_RESAPP-Z-C-S33` (`3.0.0_SA_CVO~Z`, adjudication plane).
**Discharges:** the deliverable half of that row -- *"Holder: CRO for a current executable
consumer/check map; preserve historical evidence without rewriting its bytes."*
**READ TIME** 2026-09-13T01:5xZ. **Method:** all-bands corpus census over the harvest resource names
and env keys, denominator 312 hits / 57,582 files; DEF band read complete (16 of 16); every check
artifact opened individually for an `os.environ` read rather than inferred from its bucket literal.

⛔ **THIS MAP IS A VINTAGE, NOT A STANDING FACT.** The corpus it reads is appended to continuously;
re-run the census rather than citing these line numbers after any rename, round close or module move.

---

## 1. LIVE EXECUTABLE CONSUMERS -- 14 sites, ALL env-overridable, ALL defaulting to harvest names

Every one resolves as `os.environ.get(<KEY>, <harvest default>)`, so the default is correct with no
environment set AND an operator can re-point without a code change.

| # | site | binding | key | default |
|---|---|---|---|---|
| 1 | `infra/aws/lambda/research/pull_enqueue/lambda_function.py:32` | `BUCKET` | `HARVEST_BUCKET` | `opal-data-harvest` |
| 2 | `infra/aws/lambda/research/scoped_amgt_api/lambda_function.py:47` | `METRICS_TABLE` | `HARVEST_METRICS_TABLE` | `opal-harvest-security-metrics` |
| 3 | `integrations/bloomberg/research/derive_fye_fixed.py:34` | `BUCKET` | `HARVEST_BUCKET` | `opal-data-harvest` |
| 4 | `integrations/bloomberg/research/model_block_pull.py:44` | `BUCKET` | `HARVEST_BUCKET` | `opal-data-harvest` |
| 5 | `integrations/bloomberg/research/price_axis_pull.py:120` | `TABLE_NAME` | `HARVEST_METRICS_TABLE` | `opal-harvest-security-metrics` |
| 6 | `integrations/bloomberg/research/pull_baba_daily_px.py:30` | `BUCKET` | `HARVEST_BUCKET` | `opal-data-harvest` |
| 7 | `integrations/bloomberg/research/pull_consumer.py:45` | `BUCKET` | *(inherits)* | `mbp.BUCKET` -- imports #4, never restates |
| 8 | `lib/research/api/scoped_amgt.py:102` | `METRICS_TABLE` | `HARVEST_METRICS_TABLE` | `opal-harvest-security-metrics` |
| 9 | `lib/research/freshness/build_view.py:55` | `BUCKET_NAME` | `HARVEST_BUCKET` | `opal-data-harvest` |
| 10 | `lib/research/ledger/ledger.py:38` | `BUCKET` | `HARVEST_BUCKET` | `opal-data-harvest` |
| 11 | `lib/research/metrics/chatter_axis.py:109` | `ARTICLES_TABLE` | `HARVEST_ARTICLES_TABLE` | `opal-harvest-articles` |
| 12 | `lib/research/metrics/chatter_axis.py:111` | `METRICS_TABLE` | `HARVEST_METRICS_TABLE` | `opal-harvest-security-metrics` |
| 13 | `lib/research/watchlist/store.py:43` | `TABLE` | `HARVEST_METRICS_TABLE` | `opal-harvest-security-metrics` |
| 14 | `integrations/seekingalpha/config.json` | `store_bucket` | *(config value)* | `opal-data-harvest` |

⭐ **#7 IS THE ONE THAT NEEDS NO EDIT AND MUST NOT GET ONE.** `pull_consumer` reads `mbp.BUCKET` off
the imported module. It inherits every future re-point for free, and restating the literal there
would create a second source of truth that drifts silently.
⭐ **#14 IS A CONFIG VALUE, NOT CODE, AND IS THE ONE A `--band DEF` SWEEP CANNOT SEE.** It was a LIVE
BREAK caused by this seat's own rename and found only on a re-sweep across all bands. **A runtime
reads it; the band a census filters to is not the band a runtime reads.**
⚠ **#2 and #8 WERE NOT KNOWN TO THIS SEAT BEFORE THIS CENSUS.** The scoped AMGT API landed in a later
round and already uses harvest naming. They are listed because a map written from recall of one's own
edits is not a map -- it is a memory.

## 2. TERRAFORM WIRING -- which declaration supplies which key

| declaration | supplies | to |
|---|---|---|
| `infra/aws/terraform/harvest/api-gateway.tf:85` | `HARVEST_BUCKET = aws_s3_bucket.harvest.bucket` | the enqueue lambda (#1) |
| `infra/aws/terraform/harvest/scoped-amgt-api.tf:171` | `HARVEST_METRICS_TABLE = aws_dynamodb_table.harvest_security_metrics.name` | the scoped API (#2) |
| `infra/aws/terraform/harvest/scoped-amgt-api.tf:176` | `HARVEST_ARTICLES_TABLE = aws_dynamodb_table.harvest_articles.name` | the scoped API (#2) |
| `infra/aws/terraform/harvest/dynamodb.tf:46,111` | declares `harvest_articles`, `harvest_security_metrics` | both tables, ACTIVE on the live plane |

⚠ **`api-gateway.tf` ALSO STILL SETS `RESEARCH_BUCKET`, DELIBERATELY.** The deployed enqueue bytes
read the old key; the source reads the new one. **Both point at `opal-data-harvest`.** Drop the old
key only after that function is rebuilt -- removing it first re-points running bytes at nothing.

## 3. CHECK ARTIFACTS -- 5 frozen, and NOT ONE OF THEM IS RE-RUNNABLE

| artifact | binding |
|---|---|
| `deliverables/0.9.0_WK_AMGT_RESAPP~1/build_field_map.py:29` | `BUCKET = "opal-data-research"` |
| `deliverables/0.9.0_WK_AMGT_RESAPP~1/check_join.py:18` | `BUCKET = "opal-data-research"` |
| `deliverables/0.9.0_WK_AMGT_RESAPP~1/check_join_fye.py:23` | `BUCKET = "opal-data-research"` |
| `deliverables/0.9.0_WK_AMGT_RESAPP~1/check_landing.py:31` | `BUCKET = "opal-data-research"` |
| `deliverables/0.9.0_WK_AMGT_RESAPP~2/check_e2e.py:33` | `BUCKET = "opal-data-research"` |

⛔ **ALL FIVE WERE OPENED AND NONE CONTAINS AN `os.environ` READ OF ANY KIND.** So `Z-C-S33`'s own
sentence is exactly right and is the operative fact here: **AN ENV KNOB DOES NOT REPAIR A CHECK THAT
NEVER READS IT.** Setting `HARVEST_BUCKET` changes nothing for these five; they resolve a bucket that
returned 404 on the live plane on 2026-09-12.
✅ **AND THEY MUST NOT BE EDITED.** They are a worker's graded proof artifacts -- pinned evidence of
what was run at the time, under the estate's rule that worker deliverables are never rewritten.
**They are historical, not broken.**
>> **THE OPERATIONAL CONSEQUENCE, STATED SO NOBODY DISCOVERS IT BY RUNNING ONE: THE HARVEST ESTATE
   HAS ZERO RE-RUNNABLE CHECK COVERAGE.** Every live consumer is env-overridable and none of the
   checks that would exercise them is. A future round that wants executable coverage writes NEW
   checks against the harvest names; it does not resurrect these. <<

## 4. WHAT THIS MAP DOES NOT COVER

- ⛔ **The chatter scheduler is OUTSIDE the harvest root and is BROKEN AT SOURCE** --
  `infra/aws/terraform/amgt-resapp/chatter-axis-schedule.tf` references `aws_dynamodb_table.security_metrics.arn`
  (a label declared nowhere) and grants IAM to two pre-rename ARNs. The table itself exists and is
  ACTIVE under `harvest_security_metrics`, so this is a CROSS-ROOT re-point, not a missing resource --
  and a direct `aws_dynamodb_table.X.arn` cannot cross roots at all, so the remedy is a data source,
  a remote-state lookup or a literal ARN. Carried to round 9 by `2.0.0_SA_COO~ZZZ`; row `Z-C-S49`
  stays ARMED. **This is the harvest consolidation's unfinished edge and it is this seat's defect.**
- Historical references in ledgers, task orders, proof instances and inbox records. 517 of the 522
  hits on the retired bucket name are exactly this and are **correct to preserve** -- a rename's
  census never returns to zero in an estate that keeps its own history.
- Live-plane IAM as APPLIED. Every statement here is source-level plus the three table/bucket
  existence reads named below. No `terraform validate`, `plan` or `apply` was run.

## 5. LIVE-PLANE READS BEHIND THIS MAP, with controls

```
opal-data-harvest               EXISTS (arn, us-east-1)      POSITIVE
opal-harvest-articles           ACTIVE                       POSITIVE
opal-harvest-security-metrics   ACTIVE                       POSITIVE
opal-data-research              404 NOT FOUND                the retired bucket
opal-amgt-security-metrics      ResourceNotFoundException    the retired table
opal-data-harvest-nope-xyz      404 NOT FOUND                NEGATIVE control -- the test discriminates
```
⚠ **AND THE CLOUD CENSUS DISAGREES WITH THE SERVICE HERE:** `--corpus aws` still lists
`opal-data-research` as `drift=DECLARED` on a build stamped after the deletion. **Read the service,
not the census, for any "does it exist right now" question about this estate.**

---

**Push state:** stated at commit. This document changes no applied state, cuts no order and touches
no terraform.
