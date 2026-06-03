# ws-charter — 2026-06-03 1748Z — PMTRDX.001 canonical-unit RULING (FRACTION)

**CLASS:** FIX (architectural ruling — data-contract canonical unit). Unblocks RD~B deploy [BLOCKED-ASK].
**Trigger:** RD~B RAVC2+RULING-ASK (`20260603T174701Z`); brief `docs/briefs/pm-export-trade-submission-weight-x100-determination-20260603.md`.

## Determination accepted (RD~B, verified vs served artifacts)

NOT a live bad-trade — Vident broker CSV correct (DELL 0.200000 = 0.20% = 20bps). The ×100 is a DISPLAY bug: PM-export Lambda writes PERCENT-NUMBER (0.20) into opal-trade-submissions `securities[].{current,proposed,delta}`, but the domain canonical is DECIMAL FRACTION (0.0020) — FE renders `proposed_weight*100` (TradeDetailsModal:172) → shows 20%. 3 unit-handlings in the wild: FE/manual/fileParser = FRACTION; PM Lambda = PERCENT-NUMBER; downstream execute/download Excel = percent-number-ish (already misrenders manual fractions today).

## RULING — canonical = FRACTION (decimal). RD~B recommendation APPROVED.

Evidence triangulates: (a) `fileParser.ts:205` explicit documented intent "store as decimals, display as percentages"; (b) manual prod records already fraction (0.0716=7.16%); (c) type system + SecuritiesTable + primary FE encode fraction. So FRACTION is the documented + de-facto canonical; PM Lambda + the 2 Excel generators are DEVIANT writers/readers (the Excel ones already-buggy vs manual records — fixing them corrects a PRE-EXISTING latent bug, not a new break).

**FIX SET (approved, all backend → AE deploy, Terraform/safe-apply Rules 1/2/18; RD~B preps patches):**
1. PM Lambda `portfolio_excel_generator/lambda_function.py build_trade_securities` (L123-144) ÷100 → write FRACTION. (Fixes Yang's symptom + aligns PM with manual.)
2. Align the 2 downstream `excel_generator.py` (trade-workflow-handler + trade-dashboard-api) to fraction: drop /100 on current/delta, add %-format on proposed. (Corrects the pre-existing manual-record misrender too.)
3. One-time ÷100 remediation of existing `source=portfolio_export` PENDING records.
**Vident CSV/Excel stay PERCENT-NUMBER (UNCHANGED)** — correct for the Vident broker template; the order is already right. Only DynamoDB-record + FE/Excel-consumer side changes.

## Conditions on the ruling

- **#3 remediation = prod-data mutation → EXTRA care (the one risky piece):** scope STRICTLY to `source=portfolio_export` + status PENDING (NOT manual records — already fraction); IDEMPOTENT (guard against double-÷100 on re-run, e.g. a remediated-marker or value-range check); DRY-RUN + count + sample-verify BEFORE the write; verify against actual records after. NOT a blind script. (Lower stakes than feared — PENDING tracking-records, broker orders already correct — but still live data.) Andrew-awareness flagged (his bug-fix directive covers it; not a separate gate).
- **Coherent landing:** #1 + #3 land together (no window where new fraction-writes coexist with un-remediated percent-number records confusing the FE). #2 rides along; verify no consumer depends on the current percent-number Excel output before flipping it.
- **Root-cause durability:** the deviation happened because the canonical-unit contract was documented only in fileParser, not enforced/visible at the `securities[]` type. Add an explicit canonical-unit contract note at the type definition so the next writer can't silently deviate.
- **CVO verify on close:** end-to-end served-artifact verify — 20bps PM export → stores 0.0020 (fraction) → FE shows 0.20%/20bps → Excel download correct → Vident CSV still 0.200000. + remediated-record served-parity.

## Routing / follow-on

- Ruling → RD~B (unblocks; prep exact Lambda patches + remediation script for AE) + COO (deploy-coordination, the RAVC2 BLOCKED-ASK resolves) + AE (executes deploy + remediation under the #3 conditions).
- Rides a backend deploy (AE) + the FE side already correct (no FE change needed — FE was right; the data was wrong). CVO verify on close.
