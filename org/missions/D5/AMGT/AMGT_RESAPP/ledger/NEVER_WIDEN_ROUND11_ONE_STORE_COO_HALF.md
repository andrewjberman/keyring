# NEVER-1 co-sign, ROUND 11 -- the COO half: the served read path moves from the DynamoDB articles table and bare date partitions to the pool and committed generations

**Signer:** `2.0.0_SA_COO~W` | **Date:** 2026-09-15 ~07:1xZ | **Act covered:** `AMGT_RESAPP.TO-AMGT-rj-10` (the round's ONE terraform act in `infra/aws/terraform/harvest/`) | **The other half:** `1.0.0_SA_CTO~W`, requested in the round-11 issuance commit; the act does not run until both halves are files (rj-10 AC1).

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| key | what moves | how it is measured | rollback |
|---|---|---|---|
| `aws_lambda_function` `opal-amgt-scoped-api` (module.scoped_amgt_api) | code: the closure zip rebuilt to carry `lib/research/coverage/pool_reader.py`, its schema files from `lib/opal_data_harvest/`, a vendored `jsonschema`, and chain A's route edits | `terraform plan` shows the function UPDATED IN PLACE (source_code_hash); 0 destroy | re-upload the prior artifact (head-object `Meta.content-sha256 sSanbq4vc+SDwxKfHplJr32E7hiPTYSJKm37hVMkPHA=`, 75917 B, the round-10 object, kept in the deliverables) and re-apply |
| `aws_lambda_function.chatter_axis_producer` (`amgt-resapp-chatter-axis`) | code: the producer zip rebuilt with the pool reader, the crosswalk and the generation writer | UPDATED IN PLACE; 0 destroy | re-upload the prior zip (`CodeSha256 fj8wqp9jaZWfMaBrrAyUImGnt2c5Xeb7losUr+i65mM=`, 24370 B) and re-apply |
| `aws_iam_role_policy.chatter_axis_lambda` and `aws_iam_role_policy.scoped_amgt_api_grants` | READ grants added: `s3:GetObject` + `s3:ListBucket` on `opal-data-harvest` for the prefixes `publication-links/v1/`, `publications/v1/`, `universe/v1/`, `crosswalk/v1/`, `filings/v1/`, `drafting/v1/`, `peers/v1/`, `management/v1/`, `posture/v1/`; the DynamoDB `opal-harvest-articles` grants REMOVED from both; no Scan, no wildcard resource | UPDATED IN PLACE; the plan's policy diff lists exactly these statements | re-apply the prior policy documents (in git at the pre-act commit) |
| DynamoDB `opal-harvest-security-metrics` -- DATA, written by the producer's QA invoke | new items under `<AXIS>#<date>#<generation_id>` and the pointer items `<AXIS>#<date>` / `_CURRENT`; prior generations and prior bare-date rows are NEVER deleted | the invoke's output and a COUNT per partition | none needed: additive; the reader selects by pointer |
| The served payloads of `/api/scoped/amgt/security/{key}/coverage`, `/thesis`, `/peers`, `/security/{key}/overlay` (points), `/lead-panel/rankings/*`, `/lead-panel/timeseries/*`, the new management and posture routes | their CONTENT moves: coverage from the pool instead of an empty table; rankings from committed generations; thesis with drafted sections and passages; peers from R-1; management from M-1; posture from O-1 | rj-10's live reads, each with its denominator, and rj-3's exact-input exercise | the two code rollbacks above restore the round-10 payloads |

**Writers of the named properties, counted (NEVER-1's rule):** the metrics table's ranking partitions have ONE writer, the producer (its QA invoke and its 10:00Z schedule); the pool prefixes have ONE writer each (19d); the served payloads have ONE producer, the adapter. No second writer sets any property this act names.

## What the act may NOT touch

The `portal` gitlink and any served portal artifact (PORTAL FROZEN: COMMIT YES / PROMOTE NO); any other Lambda, role, table or bucket in the harvest root (the 16 pre-existing resources and the mount's 19 stay unchanged -- the plan's census proves it); `opal-data-etfs` (read-only, never a grant to write); `s3://opal-data-harvest` objects (the act deploys readers; the pool's writers are the local batches and the harvester); the analyzer, the ranker, the management lane, Posture (local jobs; no function, no schedule); the harvest collection mechanism and cadence (Andrew's); any monitor, alarm, SNS or SES.

## Both branches of every outcome named

- The plan reads `0 to add, N to change, 0 to destroy` with N the two functions and the two policies (4) plus the source-code-hash-only changes the closure rebuild causes: SIGNED. Any add, any replace, any destroy, or a change on an address outside the table above: NOT SIGNED -- the act STOPS on a row.
- The producer's QA invoke writes a COMPLETE generation for the day (or an EMPTY one on the BREAKOUT axis on an all-zero day): both are inside the act. A FAILED marker is inside the act too (the prior pointer stays current).

## Provenance

PRD v0.8 @`1170b4da69` C-ONE-STORE, C-RANKING-GENERATION, C-ONE-IDENTITY; the round-10 halves `NEVER_WIDEN_ROUND10_MOUNT_COO_HALF.md` / `..._CTO_HALF.md` @`cf54bd03f3` (the mount this act updates); decomposition v1.3 s.19 @`73938cdae4` (rj-10). Push state: LOCAL.

## CORRECTION (2026-09-15 ~07:4xZ, `2.0.0_SA_COO~W`, on the CTO half @`e1c3cf0cb3` s.6; the signature above stands for the same set)

- **The census.** "the 16 pre-existing resources and the mount's 19 stay unchanged" understated the root: at HEAD it holds **32 state
  entries / 42 instances** (round 10's 16, the 6 the producer's consolidation moved in under ri-2, and the mount's 10 entries that expand
  to 19 instances). The act changes 4 entries; **28 entries stay unchanged**; the two data sources are counted apart. rj-10 AC4 prints
  entries and instances separately.
- **The writers.** "the metrics table's ranking partitions have ONE writer" is true of the CHATTER partitions this act touches and false
  of the table: the box-side price pull (`integrations/bloomberg/research/price_axis_pull.py`, TRENDING_/BREAKOUT_PRICE#, no pointer)
  and `lib/research/watchlist/store.py` (star markers) also write it. Neither is inside this act; no PRICE partition exists live, so the
  served PRICE ranking already reads row_count 0 and the act cannot lower it.
- **The pointer.** The `_CURRENT` pointer sits inside the legacy bare-date partition the rolled-back adapter queries through
  `axis-rank-index`; it carries NO `rank_sort` attribute (rj-5's writer guarantees it, rj-10 AC7 prints the attribute names), so a
  rollback never serves it as a row.
- **The artifact.** `research/opal-amgt-scoped-api.zip` is overwritten by this act; the rollback is the prior `VersionId`, printed by
  rj-10 AC2 before the upload.
- **The producer's grant** is the four-prefix shape (`publication-links/v1/`, `publications/v1/`, `crosswalk/v1/`, `universe/v1/`); the
  adapter's is the nine-prefix shape. Both are inside the CTO's signature.
