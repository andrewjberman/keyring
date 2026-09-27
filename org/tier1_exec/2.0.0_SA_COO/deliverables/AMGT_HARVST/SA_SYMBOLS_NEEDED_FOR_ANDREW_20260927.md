# 33 names still needing a SEEKING ALPHA symbol -- for Andrew to fill

**Andrew-direct 2026-09-27:** *"What exactly is the issue, you don't know the tickers? If so, give me the list
and I will find them myself."*

---

## THE ISSUE IS NOT THAT WE DO NOT KNOW THE TICKERS

⛔ **We know the BLOOMBERG ticker for every one of these** -- it is in the folder name (`Sanofi SAN FP`,
`Rio Tinto RIO LN`). What is missing is **SEEKING ALPHA's OWN INTERNAL SYMBOL**, which is a different
namespace: Sanofi's Bloomberg ticker is `SAN FP` and its SA symbol is `SNY`. One does not derive from the
other for a non-US line -- `infer_sa_symbol` (`lib/research/identity/resolver.py:80`) only infers for US
names, by stripping a ` US` suffix, and returns UNRESOLVED for everything else.

⛔ **THE RESOLUTION FAILURE IS HTTP 403 RATE LIMITING ON seekingalpha.com**, not a knowledge gap and not a
per-security restriction. The endpoint that maps a company name to SA's symbol is the only automated source
we have, and it refuses us. Measured tonight: resolutions went 18 -> 56 and then flatlined while search
refusals climbed 24 -> 28 -> 29.

⚠ **AND 26 OF THE 33 WERE NEVER ASKED AT ALL.** The pass walks folders in order, so once refusals start it
never reaches the rest of the alphabet -- every unresolved name from `SSE plc` to `Zurich` is simply
**unreached**, not refused. That is why the list below looks alphabetical from S onward.

## WHAT WOULD HELP MOST

**SA's symbol for each row.** Where we already have a candidate it is in the table -- those came from SA's
own search and matched on company name, but the pass could not run its second test (do the returned article
TITLES name this company?) because the news call was also 403'd. ⛔ **So treat our candidates as UNCONFIRMED
suggestions to check, not as answers** -- one of them, `OBT` for Orange, turned out to be *Orange County
Bancorp*, a different company that matched on the token "orange". Two candidates on one row usually means
two lines of the same issuer (ADR vs OTC ordinary, or a Canadian listing); the one we want is **the line SA
publishes its news under**.

**11 of 33 carry a candidate. 22 are blank.**

---

| # | research folder | bloomberg ticker | OUR CANDIDATE(S) -- UNCONFIRMED | why unresolved |
|---|---|---|---|---|
| 1 | Haliburton HAL | HAL US | `HAL` = Halliburton Company | search 403 |
| 2 | International Container Terminals | (none recorded) | `ICTEF` = International Container Terminal Services, Inc. | news 403 (the search WORKED) |
| 3 | Nestle NESN SW | (none recorded) | `NSRGF` = Nestlé S.A.; `NSRGY` = Nestlé S.A. | search 403 |
| 4 | Nike NKE US | (none recorded) | `NKE` = NIKE, Inc.; `NKE:CA` = NIKE, Inc. | search 403 |
| 5 | Novartis NOVN SW | NOVN SW | `NVS` = Novartis AG; `NVSEF` = Novartis AG | search 403 |
| 6 | Nubank NU | NU US | -- | refused on evidence |
| 7 | Orange ORA FP | (none recorded) | `OBT` = Orange County Bancorp, Inc.; `ORANY` = Orange S.A. | search 403 |
| 8 | QXO | (none recorded) | `QXO` = QXO, Inc.; `QXO.PR.B` = QXO, Inc. 5.50 DEP PFD | search 403 |
| 9 | Rio Tinto RIO LN | (none recorded) | `RIO` = Rio Tinto Group; `RTPPF` = Rio Tinto Group | news 403 (the search WORKED) |
| 10 | Roche ROG SW | ROG SW | `RHHBF` = Roche Holding AG; `RHHBY` = Roche Holding AG | news 403 (the search WORKED) |
| 11 | SSE plc SSE LN | SSE LN | -- | search 403 |
| 12 | Sanofi SAN FP | (none recorded) | `SNY` = Sanofi; `SNYNF` = Sanofi | news 403 (the search WORKED) |
| 13 | Schlumberger SLB | SLB | -- | refused on evidence |
| 14 | Shopify SHOP CA | (none recorded) | `SHOP` = Shopify Inc.; `SHOP:CA` = Shopify Inc. | news 403 (the search WORKED) |
| 15 | Singapore Telecom ST SP | ST SP | -- | search 403 |
| 16 | Spotify SPOT US | (none recorded) | -- | search 403 |
| 17 | Sumitomo Mitsui Financial Group 8316 JP | (none recorded) | -- | search 403 |
| 18 | Synopsys SNPS US | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 19 | Taiwan Semiconductor Manufacturing TSM US | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 20 | Telefonica Brazil VIVT3 BZ | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 21 | Tokyo Electron 8035 JP | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 22 | Tokyo Marine 8766 JP | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 23 | Total Energies TTE FP | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 24 | UBS | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 25 | Uber Technologies UBER US | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 26 | Unilever ULVR LN | ULVR LN | -- | never asked -- alphabetical tail, never reached |
| 27 | Universal Music Group UMG NL | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 28 | Valero Energy VLO | VLO US | -- | never asked -- alphabetical tail, never reached |
| 29 | Visa V | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 30 | Walmart de Mexico WALMEX MM | WALMEX* MM | -- | never asked -- alphabetical tail, never reached |
| 31 | Workday WDAY US | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 32 | Zoetis ZTS US | (none recorded) | -- | never asked -- alphabetical tail, never reached |
| 33 | Zurich Insurance ZURN SW | ZURN SW | -- | never asked -- alphabetical tail, never reached |

---

## AFTER YOU FILL IT

Hand it back in any form and the values go in through the same rule the pass uses -- never as a bare
overwrite. Where you have confirmed a symbol yourself, that is a MEASURED value on your authority and it is
recorded as such (`resolution_reason` naming you), which is a stronger provenance than the pass's own
INFERRED-from-two-readings-of-one-source. The field feeds
`publication_gold._listing_hit_query_identifiers`, so a wrong symbol files another company's chatter against
ours -- which is the only reason the pass refuses a best guess in the first place.

**Note the ceiling this does NOT lift:** attaching symbols to the securities file the gold builder reads is
capped at the Bloomberg-ticker join, currently 31 of 191 pool securities, because only 32 of 89 research
folders carry a `bloomberg_ticker`. Symbols fix the sa join; that join key is a separate axis.
