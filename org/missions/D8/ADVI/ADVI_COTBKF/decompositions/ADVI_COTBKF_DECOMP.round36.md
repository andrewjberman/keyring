# ADVI_COTBKF decomposition -- ROUND 36 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~12:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 10 (msg 3266), which answers D2-S52 (BLOCKING): REWRITE the 38 cot price keys under a
never-widen pair, not delete them.
- The rewrite removes the 49F-sourced rows and re-prices the three bonds from Cottonwood's source of record (Yahoo as-traded). Every
  other row stays byte-identical, proven by a per-key diff.
- The pair names all 38 keys with their prior VersionIds; rollback is `copy-object`.
- Deleting the old versions is Andrew's act, listed for him.
- The as-traded FWD-3 rebuild (round 34 CB-ah-3) reads the REWRITTEN keys, and is sequenced after.

Round 34 stays open. Its COO half @64b302f3a8 is SUPERSEDED because its build read the unrewritten store. CB-ah-3 is re-pointed by an
amendment after this round's rewrite lands.

**Rule 24.** Domain: one item (the rewrite) -> two cells:
- `CB-aj-1`, LOCAL + Yahoo: build the 38 rewritten files locally, prove the diff, run the writer census;
- `CB-aj-2`, SERVED: write the 38 new versions under the pair.

## Measured constraints (issuer, ~12:3xZ)

1. `opal-data-cot` versioning reads `Enabled`. The store `silver/prices/canonical_prices.parquet` reads VersionId
   `5JN8rkV4dcE.v64dYVAA6PR5jccvS8Rc`, LastModified 2026-06-09T20:42:16Z, unchanged since round 35.
2. The 38 keys with their versions are section 5 of `deliverables/0.9.0_WK_ADVI_COTBKF~63/bd_txn_provenance.md`. All were written
   2026-06-09T20:42:15-16Z.
3. **The bonds are 05613L3H2 (BNP Paribas), 95000U2D4 (Wells Fargo 4.15% 2029) and 651639AX4 (Newmont 2.8% 2029).** Their equity tickers
   are what mis-priced them originally (the 49F exceptions file's own `reason` field). Whether Yahoo carries a usable series for the
   BONDS is unmeasured. CB-aj-1 measures it, and the pair covers BOTH branches:
   - found: the rows are re-priced from it;
   - not found: the 49F rows are removed with no replacement, the bonds read unpriced, and a BLOCKING row is filed for a source ruling.
4. **Writers of the named property:** the cot gold run (SSM doc in `infra/aws/terraform/cot-pipeline/ssm.tf`). No key has moved since
   2026-06-09. CB-aj-1 counts the writers and their schedule, because a scheduled writer would overwrite the rewrite.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-aj-1` | build the 38 rewritten price files locally: 49F rows out, bonds re-priced from Yahoo or left unpriced, per-key diff, writer census | FWD-3 | WORLD | none | `0.9.0_WK_ADVI_COTBKF~64` |
| `CB-aj-2` | write the 38 new versions to `opal-data-cot` under the pair; read back | FWD-3 | SERVED | CB-aj-1, both pair halves | `0.7.0_AE_CloudOps~CB2` |

**Fan-out:** `1 of 2 chains now, cap 8`. `CB-aj-2` is spawned after `CB-aj-1` drains and both pair halves exist.
