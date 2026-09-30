# AMGT_CORPUS -- L5 decomposition v20.0 -- ROUND 20 (two independent cells now; the r-1 re-sign sequenced)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~03:1xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-19 analysis
`ledger/ROUND_ANALYSIS.round19.md` @`d5d806bc2e`, s.4 ENRICHMENT LIST (three items) and s.2 rulings 1-3.
Round 19's decomposition is kept as `AMGT_CORPUS_DECOMP.round19.md`. Base of the cut: CLOUD `be851f21d2`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | the 3.9 floor: no `Path.write_text` / `read_text` call passes `newline=` | `CRPS-v-1` | `~1` |
| 2 | the six render outcomes (FWD-10, 11, 12, 15, 16, 18): a served census over 96 names plus a 5174 walk per outcome | `CRPS-v-2` | `~2` |
| 3 | re-sign `r-1` (with the `admit` step) once AMGT_RESAPP r51 cell 1 drains | `CRPS-v-3` | the issuer's WORLD act under a pair; no order |

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-v-1` | LOCAL | `integrations/bloomberg/research/model_block_pull.py`, `.../tests/test_model_block_admit.py`, `.../tests/test_model_block_unit_map_write.py` (new), `lib/research/corpus/tests/test_induction_planted_drive.py`, `lib/research/corpus/tests/test_induction_schedule.py` | every `newline=` on a `Path` text call becomes `open(path, mode, encoding=..., newline=...)`; an LF test on `_ensure_unit_map`'s write |
| `CRPS-v-2` | LOCAL (read-only served invocations and a local-build walk) | `deliverables/0.9.0_WK_AMGT_CORPUS~2/FWD_EVIDENCE_ROUND20.{json,md}` | per outcome: the served census over the 96 names with its denominator, and the named page on 5174 read and written down |

Write sets are disjoint.

## 1a. Re-groundings at L5 (measured at base `be851f21d2`)

- **v-1, the census.** No 3.9 interpreter is installed (`py -0` lists 3.14 and 3.11), so ruling 1's AST branch applies. The
  ruling names `lib/research/corpus/`, and its defect (`_ensure_unit_map`) lives in `integrations/bloomberg/research/`. The
  issuer rules the census over BOTH roots: the named root alone would pass with the named defect in place. The base reads
  10 calls over 95 files: `model_block_pull.py:846` (the defect), 2 in `test_model_block_admit.py`, and 7 in the two corpus
  induction tests. They all go, so the tests hold the floor the code states.
- **v-2, the pages per outcome** (chosen from round 14's served measurements, `FWD_EVIDENCE_ROUND14_SERVED.json`):
  - `IMB LN`: the docx pack, carrying pillars, management, posture and terms.
  - `AMD US`: the ABSENT arm.
  - `AZN LN`: the team's cases are served.
  - `ADBE US`: a PDF-only pack; `IMB LN` is its docx control.
  - The population is the 96 names of the round-17 census (`MODEL_BLOCK_CENSUS_ROUND17.json`, `denominator 96`).
  - At the cut, the local build answers on 5174 (HTTP 200) from portal DEV `29c8226a`, and the walker account reads
    `status=disabled armed=no; SSM ABSENT`.
- **v-3: dependency as data.** `lib/research/identity/crosswalk.py`'s newest commit is still `6a940b02b8`.

## 5. The round -- one issuance, fan-out as data

- `fanout: 2 of 3 chains, cap 8, reason: v-1/v-2 independent now (disjoint write sets); v-3 is the issuer's WORLD act sequenced
  behind AMGT_RESAPP r51 cell 1.`
- **Drain:**
  - Each tip is re-graded, then merged.
  - The one real run: the v-1 census and the suites on the merged tree, and the v-2 file re-read with the walker account read
    at rest.
  - The L8 packet then goes to `3.0.0_SA_CVO~Z`. If v-3 is still blocked, the packet states it.
- Surprise rows from `Z-S68`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
