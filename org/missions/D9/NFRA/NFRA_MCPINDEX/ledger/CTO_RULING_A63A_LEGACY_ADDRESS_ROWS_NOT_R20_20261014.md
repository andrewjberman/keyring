# NFRA_MCPINDEX -- CTO ruling on call sitez-20261014T015958Z-a63a: legacy_addresses rows, NOT an R20 exception (`1.0.0_SA_CTO~Z`, 2026-10-14 ~02:1xZ)

**The call:** the naming gate (LGIC ENFORCE) refuses six existing hyphenated `opal-data-harvest` keys as new
out-of-pattern literals (row Z-W34-S6):
- `amgt/harvest/gold/research-backlog`
- `research-continuation`
- `research-dossier`
- `research-fund-form`
- `research-model-typecast`
- `research-sector-template`

So row 12b's catalog rows cannot land, and c9.AC2 reads 1 of 7. The REC was an R20 declared exception.

## Ruling: NO R20. Add six rows to `infra/logic/registry/legacy_addresses.json`.

- **R20 is for a deliberate departure in what a pipeline BUILDS,** and it needs Andrew's sovereign acknowledgement
  (`infra/logic/02_DOCTRINE.md` R20). This is not that. It is a READ of keys that already exist and predate the canon.
- **The canon has a registry for exactly that.** `lib/opal_naming.py:794`: "legacy_addresses.json: a READ address for a
  store that predates the canon". CLAUDE.md rule 30: "a builder REFUSAL is a missing registry row to add
  (`infra/logic/registry/`), never a hand-typed workaround".
- **Precedent:** ADVI_COTBKF's Cottonwood price keys (@9cfa6f9584, @c904299ad5), read through `legacy_address()`.
- Nothing is renamed and nothing new is built. The producer's tables reach conformance through AMGT_HARVST's own
  migration (R19), never as a rider here.

## The rows (closed field set `LEGACY_FIELDS`: key, bucket, template, shape, params, reader, evidence, note)

One row per hyphenated table:

| field | value |
|---|---|
| `bucket` | `opal-data-harvest` |
| `template` | `amgt/harvest/gold/<table>/` |
| `shape` | `prefix` |
| `params` | `[]` |
| `reader` | `NFRA_MCPINDEX` |
| `key` | a lowercase kebab key per table |
| `evidence` | the list-objects read that shows the prefix exists |
| `note` | AMGT_HARVST owns any rename (R19) |

The catalog rows name each key through `legacy_address()`, never the literal.

- **If the validator refuses `bucket` because `opal-data-harvest` is not a bucket `scopes.json` knows,** that is one
  more missing registry row, in `scopes.json` or `bucket.standing_shared`. It is added the same way, never with an R20
  or an override.
- **The seventh table, `research_dossier`** (underscored), already passes and is unchanged.

**Issuer:** `2.0.0_SA_COO~MI` adds the six rows as a cell, or as an amendment to round 11's H1 if H1 is not yet drained.
The proof is `python lib/opal_naming.py` validate PASS plus c9.AC2 reading 7 of 7.

-- 1.0.0_SA_CTO~Z
