# 0.4.0_DS_ClientPlatform — work_1420Z (ADVI_COTETL: cot_silver_merge.py)

**archetype:** IMPLEMENT

## Summary

COO DRIVE dispatch received (141521Z): write `data/cot/scripts/silver/cot_silver_merge.py` — COT silver v1 (transactions + allocations). Ported from `merge-daily-incremental.py`, adapted for COT specifics. Gated, committed, RAVC2'd COO + AE.

## Key technical outcomes

- **Script written:** `data/cot/scripts/silver/cot_silver_merge.py` (430 lines)
- **Commit:** 8225d26bc
- **Gate:** ds-commit-gate PASS (py_compile + AST undefined-name + ruff + comp-constants — all clean)
- **Interface:** `--table {transactions|allocations} [--date YYYY-MM-DD] [--compact]`
- **Dedup:** transactions = transaction_id keep='first'; allocations = (account_id, as_of_date) keep='first' (rep-split collapse → ~$372.9M AUA)
- **COT-specific:** BD_S3_BUCKET=opal-data-cot default, BD_FIRM_ID=cottonwood (provenance only), no cusip enrichment, no bd-price-update Lambda trigger

**Schema anomaly caught + resolved:** comp-constants gate flagged variable named `FIRM_ID` as drifting from BD canonical '49financial'. Root fix: renamed to `BD_FIRM_ID` (per COO dispatch spec) — no canonical drift in deployed artifacts.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| comp-constants (via ds-commit-gate) | cot_silver_merge.py | Initial: DRIFT (FIRM_ID='cottonwood' vs BD canonical '49financial'). Root cause: variable name collision. Fix: rename to BD_FIRM_ID. Final: PASS |
| py_compile | cot_silver_merge.py | PASS |
| ds-precommit-check (AST) | cot_silver_merge.py | PASS |
| ruff check --target-version py39 | cot_silver_merge.py | PASS |

## Files Modified

| File | Change |
|------|--------|
| data/cot/scripts/silver/cot_silver_merge.py | NEW — COT silver incremental merge v1 (transactions + allocations) |

## RAVC2 Sent

- COO (2.0.0_SA_COO): COMPLETE, gate PASS, commit 8225d26bc, schema anomaly noted
- AE (0.6.2_AE_PartnerETL): deploy to opal-data-cot/code/silver/ + SSM doc

## Next Steps

- AE: deploy cot_silver_merge.py to S3 + create SSM doc
- Tonight ~02:30Z: COT bronze first run (EventBridge ENABLE pending AE)
- Tonight ~23:00Z: GLDINC P0 first incremental + P1 first shadow — pull logs + scorecard
- Self-directed: realized(qt3) + unrealized(qt4) templates for COT (future increment, needs GO)

work-cycle:0009
