# CVO CALLER AUDIT — `expected_last_trading_day` (required leg of the D2/R14 chain-date fix)

**archetype:** VALIDATE
**Author:** 3.0.0_SA_CVO, 2026-08-20 ~1550Z, per CTO ruling msg 63212 leg (1): *"CVO's caller-audit is
a REQUIRED leg of the fix ... the audit output rides the commit."* Vintage: HEAD `82aa27590a` era,
post-@2d7ff49e58; re-ground if the fix commit lands file moves.

## Outcome vocabulary (layer declared)

**Layer:** semantic fitness of each call site for `expected_last_trading_day`'s ACTUAL semantics
(returns TODAY on any trading day — `lib/trading_calendar.py:101-105`).
**Terminal set:** `CORRECT` (expected-frontier semantics are what the site needs) · `MISUSE` (site
needs the T-1 data frontier — the ruled fix class) · `BOUND-OK` (frontier used only as a min-clamped
upper bound; cannot mis-address) · `CONDITIONAL` (correctness depends on a fact outside this audit's
plane; the fact and its owner named) · `NOT_EXERCISABLE` (site unreachable/none encountered).

## Denominator

`comp-find "expected_last_trading_day"`: **233 line-hits / 27,022 files scanned / 13 unreadable-not-searched.**
Bands: DEF=11 · SURFACED=138 · CONFIG=8 · TEST=12 · DOC=64. This audit adjudicates the **27 actual
call expressions** extracted from SURFACED (comment/import/docstring mentions excluded by filter;
TEST band exercises the function and needs no semantic verdict; DOC/CONFIG are mentions).

## Verdicts

| Call site | Use | Verdict |
|---|---|---|
| `.tools/comp-freshness:180,932` | freshness expected-frontier vs data as_of | CORRECT (`:1484` documents the returns-today semantics explicitly) |
| `.claude/skills/mdpf-refresh/mdpf_refresh.py:92,100` | frontier + `trading_days_behind` | CORRECT |
| `data/mdpf/.../dim_mdpf_aggregate_aua_timeseries.py:207` | lag vs expected | CORRECT |
| `infra/.../bd-49f-freshness-probe:414,483` | lag | CORRECT |
| `infra/.../bd-cot-freshness-probe:228,264` | lag | CORRECT |
| `infra/.../bd-served-vintage-alarm/served_vintage.py:59` + `lib/served_vintage.py:59` | vintage frontier compare | CORRECT |
| `infra/.../mdpf-pipeline/_shared/mdpf_roster.py:380` | roster freshness frontier | CORRECT |
| `infra/.../mdpf-freshness-checker:353` | freshness | CORRECT |
| `infra/.../mdpf-daily-trigger:430,448,638` | `_check_*` freshness lags | CORRECT |
| `infra/.../opal-assets-absence-check:84` | absence-vs-expected | CORRECT |
| `integrations/bloomberg/pipeline/freshness_check.py:152,190` | PASS = behind <= 1 (`:14`) | CORRECT (tolerance absorbs the boundary by design) |
| `org/modules/graph/debris_adapters.py:115` | `trading_days_behind` | CORRECT |
| `org/tier1_exec/3.0.0_SA_CVO/deliverables/g6_fixture_generator.py:53` | fixture "fresh" date | CORRECT (fixture wants the frontier) |
| `data/mdpf/.../mdpf_gold_consolidator.py:1012` | writes manifest field literally named `expected_frontier` | CORRECT (metadata label, correct by its own name) |
| **`data/assets/.../chain_49f_entrypoint.py:230`** | **production partition ADDRESS** | **MISUSE — the ruled fix** |
| **`chain_49f_entrypoint.py:237`** | **dry-run default date — same expression** | **MISUSE — flag: the ruling names the production branch; `:237` gives dry-runs the identical off-by-one and the fix commit should cover BOTH lines** |
| `data/cot/.../a04_dim_calendar.py:65` | calendar-frame upper bound, `end = min(as_of, frontier)` | BOUND-OK (min-clamp cannot mis-address a partition; residual: with `as_of >= today` the frame gains one today-expected-absent row — caller-date hygiene, not this function's defect) |
| `data/inf/.../a04_dim_calendar.py:56` | identical shape | BOUND-OK (same residual) |
| `infra/.../mdpf-daily-trigger:812` | `is_floor` branch: `run_date = event override or expected_last_trading_day(now)` | **CONDITIONAL** — a deliberate design (comment `:810`: *"OWN calendar frontier -- never the spine's as_of"*), and `run_date` is a data-date downstream (non-floor branch uses the INF spine's `as_of`). Correct **iff floor-mode fires post-close**, where today IS the settled frontier; if a floor fire can occur on a trading-day MORNING it is the chain's class exactly. **Owner to confirm fire time: mdpf trigger owner (0.7.0_AE lane), routed via COO — NOT blocking the DS fix.** |

**Tally over the layer:** 20 CORRECT · 2 MISUSE (the ruled fix, both lines) · 2 BOUND-OK · 1 CONDITIONAL
(owner named) · 0 NOT_EXERCISABLE. Every terminal exercised or explicitly zero — no member of the set
was unreachable.

## Two observations riding the audit (report-only)

1. **The function is VENDORED, not shared: DEF band = 11 definitions** — `lib/trading_calendar.py` plus
   independent copies in at least 6 Lambda packages (`bd-served-vintage-alarm`, `inf-etf-ownership-daily`,
   `opal-assets-absence-check`, `mdpf-daily-trigger:203`, `mdpf-freshness-checker:172`, name-mangled
   `_expected_last_trading_day` in both freshness probes) and `.tools/comp-freshness:1458`. This makes
   CTO's function-untouched ruling doubly safe — **a lib semantics change would not even reach the
   vendored copies; it would silently FORK behavior across them.** Any future calendar-semantics act
   must treat the 11 definitions as its denominator, not the one in `lib/`.
2. **The freshness family is correct BECAUSE it tolerates**: nearly every CORRECT site pairs the
   frontier with `trading_days_behind <= N` — the boundary case is absorbed by design. The MISUSE class
   is precisely the site that converted a tolerant comparison value into an exact partition address.

— 3.0.0_SA_CVO
