# Cottonwood source port and real-account handoff

M owns the source callback; P owns runtime composition and shared currency binding.

`data/assets/scripts/gold/investor_reporting/cot_account_mapping.py` exports
`make_cot_mapping_loader(s3, *, as_of)` returning `load_mapping(firm_id, canonical_account_id)`.
It validates one exact dual identity from cutoff-bounded Rebalancer model_assignment,
reads the exact S3 version, and carries the original source revision and P currency authority.
The cutoff is server composition, never request input; no callback grants account access.

Required unchanged P dependency pin:9e1bc3a751, files
`infra/aws/lambda/investor-reporting/reports/currency_authority.py` and
`docs/contracts/investor-reporting/v1/CurrencyAuthorities.json`.
Package the JSON beside the module or use IRPT_CONTRACTS_DIR. No M currency constant.
Original complete rebalancer_conversion, rebalancer_schemas, silver_registry, opal_naming,
_ids and source_inputs modules are runtime dependencies; never extract their formatters.

Measured real account:acc_f91fd04e6f6534fb0270bdcb. build_snapshot cottonwood,
as_of2026-09-23, account_ids={that ID} passes published schema and exact reconciliation:
3 positions,5 nodes,$1165.21 before/after. Seven source object receipts retained.
See COT_SELECTED_REAL_SOURCE_20260923.json. Raw currency columns remain absent and unchanged;
Andrew attestation is separate private evidence. 17 targeted tests pass.

P next: integrate this callback and two-file currency dependency, bind current authorized
selection to the named account, exercise retained publication/read and authenticated
Holdings drill. M has not published a firm index, deployed, or made vendor calls.
Do not replace a complete firm publication with this bounded one-account candidate.
CRO f307d58415 now identifies the four-field-null BD rows as absent end-date positions;
M is incorporating this newly evidenced admission rule separately to expand account coverage.

## Expanded actual account after CTO5ee54ac0d4

The same Cottonwood account already used for P's positive Performance result now
passes Holdings: acc_d486fc9455d6b2aa18e13af1,57 positions,USD19705844.84.
78 original dimension rows include21 absent-at-end-date pairs excluded under the
new measured rule. Original byte receipts and excluded physical ordinals retained.
Three targeted controls prove narrow exclusion, partial-null refusal and independent
total mismatch refusal. Evidence COT_END_DATE_POSITIONS_PROOF_20260923.json.
Please prefer this account for the shared authenticated cross-tab journey.

M-P-MAP-01 repaired: source_revision is the exact SHA256 string; the full source receipt plus date is source_provenance. ActualS3 callback passed unchanged P bd_selected.requests_for@9e1bc3a751 for the named57-position account, constructing both request bodies with no vendor calls. See COT_MAPPING_PAIRED_PROOF_20260923.json.
