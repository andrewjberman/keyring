# AMGT_CORPUS -- L5 decomposition v17.0 -- ROUND 17 (two cells: a model-block census; the r-1 re-sign, sequenced)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-29 ~23:1xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-16 analysis
`ledger/ROUND_ANALYSIS.round16.md` @`61ed59c609` (msg 26772, READ-acked), s.4 ENRICHMENT LIST (two items) and s.2 rulings 1-4.
Round 16's decomposition is kept as `AMGT_CORPUS_DECOMP.round16.md`. Base of the cut: CLOUD `c467c34342`.

## 0. What this round IS

| # | item (analysis s.4) | cell | class |
|---|---|---|---|
| 1 | a newly registered name gets its model block (`Z-W173-S5`, Hitachi) -- census first | `CRPS-s-1` | worker, LOCAL, read-only |
| 2 | re-sign `r-1` once AMGT_RESAPP r50 cell 5 (the pool-union invariant) drains | `CRPS-s-2` | the issuer's WORLD act under a pair + NEVER-2 entry; no order |

**NOT cells** (the analysis): the crosswalk invariant (AMGT_RESAPP r50 cell 5); widening the evidence rule (ruling 2: name-only
folders stay a manual act).

## 1. The rectangle

| cell | serves | `<risk>` | write set | the act |
|---|---|---|---|---|
| `CRPS-s-1` | the served read of a newly registered name | LOCAL | `deliverables/0.9.0_WK_AMGT_CORPUS~1/MODEL_BLOCK_CENSUS_ROUND17.{json,md}` | the census over the 96 live folders (present/absent, latest stamp), plus the producer chain and whether it admits new registrations |
| `CRPS-s-2` | FWD-4, FWD-19 (the scheduled induction) | WORLD | the Scheduled Task and a pinned checkout (round 16's act, unchanged) | `schedule_induction.ps1 -Register -Commit <invariant commit>` under a re-signed pair; ad-hoc QA run; first 13:00Z fire the acceptance |

## 1a. Re-groundings at L5

- **s-1:** `model_block_pull.py` requires `--securities` (at most 3, no population default), so admission is decided by its
  CALLERS. The census names them. The pull itself (a vendor call plus a served write) is not this cell's act; if admission is
  missing, the fix is the next cell and Hitachi's pull is a served write under its own pair.
- **s-2: dependency as data.** `s-2` fires when AMGT_RESAPP round-50 cell 5 (`write_pool` / `build_crosswalk` never drops a
  record present in the latest served pool) is merged on CLOUD.
  - At the cut that cell is not issued: RESAPP's round-50 list holds it.
  - Re-pin `r-1` to a CLOUD commit carrying both `bb2f3dbb18` and the invariant.
  - Re-sign with the COO half re-measured, and the CTO half grading branch 2 again. The act, the 13:00Z cadence and the builder
    name stand (ruling 3).
  - Until then, nothing is registered. The CVO measured 0 matching tasks and no pinned checkout.

## 5. The round -- one issuance, fan-out as data

- `fanout: 1 of 2 chains, cap 8, reason: s-1 is issued now; s-2 is the issuer's act sequenced behind AMGT_RESAPP r50 cell 5,
  no order.`
- **Close:**
  - s-1: re-grade at the tip, merge, and the one real run (this seat re-lists Hitachi's model-block prefix).
  - s-2: registration, ad-hoc QA run and first fire under the pair.
  - Then the L8 packet goes to `3.0.0_SA_CVO~Z`. If s-2 is still blocked on RESAPP when s-1 drains, the packet states that
    and the block.
- Surprise rows from `Z-S64`. Worker rows are `AMGT_CORPUS-Z-W1-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
