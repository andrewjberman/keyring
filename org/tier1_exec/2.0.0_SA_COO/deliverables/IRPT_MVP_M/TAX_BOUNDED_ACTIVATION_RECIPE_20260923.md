# Tax membership: bounded existing-module activation request

For CTO path/runtime adjudication; M does not edit outside current grant.
Inspected CLOUD6afa8a105cef1c59240b8aace427ec09ada5b0b9 plus exact historical
source pins6abf60e5d5/bc5efb655d/f96d5f6cd4. No new token owner or Tax project.

## Exact existing chain and actual gaps

Gateway app/taxsma_workbook.py is registered before generic /ms routes in server.py.
GET /ms/taxsma-workbook accepts no query/body/identity selectors. It uses the distinct
TAXSMA_WORKBOOK_BEARER and validated broker principal TAXSMA_WORKBOOK_IDENTITY.
Never substitute generic ingestion credentials or research snapshot JSON.

Existing data/mdpf/scripts/gold/taxsma_snapshot.py exposes
make_default_gateway_call(base_url,capability_bearer), acquire(call,S3BronzeStore(s3)).
It retains original body bytes with conditional creation; never create a guessed envelope.
Existing data/mdpf/scripts/silver/taxsma_workbook.py exposes
build_silver(bronze_reader,bronze_address,response_sha256,S3SilverStore(s3)).
The canonical response metadata, all21 rows and typed business scalars remain intact.
Existing gold/taxsma_membership.py classifies original typed rows and emits first-observed
UTC dispositions. Its S3DispositionStore append/events_for still raise NotImplementedError.
Current gold/mdpf_gold_consolidator.py run_taxsma_prelude defaults to LocalBronzeStore,
LocalSilverStore and LocalDispositionStore. Its live caller supplies only gateway_call,
with no production stores or actual custodian_records/base_population/canonical_rows.
Therefore enabling TAXSMA_GATEWAY_BASE_URL/TAXSMA_CAPABILITY_BEARER alone is insufficient.

## Smallest requested writer/activation delta

1. Grant one writer (M if CTO assigns) gold/taxsma_membership.py S3DispositionStore
and data/mdpf/tests/taxsma/test_taxsma_membership.py only: implement exact existing
protected dispositions object via conditional create/update, full read-back, idempotent
logical event IDs, same-observation conflicts and out-of-order protections. Reuse
LocalDispositionStore semantics; no new registry/storage plane or manual backdating.
2. A narrow one-shot runner under M existing investor_reporting source grant consumes
whole existing modules above. Supply explicit production stores; stop after membership
receipt. Do not enable the full Gold consolidator, category publisher or historical rebuild.
This avoids needing to change its broad integration while IRPT only needs membership.
3. Existing gateway owner validates configured delegated principal and distinct route-only
bearer. Existing runtime owner supplies the capability through the existing secret binding.
Do not echo credentials. M needs one exact capability read authorization/route deployment
assessment, not a new identity or broad Graph permission.
4. Runtime S3 permissions: GetObject/GetObjectVersion and conditional PutObject only
on canonical module-returned workbook Bronze/Silver objects and the existing protected
membership object; ListBucket only if that reader actually needs it. Check existing
KMS constraints, exact buckets, versioning and policy before activation. No hardcoded
new destination, no whole-prefix delete, no shared push.

## Executable callable sequence after the two missing runtime prerequisites

```python
call = taxsma_snapshot.make_default_gateway_call(base_url, capability_bearer)
bronze = taxsma_snapshot.S3BronzeStore(s3)
s02 = taxsma_snapshot.acquire(call, bronze, now=now)
# Abort on FailureResult; verify retained exact body/version/hash.
silver = taxsma_workbook.S3SilverStore(s3)
s19 = taxsma_workbook.build_silver(
    lambda: bronze.get_body(s02.bronze_address), s02.bronze_address,
    s02.response_sha256, silver, now=now)
table = taxsma_workbook.read_parquet_bytes(silver.get_body(s19.silver_address))
meta = taxsma_membership.file_metadata(table)
history = taxsma_membership.S3DispositionStore(s3)
rows = taxsma_membership.classify_rows(table.to_pylist(),
    previously_traded=lambda key: taxsma_membership.is_open(history, key))
count, reasons = taxsma_membership.compute_business_active_accounts(rows)
# Abort on unknown census; preserve complete source as evidence.
events = taxsma_membership.emit_dispositions_from_snapshot(rows,
    snapshot_id=meta['snapshot_id'], source_observed_at=meta['observed_at'], store=history)
# Read-back exact history version; resolve_date_status for actual custody date.
```

This is a concrete callable recipe, not an assertion that credentials or production
store implementation already exist. First fresh observation today cannot certify
September22 membership. Inception/last-trade/source-modified fields do not backdate it.
For each verified date/account M reclassifies identical custody value once from Client
to SMAs/ALT Strategies/Tax. It does not add workbook AUM to the0833 custody base.
Two workbook YES accounts absent custody remain explicitly uncovered.

## Acceptance and rollback

One authenticated capability response with stable ETag; original response SHA and
versioned Bronze/Silver readbacks; typed row census; first-observed membership receipt;
concurrent/idempotent/conflict controls; exact account/date join and unchanged custody
sum. No complete historical claim. On failure stop before Holdings acceptance; retain
immutable input evidence and last accepted history. Disable the one-shot invocation,
not delete history or restore a mutable prior history object. No full scheduler change.
