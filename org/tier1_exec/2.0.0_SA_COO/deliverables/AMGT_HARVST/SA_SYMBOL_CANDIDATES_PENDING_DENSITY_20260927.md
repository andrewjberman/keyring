# sa_symbol: 18 CANDIDATES across 9 folders that passed test (a) and never reached test (b)

> # SUPERSEDED 2026-09-27 -- DO NOT PROBE THESE. ALL 9 FOLDERS NOW CARRY A MEASURED SYMBOL.
>
> Andrew read every remaining security's Seeking Alpha page by hand and supplied the symbols
> (`SA_SYMBOLS_ANDREW_20260927.json`, 33 records, status `MEASURED`). The merged source
> `SA_SYMBOLS_MERGED_89_20260927.json` is wired at `lib/opal_data_harvest/config.json`
> (`symbol_resolution_source`, @d2be2d3b13) and the producer's own read is **89 of 89 with 0 missing**.
>
> **MEASURED 9 of 9:** Nestle->`NSRGY`, Nike->`NKE`, Novartis->`NVS`, Rio Tinto->`RTPPF`, Roche->`RHHBY`,
> Sanofi->`SNY`, Shopify->`SHOP`, QXO->`QXO.PR.B`, Orange->`ORANY`. A later seat re-probing these 18
> candidates would spend 9 vendor searches to re-derive answers already held at a STRONGER provenance --
> a human read of the vendor's own symbol page, versus this file's two-readings-of-one-source.
>
> **WHAT SURVIVES AND IS WORTH KEEPING:** the section below on `OBT` is the reason this file exists. A
> flagged candidate sitting in a column that reads as answers got picked up and supplied back to me as
> real. That is a lesson about artifact design, and it is mine; it does not age with the symbols.
> The `QXO.PR.B` density watch also survives -- serveability is the >=3-mentions-in-30-days bar, and the
> preferred line may not clear it. That is still a measurement nobody has made.

**Measured 2026-09-27 from `sa_symbol_pass_20260926/batch16.json`** (the live population: universe 89, ASKED
69, resolved 56, serveable 19). Every row below comes from that artifact's own `candidates_probed`, which
records each probed symbol with SA's own company name, the name overlap, and the news call's HTTP code.

**No vendor call was made to produce this file.** It is a read of evidence already on disk.

---

## ⛔ THESE ARE CANDIDATES, NOT IDENTIFICATIONS, AND ONE ROW BELOW PROVES WHY

I previously described these as *"symbols ALREADY identified at name_overlap 1.0"*. **That overstated it and
this file is the correction.** The pass accepts a symbol only when BOTH hold:

- **(a)** SA's own company name for the symbol shares a distinctive token with the subject company, AND
- **(b)** the returned article TITLES tie to the subject company.

**Every row here passed (a) at overlap 1.0 and NEVER REACHED (b)** -- the news call that would supply the
titles returned HTTP 403. So (b) is not failed; it is unrun.

⭐ **THE LIVE PROOF THAT (a) ALONE IS WORTHLESS IS `Orange ORA FP`.** It probed two candidates, both at
overlap **1.0**:

| symbol | SA's own company name | overlap |
|---|---|---|
| `ORANY` | Orange S.A. | 1.0 |
| **`OBT`** | **Orange County Bancorp, Inc.** | **1.0** |

`OBT` is a DIFFERENT COMPANY. It scores a perfect name overlap because it shares the distinctive token
"orange". **That is exactly the failure the pass's s.18 doctrine was written for** -- *"'ROG' returns HTTP
200 with 50 well-formed records spanning three years, and it is ROGERS CORPORATION, not Roche. A 200 with
fifty clean records is NOT evidence of the right company."* Here the same trap appears one axis over, and
**only test (b) discriminates it.** Had I written these into the universe as resolved symbols, Orange would
have been filed against a small US bank.

## A SECOND CLASS THE TITLES ALSO HAVE TO SETTLE: WHICH LINE, NOT WHICH COMPANY

Seven of the nine folders probed TWO candidates of the SAME issuer, and they are not interchangeable:

| folder | candidates at overlap 1.0 | what separates them |
|---|---|---|
| Nestle NESN SW | `NSRGF`, `NSRGY` | two OTC/ADR lines of Nestle S.A. |
| Nike NKE US | `NKE`, `NKE:CA` | US listing vs a Canadian line |
| Novartis NOVN SW | `NVS`, `NVSEF` | ADR vs OTC ordinary |
| Rio Tinto RIO LN | `RIO`, `RTPPF` | ADR vs OTC ordinary |
| Roche ROG SW | `RHHBY`, `RHHBF` | ADR vs OTC ordinary |
| Sanofi SAN FP | `SNY`, `SNYNF` | ADR vs OTC ordinary |
| Shopify SHOP CA | `SHOP`, `SHOP:CA` | US listing vs Canadian line |
| QXO | `QXO`, **`QXO.PR.B`** | the COMMON vs a **5.50 DEPOSITARY PREFERRED** |
| Orange ORA FP | `ORANY`, **`OBT`** | **a different company** (above) |

⚠ **`QXO.PR.B` is a preferred share, not the common.** A density measurement might separate the two by
article volume, but the honest discriminator here is a SHARE-CLASS rule, which this pass does not have.
**Chatter for a company should not be filed against its depositary preferred.**

## THE 18 CANDIDATES

| folder | symbol | SA company name | overlap | news HTTP |
|---|---|---|---|---|
| Nestle NESN SW | NSRGF | Nestle S.A. | 1.0 | 403 |
| Nestle NESN SW | NSRGY | Nestle S.A. | 1.0 | 403 |
| Nike NKE US | NKE | NIKE, Inc. | 1.0 | 403 |
| Nike NKE US | NKE:CA | NIKE, Inc. | 1.0 | 403 |
| Novartis NOVN SW | NVS | Novartis AG | 1.0 | 403 |
| Novartis NOVN SW | NVSEF | Novartis AG | 1.0 | 403 |
| Orange ORA FP | OBT | Orange County Bancorp, Inc. | 1.0 | 403 |
| Orange ORA FP | ORANY | Orange S.A. | 1.0 | 403 |
| QXO | QXO | QXO, Inc. | 1.0 | 403 |
| QXO | QXO.PR.B | QXO, Inc. 5.50 DEP PFD | 1.0 | 403 |
| Rio Tinto RIO LN | RIO | Rio Tinto Group | 1.0 | 403 |
| Rio Tinto RIO LN | RTPPF | Rio Tinto Group | 1.0 | 403 |
| Roche ROG SW | RHHBF | Roche Holding AG | 1.0 | 403 |
| Roche ROG SW | RHHBY | Roche Holding AG | 1.0 | 403 |
| Sanofi SAN FP | SNY | Sanofi | 1.0 | 403 |
| Sanofi SAN FP | SNYNF | Sanofi | 1.0 | 403 |
| Shopify SHOP CA | SHOP | Shopify Inc. | 1.0 | 403 |
| Shopify SHOP CA | SHOP:CA | Shopify Inc. | 1.0 | 403 |

## WHAT THIS BUYS, STATED WITHOUT INFLATION

**It does NOT resolve anything.** What it does is make the remaining work TARGETED: a later pass can go
straight to these 18 symbols' news endpoints and skip 9 searches, because the search half already succeeded
and its result is recorded here. At the measured cost of roughly one resolved name per six attempts, 9 saved
searches is real rate-limit headroom and nothing more.

⛔ **NOTHING HERE MAY BE WRITTEN INTO A UNIVERSE AS A RESOLVED `sa_symbol`.** Test (b) is unrun, `Orange`
shows what that costs, and `sa_symbol` is the field the gold builder's sa join now depends on
(`publication_gold._listing_hit_query_identifiers`, `4cc54df506`) -- so a wrong value here files another
company's chatter against ours. **The rule that refuses a best guess is the only reason this file is a
finding rather than a mistake.**
