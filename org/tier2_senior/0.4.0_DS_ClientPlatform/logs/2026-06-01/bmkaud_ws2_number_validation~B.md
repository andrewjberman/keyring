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

## WS-2 FOLLOW-ON (CTO direct): 1M/1Q window both-ways + end_date edge

### end_date edge — CLEAN
weekday-filtered max date = 2026-05-29; term_returns max AFTER all-zero(holiday) drop = 2026-05-29 (Friday, real trading day; UST model daily=0.0644 non-zero). NO all-zero rows dropped after end_date. So lambda end_date=index.max() is the legit last trading day, NOT a dropped-row artifact. AE's end_date edge confirmed.

### 1M/1Q window BOTH-WAYS (window is the only variable; geometric compound held constant)
end_date=2026-05-29. 1M: trailing-30d=(4/29,5/29] | MTD=[5/1,5/29] | lastCalMonth=[4/1,4/30]. 1Q: trailing-91d=(2/27,5/29] | QTD=[4/1,5/29] | lastCalQtr=[1/1,3/31]. Current lambda serves the TRAILING column (matches my 360/360).

| model/series | 1M_trail30 | 1M_MTD | 1M_lastMo | 1Q_trail91 | 1Q_QTD | 1Q_lastQ |
|---|---|---|---|---|---|---|
| UST model | 0.37 | 0.31 | 0.43 | 0.45 | 0.73 | 0.44 |
| UST index | 0.26 | 0.16 | 0.24 | -0.06 | 0.40 | 0.28 |
| ST model | 0.73 | 0.34 | 1.11 | -0.37 | 1.45 | 0.15 |
| ST index | 1.27 | 1.03 | 1.58 | -0.02 | 2.63 | -0.49 |
| INT model | 2.95 | 1.75 | 4.62 | 1.49 | 6.45 | -0.01 |
| INT index | 3.84 | 3.23 | 6.08 | 4.03 | 9.50 | -1.85 |
| LTC model | 3.85 | 2.29 | 6.19 | 2.22 | 8.62 | -0.05 |
| LTC index | 5.29 | 4.46 | 8.65 | 6.31 | 13.50 | -2.63 |
| LTA model | 4.08 | 2.48 | 6.74 | 2.97 | 9.39 | -0.12 |
| LTA index | 5.29 | 4.46 | 8.65 | 6.31 | 13.50 | -2.63 |

(etf series in harness output; omitted for brevity.) Harness: .runtmp/bmkaud/ws2_windows_and_edge.py.

**Decision-useful observation (for Andrew's window ruling):** the window choice changes the numbers MATERIALLY (e.g. INT 1Q: 1.49 / 6.45 / -0.01). BUT the lambda applies ONE window definition to model+index+etf alike, so the SPREAD (model-benchmark) stays apples-to-apples coherent under ANY single consistent window. The SmartX defect was MIXING windows (model=cal-month vs benchmark=trailing) → incoherent spread; the pure-yang revert uses trailing for all three → coherent. So "which window is 1M/1Q" is a LABELING/presentation ruling, NOT a correctness bug, provided consistency holds (it now does). Methodology-correctness of the chosen window = HALF-B (WS-3/CVO).

## WS-2 FINAL CLOSES (frozen-snapshot byte-verify + p95 disposition)

### HALF-A byte-verified vs FROZEN evidence — caveat CLOSED
Frozen snapshot: s3://opal-data-mdpf/bmkaud-evidence/20260601T1445Z/. Chain proven byte-for-byte:
- local recompute copy md5 = `d2503d3c8f4bdd8223f2fbd6afdb9147`
- live `opal-data-portal-v2/benchmarks/data_20260531_v1.pkl` ETag = `d2503d3c8f4bdd8223f2fbd6afdb9147` (size 8388499)
- frozen `bmkaud-evidence/20260601T1445Z/benchmarks/data_20260531_v1.pkl` ETag = `d2503d3c8f4bdd8223f2fbd6afdb9147` (size 8388499)
=> what-I-recomputed-against == live == frozen, identical. The 360/360 benchmark + 30/30 peers HALF-A results are proven against the immutable frozen evidence. Confirmed-canonical = the `data_` file (lambda reads data_ not the co-snapshotted model_; base WS-1 confirmed).

### UST 1M p95 == 0.0 — LEGITIMATE (CTO low-pri item)
xlsx UST 1M p95 raw = -1.82546433524777e-07 (real float, NOT NaN), in a clean monotonic ladder p5=0.3126 > p25=0.2926 > p50=0.2664 > p75=0.0919 > p95≈0. The 95th-percentile peer genuinely sits at ~0% 1M return -> a real clustered near-zero that rounds to -0.0, NOT a computation artifact. RD's FE falsy-zero fix is correct and 0.0 is the right number.

## Net WS-2 (HALF-A) verdict: NO data-layer derivation bug in either tab.
Both symptoms explained: Benchmark 1M/1Q = pre-revert SmartX (resolved); Peers UST-1M = data present+correct (FE-side). HALF-B (methodology) joint-pending WS-3 + CVO independent recompute.
