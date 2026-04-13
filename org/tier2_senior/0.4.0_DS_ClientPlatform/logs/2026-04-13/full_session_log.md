# 0.4.0_DS_ClientPlatform -- Full Session Log

**Date:** 2026-04-13 (EDT)
**Session span:** ~09:00 EDT to ~21:40 EDT
**Agent:** 0.4.0_DS_ClientPlatform

---

## TOs Completed This Session

| TO | Title | Status | Commit |
|---|---|---|---|
| ADVI_REBORN.W6-001 | D_04 leaderboard fee_paying/no_fee passthrough | complete | `87557c33` |
| ADVI_REBORN.W6-003 | D_00c role_combination_breakdown | complete | `1d70ecaf` |
| ADVI_REBORN.W6-005 | D_00c split_pct-weighted fee buckets | complete | `0804b377` |
| (ad hoc) | Yang benchmarks SI investigation + double-annualization fix | complete | `bc6f4ccb` |
| (ad hoc) | GEO snapshot vs continuous AUA fix (D_01) | complete | `b846b2b5` |
| ADVI_PROFAU.001 | 7-gap audit response | complete | `cbd98266` |
| ADVI_PROFAU.002 | D_02 fee_earning_mask is_billable gate + is_fee_paying on AdvisorClient | complete (QA verified) | `f2507121` |
| ADVI_PROFAU.003 | D_02 book-level tax aggregates (capital_gains_ttm, cost_basis_by_year) | complete | `b2e4e668` |
| ADVI_OFFICE.W1 | D_01 + D_00b OFC (Office) cohort view | complete | `27471bed` |

---

## Bug Fixes (ad hoc)

| Bug | Fix | Commit |
|---|---|---|
| Yang SI double-annualization | Restore annualize block in both yang Lambdas + LATEST.json path fix | `62985fcf` (yang-v2.3.8) |
| D_00c new_clients fee-bucket split | _fee_bucketed_new_clients + fee_paying/no_fee new_clients fields | `3bf7408c` |
| D_02 is_fee_paying NaN-as-True | `bool(NaN)` → `is True` strict identity check | `b0ad9811` |
| D_00b _build_office_view KeyError account_id | client_performance is rel-grained; switch to rel_office_dim via relationship_id | `e20fcf0a` |
| D_00b crash #2: _nna_drill_data UnboundLocalError | Move OFC _nna_drill_data call below nested def; add relationship_id to _AT_COLS | `15512bed` |
| D_02 fee-scoped timeseries AUA per role | {role}_aua_fee_paying / {role}_aua_no_fee in timeseries.json | `4b177154` |
| D_02 canonical NNA in timeseries | nna_canonical / inflows_canonical / outflows_canonical (inception cumulative) | `2876ec61` |

---

## Compiler Tools

| Section | Tool | Command | Result |
|---|---|---|---|
| PROFAU.001 | comp-pipescript | io D_00c, io D_04 | Confirmed leaderboard chain and platinum terminal writes |
| PROFAU.001 | comp-trace | employee_leaderboard --direction both --all | D_00c->leaderboard->D_04->platinum/firm/leaderboard.json |
| PROFAU.001 | comp-transform | schema-check AdvisorBookView, AdvisorPublicProfile | Type drift confirmed; 13/19 unused on PlatinumAdvisorSummary |
| ADVI_OFFICE.W1 | comp-pipescript | io D_01, io D_00b | Confirmed reads/writes for both scripts |
| W6-001 | comp-pipescript | io D_04 | EMPLOYEE_LEADERBOARD read, leaderboard.json terminal write |

---

## NNA Investigation Summary

Andrew flagged Lifetime Activity NNA chart showing ~$55M vs $253M canonical.

**Root cause:** `timeseries.json` sources NNA from `account_performance.cum_inflows/cum_outflows` which:
1. Resets to zero each January 1 (YTD only, not inception-to-date)
2. Has missing historical data for 2022-2023 (shows $0 for Travis those years)

**Chart diff bug** (secondary): `curr.nna - prev.nna` at year boundary = NNA acceleration, not NNA.

**Fix:** `_load_canonical_nna_per_advisor` added to D_02, embedding `nna_canonical` (inception-to-date cumulative from canonical NNA transactions) in each timeseries data point. RD switches chart to use `nna_canonical`; straight diffs always give correct period NNA.

**RD frontend fix:** Replace `net: (curr.nna ?? 0) - (prev.nna ?? 0)` with `net: (curr.nna_canonical ?? 0) - (prev.nna_canonical ?? 0)`.

---

## Scripts on S3 for Tonight's Automatic Run

| Script | Commit | Key changes |
|---|---|---|
| D_00b | `15512bed` | OFC timeseries ofc/nna_ofc; _nna_drill_data crash fix; relationship_id in _AT_COLS |
| D_01 | `27471bed` | views.ofc + views.nna[period].ofc in partner_analytics_{gran}.json |
| D_00c | `3bf7408c` | new_clients in fee_paying/no_fee sub-buckets |
| D_02 | `2876ec61` | is_fee_paying NaN fix; fee-scoped timeseries AUA; tax_exposure fee split; canonical NNA |

D_04: unchanged, pure pass-through for all above.

---

## Do NOT Rules

- Do NOT use bd-gold-trigger for manual D-group runs -- PROD runner is EventBridge only. Use QA runner (i-0090b823a4a0997e3) for manual runs.
- Do NOT use bool(NaN) checks on merged DataFrame columns -- use `val is True` for strict boolean checks.
- Do NOT call nested functions before their def in the same function body -- Python treats the name as local from first assignment.
- Do NOT source advisor NNA from account_performance.nna for charting -- use nna_canonical from canonical NNA partitions.
