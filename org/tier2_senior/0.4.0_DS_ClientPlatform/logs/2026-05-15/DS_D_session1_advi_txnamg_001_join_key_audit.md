# DS~D Session 1 — ADVI_TXNAMG.001 Join-Key Probe + Column Audit + Schema Parity

**Agent:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-05-15
**TO:** `ADVI_TXNAMG.001.dsd-join-key-probe-column-audit` (COO-issued) — read-only investigation
**Status:** COMPLETE — deliverable brief shipped, RAVC2 to COO + CC CTO.

## Current State

TO-1 of `ADVI_TXNAMG` (Transaction Silver Amalgamation) — the read-only investigation that
gates TO-3 (the amalgamating writer). Delivered an evidence-bearing brief at
`docs/briefs/txnamg-001-join-key-column-audit-20260515.md` with all three required verdicts.

## What I Did

Three empirical S3 probes (`txnamg001_probe.py` → `txnamg001_result.json`, workspace root):

1. **Join-key probe.** REST bronze `bronze/transactions/2026-05-15.parquet` (1.3M-row full-history
   snapshot) vs Custom-Report `bronze/orion-api/2026-05-13/transactions.csv` (20,212 rows).
   - REST `id` ≡ CR `Transaction ID`: **100.00% match** (20,212/20,212), 0 non-joining.
   - `orderId`/`tradeOrderId`: **100% NULL in REST bronze** — definitively not the key.
   - Cross-era: 100% on 2026-05-08/2024/2023; 94.52% on 2021-06-15 — the 36 non-joiners
     traced to 4 accounts absent from the REST spine (closed/merged-out accounts the REST
     `/Accounts/{id}/Transactions` pull no longer iterates). Spine-coverage property, not a
     key defect. Flagged for TO-3.

2. **Column-correspondence audit.** Inner-joined 20,212 overlap rows; value-compared all 29
   CR CSV columns against REST. Result: **17 ALIAS / 1 borderline / 11 CARRY.**
   - Ambiguous cases resolved by value inspection: `AcctCode`≡`accountNumber` (100%),
     `Reg Type`≡`registrationCode` (100%), `TranNotes`≡`notes` (100%),
     `Dwnld Symbol` DISTINCT from `ticker` (94% equal, 6% CUSIP — carried),
     `Description`==`Product Name` (100% — dupe of `productName`, not carried),
     `CreatedBy` DISTINCT (REST `orderCreatedBy` 100% NULL — carried),
     `fkTradeStatus` vs `status` (encoding variant — recommend not carried).
   - **Definitive 11-column carry set:** `LName`, `Activity Category`, `Dwnld Symbol`,
     `CreatedDate`, `CreatedBy`, `EditedDate`, `EditedBy`, `RepName`, `CurrentAccountValue`,
     `CurrentCashValue`, `Managed Account`.

3. **Historical schema-parity.** 14 CSV headers sampled 2020-05-26 → 2026-05-14 (backfill-era
   + daily-era): **identical 29-col header across all**. No per-era delta — TO-3 needs no
   reconciliation logic.

## Findings beyond the TO scope (surfaced in the brief)

- **CSV header whitespace:** the CR CSV header has `' Reg ID'` with a leading space; the
  current `convert_orion_api_to_silver.py` `keep` dict misses it → `reg_id` silently dropped
  from deployed CR silver. Moot for TO-3 (`reg_id` is an alias, not carried) but TO-3 must
  `.str.strip()` CR CSV headers.
- **Deployed writer-#3 silver is 31 cols**, not the 44 the repo `build_transactions` would
  emit — deployed Lambda copy predates the 2026-05-08 RICH augmentation. Moot (TO-4 removes
  writer #3's silver-write; the join sources the CSV directly).
- **Spine-coverage gap:** left-join-onto-REST-spine drops closed-account CR transactions
  (~5% of deep-backfill rows). PRD §4.1 specifies left-join; if closed-account history must
  be preserved a UNION decision is needed — surfaced for TO-3/PRD, not re-scoped here.

## Compiler Tools

| Tool | Run? | Result |
|---|---|---|
| `comp-pipescript io` | No | Per TO `<compiler_tools_mandate>` + PRD §5.2: comp graph does not model `manual_api/` pull scripts or the `silver/transactions/` artifact (documented coverage gap). Empirical S3 probes are the sanctioned authoritative basis for this investigation TO. P2/P3 N/A — read-only, no commit/deploy. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **COO 2.0.0** | RAVC2 — AC1-5 all PASS; TO `ADVI_TXNAMG.001` complete. Brief: `docs/briefs/txnamg-001-join-key-column-audit-20260515.md`. Release TO-3 `dispatch_held` on validated receipt. |
| **CTO 1.0.0** | CC on RAVC2 — one decision item: `fkTradeStatus` classified ALIAS (recommend not carried); CTO may override if the raw FK integer is wanted. |
| **DS~D (self)** | TO-3 (`ADVI_TXNAMG.003`, same receiver) is `dispatch_held` pending COO release of this brief. /loop watchdog standby until GO. |
