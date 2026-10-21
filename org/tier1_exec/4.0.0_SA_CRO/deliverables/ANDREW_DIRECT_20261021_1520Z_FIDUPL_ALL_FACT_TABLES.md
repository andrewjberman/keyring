# ANDREW_DIRECT 2026-10-21 ~15:20Z -- NFRA_FIDUPL: every Fidelity fact table, as silver parquet

- Channel: in-session, Claude Code terminal, dell1, to 4.0.0_SA_CRO~FIDELITY. Time ~15:20Z (11:20 AM ET).

## Verbatim
> yes we definitely want ALL fact tables, open tax lots, realized gain/loss, unrealized gain/loss, we need absolutely everything.

## Scope (surfaced, not adjudicated)
Beyond the 6 daily export files, land EVERY Fidelity data surface as a fact table, converted bronze .txt/JSON -> silver parquet,
explicitly including open tax lots, realized gain/loss and unrealized gain/loss. "Absolutely everything." The CTO scopes the build
(PRD addendum to NFRA_FIDUPL or a sibling silver/extraction project); the catalog of surfaces is RESEARCH_20261021_NFRA_FIDUPL_FULL_FACT_TABLE_CATALOG.md.

## Addendum ~15:28Z (VERBATIM)
> i would like to structure fidelity as close to schwab as possible if we are building it our style right out the gate, so that there
> is minimal coalescing needed. if we could do it in a manner where silver fidelity and silver schwab were actualy formulated the exact
> same way, that would be lovely. I expect there to be a need to handle this in a master gold layer though.

Design directive: **Fidelity silver is built to the SAME schema as Schwab silver** (same `fact_*`/`dim_*` table names, columns, grain), so
downstream code cannot tell custodian apart at silver; a **master gold layer coalesces** across custodians (a `custodian`/`source` column).
This is a DS/CTO architecture decision; the mapping is in the catalog.
