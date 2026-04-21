# COO Briefing — HLOT2 dual-patch

**From:** 0.4.0_DS_ClientPlatform~A
**To:** 2.0.0_SA_COO (TO author)
**Subject:** HLOT2 TO authoring packet — decision-ready inputs for single-commit dual-patch on B_01.holdings_lots.py
**Status:** Phase 0 complete, CTO signed off 20260420T221414Z, all four pre-commit extensions resolved.
**Urgency:** Andrew directive "I want a solution for this immediately" 2026-04-20 21:38Z. Nightly 23:00 UTC already held per your 21:41Z dispatch to AE. End-to-end ~3h from TO dispatch.

---

## TL;DR

Portal Books tab Firm Overview Top Holdings is reading 3-6 percentage points below Opal aggregate model targets on six of the nine top positions. Root cause is B_01.holdings_lots.py producing a starved input to D_03.composition_artifacts.py. The starvation has TWO orthogonal mechanisms; HLOT2 ships one commit with both patches.

Expected combined recovery: ~$181M across DIVZ / IEFA / SPYM / IDVZ / IEMG / SPHY. Firm total_aua unchanged at $1.649B (D_03 scales via account_performance). Mix composition restored toward model targets.

---

## Observed gap (Andrew's screenshot 2026-04-20)

Books tab firm-level Top Holdings vs aggregate model (assumes 80pct firm-in-model coverage):

| Rank | Ticker | Current | Model target (firm) | Gap | Gap to close |
|---|---|---:|---:|---:|---|
| 1 | IDVZ | 7.88pct | 8.84pct | -0.96pp | $15.9M |
| 2 | IEFA | 7.60pct | 10.90pct | -3.30pp | $54.5M |
| 3 | PFDE | 6.75pct | 6.85pct | -0.09pp | clean |
| 4 | PFOE | 6.26pct | 6.66pct | -0.40pp | clean |
| 5 | SPYM | 4.67pct | 7.31pct | -2.64pp | $43.5M |
| 6 | DIVZ | 4.54pct | 10.41pct | -5.87pp | $96.8M |
| 7 | BIV  | 3.32pct | 3.61pct | -0.28pp | clean |
| 8 | IEMG | 3.23pct | 4.13pct | -0.89pp | $14.8M |
| 9 | SPHY | 3.00pct | 3.54pct | -0.53pp | $8.8M |

Sum of model-gap across these six: **-$181M firm-level underweight on six of the top nine holdings**.

---

## Mechanism attribution (evidence-file-trace complete)

### Patch A — CA-Merger classifier bug (DIVZ only)

**What it is:** B_01.holdings_lots.py L2186-2213 classifies every Corporate Action row whose `transaction_sub_type` is in {Merger, Conversion Out, Exchange, Tender, Cash in Lieu} as `CA_SELL`. But BD records identity-migration events (ticker renames, share-class consolidations) as TWO paired rows on the same (account_id, asset_id, trade_date) where BOTH rows carry positive `units` and MV signs distinguish direction (incoming side +MV, outgoing side -MV).

**Evidence:**
- 20/20 DIVZ silent-close sample accts have the 2025-06-16 Merger pair on asset_id 3680584 (OPAL DIVIDEND INCOME ETF -> POLEN DIVIDEND INCOME ETF rename)
- Per-subtype scan of 7,615 CA rows across 12-month window: 7,540 Merger rows = exactly 3,770 +MV / 3,770 -MV pairs, 100pct on the DIVZ rename
- Under current classifier: both rows fire CA_SELL, FIFO double-sells 2X units against BUY total of X, lots zero
- Under Patch A: +MV side classified as CA_BUY, -MV side remains CA_SELL, net-zero FIFO impact as intended

**Scope:** Deterministic; only affects BD-internal identity-migration recordings. No other Top-9 ticker shows the pattern.

**Expected recovery:** ~$78.6M on DIVZ.

### Patch B — silver/unrealized-authoritative re-open (IEFA + IDVZ + SPYM + IEMG + SPHY)

**What it is:** silver/transactions is systematically incomplete for held-away positions. FIFO reconstructs only the transactions present, which on these cohorts produces net-negative or partial current_units even though snapshot sources (canonical/holdings source=reconciled with bd_units = schwab_units agreement + silver/unrealized open-positions feed) say the position is open at a specific share count.

**Evidence:**
- 99.6pct / 98.9pct / 95.5pct of the DIVZ / IEFA / IDVZ silent-close cohorts have (acct, cusip) rows in silver/unrealized that confirm the position is open.
- 100pct of overlap cohorts (accts where lots has SOME open units but fewer than canonical) have silver/unrealized coverage.
- 20-acct sample probes:
  - IEFA: 41 Sale vs 17 Buy rows, zero CA, 18/19 net-negative FIFO
  - IDVZ acct z0813100811 end-to-end: 780 BUY units vs 957 SELL units, canonical 458.6 units open, implying ~635 units of unrecorded BUYs
  - SPYM: 8 Buy vs 11 Sale, zero CA, mostly positive net but still silent-closed = missing-BUYs pattern
  - IEMG: 5 Buy vs 12 Sale, zero CA, 10/10 net-negative
  - SPHY: 5 Buy vs 5 Sale, zero CA, 2/8 net-negative

Fix is not about correcting silver/transactions (upstream ingestion problem, separate workstream). Fix is about B_01 respecting the snapshot authority when the transaction log is incomplete.

**Scope:** The fix widens the existing SL-P1 sleeve-shadow path (B_01 L860+, `_build_uln_sleeve_shadow_lots`) from a 598-acct cohort to universal billable (alloc_noncash >= $1000). Priority chain:
1. silver/unrealized confirms (acct, cusip) open -> inject synth lot, source='silver_unrealized_reopen'
2. silver/unrealized silent AND canonical/holdings confirms -> inject synth lot from canonical, source='canonical_holdings_reopen' (closes the 25 uncovered accts)
3. Both silent -> stay closed (preserves Rule 3 / RPS / PIVOT 5 legitimate closures)

**Expected recovery:** ~$102.7M (IEFA $49.8M + SPYM $43.5M + IDVZ $15.9M + IEMG $14.8M + SPHY $8.8M) + residual from other held-away tickers outside Top-9.

---

## Orthogonality (CTO concurred 20260420T220829Z)

- Patch A fires at FIFO classifier stage (pre-zeroing). Fixes DIVZ before FIFO produces current_units=0 in the first place.
- Patch B fires post-FIFO (post-zeroing re-open). Re-opens positions that legitimate FIFO processing zeroed due to tx-feed gaps.
- On DIVZ: Patch A restores FIFO so Patch B's current_units=0 predicate is false -> Patch B does not fire on these lots. No double-count.
- On IEFA/IDVZ/SPYM/IEMG/SPHY: Patch A is null (no Merger pairs), Patch B activates solo.
- Additive by construction. Single commit, single qa-runner cycle.

---

## TO acceptance criteria (ready to copy-paste)

```xml
<acceptance_criteria>
- [ ] Patch A: paired_subs set at B_01.holdings_lots.py:2186-2213 = {Merger, Conversion Out, Exchange, Tender, Cash in Lieu}. For rows where transaction_sub_type in paired_subs AND market_value >= 0, classify as CA_BUY instead of CA_SELL.
- [ ] Patch B: new/widened function emitting synth lots for (acct, cusip) pairs where (a) alloc_noncash >= $1000 AND (b) FIFO current_units == 0 or no lot exists AND (c) silver/unrealized OR canonical/holdings confirms position open.
- [ ] Patch B priority chain: silver/unrealized authority first (Tier 1), canonical/holdings fallback (Tier 2). source tag = 'silver_unrealized_reopen' or 'canonical_holdings_reopen' per tier.
- [ ] Patch B regression guard: zero re-opens for (acct, cusip) where BOTH silver/unrealized AND canonical/holdings are silent (preserves Rule 3 / RPS sell-correction / PIVOT 5).
- [ ] Pre-commit: run Patch A against 100 random accts with paired_subs rows where MV signs already disambiguate correctly. Expect zero behavior delta.
- [ ] Post-fix comp-pipescript io B_01.holdings_lots: no new COLUMN GAPS.
- [ ] qa-runner --from B --chain completes without regression on c6a.8xlarge.
- [ ] Per-patch + per-ticker + per-tier attribution in comparison pack:
    - DIVZ recovery attributable to Patch A: expect ~$78.6M
    - IEFA recovery attributable to Patch B Tier 1: expect ~$49.8M
    - SPYM recovery attributable to Patch B Tier 1: expect ~$43.5M
    - IDVZ recovery attributable to Patch B Tier 1: expect ~$15.9M
    - IEMG recovery attributable to Patch B Tier 1: expect ~$14.8M
    - SPHY recovery attributable to Patch B Tier 1: expect ~$8.8M
    - Tier 2 (canonical_holdings_reopen) coverage: expect ~25 accts, ~$1-2M
    - Any recovery on wrong patch: FLAG as unexpected interaction
- [ ] BFIX2 subsumption probe: measure post-HLOT2 BFIX2 re-inject cohort size. Expect shrinkage (HLOT2 absorbs some BFIX2 scope). Document in comparison pack.
- [ ] Post-fix firm_composition.json Top-9 pcts within 1pp of model targets (assuming 80pct firm-in-model coverage):
    - DIVZ ~9-10pct / IEFA ~10-11pct / IDVZ ~8-9pct / SPYM ~6-7pct / PFDE ~6-7pct / PFOE ~6-7pct / IEMG ~3-4pct / BIV ~3-4pct / SPHY ~3pct
- [ ] Firm total_aua unchanged at $1.649B (D_03 scales via account_performance; not affected by holdings_lots delta).
- [ ] Schema invariants: units, market_value, cusip, asset_name, is_open columns unchanged. Only count of lots + MV totals shift.
- [ ] Session log with Compiler Tools section includes comp-pipescript io B_01 (pre + post), comp-validate B_01 if config exists, comp-blast on changed functions.
</acceptance_criteria>
```

---

## Scope negatives (explicit non-goals)

- Do NOT revert cd00ff2c (Rule 3 / Gate 3 silent-close), ae759bbb (RPS-silence-not-close), 1db831aa (cusip-keyed merge), 7e57576f (PIVOT 5 alloc-billable gate), or cb6d78e2 (tiered unit cap). All four landed for legitimate reasons.
- Do NOT fix silver/transactions ingestion. Upstream completeness issue; separate workstream (likely CP-AE1 or new DE TO).
- Do NOT extend paired_subs to Reverse Split or Spinoff in this commit. 5 +MV Reverse Split rows and 5 -MV Spinoff rows surfaced in Extension 1 are edge cases worthy of follow-up HLOT3 TOs; flagged on CTO backlog.
- Do NOT address the PCHI / QQQ / ICSH / UTWO "missing from top-9 display" observations. Those positions are below the top-9 cutoff and not a data-quality issue at this scope.
- Do NOT change D_03.composition_artifacts.py, D_04, or any downstream consumer. The fix is strictly in B_01 at the FIFO classifier + re-open path.

---

## Files and code sites

**Patch A site:** `data/black_diamond/scripts/gold/B_01.holdings_lots.py` L2186-2213
- ~6-line addition
- New variable: `paired_subs` frozenset
- Modified: `is_ca_buy`, `is_ca_sell` computation

**Patch B site:** `data/black_diamond/scripts/gold/B_01.holdings_lots.py` L860+ (`_build_uln_sleeve_shadow_lots`) OR factor into a new parallel function `_build_authoritative_reopen_lots`
- ~40-60 line addition
- Widen cohort predicate from 598-acct sleeve to `alloc_billable_accts` (already in scope from PIVOT 5 load)
- Add canonical/holdings fallback authority at Tier 2

**Call site for Patch B:** insert in main build flow after `_apply_rps_lot_corrections` and before `_apply_silver_noncash_cap` (so re-opened lots can receive cap treatment if needed). Existing SL-P1 call pattern at L2538 for reference.

---

## Session context

- BFIX1+2 (081223b5) already on S3 per DT 20:34Z (42 MATCH 0 STALE 0 MISSING). Ships same qa-runner cycle as HLOT2. `--from B --chain` validates both B_01 HLOT2 + B_00 BFIX1/2 cascade in one pass.
- D_02 fix-forward 048af6a3 + D_00 + D_04 widen 8593ea51 already validated by ~D today; independent of HLOT2.
- ~A commit author line per mandate: `0.4.0_DS_ClientPlatform~A <0.4.0_DS_ClientPlatform~A@opal.agent>` with `git commit --only -- data/black_diamond/scripts/gold/B_01.holdings_lots.py data/black_diamond/diagnostics/STAUDT/HLOT1/* docs/briefs/coo_briefing_hlot2_dual_patch.md org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-04-21/staudt_hlot_top_holdings_meter.md org/compiler-tools-log.md`

---

## Evidence pack index

Location: `data/black_diamond/diagnostics/STAUDT/HLOT1/`

| File | Content |
|---|---|
| `hlot1_attribution_report.md` | Original Phase 0 attribution (4 gates ruled out) |
| `hlot1_correction_three_mechanisms.md` | Post-Andrew-pushback three-mechanism correction |
| `transaction_history_spot_check.md` | 20-acct DIVZ Merger CA verification |
| `top9_gap_profile.csv` + `.parquet` | All Top-9 tickers per-ticker gap + mechanism fingerprint |
| `model_vs_current.csv` | 28-ticker model target vs current firm composition comparison |
| `divz_silent_close_gate_eval.parquet` | 2,600-row per-acct gate evaluation DIVZ |
| `iefa_silent_close_gate_eval.parquet` | 559-row per-acct gate evaluation IEFA |
| `iefa_overlap_unit_shortfall.parquet` | 4,143-row per-acct unit gap IEFA overlap |

Also in `.runtmp/` (uncommitted): canonical/holdings, holdings_lots, silver/unrealized, silver/allocations, silver/RPS, firm_composition (stale + live), bd_transactions_backup, bd_assets_dim — raw parquets used for probes.

---

## Ask

1. Author HLOT2 TO at `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_STAUDT.HLOT2.ds-b01-ca-classifier-and-silver-unrealized-reopen.md` with the acceptance_criteria block above.
2. Dispatch GO to ~A. I commit within 30 min.
3. Orchestrate DT upload + AE qa-runner + comparison pack + PROD deploy per your standard 9-step.

CTO signed off on shape. Andrew chat-authorized "solution immediately." Nothing outstanding on my end.

Standing by.
