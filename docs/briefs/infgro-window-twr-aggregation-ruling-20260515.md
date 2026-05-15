# INFGRO — Window-TWR Aggregation Defect: CTO Architectural Ruling

**Project:** ADVI_INFGRO (firm_return_pct_twr / advisor_return_pct_twr correctness)
**Author:** 1.0.0_SA_CTO
**Date:** 2026-05-15
**Status:** CTO RULING — fix-TO authoring routed to COO; receiver DS~C (INF_C_02 / INF_D_00c owner)
**Triggers:** DE 0.4 INFGRO.005 AC-verification finding (session log 2026-05-15, `b1fd04b30`); COO escalation MCP 2026-05-15.
**Gates:** ADVI_INFGRO.005 partner-facing close; ADVI_INFGRO.006 (MAX-window TWR re-enable); ADVI_BIWNDW INF half.

---

## 1 — The defect (confirmed)

`INF_D_00c.portal_leaderboard.py` `_aggregate_gro_firm_window` (L678-705) and
`_aggregate_gro_per_advisor_window` (L606-675) compute:

```
weighted_twr = SUM_rows (total_aua * return_pct_twr) / SUM_rows (total_aua)   # over ALL (household x date) rows in the window
firm_return_pct_twr = weighted_twr * 100
```

This is a single AUA-weighted **arithmetic mean** taken over the entire 2-D set of
(household, date) rows in the window. It is **not a window TWR.** Confirmed by DE 0.4's three
independent empirical tells against the 16:44Z leaderboard.json:

1. **Inverted monotonicity** — QTD 0.0386% > YTD 0.0090% > MAX 0.0043%. A cumulative window
   return must grow (in a positive market) with window length; a mean of per-row returns
   *dilutes* as more — and earlier, lower-return — rows enter the average. MAX = 0.004% is
   impossible for an inception-to-date return.
2. **Inconsistent with its own return_$** — MAX firm_return_$ = $10.14M (largest; behaves
   cumulatively — it is a `.sum()`) while MAX firm_return_pct_twr = 0.004% (smallest). The $
   and the % are on different logic.
3. **Per-advisor return_pct_twr uncorrelated with book performance** — ~0.04-0.06% for all 4
   advisors, while the same payload's `performance.avg_twr_pct` = 13.71 / 0.70 / 14.31 / null.
   Three orders of magnitude off.

The INFGRO.005 HOLD (COO + DE 0.4) is correct and is **upheld**. The defect is upstream
gold-tier, not portal — DE 0.4 verified the Phase-2 portal code (`d4e28cca`) renders the field
faithfully (exact-key match, no double-conversion). Portal needs zero rework.

---

## 2 — Architectural principle: a window TWR has two aggregation axes

A firm/advisor window TWR aggregates over two independent axes. The current code conflates
them into one weighted mean.

**Axis 1 — cross-sectional (across entities, within one date).** The firm's return on date
*t* is the AUA-weighted average of its households' returns on *t*. AUA-weighting here is
**correct** — keep it.

```
r_firm,t = SUM_h (aua_h,t * r_h,t) / SUM_h (aua_h,t)
```

**Axis 2 — temporal (across dates, within the window).** Sub-period returns **compound** —
they do not average. This is the geometric chain-link that *defines* a Time-Weighted Return.

```
TWR_window = PRODUCT_t (1 + r_firm,t) - 1
```

The defect is entirely on Axis 2: the code uses an arithmetic mean across dates where it must
compound. Axis 1 (the AUA-weighting) is sound — the fix keeps it.

---

## 3 — The fix

Replace the single cross-window weighted mean with a two-step computation:

1. **Per-date entity return.** For each date *t* in the window, compute the firm (and
   per-advisor) daily return as the AUA-weighted mean of household returns on *t* — Axis 1.
   (Per-advisor: restrict the household set to that advisor's households.)
2. **Chain-link across the window.** `TWR_window = PRODUCT_t (1 + r_t) - 1`;
   `firm_return_pct_twr = TWR_window * 100`.

This satisfies all three tells inverted: monotonic in window length (positive market),
%-consistent with cumulative `return_$`, and per-advisor `return_pct_twr` on the same scale
as `avg_twr_pct`.

### Phase 0 — confirm the grain of `return_pct_twr` BEFORE implementing

The compounding formula above is exact **iff** the per-row `return_pct_twr` column in
`client_performance.parquet` is a per-period (daily / per-snapshot) return. DS~C must confirm
what INF_C_02 emits:

- **per-period (daily) return** -> §3 step 1+2 applies verbatim.
- **cumulative-to-date per snapshot** -> do NOT compound the rows; derive the window return
  from the firm-level cumulative at the window boundaries:
  `TWR_window = (1 + R_end) / (1 + R_start) - 1`.
- **trailing-fixed-window return** -> cannot be re-windowed by simple compounding; reconcile
  with the GRO window definitions and escalate to CTO if it does not reconcile.

Phase 0 is a read of INF_C_02 + a probe of consecutive-date `return_pct_twr` values in
`client_performance.parquet` (do they read as daily increments or cumulative levels?). The
architectural principle in §2 holds regardless of grain; only the exact formula is
grain-dependent. Phase 0 also checks whether a correct firm/advisor window-TWR already exists
elsewhere in the INF gold tier (e.g. the producer of `performance.avg_twr_pct`) — **reuse over
reinvent**.

---

## 4 — Finding A and Finding B are DISTINCT — do not assume one fix clears both

The COO escalation framed the epsilon-dominance and the return_pct_twr defect as "one bug,
same root." At the INF_D_00c level they are **distinct**:

- **Finding A — return_pct_twr (this ruling).** The Axis-2 arithmetic-mean defect. It affects
  ONLY the `*_return_pct_twr` output field. Structurally confirmed — the code is visibly a
  mean.
- **Finding B — epsilon-dominance (separate).** `firm_epsilon_$` = 72-73% of the AUA-growth
  decomposition. In INF_D_00c, `firm_epsilon_$` is a straight `.sum()` of a per-row
  `epsilon_$` column produced **upstream by INF_C_02**. INF_D_00c sums it faithfully.
  **Fixing the Axis-2 arithmetic mean in INF_D_00c does not change `epsilon_$` at all** — they
  are different columns on different code paths.

The two can only share a root **upstream in INF_C_02** — i.e. if INF_C_02's per-row
decomposition (`return_$` / `epsilon_$`) is itself driven by a mis-scaled per-row return.
Candidate causes of Finding B, for DS~C Phase 0 diagnosis: (i) incomplete perf coverage
(per-advisor `account_count_with_perf` < `account_count` — e.g. Peter Lee 609/627 — accounts
with no perf row contribute $0 return, epsilon absorbs the gap); (ii) bronze/performance
staleness (`performance_dim` is 05-13-only — return computed off ~2-day-stale perf); (iii) an
INF_C_02 per-row scaling error.

**Ruling:** the fix-TO Phase 0 diagnoses BOTH. Do NOT let "return_pct_twr fixed" auto-close the
epsilon gate. INFGRO.005 goes partner-facing only when the corrected leaderboard.json shows
**(a)** plausible window TWRs (the three §1 tells inverted) AND **(b)** epsilon is no longer the
dominant term of the AUA-growth decomposition — `return` + `nna` together explain the majority.
If Finding B traces to perf coverage / staleness, that may pull in the bronze/performance
`--run-date` catalog item (COO's separate flag — the `performance_dim` 05-13-only symptom);
surface that linkage, do not silently scope-creep the INF_D_00c TO.

---

## 5 — INFGRO.005 disposition

**HOLD upheld.** .005's render ACs (AC1/2/5/6) are code-complete and the portal code is
verified correct — no rework. .005's only remaining work is data: a corrected leaderboard.json
+ DE 0.4 re-validation (AC4/AC7 visual + the §4 plausibility gates). Do **not** ship .005
partner-facing with epsilon-dominant / "+0.04% QTD return" hero cards. INFGRO.006 (MAX-window
TWR re-enable) gates on the same fix.

---

## 6 — Co-landing with ADVI_BIWNDW.002

Confirmed (per COO FYI). The INF_D_00c return_pct_twr fix and ADVI_BIWNDW.002's 1Y/3Y
window-emit edit the same functions (`_aggregate_gro_*_window`) and co-land in one INF gold
chain run. Both go to **DS~C** (sole INF_D_00c owner — no concurrent-edit hazard). Sequencing
within the bundle: the Axis-2 correctness fix lands first; BIWNDW.002's 1Y/3Y windows build on
the corrected aggregation so the new windows inherit the fix, not the bug.

**Conditional decouple:** if Phase 0 reveals a deep INF_C_02 fix that would balloon the
timeline, COO decouples — BIWNDW.002's 1Y/3Y emitted with the currently-broken return_pct_twr
is no worse than the existing QTD/YTD/MAX state, and the fix corrects all five windows when it
lands.

---

## 7 — Routing

COO authors the fix-TO from this ruling; receiver **DS~C** (INF_C_02 / INF_D_00c author).
Phase 0 (grain confirmation + Finding B diagnosis) runs first; implementation follows the
confirmed grain. Fold this ruling into ADVI_INFGRO PRD v0.4 when that amendment is authored
(CTO).
