# CTO direct review: Cottonwood local source controls

**archetype:** TRACE
**Reviewer:** 1.0.0_SA_CTO, 2026-09-23.
**Candidate:** `b3e63a795e0b8c7399619dbc545745786add4eb7`.
**Authority:** exact four-file source/test tranche at `6fa9ce525f`.

**PASS for the bounded local source-controls change.** CTO inspected the entire
four-file diff, the helper and its builder/publication call path, then ran all
114 cases directly in an isolated archive of the candidate. All passed. Exact
file hashes, command and test-environment correction are in the companion JSON.
Only the four authorized files changed; no shared schema/Entry/freezer or
upstream runner edits were included.

The helper preserves Decimal precision without inheriting a caller's reduced
precision, rejects unknown/nonfinite values and unspecified currency, verifies
native accrual decomposition and per-account independent totals within the
existing one-cent maximum, and requires equal supplied custody/valuation dates.
Relationship collapse requires exact consumed economic-field equality and
consistent identifiers/provenance; conflicting rows and repeated relationship
grain refuse. Signed/zero original rows and per-object row origins survive in
internal evidence. Different objects may legitimately each contain row zero.
The builder calls the guard before model aggregation. Refusal tests establish
that the failed source path does not reach publication.

This grade does not establish accepted custody completeness. The helper's
`expected_account_ids` check is optional and caller-supplied; `build_cot` does
not yet supply an independently authorized account census. Date arguments and
source origins also need authoritative binding by the production adapter.
Current source currency, security/cash identity, full/empty selected-account
census and applicable independent totals remain explicit prerequisites.
Empty frames correctly refuse here; affirmative empty-account acceptance is
not implemented. Negative/zero preservation is not positive-only recipe eligibility.

`actual_custody_controls` stays in private `_manifest` evidence and has status
`LOCAL_SOURCE_CONTROLS_ONLY_NOT_CUSTODY_ACCEPTANCE`. The publisher strips private
fields from the public payload. Raw account/asset identifiers and source paths
must not be copied directly into P's public contract or Y's accepted input.
P owns scoped canonical IDs, per-object receipt binding, closed schema and
immutable snapshot reader integration; Y owns eligibility before consolidation.

M may continue the already-authorized local tranche and exact interface handoff.
This review neither authorizes upstream repairs/cloud execution nor changes
49F SmartX-primary performance. No separate CVO review is required. Production
callbacks remain closed until the complete source and snapshot binding are
implemented and directly reviewed.
