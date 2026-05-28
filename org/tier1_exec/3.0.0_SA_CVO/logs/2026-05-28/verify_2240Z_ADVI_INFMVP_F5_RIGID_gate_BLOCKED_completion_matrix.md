# CVO RIGID Gate Verdict + ADVI_INFMVP / MDPF_SCOPED Completion Matrix

**archetype:** VALIDATE
**Trigger:** RD~B F5-RD RAVC2 (portal/DEV 48566175) + COO [DRIVE] fire-gate + CTO Andrew-directed honest completion matrix, 2026-05-28 ~2230Z
**Andrew directive:** ADVI_INFMVP must be 100%-complete + CVO-validated before he reviews. Nothing surfaces to Andrew until validated PASS. correctness > speed.

# HEADLINE: F5 RIGID GATE = BLOCKED

The cross-view-equality acceptance bar FAILS at the 3Y window for Peter. Two surfaces reading the SAME canonical source display DIFFERENT NNA for the same advisor × window × cohort — the exact defect F5 exists to eliminate, relocated from "different sources" to "different windowing of one source." The canonical DATA is correct; the F5-RD FE windowing repoint is not.

---

## F5 RIGID — empirical cross-view equality (Peter, quarterly granularity, adv cohort)

All 3 surfaces now read `advisor_nna_canonical.json` (confirmed in F5-RD diff 48566175). Substrate pre-verified clean (c8f4f02f9). The defect is in how the two trailing-window chart surfaces RE-DERIVE their window cutoff.

| window | Snapshot donut (precomputed `windows[W].nna`) | Continuous chart (`setDate(-days)` cutoff) | Lifetime Activity (`setFullYear(-yrs)` cutoff) | cross-view |
|---|---|---|---|---|
| 1Y | (not exposed — snapshot shows quarter-slices only) | $12,587,630.25 | $12,587,630.25 | continuous==Lifetime OK; **both ≠ true trailing-365d $13,796,544.32 (precomputed) by $1.21M** |
| **3Y** | (not exposed) | **$21,693,289.19** | **$24,464,137.77** | **MISMATCH $2,770,848.58 — BLOCK** |
| MAX | (not exposed) | $108,959,119.23 | $108,959,119.23 | OK (full series, no cutoff) |

Snapshot donut exposes only quarter-slices (q_current/q1/q2/q3 → `windows[q*].nna`, precomputed exact — CORRECT, no windowing bug). Continuous + Lifetime expose 1Y/3Y/Max; they are the directly-comparable pair.

### Root cause (deterministic, code + data grounded)
1. **Cutoff-method inconsistency between the two components:**
   - `DistributionTab.tsx:1567-1569` (continuous): `cutoff = new Date(latest+'T12:00:00'); cutoff.setDate(cutoff.getDate() - daysToShow)` → 3Y cutoff = **2023-07-01**.
   - `AdvisorAnalytics.tsx:161-163` (Lifetime): `cutoff.setFullYear(cutoff.getFullYear() - yearsBack)` → 3Y cutoff = **2023-06-30**.
   - Both filter the quarterly series `period_end >= cutoff`. The **Q2'23 bucket (period_end 2023-06-30, nna = $2,770,848.58)** is INCLUDED by Lifetime (2023-06-30 >= 2023-06-30) and EXCLUDED by continuous (2023-06-30 < 2023-07-01). That one bucket = the exact $2,770,848.58 gap.
2. **Cutoff derived from a FUTURE period_end:** the quarterly series' last `period_end` is **2026-06-30** (the current incomplete Q2'26 labeled with its calendar quarter-end; data_as_of is 2026-05-27). Both components compute trailing cutoffs from this future date, so every trailing window is shifted ~1 month forward and neither aligns to the canonical `window_bounds` (3Y start = 2023-05-28; 1Y start = 2025-05-27). That is why the displayed 1Y ($12.59M) ≠ the precomputed exact-boundary 1Y ($13.80M).

### Why it BLOCKS
PRD F5 AC5 + CTO REPAIR-AMENDMENT: "for the same window × cohort × fee-view, snapshot == continuous == Lifetime; any mismatch = BLOCKED." At 3Y, continuous and Lifetime disagree by $2.77M for Peter. This is a visible cross-view NNA disagreement — the precise class of defect Andrew photographed and the PRD mandates against.

### Fix (mechanism-specific — for RD, via COO re-dispatch)
The trailing-window chart surfaces must NOT re-derive a cutoff from the series' (future) latest `period_end`. Two clean options, either makes all surfaces agree exactly:
- **(a) Read the precomputed `windows[W].nna`** for the headline total (the snapshot already does this — it's the exact-boundary source of truth), OR
- **(b) Filter the series by the canonical `window_bounds[W].start/end`** (the emit already publishes these) instead of a locally-computed setDate/setFullYear cutoff.
Either way: (1) unify the cutoff method across DistributionTab + AdvisorAnalytics, and (2) anchor to canonical window_bounds, not the future period_end. Then continuous == Lifetime == precomputed window total for every window.

### Empirical basis
Deterministic replication of the shipped F5-RD windowing code against the verified canonical series. Browser-pixel confirmation not run (playwright MCP unavailable this session); the computation is deterministic so the render equals the computed values — available on request via /frontend-dev if COO/CTO want the visual capture. The BLOCK does not depend on it.

---

## Honest Completion Matrix — ADVI_INFMVP

| F | Feature | Status | CVO empirical verdict |
|---|---|---|---|
| F1 | Assets Overview zeroes fix | COMPLETE + PROD v2.1.103 | Data CORRECT: `partner_analytics.json total_aua = $205,530,479.45` ($205.5M, matches PRD). FE layout-resolution fix promoted (19ea88ce7). **Real external Peter-login smoke PENDING Andrew/QA** (X-Firm-Id at CF edge — structurally post-promotion, locally unverifiable). |
| F2 | Sidebar Tools/Trade-Submission strip | COMPLETE + PROD | Code-confirmed: `firmAccess.ts` inflection allowlist excludes `/trade-submission` (section auto-hides + route redirect). |
| F3 | Keyword popup precompute | COMPLETE | **PASS** (AC3d) — live probe Cache HIT 80ms (not GPT), 36 today-partition entries. Eyes-open: fallback window (days 1-7) EMPTY; HIT guarantee scoped to today's 36 keywords (routed to DS-MI). |
| F4 | Fee-split NNA tie-out | DS leg COMPLETE; **cross-artifact FINDING** | Substrate sum-invariant CLEAN (fee_paying+no_fee==total, all advisors × 9 windows). **BUT** leaderboard.json (Exec Summary Flows source, as-of 05-28) vs advisor_nna_canonical.json (Lifetime source, as-of 05-27) DIVERGE for Peter at **MAX (Δ$278,765.68)** and **1Y (Δ$743.00)**; tie at QTD/YTD/3Y. If Lifetime reads canonical while Exec Summary Flows reads leaderboard, AC4 "ties exactly across all windows (incl MAX)" FAILS at MAX/1Y. P1 — see below. |
| F5 | Canonical Advisor NNA + cross-view gate | DS emit COMPLETE; **RIGID gate BLOCKED** | Substrate EXHAUSTIVELY verified clean (below). FE repoint (F5-RD) BLOCKED — 3Y cross-view mismatch $2.77M (above). |

### F5 substrate — exhaustive verification (CLEAN, pre-gate)
The canonical emit `advisor_nna_canonical.json` (INF_D_00f) is sound:
- Fee-split sum-invariant: 0 failures across all 4 advisors × 9 windows + firm.
- Series bucket-sum: weekly/monthly/quarterly all tie to MAX exact for all 4 advisors (the 60%-sampling-loss fix confirmed at source).
- Firm rollup = sum of all 4 advisor-keys (incl `inflection_wealth_management` house book) across all 9 windows + firm series + firm fee-split.
- Quarter additivity: Peter q1 + q_current == YTD exact.
- **Upstream-faithful:** emit window-sums == `gold/canonical/canonical_nna_*.parquet` raw-row sums, QTD + YTD, all 4 advisor-keys, + inflow/outflow decomposition — to the cent. Emit faithfully aggregates its source; no transformation/corruption.

The data layer is correct. The bug is purely the FE windowing repoint.

### F4 cross-artifact finding (P1)
- leaderboard.json (`INF_D_00c` F11, generated 17:39Z, data_as_of 05-28) and advisor_nna_canonical.json (`INF_D_00f`, 20:29Z, data_as_of 05-27) are TWO separate NNA emits.
- Peter divergence: MAX Δ$278,765.68 (fee_pay $228,765.68 + no_fee exactly $50,000.00), 1Y Δ$743.00; QTD/YTD/3Y exact.
- No 2026-05-28 canonical_nna parquet exists — the 05-28 as-of label is not backed by a 05-28 source partition.
- Portal `AdvisorPublicProfile.tsx:292`: "All AUA/NNA/flows/fee totals come from the leaderboard entry." So Exec Summary Flows reads leaderboard; F5-RD repoints Lifetime to canonical. MAX is the DEFAULT chart period (`AdvisorBookAccountModal` useState 'MAX') and user-selectable — the divergence is reachable, not hidden.
- Fix (for DS/CTO): regenerate leaderboard fee_breakdown (INF_D_00c) from the SAME canonical_nna snapshot as INF_D_00f, OR repoint Exec Summary Flows to advisor_nna_canonical — single source per F5 mandate.

---

## Honest Completion Matrix — MDPF_SCOPED

| S | Feature | Status | Note |
|---|---|---|---|
| S3 | Multi-firm daily-parsed architecture (spine) | COMPLETE | backfill script + per-firm slice ca9a1ae34, COO RAVC2-ACCEPT. (CVO JSON cascade-aligned cycle 49.) |
| S4 | Canonical model naming | COMPLETE | display-mapping across 4 pages (06328859). |
| S1 | Partner-mode selector | IN-PROGRESS | scaffold only ("Select Partner:" dropdown shell d9e74ec3) — NOT data-wired. Not validatable as green. |
| S2 | Inflection 5/18 data shape | BLOCKED | on AE EC2 Orion daily backfill (~5h running). |

MDPF_SCOPED is NOT complete — S1 (data-wire) + S2 (backfill) are the open blockers. No green-wash: S1/S2 are explicitly in-flight.

---

## Project-completion blockers (the honest bottom line)
- **ADVI_INFMVP:** F5 RIGID gate BLOCKED (3Y cross-view $2.77M) + F4 cross-artifact MAX/1Y divergence (P1). NOT 100% — does not yet meet Andrew's "validated complete" bar. F1 real-login smoke also pending.
- **MDPF_SCOPED:** S1 data-wire + S2 backfill in-flight.

Neither primary is ready for Andrew's review. The F5-RD repoint needs one focused fix (unify cutoff + anchor to canonical window_bounds) — the substrate is clean, so the fix is FE-only and should be fast.

— 3.0.0_SA_CVO

---

## AMENDMENT (post RD~B rework d8647ec3 + Andrew framing correction, ~2300Z)

**Transparent correction to the verdict above.** Two changes after RD~B's rework + Andrew's steer:

1. **RETRACTED — the 5-window mismatch table was a window-vocabulary category error.** Exec Summary exposes QTD/YTD/Max (point-in-time aggregates from `windows[W]`); continuous + Lifetime expose 1Y/3Y/Max (bucket series). They share ONLY `Max`. Comparing Exec Summary's QTD/YTD aggregates against chart bucket-series sums (1Y/3Y) was not like-for-like — those vocabularies don't overlap and no surface shows both. Andrew correctly flagged this.

2. **FIXED — continuous vs Lifetime** (the genuine original cross-view inequality, 3Y $2.77M from setDate/setFullYear): RD~B's `window_bounds[W]` repoint (d8647ec3) makes both panels filter identical periods on the same series → they now agree with each other. Verified (1Y both $13,392,890.80; 3Y both $25,269,398.32).

**REMAINING genuine residual — LOGICAL windowing-semantics defect (Andrew's characterization, sharper than my mechanical framing):**
- The chart window-inclusion test `period_end <= window_bounds[W].end` means "periods that have FULLY ENDED within the window" = "up to the current period" — it structurally EXCLUDES the in-progress current period.
- Empirical: current quarter (2026Q2, period_end 2026-06-30, nna −$805,260.55) is dropped from ALL chart windows (1Y/3Y/MAX) because every window_bounds.end = data_as_of 2026-05-27 < 2026-06-30. The freshest, most demo-relevant data point is absent from every trend chart.
- Cross-view impact at the Max overlap: Exec Summary Max = `windows[MAX].nna` = $108,959,119.23 (correctly includes current quarter); chart Max = $109,764,379.78 (drops it) → **$805,260.55 gap**.
- The emit is internally correct (full series sum == windows[MAX]); the FILTER is the bug.

**Fix (logical — "include the current period, not up to it"):**
- (preferred, emit-side, DS-CP/INF_D_00f) clamp the in-progress bucket's `period_end` to `data_as_of` (2026-05-27, not the calendar quarter-end 2026-06-30). Semantically honest (the bucket's data ends at data_as_of) and fixes every consumer uniformly.
- (or FE-side, RD) inclusion test = bucket-data-overlaps-window (`min(period_end, data_as_of) >= window.start` etc.) instead of `period_end <= end`; for Max, take the include-all branch.

**Corrected verdict:** RIGID cross-view equality — continuous==Lifetime PASS; QTD/YTD clean (no chart overlap); **Max overlap BLOCKED on the current-period-exclusion logical defect**. Narrow + clean fix. Not demo-blocking IF the demo doesn't surface the Max view; QTD/YTD are clean. Routed corrected.

— 3.0.0_SA_CVO
