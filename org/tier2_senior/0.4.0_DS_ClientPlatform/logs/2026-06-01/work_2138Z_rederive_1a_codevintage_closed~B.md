# work_2138Z — re-derive 1a code-vintage check: STAYS CLOSED (DS~B)

## Tick class: SUBSTANTIVE (/work; CTO/COO closed-work verification)

## Question (COO/CTO deeper blast-radius)
Could the verified-closed Schwab re-derive's 49F 1a (model_aua) be on the stale Jan-14 smartx-exporter image — missing AUM-affecting undeployed fixes (d621311b5 Jan-21 "SmartX retroactive AUM smoothing", feca94a1f Jan-21 total-returns/calendar, May-13 Path-B model_aum reconcile)? 2nd staleness angle, distinct from the Mar/Apr-empty angle already cleared.

## VERDICT: 49F 1a STAYS CLOSED (insulated). Code-lineage decisive.

STEP 1 — 1a value chain BYPASSES the smartx-exporter aggregation layer:
- Historical 1a (1/16-5/17, the re-derive region): build_mdpf_process_backfill.py reads RAW SmartX daily-export CSVs DIRECTLY (exports/{run-,docker-}*/{AC}_{date}T..Z_{Model}_allocations_*.csv) — explicitly NOT the consolidated parquet ("collapses to month-end, destroys daily granularity"), NOT exporter aggregation output.
- Live 1a (5/18+): wsb_49f_smartx_model_aua.py pulls DIRECT from SmartX REST API, "never the canonical SmartX exporter path."

STEP 2 — the undeployed fixes are all aggregation-layer, downstream of the raw CSVs:
- d621311b5 (Jan-21 smoothing) -> aggregate_smartx_by_transaction_dates.py = GLOBAL SmartX AUM daily-timeseries (DIFFERENT pipeline; read-time aggregation change; does not modify raw CSVs or the consolidate parquet).
- feca94a1f = total-RETURNS/calendar (returns, not AUM) -> doesn't touch 1a.
- May-13 Path-B model_aum reconcile = exporter aggregation layer -> downstream of raw CSVs.
- The MDPF 1a implements its OWN independent point-in-time logic (MDPF_SCOPED.F4: per-date period-end-consensus de-dup + drop day-1 $0 rows) — solves the same recalc-class bug independently.

STEP 3 — spot-check MATCHES by construction: current-code recompute reads the SAME immutable raw daily-export CSVs with the same deterministic period-aware code -> identical 1a. DIVERGE would require the raw CSVs to change, which no aggregation-layer fix does.

## Annotation recommended for the re-derive close record
"49F 1a confirmed insulated from stale-exporter undeployed fixes (d621311b5/feca94a1f/May-13) — reads raw SmartX daily-export CSVs directly, bypasses the exporter aggregation layer, + independent point-in-time F4 logic; current-code-consistent by construction."

## Honest caveat
Code-lineage confirmed decisively; no live recompute run (matches by construction). Residual for AE: confirm the raw-CSV PULL/export step is sound on the stale image — but the cited fixes are aggregation-layer (not the pull step), and the 1/16-5/17 CSVs are immutable months-old snapshots, so the raw 1a source is sound regardless.

## RAVC2 -> COO (213838Z), CC CTO+AE+DE.

## Both Mar/Apr-empty + 1a-code-vintage staleness angles on the re-derive now CLEARED. Re-derive stays closed.
## pre-1/16 still awaiting Andrew #3 (b3e627a75). TO-B bell-curve durable-close in AE's hands (EC2 redeploy + per-firm DAG wiring) + DE/CVO post-deploy re-verify + RD FE cutover.
