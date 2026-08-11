# Pair-matching engine built + TPFEE/SMFEE VERIFIED -- both COO required rows discharged on Andrew's GO
**archetype:** IMPLEMENT + VALIDATE
**Window:** 0706-0710Z, Andrew-direct GO.

## What happened

1. **Specimen verify -> VERIFIED, whole-family grade:** TPFEE detail text "TO ADVISOR" (debit legs)
   + "FRM {masked}" credit legs, 92 bps median implied annual over 4,881 accounts; SMFEE "TO SEP
   ACCT MGR" 100 percent debits at 34 bps (SMA-manager scale); MGFEE the explicit control, same
   two-leg shape. INFERRED retired by measurement; classification JSON re-graded (2 rows).
   **BOUNDARY GIFT:** the FRM-credit-receiving accounts are advisor COLLECTION accounts inside the
   book -- a mechanical exclude-list discriminator for the sec2 client-composite boundary.
2. **Pair-matching engine BUILT + committed** (scripts/pair_match_engine.py, ruff-clean first
   pass): cash conditional family dissolved into $193.7M MATCHED-INTERNAL (48.7 percent by value /
   16.7 percent by rows -- both denominators printed) + $204.3M EXTERNAL-BY-DEFAULT (conservative
   direction per the standard, split/multi-leg residual counted never silently internal).
3. **The in-kind 0.0 percent was MY INSTRUMENT until verified, then the estate:** IC-row
   debit_credit carries LONG/SHORT (position side, not direction; quantities unsigned) -- a
   direction-keyed matcher structurally cannot fire -- the could-not-have-said-otherwise class,
   caught by the mechanism check BEFORE publication. Measured truth underneath: 99.2 percent of
   in-kind (date,cusip,qty) groups are ONE-SIDED in-book -> EXTERNAL-dominant ACAT class; direction
   resolution for one-sided events = position-delta corroboration, named for the build.
4. All landed @5bb3b2626d; COO's two required register rows discharge; estate-truth priors handed
   to ~A (check the direction-field SEMANTIC per row-type before matching on it -- at Orion/BD too).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| pandas over the local 525-partition series | family-level fee verify + pair matcher + mechanism check | the verdicts |
| commit-gate (ruff) | on the engine script | PASSED first attempt (lesson from task 1 applied) |
| dim_balance parquet | implied-rate denominators | 92/34/77 bps distributions |

## Blockers

**None at me.** Named follow-ups riding the archetype build (owners at decomposition): in-kind
direction via position delta; the advisor-collection-account roster groupby; zero-price in-kind
valuation pass. RECON-6 resumes.
