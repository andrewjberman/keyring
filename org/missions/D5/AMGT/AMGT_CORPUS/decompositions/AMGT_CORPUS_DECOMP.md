# AMGT_CORPUS -- L5 decomposition v23.0 -- ROUND 23 (three independent builds; ONE dependency-ordered WORLD act after both unit cells)

**Issuer:** `2.0.0_SA_COO~X`, 2026-09-30 ~07:3xZ. **Source:** `1.0.0_SA_CTO~Z`'s round-22 analysis
`ledger/ROUND_ANALYSIS.round22.md` @`a940eb6813` (msg 27004, READ-acked), s.4 ENRICHMENT LIST and s.2 rulings 1-5. Round 22's
decomposition is kept as `AMGT_CORPUS_DECOMP.round22.md`. Base of the cut: CLOUD `afad83a02f`.

## 0. What this round IS

| # | item (analysis s.4) | cell | slot |
|---|---|---|---|
| 1 | unit families from the unfamilied-mnemonic census (the LEAD) | `CRPS-y-1` | `~1` |
| 2 | `derive --no-sa-fallback` | `CRPS-y-2` | `~2` |
| 3 | TSM's same-currency anchor | `CRPS-y-3` | `~3` |
| -- | the map commit, then ONE re-derive pass of every affected block under `--no-sa-fallback` (8316 and 8766 included) | `CRPS-y-4` | the issuer's WORLD act under a pair, after y-1 and y-2 drain (ruling 1) |

## 1. The rectangle

| cell | `<risk>` | write set | the build |
|---|---|---|---|
| `CRPS-y-1` | LOCAL (the map commit is y-4) | `integrations/bloomberg/research/build_unit_map.py` (the classifier families only), `.../tests/test_build_unit_map_families.py` (new) | a family for every mnemonic the census finds unfamilied; `EQY_FUND_CRNCY` as TEXT; the per-share band decides JPY-scale per-share figures by a cross-field read, never by magnitude alone |
| `CRPS-y-2` | LOCAL | `integrations/bloomberg/research/model_block_pull.py` (the derive path and CLI), `.../tests/test_model_block_no_sa_fallback.py` (new) | `--no-sa-fallback`: the fallback is never loaded or called; each gap stays a labelled gap |
| `CRPS-y-3` | LOCAL | `integrations/bloomberg/research/unit_anchor.py` (new), `.../tests/test_unit_anchor.py` (new) | `same_currency_anchor(s3, security, header)`: a TWD-line market cap or a STORED measured FX rate with its date; else None with the anchors searched. Never an invented rate. |

Write sets are disjoint. **The one hookup belongs to no cell:** `discriminate_facts` (in y-1's file) calling
`unit_anchor.same_currency_anchor` when the listing and reporting currencies differ. The issuer adds it at the merge, after y-1
and y-3 drain.

## 1a. Re-groundings at L5 (measured)

- **A CORRECTION to this seat's round-22 census, which the analysis quotes.** "9,612 of 37,746 (25%) UNRESOLVED" counted only the
  `UNRESOLVED` prefix.
  - A second class of not-measured unit is served: the reader's pointer `SEE field_map.json ... not yet built`, which means no map
    entry at all.
  - Measured over the newest block of 100 keys (read ~07:3xZ): **LABEL 21,694 (100 names); UNRESOLVED 9,595 (68 names); POINTER
    6,457 (36 names).**
  - So the not-measured share is **16,052 of 37,746 (42.5%)**. UNRESOLVED fell from 9,612 by round 22's 17 flips.
- **What today's builder does to them** (y1 census at base, into a temp map over the crosswalk population):
  - `after unresolved 14553 pointer_after 0 no_family_after 14082 crncy_after 96 per_share_after 276`.
  - A rebuild alone gives every name an entry (0 pointers), and turns most pointers into no-family UNRESOLVED.
  - Cell 1's families are therefore what moves the 42.5%, and its AC reads `no_family_after 0` and `crncy_after 0` over the same
    100 blocks.
- **Per-share:** `PER_SHARE_FIELDS` already names `IS_DIV_PER_SHR`, `REVENUE_PER_SH` and `BOOK_VAL_PER_SH`. They fail on the
  `0 < |v| < 2000` magnitude band at JPY scale. "The band covers them" is built as a cross-field read (per-share / `PX_LAST` in
  the same currency), never as a wider magnitude band.
- **TSM:** the store holds no TWD line (`2330_TT_Equity` has 0 raw objects) and no FX field (bronze families: article,
  bestdata, exec_officers, histdata, histdata_daily_px, identity, news_listing, refdata). Cell 3's honest outcome today is `anchor
  none` with the searched anchors named. Its value is the mechanism, planted-tested.
- **y-4's order (ruling 1):**
  1. y-1 and y-2 merge, and the hookup lands.
  2. ONE map commit.
  3. ONE derive pass under `--no-sa-fallback` over every block whose map entries moved, with 8316 and 8766 in that pass. It is
     never two passes on one block.
  - The expected diff is read from the builder and the derive at signing.

## 5. The round -- one issuance, fan-out as data

- `fanout: 3 of 4 chains, cap 8, reason: y-1/y-2/y-3 independent builds with disjoint write sets; y-4 is the issuer's WORLD act
  sequenced after y-1 and y-2 (and the y-3 hookup).`
- **Drain:**
  - Each tip is re-graded, then merged; then the hookup commit.
  - Then y-4's pair (the expected diff from the builder, with both branches stated), its NEVER-2 entry, and the act.
  - The L8 packet then goes to `3.0.0_SA_CVO~Z`.
- Surprise rows from `Z-S68`. Worker rows are `AMGT_CORPUS-Z-W<n>-S<k>`, with `disarm_owner 2.0.0_SA_COO~X`.
