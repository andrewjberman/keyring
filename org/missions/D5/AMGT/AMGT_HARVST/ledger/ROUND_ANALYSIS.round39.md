# AMGT_HARVST -- ROUND 39 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-03 ~01:2xZ

**Input:** CVO slug msg 28854, `surprise-channel/adjudications/ADJUDICATION_v51.md` @91385b6af2 (precondition MET).
**This seat's read:** `comp-surprise --project AMGT_HARVST` gives ARMED 0 over 294 investigation items and 146 remediation rows
(0 defects, 0 malformed).

## 1. WHAT THE ROUND DELIVERED

- **al-1 (Z-W91-S10):** a listing that answers 200 with no URLs now reads `LISTING_EMPTY_200` (`publishers.py:1095/1178/1011`) and
  reaches the job row (the worker.py amendment @5b33a747e3). The silent-zero hazard is closed in code. The live barrons proof waits on
  the terms card.
- **al-2 (FWD-16 v0.17):** FinBERT is keyed to a content hash of the exact text scored. It is built, with 0 Lambda calls and nothing
  run on publisher text.
- **Suites, on CVO~Z's own run:** 344 + 612 passed, 0 failed. Nothing was served.
- **ARMED went from 49 (02 afternoon) to 0.**

**Round 39 is CLOSED.**

## 2. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **Z-C-S69: an ft or no-text article has no content key, so `score_missing` re-appends its null-label marker row on every score run** | **Round-40 cell, LOCAL:** at most one marker row per key-less article. The plant runs two score runs over a planted key-less article and expects 1 marker row, not 2, with 0 FinBERT calls. No publisher text is processed. | This is the same reasoning as round 38's ruling 1. Fix it while FWD-16 is held, so that it cannot resume wrong. An append-only store grows by what happened, not by how often a job ran. |
| 2 | **What stays HELD** | FWD-16, FWD-17 and the event rebuild stay HELD on `CARD_HARVST_PUBLISHER_TERMS_20261002.md` @8d20bc24c8. The FWD-11 ft limb is licence-only (STOP_FT HARD). Both are carried to Andrew by this seat. | The five publishers' terms, read verbatim. |

## 3. ENRICHMENT LIST (round 40, ONE issuance by `2.0.0_SA_COO~H`)

1. **Z-C-S69** (ruling 1): one LOCAL cell with at most three mechanical criteria and the plant above.
2. **Nothing else is cuttable** until Andrew answers the terms card or the FT licence quote.

## 4. ACTS FOR ANDREW (cited)

- The publisher-terms card: pause collection (REC) or continue at his risk.
- The FT corporate licence quote (spend).
- Deleting the 62 quarantined ft articles, if wanted (REC: not yet).
