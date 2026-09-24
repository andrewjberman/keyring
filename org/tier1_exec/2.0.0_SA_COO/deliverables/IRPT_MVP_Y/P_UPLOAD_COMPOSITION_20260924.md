# Upload hops 2 and 3: the exact composition patch for 2.0.0_SA_COO~P (RESOLVE_UPLOAD, CTO 100667 shape 2)

Author `2.0.0_SA_COO~Y`, 2026-09-24 ~18:45Z, hop 3 added ~19:05Z. COO_Y.md asks Y for "literal runtime
installer/caller code ... plus exact shared patch/resource requirements and acceptance command". This is that for hops 2
and 3.

## What P applies, in order

1. Cherry-pick the three Y commits (`intake/**` and `ycharts/**` are Y's surface):
   - `bb1eb7f92b`: both halves of RESOLVE_UPLOAD (`intake/uploads.py`, `intake/upload_resolution.py`,
     `ycharts/generate/resident_worker.py`, and two test files).
   - `10a16bd89d`: the attribution fix. Without it every partner upload through `InteractiveAccess` refuses
     `UPLOAD_ACTOR_ATTRIBUTION`.
   - `d16b7c8743`: `load_input_owner` / `input_owner_lookup`, the retained-input owner lookup for hop 3.
2. `git apply P_UPLOAD_COMPOSITION_20260924.patch` (this folder). It touches only P's
   `reports/generate_installed.py` and its test. `git apply --check` passed against the P worktree at `f9c91a554d`.
   - **Hop 3:** `compose_ports` now installs `uploads(access, stores)` (Y's deferred service over the request's
     repositories) and `load_prospect_owner = input_owner_lookup(DynamoReportIndex(table))`.
   - **Hop 3:** `RoutedSubmissionService` routes an `input_id` body to Y's `ProspectSubmissionFactory`.
   - **Still absent, refused by name:** `get_catalogue` (`COMPARISON_CATALOGUE_REQUIRED`, NOT_READY; an Overview reads
     none) and `ordinary_authorizer`. For the latter, `_ordinary_viewer_not_composed` returns False, so partner
     viewers are refused.
   - **Hop 3 BLOCKER, owned by P (Y 100842, M 100846):** `ProspectSubmissionFactory` passes M's viewer-seam arguments
     (`get_organization`, `input_owner`, `current_viewer`, `authorize_viewer_input`) to `_scope/maintained_sources.py`.
     P's served file does not accept them: M's `485b69c061` was dropped by a merge. The patch's strict-xfail test
     `test_hop3_the_maintained_sources_accept_the_arguments_the_prospect_factory_passes` flips to XPASS, and fails
     strict, the moment P restores the seam. Remove the marker then. M's acceptance for the restore:
     `_scope/tests/test_maintained_viewer_sources.py` 27 of 27.
   - It adds `compose_upload(ports, request, scope)`. Per request, that builds `InteractiveAccess` on the guarded
     prospect owner's storage firm, then `ports["repositories"](access)`, then Y's
     `deferred_upload_service(index, artifacts, access.authorize_current, table=index.table, send=ports["send"] to
     queue_url)`.
   - The upload route calls `upload_csv(..., resolve_principal=access.current)`. `authorize_current` admits exactly
     `access.current()`, so any other principal shape is refused.
   - The resident factory `reports/resident_installed.py` is unchanged: the assembly composes the resolution from its
     existing ports (`requests.artifacts`, `requests.authorize_current`, `session.template_resolver`).
3. The package rebuild and deploy of `irpt-ycharts-generate` and the resident go under P's ledgered plan and
   `safe-apply` (NEVER-2 entry).

## Acceptance command (offline, P's tree after steps 1-2)

```
cd infra/aws/lambda/investor-reporting
python -m pytest -q -p no:cacheprovider reports/tests/test_generate_installed.py intake/tests/test_deferred_resolution.py ycharts/generate/tests/test_resolve_upload.py
```

Measured in Y's scratch worktree at P `aa3aabe2ca` plus steps 1-2, three suites: 27 passed, 1 xfailed (the hop-3
blocker above), 1 failed. The new tests cover:
- a template upload answers RESOLVING and sends one `resolve_upload` message;
- without the ordinary authorizer a partner upload is refused and writes nothing;
- the prospect factory composes from the real ports;
- the owner lookup returns a resolved input's owner and refuses unknown and malformed ids.

On `_contracts/test_upload_contract.py` plus `reports/tests`, P's own tip fails 4 (84 passed). Scratch fails the same
4 (88 passed, 1 xfailed), so the patch adds no failure:
- `test_generate_installed.py::test_the_two_revisions_are_derived_never_typed` (expects 22 schemas; the tree holds 23);
- `test_currency_authority.py::test_attested_denomination_is_separate_from_vendor_currency_and_detached`;
- two in `test_status_installed.py`.

## Grants the live run needs (P's ledgered plan; addresses from `lib/opal_naming.py` builder output, never typed)

| Role | Action | On |
|---|---|---|
| `irpt-ycharts-generate` | `dynamodb:GetItem`, `dynamodb:PutItem` (conditional) | irpt-requests rows `UPLOAD#`, `NORMALIZATION#`, the artifact index and retention rows of family ORIGINAL_HOLDINGS |
| `irpt-ycharts-generate` | `s3:PutObject`, `s3:GetObject`, `s3:GetObjectVersion` (+ KMS if the destination is encrypted) | the X10 reporting destination for family ORIGINAL_HOLDINGS |
| `irpt-ycharts-generate` | `sqs:SendMessage` | irpt-generation (CTO 100667 (2) says the role already holds it) |
| resident instance role | `dynamodb:GetItem`, `dynamodb:PutItem` (conditional on `state`) | irpt-requests rows `NORMALIZATION#`, `UPLOAD#` (read), `INPUT#`, the artifact index and retention rows of family NORMALIZED_PORTFOLIO |
| resident instance role | `s3:GetObject`, `s3:GetObjectVersion` for ORIGINAL_HOLDINGS; `s3:PutObject` for NORMALIZED_PORTFOLIO (+ KMS) | the X10 reporting destination |

The policy registry must list ORIGINAL_HOLDINGS and NORMALIZED_PORTFOLIO as families, or `ArtifactRepository.put`
refuses them.

## What stays refused, by name

- **An ordinary (partner) viewer is refused** until `ports["ordinary_authorizer"]` has a producer. A verified Opal
  viewer (Andrew's first submission) is admitted.
- **The legacy `csv_base64` lane** answers NOT_READY `CSV_LANE_NOT_COMPOSED`.
- **A SHARES template** resolves to NEEDS_CORRECTION `SHARES_PRICE_SOURCE_NOT_COMPOSED`.
- **Hop 3** is composed by this patch. It raises `TypeError` at `resolve_profile_fields` until P restores M's viewer
  seam. After that, an Opal viewer's Overview on the resolved `input_id` is EXPECTED to reach acceptance and the queue.
  That is inferred: no offline run gets past the seam today. A comparison refuses `COMPARISON_CATALOGUE_REQUIRED`.

## Live acceptance (after the deploy)

1. Andrew posts the 12.03 template (AAPL 10.01, VNQ 2.02, Dollars) from the Analysis screen. The POST answers
   `RESOLVING`.
2. The resident's journal shows one `IRPT_RESIDENT_POLL handled=1`. The `NORMALIZATION#` row reads `NORMALIZED` with
   an `input_id`.
3. The re-POST answers `NORMALIZED`, with `portfolio.holdings.total_dollars == "12.03"`.
