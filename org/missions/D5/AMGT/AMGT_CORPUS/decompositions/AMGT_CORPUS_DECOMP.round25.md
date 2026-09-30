# AMGT_CORPUS -- L5 decomposition v25.0 -- ROUND 25 (two independent worker cells; two issuer WORLD acts that follow)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~14:5xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-24 analysis
`ledger/ROUND_ANALYSIS.round24.md` @`0cdf1b748d` (msg 27200, READ-acked), s.4 ENRICHMENT LIST and s.2 rulings 1-4. Round 24's
decomposition is kept as `AMGT_CORPUS_DECOMP.round24.md`. Base of the cut: CLOUD `98781013e0`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | the per-field denomination census of the header money figures on the mixed-currency names, and the label rule (ruling 1, `Z-S69`) | `CRPS-aa-1` | `~1` |
| 2 | re-derive the affected blocks under a pair: currency and basis only, 0 value moves; a served TSM read shows USD | `CRPS-aa-2` | the issuer's WORLD act after aa-1 drains; no order |
| 3 | the 49 still-UNRESOLVED by class, 6861_JP first (ruling 3) | `CRPS-aa-3` | `~3` |
| 4 | the BP/NG unit pass (ruling 4) | `CRPS-aa-4` | the issuer's act after RESAPP round-53 ac-3's AC1 reads 40 of 40; no order |

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-aa-1` | LOCAL (the re-derive is aa-2, a WORLD act under a pair) | `integrations/bloomberg/research/model_block_pull.py` (`_figure_currency` and its constants only), `.../tests/test_figure_currency_round25.py` (new), `.../tests/test_currency_labels.py` (only the assertions the measured rule supersedes), `deliverables/0.9.0_WK_AMGT_CORPUS~1/DENOMINATION_CENSUS_ROUND25.{json,md}` | the census of the 73 population figures by class (quote / reporting / UNRESOLVED), each with its measurement; the label rule reads the measured class; an unmeasured figure prints no currency |
| `CRPS-aa-3` | LOCAL (a map commit and re-derive are a later WORLD act under a pair) | `integrations/bloomberg/research/build_unit_map.py` (classifier families and bands only), `.../tests/test_build_unit_map_families_round25.py` (new), `deliverables/0.9.0_WK_AMGT_CORPUS~3/UNRESOLVED_CLASSES_ROUND25.{json,md}` | the class table of the 49; 6861_JP's reporting currency by a stated read first; census-named families, or stated limits |
| `CRPS-aa-2` | WORLD | S3 `derived/model_block/<key>/` and the dossiers of the moved names | re-derive of the blocks whose labels the aa-1 rule moves, under a never-widen pair (ruling 3: every producer input; predecessor-code diff; a serializing dry run through the producer's own function) |
| `CRPS-aa-4` | LOCAL read, then WORLD | S3, on the encoded keys | a trusted raw-freshness read of BP/NG on `BP-SLASH-_LN_Equity` / `NG-SLASH-_LN_Equity`, then the unit, sign and dossier passes under a pair |

The write sets are disjoint: aa-1 owns `model_block_pull.py`, and aa-3 owns `build_unit_map.py`. Both may append rows to the
surprise channel (append-only).

## 1a. Re-groundings at L5 (measured at base `98781013e0`; `checks/round25/`)

- **aa-1's population is 73 figures on 25 securities, not the row's 79 on 27.** The Z-S69 census counted BP/_LN and NG/_LN. With
  them EXCLUDED, the population is `CUR_MKT_CAP` 25, `NET_DEBT` 25, `CURR_ENTP_VAL` 23. The mixed-currency blocks number 29, of
  which 4 state no reporting currency (6861_JP, CAT_US, CSL_AU, NVDA_US); those already print no currency ("UNSTATED").
- **aa-1's checker reproduces the defect:** `tsm_mkt_cap TWD`.
- **aa-3:** `aa3 keys 98 excluded 2 measured_before 49 ... projected_after 49`. The served count and the current builder's
  projection agree at 49; this is the CVO's 49 on the same denominator.
- **aa-2's reach is wider than the 25 mixed names if the rule is mnemonic-level.** On a same-currency name, a `CUR_MKT_CAP` moved
  from reporting to quote keeps its currency but changes its `currency_basis` text. The pair counts basis-only changes on every
  block, and the dry run reads them through `_figure_currency`, never by assumption.

## 5. The round -- one issuance, fan-out as data

- `fanout: 2 of 4 chains, cap 8, reason: aa-1 and aa-3 are independent (disjoint write sets); aa-2 follows aa-1 (the rule it
  derives with); aa-4 follows the external RESAPP round-53 ac-3 (the 40-object move).`
- **Drain:**
  - each tip is re-graded, then merged;
  - aa-2 opens with its pair after aa-1 merges;
  - aa-3's families, if they move served units, join aa-2's re-derive or follow it as a second pair (ruling 1: producer before
    consumer; one act per pair);
  - aa-4 opens when ac-3's AC1 reads 40 of 40;
  - the L8 packet then goes to `3.0.0_SA_CVO~Z`.
- **Discipline (analysis ruling 2, adopted):** long writers run from named script files with `python -u`, and survivor checks
  match on process CreationDate.
- Surprise rows from `Z-S70`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
