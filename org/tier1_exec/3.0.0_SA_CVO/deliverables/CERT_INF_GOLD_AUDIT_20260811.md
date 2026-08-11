# RULE-14e CERTIFICATION -- CRO~A INF GOLD AUDIT + REFACTOR SPEC (three-bucket map)

**Certifier:** 3.0.0_SA_CVO · **2026-08-11, pass run 0600-0610Z** · **archetype:** VALIDATE
**Subject:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/INF_ATOMDECOMP_RUN_20260811/03_GOLD_AUDIT_AND_REFACTOR_SPEC.md`
@8a93579b15 (authored ~0525Z; in-file must-calculate annotations updated on the @d272021791
ratification). **Method per @3c8418e34b:** load-bearing cells independently re-derived against live
S3 + source-at-HEAD + git provenance. Live reads 2026-08-11T06:00-06:08Z. No vendor egress used.

---

## VERDICT: **CERTIFIED, with ONE CLAUSE REFUSED AS WRITTEN** (the "reads the vendor TWR dim
## NOWHERE" scope). The three-bucket structure, the headline's data half, and every derivation-row
## mechanism check out at source. The refused clause changes W-B's SHAPE, not the refactor's direction.

## GROUNDING TABLE

| Cell | Audit claim | My re-derivation | Verdict |
|---|---|---|---|
| Headline, DATA half | Vendor account-grain TWR already landing daily; bronze `performance_dim.csv` 2026-08-10 14:28Z, 744KB | LIVE: `silver/api_dims/performance/` daily partitions through `snapshot_date=2026-08-11`; bronze `orion-api/2026-08-10/performance_dim.csv` LastModified 14:28:00Z, **744,001 bytes** -- exact. 08-11 file landed 05:40Z (CRO~A's live repair) | **CONFIRMED** |
| Headline, C_02 half | Served growth = residual from AUA deltas net of NNA; C_02 inputs = canonical_performance + canonical_nna + accounts_dimension ONLY | SOURCE `INF_C_02.client_performance.py` docstring Inputs block + full read-set grep: exactly those three keys; no `api_dims/performance` reference in the file. Served `gold/timeseries/client_performance.parquet` frozen 2026-08-01T14:54:24Z (the freeze this run diagnoses) | **CONFIRMED** |
| Bucket-1 row 1: price-series valuation | `INF_build_canonical_prices` T1 txn-median -> T2 yahoo -> T3 linear interpolation -> T4 carry-forward feeds B-chain valuation | SOURCE: tier docstring `:9-14` verbatim (T1 median `:164-189`, T3/T4 declared); consumer `INF_B_01.holdings_lots.py:5-6,22` -- joins positions_cube to canonical_prices to produce PRICED holdings; D_07/D_07a downstream. `orion-gold-dispatch.sh:306` wires it as INF_S_00 | **CONFIRMED** -- and correctly separated from B_00 (below) |
| Bucket-1 row 4: D_04 non-fee residual `:822` | `total_aua - fee_earning_aua` residual; fix drafted | TRUE AT VINTAGE; **remedy LANDED DURING THIS CERT PASS** @7341b27d50 (05:47Z) + serve-release/re-hold sentinel pair @96334728b4/@c33d2e5260: current source `:765-774` computes fee_earning_aua CLASSIFIED from the billing dim, "never total_aua - fee_earning_aua", gap surfaced as `unreconciled_aua` (= the ratified F4 bucket). The audit's row and the landed fix tell one consistent story | **CONFIRMED at vintage; remedy observed landed (fix itself NOT certified here -- DS/CTO lane owns its verification)** |
| Raw-already counterclaim | `INF_B_00` is a positions_mv pass-through; rot concentrated, not uniform | SOURCE header verbatim: "positions_mv pass-through... No TRN-as-price reconstruction", with the ARCHAEOLOGY note recording the retired TRN-reconstruction (Andrew's type-specimen class, already migrated off in B_00) | **CONFIRMED** -- the audit does not overclaim rot |
| Must-calculate annotations | Ratified set {NNA flow · non-fee residual TRANSITIONAL · rollups · F4 unreconciled} | Matches @d272021791 as relayed (CTO 054322Z). NNA-vs-residual kept as two nodes per the 045813Z correction | **CONFIRMED** |
| Unreviewed marking | ~24 of ~44 chain scripts signature-sweep only, named | Honest and named. GRAIN NOTE: `data/inf/scripts/gold/` holds **49** `INF_*` files (measured); "~44 chain" needs W-0's membership PREDICATE (a predicate is not a roster). The marked-gap discipline itself is exemplary | CONFIRMED with grain note |

## REFUSED AS WRITTEN (one clause)

**"...and reads the vendor TWR dim NOWHERE"** with the sentence's own scope apposition
"(INF_C_02 ... -> every D-chain publisher)". Measured: THREE D-chain publishers have loaded
`silver/api_dims/performance` since **2026-04-28** (git -S first-add: @72de8da626 "INF_D_00c
perf-fan-out -- silver/api_dims/performance into leaderboard"; @09b0b2046b D_02 "perf+tax+billing
fan-out into book.json summary"; @f5e7f81c81/@5293e48c79 D_04 TWR -- the 04-28 "$72.9T TWR runaway"
fix is served-output proof those fields flow). These reads PRE-DATE the audit by 3.5 months; this is
not my catching a post-audit landing. The TRUE precise statement: **C_02 -- the producer of the
served `growth` metric -- reads the TWR dim nowhere (confirmed above); the D-chain already fans
SOME vendor perf fields directly (null-tolerant WARN fallbacks), while the served growth remains
C_02's residual.** D_00c reads BOTH the C_02 base (`:705-715`) AND the TWR dim.

**Consequence, why this matters and no more than it matters:** W-B ("C_02/D_00c consume the TWR
dim") is a RE-POINT of the served growth metric plus a DEDUP of an existing partial fan-out -- not
a first introduction of a never-consumed feed. W-B's acceptance criterion survives unchanged; its
scope statement should absorb the existing three readers (which fields they already serve, which
duplicate what W-B adds). The refactor's direction is untouched -- Andrew's ruling stands on the
C_02 residual regardless.

## NOT RE-DERIVED (declared, not silently accepted)

The "33 derivation signatures" count in D_00c is the sweep instrument's own figure -- I did not
reproduce the signature definition. The five refactor waves' owner-suggestions and sequencing are
program design, outside cert scope (Doctrine §8).

## What you should have asked but did not (Doctrine §7)

What the three EXISTING TWR-dim readers DO with the fields they load -- specifically whether any
already-served field (leaderboard perf columns, book.json summary, D_04 N1-1 metrics) presents
vendor TWR beside C_02-residual growth ON THE SAME SURFACE. If yes, the portal is already serving
two performance methodologies simultaneously, and W-B is not just a re-point but a
COHERENCE repair -- worth knowing before W-B's acceptance bar is frozen, because "served
performance == vendor TWR to the basis point" (the current W-B acceptance) is only half a test if a
residual-derived twin remains beside it. One rendered-payload read per surface settles it.

-- 3.0.0_SA_CVO
