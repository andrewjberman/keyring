# NEVER-WIDEN half -- NFRA_OPLGTW OG-gw-2, the grant-writer catch-up apply from af2d762970's closure -- SIGNED (3.0.0_SA_CVO~O, 2026-10-03 ~19:5xZ)

**Asked:** `2.0.0_SA_COO~O` msg 28967. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-gw-2_20261003.md` @a0778885b5. The half
is required by R1 (`ledger/ROUND_ANALYSIS.round14.md` section 3): `data_entitlement` and the contract decide whom grants
admit.

**VERDICT: SIGNED** with guards W1-W2, on these pins:
- staged closure = `af2d762970`;
- deployed grant-writer code hash `nhz+dwJs...`;
- rollback = the saved deployed zip (sha256 `9e1cfe77...`).

## Independently measured (~19:3xZ-19:5xZ)

**Deployed blobs.**
- I searched the history of each file for the deployed member sizes (31834 / 27507 / 8806 bytes). The matches land on the
  same three commits the worker names: `aac92bdff8` (`data_entitlement.py`), `c19f86c295` (`config.py`) and
  `c2f5d5a071` (contract).
- This corroborates the worker's hash-object equality of the deployed zip members (GW2_BEHAVIOUR_DIFF section 1).

**The contract, deployed -> staged, JSON-normalized.** Exactly three changes, all `dim_transaction`:
- `datasets` gains `dim_transaction`;
- `fields.dim_transaction` is ADDED with the 15 named columns;
- `additive_fields.dim_transaction` is ADDED, empty.

Nothing else moves: the masters, operations, date mode and the other three datasets' fields are equal.

**`data_entitlement.py`, deployed -> staged.** The only hunks add tool NAMES to the `NATIVE_TOOLS` list:
- `list_email_filtered`, `inspect_email_attachment` and the three transcript tools;
- `etfs_get_positioning` and `blackdiamond_list_fees`.

`NATIVE_TOOLS` feeds tool classification (`TOOL_CLASSES`), not candidate admission. The writer's admission path is the
admin `validate_candidate`, which reads the contract's `fields`. That matches the worker's call-site trace
(GW2_BEHAVIOUR_DIFF section 2; claim: held), and the in-process probe on both closures (section 6) shows exactly one
admission flip.

## Authority for the widening

- **Andrew-direct 2026-09-30 ~13:0xZ, verbatim "Regarding schwab, sure."** Record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_13xxZ_R20_ETFS_BDFEES_YES_SCHWAB_GRANT_YES_ADVI_LIFTED.md`
  @1eba868308.
  - As recorded, it authorizes widening ONE existing Opal principal's Schwab grant to add `dim_transaction`, through
    the grant admin tool, with "no other grant change".
  - NFRA_MCPINDEX MX-r-6 A5 foresaw this very refusal: "the grant-writer Lambda bundles its own contract", row
    Z-W19-S9. This act is the path that word needs.
- **The contract change itself** came from NFRA_MCPINDEX MX-r-6 step 0 (@32ebe6bee6, A1). The live gateway already serves
  it on `af2d762970`. This act aligns the writer with what is served; it serves no new data by itself.

## Guards

- **W1 -- scope, relayed verbatim (not a new gate).**
  - After this act the writer ADMITS `dim_transaction` for ANY verified-owner candidate. Andrew's word covers ONE
    existing principal's grant, "no other grant change".
  - Any further `dim_transaction` grant needs its own word from Andrew. The capability is not that word.
- **W2 -- base at the act.** If the deployed `CodeSha256` is not `nhz+dwJs...`, or the manifest no longer names
  `af2d762970`, at PHASE B step 1, this half is VOID.

## Finding for the CTO (declarative, not a block on this act)

NFRA_OPLGTW's ratified PRD text still names three datasets:
- :37 "two masters and three silver datasets";
- :155 "Only their `silver/dim_position/`, `silver/dim_balance/` and `silver/dim_asset/` prefixes are data-readable";
- :309, the proposed first entitlement, "three datasets".

The contract it governs has carried four since @32ebe6bee6, written by another project's order with no OPLGTW addendum.
The PRD needs an addendum recording `dim_transaction` and its 15 columns. The ratified-text half then re-opens, and this
seat re-signs.

## Covers / does not cover

**Covers:** the function code (one resource, code hash only), the one admission widening and its rollback (the saved
deployed bytes, Terraform-targeted), and both branches of sections 3(a) and 3(b) of the ask.

**Does NOT cover:** writing any grant; the PRD addendum; a moved base; any other resource; the CTO half.

-- 3.0.0_SA_CVO~O
