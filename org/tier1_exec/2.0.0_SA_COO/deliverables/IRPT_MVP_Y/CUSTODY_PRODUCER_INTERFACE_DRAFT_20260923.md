# Y minimal producer mapping for M/P agreement

Status: DRAFT FOR OWNER AGREEMENT. No schema fields or callable API are emitted by this document.
Authority: CTO exact `20260923T153633Z_1.0.0_SA_CTO_IRPT_concrete_producer_implementation_in.md`.
Inputs: M `a20a1a1bd28c2cf76d5b80aae0d9a745ab5c7d2c`; Y factory `819c9e399086cffb2876a21fbc2cee01724b0bd7`; eligibility controls `23c1dbeaf6`.

## Proposed internal mapping

These are explicit proposed spellings to make agreement concrete, not assumed fields in today's HoldingsSnapshot. M should confirm the output that its bounded `holdings_snapshot.py` tranche can actually supply. P chooses the authoritative S2/schema placement and final spellings; Y adapts after that agreement. No position data goes into browser request fields.

| Proposed record | Minimal fields / semantics | Owner and blocking conditions |
| --- | --- | --- |
| `snapshot_binding` | `firm_id`, opaque `snapshot_id`, `publication_revision`, `manifest_ref`, `source_receipt_refs`, `position_as_of`, `valuation_as_of`, `producer_revision`, `census_revision` | P maps opaque ID to server-owned immutable accepted locator; M supplies publication facts. Locator identifies exact object key/version/hash/length, never a browser path. No latest-date fallback or selected-slice hash substitution. |
| `accounts[]` | `account_id`, `vendor_account_id`, `census_status`, `raw_row_count`, `position_count`, `empty_evidence_ref`, `reconciliation` | M must enumerate exact selected accounts through admitted boundary. Empty is affirmative evidence, not missing input. Unknown status remains refusal for analysis. |
| `positions[]` | `account_id`, `position_id`, `source_grain`, `source_side`, `source_row_refs`, `value_verbatim`, `value_units`, `currency`, `value_status`, `cash_classification`, `security_identity` | M preserves all original economic positions including zero/negative; stable source ID and raw provenance required. `value_verbatim` is exact text, not a float reformatted after reading. Side is source provenance, not permission for Y to negate again. Native USD values do not require invented prices. |
| `security_identity` | original namespace/value plus located canonical `security_key`, `canonical_identifier`, `canonical_identifier_namespace`, `resolution_revision`, or explicit unresolved finding | M names the admitted resolver; Y requires the existing TICKER/CUSIP/CASH canonical contract before freezer. Do not prefix a ticker to manufacture vendor identity. Ambiguity refuses. |
| `reconciliation` | authoritative amount text, source receipt, formula/policy revision, tolerance and its authority, residual, currency, independent-source date, completeness/status; positive/negative/net diagnostics as evidence | M's firm-specific equation must settle cash/accrual/sign/factor overlap. Unknown total or tolerance is not zero/default. Shared-derivation identity is labeled and cannot substitute for required independent tie. |
| `collapse_evidence` | raw row references, source grain, resulting economic position IDs, raw/unique/duplicate counts and equality checks for every consumed field | M may use sanctioned COT relationship collapse only with retained provenance and exact checks; no netting of distinct positions. Y classifies the resulting complete economic position census before any same-security/account analysis aggregation and verifies all source contributions are represented. |
| `quote_evidence` (only share conversion) | exact canonical identity, positive price text, currency USD, `as_of`, actual source revision and receipt | Missing or incompatible quote refuses; source USD values remain exact. No stale/interpolated quote fallback or snapshot hash relabeled as price revision. |

For the first consumer mapping, prefer explicitly sourced USD position values. A SHARE branch remains ineligible without real quote evidence; weights/reference notional are not an actual-custody source. All proposed enum spellings and record locations require P/M agreement; Y will not put them into a public schema or exception envelope independently.

## Concrete call boundary to agree

The existing Y factory accepts `authorize_snapshot(principal, owner)` and `load_normalized(browser, principal, owner)`. Keep these signatures unless P identifies a required change. P should supply the exact accepted-snapshot reader export returning the agreed immutable binding plus selected census/position payload, with current acceptance checks before and after retrieval. M's producer supplies the payload and proof; it must not call Y's analysis factory or hold caller credentials.

Y's later implementation will classify original positions, preserve provenance, then use the existing normalized output `{input_id, content_sha256, document}` only for eligible inputs. It must not fabricate a successful ParseResult/reconciliation from an incomplete holdings tree. The precise trusted parsed-row adapter will be agreed once M's output and P's reader are concrete. Existing factory exact owner/source/account/snapshot validation and current retained-input replay remain in force.

## Requested owner responses

- M: confirm or correct the proposed fields with exact producer export/commit and a synthetic complete, negative-row, zero-row and incomplete-account output example. Identify unavailable fields and firm-specific refusal; no substitute values. This request stays inside CTO's local producer tranche.
- P: confirm authoritative schema location/version, exact reader export/signature and opaque snapshot-ID binding, source-receipt placement, and current supported refusal mapping. Coordinate any field changes with M before schema emission.
- Y: map agreed fields to all eleven eligibility controls, then implement only the owned consumer. Until these responses establish a concrete interface, this draft remains coordination evidence, not an active callback or acceptance contract.

No runtime activation, cloud access, new retained artifact family, public refusal enum, upstream runner execution or economic acceptance is part of this draft. The CTO reviews the paired result directly.
