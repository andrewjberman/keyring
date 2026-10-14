# IRPT_ANLREQ -- decomposition, round 38A: THE WORDS FOR A SHARES FILE THE DOOR CANNOT PRICE, workstream ZC round 38 (issuer 2.0.0_SA_COO~Y2)

**Input:** row `IRPT_ANLREQ-D2-S94` (the release-28 door sitting, line D3) and the CTO's ruling (msg 7546, item 1): FWD-1's first journey is proven with a market-value file; Shares is an enrichment. A Shares file keeps answering NEEDS_CORRECTION (the Shares price source is not composed: `intake/upload_resolution.py :112`, `:133`), "but in plain words asking for a market-value column". The issuer's check of the words found none: `SHARES_PRICE_SOURCE_NOT_COMPOSED` has no entry in `CORRECTION_WORDS` (`intake/uploads.py`, `ops/status.py`), so a person is turned back without a sentence.

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-308` | the words for `SHARES_PRICE_SOURCE_NOT_COMPOSED` (and for any other not-composed code a person can reach and that has none) in BOTH tables, byte-equal; the table-lock count edit; at least 6 new tests; a census of every `_not_composed` code; `ops/status.py` words-only by AST | `intake/uploads.py`, `ops/status.py`, the two test files, the worker's record folder | WORLD (an infrastructure path) |

## Edges and chains

- One chain. Not in this round: the release (the door Lambda, `irpt-status` and the resident carry these tables: a pair after the authorizer's cell, one window if the CTO agrees), the Shares price-source READ cell (the next enrichment), the erratum to the release-28 pair (written, `ERRATUM_1_SECTION_4B_SHARES.md`).

fanout: 1 of 1 chains, cap 8, reason: two tables that must stay equal are edited by one author.
