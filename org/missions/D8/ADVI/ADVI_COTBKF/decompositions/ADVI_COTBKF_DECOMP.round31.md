# ADVI_COTBKF decomposition -- ROUND 31 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-09 ~09:1xZ)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2`'s ADDENDUM 6 @d6e3227fd7 (msg 2968). Round 31 is one cell. It fetches the 2022-10-12 as-traded close of
808524102 and 808524839 from Yahoo and stores it with its as-of at an `address()` path, as evidence, not as a served price. It then
branches by the producer's own rule:
- **A** (about 39.99 / 39.44): close D2-S45.
- **B** (about 13.33 / 19.72): repair or blank under a pair.
- **Any other value:** a BLOCKING row.

**Rule 24.** Domain: one enrichment item, one cell.

## Measured constraints

1. The r26 and r28 closes on 2022-10-12, from CB-ad-1 (`deliverables/0.9.0_WK_ADVI_COTBKF~57/scale_trace.md`):
   - 808524102: 13.3302 (r26) / 39.9906 (r28);
   - 808524839: 19.7181 (r26) / 39.4362 (r28).
   - The splits were applied 2024-10-11: x3 and x2.
2. Ticker: 808524839 = SCHZ (`deliverables/PRICE_NEED/COTTONWOOD_PRICE_NEED_RANKED.csv`, the delivery's own symbol). 808524102 is
   not in that list, because it was priced. Its symbol is resolved from the delivery's rows by the same source
   `commonwealth_price_need.py` reads.
3. **Instrument trap:** Yahoo's `Close` is split-ADJUSTED, and only `Adj Close` adds dividends. A raw `Close` for 2022-10-12 reads the
   r26 level by construction and would falsely select branch B. As-traded = `Close` x the product of every split ratio after the
   day, from Yahoo's own split series. That is the method dell1's store uses for `as_traded_close` (contract @8abd95ad3b).
4. `lib/opal_naming.address("commonwealth", "cottonwood", "silver", "price_evidence", "date=2022-10-12")` ->
   `s3://opal-data-assets/commonwealth/cottonwood/silver/price_evidence/date=2022-10-12` (builder output, read ~09:1xZ).
   - It is a new evidence key with no reader, and its write set is a literal key the actor controls. The never-widen pair does not
     apply (NEVER-1 non-application).

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-ae-1` | fetch + store the as-traded 2022-10-12 close of the two CUSIPs; print the branch | FWD-3 | WORLD | none | `0.9.0_WK_ADVI_COTBKF~58` |

**Fan-out:** `1 of 1 chains, cap 8`. The branch B cell (repair or ABSENT under a pair) is cut on this cell's result.
