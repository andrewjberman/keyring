# AMGT_CORPUS -- L5 decomposition v21.0 -- ROUND 21 (two independent cells now; the r-1 re-sign sequenced)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~04:1xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-20 analysis
`ledger/ROUND_ANALYSIS.round20.md` @`609100db54` (msg 26888, READ-acked), s.4 ENRICHMENT LIST, and its ADDENDUM @`7708a8506f`
(msg 26893, READ-acked), which adds cell 3. Round 20's decomposition is kept as `AMGT_CORPUS_DECOMP.round20.md`. Base of the
cut: CLOUD `f17ca57280`.

## 0. What this round IS

| # | item (analysis s.4 + addendum) | cell | slot |
|---|---|---|---|
| 1 | `pack_shape` in the dossier (ruling 3; FWD-16's floor) | `CRPS-w-1` | `~1` |
| 2 | re-sign `r-1` (with the `admit` step) once AMGT_RESAPP r51 `zz-1` drains | `CRPS-w-2` | the issuer's WORLD act under a pair; no order |
| 3 | a unit-map discriminator that does not rest on magnitude alone (the addendum; the nine UNRESOLVED facts) | `CRPS-w-3` | `~2` |

**Routed, NOT cells** (the analysis): the page render of the six outcomes, to DSGN_AMGTV1; 6501's empty-block reasons and the
`pack_shape` pass-through, to AMGT_RESAPP.

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-w-1` | LOCAL (a served dossier rewrite, if it moves served bytes, is the issuer's act under a pair at the drain) | `lib/research/corpus/dossier.py`, `lib/research/corpus/tests/test_dossier_pack_shape.py` (new) | `dossier.pack_shape(security_key, client=None)` and `build()`'s `fields["pack_shape"]`, from the reports the fold picks |
| `CRPS-w-3` | LOCAL (a unit-map commit and re-derive, if served units move, is the issuer's act under a pair at the drain) | `integrations/bloomberg/research/build_unit_map.py`, `.../tests/test_build_unit_map_discriminate.py` (new) | `build_unit_map.discriminate_facts(facts, s3=None)`: a cross-field consistency read that resolves a unit with its evidence or leaves it UNRESOLVED with the reason; never a guess |

Write sets are disjoint.

## 1a. Re-groundings at L5 (measured at base `f17ca57280`)

- **w-1, "the files the fold actually read"**, the ruling's words, is read as the class-A and class-B reports the dossier picks
  (`_picked_reports`, from `continuation._read_reports_with_bytes`). Measured through `_most_recent_of_class`:
  - `IMB_LN_Equity`: A `2026-07-17` docx.
  - `ADBE_US_Equity`: A `2026-07-13` pdf.
  - `AZN_LN_Equity`: A `2026-06-17` pdf, B `2026-Q2` pdf.
  - `6501_JP_Equity`: 0 report rows.

  Those four are the census's controls. All reports, rather than the picks, would call IMB "mixed" (10 pdf, 1 docx, 2 xlsx,
  2 png), which is not the shape the fold read. The census runs over the 96 keys of the round-17 census; the dossier's own
  resolved list reads 95.
- **w-3, the nine facts** (addendum), all read UNRESOLVED-ON in the committed map:
  - `SALES_REV_TURN`: 6501, 8316;
  - `CURR_ENTP_VAL`: 6501, 9433, 8035, 8766, TSM;
  - `NET_DEBT`: 8316;
  - `BEST_SALES` (the scalar exception): 6501.

  The MEASURED control is `SAP GY Equity` `CURR_ENTP_VAL` (MILLIONS; 86 names MEASURED on that field). Anchors the map holds as
  MEASURED: `CUR_MKT_CAP` (ABSOLUTE, scalar), `PX_LAST`, `IS_SH_FOR_DILUTED_EPS` (per security).
- **w-2: dependency as data.** `lib/research/identity/crosswalk.py`'s newest commit is still `6a940b02b8`; AMGT_RESAPP r51 is
  issued with `zz-1` first.

## 5. The round -- one issuance, fan-out as data

- `fanout: 2 of 3 chains, cap 8, reason: w-1/w-3 independent now (disjoint write sets); w-2 is the issuer's WORLD act sequenced
  behind AMGT_RESAPP r51 zz-1.`
- **Drain:**
  - Each tip is re-graded, then merged.
  - The one real run: the w-1 census and the w-3 discrimination on the merged tree.
  - If w-3 resolves any fact, the unit-map commit and the re-derive of the moved blocks go under a pair (NEVER-2 entry). If w-1's
    field moves served dossier bytes, the rewrite goes under a pair.
  - The L8 packet then goes to `3.0.0_SA_CVO~Z`.
- Surprise rows from `Z-S68`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
