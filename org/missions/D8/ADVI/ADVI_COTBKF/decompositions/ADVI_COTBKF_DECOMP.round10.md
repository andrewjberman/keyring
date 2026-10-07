# ADVI_COTBKF decomposition -- ROUND 10 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-07 ~12:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s round-8/9 analysis correction @283b15713f (msg 485): E1 re-cut as marketdata only -- find the
marketdata price output (`historical-prices-daily` / `historical-prices-yfinance`); if it sits in a USABLE non-firm bucket, census it
against the 9,388,961 security-days needed. Firm buckets stay out (CTO ruling 1; the CLAUDE.md cross-firm NEVER). The 49F/INF half of
msg 456 is struck.

**Rule 24.** Domain: the one re-cut item. One cell.

## Measured constraints (dell2, 12:1xZ)

1. Registry (`infra/logic/registry/resources.json`), system `marketdata`: `historical-prices-daily` (EVENT_RULE),
   `historical-prices-yfinance` (LAMBDA), `historical-prices-fetcher` (EC2_INSTANCE), plus 24 other marketdata resources. The rows carry
   no output address; the output must be read from the function's configuration and source.
2. The round-4 census graded all 40 buckets; BARRED = the five firm buckets (49financial, bd, inflection, inf, demo); it read six legacy
   price stores in USABLE buckets, none of them marketdata's.
3. Need and covered: 9,388,961 security-days; 1,297,651 covered by the six (row S17); 2,914 of 4,634 securities unpriced (row S19).

## The cell

| cell | what | serves | risk | slot |
|---|---|---|---|---|
| `CB-j-1` | locate marketdata's historical-price output by reading the function's configuration and source (never invoking it); grade its bucket USABLE / BARRED from the registry; if USABLE, census it against the 4,634 securities and 9,388,961 security-days, and print the gain over the six stores | FWD-3 (CB4d1-AC3) | SERVED | `0.9.0_WK_ADVI_COTBKF~26` |

**Write set:** `data/assets/scripts/analysis/commonwealth_marketdata_prices.py` + its test; the deliverables folder; the investigation
file. **Fan-out:** `1 of 1 chains, cap 8`.
