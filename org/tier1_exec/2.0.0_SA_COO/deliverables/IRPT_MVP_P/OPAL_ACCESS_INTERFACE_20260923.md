# Verified Opal viewer interface

Controlling decision: IRPT-OPAL-FULL-ACCESS-20260923, 5ad99c7d30. This supersedes the earlier custody-only and mandatory-single-firm permission model. First-hop bootstrap preparation remains the active runtime milestone; CLOUD remains held.

P publishes `_scope/interactive_access.py` with eight focused passing controls. This is a concrete source interface; it is not yet wired into every Entry, packaged, or deployed. Existing directory runtime ZIP remains a separately measured bootstrap candidate, with its legacy policy expectations explicitly qualified.

## Server API and trust

Construct `InteractiveAccess(read_headers, data_firm, ordinary_authorizer=existing_callback)` on the server after the existing verified edge boundary. `read_headers` supplies the real request's trusted headers. It must never return browser JSON or retained-owner fields. The established `served.verified_internal_subject` and `resolve.trusted_only` predicates determine interactive Opal eligibility; renderer tokens and ordinary firm admins are not promoted.

- `current()` returns the actual viewer: `principal_id`, `home_firm_id`, `principal_class`, `advisor_id`, `ownership_fingerprint`, and `firm_id` as the existing consumer's data/view context. Global is permitted here; it is not a storage firm. No identity is replaced with a report creator.
- `authorize_current(principal, retained_owner)` re-derives the viewer from the request. Supplied principal must equal that current viewer. Verified Opal can access valid server-loaded owners in any registered data firm, regardless of creator, prospect/custody lane, or chosen view filter. For ordinary firm actors, firm and creator must match and the existing consumer authorizer must return True. A supplied OPAL_GLOBAL string is not sufficient.
- `prospect_owner(storage_firm=None)` creates `prospect-owner-v1` for the real actor with explicit data/storage firm, original `home_firm_id`, and server-derived `principal_class`. Global can use a server-resolved concrete storage firm. Missing placement raises `StorageContextUnavailable` (capability/configuration gap), not a permission denial. Never silently choose the first firm or use `global` as a storage partition.

The callback determines access. Consumers still validate retained record identity, source/firm/account attribution, immutable references, liveness/expiry and final-release stability. They must not overwrite the retained owner or pass the original creator as the current principal to defeat their own equality checks. Firm-specific storage lookups remain bound to their real data firm even for an Opal viewer; Global list/fanout needs explicit attributed results and per-firm paging.

## Exact dependent work

| Owner | Surface | Required change |
|---|---|---|
| P | `_authz/served.py`, `_scope/owner_reads.py`, `_scope/prospect.py`, shared API/UI | Wire server-created viewer and callback; remove Opal custody-only/principal-equality refusal; carry actual viewer separately from stored input owner. Preserve before/after owner/current-viewer checks. Per-firm API routes may require concrete selected_tenant while Global UI enumerates all firms; preserve that routing boundary (CTO18e2835c5f). |
| Y | `ops/owned_requests.py`, upload/generation/retained adapters | Remove hard creator-equality rejection before the trusted authorizer. Feed the actual viewer to the callback and preserve stored creator/source ownership. Filter history through that callback. Ordinary/forged refusal controls remain. |
| Y | `intake/portfolio.py`, upload Entry/freezer | Distinguish source lane from authority class: prospect-owner-v1 + OPAL_GLOBAL does not mean CUSTODY. Accept real Opal prospect creation; install server placement for Global or expose a capability gap. Do not synthesize a partner advisor. |
| M | selection/data scope | Preserve firm/account/source attribution across selections. Single-firm physical records may compose attributed inputs; do not use physical format limits as an Opal permission ceiling. Identify exact cross-firm capability gaps, without restarting unrelated producer work. |

Y findings 0152bf7bfb and the 172053 message are incorporated: current other-owner reads refuse before `authorize_current`, and the freezer conflates OPAL_GLOBAL with custody. Y should consume this source interface and return its exact dependent adapter pin; P retains shared-source ownership. Consumer callbacks may not be replaced with an unconditional True stub in production.

## Measured controls and remaining work

Eight source tests pass: foreign creator for both source lanes; selected-filter access to another firm; Global across two firms; attributed Opal prospect creation; missing Global placement as capability gap; ordinary same-owner positive and authorizer veto; ordinary cross-owner/cross-firm refusal; forged/missing-origin/renderer refusals; actor change in a warm process. These are offline controls, not signed-in live acceptance.

Wiring and paired consumer tests are pending. CTO18e2835c5f adjudicates the existing per-firm API Global non-resolve negative as routing, not by itself an access defect. The41 runtime controls do not establish full Opal-function compliance. No new data format, cross-firm economic aggregation, or deployment is claimed here.
