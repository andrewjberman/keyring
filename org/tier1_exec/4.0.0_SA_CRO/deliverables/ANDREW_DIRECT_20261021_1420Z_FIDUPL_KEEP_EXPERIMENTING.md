# ANDREW_DIRECT 2026-10-21 ~14:20Z -- NFRA_FIDUPL: keep experimenting with the backfill depth

- Channel: in-session, Claude Code terminal, dell1, to 4.0.0_SA_CRO~FIDELITY. Time ~14:20Z (10:20 AM ET).

## Verbatim
> Let's keep experimenting and see where they gio

## Scope (surfaced, not adjudicated)
Keep probing empirically how far back each Fidelity surface serves; land what it gives; report what is found. Read-only,
spaced runs (throttle), no account values committed. The runs are 2.0.0_SA_COO~P1's; the CRO frames the experiments and
reports depth.

## Experiments worth running (CRO list)
1. Transaction floor: per-account historical-transactions, timePeriodOption="custom", step the from-date back 1y/2y/3y/5y until EMPTY.
2. Does the Historical export reach deeper with different fileTypes/indicatorName combos, or per file type (positions already ~128d)?
3. Other dated surfaces: statements/getDocumentsSearchResult (date range), realized gain/loss history, open-lots / tax-lot history, tax documents.
4. The standard-format on-demand export with an early transaction date, vs the custom API -- compare reach.
