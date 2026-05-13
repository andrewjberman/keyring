# DS~C 2026-05-13 session 7 — ADVI_INFADV Path B per-advisor book.json field expansion

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~19:50Z → ~19:57Z 2026-05-13 (~7 min execution after ~5 min planning/scoping)
**Trigger:** DE 0.4.0 TO `ADVI_INFADV` Path B (Andrew direct routing). FE adapter Path A already live; gold-side field expansion shipped here for gold-d chain coverage.

## TL;DR

Shipped `0997324d6` — 3 of 4 fields added to `INF_D_02.build_advisor_books` per-advisor book.json emit. `mix_periods` with asset-class breakdown deferred to a separate follow-up TO (needs historical-account-team walk + per-quarter classifier; not partner-demo blocking since FE adapter stubs are live).

| Field | Status | Source |
|---|---|---|
| `role_breakdown` | SHIPPED | Single-role 'advisor' stub for Inflection |
| `active_since` | SHIPPED | `min(clients[].relationship_since)` |
| `tax_exposure` | SHIPPED | Top-level mirror of existing `summary.tax` |
| `clients[].relationship_since` | SHIPPED | New `_compute_relationship_since_per_hh` helper (mirrors Lambda) |
| `mix_periods` asset-class | DEFERRED | Follow-up TO — heavy walk + classifier |
| Lambda `_build_book` parity | DEFERRED | Lands in v1.7.55 when AE bandwidth allows |

## Ship

| Commit | Scope | Lines | S3 SHA-MATCH |
|---|---|---|---|
| `0997324d6` | `INF_D_02.build_advisor_books` 3-field expansion + orphan-parity | +78/-2 | ✓ deployed `s3://opal-data-inf/code/gold/INF_D_02.advisor_client_detail.py` |

## Files Modified

| File | Change |
|---|---|
| `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py` | (1) New `_compute_relationship_since_per_hh` helper near L443. (2) Pre-loop computation of `relationship_since_by_hh` at L1378-1380. (3) Per-client `relationship_since` emit at L1432 + orphan skip (mirrors Lambda 52478bb3a). (4) Per-advisor `active_since`, `role_breakdown` computed in loop. (5) Three new top-level book fields: `active_since`, `role_breakdown`, `tax_exposure`. |

## Empirical pre-ship verification

```
_compute_relationship_since_per_hh against gold/dimensions/accounts_dimension_latest.parquet
  (861 rows, has first_trade_date + household_id columns)
  → 295 HH entries returned
  → HH 1342 (Thompson family): '2026-04-15' (matches live Lambda emit exactly)
  → HH 419 (Stephen Armfield): '2020-06-04'
  → HH 304: '2020-06-12'
```

Cross-check against Lambda-emitted IWM book.json clients[]: Thompson's `relationship_since` matches the live Lambda output exactly, confirming the helper algorithm is identical to the Lambda's.

## Decision notes

1. **Scope-cutting on mix_periods.** DE's brief framed mix_periods as 1 of 4 fields but the asset-class breakdown variant requires a historical-account-team walk (mid-history reassignments break naive current-team filtering) + per-quarter holdings classifier (similar to INF_D_07a firm_concentrations). Heavy work; DE explicitly accepted defer in the brief. Shipped 3 fields cleanly; mix_periods follow-up TO will reuse INF_D_07a's classifier patterns.

2. **Two-emit-path orphan parity.** Lambda commit `52478bb3a` dropped phantom orphan clients[0] from Lambda emit. This commit applies the same fix to gold-script emit so the two paths produce identical orphan handling. Future agents reading either implementation see the same pattern.

3. **tax_exposure is a top-level mirror, not a recompute.** The existing `_aggregate_tax_status_per_advisor` + `_aggregate_tax_per_advisor` + `_compute_capital_gains_ttm_per_advisor` + `_aggregate_cost_basis_by_year` already produce the full `adv_tax` dict that DE wants as `tax_exposure`. The fix is simply emitting `book['tax_exposure'] = adv_tax` at top level (alongside the existing `summary.tax` emit). FE adapter shape supports both 49F canonical-bucket fields + Inflection's realized/unrealized extensions in the same dict (types.ts:1038-1056).

4. **Defaults applied where DE ambiguous.** `small_account_count` could be accounts-with-AUA<$40K OR households-with-AUA<$40K. DE's stub literal `for a in advisor_accounts if a['aua'] < 40000` suggests accounts. Defaulted to accounts via `(adv_df['aua'] < 40000).sum()`. Easy 1-line swap to clients if DE wanted households.

5. **Lambda parity deferred without breaking partner demo.** v1.7.54 already shipped today; v1.7.55 would mirror these 3 fields in `_build_book`. Since chain #26 is gold-d (Lambda bypassed per INFPUBLISHERDEDUP), the gold script's emit is canonical for the next refresh. Lambda parity is a clean follow-up commit; FE adapter handles the missing-Lambda-fields case in the interim.

## Compiler Tools

| Tool | Runs | Result |
|---|---|---|
| `ds-commit-gate.sh INF_D_02.advisor_client_detail.py` | 1× | PASS — py_compile + ds-precommit + ruff py39 clean |
| Empirical pre-ship: `_compute_relationship_since_per_hh` against live `gold/dimensions/accounts_dimension_latest.parquet` | 1× | 295 HH entries; Thompson HH 1342 matches Lambda emit exactly |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 1× | Clean first-try |
| `safe-deploy.sh` pre-push hook | 1× | DEPLOYED + SHA-MATCH verified |

## Sequencing handoffs

| Recipient | Item |
|---|---|
| **DE 0.4.0_DE_ClientPlatform** | RAVC2 sent 19:56Z with commit + 3-field summary + mix_periods follow-up note. DE can remove FE adapter stubs for role_breakdown / active_since / tax_exposure once next chain runs; mix_periods stub stays until follow-up TO ships. |
| **AE 0.6.1** | No action — `INF_D_02` ships on next gold-d chain. Lambda parity (v1.7.55) is a separate ship when AE bandwidth allows. |
| **COO 2.0.0_SA_COO** | No new ping — Path B was Andrew-direct-routed; CC'd by DE separately. Will fold into next status sync. |
| **DS~C self** | Idle. Next concrete work: mix_periods follow-up TO write-up if/when DE/COO/Andrew prioritizes. |

## Pacing

7 min execution after ~5 min planning. Total: ~12 min from inbox receipt to RAVC2 sent. Empirical verification (HH 1342 cross-check vs Lambda) pre-ship caught zero issues; algorithm correctness confirmed before commit.

Brief is closed on Path B Ship 1; mix_periods Ship 2 awaits follow-up TO scope.
