# Opal full-access dependent changes -- Y

Authority: controlling `IRPT-OPAL-FULL-ACCESS-20260923` at `5ad99c7d30`.
Inspected Y source `10627906f24aa42db4c08fd66105599f35bf7819`.
This is a concrete dependency report, not a permission policy or live proof.
P owns shared verified identity, scope, prospect ownership and API/UI changes.
Y owns the generation/upload/freezer/retained-request consumer changes below.

## Reproduced retained-read failure

`ops/owned_requests.py::OwnedRequestReader._validate` rejects a record when
its retained owner principal differs from the current viewer, before invoking
`authorize_current(principal, owner)`. In a pure local probe, an otherwise valid
cottonwood record owned by `original-author` passes the same-owner control.
The synthetic current viewer `{firm_id: cottonwood, principal_id:
verified-opal-viewer, home_firm_id: opal-capital, principal_class: OPAL_GLOBAL}`
is refused with `REQUEST_UNAVAILABLE`; the installed permissive current
server-authorizer callback has **zero calls**. No browser identity is verified
by this probe; it isolates the unconditional pre-authorizer owner ceiling.

The retained owner must remain original-author. The fix must consume P's
verified interactive-viewer authority, not impersonate that author. `_principal`
currently chooses the tenant lookup from principal.firm_id; cross-firm and
Global history need P's concrete actor-versus-data-firm/current-view contract.
History cursors must remain bound to current viewer and query scope, not become
portable grants. Equivalent ordinary-firm and forged-identity refusals remain.

## Prospect/upload/generation dependencies

- Shared `_scope/prospect.py` and the shared guarded Entry currently exclude
  Opal prospect access. P owns that correction and publishes the exact verified
  prospect owner/viewer contract. No parallel identity schema is created by Y.
- Y `intake/upload_entry.py::upload_csv` builds a two-field principal from the
  prospect owner; `intake/uploads.py::_allow` requires exact owner principal/firm
  equality. These consumers must receive the real current actor separately when
  P enables another-owner access. Creation and immutable attribution stay intact.
- Y `intake/portfolio.py::freeze_parsed_portfolio` currently treats every
  OPAL_GLOBAL owner as custody and rejects a CSV source, with custody-only
  snapshot/account requirements. That must be split by source lane once the
  exact Opal prospect-owner contract is supplied. A pure frozen owner does not
  itself grant permission; shared current authorization remains mandatory.
- `ycharts/generate/tests/test_custody_entry.py::test_explicit_prospect_install_preserves_partner_access_and_opal_refusal`
  contains an explicitly obsolete Opal refusal assertion. Replace it with the
  actual P boundary's verified-Opal positive control and retain ordinary-firm,
  forged-Opal and warm-process negative controls after consuming the shared pin.
- `build_custody_entry` does not install a prospect service/owner lookup. Missing
  runtime ports remain a capability gap, not a valid Opal permission denial.
  The broader service must route both lanes without inventing runtime capability.

## Coordination and next proof

P received exact dependency message `20260923T172053Z_2.0.0_SA_COO_Y_IRPT_Opal_access_dependency__retained_vi.md`.
Needed: concrete verified viewer/current-authorizer, data-firm and prospect owner
interfaces plus P's pin. Y then updates owned consumers/tests against that shared
boundary and hands back a pinned patch. No current authoritative replacement
interface has been consumed. No code change or new access PASS is claimed here.

The previous bounded consumer review does not establish compliance with the
new full-access requirement. Live-first remains in force, and deeper custody
package/source work stays parked unless the first-hop trace requires it.
CLOUD push remains held. No cloud operation, vendor operation or deployment.
