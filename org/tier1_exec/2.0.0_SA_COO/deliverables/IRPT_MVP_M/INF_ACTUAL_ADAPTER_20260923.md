# Inflection actual custody adapter candidate

Seat 2.0.0_SA_COO~M; direct Codex continuation on 2026-09-23: Andrew, verbatim,
"Go". Existing Holdings mandate and 600-second drive remain active.

Production dispatch build_inf_actual now consumes positions_mv and accounts_v2 through the native
position validator before returning a snapshot. The previous portfolio/account
projection remains build_inf (its exact adjudicated legacy read is preserved)
and is retained as private attribution evidence by the production adapter; its
successful construction cannot stand in for actual security holdings. Historical
membership tests call that isolated helper explicitly, while new dispatch tests
exercise the production builder and published snapshot schema.

The exact requested account census must exist in both native positions and
independent totals, with matching source dates and source-backed currency in
both frames. Unknown currency/value/quantity, duplicate position ids, duplicate
totals, missing requested accounts and differences above one cent refuse.
Distinct positions sharing an Orion product id stay distinct. Signed/zero values
and absent optional prices are preserved; no value is reconstructed from a price.
Outside-request position/account counts remain explicit private source controls.

Observed ACCOUNT -> Client SLEEVE -> SECURITY is emitted from validated custody.
Client is resolved from the canonical MDPF registry VIEW_TREE, not a copied
category table. Unknown model/SMA membership is retained as provenance. Security
identity remains VENDOR/native product id; quantity is validated but the current
public schema cannot carry a separate quantity/name field. P owns that extension.
Custody and overlay dates remain distinct. Public Unresolved nodes are not emitted
by this actual INF adapter. Known portfolio attribution is retained privately;
this candidate does not yet allocate actual positions to Models or SMAs.

## Checks

- 12 focused native controls and production dispatch checks PASS, including
  snapshot reconciliation and validation against HoldingsSnapshot.schema.json.
- 17 existing INF/Eclipse checks PASS (83 unrelated checks not selected).
- Unmodified real Sept23 positions_mv/accounts_v2 inputs REFUSE because explicit
  source currency is absent. This is an exercised refusal, not live acceptance.
- Live native id/account_id/product_id dtypes are Int64; current_shares has zero
  nulls. No native prices are required or synthesized.

## Integration and open work

No vendor call, publication, deploy, schedule activation or browser proof occurred.
CTO/CRO source authority finding0d0fd51b33 remains binding; USD cannot be inferred
from absent FX columns. The source-backed currency binding is still required.
The default producer census remains accounts_v2; outside positions accounts are
counted explicitly, and prior original-roster checkd0fe9f1a2b explains the current
82 inactive accounts. That is NOT a complete historical/selected-account admission
policy. Per-account availability and roster-backed selected/historical inputs
remain open so one bad account does not poison independently valid accounts.
Do not present this first integration as completion of M1/M7 or all-firm coverage.

P must consume the exact Holdings source candidate and its new inf_positions.py
module. Canonical taxonomy lookup depends on existing MDPF category registry and
its imports. Supply these in the producer runtime package; do not copy a taxonomy.
P's shared display projection must read classification.hierarchy_path=["Client"]
for the observed sleeve/security, preserve vendor security identity and avoid
pretending this confirms a fee/advisory classification. Existing owned UI fix is
portal e5604c03, separately queued with P.

Next proof remains source-backed currency -> one real INF account snapshot ->
accepted immutable publication -> scoped API -> real-login Holdings/security drill.

Commit boundary: this candidate is currently an uncommitted working diff. Naming
gate refused the new actual positions read path. CTO202806/G own the approved
locator mechanism; old legacy-read01 context is preserved. This document and the
projection patch are review/handoff artifacts, not accepted source code or a waiver.
