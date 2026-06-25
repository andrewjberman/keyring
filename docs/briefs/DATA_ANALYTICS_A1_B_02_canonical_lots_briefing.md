# B_02 -- canonical_lots -- DATA_ANALYTICS layer briefing

**Script:** `data/black_diamond/scripts/gold/B_02.canonical_lots.py`
**Outputs:** `gold/canonical/lots_unrealized/{date}.parquet`, `gold/canonical/lots_realized/{date}.parquet` (+ `gold/meta/canonical_lots_incr_watermark.json`, + `gold/_parity/canonical_lots/{*}/scorecard.json`)
**Layer / order:** Group B (canonical), order 102; catalog line 87. Reads canonical_holdings (B_00, gating), BD lots (silver/unrealized + silver/realized), Schwab lots (schwab/silver/uln + schwab/silver/rld), prices (S_00), account mapping, accounts_dimension (A_00).
**Essential status (Andrew's framework):** ESSENTIAL -- AGNOSTIC-core. Feeds B_03 (account_gains) -> C/D -> ADVI/MDPF tax/gains surfaces. The per-lot capital-gains canonical (short/long-term, cost basis, accrued gain) -- every firm with taxable accounts.
**Author/project:** 0.4.0_DS_ClientPlatform / ADVI_GLDOPS.
**Briefing by:** 0.4.0_DS_ClientPlatform, 2026-06-25 (Andrew-direct A1 layer-walk, B-tier). Source-grounded (file:line).

---

## 1. What it does -- and what it is NOT

B_02 produces the two **canonical lot tables** -- `lots_unrealized` (open tax lots per date; grain `(date, account_id, asset_name, acquired_date, lot_index)`) and `lots_realized` (closed lots per date) -- with per-lot capital-gains fields for downstream tax intel. It is **gated by canonical_holdings** (B_00): lots AUA must tie back to canonical holdings AUA (docstring L24).

**Crucially, B_02 is a CANONICALIZER, not a FIFO reconstructor.** It READS already-built lot tables from two feeds and merges/dedups them into the canonical shape:
- BD lots: `silver/unrealized/unrealized_gain_loss.parquet` (open) + `silver/realized/bd_realized_compact.parquet` (closed).
- Schwab lots: `schwab/silver/uln/{date}` (unrealized) + `schwab/silver/rld/{date}` (realized) -- **the custodian's own lot tables, direct.**

The actual FIFO lot RECONSTRUCTION (from `silver/transactions/`) happens upstream in **B_01 (holdings_lots)** -- that is the stateful per-position FIFO kernel; B_02 just canonicalizes the resulting (and the custodian-provided) lots.

## 2. The clean-rebuild relevance (chunk-1 "lots-FIFO redundant" -- grounded here)

B_02 is where the **custodian-direct lot path already exists**: it reads Schwab's ULN/RLD lot tables alongside BD's reconstructed lots. This is the concrete grounding for the reverse-ETL/chunk-1 finding ("lots-FIFO = redundant vendor-IP, re-sourceable from Schwab-direct"): for the Schwab (49F) book, the lots are **already available custodian-direct (ULN/RLD)** -- B_01's FIFO reconstruction is the redundant path. The clean-rebuild's "re-source lots from the custodian, retire the FIFO reconstruction" is partially realized in B_02 today; A2/A3 generalizes it (drop the B_01 FIFO dependency for custodian-covered books, keep it only where no custodian lot feed exists).

## 3. Recompute posture -- WATERMARK-incremental + parity-gated (HEALTHY)

- **Catalog = `B_02|...|--upload`** (line 87) -- no `--incremental` flag (gated to INCREMENTAL_CAPABLE only), BUT B_02 carries its OWN incremental mechanism: `CANONICAL_LOTS_INCR_WATERMARK` (`gold/meta/canonical_lots_incr_watermark.json`, written L852/L1004/L1139) + `--start-date`. So it processes new/changed dates against the watermark rather than rebuilding all history. Healthy (same class as B_00's watermark model, distinct from A_01/A_02's SCD-incremental).
- **Parity-scorecard gated:** writes `gold/_parity/canonical_lots/{*}/scorecard.json` -- a built-in parity check (the lots-vs-holdings AUA tie). Good control.

## 4. Compiler-tool FINDING (gap to log)

`comp-pipescript io B_02` reports B_02 **WRITES** `canonical_holdings_key -> B_00/B_03/C_02/D_04`. This is a **FALSE POSITIVE** -- the tool's own ROLLING-WINDOW warning fired on it. Verified at source: `canonical_holdings_key(date_str)` at L202 is a **READ** (`key = canonical_holdings_key(date_str)` then `get_object`); B_02's only `put_object` writes are the lots tables (L622-629), the watermark (L852/1004/1139), and the parity scorecard. The io tool's alias-collision (matching the `canonical_holdings_key` function name to an unrelated `Key=key` write) over-attributes a canonical_holdings write to B_02. Logged as a comp-pipescript io alias-collision gap (the rolling-window heuristic needs read-vs-write disambiguation on FUNC-keys).

## 5. Tech debt / smells
- **CUSIP bridge re-built locally** (`build_cusip_bridge`, L149) -- same bridge logic as B_00; two scripts independently build a CUSIP->asset_name map from silver/unrealized+realized. Candidate to factor into a shared lib (A2 dedup; low-risk).
- 14 READS (io manifest) -- a wide input surface (BD lots + Schwab lots + prices + mapping + holdings + parity + watermark). Reasonable for a canonicalizer that must reconcile two lot feeds, but worth noting as the heaviest-fan-in Group-B node.

## 6. What's GOOD (keep)
- **Dual-feed canonicalization with a parity scorecard** -- merges BD + Schwab-direct lots and self-checks the AUA tie. This is the right shape and it ALREADY embodies the custodian-direct lot sourcing the clean-rebuild wants.
- **Watermark-incremental** -- no full-history rebuild.
- Outputs structured for tax intel (short/long term, cost basis, accrued gain) -- the decision-useful grain.

## 7. Actions
| When | Action | Owner |
|---|---|---|
| A2 | Factor the duplicated CUSIP bridge (B_00 + B_02) into a shared lib | DS |
| A2/A3 | Use B_02's existing Schwab ULN/RLD read as the template for the custodian-direct lot re-sourcing that retires B_01's FIFO reconstruction for custodian-covered books | DS / CTO arch-gate |
| now | Log the comp-pipescript io canonical_holdings write false-positive (alias collision) | DS (this brief + comp-tools-log) |
| -- | Recompute: NO action -- watermark-incremental + parity-gated | -- |

## 8. Status / ledger row
- **Tag: ESSENTIAL / AGNOSTIC-core** (per-lot gains canonical; feeds B_03 -> C/D -> portal tax surfaces).
- **Recompute: HEALTHY** (watermark-incremental + parity scorecard).
- **Key fact: it is the lot CANONICALIZER (reads BD + Schwab-direct lots), NOT the FIFO reconstructor (B_01 is)** -- and it already houses the custodian-direct lot path central to the clean-rebuild.

### Ledger entry (supersedes the v0.1 INFERRED B_02 row)
| Script | Output | Consumers | Tag | Recompute | Notes |
|---|---|---|---|---|---|
| B_02.canonical_lots | gold/canonical/lots_{unrealized,realized}/{date} (+watermark, +parity) | B_03 | ESSENTIAL / AGNOSTIC-core | watermark-incremental + parity-gated (HEALTHY) | lot CANONICALIZER (BD silver lots + Schwab ULN/RLD direct), NOT FIFO reconstructor (=B_01); houses the custodian-direct lot path (chunk-1 re-source target); io canonical_holdings-write = alias false-positive |
