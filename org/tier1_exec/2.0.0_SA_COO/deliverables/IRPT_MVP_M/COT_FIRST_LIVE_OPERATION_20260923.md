# Cottonwood first live Holdings operation

M owns producer, native publisher, Holdings API/UI assembly. P owns shared runtime
packaging/IAM and retains its writer claim. This preparation does not depend on X10.

## Prepared producer operation

Source candidate here adds the selected-account operator option and refuses any
existing accepted index before reading sources on a bounded initial upload. It uses
actual custody business_date2026-09-22 for publication, separately from source cutoff
2026-09-23 and overlay date. No relabeling an older custody date as current.

Validated dry-run (real S3, no cloud writes):
```powershell
python data/assets/scripts/gold/investor_reporting/holdings_snapshot.py --firms cottonwood --as-of 2026-09-23 --account-id acc_d486fc9455d6b2aa18e13af1 --dry-run --local-out .runtime/holdings-journey-20260923/publication-prepared
```
Output:59nodes/57securities/1account, USD19705844.84, independent reconcile and schemaPASS.
Gold Parquet and canonical JSON prepared locally. See COT_PREPARED_PUBLICATION_20260923.json.
The later actual invocation is identical except --upload replaces --dry-run. It captures
current index first, builds from version-bound sources, verifies all uploaded versions/hashes,
and conditionally accepts manifest last. It refuses if a prior index appears.
Local dry-run revision changes when the next invocation captures a new as_of_timestamp;
source version/hash receipts and schema/economic controls remain mandatory on that invocation.
No blind retry after ambiguous final-index PUT; inspect exact index version/readback.

Canonical target from builder: opal-data-cottonwood,
irpt/cottonwood/{gold,platinum}/holdings/date=2026-09-22/ with revision-named artifacts;
index irpt/cottonwood/platinum/holdings/current/manifest.json.
Readiness measured live: bucket versioning Enabled, accepted index absent.
One-account scope is declared explicitly; other accounts remain unavailable, never silently
included. Initial-publication command cannot replace existing firm-wide accepted state.

## Installed runtime finding and precise P integration delta

COT_HOLDINGS_INSTALLED_RUNTIME_20260923.json records current deployed Lambda bytes:
September21 CodeSha256 1XkzWP6p8OfobrSCI8ZrRCyMxfWgSK6sPZeYjdON50I=.
Only15zip entries, no publication.py or retained selection modules. Environment lacks
IRPT_REQUESTS_TABLE. Live role has only legacy GetObject/ListBucket plus logs;
no GetObjectVersion or DynamoDB selection read. Publishing data alone cannot fix this.

Use P's already authored current holdings package/IAM/lambda declarations@5765ea21a5,
including exact M entry/snapshot/publication files and e5604c03 UI drill changes.
P source has IRPT_REQUESTS_TABLE, contracts at /var/task/contracts, registry at
/var/task/firm_registry.json; compiled desired IAM includes current selected request
read and native index/version reads. Reuse these exact changes, no duplicate patch
or manual environment edits by M. P supplies final package checksum plus never-widen
scoped Terraform/apply/rollback packet under its existing integration ownership.
Compare final installed package digest and only required native firm prefix/current
selection grants; the Lambda remains a reader, never publisher/source vendor client.

## Required execution and observed acceptance

CTO reviews this exact bounded native publication and P runtime packet through existing
release prerequisites. No scheduler activation. M executes the admitted producer operation,
loads accepted manifest by exact receipt, then drives a real-login request on the shared
account through current server grants/retained selection. Confirm Models/SMAs/Client,
USD19705844.84,57security rows, percentages and both clocks; refresh/reopen keeps the
accepted revision and authorization. Prior broader/no-grant cases remain refused.
M owns this observation and reports actual browser evidence, not P's status message.
The first COT thread is a milestone; INF/49F and richer model-membership cases remain.
