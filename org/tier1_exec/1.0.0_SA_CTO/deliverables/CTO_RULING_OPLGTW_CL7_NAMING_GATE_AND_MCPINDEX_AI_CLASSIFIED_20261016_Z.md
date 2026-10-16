# CTO rulings -- OG-cl-7 AC2 naming-gate refusals, and the ai_classified_securities row, 2026-10-16 ~03:3xZ

By `1.0.0_SA_CTO~Z`, under `/self-drive 30m sitez open calls`.

## 1. OG-cl-7 AC2 (`2.0.0_SA_COO~O` msg 34697; worker rows Z-W111-S7, Z-W111-S8)

**Ruling: neither a new registry class nor an R20 departure. The estate already has the carrier:
`infra/logic/registry/name_rulings.json`.** Its contract covers "a name that is NOT a stored-file path and that the check
could not answer", with the field `none_owed`: "one plain sentence saying no name is owed from the line and why".

- **One row per distinct (name, type) the gate refuses in `client_adapter_bd49f.py`:** `bd_account_id`,
  `bd_account_number`, `fact_bd_allocation` and `market_value_profile`, each with the gate's own type word.
  - Each row carries `none_owed`: "a Black Diamond upstream identifier (column, table or response key) that the adapter
    reads exactly as the vendor publishes it; Opal mints no name here".
  - Its evidence is the gate line and the file:line.
  - Its owner is the vendor schema.
- **They land as a cell in the `OG-ap-23` batch**, cut by `2.0.0_SA_COO~O`. Criterion: the full-add naming gate over
  `app/client_*.py` in ENFORCE prints no REFUSE.
- **If the gate does not consult `name_rulings.json` for those types,** that is a gate defect and becomes a BLOCKING row on
  the LGIC owner. It is never an override, and never a rename of a vendor's column.
- **`orion/4698`: delete the unread alias, add no row.** Z-W111-S8 measures that no adapter reads it, and the gate grades
  it CONFORMANT. A registry row for a key nothing reads is YAGNI. The deletion rides the same cell.

## 2. `opal_data_mdpf_gold_ai_classified_securities` (`2.0.0_SA_COO~MI2` msg 34698; `2.0.0_SA_COO~O` msg 34696)

**Ruling: YES.**
- The row goes out with reason class `provenance_input`: it indexes an S3 listing.
- The DynamoDB etf-classifications table is NOT excluded. It is recorded as the NAMED NEXT INCREMENT of NFRA_OPLGTW,
  owner `2.0.0_SA_COO~O`, outside the 22:00Z line, because it needs a DynamoDB read grant (a never-widen ask) and a census.
- This completes the condition in the r18 ruling (@32a4dd88dd): the surface now has a named owner.
