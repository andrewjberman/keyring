# RESEARCH -- AMGT_RESAPP keying structure for a global IEFA universe

**From** `4.0.0_SA_CRO~Z`. **To** `1.0.0_SA_CTO~Z` (design fork, msg 24222). **Date** 2026-09-22 ~13:xxZ.
**Andrew's word:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_125xZ_AMGT_KEYING_STRUCTURE_IEFA_GLOBAL_BLOOMBERG_STABLE_KEY.md`
@`5c20841dd1`: *"keying off of Bloomberg's most stable key is probably the way to go"*; IEFA is global, so the key must be
*"foreign-friendly non-US from the start"*.
**Scope:** research plus a recommendation. Nothing was written to S3, no Terminal pull ran, no vendor was called.
**Every figure below is tagged MEASURED or INFERRED.**

---

## 0. The answer in one screen

- **Primary key: the composite FIGI** (Bloomberg field `COMPOSITE_ID_BB_GLOBAL`). It sits at the SAME grain as
  today's key: `<ROOT> <CC> Equity` is a Bloomberg composite ticker, and the composite FIGI is that composite line's
  permanent id. It is an open standard, never reused, unchanged by a ticker change, path-safe (`BBG` + 9 alphanumerics,
  never a `/`), and it exists for every Bloomberg-covered equity in any country. *Properties INFERRED from the public
  FIGI standard; not measured in this estate, see s.2.*
- **Fallbacks, in order,** for a name with no composite FIGI yet:
  1. exchange-level FIGI (`ID_BB_GLOBAL`), which resolves to its composite on the next Terminal pass;
  2. ISIN + listing country;
  3. SEDOL (7 characters, check digit validated) + listing country;
  4. local ticker + Bloomberg exchange code, marked PROVISIONAL.
  **CIK is never a key:** measured, it covers **2 of 23** non-US names in the live universe.
- **Attributes, never keys:** display ticker, Bloomberg composite ticker, share-class FIGI (to link cross-listings),
  `ID_BB_COMPANY` (issuer grouping), ISIN, SEDOL, CUSIP, LEI, CIK.
- **Slash rule:** not needed for the primary (a FIGI never carries `/`); **kept** for fallback 4 and for the display
  ticker, using the already-built slash-safe form (AMGT-rk-76).
- **IEFA coverage cannot be measured from the estate:** **no IEFA constituent file exists** in `opal-data-etfs` (0 of
  1,663 object keys) or anywhere else found. Measuring it needs ONE Terminal pull, sized in s.3, on Andrew's word.
- **Cut it now, not after the backfill:** re-keying is cheapest before any backfilled object exists. The re-key is
  "add the identity, re-partition the new grammar", not "rename `security_key` in 177 files" (s.4).

---

## 1. Estate patterns -- what the estate already keys securities on, and why (MEASURED)

| surface | key | evidence |
|---|---|---|
| **AMGT_RESAPP** | `security_key` = `<ROOT>_<CC>_Equity`, derived from the Bloomberg composite ticker; slash-safe form since rk-76 | `lib/research/identity/crosswalk.py` @`a8b0eb58b7`. The live crosswalk (`crosswalk/v1/2026-09-19.json`, 96 records) enumerates **6** key conventions: bare-root-pilot-key, security-hash-key, pack-key, model-key, bloomberg-identifier, bloomberg-identifier-with-equity-suffix. Its record fields carry NO FIGI, ISIN or SEDOL. |
| **The ETF plane** (`opal-data-etfs`, Opal's own books DIVZ/IDVZ/PFDE/PFOE) | **CUSIP**, with FIGI and SEDOL as shape-detected fallbacks | `lib/research/identity/positioning_chain.py:30-51` @`0a5064ded5`: precedence (1) CUSIP with a valid check digit, compiled to an ISIN, "161 of 164"; (2) FIGI-shaped `BBG`+9, "1"; (3) SEDOL + domicile, check digit validated, "1"; (4) Bloomberg security + name, never guessed. `gold/holding/date=2026-09-18/holding.parquet` (186 rows) columns: `ticker`, `cusip`, `domicile` and no ISIN/FIGI column. `silver/holdings/2026-09-21.parquet` (184 rows): `holding_ticker`, `cusip`, `id_kind`. |
| **Trade identifiers** | `<ROOT> US EQUITY` with isin/figi/sedol attributes | DynamoDB `trade-security-identifiers` (92 rows, per `positioning_chain.py:30-31`); a US-listing table |
| **The peer scanner** (`opal-data-portal-v2/json/security_scanner/latest/`) | one mixed `ticker` field | measured below; dated 2026-08-06, 47 days stale |
| **POSN / MDPF / client pipelines** | CUSIP / ISIN / SEDOL as vendor-delivered columns | ISIN or SEDOL occurs in 252 `.py` files under `data/`, `integrations/`, `infra/aws/lambda/`, mostly custodian feeds (Schwab, Orion, SmartX, BlackDiamond). None keys a global equity universe. |
| `lib/opal_naming.py` | no security-identity rule | the key grammar treats an entity as a partition `{entity}={id}` and refuses `/` in it; it does not choose the entity |
| **Rulings on security identity** | the estate's own precedence (above) | no LD record was found that picks a global security key; the only codified precedence is `positioning_chain`'s, which is US-centric by construction (CUSIP first) |

**The measured case that decides it, the peer scanner's EAFE universe** (the only foreign-developed population in the
estate, EFA-weighted `wt_efa`, as-of 2026-08-06, **660 names, 23 countries**; Japan 168, UK 63, France 53, Germany
51):

| the one `ticker` field holds | count | share |
|---|---|---|
| a 6-character SEDOL-shaped code (e.g. `B929F4`, `710306`) | 481 | 72.9% |
| a Japanese 4-digit local code (e.g. `7203`, `8306`) | 167 | 25.3% |
| other (US tickers `SPOT`, `TEVA`; an ISIN fragment `US066922477`) | 12 | 1.8% |

**No ISIN, FIGI, LEI or CIK field exists on any row** (the 10 fields are country, weights, industry, mkt value, name,
price, sector, ticker, values). So the estate's foreign population is keyed by three incompatible identifiers in one
column. `lib/research/peers/engine.py:486` already records the join failure this causes: *"sit under SEDOL-shaped
identifiers ('484628' is SAP SE)"*. This is the ticker-derived failure mode, live.

**CIK in the live AMGT universe** (`universe/v1/2026-09-16.json`, 250 names, MEASURED): `cik` populated on **11 of
168** US-keyed names, **2 of 23** non-US, **0 of 59** unkeyed. CIK is a US SEC identifier and cannot anchor an IEFA
key. This confirms Andrew's instinct against "CIK primary".

---

## 2. Bloomberg identifier stability (INFERRED from the public FIGI standard and Bloomberg field definitions)

**Not measured here:** the estate holds no FIGI history on which a stability test could run. A measured stability
test needs the pull in s.3 plus a corporate-action sample; the table states the published behaviour.

| candidate | grain | ticker change | re-listing / venue change | merger | share class | open? | path-safe? |
|---|---|---|---|---|---|---|---|
| **ticker-derived** `<ROOT>_<CC>_Equity` (today) | composite line | **CHANGES** | changes | changes | per ticker | n/a | **no** (`BP/ LN`, needs the slash rule) |
| **exchange FIGI** `ID_BB_GLOBAL` | one listing on one exchange | stable | a new venue is a NEW FIGI | survivor keeps its own, the target's retires | per class | yes (OpenFIGI) | yes |
| **composite FIGI** `COMPOSITE_ID_BB_GLOBAL` | one security in one COUNTRY (all that country's venues) | stable | stable across venues in the country | survivor's persists | per class | yes | yes |
| **share-class FIGI** `ID_BB_GLOBAL_SHARE_CLASS_LEVEL` | one share class, all countries | stable | stable | survivor's persists | exactly one class | yes | yes |
| `ID_BB_UNIQUE` | security (legacy, `EQ...`) | stable | stable | as above | per class | **no** (proprietary) | yes |
| `ID_BB_COMPANY` | ISSUER (integer) | stable | stable | **re-points or retires** | **collapses classes** | no | yes |

**The grain a research page needs** is one page per security with a primary listing. The first three rows are
security-level; `ID_BB_COMPANY` is issuer-level and collapses share classes, so it is the wrong grain for a key
(it stays an attribute for "same company" grouping).
- Exchange FIGI is too fine: a Japanese name trading on Tokyo and its PTS venues would split.
- Share-class FIGI is too coarse for a primary-listing page: it merges a name's home listing with its foreign
  secondary listings of the same class. That is useful for deduplication, but it loses "which listing is primary".
- **Composite FIGI matches today's key's grain exactly**, so the re-key changes identity without changing grain,
  and every existing per-security artifact maps one-to-one. **Most stable at the needed grain: the composite FIGI.**

---

## 3. Coverage over IEFA -- what can and cannot be measured

**MEASURED absence:** `opal-data-etfs` holds 1,663 objects under `bbg/`, `gold/`, `silver/`, `snapshots/`, `daily/`,
`config/` and `platinum/`. **0 object keys contain `iefa`**, and the plane's books are Opal's own four ETFs. The 24 repo
files that mention IEFA are client-holdings and classification code (IEFA held as a position), not a constituent list.
The closest population in the estate, the scanner's EAFE universe (s.1), is **EFA-weighted (660 names), not IEFA**.
IEFA tracks the broader MSCI EAFE IMI index, so it is a larger, small-cap-inclusive superset (INFERRED; roughly 2,600
constituents on iShares' public page, not measured).

**So every coverage number the ask lists needs one Terminal pull:**

| step | Bloomberg request | size |
|---|---|---|
| constituents | one reference request for IEFA's holdings (`IEFA US Equity`, fund-holdings bulk field) or the index members of MSCI EAFE IMI | 1 request, about 2,600 rows (INFERRED) |
| identifiers | one reference request over those securities for 12 fields: `COMPOSITE_ID_BB_GLOBAL`, `ID_BB_GLOBAL`, `ID_BB_GLOBAL_SHARE_CLASS_LEVEL`, `ID_BB_UNIQUE`, `ID_BB_COMPANY`, `ID_ISIN`, `ID_SEDOL1`, `LEGAL_ENTITY_IDENTIFIER`, `CENTRAL_INDEX_KEY_NUMBER`, `TICKER`, `EXCH_CODE`, `CNTRY_OF_DOMICILE` | about 2,600 x 12, roughly 31,000 data points, batched |

That is ONE Terminal session, under the two-phase budgeted sign-in in `integrations/bloomberg/READ_HERE.md`. **It needs
Andrew's word** (a Terminal pull), and its bronze lands under `C-BRONZE-AS-RECEIVED` form (a) with `received-form:
bbg-client-json`. Expected result, INFERRED and not measured:
- FIGI family ~100% for any Bloomberg-priced constituent;
- ISIN ~100%;
- SEDOL near-100% in developed markets;
- LEI high but below 100% (issuer registration);
- CIK low (only SEC registrants).

The pull is what turns this table into measured fact.

---

## 4. Re-key blast radius (MEASURED)

| surface | count | built from `security_key` how |
|---|---|---|
| backend code (`lib/research`, `lib/opal_data_harvest`, `integrations/bloomberg/research`, `integrations/seekingalpha`, `infra/aws/terraform/harvest`) | **1,406 occurrences in 135 files** (about 40 of them tests) | field, dict key, path segment; heaviest: `api/scoped_amgt.py` 143, `peers/engine.py` 58, `filings/batch.py` 49, `identity/crosswalk.py` 47, `management/enrich.py` 46, `filings/battery.py` 42 |
| portal (`portal/src` @`f22e369c`) | **275 occurrences in 42 files** (about half are `__harness__` fixtures) | route parameter, props, fixture file names (`execFixture.CSL_AU_Equity.json`) |
| IAM | `infra/aws/terraform/harvest/scoped-amgt-api.tf` (8) | prefixes, not per-key; unaffected by a value change |
| new-grammar S3 partitions, `security_key=` | bronze: bloomberg 110 + seeking-alpha 18; state: `filing_attempt` 180 | the entity partition |
| legacy served JSON paths, per-key folders | model_block 122, management 18, posture 33, peers 797, scores 66, drafting 12, packs 40 | the folder name; these move at the gold chain anyway (`C-FORMAT-SEQUENCE`) |
| silver parquet | `filing_source` 14 rows | a column |

**The consequence for the cut: do NOT rename `security_key` across 177 files.** Change what IDENTITY is, and let the
existing name become an attribute:
1. **The crosswalk gains the identity columns** (`composite_figi`, `figi`, `share_class_figi`, `bb_company`, `isin`,
   `sedol`, `lei`, `cik`) from the s.3 pull, plus the fallback ladder and a `key_basis` naming which rung resolved each
   name (the `positioning_chain` pattern, never guessed).
2. **The new-grammar entity partition becomes `composite_figi=<BBG...>`**, via `address()`. The H0-H6 writers take it
   from their generated constants, and the 128 bronze and 180 state objects are re-partitioned by lossless copy (they
   are the only objects in the new grammar). This is small, and nothing is backfilled yet.
3. **`security_key` stays**, as the display/lookup token and the portal route. The API resolves it to the FIGI through
   the crosswalk. The portal's 275 uses do not move.
4. **The legacy served folders re-key when the gold chain re-homes them** (already planned), so they carry no second
   migration.

---

## 5. Recommendation

| item | recommendation |
|---|---|
| primary key | **composite FIGI (`COMPOSITE_ID_BB_GLOBAL`)**: Bloomberg's most stable key at the page's grain, open, permanent, path-safe, global |
| fallback 1 | exchange FIGI (`ID_BB_GLOBAL`), resolved to its composite on the next pass |
| fallback 2 | ISIN + listing country (ISIN alone is share-class-level and would merge listings) |
| fallback 3 | SEDOL (check digit validated) + listing country; covers 72.9% of the estate's EAFE scanner as delivered |
| fallback 4 | local ticker + exchange code, PROVISIONAL, slash-safe; covers the Japanese 4-digit codes (25.3%) until a pull resolves them |
| never a key | CIK (2 of 23 non-US), `ID_BB_COMPANY` (issuer grain), ticker (changes) |
| attributes | display ticker, composite ticker, share-class FIGI (cross-listing link), `ID_BB_COMPANY`, ISIN, SEDOL, CUSIP, LEI, CIK |
| slash rule | not needed for FIGI; keep it for fallback 4 and display (rk-76's form) |
| precondition | ONE Terminal pull of IEFA constituents x 12 identifier fields, on Andrew's word. It measures coverage and seeds the crosswalk in the same act |
| sequencing | before any backfill; re-partition only the 308 new-grammar objects; legacy folders ride the gold chain |

**The one design call for Andrew,** beyond the pull: composite FIGI (one page per country listing) versus share-class
FIGI (one page per share class, merging a company's home and foreign listings of the same class). This research
recommends composite, because it preserves today's grain and the primary-listing notion. Share-class FIGI is the
alternative if he wants one page per company regardless of where it lists.
