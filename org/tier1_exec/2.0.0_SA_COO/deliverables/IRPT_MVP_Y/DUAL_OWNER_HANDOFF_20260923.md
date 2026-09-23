# Y acting-submitter and retained-input handoff

Source `1385a126e7d9bbc9b4fe211cc708a52a93ce64e6`, branch
`irpt-mvp-y-20260922`, seat `2.0.0_SA_COO~Y`, 2026-09-23T18:14Z.
LOCAL. Origin CLOUD measured `365ab567ba1250a6a3569df38cb75d12fe2e8d0e`;
no push, deployment, secret read or vendor call.

## Result and attribution

A verified Opal user can create a new analysis using a partner's or another
Opal user's retained prospect input. The accepted request owner and request ID
use the actual submitter. `resolved.input_owner` is exactly the original
normalized document's base owner. Original normalized bytes, artifact reference,
CSV, source digest and storage firm are unchanged. No reupload or impersonation.

Request IDs remain keyed by concrete input firm, actual actor and browser request
token. One concrete input firm is supported in this composition; Global is a
view context, never storage or a permission ceiling. New multi-firm economics
are not claimed. Recipe/settings descriptors bind the actual request owner;
M profile/comparison descriptors bind the original input owner, with actual
actor/home attribution in their actor-specific source scopes.

The service validates exact original retention owner and bytes before acceptance
and dispatch. Retry uses retained composition and reads no maintained profile,
organization or recipe source. Worker replay and retained date projection use
the original input owner while checking current access and accepted request owner.

## Exact combined source

| Owner | Source | Purpose |
|---|---|---|
| Y | `1385a126e7d9bbc9b4fe211cc708a52a93ce64e6` | Factory, acceptance/retry, frozen worker, dates, 20 paired controls |
| Y | `104d9472f1` ancestor | Actual Entry selected_tenant and ordinary upload principal compatibility |
| P | `37526d36aeb9a1299d0046355aa3c1e96e852b4f` | Closed composition schema/validator, repository.head compatibility |
| P | `9a3ec2a11f` | Trusted InteractiveAccess |
| P | `4ec461a2e9aa06b380592c43cffd03687e9f536a` | Actual guarded prospect/owner Entry |
| M | `485b69c061` | Viewer-aware maintained profile/comparison resolvers |

Y touched only these source paths below `infra/aws/lambda/investor-reporting/`:
`ops/prospect_dates.py`, `ycharts/generate/frozen_worker.py`,
`ycharts/generate/submission.py`, `ycharts/generate/submission_service.py`,
`ycharts/generate/prospect_submission.py`, and
`ycharts/generate/tests/test_prospect_submission.py`.
P schema, repository, Entry and M resolver files were extracted into `.runtime`
for testing; their tracked source was not overwritten.

## Runtime installation

`ProspectSubmissionFactory(*, acceptance, repositories, uploads, schema_directory,
get_user, get_partner_profile, get_organization, get_catalogue, send, queue_url,
ingestion_revision, destination_revision, ordinary_authorizer,
configuration=capture_configuration)`.

- `repositories(access)` supplies P retained repositories bound to this request's
  real `access.authorize_current`. `uploads(access, stores)` supplies Y UploadService
  with those repositories and the same current authorization.
- `get_user`, `get_partner_profile`, `get_organization` are installed canonical
  reader methods; the factory invents no source rows or clients.
- `ordinary_authorizer(request, viewer, retained_owner)` is the existing server
  policy adapter, mandatory. Test permissive callbacks are not runtime defaults.
- Entry scope supplies `current_owner` as the real viewer and `prospect_owner`
  as the original retained base owner. The new service verifies both.
- `build_prospect_entry(*, load_prospect_owner, **ports)` returns the existing
  guarded Entry with this service explicitly installed. P remains runtime writer.
- `FrozenCompositionWorker.prepare/recipe_inputs(viewer, request_id, *,
  data_firm=None)` now permits explicit retained partition with unchanged viewer.

M calls are exactly `resolve_profile_fields(..., input_owner=base_original,
current_viewer=access.current, authorize_viewer_input=authorize_exact,
get_organization=canonical_reader)` and equivalent comparison keywords. The
callback re-reads exact original input/retention before its final policy check,
with stable viewer checks before/after; the reader retains its own access gate.

## Measured tests

Generation suite: **232 passed, 32 subtests**. Ops: **179 passed**. Intake:
**93 passed, 18 subtests**, initially one missing-env skip; exact pinned-reader
`test_custody_portfolio.py` rerun: **39 passed**, resolving that skip. Combined
unique coverage is **505 tests / 50 subtests**, with no outstanding skipped control.
Code commit gate passed all six files after fixing test import lint.

The 20 new controls pair real P storage/admission/Entry and real M resolution
with offline AWS-shaped storage and profile source fixtures. They cover both
original creator classes, distinct actual request identity, frozen retry,
worker recipe replay, retained source dates, original retention-owner tampering,
expiry before acceptance and after acceptance/before dispatch, ordinary/service/
untrusted/changed actors, and actual guarded Entry acceptance. Actual canonical
organization SDK requests are asserted through Stubber when building the fixture.
Queue lease/delivery and live vendor generation are explicitly not established.

Reproduce from the Y worktree with these byte-exact extractions:

- `IRPT_DUAL_OWNER_TEST_ROOT=.runtime/dual-owner`: M485 `maintained_sources.py`;
  P375 `request_composition.py`, `repository.py`, `retention.py`; all P375
  `docs/contracts/investor-reporting/v1/*.json` under `schemas/`.
- `IRPT_INTERACTIVE_ACCESS_TEST_ROOT=.runtime/interactive-access-9a3ec2a11f`.
- `IRPT_INTERACTIVE_ENTRY_TEST_ROOT=.runtime/entry-4ec461a2e9`.
- `IRPT_INTERACTIVE_STORAGE_TEST_ROOT=.runtime/storage-dd6edfc3aa` for older ops
  fixture controls, which retain their own prior exact pin.
- `IRPT_ACCEPTED_READER_TEST_ROOT=.runtime/custody-reader-8845b7ef23`.

The committed fixtures assert source hashes. Run generation, ops and intake
test directories separately with `python -m pytest <directory> -q`.

## Next owner and live boundary

P consumes this exact combined candidate and installs real ports/package wiring.
CTO is direct reviewer under `f50aff2ce1`; no additional CVO gate is introduced.
Andrew confirmed the bounded Global/Select Firm and investor-list bootstrap
symptom. Full browser continuity, selection/account drilldown, queue/vendor and
report/export journey remain unproved by this handoff. CLOUD push remains held.
