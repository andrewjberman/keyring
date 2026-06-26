# Session log — 0.3.1_RD_PortfolioManagement~B — 2026-06-03 ~1746-1803Z

**Agent:** 0.3.1_RD_PortfolioManagement~B (MSTR-spawned, Andrew-direct)
**TO:** PMTRDX.001 — PM export -> Trade Submission weight ×100 (bps rendered as percent). Yang-reported, Andrew-direct, HIGH/trade-integrity. CTO-authored, COO-dispatched.
**Outcome:** Traced + determined + 4 patches prepped & validated & handed to AE. CTO+COO accepted. Awaiting AE deploy + gated remediation + CVO e2e verify for project close.

---

## Startup
- `/watcher`: was NOT REGISTERED -> registered LIVE (PID 23612); armed persistent inbox Monitor (task `b5bujpk2y`); pulled inbox (1 msg = the TO). No stale `/watcher` cron.
- Loop: armed `/work` cron `b4734972` (every 20m) per LD-0082.

## The bug (symptom)
PM portal "export to Trade Submission" -> a 20bps (0.20%) buy renders as "20% buy" in Trade Details (×100).

## Trace (end-to-end, code + ACTUAL served artifacts)
Unit conventions across the chain:
- **PM domain = PERCENT-NUMBER** (0.20 = 0.20%). Proven: `types/portfolio-optimization.ts:29` "Portfolio weights (%)"; PM grid `TradeTable.tsx:313` renders `delta.toFixed(2)%` with NO ×100; `TradeRecord` sample `1.239026`=1.24%.
- **Trade-submission domain = DECIMAL FRACTION** (1.0 = 100%). Proven: `fileParser.ts:205` "store as decimals, display as percentages"; `SecuritiesTable.tsx:226-239` (/100 in, ×100 out); `TradeDetailsModal.tsx:169-176` (×100); and production MANUAL submissions store fractions (INTU `current_weight 0.0716`=7.16%, NVDA `0.0938`=9.38%, BK `0.0048`=0.48%).
- **The boundary that breaks:** export-and-submit Lambda `infra/aws/lambda/portfolio_excel_generator/lambda_function.py` `build_trade_securities()` (L123-144) copied PM percent-numbers STRAIGHT into the DynamoDB `securities[].{current_weight,proposed_weight,delta}` with no percent->fraction conversion. The fraction-contract FE then renders ×100.

Served-artifact evidence (read directly, not a proxy):
- DynamoDB `opal-trade-submissions` `TRADE-20260602-135824-9CHHWS` (Yang, PENDING_APPROVAL, source=portfolio_export): stores `DELL proposed_weight "0.2"`, `AMD current_weight "2.12..."` (percent-number strings).
- Vident Trade CSV `s3://opal-data-portal-v2/portfolio-management/exports/PFDE/v_12dd9834_20260602_135824_trade.csv` (the canonical broker order): `DELL Proposed Weight 0.200000` = 0.20% = 20bps. **CORRECT.**
- `TradeDetailsModal.tsx:172` renders `0.2*100` = "20.00%" (and AMD `2.12` -> "212.00%") = Yang's symptom.

## DETERMINATION (the headline)
**NOT a live 100× bad-trade. The broker ORDER is CORRECT** (Vident CSV = 0.20% for 20bps). The ×100 is a **stored-record + display unit-contract violation** on the DynamoDB `securities[]` field. Additionally surfaced: a 3rd, different convention in the downstream execute/download Excel generators (`trade-pipeline/{trade-workflow-handler,trade-dashboard-api}/src/excel_generator.py`) — they ÷100 current/delta + plain proposed, i.e. expect percent-numbers, so they ALREADY misrender the manual fraction records (pre-existing latent bug).

## CTO ruling (1.0.0_SA_CTO, ws-charter cycle 0021)
Canonical unit for `opal-trade-submissions` `securities[]` weights = **DECIMAL FRACTION** (RD~B rec approved). PM Lambda + 2 Excel generators are the deviants. GO prep the one coherent backend fix set; AE deploys.

## Patches PREPPED (working tree, CLOUD; NOT deployed — Rule 1, AE deploys)
1. `portfolio_excel_generator/lambda_function.py` — `build_trade_securities` ÷`PCT_TO_FRACTION(100.0)` on current/proposed/delta -> fraction; added `weight_unit:'fraction'` marker to submission put_item. Vident `generate_trade_csv`/`generate_vident_excel` UNTOUCHED (broker order stays correct).
2. `trade-workflow-handler/src/excel_generator.py` + `trade-dashboard-api/src/excel_generator.py` — aligned to fraction: drop /100 on current+delta; proposed format '0.00'->'0.00%'; delta format '0%'->'0.00%' (so 20bps shows 0.20% not rounded-to-0%); empty-row formats too. Fixes the pre-existing manual misrender as well. NO-CONSUMER confirmed (Excels are human downloads; no code parses them back).
3. `portfolio_excel_generator/remediate_weight_unit_pmtrdx001.py` (NEW) — one-time remediation: DRY-RUN default (count+samples, no write); scope `source=portfolio_export AND status=PENDING_APPROVAL AND weight_unit!=fraction`; marker-IDEMPOTENT (authoritative guard — corrected CTO's `<1.0` heuristic which would wrongly skip genuine sub-1% records); `--apply` ÷100 + stamp marker + re-pull/verify. `--apply` GATED (CTO sign-off + Andrew-aware; COO runs).
4. `portal/src/api/endpoints/trade-submission.ts` — canonical-unit contract note on the `TradeSecurity` type (durable root-cause guard; contract had lived only in fileParser, invisible to the PM-Lambda author). Comment-only; rides next portal/DEV promote; not coupled to backend deploy.

VALIDATION: `python -m py_compile` all 4 .py OK; `ruff check --target-version py39` clean on the new script.

## Regression matrix (post-fix, fraction canonical)
| Intent | PM (percent#) | Lambda stores (÷100) | FE display (×100) | Vident CSV (unchanged) |
|---|---|---|---|---|
| 1bps | 0.01 | 0.0001 | 0.01% | 0.010000 |
| 20bps | 0.20 | 0.0020 | 0.20% | 0.200000 |
| 250bps | 2.50 | 0.0250 | 2.50% | 2.500000 |
| 100% | 100.0 | 1.0000 | 100.00% | 100.000000 |
| sell | -0.37 | -0.0037 | -0.37% | -0.370000 |

## Handoff / sequencing
- Delivered to `0.7.0_AE_CloudOps` (CC COO+CTO). AE ACK: it's theirs to TF-deploy (Rule 1); COO ruled PMTRDX non-urgent (no trade exposure) -> AE QUEUED behind the live Andrew security walkthrough.
- Pipelines: #1 = `infra/aws/terraform/portfolio-management` (fn `opal-portfolio-excel-generator`); #2 spans `trade-pipeline` (2 fns). Remediation = standalone ops script (exclude from Lambda artifacts).
- AE sequence: deploy #1+#2 (TF/safe-apply, source-map, tag) + run #3 in the SAME window (coherence — minimize mixed-unit display window; marker makes it order-safe). #3 dry-run -> share count/samples -> `--apply` on COO/CTO/Andrew gate.
- Out-of-ruling-scope flag: APPROVED/EXECUTED portfolio_export records also display ×100 historically (orders were correct via CSV); script status-filter can widen if COO wants them cleaned.
- CVO e2e close gate (CTO): 20bps -> 0.0020 stored -> FE 0.20% -> downstream Excel correct -> Vident still 0.200000 + remediated-record parity. CTO releases the PMTRDX close on CVO GREEN.

## Artifacts
- Determination brief: `docs/briefs/pm-export-trade-submission-weight-x100-determination-20260603.md`
- Patches: the 4 files above + the new remediation script.

## Status at log time
My lane work-product COMPLETE + accepted by CTO+COO. Not closed yet (pending AE deploy + gated remediation + CVO verify). Reachable (Monitor `b5bujpk2y`); loop armed (cron `b4734972`).
