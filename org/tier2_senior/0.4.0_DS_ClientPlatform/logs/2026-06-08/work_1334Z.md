# 0.4.0_DS_ClientPlatform — work_1334Z (GLDINC P2 A_03 reconcile-correctness design draft)

**archetype:** IMPLEMENT (design) + TRACE

## Task (COO 133150Z RAVC2-ACCEPT + forward)

Pre-stage the P2 A_03 reconcile-correctness design parallel to AE's P0 validation (different scripts,
parallelizable). Cover: injection-date re-FIFO, per-(account,asset) invalidation, the one-time
state-seed (§4 FLAG 3), and how refinement #5's checksum detector wires into A_03's canonical_prices
read. No prod touch, C1. RAVC2 the draft when ready.

## Method — read A_03 source end-to-end (1764 lines), grounded the design in actual mechanics

Did NOT design abstractly. Traced A_03.positions_cube.py fully. Key findings that SHAPED the design:
- A_03 is the **units cube** (date,account,asset,units), not cost-basis lots → reconcile is cum-unit
  prefix-sum correctness + a date-anchored injection layer (NOT FIFO-lot reconcile).
- `expand_pairs_to_daily()` materializes the whole ~300M-row pair×day cross-product = the 76 GB floor
  (the P2 prize). The incremental store can BE the prior-day open-position set carried forward.
- Injection events are stamped at **2024-04-30** (RPS/sell) or unrealized open_date (buy); the buy
  back-solve uses canonical_prices **latest-price-per-asset** only (L679).
- `gold/synthetic_positions_index` ALREADY persists injection events → a ready seed primitive.
- **`build_single_date()` OMITS the injection layer** (raw txn snapshot, not injection-consistent with
  full) → the incremental day-builder CANNOT reuse it as-is. Surfaced as risk #1 for AE.

## Deliverable
`docs/briefs/gldinc-p2-a03-reconcile-correctness-design-20260608.md` (draft). Sections: A_03 scoping;
incremental carry-forward state model + the 4 seed artifacts; normal-day dirty-set; the **3 reconcile
triggers** (4.1 txn-partition LastModified §5a primitive; 4.2 injection-snapshot change incl the
2024-04-30 re-FIFO = the §4a scoped-carve-out parity target; 4.3 canonical_prices refinement-#5 wiring
with the A_03-specific latest-price-per-asset narrowing) + invalidation scope [trigger_date, today] for
affected pairs only; §4b scorecard hooks; 4 open constraints for AE at kickoff.

## Sharpest design calls
1. **canonical_prices/refinement-#5 wiring, A_03-narrowed:** A_03's injected units change iff the LATEST
   price of an injection-target asset moved (a strictly-historical price restatement doesn't change A_03
   output — but the full per-date manifest is still emitted for Stage-3 valuation). Trigger =
   changed_assets ∩ injection_target_assets with a moved latest-price row.
2. **Reassignment + freeze-baseline cascades are NOT A_03** (keys are (account,asset), reassignment-
   invariant; no frozen period) → explicitly out-of-scope so P2 isn't over-engineered. A_03's only
   cascade is the prefix-sum-forward one.
3. **State-seed = one full pass** emitting cum_units@wm + account_end_dates@wm + (existing) synthetic
   index + watermark-with-per-input-checksums; gated complete before parity accrual.

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| Read (A_03 full) | A_03.positions_cube.py 1-1764 | full mechanics: cum_units, expand, 3 injection sources, build_single_date injection-gap |
| (design trace) | reconcile triggers vs A_03 inputs | 3 trigger classes scoped; 2024-04-30 = §4a carve target; refinement #5 wired |
| comp-pipescript io | N/A (design-only, no prod touch C1) | deferred to P2 build-time per gate |

work-cycle:0003
