# ADVI_COTBKF decomposition -- ROUND 42 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~14:2xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 14 @9a98e3b0a1 (msg 3442). Round 40 is MET. The ruling has three parts:
- **W68-S2.** The writer's deploy ships the registry it reads, in the SAME pair: ONE SERVED cell with two keys under `code/gold/`.
  - The writer loads the registry from its own directory, with no new sync prefix and no second path.
  - The census shows exactly those two keys.
  - The proof is the next silver-prep census reading `source_firm=cottonwood` with `BREACH=0`, which closes D2-S62.
- **W68-S1.** Remove the dead share-class check in the same cell (YAGNI).

**Rule 24.** Domain: one SERVED act. Its code change is a worker's build, and the deploy is the applier's. So there are two cells, of
which only one is SERVED, matching the ruling's "one SERVED cell":
- `CB-ap-1`, LOCAL: the code change and its tests;
- `CB-ap-2`, SERVED: the two-key deploy under one pair.

## Measured constraints (issuer, ~14:2xZ)

1. **The deployed writer** is `s3://opal-data-cot/code/gold/build_canonical_prices_v2.py`, VersionId
   `4M4XPMtc2JCbbWi22WuxrVIaicQqPzy6`, LastModified 2026-06-12T20:07:45Z, 28,290 bytes. It is older than round 40's change; the repo
   file at HEAD carries `source_firm` (@ba35c04d1c).
2. `lib/opal_naming.lookup()` reads `infra/logic/registry/scopes.json` and, for the closed enumerations,
   `org/standards/NAMING_SCHEMA.json`. Which of these the writer's firm resolution actually needs is for CB-ap-1 to measure.
   - The ruling names ONE registry file. If the writer needs more than `scopes.json`, the cell reads only the fields it needs from one
     file, or names the gap as a row.
3. The gold run syncs only `code/gold/` (`gold_dispatch.sh`:497-498).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ap-1` | the writer resolves `source_firm` from ONE registry file in its own directory (pinned copy); the dead share-class check removed; tests; no deploy | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~69` |
| `CB-ap-2` | deploy the writer and its registry file as TWO `code/gold/` keys under ONE pair; read back | FWD-3 | SERVED | CB-ap-1, both pair halves | `0.7.0_AE_CloudOps~CB2` |

**Fan-out:** `1 of 2 chains now, cap 8`.
