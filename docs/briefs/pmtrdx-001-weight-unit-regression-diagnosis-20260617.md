# PMTRDX.001 weight-unit bug — re-diagnosis + turnkey fix spec (2026-06-17)

**Author:** 0.3.0_DE_TradingOperations (Andrew-direct)
**Status:** DIAGNOSIS COMPLETE — fix is a coordinated AE Lambda deploy + CTO-gated remediation. Portal display needs NO change.
**Trigger:** Andrew + Yang — PFDE trade submission `TRADE-20260617-144856-MKYYDP` renders weights ×100 too large (AMZN CURRENT 555.00% should be 5.55%).

---

## TL;DR

The PM-export trade-submission weights are stored as **percent-numbers** (5.55) when the
trade-submission domain's canonical unit is **decimal fraction** (0.0555). The portal
display multiplies by 100, so a percent-number renders ×100 too large.

The 2026-06-03 fix (CTO ruling `fa9dc3cb3`: canonical = FRACTION) shipped only **two of its
three legs**:
1. ✅ the type-contract doc-note in `trade-submission.ts` (rode portal v2.1.114 to PROD)
2. ✅ the one-time remediation script `remediate_weight_unit_pmtrdx001.py` (committed later, 2026-06-15, in DT custodial sweep `d17d45be0`)
3. ❌ **the actual going-forward producer fix (÷100 in `build_trade_securities` + `weight_unit='fraction'` stamp) was NEVER committed AND the Lambda was NEVER redeployed.**

So every PM-export submission since has regressed. **Both of Andrew's hypotheses are correct**:
the producer code change never made it into committed source (lost/overwritten before commit) *and*
the Lambda deploy never happened.

**This is NOT a bad trade.** Per the 2026-06-03 determination (`8e0702cd6`), the broker order is
correct — the Vident Trade CSV/Excel intentionally uses percent-numbers (the broker template
convention). This is a **display / stored-record integrity** bug only.

---

## Evidence (ground-truth, not self-report)

- **DynamoDB record `TRADE-20260617-144856-MKYYDP`** (live): AMZN `current_weight="5.54999..."`,
  `proposed_weight="5.04999..."`, `delta="-0.5"`; `source="portfolio_export"`; **`weight_unit` absent**.
  Percent-numbers, un-remediated, PM-export provenance.
- **Producer `infra/aws/lambda/portfolio_excel_generator/lambda_function.py` `build_trade_securities()`**:
  writes `current_weight=str(initialWeight)`, `proposed_weight=str(compute_final_weight)`,
  `delta=str(finalTrade)` — the portal sends these as percent-numbers, and there is **no ÷100**.
- **Git history**: all 6 commits to `lambda_function.py` are Jan–Feb 2026 (last 2026-02-27).
  `git log -S 'weight_unit'` and `git log -S '/ 100'` on the file are both **empty** — the fix
  never existed in committed history.
- **Deployed Lambda `opal-portfolio-excel-generator` LastModified = 2026-05-19T17:36:42Z** — never
  redeployed for the 06-03 fix (in fact predates the whole PMTRDX episode).
- **`remediate_weight_unit_pmtrdx001.py` docstring (lines 11, 26)** states the intended-but-never-done
  Lambda half verbatim: *"The going-forward fix divides by 100 in build_trade_securities() and stamps
  weight_unit='fraction'"* … *"Run #1 (Lambda deploy) and this in the SAME window."*

---

## The frontend / downstream inconsistency (Andrew's second question)

The portal **display** is the only contract-correct consumer. The stored field has **inverted**
unit assumptions across consumers:

| Consumer | File | Assumes stored is | On a percent-number record (today) | On a proper fraction record |
|---|---|---|---|---|
| Portal display | `TradeDetailsModal.tsx` / `SecuritiesTable.tsx` (`×100`) | fraction | 555% ❌ | 5.55% ✓ |
| Download/exec Excel — current | `trade-workflow-handler/excel_generator.py` col-5 (`÷100`, `0.00%`) | percent-number | 5.55% ✓ | 0.06% ❌ |
| Download Excel — proposed | same, col-6 (`raw`, `0.00`) | percent-number, plain | "5.05" | "0.05" ❌ |
| Download Excel — delta | same, col-7 (`÷100`, `0%`) | percent-number | ~-1% rounded | ❌ |
| Analytics parquet | `parquet_exporter.py` (pass-through) | — | inherits stored | inconsistent |

`trade-dashboard-api/src/excel_generator.py` is byte-identical to the workflow-handler copy (same bug).

Because the display and the Excel are inverted, you cannot fix one producer in isolation — the
producer and the Excel generators must move together to the canonical FRACTION unit.

---

## Fix spec (canonical = FRACTION; align everything to it)

### PATCH 1 — Producer: `infra/aws/lambda/portfolio_excel_generator/lambda_function.py`
In `build_trade_securities()` divide the three stored weights by 100:
```python
'current_weight': str(s.get('initialWeight', 0) / 100),
'proposed_weight': str(compute_final_weight(s) / 100),
'delta': str(delta / 100),
```
And in the submission `put_item` (the `is_submit_flow` block) add the idempotency marker:
```python
'weight_unit': 'fraction',
```
Leave `generate_trade_csv` (Vident broker CSV) and `generate_vident_excel` **unchanged** — the
Vident broker template is intentionally percent-numbers (contract note, `trade-submission.ts:44`).
The filter/`derive_instruction` thresholds stay in percent-number space (sign-only) — do not touch.

### PATCH 2 — Realign BOTH Excel generators to fraction
`trade-workflow-handler/src/excel_generator.py` **and** `trade-dashboard-api/src/excel_generator.py`
(identical). For the three weight columns, treat stored as a fraction and let Excel's `%` format do
the ×100 — one consistent convention:
```python
# col 5 current:  value=current_wt      number_format='0.00%'   (remove the /100)
# col 6 proposed: value=proposed_wt     number_format='0.00%'   (was raw value + '0.00')
# col 7 delta:    value=delta_wt        number_format='0.00%'   (remove the /100; '0%'->'0.00%')
```
(The `delta_weight` vs `delta` field-name mismatch is harmless — the fallback
`proposed_wt - current_wt` is correct in fraction space.)

### PATCH 3 — Remediate existing records (CTO-gated)
`python infra/aws/lambda/portfolio_excel_generator/remediate_weight_unit_pmtrdx001.py --apply`
— idempotent (skips records already stamped `weight_unit='fraction'`), scoped to
`source=portfolio_export` + `PENDING_APPROVAL`. Fixes today's record + every PM-export submission
since 2026-06-03. Per its own SAFETY block: CTO sign-off + COO gate + Andrew-aware; run in the SAME
deploy window as PATCH 1+2.

### Sequencing (critical)
Deploy PATCH 1 + PATCH 2 in ONE deploy, then immediately run PATCH 3. Order matters: while the new
producer/Excel expect fractions, any not-yet-remediated record is briefly mismatched in the Excel —
minimize with same-window discipline (PENDING_APPROVAL trades are not mid-execution).

### NO change to the portal
`TradeDetailsModal.tsx` / `SecuritiesTable.tsx` are already contract-correct (expect fraction, ×100).
Manual SubmitTab submissions already store fractions.

---

## Related latent finding (separate, lower priority — DE lane)
`fileParser.ts` `parseWeight()` comments claim "if between 0 and 1, assume decimal" but never
range-checks — a numeric/non-`%`-string cell in percent form (e.g. `5.55`) is stored un-normalized.
NOT the cause of today's bug (today's is PM-export, not manual upload), but it could produce the same
×100 symptom on a manual upload of a percent-formatted file. Defensive hardening, tracked separately.

## Durability (why this won't be lost again)
The original fix was lost because it lived only as an uncommitted working-tree edit. This brief carries
the exact patches; the deploy must land as a committed Terraform apply (Rule 1/2), and the
`opal-portfolio-excel-generator` LastModified + a fresh fraction-stamped record are the verify gates.
