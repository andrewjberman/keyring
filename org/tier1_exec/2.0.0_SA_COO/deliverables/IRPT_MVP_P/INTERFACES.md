# IRPT P shared interfaces - candidate v1

Owner: `2.0.0_SA_COO~P`. Authority: CTO completion CONTRACT v1.1 at `9b99dc12cd`.
Status: proposed producer/consumer agreement, not a deployed interface. 2026-09-22.
Source baseline: workspace `1ca9d3edfecaeead06ef1286df4354098f0f0885`, portal
`7dd3d067a17ee00b878ecfceff23c557649a2331`. B/F final integration pins still owed.

## Report repository (S4)

Proposed module: `infra/aws/lambda/investor-reporting/reports/repository.py`.
P implements this module and durable adapters. Y owns request acceptance, outbox,
job transitions, attempt identities and certification. Publication cannot mark a
job READY: Y does that only after a successful repository receipt and certification.

```python
repository.persist(owner, report_kind, request_ref, report, provenance)
# -> {report_id, revision, report_kind, sha256, immutable: True}
repository.get(principal, report_id, revision)
# -> {ref: <receipt>, report: <unchanged typed document>, provenance: <frozen context>}
repository.list(principal, report_kind=None, cursor=None, limit=25)
# -> {items: [<receipt>], next_cursor: <opaque token or None>}
```

`report_kind` is `PERFORMANCE` or `ANALYSIS`. The report is the existing v1
PerformanceReport or AnalysisReport; no additional top-level wire properties
are inserted into either document. Existing `request_ref`, `release`, units,
dates and section meanings remain Y's. P validates the declared report schema.

`owner` is resolved on the server, not accepted from a browser body:

```json
{"firm_id":"<canonical registry firm>","principal_id":"<verified stable principal>",
 "account_ids":["<canonical selected account>"],"prospect_input_id":null}
```

For prospects use `account_ids: []` and the issued `prospect_input_id`.
Do not create fake client/account IDs. Exactly one ownership basis is required.
M supplies principal/firm binding and selected-account resolution. The repository
receives a required current-authorization callback; missing callback fails closed.
Persist validates ownership. Get and every listed item recheck current access;
having possessed a report ID or old entitlement revision does not grant access.
An account report is readable only when its entire selected set remains permitted.
Prospect reports require current access to the firm-bound input owner.

`request_ref` is the server-owned immutable request/attempt identity. Y supplies
its existing `{request_id, request_revision, attempt_id, attempt_number}` object.
P's performance entry issues its own request identity. An identical publication
retry resolves to the same report/revision; different bytes never overwrite a
previous revision. Refused writes must not create a READY index entry.

`provenance` freezes selected/input reference and hash, source revisions,
schema/adapter/recipe versions, coverage and source evidence references. Values
must be JSON-compatible and finite; hashes use canonical JSON with no NaN/Infinity.
Raw vendor documents are retained separately through the registered destination
and referenced by immutable version plus digest. Credentials are never artifacts.

Durable composition reuses S3 for immutable bytes and the existing tenant-keyed
`irpt-requests` table for a separately prefixed report index. Conditional publication
occurs after persisted bytes have a verified hash/version. No S3 listing serves
history. M's registered destination builder supplies addresses; P will not invent
an alternate bucket while the reporting-artifact policy is unresolved. The first
module tests will be network-free with persistent adapter test doubles; that is
not deployed acceptance.

## Analysis producer and reader example

```python
receipt = repository.persist(
    owner=resolved_owner,
    report_kind="ANALYSIS",
    request_ref=certified_report["request_ref"],
    report=certified_report,
    provenance={"input_ref": frozen_portfolio_ref,
                "recipe_version": recipe_version,
                "source_evidence": [vendor_pdf_version_and_sha256]})
# Y records receipt in its conditional job transition before publishing READY.
saved = repository.get(current_principal, receipt["report_id"], receipt["revision"])
# Actual sections endpoint returns saved["report"] as envelope.data, not job status.
```

Y must retain the report reference in durable job state and pass it to the sections
reader. P will provide immutable blob persistence primitives alongside the repository
for Y's frozen input and original PDF; Y retains its own lifecycle semantics.

## HTTP and frontend integration (S5)

P integrates `portal/src/api/endpoints/investor-reporting.ts`,
`portal/src/pages/InvestorReporting/contracts/adapt.ts` and shared route/schema
aggregators. Y/M send exact function patches and paired request/response examples.
Each response stays `{contract_version, operation, firm_id, data, status}`;
`data` is the declared typed report, never `{report, diagnostics}`. Status and
source dates must survive the browser adapter. Diagnostic coverage belongs in
declared report/status fields or protected evidence, not a new response wrapper.

New report-history HTTP route names and generated contract extensions will be
published after owner agreement. The Python interface above permits Y's worker
and sections reader to progress without inventing a browser route.

## Frozen export input (S6)

```json
{"report_id":"<issued report ID>","revision":"<immutable revision>",
 "report_kind":"ANALYSIS","selected_sections":["<existing section ID>"],
 "brand_revision":"<approved revision>","narrative_packet_ref":null}
```

This is the requested reference, not an arbitrary object path or an inline
replacement financial report. P's server assembly reauthorizes and loads the exact
repository revision, then feeds the existing `export/bundle.py:freeze` and export
controller. `authorized_report_revisions` retains report_id/revision/immutable and
the bundle includes the corresponding frozen payload. Export never invokes a
provider or substitutes start=end=business_date. Analysis and performance use the
same assembly. Approved assets, renderer/template/disclosure versions and optional
narrative are frozen; receipt binds report revision, bundle/PDF hash and S3 version.
Protected download checks current access. Existing B/F render-chain repairs and
provisioning gates remain. This example is an assembly seam, not an implemented
new public request schema.

## Requested peer decisions

- Y: confirm request_ref remains the existing AnalysisReport request_ref, return
  exact frozen-input/PDF blob operations needed, and send candidate sections response.
- M: supply verified principal/owner and reauthorization callback shape, selected-set
  reference resolution, dated SmartX/BD crosswalk and registered artifact destinations.
- P: implement the agreed seam, publish tests and candidate pin before callers integrate.

No acceptance ID is complete merely because this interface has been published.
