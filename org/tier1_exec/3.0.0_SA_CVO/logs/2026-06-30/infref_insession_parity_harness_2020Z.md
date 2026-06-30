# INFREF in-session parity harness — the live-detector gate

**Context:** Andrew-direct (2026-06-30 ~2015Z): "bang out this ENTIRE refactor in this
session, we are not going to fuck around and test. If we do the full rebuild tonight and
something bad happens, then we stay up all night." Timeline COLLAPSED: structure +
one-time canonical rebuild + perf-incremental flip + cutover + 9-cron decommission ALL
this session. The cutover's no-tolerance parity gate is NOT relaxed — it is **compressed
into the session** and I run it as the live detector (full-recompute vs served, to the
cent, within minutes of each artifact landing). A break tonight = in-session fix, not a
follow-up.

Propagated to COO/CTO/~A/0.6.1 at 2020-2056Z.

## The 5 parity passes (each = a HARD gate before its next step)

Each pass: pick the SHARPEST check (row-for-row content equality, to the cent — never
row-count or a coarse proxy). Ground against the SERVED/live artifact, never a self-report
or the producer log. Confirm exact paths on-land (marked `confirm-on-land`).

| # | Pass | LEFT (anchor = current path) | RIGHT (the new thing) | Sharp check | Gates |
|---|---|---|---|---|---|
| 1 | LEG-2 pull-stage | current full-chain pull output (per dim) | `--stage pull` staged output | per-dim row+value equality; same 57-script set produced | LEG-2 deploy |
| 2 | 4-dim de-convert | prior silver path content (per dim) | typed-silver parquet `silver/orion-api/{dim}/` | dtype-only delta; NO field slim, NO row drop (Rule 17); gold reads byte-equiv | each dim cutover |
| 3 | one-time FULL REBUILD | current served (post-nightly, pre-rebuild) | rebuild canonical output | served AUA + position-level row-for-row, to the cent | THE tripwire / cutover |
| 4 | perf-incremental | full-recompute TWR series | trailing-window incremental chained onto stored TWR | TWR equality across 313 clients x windows, to the cent | perf cron decommission |
| 5 | true sole-source | n/a (census) | live writer set per served key | single-runner = sole producer; 9 legacy crons gone; no double-write | P3 done |

## Anchor artifact paths (confirm-on-land)

- **Served AUA headline:** INF_D_04 rich header -> `platinum/firm/header_metrics.json`
  (`holdings.market_value.sum`). [NOT INF_D_00's thin stub total_aua — that's the
  client_performance basis; the rich header is the served number.]  `confirm-on-land`
- **Position-level anchor:** `gold/canonical/holdings/{date}.parquet[market_value]`
  (ties to `client_performance.total_aua` to the cent in the current path — the computed
  leg's no-tolerance tie).  `confirm-on-land`
- **Silver flats (gold-consumed, per SPEC-2 §5.2):** `silver/performance/` <- INF_C_02;
  `silver/assets_v2/` <- INF_D_03; `silver/transactions/` <- A-stage. De-convert target =
  `silver/orion-api/{dim}/snapshot_date={date}/`.  `confirm-on-land`
- **perf source (the L89/L257 root):** `pull_inflection_performance_rest.py`
  HISTORY_START=2020-01-01 (L89), `_chunk_windows(HISTORY_START, end)` (L257) — full-6yr
  rebuild-daily; incremental = trailing window chained onto the stored TWR series.
  `grounding: SOURCE-CONFIRMED` (0.6.1).
- **pull sentinel:** `gold/meta/pull-complete.json` (compute asserts run_date==RUN_DATE).

## Grounding discipline (Rule 22)
State/value claims grounded vs served — no grounding field. Any MECHANISM claim (a break's
"because X") carries `grounding: SOURCE-CONFIRMED <file:line>` or `INFERRED`. The perf
mechanism is now SOURCE-CONFIRMED (L89/L257) — upgrade SPEC-3 §6 from INFERRED. Reserved
words (proof/root-cause/definitively) legal only on source-confirmed claims.

## UPDATE 2046Z — grounded refinements (this turn)

**Pass-0 / L1-PRECONDITION — CATEGORICAL INGESTION COMPLETENESS (Andrew-direct + /seams catch).**
~A's /seams found `orion_tax_dim.py`+`orion_billing_dim.py` were Lambda-only, MISSING from the EC2
CHAIN_PULL → a parity run on that stage would be a FALSE-GREEN on partial coverage. So before ANY
L1: verify the EC2 single-runner produces the COMPLETE Lambda ingestion set. Independent census
(`pipescript advi-inf`, cross-confirmed vs 0.6.1's TF addrs) = **9 EventBridge-scheduled bronze-pull
Lambdas** (inf-api-reps, inf-accounts-v2-daily, inf-unified-account-dim-daily, inf-api-assets-v2,
inf-api-positions, inf-tax-daily, inf-billing-daily, inf-performance-daily, inf-api-txn) + the Eclipse
EC2 bronze runner. **L1 gate = 11/11 bronze artifacts present**: representatives.json,
household_rep_mapping.json, new_portfolio_accounts.json, unified_account_dim.csv, assets, positions,
tax_unrealized.csv, tax_realized.csv, billing.csv, performance_dim.csv, transactions.csv (+ Eclipse).
This census == the L7 decommission target (Lambdas-to-delete == dims-EC2-must-absorb).

**Pre-refactor baseline (grounded `comp-freshness inf`):** gold served FRESH+PASS (canonical_holdings
3.5h, client_performance 3.5h) = known-good start line. Stale/deprecated (Andrew "1490h=deprecated"):
accounts_dim 1490h FAIL (no producer → retire after LEG-1 repoint), gap_manifest 1490h, household 1204h,
old assets 1326h. historical_prices SKIP/N-A (yahoo, removed).

**Teardown form = ATOMIC-OFF (not shadow):** pull scripts write fixed bronze path, no redirect param.
Decommission STAGED: L5 disable 8 crons (perf #9 HELD — sole perf writer while stage tolerates perf =
single-writer-safe) → Pass-4 disable perf cron as stage takes over perf write (verify handoff atomicity:
no overlap/no gap) → L7 delete all 9 after L6 GREEN + 1 day. .tf retained = recoverable ~min reapply.

**L5 trigger = 14:00Z `inf_canonical_prices_daily` → gold-trigger → runner (already on new runner).**
HARD REQ: dispatch `--chain FULL` (pull+compute), else compute-only reads now-absent bronze. Old
event-driven path-(a) retires with the pull crons (confirm not half-wired). L6 (no shadow) = runner-served
vs Orion-live DIRECT first-scheduled-run + Orion-morning-reset reconcile. Schedule rename (canonical-prices
→ inf-nightly-dispatch) = L7-era declarative cleanup.

## Trigger order tonight
ETag from ~A (3-cron-dim CHAIN_PULL staging) -> Pass 1 -> LEG-2 deploy -> Pass 2 per dim
-> de-convert cutover -> one-time rebuild -> Pass 3 (the tripwire) -> perf-incremental ->
Pass 4 -> P3 decommission TF apply -> Pass 5 -> single-runner sole-source = INFREF done.
