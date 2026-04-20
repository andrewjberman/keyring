# Session — 0.4.0_DS_ClientPlatform~ABC — 2026-04-17 (session L)

**Agent:** 0.4.0_DS_ClientPlatform~ABC
**Window:** 15:56Z (overshoot tapering GO received) — 17:58Z (cap shipped, MCP COMPLETE to base DS)
**Scope:** CP-DS1 Gate 2 overshoot side — received three-bucket tapering brief, ran two-pass
forensic that refuted the brief's RPS-premium + private-fund + liability-type hypotheses in
favor of a unit-count framing, worked the surgical B+C cap design with Andrew in chat,
validated $61.48M of confirmed-cusip ETFs would be wrongly compressed under the original
proportional cap, wrote the cap into B_01 with the two CTO-approved adds
(market_value_uncapped + per-acct log line), shipped end-to-end. Also produced two companion
briefs for follow-up: canonical_prices share-class audit (BND example) and cap timing rule.

## Current State (leaving off at T1758Z)

**HEAD:** `cb6d78e2` (surgical B+C cap) — committed, pushed to `origin/CLOUD`, S3 MATCH confirmed
**TO status:** informal overshoot-tapering GO delivered via MCP brief + chat; CP-DS1 remains active
**Pending action:** awaiting QA runner fire on bd-gold-qa-runner (i-0090b823a4a0997e3) for
snapshot_date 2026-04-15, --single B_01. Base DS coordinating with COO on single-SSM-command
discipline (must not collide with ~B's CP-DS1 Run 9).

**Expected QA run outcome (from pre-commit simulation against 2026-04-15):**
  - accts-fired: ~2,553
  - mv-removed total: ~$121.2M  (from_B ~$115.2M, from_C ~$6.1M, **from_A $0**)
  - firm run11 POST-cap: ~$1,636.5M
  - silver canonical: $1,694.6M
  - gap: −3.43% (undershoot side; owned by ~XYZ workstream)
  - high-conf-exceeded: ~3 (all T1==silver equality, cosmetic)
  - market_value_uncapped: preserved on every lot

## Session Arc (chronological)

### 1. GO received + diagnosis pass 1 (15:56Z — 16:02Z)
Brief `docs/briefs/ds-brief-abc-overshoot-tapering.md`: three-bucket framing. Bucket 1
RPS price premium (1,531 accts, +$111M), Bucket 2 AQR DELPHI private-fund (9 accts, +$5M),
Bucket 3 FIFO cost basis inflation (9 accts, probably liability-type).
Ran `comp-pipescript io B_01` (no column gaps). Built `cp_ds_abc_overshoot_diagnosis.py`
(schema probe) + `cp_ds_abc_overshoot_pass2.py` (full classification).

**Key finding that inverted the brief:** 100% of overshoot is `linear_interpolation`-dominant,
not `rps_injection`. 1,626 of 1,628 overshoot accts dominant=linear_interp; `rps_injection`
dominates 0. The "RPS premium" framing was wrong.

Delta-pct bands: only 10% of $123M in 5-15% (plausible); 65% in 30-100%; 3% >100%.

### 2. Bucket 2 + 3 refinement (16:03Z — 16:08Z)
Bucket 2 signature (no-CUSIP + $1/unit, excluding cash patterns) caught 24 accts / $18.7M —
AQR TA DELPHI PLUS + IRONSIDES + SHAW PARK + INFRA INVEST FEEDER + INFINITY RE. Broader than
brief's 9-acct AQR scope. MCP to base DS recommending broader no-CUSIP-$1/unit cap.

Bucket 3 deep-dive (`cp_ds_abc_bucket3_deep.py`): 64 tight-cohort accts. Account types:
Brokerage 18, IRA 17, Joint 12, RothIRA 5. **Zero Loan/Mortgage/liability types** — brief's
hypothesis fully refuted. Billable: 57 Billable, 7 Non-Billable. Investment strategy:
100% "No Investment Strategy Defined". MV magnitude bands: 9 accts with silver<$1K are
denominator-near-zero artifacts (stale-feed orphan pattern). Base DS accepted analysis and
CLOSED Bucket 3 at 16:08Z.

### 3. Andrew's two inversions (16:10Z — 16:12Z)
Andrew flagged: "how is linear interpolation playing here? rolling forward too-high prices or
bringing in bad prices?" and "these can't be equities — must be mutual funds / alts".

Built `cp_ds_abc_linearinterp_forensic.py`: loaded canonical_prices, per-asset drift vs last
real T1/T2 observation.
- `drift_vs_last_real_price` median = 0.000 across 2,018 overshoot assets
- Zero assets drift 10%+ above last real price
- 1,464 assets are equity_etf_yahoo ($522M), 554 fund_alt_txn_only ($26.6M)
- **Both of Andrew's hypotheses inverted**: prices are correct; overshoot assets ARE Yahoo
  ETFs; `linear_interpolation` label is a historical-resolver artifact, not a drift.

**Reframed root cause: UNITS, not prices.** FIFO holds more units than silver says. Missing
sells, pre-RPS era exit txns not captured, or duplicate buys.

### 4. Base DS GO → Andrew's surgical override (16:12Z — 16:30Z)
Base DS sent GO at 16:12Z with cap=1.00 and original proportional-LOW_CONF cap spec
(per `GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md`).

Andrew in chat pushed back: "anything overvalued post B&C nuke is a prime suspect for
cleaning up prices" — i.e. use silver/unrealized cusip presence to separate confirmed
positions (A) from phantom positions (B) from no-cusip (C); compress only B+C.

Implemented via `cp_ds_abc_compression_attribution.py`:
- Class A (cusip in silver/unrealized): **$61.48M** wrongly compressed under base DS's GO
- Class B (phantom): $62.98M correctly compressed
- Class C (no-cusip): $5.59M correctly compressed

**~half of the $130M original cap was wrongly hitting confirmed-cusip ETFs.** Andrew direct:
"our work is the priority". Proceeded with surgical design.

### 5. Cap design checks (16:32Z — 17:05Z)
Co-mingling check (`cp_ds_abc_comingling_check.py`): 24 PF accts, 12 co-mingle with non-PF
T3. $1.2M of "wasted" non-PF compression under proportional. Andrew ruled: $1.2M / $123M
= 1% is below the noise floor; one-stage surgical is correct.

Downstream MV-invariant-break check: grepped consumers of `gold/timeseries/holdings_lots/`.
C_05, D_00b, D_02, D_03 all read `market_value` directly; none recompute from units × price.
**Safe** — invariant break contained.

Andrew's cash-accounting correction: only `asset_name == 'CASH'` is cash per Opal taxonomy;
MMFs, T-bill ETFs, treasury proxies are noncash. Rewrote cash signature
(`cp_ds_abc_cash_audit_v2.py`). True cash double-count is $0.28M of the $123M overshoot
(negligible). The 2 AQR accts previously flagged as cash-double-count (z0822224971,
z0822409881) are real private-fund overshoots with empty-`asset_name` $1/unit lots.

### 6. Simulations (17:05Z — 17:20Z)
Option A (proportional, agnostic): `cp_ds_abc_cap_simulation_optionA.py`. $130M compressed,
47.3% on A.

Andrew's surgical (B+C, A excluded): `cp_ds_abc_surgical_cap_sim.py`. After a denominator
correction (A NOT in denominator, only B+C), final numbers: $121.2M compressed, $0 on A,
$115.2M from B, $6.1M from C. Gap to silver canonical −3.43% (undershoot side).

Phantom spot-check (`cp_ds_abc_phantom_spotcheck.py`): 99.97% of B-class classifications
are TRUE phantoms. 4 false-phantom edges ($0.11M) — cusip collisions on share classes /
cusip changes / warrants. Below noise.

### 7. Top-residual A-class inspection + BND smoking gun (17:20Z — 17:35Z)
Andrew: "investigate top 3 residual accounts for bad prices".

Built `cp_ds_abc_top3_residual_a_inspection.py`. Three accounts:
- **z0820311441**: 23 BND lots at cost_per_unit $9.45, current_price $73.88 (7-8x ratio)
- **z0812896531 (Staniford)**: 124 short-duration T-bill ETFs, cost_per_unit ~ current price, clean DCA pattern
- **z0822596361**: 209 A-class lots all acquired 2026-04-07/08 (fresh ACAT, silver lag)

Andrew's journal-transfer-out hypothesis for BND: tested in `cp_ds_abc_bnd_staniford_forensic.py`.
Only 3 accts firm-wide hold BND in run11 AND silver/unrealized. No receiving-end
undervaluation. Cluster of 3 accts all show same $9.01-$10.00 cost_per_unit pattern.

Andrew confirmed: "if no records, no receiving account, no Schwab trace, then our process
is right, it's just unnerving."

### 8. Silver transaction reconciliation → BND mispricing root cause (17:35Z — 17:45Z)
Andrew: "bronze is not deduplicated; use silver transactions only."

`cp_ds_abc_silver_txn_reconcile.py` loaded silver/transactions across 1,772 daily files,
filtered to 5 target accounts. Results:

**z0820311441 BND reconciles perfectly**:
- ACAT In 2025-01-15: 8,037.311 units at **$9.45**, market_value $75,952.59
- 22 subsequent buys at $9.50-$9.87 per unit
- FIFO current_units (8,750.99) == txn sum (8,750.99), delta = 0.0000

**CUSIP 921937504** = Vanguard Total Bond Market Index **mutual fund** (Investor Class).
The mutual fund NAV is ~$9-10. BND the ETF has CUSIP `921937804` or `922908744`.
**canonical_prices.parquet has ticker "BND" assigned to cusip 921937504 with ETF's $73.88 price.**

Impact: $1.29M of overshoot attributable to this single mispriced cusip (17% of post-cap
residual). Units are correct; prices are correct in silver transactions; current_price is
wrong because canonical_prices has the wrong ticker-to-cusip mapping.

**Smoking gun found**: the bad-price case my earlier linear-interp drift forensic missed
because drift-vs-last-observed-price was internally consistent at $73.88 — the bug is
upstream of that observation.

### 9. Briefs written (17:45Z — 17:55Z)

(a) `docs/briefs/ds-brief-canonical-prices-shareclass-audit.md` — canonical_prices CUSIP
mispricing audit using BND as example. Detection method: `cost_per_unit / current_price <
0.25` combined with clean txn/FIFO reconciliation.

(b) `docs/briefs/ds-brief-b01-cap-timing-rule.md` — persistence gate + introduction ramp
proposal. Reviewed by Andrew + CTO at 17:44Z. Decisions:
  - APPROVED: `market_value_uncapped` column + per-account cap log line. Required.
  - DROPPED: 5-day ramp (don't publish deliberately wrong values for 5 days to smooth a chart)
  - DROPPED: 3-of-4 persistence gate (chronic cohort passes immediately, adds latency +
    fragility without benefit)

### 10. Cap implementation (17:55Z — 17:58Z)

Rebased local 2 base-DS commits (`178d0cce`, `fd6f362d`) onto `origin/CLOUD` (picked up
~XYZ's `_resolve_unrealized_key(snapshot_date)` from `2a69b97e` + AE's revert `32fbb0d6` +
base DS's `09ac915b` D_03 fix). No conflicts — all edits in different regions.

Edited `B_01.holdings_lots.py`:
- `load_allocations`: added alloc_cash + alloc_noncash columns
- `_apply_silver_noncash_cap(df, allocations, snapshot_date)`: new function, ~150 lines
- Call site: after L2388 (last RPS price override), before L2390 (summary)

Shipped:
- Commit `cb6d78e2`, Author `0.4.0_DS_ClientPlatform~ABC`, --only on B_01 file
- Pushed to `origin/CLOUD`
- `aws s3 cp` to `s3://opal-data-bd/code/gold/B_01.holdings_lots.py`
- `comp-pipescript deployed B_01` -> MATCH

MCP COMPLETE to base DS at 17:58Z.

## Next Steps

- [COO/AE] Coordinate QA runner fire on bd-gold-qa-runner (i-0090b823a4a0997e3) for
  snapshot_date 2026-04-15, --single B_01. Must not collide with ~B's CP-DS1 Run 9.
- [~ABC] On artifact land: run validation (accts moved >5% band -> <5%, firm MV delta to
  silver, market_value_uncapped column present, per-acct log lines present in stdout,
  private-fund accts post-cap <= silver_noncash). MCP validation summary to base DS + CTO.
- [Base DS] Issue follow-up TOs for:
  1. Canonical_prices share-class audit (my brief) — systemic scan + BND spot-fix
  2. Silver/transactions dedup for z0818012711 2026-04-15 duplicate TRANSFER-IN rows
  3. Bronze per-account transaction reconciliation (requires full aggregate history load)
- [CTO] If QA validates, coordinate PROD GO. PROD holds pending ~XYZ's undershoot
  workstream convergence.
- [Remaining staged TOs] ADVI_ROLLUP.SL-P1, BDPL_CNPRCS.WP-10b, COMP_LEARNS.005 — unchanged,
  not unblocked by this session.

## Commit Chain (today, 2026-04-17)

| Commit | Purpose | Stack |
|---|---|---|
| ... | prior session K work (~B lane, d39c4dff at close) | |
| `178d0cce` | base DS: canonical share-class ticker corrections (from my brief's spot-fix) | canonical |
| `fd6f362d` | base DS: B_01 non-unitized $1/unit override + EQT bond ticker cleanup | B_01 |
| `09ac915b` | base DS: D_03 step 6b for non-architect advisors | D_03 |
| **`cb6d78e2`** | **~ABC: surgical B+C unit-count cap — CURRENT HEAD** | **B_01** |

Plus (on `origin/CLOUD` pulled in via rebase): `2a69b97e` (~XYZ stale-key fix),
`c270a9b2` / `32fbb0d6` (AE rolling-key refresh + revert), `372086d6` / various DT docs.

## Compiler Tools

| Tool | When | Result | Notes |
|---|---|---|---|
| `comp-pipescript io B_01` | before diag | no COLUMN GAPS | silver/allocations was already a declared read via load_allocations |
| `comp-pipescript deployed B_01` | pre-edit | STALE (e65e1f65 local vs e266deb1 s3) | ~XYZ uploaded 2a69b97e at 16:57, needed rebase |
| `comp-pipescript io B_01` | after edit | no COLUMN GAPS | clean |
| `comp-pipescript deployed B_01` | post-push + upload | MATCH | 2 MATCH, 0 STALE |
| `comp-blast B_01.holdings_lots` | timing-brief prep | "no downstream consumers" | script-level graph doesn't trace holdings_lots parquet consumers; fell back to grep for manual invariant check |
| `python -m py_compile B_01.holdings_lots.py` | pre-commit | exit 0 | passes |

No `comp-validate B_01` — no gold_validate_config.yaml entry for B_01 holdings_lots;
artifact-level validation is QA runner's --single B_01 outcome.

## Files Modified

| File | Change |
|---|---|
| `data/black_diamond/scripts/gold/B_01.holdings_lots.py` | `load_allocations`: added alloc_cash + alloc_noncash. New `_apply_silver_noncash_cap(df, allocations, snapshot_date)`. Call site post-L2388 before summary. +197/-3 lines. Commit `cb6d78e2`. |

### Diagnostic scripts created (all in `data/black_diamond/scripts/diagnostics/`)

| Script | Purpose |
|---|---|
| `cp_ds_abc_overshoot_diagnosis.py` | Schema probe + first-pass classification |
| `cp_ds_abc_overshoot_pass2.py` | Per-acct dominant price_quality + private-fund pattern scan |
| `cp_ds_abc_bucket3_deep.py` | Liability-type refutation + tight cohort inspection |
| `cp_ds_abc_linearinterp_forensic.py` | canonical_prices per-asset drift vs last real observation |
| `cp_ds_abc_comingling_check.py` | PF T3 vs non-PF T3 overlap in 24 private-fund accts |
| `cp_ds_abc_silver_unrealized_probe.py` | silver/unrealized schema confirm (no units column) |
| `cp_ds_abc_cash_audit.py` / `cp_ds_abc_cash_audit_v2.py` | Cash double-count under broad vs tight (CASH-only) definition |
| `cp_ds_abc_cap_simulation_optionA.py` | Proportional LOW_CONF cap sim — firm-level impact |
| `cp_ds_abc_surgical_cap_sim.py` | Andrew's surgical B+C cap — A excluded from denominator |
| `cp_ds_abc_compression_attribution.py` | Breaks $130M compression by A/B/C class |
| `cp_ds_abc_phantom_spotcheck.py` | 99.97% of B-class classifications are true phantoms |
| `cp_ds_abc_top3_residual_a_inspection.py` | Top 3 accts with residual post-B+C-nuke |
| `cp_ds_abc_bnd_staniford_forensic.py` | Firm-wide BND audit + Staniford lot detail |
| `cp_ds_abc_silver_txn_reconcile.py` | 1,772 silver/transactions files loaded for BND + JAAA + OBIL reconciliation — **BND mispricing root cause found** |

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| Canonical_prices CUSIP/share-class audit (BND example) | `docs/briefs/ds-brief-canonical-prices-shareclass-audit.md` | Base DS → whoever owns canonical_prices / ticker_overrides |
| B_01 cap timing rule (persistence gate + ramp) | `docs/briefs/ds-brief-b01-cap-timing-rule.md` | Base DS → CTO → Andrew (already reviewed, decisions in inbox) |

## MCP / RAVC

Major loops driven to close:
- Base DS overshoot brief → ACK → 2-pass diag → Bucket 3 deep-dive → base DS CLOSED Bucket 3
- Andrew chat: tiered cap design → simulations → BND investigation → brief package → cap implementation
- Base DS GO (16:12Z) + CORRECTION (16:15Z) → Andrew surgical override (chat) → cap implementation
- CTO timing-rule review (17:44Z) → 2 approvals + 2 drops → incorporated into cap patch
- MCP COMPLETE to base DS at 17:58Z with cap SHA + simulation expectations

## Current State (verbatim repeat for grep)

- Commit HEAD: `cb6d78e2`
- S3 MATCH: YES
- Runner: NOT FIRED (awaiting COO + ~B coordination — single-SSM-command discipline)
- Cap mechanism: surgical B+C (A excluded from denominator)
- market_value_uncapped column: preserved for every lot (CTO-approved audit surface)
- Per-account cap log line: emitted for every fired account (CTO-approved)
- Expected post-cap firm total: ~$1,636.5M vs $1,694.6M silver canonical (−3.43% undershoot residual)
- Out-of-scope TOs queued: canonical_prices share-class audit, silver/transactions dedup, bronze txn reconciliation

## Do NOT

- Do NOT revert the A-class protection (cusip in silver/unrealized). $61.48M of confirmed-
  cusip ETFs (BIL, VTI, VOO, FXAIX, JEPI, IEFA, JAAA, etc.) would be wrongly compressed.
  This was the central Andrew-chat design decision and validated by the compression-
  attribution diagnostic.
- Do NOT re-introduce the ramp or persistence gate without explicit CTO override — Andrew
  rejected "publishing deliberately wrong values for 5 days to smooth a chart" at 17:44Z.
- Do NOT assume silver/unrealized has unit counts — it does NOT. Only cusip presence. Any
  future per-position units capping requires bronze/unrealized XLSX ingestion upstream
  (AE-side prerequisite).
- Do NOT fire the QA runner without COO coordination — single-SSM-command discipline, and
  CP-DS1 Run 9 (~B) is also pending.
- Do NOT re-count CASH lots against silver.noncash — cash lots pass through the cap
  untouched per Andrew's "only CASH_USD is cash" rule. MMFs / T-bill proxies stay noncash
  on both sides of the comparison.
- Do NOT compress dryrun (`holdings_lots_v2_dryrun`) or shadow (`holdings_lots_shadow`)
  artifacts — they are pre-cap reference. The cap runs on PROD stack only.
