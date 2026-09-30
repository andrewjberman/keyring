# ANDREW-DIRECT 2026-09-30 ~13:0xZ -- R20 yes (ETF + BD fees), Schwab grant widening yes, platinum/advi hold lifted

**Where:** the 1.0.0_SA_CTO~O terminal, site Z. He was answering three items this seat listed as acts only he can do
(tick logs 29, 32 and 35).

**His words, VERBATIM:**
> "yes thats fine on naming exception. Regarding schwab, sure. advi tool, what not yet are you referring to? but yeah
> certainly whatever needs to be lifted should be lifted"

## What each answer covers (no wider, no narrower)

1. **"yes thats fine on naming exception"** is his CLAUDE.md rule 30 / `infra/logic/02_DOCTRINE.md` R20
   acknowledgement of ONE declared departure covering the two served legacy keys put to him:
   - (a) `opal-data-portal-v2` `platinum/etfs/positioning_data.json`, read at NFRA_MCPINDEX MX-t-10's new sites (the
     catalog row, the emitter and the ETF tool). This is ruling B3 of `REINSTATE_RULINGS_20260930.md`.
   - (b) `opal-data-bd` `silver/fees/` (scope `49financial`), read by MX-t-13 (`blackdiamond_list_fees`) and its reader
     role, released by MX-r-7.
   - The departure is READ-ONLY, at those keys, where the data lives today. It does not move either key and does not
     authorize any write. Its end condition: when the owning migration moves a key onto the builder grammar, that key's
     departure ends. For (b) that is ADVI_FIRMBKTS. For (a) no migration owns `platinum/etfs` yet (Z-W15-S5).
2. **"Regarding schwab, sure"** authorizes widening ONE existing Opal principal's Schwab grant to add `dim_transaction`,
   through the grant admin tool.
   - It makes FWD-3's transaction half reachable, and r6.J1's transaction question can then be answered rather than
     refused.
   - It lifts ruling B2 for that one grant only. No new identity, no new principal, and no other grant change.
3. **"whatever needs to be lifted should be lifted"** lifts the hold he set on `platinum/advi`: "platinum/etfs YES,
   platinum/advi NOT YET", relayed at MX-t-11's supersession @a120fec68b and cited to `DATA_CATALOG.yaml:32` "WIDENING
   IS ANDREW-ONLY".
   - That hold kept the `advi` catalog row and tool, MX-t-12 (formerly MX-t-11), from being built.
   - It is now his widening word for `platinum/advi`, and MX-t-12 may proceed under its own order.
   - The MX-t-8 authority's advi limit (`platinum/advi/49financial/` only, because the firm scope is the key segment,
     C7) is unchanged.

## Routing

- To 2.0.0_SA_COO~MI (NFRA_MCPINDEX issuer): items 1-3.
- The R20 register entry goes in `infra/logic/06_CONFORMANCE_LEDGER.md` section 6, which is 4.0.0_SA_CRO's lane.
- The naming gate grades NEW literals before any waiver (`.tools/naming-gate.py:1413`, `:1444-1446`) and reads no R20
  entry. So this acknowledgement lands in the code only once the gate honours a register entry. That is gate owner laptop
  1.0.0_SA_CTO's (LGIC_ENFORCE) edit, and it is asked the same turn.

## Addendum 2026-09-30 ~20:2xZ -- the naming-gate entries this acknowledgement carries (1.0.0_SA_CTO~O)

Andrew's words above are unchanged. This section exists because `.tools/naming-gate.py` `authority_ok` honours an
`r20_exception` entry only when the record at a full pin carries that entry's id as a whole token. The eight entries
(computed by 2.0.0_SA_COO~MI against the frozen bytes, @b9d1b053bc) land in `org/standards/NAMING_LEGACY_READS.json`
in the commit after this one, pinned to this one.

| entry id | register row | file | literal | occurrences |
|---|---|---|---|---|
| NFRA-MCPINDEX-R20-01 | X11 | `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml` | `platinum/etfs/positioning_data.json` | 1 |
| NFRA-MCPINDEX-R20-02 | X11 | `workflows/atom_decomposition/emit_catalog_v02.py` | `platinum/etfs/` | 3 |
| NFRA-MCPINDEX-R20-03 | X11 | `workflows/atom_decomposition/emit_catalog_v02.py` | `platinum/etfs/positioning_data.json` | 1 |
| NFRA-MCPINDEX-R20-04 | X12 | `infra/aws/ec2/opal-gateway/app/integrations/blackdiamond/integration.py` | `opal-data-bd` | 3 |
| NFRA-MCPINDEX-R20-05 | X12 | `infra/aws/ec2/opal-gateway/app/integrations/blackdiamond/integration.py` | `silver/fees/` | 4 |
| NFRA-MCPINDEX-R20-06 | X12 | `infra/aws/ec2/opal-gateway/app/integrations/blackdiamond/integration.py` | `49financial` | 5 |
| NFRA-MCPINDEX-R20-07 | X12 | `infra/aws/terraform/opal-gateway/blackdiamond_reader_iam.tf` | `opal-data-bd` | 1 |
| NFRA-MCPINDEX-R20-08 | X12 | `infra/aws/terraform/opal-gateway/blackdiamond_reader_iam.tf` | `silver/fees/` | 1 |

- **as_of_cutoff 2026-12-31, all eight.** X11 and X12 are CONDITIONAL rows, and their conditions are events (the
  platinum/etfs key's R19 repoint; the D14 port of `opal-data-bd`), not dates. The gate maps conditional to a date. The
  date is therefore a REVIEW POINT, not the condition: on it, owner 1.0.0_SA_CTO re-reads each row's condition and renews
  the entries if it still holds, or removes them if the migration has landed. PERMANENT would misstate a conditional row.
- **remediation:** ETFS_CANON (01-03) and ADVI_FIRMBKTS (04-08), as computed. The R20 kind advances no remediation.
- Scope is unchanged from item 1: read-only, these keys, no key move, no write.
