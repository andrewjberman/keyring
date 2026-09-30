# AMGT_CORPUS -- L5 decomposition v18.0 -- ROUND 18 (three independent cells now; the r-1 re-sign sequenced)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~01:1xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-17 analysis
`ledger/ROUND_ANALYSIS.round17.md` @`50a4593cba` (msg 26826, READ-acked), s.4 ENRICHMENT LIST (four items) and s.2 rulings 1-4.
Round 17's decomposition is kept as `AMGT_CORPUS_DECOMP.round17.md`. Base of the cut: CLOUD `9dc713f359`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | registered names with no block get pulled: a population mode on `model_block_pull.py`, a step of the scheduled induction | `CRPS-t-1` | `~1` |
| 2 | `Z-S65`: per-security exceptions in `build_unit_map` | `CRPS-t-2` | `~2` |
| 3 | `Z-S64`: the key form each model-block reader uses (read-only) | `CRPS-t-3` | `~3` |
| 4 | re-sign `r-1` (with t-1's step) once AMGT_RESAPP r51's `write_pool` union drains | `CRPS-t-4` | the issuer's WORLD act under a pair; no order |

**NOT cells** (the analysis): re-keying the model block; widening the evidence rule.

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-t-1` | LOCAL (the fire goes under t-4's pair) | `integrations/bloomberg/research/model_block_pull.py`, `.../tests/test_model_block_admit.py` (new), `lib/research/corpus/induction_scheduled.py`, `lib/research/corpus/tests/test_induction_schedule.py` | the `admit` stage (the population prints first; a loud refusal if not signed in; batches of at most 3), run after registration on the scheduled path |
| `CRPS-t-2` | LOCAL | `integrations/bloomberg/research/build_unit_map.py`, `.../tests/test_build_unit_map_exceptions.py` (new), `.../tests/test_build_unit_map_classification_split.py` | an exception per security; never a shared status or type change |
| `CRPS-t-3` | LOCAL, read-only | `deliverables/0.9.0_WK_AMGT_CORPUS~3/MODEL_BLOCK_READERS_ROUND18.{json,md}` | the reader census, with BP/NG measured |

Write sets are disjoint. `t-1` and `t-2` both sit under `integrations/bloomberg/research/`, but in different files.

## 1a. Re-groundings at L5

- **t-1:** `model_block_pull.main` requires `--securities` on every stage. `admit` is the one stage without it. The population
  matches the round-17 census (the live library through the served crosswalk, 96), and today reads 0 without a block.
- **t-2:** the replay instrument (`checks/round18/t2_replay.py`) runs `build_unit_map.main(["--securities", "6501 JP
  Equity"])` against the pre-Hitachi map (`ead621d685^1`) in a temp file. It reads S3 raw only.
  - List elements are matched by identity. A positional diff read 2918 "changed", because the CLI inserts in sorted order.
  - At base: `shared_changed 23 type_changed 4 hitachi_reproduced 209 of 214`.
  - The CTO's "byte-equal" is graded as 0 shared or type change, with the reproduction count reported. An exception entry is
    a 6501-scoped addition by construction.
- **t-3:** the writer's form is measured (`BP/_LN_Equity` raw, 6 objects). The census measures every reader against it.
- **t-4: dependency as data.**
  - It fires when AMGT_RESAPP round 51's cell 1 merges on CLOUD. That cell moves the union into `write_pool` itself, so
    `add_security` is covered (row `Z-S66`). Until then, `add_security` builds without `served=`.
  - It also waits on `t-1`'s merge.
  - The re-sign's fork test runs through `add_security` on both sides, and the CTO half re-grades branch 2, including t-1's
    step.

## 5. The round -- one issuance, fan-out as data

- `fanout: 3 of 4 chains, cap 8, reason: t-1/t-2/t-3 independent now; t-4 is the issuer's act sequenced behind AMGT_RESAPP
  r51 cell 1 and t-1.`
- **Drain:**
  - Each tip is re-graded, then merged.
  - The one real run: `admit --dry-run` on the live population, the t-2 replay at HEAD, and the t-3 table re-read for BP.
  - The L8 packet then goes to `3.0.0_SA_CVO~Z`. If t-4 is still blocked, the packet states it.
- Surprise rows from `Z-S67`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
