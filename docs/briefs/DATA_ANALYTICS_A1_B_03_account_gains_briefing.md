# B_03 -- account_gains -- DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/B_03.account_gains.py`
**Output:** `gold/canonical/account_gains/{date}.parquet` (+ `gold/meta/account_gains_incr_watermark.json`, + `gold/_parity/account_gains/{*}/scorecard.json`)
**Layer / order:** Group B (canonical), order 103; catalog line 88. Reads canonical_holdings t/t-1 (B_00), canonical lots_realized/unrealized (B_02, optional), silver/transactions (income).
**Essential status (Andrew's framework):** ESSENTIAL -- AGNOSTIC-core. `account_gains` -> C_00, C_01, C_02 (the performance/NNA/client-perf chain) -> served AUA/NNA -> ADVI/MDPF. The per-account daily AUA-decomposition ledger -- the arithmetic backbone of the served growth/flows numbers.
**Author/project:** 0.4.0_DS_ClientPlatform / ADVI_GLDOPS.
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-25 (Andrew-direct A1 layer-walk, B-tier). Source-grounded (file:line) + io-grounded.

---

## 1. What it does

The **per-account daily capital-gains ledger** -- decomposes each account's daily AUA change into its drivers:
```
AUA(t) - AUA(t-1) = Growth(t) + NNA(t)
Growth = price_return + realized_gl + income
NNA    = aua_change - growth        (residual)
```
One row per account per date. This is the arithmetic that separates **market growth** from **net new assets (flows)** -- the foundation of every served growth/NNA/performance surface.

**It is PURE ARITHMETIC on canonical outputs** (docstring L9-12): no S3 source joins, no Schwab reconciliation, no CUSIP bridges, no account mapping -- all of that happened upstream in B_00 (canonical_holdings) and B_02 (canonical_lots). B_03 just reads the canonical layer and does the AUA-decomposition math.

## 2. Architecture / data flow
- READS: `canonical/holdings/{t-1}` + `{t}` (B_00, the AUA endpoints), `canonical/lots_realized/{t}` + `lots_unrealized/{t}` (B_02, for realized_gl -- optional), `silver/transactions/{t}` (dividend/interest income).
- COMPUTES: price_return + realized_gl + income = Growth; NNA = aua_change - Growth (residual).
- WRITES: `canonical/account_gains/{date}` -> C_00, C_01, C_02; + the incremental watermark + a parity scorecard.

## 3. Recompute posture -- WATERMARK-incremental + parity-gated (HEALTHY)
- **Catalog = `B_03|...|--upload`** (line 88) -- no `--incremental` flag (gated to INCREMENTAL_CAPABLE), but B_03 carries its own `ACCOUNT_GAINS_INCR_WATERMARK` + `--start-date` -> watermark-incremental (same healthy model as B_00/B_02; processes new/changed dates, not full history).
- **Parity-scorecard gated** (`gold/_parity/account_gains/`) -- the decomposition self-checks (the Growth+NNA = aua_change identity is itself a built-in invariant; a non-zero residual misclassification would surface).
- Lightweight: pure arithmetic on already-canonical inputs (no heavy reconstruction) -- cheap per date.

## 4. Tech debt / smells
- **NNA-as-residual** (`NNA = aua_change - growth`): correct by construction, but it means ANY upstream error in Growth (a mispriced position, a missed income txn, a lot-realized gap) silently lands in NNA (the residual absorbs all unexplained AUA change). This is the standard decomposition risk -- NNA quality is only as good as Growth completeness. The parity scorecard mitigates (it can flag implausible NNA), but NNA outliers should always be traced to a Growth gap first, not assumed real flows. (This is the mechanism behind the historical NNA-variance investigations -- ADVI_NNAVAR.) Note for the A1 ledger: NNA is a DERIVED residual, not an independent measurement.
- Income from `silver/transactions/{t}` only (current-day) -- a back-dated income correction in a later transactions file would not retro-adjust a prior account_gains row unless that date is reprocessed (the watermark/restatement window governs this).

## 5. What's GOOD (keep)
- **Clean separation of concerns** -- B_03 does ZERO source wrangling (all upstream in B_00/B_02); it is purely the decomposition arithmetic. This is exactly the right layering (the reconciliation/bridging complexity is isolated upstream; the AUA-math is a thin, auditable layer).
- **Identity-based + parity-gated** -- the Growth+NNA=aua_change identity is self-checking.
- **Watermark-incremental** -- no full-history rebuild.

## 6. Actions
| When | Action | Owner |
|---|---|---|
| -- | Recompute: NO action -- watermark-incremental + parity-gated + lightweight | -- |
| (doctrine) | Carry the "NNA = residual, quality-bounded-by-Growth-completeness" note into A2 so the rebuild treats NNA as derived (trace outliers to Growth gaps, the ADVI_NNAVAR lesson) | DS / A2 |
| -- | Essential tag: KEEP -- the AUA-decomposition feeding C_00/C_01/C_02 -> served growth/NNA | -- |

## 7. Status / ledger row
- **Tag: ESSENTIAL / AGNOSTIC-core** (per-account AUA decomposition; feeds C_00/C_01/C_02 -> served growth/NNA -> portal).
- **Recompute: HEALTHY** (watermark-incremental + parity-gated; lightweight pure-arithmetic).
- **Cleanliness: GOOD** -- the cleanest B-tier layer (zero source wrangling; pure decomposition math). Only doctrinal note = NNA-as-residual is Growth-completeness-bounded.

### Ledger entry (B-tier, census-done)
| Script | Output | Consumers | Tag | Recompute | Notes |
|---|---|---|---|---|---|
| B_03.account_gains | gold/canonical/account_gains/{date} (+watermark, +parity) | C_00, C_01, C_02 | ESSENTIAL / AGNOSTIC-core | watermark-incremental + parity-gated (HEALTHY) | pure AUA-decomposition arithmetic (Growth+NNA=dAUA) on canonical inputs; NNA=residual (Growth-completeness-bounded, the NNAVAR doctrine); cleanest B-tier layer |
