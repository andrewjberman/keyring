# CVO Triple-Check — ETFS AVGCAP Apr/May/Jun 2026 (Andrew-direct): PASS + 1 renderer finding

**archetype:** VALIDATE
**Date:** 2026-07-07 | **Agent:** 3.0.0_SA_CVO | **Trigger:** Andrew-direct ("make sure these numbers are correct, double and triple check")
**Deliverables (Desktop):** `ETFS_AVGCAP_Report_Apr-May-Jun2026.md` (v3, verification record folded in) + `ETFS_Ownership_Official_{2026-04,05,06}.{pdf,html}` (official 5-slide render, corrected complete-month averaging).

## Blessed numbers (full-calendar-month carry-forward, per-partner totals)

| Partner | 2026-04 | 2026-05 | 2026-06 |
|---|---:|---:|---:|
| 49financial | 508,302,763.59 | 525,214,138.69 | 516,396,695.80 |
| inflection | 374,240.01 | 7,485,316.28 | 38,955,292.82 |
| cottonwood | 0.00 (real zero) | 0.00 (real zero) | 865,986.82 |

## Verification chain (battery: session-scratchpad `verify_battery.py`)

1. **Raw-vendor layer numerically proven, all 3 partners** (not code-read alone):
   - 49F: from-scratch parse of the raw Schwab CRS file (`opal-data-schwab/bronze/rps/CRS20260415.RPS`, H2 col 38 "Market Value") == silver-derived, all 4 ETFs to the cent.
   - INF: `silver/api_dims/positions_mv` (Orion `currentValue`) vs `gold/canonical/holdings_2026-04-15` row-wise: 6/6 ETF rows, 0 diffs >1c.
   - COT: `silver/holdings/2026-06-15` (BD "Market Value") == `gold/canonical/holdings/2026-06-15` == report input, all 4 ETFs exact. (COT `price` is derived mv/units at `data/cot/scripts/gold/B_00.canonical_holdings.py:141`; `market_value` itself is raw BD.)
   - => `market_value` = raw vendor field everywhere; only derivations in the chain: numeric parse, 49F zero-qty row drop, the monthly average itself.
2. **Two independent averaging implementations** (imperative loop vs pandas reindex+ffill) exact-match on all 9 partner-months.
3. **Third-leg convergence:** May 49F == production AVGCAP artifact `monthly/2026-05.json` to the cent (two clean-room implementations + the deployed engine agree).
4. **All discrepancies reproduced to the dollar; zero unexplained residuals** — deck-v1 Apr/May 49F deltas were exactly the renderer mtd_cap denominator (29 vs 30/31); served-artifact deltas were exactly the 06-25 mid-month generation vintage (June) + the superseded onboarding-clock window (INF May).

## Findings routed

- **P2 → 0.4.0_DE (150944Z):** `render_month_end.py:175` `mtd_cap=min(m_end, last-data-date)` truncates COMPLETE months ending on no-data days — May 49F rendered $526,005,023 vs correct $525,214,138.69 (+$790,884) in the production May deck; contradicts the function's own comment + AVGCAP + Andrew's full-month billing ruling. Recommend m_end cap for completed months. (P2: logged, driver MCP'd; small $, monthly cadence.)
- **LOW → 0.6.2_AE (150953Z):** CRS20260430.RPS absent at bronze AND raw — Schwab/OneDrive delivery gap, not conversion. OneDrive check requested; April self-heals if recoverable (≤~0.1% impact).
- **Observation (real data, no action):** 49F PFOE −$31.2M in one day 05-20→05-21 ($101.7M→$70.6M, stable after) — genuine reallocation, present in raw vendor file.
- **Prior finding stands:** `infra/aws/ec2/bd-exporter/README.md` carries live plaintext BD credentials in-repo (flagged to Andrew verbally this session; separate remediation).

## Compiler Tools

- `pipescript --resource opal-data-mdpf` / `--resource opal-data-cot` — thread ownership + evidence_ref reproduction (earlier in session, FEDOBS + this).
- `comp-which "run a trino query against globgrph fedobs views"` — routed (comp-depth; used `_trino_fed.py` direct for the FEDOBS leg).
- Raw `aws s3 ls`/greps carried `# rail-checked` markers where no comp-tool fit (enumeration-for-computation, not inspection); several Grep/Glob native calls under the light escape.
- Gap noted: no comp-tool answers "which script WRITES artifact X" directly (comp-pipescript io is script-rooted, not artifact-rooted) — worked around via targeted grep; possible `comp-pipescript writers <artifact>` candidate.

Production state untouched throughout: no S3 writes to opal-data-etfs, no lambda invokes, no deployed-script edits; decks rendered locally from the renderer's own code with the data-source + averaging monkeypatches documented in the report.

— 3.0.0_SA_CVO
