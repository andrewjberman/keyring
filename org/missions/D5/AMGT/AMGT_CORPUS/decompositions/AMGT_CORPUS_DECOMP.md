# AMGT_CORPUS -- L5 decomposition v36.0 -- ROUND 36 (the V3 rows on the Model tab, the units judgment read, the 10-05 fire read)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-04 ~21:3xZ.

**Source:** `1.0.0_SA_CTO~Z` round-35 analysis `ledger/ROUND_ANALYSIS.round35.md` @`02bbbc0208` s.4, the enrichment list (msg 29236,
READ-acked). The rectangle is its three items. Round 35's decomposition is kept as `AMGT_CORPUS_DECOMP.round35.md`. Base: CLOUD
HEAD at the cut; portal `DEV` @`ec65c5d637`.

## 0. What this round IS

| # | item (analysis s.4) | cell | path | risk |
|---|---|---|---|---|
| 1a | FWD-20: the Model slice serves the reason a V3 line has no figure | `CRPS-al-1` | worker `0.9.0_WK_AMGT_CORPUS~1` (worker-light), then `CRPS-al-2` on the same slot | LOCAL |
| 1b | FWD-20: `modelSheet.ts` renders the 49 V3 lines, with measured units or reasons | `CRPS-al-2` | worker `0.9.0_WK_AMGT_CORPUS~1` (queue position 2) | LOCAL (portal candidate; DEV push on Andrew's word) |
| 2 | The units judgment read: one non-USD name, and one field per family across three names | `CRPS-al-3` | worker `0.9.0_WK_AMGT_CORPUS~2` (worker-light) | LOCAL (read only; judgment at L9) |
| 3 | The 2026-10-05 13:00Z fire on pin `74e00624b0`: 96 pulled, rc 0, 0 pointer units | `CRPS-al-4` | the issuer's read (no order) | LOCAL (read) |
| 1c | The served move for 1a: one code-only redeploy of `opal-amgt-scoped-api` carrying al-1 | `CRPS-al-5` | the issuer's paired act after al-1 drains (pair to `1.0.0_SA_CTO~Z`) | WORLD |

**Why item 1 is three cells (issuer ruling, measured at the cut).** The 49 V3 mnemonics are 44 fiscal lines + `BEST_CPS` (a
forecast line) + 4 header facts (`SHORT_NAME`, `COUNTRY_FULL_NAME`, `AVG_DAILY_VALUE_TRADED_3M`, `CRNCY_ADJ_MKT_CAP`). The analysis
asks for "their reason where none is measured". The block carries that reason in `unresolved` (scope `fiscal_year_line_item`;
1299 HK: 97 entries, e.g. "not dated at the fiscal period end (non-December FYE, fye_join)"), but `scoped_amgt.read_model` serves
only the forecast reason today (`scoped_amgt.py:4271-4283`). So the reason needs an API field (al-1), the page needs the rows
(al-2), and the API field reaches the page only after a Lambda redeploy (al-5, a pair, like round 66's ap-4).

**Chains:** `al-1 -> al-2 -> al-5` (al-2 renders al-1's field; al-5 serves it), `al-3` (alone), `al-4` (alone, the issuer's read on
the 10-05 fire). `fanout: 2 of 2 worker chains, cap 8`. Write sets are disjoint:
- al-1: `lib/research/api/scoped_amgt.py` (the `read_model` return only) + one new test file;
- al-2: `portal/src/pages/SecurityAnalysis/{modelSheet.ts, tabs/ModelTab.tsx, types.ts}`;
- al-3: its read file under `deliverables/0.9.0_WK_AMGT_CORPUS~2/`;
- al-5: the Lambda artifact and its ledger entry.
No open AMGT_RESAPP order names `scoped_amgt.py` or `SecurityAnalysis/` at the cut (measured over every non-terminal RESAPP order).

## 1. The cells

**CRPS-al-1 (analysis ruling 1, the reason's seam).**
- `read_model` adds `fiscal_unresolved`: the block's `unresolved` entries whose scope is `fiscal_year_line_item`, each as
  `{mnemonic, fiscal_year, reason}`, in the block's order; `[]` when the block has none or there is no block (the unconditional
  literal, like the forecast keys). Nothing else in the slice moves.
- **Check** `checks/round36/al1_check.py` at the base: `al1 build 0/1 control 1/1` (b1 `fiscal_unresolved absent` on both names;
  c1 `fiscal_year_figures` 543 = block 543 on 1299 HK, 686 = 686 on BA). As expected.

**CRPS-al-2 (analysis ruling 1, the rows).**
- `buildModelSheet` takes two more optional arguments, `fiscalUnresolved` and `headerFigures`, and returns a third group titled by
  a new exported `V3_LINES_TITLE`, appended AFTER the two existing groups, with one row per V3 sheet mnemonic (the 44 + `BEST_CPS`,
  the latter in the E columns only). Each row is named in words and typed from the served unit.
- A V3 row with no figure in any column carries `absentReason` in words a PM reads, built from the served reasons. It never
  says ABSENT, REFUSED, "not read", "mnemonic", or a vendor code.
- The sheet also returns `v3Facts`: the 4 V3 header facts, each `{mnemonic, label, value}`, the value as served.
- `ModelTab.tsx` passes `data.model.fiscal_unresolved` and `data.header_figures`, and renders the V3 group and its facts.
- The 17 existing rows do not move.
- **Check** `checks/round36/al2_check.cjs` on the base portal: `al2 build 0/3 control 1/1` (b1 0/45 rows; b2 no V3 rows; b3 4 facts
  missing; c1 the 17 rows unchanged against `al2_base_snapshot.json`). As expected. Its fixture `al2_fixture.json` was captured
  from the real read path at the cut (BA 686 fiscal + 35 forecast + 24 header figures, 0 fiscal reasons; 1299 HK 543 + 30 + 23,
  97 fiscal reasons).

**CRPS-al-3 (analysis ruling 2, the units judgment).** A read, from the stored blocks, no vendor call:
- one figure per family for each of BA_US_Equity, TSM_US_Equity and SAP_GY_Equity. The families are ak-1's 8: TEXT, DATE, YEAR,
  PERCENT, ABSOLUTE_OR_MILLIONS, SHARE_COUNT_MILLIONS, PER_SHARE, RATIO. Each figure's served unit and value are set beside
  Bloomberg's definition (the producer's `FIELD_BASIS` text), with a verdict RIGHT / WRONG / CANNOT-TELL;
- TSM's currency labels over its 52 figures (an ADR: the quote is in USD, the filings are not).
- **Check** `checks/round36/al3_check.py` at the base: `al3 build 0/2` (file absent). As expected. The verdicts are a JUDGMENT
  criterion, graded by the CVO at L9.

**CRPS-al-4 (analysis ruling 6, the issuer's read).** After the 2026-10-05 13:00Z scheduled fire, read the run log's closing and
refresh lines and run `checks/round35/v35.py` over the fire's stamp: expect 96 pulled, rc 0, 0 pointer-unit figures. It is a
Monday, so the content is Friday's close. A regression read, not a re-grade of FWD-22.

**CRPS-al-5 (the WORLD act, after al-1 drains).** A code-only redeploy of `opal-amgt-scoped-api` at the drain commit, under a
never-widen pair: the COO half here, the CTO half by `1.0.0_SA_CTO~Z`. The deploy is run by the seat that ran round 66's ap-4
(`0.7.0_AE_CloudOps~A`) or by the issuer, under one NEVER-2 entry. Legs: upload, code-only safe-apply, verify (`al1_check.py` b1
against the deployed `/thesis` payload for 1299 HK, plus the deployed route's existing regressions). Rollback: the prior
VersionId.

## 2. Found at the cut (rows, not cells)

None new. The 4 V3 header facts are placed in al-2 as `v3Facts` (issuer ruling above).

## 3. Coverage

| cell | order | slot |
|---|---|---|
| CRPS-al-1 | `AMGT_CORPUS.TO-CRPS-al-1.model-slice-serves-fiscal-reasons.md` | `~1` |
| CRPS-al-2 | `AMGT_CORPUS.TO-CRPS-al-2.model-sheet-v3-rows.md` | `~1` (after al-1) |
| CRPS-al-3 | `AMGT_CORPUS.TO-CRPS-al-3.units-judgment-read.md` | `~2` |
| CRPS-al-4 | the issuer's read (no order) | -- |
| CRPS-al-5 | the issuer's paired WORLD act (no order) | -- |

## 4. Acts for Andrew (cited from the analysis)

- The portal DEV push of al-2 after `1.0.0_SA_CTO~Z`'s review (CLAUDE.md Portal: a product-file candidate).
