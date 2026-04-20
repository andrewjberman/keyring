# ofc-l2-advisor-distribution — per-advisor AUA distribution on platinum advisor summary

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-04-15
**TO:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ofc-l2-advisor-distribution.md`
**Commit:** `870be4bc` (CLOUD pushed)
**S3:** `s3://opal-data-bd/code/gold/D_04.client_portal_summary.py` ETag `28161081079a3e9391af7e9d8c529761` (matches md5)

---

## Goal

Emit `summary.distribution = {'total': <DistributionStats>}` on `platinum/advisors/{slug}/summary.json` so the OFC L1 click-into-advisor bell curve can render that advisor's full account-AUA distribution (FE already wired for `selectedAdvisorKey` per TO context).

## Scope Pivot — D_03 → D_04

TO recommended the write at D_03. `comp-pipescript io D_03` confirmed D_03 writes `advisor_mix/mix_daily/mix_timeseries` but NOT `summary.json`. The summary artifact is owned by D_04.

Two paths considered:
1. Compute in D_03, store in `advisor_mix.json`, D_04 passes through.
2. Compute directly in D_04 by adding ACCOUNT_PERFORMANCE + ACCOUNT_TEAM reads.

Path 2 chosen — single-script change, no new intermediate artifact, no D_03 contract change. D_03 is heavy (process pool + 500+ advisor entity loop); adding per-advisor distribution there would bloat its critical path. D_04 advisor summary loop already iterates every advisor once — the reads are pipelined there.

## Implementation

1. **New D_04 imports:** `ACCOUNT_PERFORMANCE` + `ACCOUNT_TEAM` from `lib.s3_layout`; `numpy as np`.
2. **New helpers:**
   - `_fmt_currency_bin(v)` — histogram-label formatter ($1K / $1M / $1B shortform).
   - `_calculate_distribution_stats(aua_values)` — 20 log-spaced bins, p10/p25/p50/p75/p90, count/mean/median/std_dev. Inlined from `D_01.calculate_distribution_stats` with identical contract (FE DistributionStats type consumes both).
   - `_build_advisor_accts_aua(account_team, acct_aua)` — for each `account_team` row, each advisor tagged in any of 5 role columns (architect/implementor/consultant/local_ops/addl_advisor) accumulates the account's `total_aua`. Mirrors D_01 L938-968 mechanic. Keyed by full advisor name (matches `book.book_name`).
3. **In `build_advisor_summaries`:**
   - At top (once): read ACCOUNT_PERFORMANCE (date + account_id + total_aua columns only); filter to latest date; read ACCOUNT_TEAM full; build `advisor_aua_by_name` dict.
   - In per-advisor loop: look up `book.book_name` → list of AUAs → `_calculate_distribution_stats` → inject as top-level `summary.distribution = {'total': <stats>}`.
4. **Defensive path:** prep section wrapped in try/except. On parquet-read failure, emits empty `distribution.total` block (count=0, histogram empty). Never throws.

## Compiler Tools

| Phase | Step | `<run>` | `<expect>` | Observed | Pass/Fail |
|-------|------|---------|-----------|----------|-----------|
| 1 | 1 | `comp-pipescript io D_03` | platinum/advisors/{slug}/summary.json in WRITES; account AUA available | D_03 WRITES are `advisor_mix/mix_daily/mix_timeseries` + firm_mix_views; summary.json NOT in D_03's WRITES. Confirms TO's "recommended D_03 path" is wrong. READS include `ACCOUNT_PERFORMANCE` (daily per-account total_aua) — available for D_03-side computation, but not where it needs to land. | PIVOT (D_04 chosen) |
| 1 | 2 | `comp-pipescript io D_04` | platinum/advisors/{slug}/summary.json in WRITES; confirms portal consumer AdvisorBookView | WRITES list includes `platinum/advisors/{*}/summary.json [HARDCODED]`. PORTAL CONSUMERS: AdvisorBookView, ClientsTab. | PASS |
| 1 | 3 | `grep -n calculate_distribution_stats` gold/ | Only D_01; no shared lib helper | `D_01.partner_analytics.py:549` defines it; no lib/ version. Choice: inline copy vs extract to lib. Inlined for minimal scope. | PASS |
| 1 | 4 | Inspect book.json (travis_penfield) for name-mapping | `book_name` = full name, matches account_team role-column values | `book_name = "Travis Penfield"`. No `advisor_name`/`advisor_id` on book. Keyed the advisor_aua dict on full name. | PASS |
| 2 | 1 | `python -m py_compile D_04.client_portal_summary.py` | Exit 0 | `OK py_compile exit 0` | PASS |
| 2 | 2 | `comp-pipescript deployed D_04` | MATCH | Pre-existing tool-gap (aws PATH subprocess isolation bug, flagged from RF01). Manual parity: `aws s3api head-object ... ETag = "28161081079a3e9391af7e9d8c529761"`; `md5sum` of local = `28161081079a3e9391af7e9d8c529761`. | PASS (manual) |
| 2 | 3 | Dry-run D_04 locally | Skipped — heavy downstream deps; QA runner handles full build. Spot-check will validate via artifact inspection post-rerun. | Deferred to post-rerun | DEFERRED |
| 3 | 1 | `comp-blast D_04` | No new downstream consumers | `No downstream consumers found for: gold:D_04.client_portal_summary` — D_04 is terminal (writes to platinum/, served via S3 CloudFront origin). Blast radius unchanged. | PASS |

## Deployment Sequence

| Step | Result |
|------|--------|
| `git status` pre-commit | Working tree clean on D_04 target |
| `git commit --only --author=0.4.0_DS_ClientPlatform~A` | `870be4bc` (148 insertions) |
| `git push origin CLOUD` | `87315f90..870be4bc CLOUD -> CLOUD` |
| `aws s3 cp ... code/gold/D_04.client_portal_summary.py` | Upload OK |
| ETag parity | `28161081…` = local md5 ✓ |
| MCP REQ to AE 0.6.0_AE_PartnerETL | Delivered 20260415T172054Z — D_04 rerun request |
| MCP SHAPE to DE 0.4.0_DE_ClientPlatform | Delivered 20260415T172103Z — L1-click FE wire greenlight |
| MCP STATUS to COO 2.0.0_SA_COO | Delivered 20260415T172110Z |

## Pending

- AE fires D_04 rerun on bd-gold-qa-runner (or picks it up in the full A→D rerun once RA-P1 lands — additive-only either way).
- Pull `platinum/advisors/travis_penfield/summary.json` from post-rerun S3.
- Verify `summary.distribution.total.count` is plausible (Travis has ~500+ accounts per D_01 output), `histogram.counts` is non-degenerate, `percentiles` are populated.
- MCP COMPLETE to COO with spot-check evidence + commit hash.
- DE wires L1 click handler post-confirmation (their TO, not mine).
