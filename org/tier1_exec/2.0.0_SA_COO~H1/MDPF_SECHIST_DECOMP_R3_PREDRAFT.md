# MDPF_SECHIST decomposition -- ROUND 3, PRE-DRAFT for the PASS branch (issuer 2.0.0_SA_COO~H1, dell1; 2026-10-09 ~04:5xZ)

**Status: PRE-DRAFT, NOT ISSUED, NOT A DECOMPOSITION OF RECORD.** It lives in the issuer's folder, not in `decompositions/`, so no
gate or reader takes it as cut. It is copied into `decompositions/MDPF_SECHIST_DECOMP_R3.md` and re-checked only after the CTO issues
the round-2 analysis on the PASS branch. On FAIL it is void (FAIL re-arms TO-SH-t3 or cuts one repair cell, nothing here).

**Inputs read:** the CTO pre-draft `org/missions/D8/MDPF/MDPF_SECHIST/ledger/ROUND_ANALYSIS.round2.PREDRAFT.md` (@fc38afc55b, amendments
1-3 @7b888dcd22 / @62c6adbde9 / @ad986584f4); the CRO substrate note
`org/tier1_exec/4.0.0_SA_CRO~DELL1/deliverables/MDPF_SECHIST_ROUND3_SUBSTRATE_NOTE_20261009.md` (@47baa5efca); the Yahoo ownership ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_YAHOO_BACKFILL_OWNER_DEMQUE_VS_SECHIST_20261009.md` + ADDENDUM 1 (KEEP + PORT).

## The rectangle (PASS items, as the pre-draft lists them)

| # | FWD | cell | gate | write set (draft) | risk | chain |
|---|---|---|---|---|---|---|
| 1a | FWD-4 | `SH-r3-a` gap record, READ SIDE: per tracked security, stored range, required range, and missing/held-null days, derived from the stored partitions against each partition's `vendor_observations` (the vendor's own count, `etf_daily_pull.py:697`), never a trading calendar (`compute_returns` docstring, `etf_positioning_gold.py:855+`) | none | a new gold-side module beside `data/etfs/scripts/gold/etf_positioning_gold.py`; its S3 key is `lib/opal_naming.py address()` output: `address("bloomberg", "etfs", "silver", "history_gaps", "as_of=<d>")` -> `s3://opal-data-etfs/bloomberg/etfs/silver/history_gaps/as_of=<d>` (builder ACCEPTED at 04:5xZ; source `bbg` is REFUSED, not a systems.json key -- the pull's legacy `bbg/<asof>/` prefix is not re-used, and is not migrated here, rule 30 non-application) | SERVED | A1 |
| 1b | FWD-5 | `SH-r3-b` blank over a gap: `compute_returns` blanks any window containing a day the gap record lists (an ABSENT interior day, which it compounds across today; a NULL already blanks, `:913-915`) | after 1a (data edge: the gap record) | `data/etfs/scripts/gold/etf_positioning_gold.py` + its tests | SERVED | A2 |
| 1c | FWD-5 | pull-side fill: the pull widens its next request to the listed days | **Andrew's act, call b186** (no-modify order on `integrations/bloomberg/pipeline/`) | `etf_daily_pull.py` | WORLD (site Z take, CTO~Z half, DEMQUE quote) | not cut without b186 |
| 2a | FWD-3 | `SH-r3-c` where each security entered: per source (Opal ETF, client account by firm, rival fund) its required depth, deepest rule governing (C-DEPTH) | none | read the table row, add the depth record beside it; never write classification (C-TABLE) | SERVED | B |
| 2b | FWD-2 | `SH-r3-d` Cottonwood id join, READ ONLY: map the 4,545 `PRICE_NEED_FOR_SECHIST.csv` ids to table keys (234 match `CUSIP:` today), list the unmapped | none (not under card A) | evidence file only | LOCAL | C |
| 3 | FWD-6 | `SH-r3-e` `NAME::` census, READ ONLY: which writer mints `NAME::` keys, population per writer (5,673 today), and whether any hop carries one to the pull label or the join | none; the FWD-6 build cell waits on MDPF_SECCLASS's key ruling on this census | evidence file only | LOCAL | D |
| 4 | FWD-9 | total-return level field in the history request (route 2a) | **Andrew's act, call b186** | `etf_daily_pull.py` + gold | WORLD | not cut without b186 |
| 5 | FWD-7 | budget ledger over the history legs | only if round 2 graded FWD-7 below REALIZED | -- | -- | conditional |
| Y | FWD-2 (Yahoo share) | `SH-r3-f` the SECHIST Yahoo series writer on `price_store`'s SAME keys (Commonwealth 9-char CUSIP, `s3://opal-data-assets/yahoo/global/silver/price_history/cusip=<id>`), built to the contract `PRICE_STORE_CONTRACT.md`; the writer switch is ONE window with dell2 re-pointing and a same-window rollback, never two writers | the CTO places it in a round (the ruling names no round); listed so the issuance can carry it if the analysis does | `data/etfs/scripts/...` new writer, no write to `price_store`'s paths until the switch window | SERVED, then WORLD at the switch | E |

Fan-out (draft): 5 chains (A1->A2, B, C, D, E if placed), cap 8. Items 1c and 4 are absent until b186 is answered; with a yes they join
as chain F (one pull cell carrying both edits, at most three criteria, landing after a scheduled pull).

## Rule 24 (draft)

Domain: the PASS enrichment list (items 1-5) plus the Yahoo writer if the analysis places it. Subtraction: 1 -> 1a, 1b (+1c gated);
2 -> 2a, 2b (card A's Bloomberg leg held); 3 -> census only (build waits on the key ruling); 4 -> gated; 5 -> conditional. Remainder:
FWD-8 (goes with MDPF_SECCLASS FWD-5), FWD-2's Bloomberg backfill (Andrew's card A, call deae).

## Checks to dry-run at the base before the cut (each must FAIL at base)

- 1a: one known gap read from the record -- the 2026-10-01..10-05 DIVZ/IDVZ outage days (prior art
  `s3://opal-data-etfs/bbg-testpull/tickers/SALXX/gap_20261001_20261005/history.csv`), expect the days listed.
- 1b: one planted absent interior day, window over it reads blank; same window with the day present reads a value.
- 2b: `matched=<n>/4545` printed, expect `n>=234` and an unmapped list with its denominator.
- 3: `NAME:: rows=<n> writers=<k>` printed, expect `n=5673` at the scan's vintage.
