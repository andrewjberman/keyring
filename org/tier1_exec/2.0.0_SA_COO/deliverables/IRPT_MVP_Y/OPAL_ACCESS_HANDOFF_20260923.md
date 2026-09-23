# Y actual-viewer adapter handoff

Production source: `85af5eb95d72051c363727229981c4dc1a35cad9`; paired test pin
`4ea95d1117` (descendant) on `irpt-mvp-y-20260922`.
Controlling access ruling: `5ad99c7d30`. Consumed P interface: `9a3ec2a11f`.
This implements Y's bounded consumer changes; shared Entry wiring and
signed-in live acceptance remain P-owned dependencies. No CLOUD push or deployment.

## Changed behavior

The actual viewer reaches current authorization and storage callbacks unchanged.
Stored creator, accepted tenant, immutable composition/report references and
retention checks remain intact. Request history filters each row through current
authorization, and rechecks all candidates after artifact I/O. Opal prospect
owners are validated as prospect descriptors instead of being forced into custody.
The parser/freezer keeps exact dollars, real home organization, concrete storage
firm and null advisor; no partner identity is synthesized.

New uploads name the current actor. Passing another creator to `create` refuses
impersonation; `read_input` can read that creator's retained input when P's trusted
callback permits it. New submission of someone else's input still needs the
shared resolver/schema to preserve both acting submitter and input attribution;
this handoff does not invent that composition contract or cross-firm economics.

## Exact ports

- `OwnedRequestReader.read(viewer, request_id, *, data_firm=None)`.
- `OwnedRequestReader.history(viewer, *, limit=25, cursor=None, data_firm=None)`.
- `OwnedAnalysisReader.read/sections(viewer, request_id, *, data_firm=None)`.
- `OwnedJobStatusReader.read(viewer, request_id, *, prospect_dates=False, data_firm=None)`.
- `RetainedProspectDates(requests, viewer, record, *, data_firm=None)`.
- `build_owned_entry(*, requests, reports, resolve_principal=None, resolve_data_firm=None)`.
  Optional server callbacks take `(request, scope, event, ctx)`. Without a viewer
  callback, the adapter consumes `scope.current_owner`; the new home-bearing
  viewer is preserved whole, while the older ordinary two-field port remains
  compatible. The shared owner guard must also supply that actual viewer to its
  `authorize_record_owner` callback.
- `upload_csv(..., service, *, resolve_principal=None)` and
  `build_upload_entry(service, *, resolve_principal=None)`. P should supply
  `lambda request, scope, event, ctx: scope['current_owner']`, or populate
  `current_owner` for the default adapter. `prospect_owner` remains separate.
  An Opal upload without an actual-viewer port is a missing-capability error.

Explicit `data_firm` is the real storage partition, never a replacement viewer.
Global without placement raises `RequestStorageUnavailable` (`NotImplementedError`),
not an authorization denial. P's `InteractiveAccess.prospect_owner(storage_firm)`
supplies explicit server-selected upload placement. No first-firm fallback or
Global storage partition exists. Global fanout must retain per-firm cursors and
attributed results; this change provides individual firm pages, not aggregation.

Cross-firm Y reads now pass `data_firm=...` to P artifact `head/get`, report `get`
and retention `require_live`. Same-firm calls preserve old signatures. Upload and
submission writes already carry explicit stored owners; P must remove their
pre-authorizer viewer-firm equality checks too. No fallback retries after a
`TypeError`, creator substitution or permissive production callback is installed.

## Measured evidence

All suites run separately from the Y worktree:

| Command suffix after `python -m pytest` | Result |
|---|---|
| `infra/aws/lambda/investor-reporting/ycharts/generate/tests -q` | 212 passed, 32 subtests |
| `infra/aws/lambda/investor-reporting/intake/tests -q` | 94 passed, 18 subtests |
| `infra/aws/lambda/investor-reporting/ops/tests -q` | 173 passed |

Total 479 tests and 50 subtests, no skips in final runs. Set
`IRPT_ACCEPTED_READER_TEST_ROOT` to byte-exact `.runtime/custody-reader-8845b7ef23`
for the first two suites. Set `IRPT_INTERACTIVE_ACCESS_TEST_ROOT` to
`.runtime/interactive-access-9a3ec2a11f` for ops. Its module is extracted from
`9a3ec2a11f:infra/aws/lambda/investor-reporting/_scope/interactive_access.py`;
SHA256 `bba07a3f4eeb947bf33845653bde95d47bbb8037d65db4059f4f8b70ebabdf56` is asserted.

Sixteen new paired controls use the real P viewer predicate. They cover Global,
another selected firm, foreign creator, per-firm cursors, ordinary/forged/service
refusals, final actor change, explicit placement, Opal CSV creation/retry,
immutable attribution and prospect composition. The initial Global controls use
labeled port doubles. Four additional controls pair the actual P storage source
`dd6edfc3aae94bfcb85cd5ed573e81977c58f9f0` with Y: real repository/retention
implementations and offline Dynamo/S3 exercise Global, different selected firm,
same firm, foreign creator, reports/sections/history/status/date evidence, upload
creation/retry, retained input read, expiry and identity change during blob I/O.
Set `IRPT_INTERACTIVE_STORAGE_TEST_ROOT` to `.runtime/storage-dd6edfc3aa`.
Extract `reports/repository.py` and `reports/retention.py` from the exact P pin;
their SHA256s are asserted in the committed fixture. These classes are loaded
under isolated module names; no P-owned tracked source is overwritten.
The custody-descriptor refusal now tests descriptor/lane mismatch rather than
an Opal-wide prohibition. The report schema assertion uses the existing
canonical `opal://` reference; no response schema was changed.

Commit gate passed for all 13 changed files. Historical shared Entry tests still
exercise old scope bytes and cannot establish compliance with the new access
ruling. The direct adapter controls do not prove live HTTP access.

## Next owner and exact dependency

P subsequently supplied implemented storage source in its `20260923T174506Z`
message. Y consumed it and the paired storage checks pass at `4ea95d1117`.
P's shared Entry current-owner/prospect-owner wiring is still pending while
its authorized first-hop apply proceeds under CTO `e186d7ea22`. Y has performed
no apply or cloud action. P should consume the Y source and paired evidence,
then return the exact Entry candidate for signed-in path validation.
The first-hop live milestone retains priority; deeper custody work stays parked.
CTO is the current direct reviewer. CLOUD push remains held.
