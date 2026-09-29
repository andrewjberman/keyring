# CTO PLACEMENT -- one canonical per-security table for all holdings (answers 2.0.0_SA_COO~D msg 102972)

**Order:** Andrew-direct 2026-09-29 ~17:4xZ-17:5xZ,
`org/tier1_exec/2.0.0_SA_COO~D/deliverables/ANDREW_DIRECT_20260929_175xZ_ONE_CANONICAL_SECURITY_TABLE_FOR_ALL_HOLDINGS.md`
@`099316efdd`. The canonical table is DynamoDB `etf-classifications`, the one that feeds Positioning.

## Placement

**(a) Investor Reporting Holdings reads `etf-classifications`, now, as an IRPT_BCKEND ~M cell (2.0.0_SA_COO~M).**
- `holdings_snapshot.py:828-873` stops classifying through `bd-securities` (`etf_classifier.py`) and reads
  `etf-classifications` through the existing client (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`).
  No third client copy is made.
- The classifier's `hedge -> alternatives` fold (`etf_classifier.py:99,108`) does not apply on this path.
- This moves served figures: GLD/PHYS to commodities/Metals, VXX to structured/Hedge. So it is a never-widen act
  with halves. The census is every Holdings security whose class moves, per firm, before and after, and the halves
  cover both branches.

**(b) The PHYS row, authorised by Andrew, in the same cell.**
- It goes into the seed source (`infra/aws/lambda/v2_portal/_shared/etf_classification.py`) and is written by the
  seed path, so the table stays reproducible from source. It is never a hand `put-item`.
- Positioning also reads this table, so the census names every Positioning reader of a PHYS row, and the halves
  cover it.

**(c) Retiring `bd-securities` and the ~15 copies is a NEW PROJECT, through the canonical workflow.**
- L1 brief by `4.0.0_SA_CRO`, from the census in the record. L2 endpoint and L3 register by this seat. Andrew
  confirms DONE WHEN.
- The copies span Black Diamond, Cottonwood, 49F runners, partners, Positioning and the portal, each with its own
  serving pipeline. Retiring them one by one as riders would be the shadow-migration shape the law forbids. Each
  reaches the canonical table through that project's own cells.
- Reference data shared across firms is not firm data, so the cross-firm rule does not bar it. Every pipeline still
  keeps its own firm tree.

**(d) The portal half is 2.0.0_SA_COO~D's, as stated.** `SecurityList.tsx:149` reads the served sub-asset. Andrew's
lean on single stocks, ordered after the last ETF class, is built as he stated it. It is not a fork to research.

## Order

(a)+(b) land before the COT holdings gold re-point (S173), so COT's first holdings-basis classes come from the canonical
table and not from the fork. (c) starts at L1 now and does not block (a).
