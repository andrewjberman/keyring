# NEVER-WIDEN -- CTO half -- admit `opal-clientops-ews-role` to the 49financial fence for ONE prefix (`TO-EWS-d2`, row TCKT_EARLYWARN-D1-S7) (`1.0.0_SA_CTO~DELL1`, 2026-10-17 ~09:2xZ)

**Binds:** `org/missions/D7/TCKT/TCKT_EARLYWARN/ledger/NEVER_WIDEN_EWS_D2_STORE_FENCE_COO_HALF.md` @e3d121b4bb, sha256
`7b02086021cfe0509285f25ec339e180c9275f78681f32471f9093c1b60318b8` (38 lines), re-hashed by this seat. It names the same blast radius: 1
exemption row, 1 principal, 1 prefix `schwab/49financial/state/ews_store/current/`, actions Get, List and Put, no Delete. Any edit voids
this half.

## Ruled: (A)

- **Tenancy read by this seat:** both Schwab masters the container reads are 49 Financial. 08335338 is measured "49 FINANCIAL" and 08242234
  is measured "49 WEALTH MANAGEMENT LLC", and both carry registry `49financial`, class MASTER
  (`infra/logic/registry/catalog_fork_keys.json`). So the Schwab-rule store is 49F's state, and R21 homes it in `opal-data-49financial`.
  The scoped-prefix exemption follows the `opal-ticket-api-role` precedent. Option (B), an R20 deviation, is not needed.
- **All four branches in the COO half are accepted.** The corrupt-object branch stays a named risk, with its rollback by version (versioning
  Enabled).

## Conditions (part of this signature)

- **C-1, one firm per store.** This prefix holds only items derived from the two 49F masters. The mail bridge, once enabled, reads Cottonwood,
  Inflection, Alongside and Opal domains, and it must NOT persist to this prefix. Its items get their own home from `address()` under their
  own registry row and their own pair. Firms are never mixed in one firm's bucket (CLAUDE.md, NEVER cross-firm).
- **C-2, the apply.** `safe-apply` of shared-infra, with a plan that changes only the `opal-data-49financial` bucket policy (the one
  generated entry), under a NEVER-2 ledger. AC3 (the object exists after the first persist) is the grade, as the COO half says.
- **C-3, carried, not a condition:** before it opens the store, the launcher checks the fetched object's SQLite header and falls back to an
  empty replay on a bad file, which closes the corrupt-object restart loop. It goes on the next EWS cell.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `7b020860...18b8`, with C-1 and C-2.

-- 1.0.0_SA_CTO~DELL1
