# Reporting backend and LGIC model/holdings foundation

Prepared by 4.0.0_SA_CRO, September 22, 2026. Proposed product/backend brief responding to Andrew's direction. This specifies the target and completion requirements; it does not create resources, change registry policy, migrate data, or deploy code.

## Recommendation

Adopt **`opal-data-irpt` as the proposed product-named reporting artifact store**, using the useful request/revision/attempt separation established for `opal-data-ycharts`. Preserve **all-client-account model/holdings data in each firm's canonical bucket**, with LGIC Gold Parquet history and Platinum JSON serving projections. Reuse the existing IRPT services and durable-state resources while completing their missing connections.

There are two distinct responsibilities:

1. **Firm data foundation:** a complete, reconciled account/position population and its model membership, maintained for every client account in each firm, independent of who is currently viewing the portal.
2. **Reporting records:** an immutable record of what a user requested, which data/settings were used, what the vendor returned, what Opal displayed, and which PDF was exported.

The model tab reads the first. Sensitivity and performance runs produce the second. A report may reference a specific firm snapshot revision and retain its frozen selected input; it must not become a second competing canonical holdings database.

## Current baseline and the delta

The preceding storage audit found `opal-data-ycharts` provisioned but containing research artifacts and synthetic export bundles rather than a production report history. IRPT currently reads directory/holdings paths from legacy firm buckets `opal-data-bd`, `opal-data-cot`, and `opal-data-inf`; all three holdings serving prefixes were empty. Performance has no connected immutable report archive.

A fresh read-only check at **4:12 PM Eastern** returned 404 for `opal-data-irpt` and 200 for all three canonical long-form client buckets. The naming registry recognizes `irpt` as a PRODUCT system, but has no `irpt` scope row. The current builder successfully generated the nine example firm Gold, Platinum, and state addresses retained in the evidence file.

| Function | Proposed authoritative home | Main delta from current implementation |
|---|---|---|
| All-account holdings and model attribution | Each firm's canonical Gold/Platinum planes | Build complete custody coverage, repair attribution/value grain, introduce durable Gold history, publish bounded serving projections |
| Performance request/result history | Private, firm-scoped reporting records in proposed `opal-data-irpt` | Persist exact vendor responses and normalized immutable reports; implement report lookup/history |
| Sensitivity input/run/result history | Same reporting store, separate request and attempt families | Connect both input lanes to durable normalized inputs, jobs, vendor PDFs, certified sections, and retrieval |
| Branded exports from either report type | Same reporting store, linked to the source report revision | Connect frozen bundle, renderer, validated PDF, receipt, and protected download |
| Workflow state | Existing tenant-keyed DynamoDB resources; any S3 workflow objects in `state/` | Make richer job transitions and report/artifact receipts durable; keep state out of Gold/Platinum |

## 1. LGIC placement and the reporting-bucket boundary

Canonical model/holdings homes are:

| Firm | Canonical client bucket | Authoritative model feed |
|---|---|---|
| 49 Financial | `opal-data-49financial` | SmartX |
| Cottonwood | `opal-data-cottonwood` | Black Diamond Rebalancer |
| Inflection | `opal-data-inflection` | Eclipse |

The LGIC key grammar remains **`{source}/{scope}/{tier}/{table}/{partition}`**, with the object beneath it. The bucket does not replace the source/scope segments. Use `irpt` as the derived system and the firm's LONG form as scope. Obtain destinations through `lib/opal_naming.py` and the canonical registries, not duplicated bucket maps.

**A specific distinction must be recorded for the new shared reporting bucket.** Current LGIC `address()` places FIRM-scoped Gold, Platinum, and S3 state in the firm's bucket. Merely naming a shared bucket `opal-data-irpt`, or labeling its objects `state`, does not make private per-firm records there conformant. This brief recommends a **narrow, explicitly recorded reporting-artifact placement policy** for that shared bucket, consistent with Andrew's recommended structure. Implement its registry/destination-policy support and any required LGIC exception record together. It is a proposal here, not a claim that an exception has already been acknowledged or that the current builder returns that address.

That policy covers request/run evidence and frozen report/export artifacts only. It does not relocate canonical client Gold/Platinum, relabel private data as global, or grant cross-firm visibility. Shared product resources may have shared execution, but every private object has an immutable firm owner. `opal-data-portal-v2` receives no private client reporting publication under this design.

## 2. Complete model/holdings data, before viewer filtering

Begin with the **full client-account census for each firm**, joined to complete custody holdings. Apply the SmartX, BD Rebalancer, or Eclipse overlay to that population. Do not start from the model-assignment roster: accounts absent from a model platform must still appear.

Include modeled, non-modeled, partially modeled, zero-balance, closed/terminated accounts with retained records, and accounts with stale or missing inputs. Account status and source freshness are explicit. An account with unavailable holdings is present with an availability finding, not silently omitted or valued at zero. An account's legitimate zero is distinct from an unknown amount. Missing value means the total is incomplete; it cannot be converted into a known dollar residual.

Canonical identities and coverage should support:

- Stable firm, relationship/household, account, position, security, sleeve/allocation, and model IDs, with retained vendor crosswalks.
- A dated relationship/account membership bridge, avoiding duplication when an account appears in multiple source hierarchies.
- Model-associated, confirmed non-model, and unresolved attribution; model provider and Opal/third-party status as separate attributes.
- Quantity, observed market value, currency, custody date, overlay date, source revision, and valuation basis. Targets remain separate from observed ownership.
- One holding's contribution counted once. Multiple allocations within one account and an Eclipse portfolio spanning several accounts require explicit allocation at the supported grain.

The completeness test is both **account coverage and dollar reconciliation**. For known-valued holdings, model + non-model + unresolved value must equal unique custody value. Also report accounts/positions with unknown values, currency limitations, and mapping gaps. No aggregate is described as complete merely because its included rows sum correctly.

## 3. Bronze/Silver -> firm Gold -> firm Platinum

Reuse the existing vendor ingest families. For client/partner custodial inputs, retain raw Bronze and complete typed/deduplicated Silver in their LGIC ingest homes in `opal-data-assets`; declare legacy source paths until their own migrations are complete. This brief does not silently move every upstream pipeline.

Build a common IRPT Gold contract, parameterized by firm and fed by the three vendor adapters. Proposed logical tables are:

| Gold table | Grain / purpose |
|---|---|
| `account_census` | Every firm account as of a source date/revision, status, source presence, and coverage |
| `relationship_account` | Dated relationship-to-account membership |
| `account_holdings` | Unique custody position by account/date/revision, quantity and observed value |
| `model_membership` | Position/allocation/account membership evidence, effective dates, model identity, supported attribution granularity |
| `model_attribution` | Reconciled observed holdings/value classified by model status, with unresolved reasons |

Reuse an existing canonical fact when its grain and completeness satisfy the contract; do not duplicate valuation engines. Gold remains typed **Parquet**, retaining available history and explicit corrections. The UI remains a current snapshot; historical storage exists to reproduce that snapshot, not to expand the requested interface into historical model analytics.

The publisher is the only producer of served **Platinum JSON**, and it reads accepted Gold Parquet. It produces account model/holdings views, relationship summaries, and a lightweight paginated registry. Prefer bounded account/relationship projections and indexes over transmitting an entire firm's large snapshot to every viewer. Server-side scope resolution selects authorized accounts and recalculates selected-set weights.

Illustrative addresses generated by the current naming builder:

```text
s3://opal-data-49financial/irpt/49financial/gold/account_holdings/
  date=2026-09-22/account_holdings_20260922.parquet

s3://opal-data-cottonwood/irpt/cottonwood/platinum/model_holdings/
  account_id=A-EXAMPLE/model-holdings.json

s3://opal-data-inflection/irpt/inflection/state/publication/
  run_id=RUN-EXAMPLE/manifest.json
```

These are naming examples, not existing datasets. Final table schemas, partition/revision rules, and registered producer identities belong in the implementation contract. Current serving objects can use stable keys only if their exact object versions are retained and referenced. A publication manifest points to one complete accepted revision set; it must not combine account files from different runs.

## 4. A common report lifecycle in `opal-data-irpt`

Preserve the conceptual separation of intake, request revision, generation attempt, report, and export from the existing YCharts layout. Use product-first, firm-scoped addressing rather than copying the old `firms/{firm}/...` tree unchanged.

**Proposed logical families, subject to the reporting-artifact placement policy above:**

```text
s3://opal-data-irpt/irpt/{firm}/state/
  inputs/{input_id}/...
  requests/{request_id}/revisions/{revision}/...
  performance_reports/{report_id}/revisions/{revision}/...
  analysis_reports/{report_id}/attempts/{attempt_id}/...
  exports/{export_id}/revisions/{revision}/...
```

IDs, not client names, identify paths. These are logical workflow layouts; concrete partition columns, leaves, and builders must be registered before use. The current `address()` still places such FIRM state in the firm bucket. No code may bypass that result by concatenating an alternate bucket.

Each report revision should bind the verified owner/firm, exact selected account set or prospect input, input/source revisions, dates, parameters, provider result, normalized report, schema/adapter versions, coverage, and content hashes. A server-owned index resolves opaque report IDs to authorized object versions. The browser never supplies an arbitrary bucket/key as authority.

Reuse `irpt-requests`, `irpt-jobs`, `irpt-outbox`, and `irpt-checkpoints` where their keys/contracts fit. Define report-history queries/indexes explicitly; an S3 folder listing is not an advisor's authorized report history. Persist accepted work before dispatch, use a durable outbox and conditional job transitions, and distinguish interrupted/uncertain attempts from ready reports. S3 holds retained bytes; DynamoDB holds authoritative process state. S3 versioning is not a substitute for leases or transaction boundaries.

## 5. Per-function behavior

**Performance Reporting.** Resolve the exact selected accounts and period, then obtain the provider-calculated result from Black Diamond or Orion. Store the request parameters and original provider response evidence with the normalized immutable PerformanceReport. Preserve return methodology, units, actual coverage and requested/actual dates. Do not derive household performance by averaging account returns. Refresh creates a new report revision; export does not rerun the vendor calculation.

**Sensitivity Analysis.** Lane A freezes selected actual custody positions from an accepted firm-data revision. Lane B preserves a CSV upload and its preview/corrections under the user's verified firm/advisor ownership, without inventing a client relationship. Both converge on one normalized-portfolio contract. Retain amount units, dated prices/reference notional where applicable, security resolutions, and row dispositions. Then persist recipe/settings/comparisons, durable execution, original YCharts PDF, certified sections, and the displayable AnalysisReport. A downloaded PDF and a certified native report are distinct release states. Prospect account data does not enter the client model census unless the prospect is separately onboarded as a client.

**Model Overlay.** Read published firm Platinum derived from complete Gold; do not invoke YCharts or a performance endpoint. Return selected-scope dollars, weights, model/non-model/unresolved classifications, source dates, and account/security drilldowns. Missing overlay data affects attribution coverage without removing custody ownership. The backend is firm-complete even though each viewer receives only the authorized subset.

**Exports.** Freeze the exact report revision, included narrative/disclosures, branding assets and renderer version into `bundle.json`; write the validated PDF and receipt under the export revision. The receipt identifies the report, bundle, output hash and object version. Download rechecks entitlement. A branding change may create a new export revision without recalculating the financial report.

## 6. Publication, operational controls, and migration

Build only from declared completed source revisions. Carry custody and overlay dates separately, and report freshness honestly when one lags. Record account/position counts, independently reconciled values, missing mappings and source completeness in a run manifest outside the data tiers. Publish only accepted outputs, then atomically advance the release reference. Keep a previous accepted revision explicitly stale if a new run fails; never relabel it current.

Provision the proposed reporting store through infrastructure code with KMS encryption, versioning, blocked public access, TLS enforcement, and per-firm/purpose permissions. Define retention and expiry by artifact class under the records policy; synthetic proofs, transient attempts, raw inputs, and final client reports do not automatically share one retention period. Credentials/session cookies remain in Secrets Manager. Synthetic research remains visibly separate from production report history.

Treat migration as a mapped, bounded cutover coordinated with IRPT backend/frontend owners and the existing client-bucket/LGIC migration owners. Inventory every producer, reader, object reference, IAM grant, and status/download route. Preserve byte identity of historical evidence, record old-to-new version mappings, and retain existing report IDs. Repoint new writes and their readers as one change; no standing dual-write, shadow report store, or indefinite old-path fallback. Any same-window rollback copy is explicitly bounded. Preserve caller URLs where practical.

Do not delete or repurpose all of `opal-data-ycharts` merely because IRPT changes homes: establish every remaining consumer first. The current research objects may remain as historical evidence until their migration/retention disposition is recorded. The legacy short-form firm buckets similarly remain existing-system dependencies until their coordinated cutovers; this brief does not authorize estate-wide retirement.

## 7. Completion order and product acceptance

1. Register the proposed IRPT product scope and reporting-artifact destination policy, with the precise shared-bucket tenancy treatment; map current-to-target firm/output addresses using the canonical builders.
2. Complete each firm's account/position census and model membership; repair the known SmartX duplicate, Eclipse shared-portfolio, and Cottonwood target/weight defects.
3. Produce reconciled Gold history and complete Platinum current views for all three firms, then connect registry and authorized selection.
4. Connect durable performance and sensitivity request/result storage and retrieval, including both sensitivity input lanes.
5. Connect exports to frozen report revisions; prove migration, recovery, and protected retrieval through the deployed API/UI path.

Acceptance requires all source accounts represented or explicitly accounted for, including entirely non-model accounts; repeatable totals at account, relationship, and selected-set grain; no duplicate contribution from shared portfolios/multiple sleeves; transparent unknown values and attribution; no cross-firm reads/writes; reproducible report/export revisions after refresh or restart; and no dependence on the user's browser remaining open. Source freshness and genuine zero holdings must be distinguishable from failed ingestion. Builder-generated addresses and declared storage policy must agree with actual AWS writes.

## Supporting references and evidence

- `infra/logic/02_DOCTRINE.md`: R1-R7, R9-R15, R18-R22; source-first keys, firm tenancy, Parquet/JSON boundaries, state, and bounded migration.
- `org/standards/NAMING_SCHEMA.json`; `infra/logic/registry/{scopes,systems,tiers}.json`; `lib/opal_naming.py`.
- `.runtime/codex-seats/4.0.0_SA_CRO/irpt_backend_lgic_evidence_20260922.json`: actual builder output, bucket HEAD checks, missing IRPT scope row. Name generation proves addressing behavior, not dataset or IAM readiness.
- `IRPT_STORAGE_STATE_AND_END_STATE_20260922.md` and the three function briefs in this deliverables directory, with their dated audit/probe evidence.
- `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md`; current `core/layout.json`, `core/s3.tf`, and export/generation storage implementations. The new product bucket and LGIC paths are proposed changes to that implementation, not a restatement of current deployment.

## Andrew-direct requests — verbatim record

Channel: user messages to Codex seat 4.0.0_SA_CRO, September 22, 2026; exact message timestamps unavailable. Recorded during the 4 PM Eastern design review.

> ok now write one more brief that covers the appropriate backend for reporting. i would recommend a similar structure to opal-data-ycharts, maybe opal-data-irpt. the model backend should cover all client accounts per firm and be stored in the respective  client buckets in LGIC form.

> include both of these briefs in the folder that holds the initial three in relevant folders with relevant evidence.
