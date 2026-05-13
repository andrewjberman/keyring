# Proposal — `inf-portal-advisor-publisher` Hardening Pass

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-13
**Status:** Proposal — awaiting COO routing to a TO when bandwidth allows
**Suggested ADHC code:** `ADHC_INFPUBHRD` (or whatever convention the harness uses)
**Recipient on routing:** Whichever DS lane gets assigned by COO; could fold into the broader "platinum publisher tech debt" backlog if one exists

## Why this proposal exists

`inf-portal-advisor-publisher` accumulated **3 distinct bugs of similar shape in a single session** (2026-05-13). Each was a quick-fix patch on top of the prior; none surfaced via a per-emit-field smoke test; all surfaced via either Andrew-at-console visual inspection or RD-routed user-facing brief.

| # | Commit | Function | Bug | Visible symptom |
|---|---|---|---|---|
| 1 | `52478bb3a` (DS~C) | `_client_list` L504 | groupby `household_id` synthesised a phantom client row for null/'unknown' HH ids (IWM catchall accounts) | FE Newest Relationship card "Pending DS emit" + empty-name row in Client List panel |
| 2 | `9301dfe97` (DS~B prior) | `_build_summary` L588 + cross-script with `INF_D_04` | mix_periods + avg_fee_bps overwrite — Lambda silently re-emits fields already computed in INF_D_04 gold script | (background bug surfaced in chain #24 RAVC2) |
| 3 | `14c54aec2` (DS~C) | `_build_timeseries` L767 | sparse-cumsum + dict-lookup-with-fallback-to-0 → emitted `nna_canonical` flickers between cumulative-to-date and $0 → FE chart diffs adjacent quarter-ends → alternating ±$15M visible | FE Lifetime Activity NNA mode +/-$15M oscillation while AUA grew smoothly |

Plus 2 prior bugs in nearby sessions that should be folded into the hardening framing:
- v1.7.52/v1.7.53 series — multiple back-to-back fixes for null-HH / fee-rate / FE-readability gaps
- Display label inline (`d12598087` DS~C session 4) — Lambda's `_build_top_holdings` had no opaque-ticker → readable-label translation

**Pattern:** every Lambda emit field can be wrong in isolation; the surfacing mechanism is downstream (FE render, RD smoke, Andrew visual) rather than self-checking. The Lambda has no per-emit-field validation.

## Proposed hardening — scope

### 1. Code-pattern detection (preventive grep harness)

A `comp-*` style audit that greps the Lambda source (and per-firm gold scripts that participate in advisor-timeseries emit) for known-fragile patterns:

| Pattern | Anti-pattern signature | Defense |
|---|---|---|
| Sparse-cumsum dict-lookup | `cumsum()` followed by `dict.get(key, default)` over a date-indexed sparse source | reindex + ffill (this commit's fix) |
| Null-key groupby synthesis | `groupby(col)` where `col` can be null/'unknown' followed by `clients.append({...})` without `if _key is None: continue` | continue on null + structured "Unallocated Bucket" emit if AUA non-zero |
| Empty-partition silent no-op | `_latest_silver_partition(prefix)` returning empty parquet without row-count check | walk-back-to-non-empty (MEMORY pattern C.1) |
| Field-overwrite drift | Lambda re-emits a field that's already emitted by an upstream gold script | single-source-of-truth audit per field |
| Opaque-ticker emit | Emit `ticker` field without a `display_label` companion | `resolve_display_label(ticker, security_name)` mandatory in emit |

Grep harness sketch (proposed location `comp-tools/audit_publisher_patterns.py` or similar):

```python
# Detect cumsum + dict.get with default-empty
re.search(r'\.cumsum\([^)]*\).*\n.*\.get\([^,]+,\s*(0|0\.0|\{\})\)', src, re.DOTALL)
# Detect groupby + append without null-check
re.search(r'groupby\([^)]+\).*\n[^#]*\.append\(\{', src, re.DOTALL)
# ...
```

CI-runnable on every Lambda code change.

### 2. Per-emit-field test corpus

Each field in the publisher's output schema needs a synthetic + real-data test that exercises edge cases:

| Field | Test cases |
|---|---|
| `clients[]` | null HH (IWM catchall) / 'unknown' HH / empty display_name / single client / 11+ clients (sort + truncate) / $0 AUA dormant client |
| `headline.historical_quarters` | sparse activity days / quarter ending on non-activity day / first activity post quarter-floor / reorg-window with $1.19 anomaly / pre-history period / future period |
| `top_holdings` | masked CUSIP (Ameris-style) / annuity slug / standard ticker / share class (BRK.B) / single-letter (F) / Cash position / nan ticker |
| `composition` (inlined) | missing composition.json upstream / cash-only book / single-asset-class concentration / unclassified-heavy book |
| `nna_canonical` (timeseries) | sparse canonical_nna / dense canonical_nna / quarter-end on activity day / quarter-end on non-activity day / single-day advisor / long-history advisor |
| `summary.tax.*` | missing tax_unrealized/tax_realized data / null taxable_aua / negative cost_basis / TTM-locked windows |
| `summary.billing.*` | weighted_avg_annual_fee_pct cap fire (flat schedule) / zero fee_earning_aua / null fee data |
| `relationship_since` | first_trade_date for HH = ingested date / NaT first_trade_date / multi-account HH with different first_trade_dates |

Test corpus delivered as `tests/inf-portal-advisor-publisher/test_per_field.py` with pytest cases + fixture parquets for synthetic + real-data scenarios. Sentinel: each test verifies expected output matches a known-good baseline OR a derived invariant.

### 3. Sentinel comparison framework

Where INF_D_04 (gold script) computes a field that Lambda re-emits, the Lambda's emit must match INF_D_04's. Sentinel:

```python
# Pull Lambda-emitted artifact + INF_D_04-emitted artifact for same advisor
lambda_book = pulled from platinum/advisors/{key}/book.json
d04_summary = pulled from gold/views/clients_tab.json (or similar)
for field in ['headline.total_aua', 'summary.tax.capital_gains_ttm', 'mix_periods', ...]:
    assert lambda_book.get(field) == d04_summary.get(field), \
        f"Drift on {field} for {key}: Lambda={lambda_book.get(field)}, D_04={d04_summary.get(field)}"
```

Run as part of post-chain RAVC sentinel pack. Surfaces silent overwrite drift (bug #2 above) automatically.

### 4. Empirical-test-on-deploy gate

When AE applies a Lambda redeploy, automatically fire the Lambda + pull a sample of platinum artifacts + run the per-field test corpus + sentinel framework against live data. Block the apply tag (e.g. `inf-pipeline-v1.7.55`) until tests pass.

Implementation outline: GitHub Actions workflow triggered on `infra/aws/lambda/inf-portal-advisor-publisher/**` changes that does build-and-upload to a staging Lambda alias + invoke + diff. Or per-existing CI scaffolding.

### 5. Cross-firm parity check

When INF Lambda changes, automatically grep the BD analog (`bd-portal-advisor-publisher` Lambda + `D_02.advisor_client_detail.py` gold script) for the same code patterns. If parallel code paths exist, require cross-firm test coverage. Captured methodology: `memory/feedback_cross_firm_publisher_audit_pattern.md`.

## Deliverable spec

| # | Deliverable | Owner suggestion | Effort estimate |
|---|---|---|---|
| 1 | Code-pattern audit harness (`audit_publisher_patterns.py` + CI integration) | DS or DT | ~4 hr |
| 2 | Per-field test corpus (`tests/inf-portal-advisor-publisher/`) + pytest CI | DS (someone with full INF data familiarity) | ~8-12 hr |
| 3 | Sentinel comparison framework (Lambda-vs-gold-script field-drift detector) | DS | ~4-6 hr |
| 4 | Empirical-test-on-deploy gate (CI workflow) | AE or DT | ~3-4 hr |
| 5 | Cross-firm parity grep + alert pattern | DS or DT | ~2 hr |

**Total estimated effort: ~21-28 hr (3-4 person-days)** across DS + AE + DT lanes.

## Risk and trade-off

- **Hardening adds CI weight.** Per-deploy sentinel framework + per-field tests slow the deploy cycle by ~minutes. Acceptable trade-off given 5 bugs in <2 weeks.
- **Test corpus needs real-data fixtures.** Maintaining synthetic parquets that match production schemas is ongoing work. Risk: tests drift from prod reality if not refreshed.
- **Hardening doesn't replace user-facing testing.** Even with this proposal, FE smoke + RD/Andrew visual inspection remain the final acceptance bar. Hardening shifts left.

## Recommendation

Phase the work:
- **Phase 1 (1-2 days)**: Code-pattern audit harness + sentinel comparison framework. These produce immediate value without needing test fixture refresh discipline.
- **Phase 2 (2-3 days)**: Per-field test corpus + empirical-test-on-deploy gate. Higher cost, higher value, requires fixture discipline.
- **Phase 3 (~half day)**: Cross-firm parity check.

Phases can be picked up by different DS lanes in parallel.

## Open questions for COO

1. Does the harness convention `ADHC_INFPUBHRD` map cleanly to an existing pattern, or does it need a new code-letter prefix?
2. Should the test corpus live in `tests/` (new top-level test dir) or `infra/aws/lambda/inf-portal-advisor-publisher/tests/` (per-Lambda colocation)?
3. Is there bandwidth before partner demo wraps for Phase 1 (code-pattern audit), or should the whole proposal queue post-demo?

Standing by for COO routing.
