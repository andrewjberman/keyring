# COT Snapshot-First Restructure — Proposal

**Author:** 0.4.0_DS_ClientPlatform | **Date:** 2026-06-12 | **Status:** PROPOSAL (Andrew-direct, routed COO + CTO, CC CVO)
**Driver:** Andrew-direct 2026-06-12 ~20:10Z: cot has data only back to 2026-04-22; every holdings value and
accounts value is available directly from the daily Snapshot pull — so the bd-style transaction
reverse-engineering is unnecessary for Cottonwood. "Cottonwood should be very light and easy to work with."
**Scope guard:** cot scripts are entirely forked from 49 Financial / bd-pipeline. **Every change in this
proposal is `data/cot/**` only — zero edits to bd-pipeline or bd-gold.**

---

## 1. What we actually pull from BD for Cottonwood (surveyed live)

Five BD DataMining tables, pulled by `cot_bronze_ingest.py` on cot-exporter (templates are S3 config,
persisted-templateId taps; `s3://opal-data-cot/code/bronze/templates/`):

| Table | qt | Mode | Columns (key) | Landing since | Silver-merged? |
|---|---|---|---|---|---|
| transactions | 2 | Custom, 14d rolling | 68 cols: TransactionID, Action, Type/SubType, External Flow, Price, Trade/Settle/Entry Date, account+relationship dims, tax status | 2026-04-22 (backfilled) | YES (`silver/transactions/`) |
| allocations | 5 | CurrentDay snapshot | 47 cols: Team/Relationship/Portfolio/Account dims, fee schedule, custodian, rep, billing config | 2026-04-22 (backfilled) | YES (`silver/allocations/`) |
| **holdings** | 1 | CurrentDay snapshot | account x asset x **Units x Market Value** + asset attributes (Andrew-built "Assets_Dim" templateId 226355) | **2026-06-09** | partial (one-off merges 06-08/06-09; NOT in `cot_silver_merge.py` TABLE_CONFIG) |
| unrealized | 4 | CurrentDay snapshot | per-lot: **Open Date, Units, Cost Basis, Market Value, ST/LT/Total G/L**, CUSIP/Ticker, account+relationship | template fixed 9abd0181b (06-12), validates tonight | NO |
| realized | 3 | Custom, 14d | per-disposal: Open/Trade Date, Units, Cost Basis, **Proceeds, ST/LT/Total G/L** | same | NO |

Two facts make snapshot-first decisive:

1. **The holdings qt1 snapshot is already the certified truth.** Its own template comment: reconciles to
   allocations certified AUA ($373.2M vs $372.9M, 0.1%) across 680 accounts and **captures transferred-in
   positions that positions-FIFO misses**. The snapshot is not merely sufficient — it is *more correct*
   than the FIFO reconstruction (transfers-in have no purchase transactions to replay).
2. **The qt4 unrealized snapshot is a per-lot table** (open date, units, cost basis, MV, ST/LT G/L per
   account per asset per day). That is exactly what bd's `B_01.holdings_lots.py` spends a full-history
   FIFO replay reconstructing — BD just *gives* it to Cottonwood daily.

## 2. What the forked gold tree does today (43-script census)

Full census run 2026-06-12 (chain defs from `gold_dispatch.sh`). Mechanism classes:

| Class | Count | Scripts |
|---|---|---|
| TXN-RECONSTRUCT (the bd reverse-engineering core) | 3 | `A_03.positions_cube` (FIFO over full txn history, ~1,764 silver files), `B_01.holdings_lots` (FIFO lot replay + tax classification), `S_00 build_canonical_prices_v2` T1 tier (txn-median prices) |
| SNAPSHOT-NATIVE / dimensions | 11 | A_00, A_01, A_02, A_04, B_00 (partially), B_02 (partially), C_02, C_03, C_05, C_07, C_04 |
| DERIVED-METRIC (mechanism-agnostic arithmetic) | 14 | B_03 gains ledger, C_00 performance, C_01 NNA, C_01b/c, C_06 mix, C_08 fees, E_24 |
| PORTAL-EMIT | 7 | D_00, D_00b, D_00c, D_01, D_02, D_03, D_04 (platinum) |
| DIAG/VALIDATE | 9 | E_00, E_01, E_18, E_20–E_23, diag_gold_silver_recon, validate_* |

**Dead/unadapted fork machinery found (cot has NO `schwab/` data in opal-data-cot — verified live):**
- Schwab RPS merge in `B_00.canonical_holdings` ("reconciled/bd/schwab/schwab_override" source labels)
- Schwab ULN/RLD enrichment in `B_02.canonical_lots`
- Schwab refs in `A_03`, `B_01`, `C_01`, `lib/schwab_flows.py`, `lib/s3_layout.py`
- `'49F House'` advisor placeholder in `C_07`; `bd-securities` DynamoDB table name in B_01b/E_18
- Orphan `B_00.hybrid_price_fill.py` precondition key in `gold_pipeline_deps.yaml` (cot's B_00 is
  canonical_holdings; no hybrid_price_fill exists in cot) — flagged in DEBTSCAN D2X, deferred to here
- (Already fixed 2026-06-12, 319a716cb: the 49F-only `inject_scoped_overrides` enforced auto-chain)

The bd fork carried in a holdings-derivation pipeline shaped by 49F's constraints (deep history, corrupted
transactions, dual custodian feeds) that Cottonwood does not have.

## 3. Proposed architecture: snapshot-first

**Principle: per-day state comes FROM the snapshot pull; transactions are used ONLY for flow
classification (NNA), never for state reconstruction.**

```
BRONZE (unchanged pulls)          SILVER (extend merge)              GOLD (restructured)
transactions  qt2  14d   ──────►  silver/transactions/{d}  ───────►  flows ONLY (C_01 NNA)
allocations   qt5  daily ──────►  silver/allocations/{d}   ──┐
holdings      qt1  daily ──────►  silver/holdings/{d}      ──┼────►  SNAP_00 daily state assembler
unrealized    qt4  daily ──────►  silver/unrealized/{d}    ──┤        ├─ gold/canonical/holdings/{d}
realized      qt3  14d   ──────►  silver/realized/{d}      ──┘        ├─ gold/canonical/lots_unrealized/{d}
                                                                      ├─ gold/canonical/lots_realized/{d}
                                                                      └─ gold/prices/daily_reference/{d}  (MV/units)
                                                                              │
                                              B_03 gains ledger ◄─────────────┘  (unchanged arithmetic)
                                              C_00..C_08, D_00..D_04, E_*       (unchanged, inputs re-pointed)
```

### 3a. New: `SNAP_00.daily_state.py` (one assembler replaces the reconstruction stack)
- Reads the four daily snapshot tables; applies `lib/exclusions.py` (ghost accounts / nna exclusions —
  the existing, working cot mechanism); writes the same canonical artifact shapes the downstream already
  consumes (`gold/canonical/holdings/{date}`, `lots_unrealized/{date}`, `lots_realized/{date}`).
- Emits a thin per-asset daily price reference as `price = Market Value / Units` from the holdings
  snapshot (what B_03's price_return decomposition needs), with yfinance fallback only for gap days.
- Validation built in: holdings-snapshot AUA vs allocations certified AUA per day (the 0.1% reconciliation
  that the template comment already demonstrates) — fail loud above threshold.

### 3b. Retired (cot only; bd untouched)
| Retire | Replaced by | Why safe |
|---|---|---|
| `A_03.positions_cube.py` (FIFO, heaviest script in the chain) | holdings snapshot | snapshot captures transferred-in positions FIFO misses; certified-AUA reconciled |
| `B_01.holdings_lots.py` (FIFO lot replay) | qt4 unrealized per-lot snapshot | BD provides open date / units / cost basis / ST-LT per lot directly |
| `S_00 build_canonical_prices_v2.py` (4-tier reconstruction) | MV/units price reference + yfinance fallback | prices only needed for B_03 day-over-day decomposition + mix views; snapshot carries MV directly |
| Schwab merge paths in B_00/B_02 + `lib/schwab_flows.py` | (nothing — no Schwab data exists for cot) | dead code; reads prefixes that do not exist in opal-data-cot |
| `B_00`/`B_02` as separate scripts | folded into SNAP_00 | they become trivial snapshot passthroughs once FIFO + Schwab legs are gone |

### 3c. Kept as-is (inputs re-pointed where needed)
- **B_03 gains ledger** — pure arithmetic over holdings(t-1,t) + lots + transactions(t); shape preserved.
  The B_03→C_00 AUAGAP guard added 2026-06-12 stays.
- **C_00–C_08** (performance, NNA, tax, mix, attribution, fees) — mechanism-agnostic; C_06 re-points from
  positions_cube to canonical holdings.
- **All D_* portal publishers + platinum** — untouched (read downstream aggregates only).
- **A_00–A_02, A_04 dimensions** — kept; already allocations-snapshot-driven.
- **Diagnostics**: E_20/E_21/E_22/E_23, diag_gold_silver_recon kept; **E_00/E_01 (AUA-gap decomposition /
  quality tiers) retire or reframe** — they exist to measure the FIFO-vs-allocations gap, which
  snapshot-first eliminates by construction.

### 3d. Config/cleanup (rides along)
- `cot_silver_merge.py` TABLE_CONFIG: add holdings / unrealized / realized (today it handles only
  transactions + allocations; holdings silver files were one-off merges).
- `gold_pipeline_deps.yaml`: remove orphan `B_00.hybrid_price_fill.py` precondition (D2X residual);
  re-key preconditions to SNAP_00 inputs (silver/holdings/{d} freshness gate).
- `gold_dispatch.sh`: collapse PHASE_A/B serialization built for FIFO memory pressure (B_00→B_01
  4.6x-slowdown workaround becomes moot); chain shortens by the 3 heaviest scripts.
- Rename bd-isms: `'49F House'` → `'House'`; decide `bd-securities` DynamoDB table (shared estate-wide
  enrichment — keep shared, or fork `cot-securities`; recommend keep-shared, it is firm-agnostic security
  classification, flag to CTO).
- Commit the in-flight `templates/holdings.json` working-tree delta (startDate/endDate fields).

## 4. The one open design question: 2026-04-22 → 2026-06-08 holdings history

Holdings qt1 only started landing 2026-06-09; transactions/allocations go back to 04-22. Three options
for the ~7-week pre-snapshot window:

| Option | Mechanism | Trade-off |
|---|---|---|
| **A (recommended): probe BD for as-of holdings** | qt1/qt4 with Custom + asOfDate via `cot_backfill_date_probe.py` (the existing probe harness; prior probes established the MM/DD/YYYY + asOfDate requirements) | If BD serves historical snapshots, the entire window is pulled in one backfill batch and the FIFO machinery is never needed at all |
| B: one-time FIFO bridge | run the existing A_03/B_01 once for 04-22→06-08, freeze outputs, then retire | Uses the machinery being retired exactly once; known transferred-in blind spot for that window |
| C: accept the 06-09 floor | account-level values back to 04-22 from allocations; broken-out holdings start 06-09 | Simplest; loses ~7 weeks of position-level history that may never be queried |

Recommend A-then-C: probe first (cheap, existing harness); if BD can't serve as-of holdings, take C unless
a consumer actually needs position-level pre-06-09 history (none identified today — portal timeseries are
account/AUA-level for that window).

## 5. Sequencing (each phase independently shippable, nightly-validated per cost discipline)

| Phase | Work | Gate |
|---|---|---|
| P0 | Silver merge TABLE_CONFIG + qt3/qt4 landing validation (tonight's scheduled run) + commit holdings.json delta | qt3/qt4 xlsx land + silver-merge clean |
| P1 | SNAP_00 assembler, dual-run SHADOW vs current B_00/B_02 outputs (gldinc_p1_shadow pattern); daily AUA reconciliation report | N consecutive nightly shadow-matches within threshold (CTO sets N) |
| P2 | Cut over canonical/{holdings,lots_*} to SNAP_00; re-point B_03/C_06; retire A_03/B_01/S_00 + Schwab legs (path-anchored removal, DTAFLP orphan-sweep discipline) | never-widen: served-output movement needs CTO+COO sign-off; shadow evidence carries |
| P3 | Dispatch/deps/diagnostics cleanup (3d) + backfill decision (4) | comp-pipescript deployed all-MATCH; 0-residual sweep incl. split-component grep |

**Cost note:** all validation on scheduled nightlies (no ad-hoc gold runs). Chain gets lighter, not
heavier: drops full-history FIFO replay (A_03's ~1,764-file scan) and the B-group serialization workaround.

## 6. Risks / explicit non-goals

- **BD ~14d restatement window:** a CurrentDay snapshot captures BD's view that day and is never
  re-captured. Transactions/realized keep the 14d rolling lookback for flow restatements; holdings
  restatements for already-captured days are accepted as-is (same posture the snapshot pull already has
  today). If this matters later, a t-1..t-3 re-pull variant is a small bronze change.
- **Lot fidelity:** qt4 is BD's lot view (covers transferred-in lots with custodian cost basis — better
  than FIFO inference). We inherit BD's lot accounting rather than re-deriving it; that is the point.
- **NON-GOAL: zero bd-pipeline/bd-gold changes.** bd keeps its FIFO machinery — 49F genuinely needs it
  (deep pre-pull history + corrupted transaction history). This proposal is cot-tree-only.
- **NON-GOAL: no portal-contract changes.** D_*/platinum artifact shapes are preserved; the portal does
  not know or care how canonical holdings were produced.

---
*Survey evidence: bronze templates + S3 listings (opal-data-cot forwardfill_v2/, silver/), 43-script gold
census 2026-06-12, gold_dispatch.sh chain defs, lib/ audit. Predecessors: DEBTSCAN D2X ledger
(`org/modules/graph/debtscan/2026-06-12_D2X_composition_ds_infcotmdpf.md`), 319a716cb inject removal.*
