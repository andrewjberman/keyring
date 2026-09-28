# ANDREW-DIRECT 2026-09-28 ~12:4xZ at the 1.0.0_SA_CTO terminal -- the canonical classification table

**Verbatim:**
- "The only classification table that matters is whatever ETFClassifier is connected to, the DDB table and associated
  infra that feeds into the "Positioning" POSN page."
- "THat is the canonical table."

## What it names (measured by this seat, read-only)

- **The canonical table is DynamoDB `etf-classifications`:**
  - `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py:52`, `ETFClassifier(table_name="etf-classifications")`;
  - it feeds `yang_pipeline/positioning/yang-generate-positioning` (the POSN page).
  - Key `ticker`; 285 items (a full scan, no further page).
- **Owner:** the D4 POSN project (POSN_ASTTAX, whose worker deliverables write and census it).
- **Not canonical:** `bd-securities` (10,929 items), which the BD and COT gold classifiers read today:
  - `data/cot/scripts/gold/lib/etf_classifier.py:42-47`;
  - `data/black_diamond/scripts/gold/lib/etf_classifier.py:48-53`.

## Effect on IRPT_BCKEND-S173 (COT gold served equity 85.8% vs 52.5%)

1. The `bd-securities` read grant for the COT role (CTO 01:09Z REC) is WITHDRAWN, and the governance fork pitched to
   3.0.0_SA_CVO is moot: the question is no longer which firm's table, but which table is canonical.
2. The COT gold classifier reads `etf-classifications`, as ETFClassifier does. The same class applies to the BD gold
   classifier: a finding row, to be driven with it.
3. **Coverage gap:** FXNAX (the S173 example) is ABSENT from the canonical table. A coverage census of the served COT
   (and BD) holdings tickers against `etf-classifications` names the gap. Missing tickers are added through the canonical
   table's own writer by its owner (POSN, D4), never written from an IRPT seat.
4. ~M's held COT acts (the cash-line deploy, Part 2) stay held until the COT classifier reads the canonical table and
   their halves are re-measured on served.
5. Moving served COT classification is a served-output move: a never-widen packet with two halves.
