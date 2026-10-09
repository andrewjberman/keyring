# ADVI_COTBKF decomposition -- ROUND 44 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~14:4xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s CB-ap-2 CTO half @d92ed8390f (msg 3486), which places a stale-pin item "as one LOCAL line next
issuance": the silver-prep census compares the served and repo `scopes.json` sha256 values and STOPS on a mismatch.

The reason: round 42 deploys a PINNED copy of `infra/logic/registry/scopes.json` at `code/gold/scopes.json` (blob 261c0cf8). When the
repo's file changes, the served pin goes stale silently, and the price writer's `source_firm` resolution would read outdated scopes.

**Rule 24.** Domain: one item -> one cell, LOCAL.

## Measured constraints (issuer)

1. The silver-prep census is `data/assets/scripts/silver/commonwealth_cot_price_rewrite.py --source-firm-only` (CB-an-1). D2-S62
   closes on its read.
2. The served pin is `s3://opal-data-cot/code/gold/scopes.json` (minted by round 42's CB-ap-2, now applying). The repo file is
   `infra/logic/registry/scopes.json`.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ar-1` | the `--source-firm-only` census first compares the sha256 of the served `code/gold/scopes.json` against the repo `infra/logic/registry/scopes.json`, and STOPS (non-zero, no census) on a mismatch or a missing pin; test | FWD-3 | LOCAL | none | `0.9.0_WK_ADVI_COTBKF~71` |

**Fan-out:** `1 of 1 chains, cap 8`.
