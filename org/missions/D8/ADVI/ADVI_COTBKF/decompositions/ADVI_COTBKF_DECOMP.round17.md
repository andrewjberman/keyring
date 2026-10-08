# ADVI_COTBKF decomposition -- ROUND 17 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~21:3xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-16 analysis `CTO_ROUND_ANALYSIS_ADVI_COTBKF_ROUND_16_20261007.md` @8b6829c89f (msg 1100):
E1 flow timing (D2-S28), E2 zero-amount transfers (D2-S27), E3 document page counts (D2-S26); all LOCAL; ONE issuance.

**Rule 24.** Domain: E1-E3. One cell per item; MECE over the list.

## Measured constraints

1. Zero-Amount external flow rows on the applied transactions: `lo` 18,157; `li` 1,424; `trfo` 611; `trfi` 60; `trco` 147 of 147
   (round-16 census). The same-day prices exist inside `commonwealth_daily_valuation.py` but are not written out.
2. Graded months on round 16's real run: flow months 272 MATCH / 866 DIFF (median |diff| 7.445); no-flow months 1,675 / 1,418 (0.353).
   The return takes flows at the end of the day.
3. `page_count` in the served document index comes only from the listing field `NumberOfPages`
   (`commonwealth_document_index.py:268`): 10,072 of 11,119 listings lack it and 1,034 carry "0" (issuer read, 2026-10-07 ~21:3xZ).
   `pypdf` is installed on dell2.

## The cells

| cell | item | serves | risk | slot |
|---|---|---|---|---|
| `CB-q-1` | E2: zero-Amount transfers valued at quantity x the same-day close; valuation writes `security_day_price.parquet` | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~35` |
| `CB-q-2` | E1: flow timing, start vs end of day, side by side on the fully priced months; the convention chosen by the result | FWD-3 | LOCAL | `0.9.0_WK_ADVI_COTBKF~35` (after CB-q-1) |
| `CB-q-3` | E3: page counts read from each served PDF; the cause named; the served index is filled afterwards by the issuer's apply | FWD-5 | LOCAL | `0.9.0_WK_ADVI_COTBKF~36` |

**Dependencies:** CB-q-1 and CB-q-2 write the same file (`commonwealth_daily_returns.py`), so they are ONE chain on one worker, E2 first
(the flow-timing test is fairer once zero-Amount flows are valued). CB-q-3 is independent.
**Fan-out:** `2 of 2 chains, cap 8`.
