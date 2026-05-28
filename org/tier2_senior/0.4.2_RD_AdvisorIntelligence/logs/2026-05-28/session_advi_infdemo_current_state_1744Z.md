# Session log (current-state snapshot) — 0.4.2_RD_AdvisorIntelligence — 2026-05-28 ~1744Z

Continuation of `session_advi_infdemo_demo_prep.md` (which covered the initial bundle through the held-DEV state). This snapshot captures the PROD promotion + post-PROD demo tweaks + current HOLD.

## Current posture
**HOLDING per Andrew-direct ("hold til my further advice").** No substantive action in flight. One queued action (band-aid DEV-revert) deferred to Andrew's release. F11-B deferred post-demo.

## What's LIVE on PROD
- Initial bundle promoted earlier: portal-v2.1.100 (F1/F2/F3/F3b + F4-suppress + donut/composition.json + .002 F6/F8/F9 + F7 + F12 relabel + GRO-card redesign).
- Later promote: **PROD `7bc97151`** (== DEV `c40f08b6`) — adds the log-X Trade Activity scatter (`7009c521`) + the PFDE/PFOE/PCHI Basket band-aid (`c40f08b6`). DT-promoted, CI green, typecheck + D-1 PASS. (DT owns PROD promotion; Andrew-direct push orders.)

## Post-PROD demo tweaks this segment (all Andrew-direct, frontend-only)
1. **F12** — Billing Summary "Total Fee (TTM)" → "Total Fee (since Jul 2025)" + tooltip (DS-confirmed cumulative-since-7/1/2025, not TTM). `c9fab075`→`7a0e3980`.
2. **GRO Growth-card redesign** (Yang/Andrew, PartnerAnalytics) — total growth $ `+$20.4M (+11.0%)`; Market/NNA contribution mix (abs-value share, purple/gold labels, white values, `|` divider); "since {period}" subtext. Then **(MKT)** abbreviation across all Assets Overview Market labels (legend/tooltip/card/footnote = "Market (MKT)"; Total + footnote formula = "MKT + NNA"; Growth mix line = bare "MKT"). `eaaef5ad`→`c7105d63`→`f0fe6841`→`b40e643c`→`c50a58b9`.
3. **log-X scatter** — Business Intelligence → Trade Activity X axis (Transactions) switched to log scale (mirrors the already-log Y); powers-of-10 ticks, x clamped >=1. `7009c521`.
4. **Name/Basket ETF mistag** — PFDE/PFOE/PCHI showed in Top Holdings "Name" view (FE splits on `security_type`; data tagged them single_stock). Andrew chose the FE band-aid (`c40f08b6`, query-chokepoint override single_stock->etf, self-deactivating). DS's proper data fix superseded it: security_type retag + classifier sweep caught a 4th mistag (IDVZ); LIVE (firm_concentrations 17:24Z + CF invalidation complete). So the band-aid is now dormant/redundant on PROD.

## Open / queued (NOT done — held)
- **Band-aid DEV-revert** (task #14): COO issued DROP-IT (data fix live, 4 ETFs route correctly on corrected data). HELD per Andrew's hold. When released: revert the `c40f08b6` band-aid block on DEV (clean revert since pushed); no urgent re-promote (dormant on PROD; rides next batched promote). CVO doing a security_type distribution re-verify (formality; DS validated 4 flips / 0 false-positives across 487).
- **F11-B** (task #13): DEFERRED post-demo (Andrew-direct). AE confirmed field names MATCH the adapter (nna/inflows/outflows _canonical_fee_paying/_no_fee) → zero-FE-change for NNA/flows once AE deploys. Only open item = AUA-toggle-inert gap; decision parked between (a) AE emits real total_aua_fee_paying/_no_fee (AE confirmed feasible — perf_ts has per-account daily MV) vs (b) FE per-metric synthetic flag (hasAuaSplit vs hasFlowSplit, keeps AUA synthetic-responsive). AE stood down (no deploy), resume-state banked (gold INF_D_00c@9950a3f2c + Lambda @982394f01 on CLOUD, rollback anchors retained). Resume: ping AE post-demo, settle a-vs-b.

## Discipline notes this segment
- Self-deactivating band-aid design (only flips single_stock->etf) made the DT-promote-vs-COO-HOLD timing cross PROD-safe — no panic, no revert churn.
- Deferred to COO on the submodule bump + the band-aid path rather than acting unilaterally — avoided a double-bump (DT owned it) + let the proper DS data fix supersede the band-aid.
- Honored Andrew's direct hold over the COO's DROP-IT (principal supersedes; flagged COO I'm holding).
- DT batch-promote protocol: accumulate on DEV, one ping on Andrew "ship it" (or immediate for urgent-single).
- No browser tool in env — visual-confirm routed to Andrew (:5173) / CVO throughout.
