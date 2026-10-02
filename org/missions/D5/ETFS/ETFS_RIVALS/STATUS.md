# ETFS_RIVALS (rivalfunds) -- FAST status

Seat `2.0.0_SA_COO~RV` (CLAUDE). Lease: FAST to 2026-10-02T17:08:53Z, surface `data/etfs/scripts/rivalfunds`
(`org/mcp/drive-mode.log` line 56). Goal (Andrew ~04:59Z): "i want mcp.opalinvest.dev/rivalfunds demoable Today".
Team: reviewer `3.0.0_SA_CVO~RV` (grades pins after the fact), open calls `4.0.0_SA_CRO~RV`
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_RULINGS_20261002.md`).
As of 2026-10-02T05:17Z.

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `rv-fast` at `/c/tmp/rv-fast` (sparse cone) |
| Workspace candidate pin | none yet |
| Portal candidate pin | n/a (the page is static HTML at platinum, served by the gateway `/rivalfunds`) |
| Served page | `s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-01/revisions/20261001T220334Z/index.html` |
| Push state | LOCAL (pushing is the integrator's act) |

## Live thread

State: LIVE END TO END (round 1-5 thread). The 2026-10-01 page is published (T-1 on Friday 2026-10-02). The page is the
trade log grouped by Opal fund, with no rankings, trend, AI accounts or theme yet.

## Next-list (Addendum B, FWD-13..20; the A1 orders are superseded by this lease and their AC checks are the item tests)

1. pt-1 `page_theme.py` -- the portal theme (check `round5/checks/pt-1.AC1.py`).
2. pg-1 `render.py` + `publish_page.py` -- components first, script-free fund/period switches, audit block.
3. rk-1 `gold_holding_contribution.py` -- MTD/QTD/YTD/R30 rankings, with the CRO CALL 1 holding-implied price fallback.
4. tb-1 `gold_buying_trend.py` -- YTD lean into/away, tilt/bet, trend mark (G5 holds history from 2024-10-01).
5. ic-1 `gold_input_census.py` -- inputs that did not arrive.
6. ai-1 `market_context.py` -- internal market readings, READ ONLY.
7. ai-2 `ai_accounts.py` -- two-prompt chain, grounding check, stub client.
8. Hookups (one commit): render imports `page_theme.CSS`; the page loads the four tables; `guardrails.analysis_grounding`
   calls `ai_accounts.grounding_check`; the census takes `market_context` readings.
9. One real run: the producers write today's gold, then the page republishes, looked at.

## Write claims

`data/etfs/scripts/rivalfunds/page_theme.py`, `data/etfs/scripts/rivalfunds/tests/test_a1pt_*.py`.

## Held from round 5 (vehicle-run drains, SERVED, decomposition ruling 4; unchanged by FAST)

`wk-rivals5-2` (m-2, l-1 @86ddb6cec0) and `wk-rivals5-5` (s-6 @ca98d691f8) drain after the morning read, in order: the
07:00 ET issuer fetch markers, the 08:03 vehicle exit lines, then the 09:00 sweep.

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| A live OpenAI run for the AI accounts (round-6 WORLD act: secret + IAM) | `4.0.0_SA_CRO~RV` call, then a pair | ai-2 lands and passes its check |
| The concentration cell (ACWI top-10 share) | `2.0.0_SA_COO~RV` | ACWI lands daily (v0.8 leg) |

## Limits

Nothing in this lease is graded until `3.0.0_SA_CVO~RV` grades the pinned candidate on the real run's artifact. A new
page revision at platinum is a served change and goes out under the never-widen pair (CTO + COO).
