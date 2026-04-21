# ADVI_STAUDT.HLOT2 — B_01 dual-patch (CA classifier + silver/unrealized re-open)

**Agent:** 0.4.0_DS_ClientPlatform~A
**Date:** 2026-04-21
**Task order:** `ADVI_STAUDT.HLOT2` (COO 979bb971; status pending → begin 2026-04-21 12:24Z)
**Status:** commit landed; standing by for DT upload + AE qa-runner `--from B --chain`

---

## Summary

Dual-patch on `data/black_diamond/scripts/gold/B_01.holdings_lots.py`. Single commit; B_00 fix-forward `1a54d46a` lands in the same qa-runner cycle if DT batches.

- **Patch A** — CA-Merger MV-sign disambiguation at L2186-2213 (~18 lines added). Flips +MV paired-CA rows from CA_SELL to CA_BUY for `{Merger, Conversion Out, Exchange, Tender, Cash in Lieu}`. Fixes DIVZ silent-close via OPAL→POLEN 2025-06-16 rename pair (2,600 accts / $78.6M expected recovery).
- **Patch B** — `_build_authoritative_reopen_lots` new function + call site. 3-tier snapshot-authority re-open with 4-way source tags for attribution clarity (`silver_unrealized_reopen` / `silver_unrealized_topup` / `canonical_holdings_reopen` / `canonical_holdings_topup`). Fixes IEFA + IDVZ + SPYM + IEMG + SPHY silent-close + overlap cohorts (~$102.7M expected recovery).
- **Cap interaction** — Patch B emits BEFORE `_apply_silver_noncash_cap`; new tags added to `HIGH_CONF` (T1 protected). Cap still enforces silver_noncash ceiling on B/C phantom lots; reopen lots never compressed.
- **ACCEPTANCE FLEX** — TO L112 condition (b) "current_units == 0 OR no lot exists" widened to "FIFO current_units < 99pct canonical_units" to recover overlap cohort (~$66M, per TO expected-recovery table). COO ACK 20260421T122952Z; CTO ACCEPT 20260421T123116Z.

**Expected combined recovery: ~$181M** holdings_lots meter close across six Top-9 underweight tickers. Firm `total_aua` invariant at $1.649B (D_03 scales via account_performance).

---

## Files modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/B_01.holdings_lots.py` | +215 / -14. Patch A classifier fix + Patch B new function `_build_authoritative_reopen_lots` + call site + HIGH_CONF extension in `_apply_silver_noncash_cap`. |

One file; one commit. See commit message body for three-segment diff summary.

---

## Compiler Tools

### Phase 1 — before write

| Tool | Command | Result | Note |
|---|---|---|---|
| comp-pipescript io | `comp-pipescript io B_01` | PASS | READS: ACCOUNTS_DIMENSION + silver/bd_assets_dim. WRITES: holdings_lots + backfill + shadow + v2_dryrun. No COLUMN GAPS. silver/transactions + silver/unrealized + silver/RPS reads not indexed (ADHC_ROUTER Phase 2 known gap); all three have direct grep confirmation in source; new function `_build_authoritative_reopen_lots` uses `_read_parquet_from_s3(_resolve_unrealized_key(...))` + `_read_parquet_from_s3('gold/canonical/holdings/{date}.parquet')` — no new WRITE key added. |
| comp-platinum reverse | `comp-platinum reverse platinum/firm/firm_composition.json` | PASS | Speculative matches enumerate AdvisorIntelligence / AdvisorsTab / ClientsTab / DistributionTab / PartnerAnalytics consumers. Expected set; no unanticipated consumer surfaced. |
| comp-transform schema-check | `comp-transform schema-check AdvisorBookView` | PASS | "All rendered fields match their response types." No MISSING on Top Holdings / Mix composition render path. UNUSED entries are pre-existing non-Books-tab fields. |
| comp-cache collisions | `comp-cache collisions` | PASS | Exactly the 4 existing shared keys (advisor-book-view + advisor-intelligence/timeseries-overview + firm-leaderboard + partner-analytics/granularity). No new collision. |

### Phase 2 — before commit

| Tool | Command | Result | Note |
|---|---|---|---|
| ast.parse smoke | `python -c "import ast; ast.parse(open('B_01.holdings_lots.py').read())"` | PASS (exit 0) | Syntactic validity confirmed. Same-class gate that would have caught 081223b5 defaultdict NameError + 048a6fa3 D_02 KeyError locally. |
| importlib exec_module smoke | `python -c "import importlib.util; spec=spec_from_file_location('B_01',path); m=module_from_spec(spec); spec.loader.exec_module(m)"` | PASS (exit 0) | All module-level imports resolve; no NameError / ImportError. Spot-check: `_build_authoritative_reopen_lots` callable; `CA_SELL_SUBTYPES` / `CA_BUY_SUBTYPES` intact. |
| comp-pipescript deployed | `comp-pipescript deployed B_01` | STALE (expected) | Local md5 fd1531fec... vs S3 ad9b5638... — commit pending; DT upload next. |
| comp-blast | `comp-blast holdings_lots` | graph-gap (expected) | "No downstream consumers found" — ADHC_ROUTER Phase 2 indexer gap documented in TO. Evidence-file-trace from HLOT1 briefing §4 is authoritative substitute (positions_cube, C_00, D_02, D_03, D_04, fee/tax). No new downstream introduced; Patch B adds only source enum values to existing lot rows. |
| Patch A regression guard | 50-partition sample, 50 CA rows non-DIVZ | PASS (no unexpected flips) | 6 rows flipped — ALL `Merger` subtype on asset_id 2561 on 2026-02-02 exhibiting the same paired +MV/-MV identity-migration pattern as DIVZ 3680584 on 2025-06-16. These flips are the intended behavior (Patch A fixes this class broadly, not just DIVZ). Zero rows where OLD classifier was already correct flipped. Zero false-positive flips on non-paired rows. |

### Phase 3 — after commit (deferred until qa-runner comparison pack)

| Tool | Command | Expected |
|---|---|---|
| comp-validate | `comp-validate B_01 --artifact gold/timeseries/holdings_lots/{DATE}.parquet` | SKIP-by-default (B_01 has no dedicated validator block in gold_validate_config.yaml). Substituted by Phase 3 per-patch per-ticker per-tier attribution table in comparison pack. |
| per-patch attribution | comparison pack vs briefing table | DIVZ Patch A ~$78.6M / IEFA Patch B Tier 1 ~$49.8M (silent $14.4M + topup $35.4M) / SPYM ~$43.5M / IDVZ ~$15.9M / IEMG ~$14.8M / SPHY ~$8.8M. Tier 2 `canonical_holdings_*` ~25 accts / $1-2M. ±10pct. Wrong-patch = FLAG. |
| BFIX2 subsumption | post-HLOT2 BFIX2 re-inject cohort size vs 62 accts / $14.2M at 1a54d46a | expected shrinkage; GROWTH = FLAG. |
| firm total_aua invariant | firm_composition.json total_market_value | unchanged at $1.649B. |

**What worked:** evidence-file-trace discipline caught the three-mechanism reality during Phase 0 that would have shipped as single-mechanism fix. Pre-flag ACCEPTANCE FLEX on widened-(b) within 60s window closed the TO-predicate vs expected-recovery inconsistency cleanly. 4-way source tag (reopen/topup × silver_unrealized/canonical_holdings) gives comparison pack per-cohort attribution without instrumentation.

**What failed:** `comp-blast` still returns "No downstream consumers" on the top-level artifact name — known ADHC_ROUTER Phase 2 indexer gap. Not a blocker (evidence-file-trace from HLOT1 briefing §4 is authoritative), but worth filing as a graph tool enhancement TO.

**Gap found:** `comp-validate` has no block for B_01 in `gold_validate_config.yaml`. Substituted with per-patch per-ticker per-tier attribution table in comparison pack (post-qa-runner). Follow-up: file a TO to author `comp-validate B_01` config block once HLOT2 lands + attribution table format is stable.

One-line log appended to `org/compiler-tools-log.md` covering the 8 compiler runs above.

---

## Patch A detail

**Site:** `B_01.holdings_lots.py:2186-2213` (inside `build_holdings_lots_snapshot` FIFO classifier).

**Logic:**
```python
_HLOT2_PAIRED_SUBS = frozenset({'Merger', 'Conversion Out',
                                'Exchange', 'Tender', 'Cash in Lieu'})
_is_paired_incoming = (is_ca
                       & txn[sub_col].isin(_HLOT2_PAIRED_SUBS)
                       & (txn['market_value'] >= 0))
is_ca_buy = (is_ca & txn[sub_col].isin(CA_BUY_SUBTYPES)) | _is_paired_incoming
is_ca_sell = (is_ca & txn[sub_col].isin(CA_SELL_SUBTYPES)) & ~_is_paired_incoming
```

Effect: rows where `transaction_type == 'Corporate Action'` AND `transaction_sub_type in paired_subs` AND `market_value >= 0` flip from CA_SELL (original) to CA_BUY. All other CA rows unchanged. FIFO pair of (+60.6654 units / +2101.95 MV) + (+60.6654 units / -2101.95 MV) now classifies to (CA_BUY / CA_SELL) instead of (CA_SELL / CA_SELL). Net FIFO impact: zero instead of -120 units.

**Evidence of paired pattern for other assets beyond DIVZ:** regression guard surfaced 6 Merger rows on `asset_id=2561` on `2026-02-02` with the same +MV/-MV pair shape. These flips are intended — Patch A fixes the mechanism broadly, not just DIVZ. Confirmed `asset_id=2561` has +MV and -MV Merger rows on the same trade_date; OLD classifier fired CA_SELL on both; NEW classifier correctly routes +MV to CA_BUY and -MV to CA_SELL.

---

## Patch B detail

**Function:** `_build_authoritative_reopen_lots(df, snapshot_date, accounts_dim, rps_context)` at `B_01.holdings_lots.py` (inserted above `_build_rps_synthetic_lots`).

**Cohort gates:**
1. `alloc_billable_accts` — accounts with `silver/allocations.account_market_value - cash_market_value >= $1000` (inherits PIVOT 5). Loads from `rps_context` if available; else loads fresh from silver/allocations.
2. Canonical/holdings row present for (acct, cusip) with units > 0 and price > 0.
3. Shortfall: `canonical_units - FIFO_current_units > 1pct of canonical_units`.

**Authority resolution (4 tags):**
- `silver_unrealized_reopen` — Tier 1 + silent-close (FIFO current_units=0)
- `silver_unrealized_topup` — Tier 1 + overlap shortfall (FIFO has some units but < 99pct of canonical)
- `canonical_holdings_reopen` — Tier 2 + silent-close (silver/unrealized silent on (acct, cusip))
- `canonical_holdings_topup` — Tier 2 + overlap shortfall

**Lot shape:**
- `units` = `canonical_units - FIFO_current_units` (shortfall only; top-up not replacement)
- `current_price` = canonical `price`
- `market_value` = units × price
- `cost_per_unit` = current_price (→ `cost_basis` = market_value → `accrued_gain` = 0 on day-of-reopen)
- `acquisition_date` = snapshot_date (synthetic, not back-dated)
- `purchase_year` = snapshot_date year
- `is_open` = True; `holding_period_days` = 0; `term` = 'short_term'
- `lot_id` = `'{acct}:{cusip}:hlot2_reopen:1'`
- Cost-basis rationale: synth top-up should NOT claim realized gain if sold today; conservative cost = current_price means zero accrued_gain. Downstream cap (T1 protected) pass-through.

**Call site:** between `_apply_rps_price_override` (L2562-2568) and `_apply_silver_noncash_cap` (L2582). Kill switch `HLOT2_REOPEN_DISABLE=1`. try/except so PROD is not blocked if re-open fails.

**Cap interaction:** 4 source tags added to `HIGH_CONF` inside `_apply_silver_noncash_cap`. Reopen lots classified as T1, excluded from B/C compression. Cap still clips B/C phantom FIFO lots against silver_noncash ceiling — re-opens add to account total without being compressed themselves.

---

## ACCEPTANCE FLEX trail

Per feedback_acceptance_flex_preflag_is_write_before_acting.md, 1-line ACCEPTANCE FLEX pre-flag fired BEFORE deviating commit.

**Original TO (L112):** `(b) FIFO current_units == 0 OR no lot exists`
**Substituted:** `(b) FIFO current_units < 99pct canonical_units` (silent-close is the degenerate case)
**Why:** TO predicate would have hit ~$66M attribution shortfall vs. TO expected-recovery table (which includes overlap cohort per briefing L32-35).
**MCPs:**
- DS~A to COO + CTO 20260421T122822Z ("60s don't-object window")
- COO ACK 20260421T122952Z (authorized; TO authorship miss confirmed)
- CTO ACCEPT 20260421T123116Z (per COO relay) + 3 non-blocking clarifications on tax-lot identity / cap interaction / attribution split

**Non-blocking clarifications addressed in this commit:**
1. Tax-lot identity: 4-way source tag (reopen/topup × Tier-1/Tier-2) for attribution clarity. cost_basis = current_price for conservative accrued_gain=0 on day-of-reopen. acquisition_date = snapshot_date (synthetic).
2. Cap interaction: moved Patch B to BEFORE cap; added 4 tags to HIGH_CONF (T1 protected). Cap still enforces silver_noncash ceiling on B/C phantom lots.
3. Attribution split: 4-way tag enables silent-vs-topup split in comparison pack without additional diagnostic instrumentation.

---

## Decisions made

| Decision | Rationale |
|---|---|
| 4 source tags (reopen × topup × tier1 × tier2) not 2 | CTO clarification #1 non-blocking + clean comparison-pack attribution |
| Patch B emits BEFORE cap + HIGH_CONF extension | CTO clarification #2 non-blocking — cap still enforces silver_noncash ceiling on phantoms; reopens preserved |
| Shortfall threshold = 1pct of canonical | Balance between noise (tiny fractional divergence) and real shortfall. Conservative — skips FIFO-sufficient cases. |
| cost_basis = current_price (accrued_gain=0 day-of-reopen) | Conservative — no phantom realized gain on next sale. Real basis recovery is HLOT3 follow-up (FIFO can rebuild from silver/transactions BUY stream when upstream feed is fixed). |
| acquisition_date = snapshot_date | Matches SL-P1 synth-lot convention. Back-dating from silver/unrealized.open_date is a refinement for HLOT3 (short/long-term tax classification). |
| Call site after cap moved to BEFORE cap | Initial impl was AFTER cap (safer from compression); moved per CTO clarification #2 + HIGH_CONF extension makes BEFORE cap safe and preserves ceiling enforcement on phantoms. |
| No attempt to correct silver/transactions ingestion | Upstream (CP-AE1 or DE lane); explicitly out of HLOT2 scope per TO §scope-negatives. |

---

## Blockers

None. Commit complete. Standing by for DT S3 upload + AE qa-runner `--from B --chain` dispatch.

---

## Current state

`1a54d46a` (B_00 NameError fix) on CLOUD, already on S3 per DT 12:17Z.
HLOT2 B_01 commit (this session) on CLOUD, pending DT S3 upload.
~D's D_02 fix-forward 048af6a3 + D_00 + D_04 widen 8593ea51 already validated via `--chain bcd` yesterday.

Next ship cycle: AE qa-runner `--from B --chain` on c6a.8xlarge; if DT batches with 1a54d46a upload, single run validates BFIX1+2 + HLOT2 together. Comparison pack + RAVC4 close on completion.

---

## Next steps

1. **[0.4.0_DT_ClientPlatform]** Pull commit from CLOUD, upload `git show {SHA}:data/black_diamond/scripts/gold/B_01.holdings_lots.py` to `s3://opal-data-bd/code/gold/B_01.holdings_lots.py`. Expected post-upload comp-pipescript deployed B_01 = MATCH. Batch with 1a54d46a if timing permits.
2. **[0.6.0_AE_PartnerETL]** qa-runner `--from B --chain` on c6a.8xlarge (or c6i.16xlarge if capacity). ~1.5-2h.
3. **[0.4.0_DT_ClientPlatform]** comparison pack post-qa-runner:
   - Per-patch per-ticker per-tier attribution table (expected vs observed)
   - BFIX2 subsumption probe (re-inject cohort size)
   - firm `total_aua` invariant check ($1.649B)
   - Top-9 firm_composition.json pcts vs model targets (±1pp)
   - Tiered cap clip-count before/after (expect no material increase)
4. **[0.4.0_DS_ClientPlatform~A]** RAVC4 close MCP to COO on commit SHA + attribution table + evidence citations + pass/fail on each acceptance criterion. Cites ACCEPTANCE FLEX per Rule 7.
