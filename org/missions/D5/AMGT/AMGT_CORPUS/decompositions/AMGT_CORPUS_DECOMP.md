# AMGT_CORPUS -- L5 decomposition v26.0 -- ROUND 26 (four independent worker cells; one paired served act after cells 1-3)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~20:3xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-25 analysis
`ledger/ROUND_ANALYSIS.round25.md` @`19207dfb83` (msg 27357, READ-acked), s.4 ENRICHMENT LIST and s.2 rulings 1-6. Round 25's
decomposition is kept as `AMGT_CORPUS_DECOMP.round25.md`. Base of the cut: CLOUD `ae1c849af1`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | `Z-S71`: `dossier.py`'s model-block readers through `slash_safe_key` | `CRPS-ab-1` | `~1` (worker-light) |
| 2 | the unit classifier decides from the SERIES median (ruling 2) | `CRPS-ab-2` | `~2` |
| 3 | `case_rule` refuses a mixed-currency INPUT (ruling 3) | `CRPS-ab-3` | `~3` (worker-light) |
| 4 | the served act: re-derive what cells 2, 3 and 5 move, then `write_one` BP/NG (cell 1) | `CRPS-ab-4` | the issuer's WORLD act after 1-3 and 5 drain; no order |
| 5 | the header-currency census extended to BP/NG | `CRPS-ab-5` | `~5` |

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-ab-1` | LOCAL | `lib/research/corpus/dossier.py`, `lib/research/corpus/tests/test_dossier_slash_safe_round26.py` | every per-security model-block path through `slash_safe_key` |
| `CRPS-ab-2` | LOCAL | `integrations/bloomberg/research/build_unit_map.py`, `.../tests/test_build_unit_map_series_round26.py`, `deliverables/0.9.0_WK_AMGT_CORPUS~2/SERIES_MEDIAN_ROUND26.md` | unit from the series median; the bands unchanged |
| `CRPS-ab-3` | LOCAL | `lib/research/api/case_rule.py`, `lib/research/api/tests/test_case_rule_mixed_input_round26.py` | a mixed-currency constructed input served null with its reason |
| `CRPS-ab-5` | LOCAL | `integrations/bloomberg/research/model_block_pull.py` (the denomination tables only), `.../tests/test_figure_currency_round26.py`, `deliverables/0.9.0_WK_AMGT_CORPUS~5/DENOMINATION_CENSUS_ROUND26.{json,md}` | the BP/NG census of 6 header figures, and their table entries |
| `CRPS-ab-4` | WORLD | S3 blocks + dossiers | under a pair: serializing dry run, predecessor-code diff, act-start gate on the IMPORT CLOSURE (aa-4 AMENDMENT 1) |

The write sets are disjoint. All four cells may append rows to the surprise channel (append-only).

## 1a. Re-groundings at L5 (measured at base `ae1c849af1`; `checks/round26/`; every count states its key population, ruling 4)

- **ab-1:** `bp_reads raw bp_newest False ng_reads raw ng_newest False control_unchanged True`. The dossier reads the kept 09-25 raw copies,
  which reproduces `Z-S71`.
- **ab-2, over the newest block of 100 keys** (the raw-slash copies excluded; the encoded BP/NG included): **31 UNRESOLVED**. That is
  BBSE3 `CAPITAL_EXPEND` 10, BP `PE_RATIO` 10, BP `PROF_MARGIN` 10, and TSM `CURR_ENTP_VAL` 1, equal to the CVO's census.
  - The band constants' base hash is recorded (8 constants).
- **ab-3:** `bp_trailing_input 778.57 bp_input_reason_set False ng_value 1298.21`. The mixed input is reproduced.
  - **Its served reach:** `scoped_amgt.py:3195` recomputes the case per request from the DEPLOYED `case_rule`, so `/thesis` moves only
    with AMGT_RESAPP's next redeploy. ab-4 names this; the redeploy is RESAPP's act.
- **ab-5:** population **6 figures on 2 securities** (the encoded BP/NG keys, mixed, header, reporting-labelled).
- **Correction to this seat's round-25 packet (from the CTO's analysis):**
  - "375 BP/NG pointer units became measured" is wrong. BP's 10 `PE_RATIO` went from pointer to UNRESOLVED, so the true count is
    **365 measured and 10 to UNRESOLVED**. The aa-4 m3 transition print truncated the reason, and this seat did not census every
    (from, to) pair.
  - ab-4's measurement prints every (from, to) pair.

## 5. The round -- one issuance, fan-out as data

- `fanout: 4 of 5 chains, cap 8, reason: ab-1/ab-2/ab-3/ab-5 independent (disjoint write sets); ab-4 follows 1-3 and 5 (the rules it
  derives with and the dossier reader it writes through).`
- **Drain:**
  - each tip is re-graded, with every proof pin read by CONTENT (`git show <pin>:<path>`, `Z-S70`), then merged;
  - ab-4 opens its pair after 1, 2, 3 and 5 merge;
  - the L8 packet then goes to `3.0.0_SA_CVO~Z`.
- Surprise rows from `Z-S72`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
