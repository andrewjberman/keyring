# M current interfaces

Source implementation: **485b69c061**. Controlling Opal ruling `5ad99c7d30`,
acting-submitter contract `e07a5ca692`, P implementation request175350 and Y
caller handoffs175601/180039. CTO is the reviewer. Prior source reviews and
proposal452b20dc07 are retained in [INTERFACES_HISTORY.md](INTERFACES_HISTORY.md).

## Maintained profile and empty comparison ports

```python
resolve_profile_fields(headers, input_ref, browser, *, get_user,
    get_partner_profile, authorize_input=None, registry_path=None,
    recipe_title_source=None, input_owner=None, current_viewer=None,
    authorize_viewer_input=None, get_organization=None)
resolve_comparison_fields(headers, input_ref, comparison_keys, *,
    get_catalogue, authorize_input=None, input_owner=None,
    current_viewer=None, authorize_viewer_input=None)
```

`snapshot_profile_sources` accepts the same profile reader and authorization
ports. `snapshot_custody_profile_sources` and `resolve_custody_profile_fields`
retain positional original owner and add the same optional viewer callback pair.
The legacy two-argument `authorize_input(owner, ref)` mode remains explicit;
partial new ports or mixing modes refuses. No permissive fallback.

The production invoking adapter is Y's
`ycharts/generate/prospect_submission.py::ProspectSubmissionFactory.submit`.
P installs it with real repositories, upload and canonical profile readers.
Y passes the original normalized document.owner base prospect-owner-v1 (not the
repository-augmented account_ids/prospect_input_id shape), exact read_input
receipt, and request-local `InteractiveAccess.current`.

`authorize_viewer_input(viewer, original_owner, input_ref)` must reload exact
retained bytes/owner/ref/placement/expiry, compare them, then apply current viewer
policy. It returns literal True only. The retained reader may enforce its own
access gate. M verifies detached owner/ref/viewer stability before/after callback
and before/after source reads; dictionary equality is not storage verification.
Y180533 reports repairing the early policy call flagged in M180451. This report
is not yet a combined acceptance/replay verdict.

## Attribution and frozen behavior

New preparation reads the actual viewer.principal_id and validates its active
canonical user/home firm. Opal uses get_organization(home_firm_id); ordinary
advisors use their actual partner reader and ordinary operations their own user.
A selected partner firm is never substituted for the Opal home organization.

Every M-generated source descriptor binding remains the original normalized
input-owner binding. User/organization/partner/browser source_scope identifies
actual actor/home; browser source_owner is the acting submitter. Input bytes,
reference, creator and placement remain unchanged. Optional contact absence
remains input-bound. ProfileSourceSnapshot carries viewer only as an internal
member; returned profile/profile_provenance/source_descriptors keys are unchanged.

Y recipe/settings descriptors retain actual concrete request-owner binding.
Optional recipe_title_source in viewer mode must match that actual actor binding
and its actual source scope (or unscoped configuration), with a valid projection
digest. It is not rewritten into the original input creator. P owns shared schema
and validate_bindings changes distinguishing these two descriptor roles.

Frozen accepted composition must be replayed without invoking these resolvers.
M returns detached projections; Y owns retry/replay/final dispatch. Empty
comparisons reauthorize the exact input twice and read no catalogue. Nonempty
comparison capability remains unimplemented; no fabricated verification/entitlement.
Single-firm selection primitives, custody producer and publication are unchanged.

## Bounded evidence and integration

**61 tests plus45 subtests PASS** offline. Test overlay: git archive9a3ec2a11f of
infra/aws/lambda/investor-reporting and data/firm_registry.json, then copy M
maintained_sources.py and the two maintained-source test files. Real P
InteractiveAccess is used; canonical profile rows and retained storage are
fixtures. Run with PYTHONPATH containing _scope,_authz,_ids,_keys:

```text
python -m pytest -q _scope/tests/test_maintained_sources.py
  _scope/tests/test_maintained_viewer_sources.py _scope/tests/test_interactive_access.py
```

Checks cover Global/different-filter Opal using partner-created and Opal-created
inputs; actor attribution with unchanged input binding; actual InteractiveAccess
ordinary/forged/service refusal; input backing/ref/expiry changes before and
during preparation; actor change; inactive/wrong-home source; source projection
change; detached frozen projection; callback defensive copies; mixed/partial
ports; empty comparison retention; actual actor recipe binding; custody account
and snapshot attribution. No live/deployed or complete acceptance/replay claim.

The source file was first aligned to P9a3ec2a11f, preserving prior custody/profile
changes4911c398d9 andbc3727b3a3, then the optional viewer mode was added. Integration
must compare that exact file or reconcile this baseline when cherry-picking into
the newer P tree; do not replace unrelated shared files. Test imports require P's
interactive_access module, intentionally not duplicated in M's source branch.
Safe-commit compile/ruff/naming gates passed; git diff --check clean. Initial lint
failure was corrected with explicit E402 annotations for test path bootstrap.

Next owner: Y pairs the exact source with its new caller and P's closed schema,
proves stable retry, immutable replay and revoke-before-acceptance/dispatch; P
integrates source and caller; CTO reviews the pinned combined candidate.

## Preserved publication interface

Runtime3539ad2ae5, doc correction200ba442f5, CTO bounded PASSbb43292167 (99 tests).
HoldingsPublication.capture(as_of=None, account_ids=None) returns document,
manifest and immutable acceptance receipt; load_pinned(receipt, account_ids=None)
replays exact index version/date row/manifest/parts. Snapshot wrappers preserve
receipt.date_row.revision separately from selected/decorated document revision.
No fallback or alias promotion. A readback failure can follow successful PUT:
unconfirmed result needs exact-version reconciliation, not rollback/blind retry.
This work and actual producer/deployment remain parked beyond the current caller.

Push state **LOCAL**. Observed origin/CLOUD
`365ab567ba1250a6a3569df38cb75d12fe2e8d0e`. No deploy or push performed.

## Canonical upload reference dependency (CTO fd32cac392)

See [CANONICAL_REFERENCE_PORTS_20260923.md](CANONICAL_REFERENCE_PORTS_20260923.md)
and its exact seven-source evidence. Four offline source characterization checks
pass. Existing canonical classification and security keys differ; no inspected
installed IRPT identity/dated-price facade supplies the requested immutable
identity/USD/share-class evidence. P must pin actual materialized-reader payload
and installation before M binds a pure consumer. Y must use explicit UNAVAILABLE
for missing capability, never classifier guesses as identity/provider FOUND.
No canonical producer, runtime source, provider, cloud or secret operation taken.
