# C_00 -- canonical_performance -- DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/C_00.canonical_performance.py`
**Output:** `gold/canonical/performance/{date}.parquet`
**Layer / order:** Group C (performance), order 200; catalog line 89. Reads account_gains (B_03, full prefix), accounts_dimension (A_00).
**Essential status (Andrew's framework):** ESSENTIAL -- AGNOSTIC-core. `canonical_performance` -> C_02 (client_performance) -> the served performance/growth surfaces -> ADVI/MDPF. The relationship-level performance attribution layer.
**Author/project:** 0.4.0_DS_ClientPlatform / ADVI_GLDOPS.
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-25 (Andrew-direct A1 layer-walk, C-tier). Source-grounded (file:line) + io-grounded.

---

## 1. What it does

Aggregates B_03's per-account daily decomposition up to **relationship level**, with **cumulative running sums** per component (price_return, realized_gl, income, Growth, NNA). Same identity as B_03 (`dAUA = Growth + NNA`), rolled to the household.

The cumulatives reflect the relationship's **CURRENT composition** on each date (docstring L10-19): when accounts move between relationships (advisor reassignment / household restructuring), cumulatives show a deliberate discontinuity -- R1 drops the departed account's contributions, R2 gains them. This is correct-by-design: the cumulative answers "how did this relationship's CURRENT accounts get to this AUA?", not "the historical total including accounts that left." (A subtle but important semantic -- a consumer must not read the cumulative as a stable historical series across reassignments.)

## 2. Architecture / data flow
- READS: `canonical/account_gains/` (B_03, the FULL prefix -- all dates), accounts_dimension (A_00, for the relationship mapping).
- COMPUTES: group account_gains by relationship per date; cumulative running sums over the date axis per relationship (current-composition basis).
- WRITES: `canonical/performance/{date}` -> C_02.

## 3. Recompute posture -- FULL (cumulative requires full history); lightweight arithmetic
- **Catalog = `C_00|...|--upload`** (line 89) -- no `--incremental`, no watermark in the io manifest. Because the **cumulative running sums require the entire account_gains history**, C_00 reads the FULL `account_gains` prefix and recomputes cumulatives each run -- a full-recompute by necessity of the cumulative semantics (you cannot incrementally append a cumulative when a back-dated account_gains row or a reassignment reshuffles prior cumulatives).
- BUT it is **lightweight**: pandas groupby + cumsum over the account_gains partitions (C-backed vectorized arithmetic), not a stateful per-row reconstruction. The cost is the full READ of account_gains, not CPU.
- Optimization note (A2): if account_gains grows large, the full-read could be windowed for the non-cumulative columns, but the cumulatives genuinely need full history -- so this is a "read cost", not an algorithmic-CPU cost. Lower priority than A_04's full-scan (which read all of silver/transactions for a 90-day flag -- a true waste; C_00's full-read is load-bearing for the cumulative).

## 4. Rust-candidate assessment (Andrew's refactor question -- grounded here)
C_00 is **pandas aggregation arithmetic** (groupby + cumsum), C-backed -- NOT a stateful hot loop. It is NOT a Rust candidate (the hot path already runs in pandas/numpy C kernels; Python overhead is thin). Consistent with the A+B-tier finding: the ONLY genuinely CPU-bound, stateful, hard-to-vectorize kernel in the whole bd analytics flow is **B_01's FIFO lot reconstruction** -- and that is slated for deletion (custodian-direct lot re-sourcing, see the B_02 brief). The C-tier performance chain is decomposition/aggregation arithmetic, not heavy time-weighted Dietz with geometric sub-period linking. So a Rust rewrite has NO durable home in this flow: incrementalize the read-cost offenders + re-source the FIFO, and there is no irreducible compute kernel left to optimize.

## 5. Tech debt / smells
- **Cumulative-discontinuity-on-reassignment** is correct-by-design but a documentation/consumer-contract risk: a downstream chart reading the cumulative as a continuous historical series would misread the reassignment discontinuity as a real drop/jump. Ensure the consumer (C_02 -> portal) treats it as current-composition. Note for A2 (a semantic-contract item, not a bug).
- Full-read of account_gains each run (recompute posture above) -- load-bearing, low-priority.

## 6. What's GOOD (keep)
- **Vectorized aggregation** (no per-row loops); the cumulative-on-current-composition semantics are deliberate + documented.
- **Clean layering** -- C_00 only aggregates B_03's already-decomposed gains; no source wrangling.

## 7. Status / ledger row
- **Tag: ESSENTIAL / AGNOSTIC-core** (relationship perf attribution; feeds C_02 -> served performance).
- **Recompute: FULL (cumulative-necessitated) but LIGHTWEIGHT** (pandas aggregation, not CPU-bound; the cost is the account_gains full-read, which is load-bearing for the cumulative -- not a waste like A_04's).
- **Rust: NOT a candidate** (aggregation arithmetic; the only CPU-heavy kernel in the flow is B_01 FIFO, which is slated for re-sourcing).

### Ledger entry (C-tier)
| Script | Output | Consumers | Tag | Recompute | Notes |
|---|---|---|---|---|---|
| C_00.canonical_performance | gold/canonical/performance/{date} | C_02 | ESSENTIAL / AGNOSTIC-core | FULL (cumulative-necessitated) but lightweight pandas-aggregation | relationship-level Growth/NNA cumulative attribution; cumulative=current-composition (discontinuity-on-reassignment by design -- consumer-contract note); NOT a Rust candidate |
