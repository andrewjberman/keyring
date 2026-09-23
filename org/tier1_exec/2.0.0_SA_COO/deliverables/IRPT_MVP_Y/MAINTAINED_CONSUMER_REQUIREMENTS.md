# Y maintained-source consumer requirements

Owner `2.0.0_SA_COO~Y`. Authority CONTRACT v1.2 and CTO
IRPT-MAINTAINED-SOURCE-01 `0429af3604`. Consumer inspection at backend
`d29c893cf1`; no new maintained-source or vendor proof is asserted.

Y claims recipe/worker validation and consumption in ycharts/generate; M's
`_scope/maintained_sources.py` and P's RequestComposition schema are their sole
integration surfaces. Existing composition producer spelling is
irpt-analysis-composition.v1 with browser/resolved/recipe_version/settings.
The following is a consumer handoff, not a second stored schema. P publishes
the final placement and paired schema after M supplies source descriptors.

## Exact current consumers and missing values

`recipe.py:validate_envelope` expects resolved.profile strings for prepared_for,
prepared_by, organization, contact_email, contact_phone and contact_url. This
legacy validator is custody-only and is not the new prospect worker boundary.
`generation_body` requires all nine cover keys below to be present; it copies
seven cover values to both root and modal and requires consistency. Its existing
implementation does not establish that missing maintained values are known.

| Cover key | Source/meaning required for integration | Missing behavior proposed for agreement |
|---|---|---|
| prepared_by | Verified maintained acting preparer display identity | Unavailable; no generic or borrowed advisor name |
| organization | Maintained organization for verified firm | Unavailable; no fixture organization |
| prepared_for | Authorized client/prospect display value | Unavailable; no default client label |
| contact_email | Maintained advisor contact address | Explicit absent may render blank after M/P agreement |
| contact_phone | Maintained advisor contact phone | Explicit absent may render blank after M/P agreement |
| contact_url | Maintained advisor contact URL | Explicit absent may render blank after M/P agreement |
| custom_field | Authorized optional cover text | Explicit absent may render blank after M/P agreement |
| report_title | Exact browser report_title when present; otherwise maintained recipe title | Unavailable if neither exists; no new title default |
| primary_name | Actual opaque deterministic owned portfolio name from recipe.portfolio_name | Worker derives from accepted ID/revision/holdings fingerprint; no advisor-source lookup |

The optional-absence proposal emits empty strings only at the vendor-body edge;
the stored source contract must distinguish absent from populated values and
retain its basis. Existing offline recipe fixtures use empty contact/custom
strings, but those fixtures do not establish vendor or maintained-source proof.
Until agreement, no missing source value is silently converted to a default.
M should identify if required prepared_for has no prospect source in the current
intake contract; the browser currently supplies only references, title and choices.

M01:32:07 and P01:30:58 agree optional absence remains explicit in composition
and becomes an empty string only at the vendor edge. Required identity/recipient/
organization/title still refuse when missing. For FIRM_OPERATIONS, prepared_by
means the actual verified acting user, not an invented advisor: a maintained
display name bound to that principal is acceptable, preserving principal_class
and source provenance. Do not borrow an advisor identity or require a fabricated
advisorKey. This changes no grant, firm selection, or authorization requirement.
Missing acting-user binding remains unavailable. Auth MFA phone/login email
alone do not establish reporting contact preferences.

## Comparison identities and order

`generation_body` consumes an ordered list of {vendor_id, name, security_type}:
vendor_id is copied unchanged into secondarySecurity.securityId/displaySecurityID
for one comparison, or comparisonSecurities entries for two through five.
name is display text, not an identifier. Require an explicit security_type;
the function's fallback to security must not classify an unresolved model.
`recipe_for` derives Overview/Comparison/Multi from count0/1/2..5; browser
comparison_keys remain exact, unique and in the requested order. Unknown keys,
unresolved/ambiguous mappings and duplicate mapped identities must refuse.

Existing templates.json is Y-owned captured recipe configuration (blob
ed18c59c86ef89b33eb4759f0d2a939b964e5ac8). Its catalogue keys are opal_long_term,
opal_short_term, opal_intermediate_term and opal_ultra_long_term. Captured
security_id values are P:1728413/P:1728415/P:1728315/P:1728420, explicitly typed
model_portfolio; label is display text. That capture says identities were checked
through securities_info, but is not current maintained scope/entitlement proof.
It establishes neither an authorized current catalogue owner nor permission to
equate any generic source security_id with a vendor identifier. M must supply
explicit vendor namespace/identity/type evidence and source authority for each
selected mapping. Y may then copy the proven typed ID without stripping P:/M:/S:.
P: for a vendor model_portfolio is not interchangeable with M: merely because
both may be colloquially called models. M coordinates maintained catalogue source
ownership; Y retains ownership of the captured recipe/template configuration.

## Concrete consumer example and required provenance

This is a synthetic, redacted function argument example only, not a populated
maintained source record, approved schema, or authority to dispatch:

```json
{
  "cover": {
    "prepared_by": "REDACTED_ADVISOR",
    "organization": "REDACTED_FIRM",
    "prepared_for": "REDACTED_AUTHORIZED_CLIENT",
    "contact_email": "advisor@example.invalid",
    "contact_phone": "REDACTED_PHONE",
    "contact_url": "https://example.invalid",
    "custom_field": "REDACTED_COVER_TEXT",
    "report_title": "Exact requested title",
    "primary_name": "IRPT-worker-derived-owned-name"
  },
  "comparisons": [
    {"vendor_id": "P:999000000", "name": "SYNTHETIC_MODEL", "security_type": "model_portfolio"}
  ]
}
```

Before dispatch, M/P's accepted producer must bind those values to verified owner,
input/selection identity, exact ordered browser comparison_keys, maintained source
location and owner, source schema, stable revision when available, exact resolved
byte digest, applicable business/source date or explicit absence, and mapping
evidence. A local digest is not upstream authority/freshness. Y freezes those
actual resolved bytes and recipe/settings/template versions in the accepted
REQUEST_COMPOSITION, then reuses them across worker retry/reopening/export.
No later source resolution on retry; current access/retention checks still apply.
Source dates are not replaced by observation timestamps. Exact field spellings
and revision-descriptor placement remain P/M agreement work, not invented here.

Settings already map management_fee, rebalance_frequency, reinvest_dividends,
start_of_series, level_as_of_type, tax_status and benchmark to vendor fields via
SETTING_TO_VENDOR_FIELD. Preserve their frozen values and prove actual readback.
The pinned template census/configuration is separately required for extraction
and recipe identity. Session credentials and signed download URLs never belong
in this composition or the worker checkpoints.
