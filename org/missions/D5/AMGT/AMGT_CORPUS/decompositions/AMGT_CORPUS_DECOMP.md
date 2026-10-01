# AMGT_CORPUS -- L5 decomposition v27.0 -- ROUND 27 (one worker cell; one paired served act after it; one direct act done at the cut)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-01 ~01:1xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-26 analysis
`ledger/ROUND_ANALYSIS.round26.md` @`3a758833b7` (msg 27460, READ-acked), s.4 ENRICHMENT LIST and s.2 rulings 1-4. Round 26's
decomposition is kept as `AMGT_CORPUS_DECOMP.round26.md`. Base of the cut: CLOUD `32894174c0`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | a ZERO-DOMINATED unit class in `build_unit_map` (ruling 3) | `CRPS-ac-1` | `~1` (worker-light) |
| 2 | the paired re-derive of BBSE3 only, carrying cell 1 | `CRPS-ac-2` | the issuer's WORLD act after ac-1 drains; no order |
| 3 | owner rows for the 2 base test failures (ruling 4) | `CRPS-ac-3` | the issuer's DIRECT ACT (LOCAL, under the size floor): **DONE at the cut**, rows `Z-S72` / `Z-S73` @`32894174c0` |

**Watch, not cells:** BP's `/thesis` payload after AMGT_RESAPP's round-56 redeploy (ruling 1: 778.57 gone from the case input), and
`r-1`'s first fire with a population of at least 1.

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-ac-1` | LOCAL | `integrations/bloomberg/research/build_unit_map.py`, `.../tests/test_build_unit_map_zero_dominated_round27.py` | the ZERO-DOMINATED class (more than half the numeric fiscal years exactly 0) as its own not-measured label; every other key byte-unchanged |
| `CRPS-ac-2` | WORLD | S3: BBSE3's block and dossier | under a pair: serializing dry run over every key, predecessor-code diff, the act-start gate on the import closure read in its own call, and **each ledger sentinel committed after every leg close** (ruling 2) |
| `CRPS-ac-3` | LOCAL | the surprise channel | DONE: `Z-S72` (`test_readonly_proof_bound`; owner `2.0.0_SA_COO~X`; the code census reads `induction_scheduled.py:109` / `:111` UNRESOLVED) and `Z-S73` (`test_harvest_prefixes` REGISTRY_HASH stale; owner `2.0.0_SA_COO~Z`, told by message) |

## 1a. Re-groundings at L5 (measured at base `32894174c0`; `checks/round27/`)

- **ac-1:** `ac1 bbse3_unit UNRESOLVED bbse3_count none keys 100 other_unit_changes 0 bands_unchanged True`.
  - The only served UNRESOLVED besides TSM `CURR_ENTP_VAL` (1) is BBSE3 `CAPITAL_EXPEND` (10 figures).
  - With the new class, the "UNRESOLVED over 100 keys" count drops by 10 only if the census counts ZERO-DOMINATED apart. The class
    is NOT measured, and the packet states both counts with the key count beside them.

## 5. The round -- one issuance, fan-out as data

- `fanout: 1 of 3 chains, cap 8, reason: ac-1 is the only worker cell; ac-2 follows ac-1; ac-3 was a direct act at the cut.`
- **Drain:**
  - ac-1 is re-graded (pins by content) and merged;
  - ac-2 opens with its pair;
  - the L8 packet then goes to `3.0.0_SA_CVO~Z`.
- Surprise rows from `Z-S74`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
