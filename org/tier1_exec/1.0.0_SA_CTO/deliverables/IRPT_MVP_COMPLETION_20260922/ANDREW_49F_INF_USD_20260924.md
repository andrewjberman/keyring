# Andrew-direct 49 Financial and Inflection report currency confirmation

Received directly by 1.0.0_SA_CTO on 2026-09-24 ~00:4xZ as the approval of /open-calls cards 1 and 2
(record ANDREW_DIRECT_20260924_004xZ_ALL_RECS_APPROVED_SEVEN_OPEN_CALLS.md). Recorded at
2026-09-24T00:45Z.

Cards as printed:
- CALL 1: Attest that all 49 Financial report amounts are USD? (yes/no) -- REC yes.
- CALL 2: Attest that all Inflection report amounts are USD? (yes/no) -- REC yes.

Andrew's answer, verbatim:

> all recs approved

## Implementation consequence

49 Financial (Schwab custody, SmartX membership, Tax SMA workbook) and Inflection (Orion custody,
Eclipse membership) report amounts may be denominated USD on this explicit firm-level authority. P
owns the shared currency authority binder and writes the two ANDREW_ATTESTATION records into
CurrencyAuthorities.json citing this record; M consumes them for the 49F and INF Holdings
publications. Preserve the attestation reference and date in private source evidence beside the
unchanged raw vendor bytes. Do not label it as a vendor-returned currency field. No vendor query.

Scope is report amounts for those two firms, exactly as for Cottonwood (ANDREW_COT_USD_20260923.md).
It does not settle security-native currency, FX, missing values, census or date failures, valuation
basis, fees or return methodology. A future contradictory explicit vendor currency is a source
conflict to adjudicate, never an overwrite of vendor evidence. No conversion is implied.
