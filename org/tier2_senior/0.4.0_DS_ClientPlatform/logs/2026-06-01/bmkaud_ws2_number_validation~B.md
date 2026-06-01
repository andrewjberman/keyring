# BMKAUD WS-2 — Number Validation (DS~B, 2026-06-01)
Directive: docs/briefs/benchmark-yang-truth-audit-20260601.md (914faabd5). WS-2-scoped (disjoint from base WS-1 source doc). CVO = sole verify-writer; this is evidence, not a verdict.

## Scope of the claim — TWO HALVES (per CTO framing)
- **HALF-A = DERIVATION FIDELITY (this doc PROVES it):** the published JSON + FE numbers faithfully derive from the canonical source via the lambda's STATED transform. Proves no post-processing corruption, no stale cache, FE-source integrity. Reproduced using the deployed lambda's OWN functions (get_term_returns + calculate_period_returns) → tests fidelity, NOT methodology.
- **HALF-B = METHODOLOGY CORRECTNESS (NOT proven here; joint-pending WS-3 + CVO WS-5):** that the transform itself is right (period-window defs, sqrt(252) annualization, RFR tenors, weekend/holiday drop). Cannot be cross-checked with the same code I reproduced with. Closes via 0.5.0_AE WS-3 justification + CVO independent-path recompute (own implementation from spec). The "negative INT/LTC/LTA 1M/1Q spreads are REAL underperformance not bugs" reading rests on HALF-B → joint-pending.

## BENCHMARK tab — HALF-A: 360/360 EXACT (CLEAN)
Source: canonical `benchmarks/data_20260531_v1.pkl` (locked; base WS-1 + CVO WS-5 same file). Served: `json/benchmarks/model_portfolio_benchmarks.json` (gen 2026-06-01T13:49:07Z, data_as_of 5/29, pure-yang model_source_note).
- Recomputed 5 models {UST,ST,INT,LTC,LTA} x 9 periods {1D,WTD,MTD,1M,QTD,1Q,YTD,1Y,SI} x 8 fields {model,index_bm,etf_bm,index_spread,etf_spread,3 vols} = **360 cells, 0 mismatches**.
- 1M/1Q symptoms: served reproduces cleanly (e.g. UST 1M model=0.37 idx=0.26 spread=0.11). The "1M broken / 1Q suspect" was the PRE-revert SmartX-mixed state; post-revert 80224d674 + fresh run = clean (HALF-A). Whether the windows themselves are right = HALF-B.
- Corroboration for WS-4: since served == repro via the REPO pure-yang functions 360/360, the code that produced the served JSON IS the pure-yang revert (deployed == repo).
- Harness: .runtmp/bmkaud/ws2_reproduce.py.

## PEERS tab — HALF-A: 30/30 model values EXACT + UST-1M fully traced (CLEAN)
Source (ACTUAL): `data-refresh/archive/exec-3baeb762f5ac/Models Performance vs Peers 20260531.xlsx` (the file the 5/31 18:03 run processed; matches served data_as_of 5/31). Served: `json/peers/peer_performance.json`.
- 5 models x 6 periods {1M,QTD,1Q,YTD,1Y,SI} model values = **30/30 exact**. LTC←"Conservative growth" / LTA←"Aggressive growth" name-mapping is CORRECT in the served JSON.
- UST 1M DECISIVE cell-check (per COO): served UST 1M (model=0.3017, bench=0.1639, p5=0.3126/p25=0.2926/p50=0.2664/p75=0.0919/p95=-0.0) traces EXACTLY to the 20260531 xlsx UST 1M cells. → UST-1M is **NEITHER (a) source-gap NOR (b) parse-bug** — present + faithfully parsed. "UST missing-1M" is NOT a WS-2 data bug → FE-side (PeersTab render) or a pre-fix observation. Route to FE/RD.
- All (model,period) percentile bands present (none empty).

## CORRECTION to my WS-2 catch-up #1 (own error)
I flagged "Peers running on a ~5-month-stale Dec-2025 xlsx" from the `uploads/` listing alone. **RETRACTED — wrong.** The cell-check proved the 5/31 run used a FRESH `20260531` xlsx. Peers refreshes MONTHLY via the data-refresh pipeline: 202512→202601→202602→20260331→20260430→20260531 (current). The `uploads/202512` is a stale LEFTOVER (data-refresh archives processed files but doesn't clean old uploads/ entries) — cosmetic, does NOT affect served data. Lesson: don't infer source from the uploads/ listing; trace the actual processed file (COO's "open the cell" instruction surfaced this).

## Governance flag (legitimate, weaker than "stale") + remediation rec
Peers source = an EXTERNALLY-PREPARED monthly xlsx ("Models Performance vs Peers YYYYMM.xlsx"), NOT yang-PKL-derived and NOT TF-managed in the yang-PKL sense (inherent — peer-universe data doesn't exist in yang). Ingested by the data_refresh lambda (recognizes *peer*.xlsx). Open question for WS-4/governance: is the monthly xlsx UPLOAD automated or human-triggered? who owns it? Remediation rec: (1) confirm/automate the monthly peers-xlsx refresh + make it identifiable-to-the-minute like the directive wants; (2) clean the stale `uploads/202512` leftover; (3) the peers provenance (external xlsx) is a documented exception to "yang PKL = single source of truth" — ratify it explicitly.

## Net WS-2 (HALF-A) verdict: NO data-layer derivation bug in either tab.
Both symptoms explained: Benchmark 1M/1Q = pre-revert SmartX (resolved); Peers UST-1M = data present+correct (FE-side). HALF-B (methodology) joint-pending WS-3 + CVO independent recompute.
