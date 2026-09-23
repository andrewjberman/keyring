# Investor Reporting storage: current state and planned end state

Prepared by 4.0.0_SA_CRO on September 22, 2026. Fresh read-only AWS storage audit began at 4:02 PM Eastern; directory pointer/refresh checks followed during the same review. No writes to AWS, vendor calls, deployments, or schedule changes.

## Direct answer

There is no bucket named `opal-data-irpt` in the inspected AWS account. The bucket serving the shared IRPT evidence/artifact role is **`opal-data-ycharts`**. Despite its vendor-specific name, the configured shared export service also targets this bucket.

The three tabs do not currently share one completed report store:

- **Sensitivity/Analysis:** encrypted inputs, request revisions, vendor PDFs, extracted sections, and branded exports are intended for firm-scoped prefixes in `opal-data-ycharts`; the production workflow is not populating that complete chain.
- **Model Overlay/Holdings:** published snapshots are intended for `investor-reporting/holdings/` inside each firm's own bucket. All three serving prefixes are empty; older QA snapshots exist separately.
- **Performance Reporting:** the current adapter returns its response through the API, in recorded mode. A durable archive of exact performance report revisions is not connected. Shared export storage is defined in `opal-data-ycharts`, but the export entry remains unconnected to its controller.

**`opal-data-portal-v2` is not the current planned destination for private directory/holdings outputs.** The backend PRD explicitly changed this in v0.5 following finding `IRPT_BCKEND-S1`: its recorded review found the old portal origin path did not enforce the needed authentication. The replacement is firm-bucket storage served through authorized IRPT handlers. This is a documented change, not a newly proposed migration. Older brief text and `PATH_MANIFEST.json` still mention the superseded portal-v2 destination. The PRD's B1, PATHS, and SURFACE MANIFEST carry the replacement.

## Storage map

| Storage | Purpose | Measured state |
|---|---|---|
| `opal-data-assets` and existing firm source buckets | Upstream vendor/custody/model facts; inputs to IRPT | Existing source estate, not a finished IRPT report archive; this audit does not recensus every upstream dataset |
| `opal-data-bd` | 49 Financial directory and holdings publication | Directory present; holdings serving prefix empty; September 11 QA holdings present |
| `opal-data-cot` | Cottonwood directory and holdings publication | Directory present; holdings serving prefix empty; September 11 QA holdings present |
| `opal-data-inf` | Inflection directory and holdings publication | Directory present; holdings serving prefix empty; September 11 QA holdings present |
| `opal-data-ycharts` | Shared, firm-separated IRPT evidence, analysis artifacts, and exports | 35 current objects: 33 under research, two synthetic export bundles under the 49F prefix; latest object modification September 11 |
| `irpt-requests`, `irpt-jobs`, `irpt-outbox`, `irpt-checkpoints` in DynamoDB | Request revisions, job/lease state, dispatch records, refresh/intake progress | All ACTIVE; complete count scans returned 0, 1, 0, and 0 items respectively. One job item is not evidence of a completed report |
| `opal-data-portal-v2` | Other portal data/assets; earlier IRPT serving proposal superseded | Zero objects under the checked `investor-reporting/`, `irpt/`, and `platinum/irpt/` prefixes; no active IRPT output target found in the reviewed Terraform/runtime bindings |

The portal-v2 census was limited to those prefixes and a root delimiter listing, not a recursive audit of every unrelated portal object. Lambda artifact buckets and Terraform-state buckets hold deployment packages/state, not investor report outputs.

## 1. Sensitivity Analysis

### Planned object layout

The current Terraform layout and destination/key libraries name `opal-data-ycharts`, with a separate `firms/{firm_id}/` boundary for 49financial, cottonwood, and inflection:

```text
s3://opal-data-ycharts/
  firms/{firm_id}/
    intake/YYYY/MM/DD/{id}/...
    requests/{id}/revisions/{r}/...
    generations/{id}/attempts/{a}/
      vendor/report.pdf
      sections/report.json
      exports/{revision}/bundle.json
      exports/{revision}/report.pdf
  quarantine/...
```

Intake preserves original inputs; request revisions preserve the holdings, interpretation, corrections, and manifest; generation attempts preserve the vendor output and extracted report; exports preserve the exact frozen print input and final PDF. The layout defines destinations, not proof that those objects exist. The browser CSV lane still needs its upload/ownership connector; both CSV and selected-account lanes need the common frozen normalized portfolio described in the sensitivity brief. The exact browser-upload subkeys are not yet a completed contract.

### Current state

The generation and intake Lambdas point to `opal-data-ycharts`. The bucket exists, with versioning enabled, default KMS encryption, and all four public-access-block flags enabled. No S3 lifecycle rule is configured. Versioning is not a WORM/Object Lock retention guarantee, and no such guarantee was verified here.

The 33 research objects include actual vendor PDFs from synthetic research portfolios, input/payload/receipt JSON, and a research source ZIP. They live under `research/20260911/...`, including the three-variant proof. These demonstrate isolated research output, not an advisor's released production report history.

There are no current objects under the declared firm intake/request families, no firm production vendor PDFs or extracted section reports, and only two synthetic export bundle JSONs under a firm generations prefix. The generation module's richer job state and blob adapter are still in-memory implementations, while the current status reader can inspect durable leases but cannot reconstruct a released report from them. Merely provisioning the bucket and tables does not connect persistence.

### Desired end state

Every accepted run should have a durable firm-owned input revision, normalized portfolio, settings/comparison/profile revision, job state, vendor PDF, certified AnalysisReport, and artifact receipt linked by stable IDs and hashes. Reopening the page should load that same report. Corrections should create a new revision; retries should reuse or reconcile the existing attempt. DynamoDB owns state/leases; S3 owns retained bytes; queues carry identifiers. Cookie/session material remains in Secrets Manager, not report storage. Finalize retention/lifecycle under the applicable records policy rather than leaving it undefined.

## 2. Performance Reporting

### Current state

The adapter is configured for `recorded` transport. It constructs a PerformanceReport response; its inspected execution path does not persist that report to S3. The guarded entry's default cache is request-local, so it is not durable report storage. The tenant adapter's `data_plane_bucket` fields describe vendor/source boundaries; they are not evidence of a report writer.

The live census found zero objects under `investor-reporting/performance/` in each firm bucket. These were diagnostic prefixes checked for presence, not declared functioning destinations. There is no populated archive of current performance reports in the reviewed IRPT path.

### Planned and unfinished storage

The product design requires the screen, narrative, and PDF to reference the same immutable performance revision. The shared export service explicitly writes to `opal-data-ycharts`, including performance exports; its vendor-specific bucket name does not limit the export feature to YCharts analysis.

The standalone PerformanceReport archive's exact object family and connected writer/reader are still incomplete in the reviewed implementation. It would be misleading to invent a canonical `performance/{id}.json` path and describe it as already planned/deployed. The next implementation must specify that destination in the tenant policy and bind the report ID to exact selected accounts, date windows, vendor response/source revision, and methodology. This should retain the vendor-calculated result, not recalculate returns.

A persisted complete export bundle can freeze the result used by a PDF, but it does not by itself provide general report history/list/retrieval. Both capabilities must refer to the same report revision.

## 3. Model Overlay / Holdings

### Declared and configured serving paths

For each firm's bucket:

```text
s3://{firm_bucket}/investor-reporting/holdings/{business_date}/snapshot.json
s3://{firm_bucket}/investor-reporting/holdings/latest.json
```

`latest.json` is the pointer the reader follows; the dated snapshot contains the node hierarchy and source/coverage facts. Input model sources remain SmartX for 49F, BD Rebalancer for Cottonwood, and Eclipse for Inflection, joined against complete custody holdings. Those source locations are distinct from the published snapshot location.

### Current state

All three `investor-reporting/holdings/` prefixes have zero objects. Each firm instead has two historical QA objects:

```text
investor-reporting/qa/holdings/2026-09-11/snapshot.json
investor-reporting/qa/holdings/latest.json
```

The default serving reader does not follow the QA prefix. Earlier same-day measurement found the holdings schedule disabled. The model-overlay brief documents why those QA artifacts cannot simply be promoted: duplicate/account-grain valuation defects, missing model/security output, and incomplete weights/classification.

### Desired end state

Publish a validated, complete current ownership snapshot per firm, preserving custody and model-overlay dates, unique actual holdings, model/non-model/unresolved classification, values, weights, and drilldowns. Only advance the serving pointer after successful independent reconciliation and coverage checks. Retain enough version/revision identity to retrieve the exact snapshot previously displayed; date-only names must not hide same-day corrections. Serve the selected authorized account set through the API. No move into portal-v2 is required by the current PRD.

## Shared directory and export storage

The header registry already has real storage at `s3://{firm_bucket}/investor-reporting/directory/{business_date}/directory.json`, plus `latest.json` and `_refresh/{date}/manifest.json`. Current pointers for all three firms still resolve to September 17 source data. September 22 refresh manifests exist, but report `UNCERTAIN` / `REFRESH_TRIGGER_MISSED` and a null source-completion date. A fresh monitoring manifest is not a fresh directory dataset.

The shared export library defines these keys in `opal-data-ycharts`:

```text
firms/{firm}/generations/{generation}/attempts/{attempt}/exports/{revision}/bundle.json
firms/{firm}/generations/{generation}/attempts/{attempt}/exports/{revision}/report.pdf
firms/{firm}/generations/{export_id}/receipt.json
```

It contains real bundle/receipt S3 writers, including read-back verification. However, the deployed submit entry still returns NOT_READY rather than connecting the full controller. The two current firm-scoped objects are synthetic bundle proofs; the bucket contains no current final PDFs under the firm export layout. The required end state is a frozen bundle, validated PDF, durable receipt, and authorized download of the same revision. Research PDFs do not count as this branded export pipeline.

## Completion priorities

1. Retain the current separation: firm buckets for private directory/holdings JSON; firm prefixes in the shared evidence bucket for inputs, analysis, and exports; DynamoDB for durable process state.
2. Finish the missing writers/readers and exact PerformanceReport storage contract, rather than create another bucket as a substitute for those connections.
3. Restore genuinely fresh directory/holdings publication after the correctness issues are fixed.
4. Connect both analysis inputs to retained revisions, durable execution, sections publication, and history retrieval.
5. Complete export finalization and retention rules, and remove stale portal-v2 destination wording from subordinate references through the owning implementation process.

## Evidence

- Fresh local audit: `.runtime/codex-seats/4.0.0_SA_CRO/irpt_storage_audit_20260922.py` and `.json`.
- Full 35-object evidence-bucket key census: `.runtime/codex-seats/4.0.0_SA_CRO/irpt_storage_objects_20260922.json`.
- Fresh directory pointer/refresh evidence: `.runtime/codex-seats/4.0.0_SA_CRO/irpt_storage_directory_20260922.json`.
- `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`: B1, B17, PATHS, SURFACE MANIFEST; explicit portal-v2 replacement.
- `infra/aws/terraform/investor-reporting/core/{s3.tf,layout.json,dynamodb.tf}`; generation/export/holdings runtime configuration.
- `infra/aws/lambda/investor-reporting/_keys/keys.py`; `ycharts/generate/job.py`; `ops/status_loader.py`; `performance/entry.py`; `_authz/served.py`; `export/{entry.py,handler.py}`.
- `docs/briefs/investor-reporting-performance-review-20260910.md` and `investor-reporting-ycharts-design-20260910.md`, read with the later PRD changes, not as current deployment inventories.

## Andrew-direct request — verbatim

Channel: user message to Codex seat 4.0.0_SA_CRO, September 22, 2026. Message timestamp unavailable; recorded during the 4 PM Eastern review.

> Qualify the state of data storage for each of these functions. where are the outputs saved? is there an irpt bucket? are they stored in opal-data-portal-v2? give me an overview on that aspect per tab and let me know its state and desired end state as planned.
