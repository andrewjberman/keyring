# C -- FILINGS, ISSUER SITE / IR, ESEF, AND TRANSLATION: field-level map

Branch SITEZ @78106b9cea. Read-only. S3 reads made 2026-09-22 through `.tools/aws` (bucket `opal-data-harvest` unless
named). Code citations are `file:line` at this checkout. Bronze skeletons verified against, and built on, the CRO's two
inventories: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESAPP_DATA_SHAPE_INVENTORY_20260918.md` s.2 items 4-7 (the
09-18 vintage, before the M2 move) and `.../PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` s.5.2-5.3. What is new here:
the post-M2 silver `filing_source` (24 columns, read from the live parquet), the translation method against the
contracts, and the per-component trace.

## 0. Live object census (measured 2026-09-22, `s3 ls --recursive | wc -l`)

| prefix | objects | what is there |
|---|---|---|
| `sec/harvest/bronze/filing/` | **0** | nothing (also 0 under the same prefix in `opal-data-assets`) |
| `sec/harvest/bronze/company_tickers/` | **0** | nothing |
| `sec/harvest/silver/filing_source/` | 1 | `date=2026-09-22/part-20260922T033157Z.parquet`, 808,344 B, **13 rows** |
| `issuer-site/harvest/bronze/document/` | **0** | nothing (the Keyence PDF is stored nowhere) |
| `issuer-site/harvest/silver/filing_source/` | 1 | same stamp, 283,596 B, **1 row** (6861_JP_Equity, Keyence) |
| `filings-xbrl/harvest/` | **0** | nothing, in either bucket |
| `amgt/harvest/state/filing_attempt/` | 180 | one `security_key=<k>/UNRESOLVED-SOURCE.json` per name |
| `filings/v1/` (legacy) | 206 | 194 `.source.json` (180 UNRESOLVED + 13 EDGAR + 1 Keyence) and 12 `.analysis.json` |
| `drafting/v1/` (legacy served) | 12 | one `<security_key>.json` per analyzed name |

The 12 analyzed names: ASML, BABA, BA, COST, HAL, HD, INTU, KMB, NU, PBR, SAP_GY, VLO. CAT (source only) and Keyence
(source only) have **no** analysis and **no** drafting object in S3.

---

## CHANNEL 1 -- SEC EDGAR (submissions JSON, primary document, ticker table)

### 1.1 Channel
- **Vendor:** SEC EDGAR over HTTPS, `urllib` GET with the SEC fair-access User-Agent (`lib/research/filings/fetch.py:100-113`,
  UA constant `:73`, which carries a contact e-mail -- not quoted here).
- **Endpoints:** `https://data.sec.gov/submissions/CIK%010d.json` (`fetch.py:75`); archive document
  `https://www.sec.gov/Archives/edgar/data/<cik>/<acc>/<primary>` (`:76`); ticker table
  `https://www.sec.gov/files/company_tickers.json` (`battery.py:563`).
- **Two code paths reach EDGAR:**
  1. **EDGAR-by-CIK** (old single path): `fetch.build_source_object(security_key, cik, form)` (`fetch.py:346-469`), driven by
     `filings/batch.py:403` from the universe row's `filing_identity {cik, form_expected}`. The batch uses this path ONLY; it
     never calls the battery.
  2. **The battery**, steps 1-2 (`battery.py:685-793`): step 1 matches `ticker_root` against the LIVE ticker table, with a
     name guard (`_entity_test` against the SEC `title`, `:722`); step 2 uses Bloomberg's `CENTRAL_INDEX_KEY_NUMBER`. Each
     tries the domicile-preferred form (US: 10-K then 20-F; else 20-F then 10-K; `:66-73`, `:604-621`).
- **Form selection:** the most recent filing whose `form` equals EXACTLY `10-K` or `20-F` in `filings.recent`
  (`fetch.py:137-140`); `10-K/A` never matches.
- **Trigger / cadence today:** manual CLI only. `python -m lib.research.filings.batch` behind the Windows task
  `OpalResearch-FilingsAnalyzer`, weekly Sunday 06:00, **created DISABLED** (`batch.py:6-19`, `:40`, `:48-69`);
  `python -m lib.research.filings.battery --security-key ...` for the battery. Bronze is written only with the opt-in
  `--write-bronze` flag (`battery.py:1393-1396`, `batch.py:509-512`); silver/state only with `--write-pool`.

### 1.2 Storage (in order)
| layer | key pattern | live |
|---|---|---|
| bronze, document (form b) | `sec/harvest/bronze/filing/cik=<10 digits>/<accession>/<vendor file name>` (`harvest/filings.py:101-121`) | 0 |
| bronze, ticker table (form c) | `sec/harvest/bronze/company_tickers/date=YYYY-MM-DD/company_tickers.json` (`:156-162`, name from `fetch.py:68`) | 0 |
| silver | `sec/harvest/silver/filing_source/date=<fetch date>/part-<stamp>.parquet`, record key `(security_key, accession)` (`:230-248`) | 1 part, 13 rows |
| state (failures) | `amgt/harvest/state/filing_attempt/security_key=<k>/UNRESOLVED-SOURCE.json`, write-once (`:315-408`) | 180 |
| legacy served (gold) | `filings/v1/<security_key>/<accession>.analysis.json` (`analyze.py:1524-1525`, via `fetch.pool_key`) | 12 |
| legacy served (gold) | `drafting/v1/<security_key>.json` (`analyze.py:1526`) | 12 |
| legacy source (retired) | `filings/v1/<security_key>/<accession>.source.json` -- still present, 194 objects | 194 |
| DynamoDB | none found for filings | -- |

### 1.3 Field dictionary

**Bronze (as received, 0 objects live -- shape is the vendor's):** the submissions JSON is read in memory only, never
persisted. Fields the code reads from it: `name`, `website`, `investorWebsite`, `lei`, `filings.recent.{form[],
accessionNumber[], primaryDocument[], filingDate[], reportDate[]}` (`fetch.py:131-170`). The primary document is the raw
HTML/iXBRL bytes (or a PDF, sniffed by `%PDF`, `fetch.py:231-233`). The ticker table is `{"<i>": {cik_str: int, ticker:
str, title: str}}` (read at `battery.py:709-733`; 10,438 rows on the live reads recorded in state objects).

**Silver `filing_source` -- the 24 columns, read from the live parquet** (writer `harvest/filings.py:84-90`, `:189-204`;
lineage columns from `harvest/store.py:38`):

| column | type (arrow) | null? | example shape | meaning |
|---|---|---|---|---|
| `security_key` | string | no | `"SAP_GY_Equity"` | ticker-derived key; half of the record key |
| `status` | string | no | `"RESOLVED"` | only RESOLVED reaches silver (`:169-175`) |
| `accession` | string | no (sec) | `"000110465926020058"` (18) | dashless accession; half of the record key |
| `accession_raw` | string | yes | `"0001104659-26-020058"` | dashed form |
| `form` | string | yes | `"20-F"` | EDGAR form |
| `family` | string | **12 of 13 null** | `"10-K"` | cutter family; set only by the battery path (CAT only) |
| `language` | string | **12 of 13 null** | `"en"` | `document.detect_language` code; CAT only |
| `entity_name` | string | yes | str(15) | SEC `name` |
| `filing_date` | string | yes | `"2026-02-26"` | |
| `period_end` | string | **12 of 13 null** | `"2025-12-31"` | EDGAR `reportDate`; battery path only |
| `url` | string | yes | str(83) | archive URL of the primary document |
| `primary_document` | string | yes | `"sap-20251231x20f.htm"` | the vendor file name |
| `retrieved_at` | string | no | `"2026-09-17T02:29:52Z"` | the real fetch time |
| `parser_version` | string | no | `"opal-filings-fetch/1.0.0"` or `/2.0.0` | |
| `document_bytes` | int64 | yes | `24864615` | size of the primary document as served |
| `document_sha256` | string | yes | str(64) | sha256 of the document bytes -- **the bytes are stored nowhere** |
| `document_text_chars` | int64 | yes | `1374962` | length after `html_to_text` |
| `verified_site_reason` | string | yes | str | why `verified_site` is null |
| `reason` | null type | always null | -- | UNRESOLVED reason; never set on a RESOLVED row |
| `object_keys` | string (JSON list) | no | `["accession",...]` | the absent-vs-null carrier |
| `object_json` | string (JSON) | no | ~70-200 KB | **the whole source object, lossless** -- every nested field below lives only here |
| `bronze_key` | string | no | `"filings/v1/SAP_GY_Equity/000110465926020058.source.json"` | lineage pointer: the LEGACY `.source.json` key (M2 move, `harvest/filings.py:503`), not a bronze key |
| `fetched_at` | timestamp[us, UTC] | no | `2026-09-22 03:31:57Z` | **the M2 MOVE time** (`:499`, `:505`), not the fetch time |
| `record_hash` | string | no | sha256 | added by `store.silver_append` (`store.py:361-368`) |

**Nested fields inside `object_json`** (the source object; `fetch.py:401-469` EDGAR path, `:286-343` battery path):
- `filing_identity`: `{source: "edgar", cik: int, form_expected: str}` (EDGAR path) or `{source: "battery", step: int,
  route: str, key: str}` (battery).
- `excerpt`: `{items: list[str] (item labels), item_keys: list[str] ("risk","mdna"), text: str (up to ~150K chars, the
  raw cut text), chars: int, excerpt_sha256: str(64), truncated_items: list[str], item_chars: {risk: int, mdna: int},
  item_full_chars: {...}}`. Caps: risk 70,000, mdna 80,000, officers 40,000 chars (`document.py:69`).
- `officer_section`: `{status: "OK"|"FAILED", item: str, text: str, chars: int, sha256: str|null, extracted: false,
  extraction_owner: "AMGT-rj-8", reason?: str}`. **12 of 13 live rows are the pre-rk-39 shape with NO `status` key**, and
  2 of them (ASML, PBR) have `chars: 0`, the D9/E10 defect `fetch.py:442-446` describes.
- battery path only: `battery {order[5], attempts[], winner}`, `entity_evidence`, `verified_site {host, url_root, step,
  source, evidence}`, `family`, `language`, `period_end`.
- Measured per row: excerpt items are `[risk, mdna]` for 11 names, `[risk]` only for ASML and PBR (mdna cut FAILED),
  `[mdna]` only for HAL. Officer section chars range 0 to 40,000 (capped).

**Which 10-K / 20-F items are extracted** (`document.py:632-684`, `fetch.py:89`):
| key | 10-K | 20-F | in the analyzed excerpt? |
|---|---|---|---|
| `risk` | Item 1A Risk Factors (ends at 1B / Item 2) | Item 3.D Risk Factors | yes |
| `mdna` | Item 7 MD&A (ends at 7A / Item 8) | Item 5 Operating and Financial Review and Prospects | yes |
| `officers` | Item 10 Directors, Executive Officers and Corporate Governance, or "Information about our Executive Officers" | Item 6 Directors, Senior Management and Employees | **no** (persisted separately as `officer_section`) |
**NOT extracted:** Item 1 Business, Item 1C Cybersecurity, Item 7A, Item 8 financial statements, Item 11 compensation,
20-F Item 4 (Information on the Company). No numeric table is cut; segment revenue reaches the page only as model prose
(`scoped_amgt.py:2086-2090`). `roster.py:457-478` can follow an officer "pointer" to another item only if that item's text
is already held in the object, which for EDGAR it never is.

**State `filing_attempt` (180 objects):** 178 are the OLD single-path marker, 422-426 B, keys `security_key, status,
reason, filing_identity{source:"none"}, retrieved_at, parser_version "opal-filings-fetch/1.0.0", accession, form, url,
document_sha256, excerpt, officer_section` all null (sample `security_key=2317_TT_Equity`, reason *"filing_identity.source
is 'none': no cik and expected form to fetch by"*). **Only 2 carry a battery run:** `CSL_AU_Equity` (4,488 B) and
`6861_JP_Equity` (3,224 B), with `battery.attempts[] = {step, route, key, url, http_status, document_sha256, tests,
language, reason, seconds, seed_sources}`. CSL: step 1 name guard refused (the ticker CSL is Carlisle), step 2 CIK found
but no 10-K/20-F, step 3 ESEF 404, step 4 crawl cap of 40 pages hit with 292 queued and 0 candidates, step 5 no adapter.
**Keyence carries BOTH a 09-19 UNRESOLVED state marker and a RESOLVED issuer-site silver row** (the later run won; the
state object is write-once, so it was never cleared).

**Legacy analysis `filings/v1/<k>/<acc>.analysis.json`** (sample SAP_GY_Equity; skeleton as in the CRO inventory item 6):
`security_key, accession, form, filing_date, source{url, document_sha256, excerpt_sha256, retrieved_at, parser_version,
excerpt_items, excerpt_chars, pool_key}, model "claude-opus-5", analyzer_version "opal-filings-analyze/1.0.0",
prompt_version "rj6-two-pass/1", passage_map[] {id "P0001", start, end, chars, location, text, ascii_replacements},
items{guidance, segments, risks, commentary, big_bets, big_challenges}[] {text, evidence_ids[]}, held_uncited[] {class,
reason, tag, text}, thesis_driver {series, unit, why, source_passage_id, resolution}, thesis_driver_record, citations[]
{cited_text, passage_ids, resolved, shape, span, tag}, denominators{...}, passes{pass_1, pass_2}, usage{...},
ascii_normalisation {applied, rule, characters_replaced_in_items, characters_replaced_in_passages}, pass_1_text,
generated`. **No `language` and no `translation` key on the served SAP analysis**, and its passages are ASCII-FOLDED
(the pre-rk-40 rule). Analyzer today is `2.1.0` / `rj6-two-pass/3` (`analyze.py:68`, `:80`); the served objects predate it.

**Legacy drafting `drafting/v1/<k>.json`** (sample SAP): `sections[5] {section, sentences[] {text, generated,
evidence[], quoted_spans[], quote_method, item_class, verbatim_check}, absent?}`, `evidence_records[] {id, passage,
source{accession, document_sha256, excerpt_sha256, location}}`, `thesis_driver`, `denominators`, `dropped`,
`dropped_reasons`. Five sections from `drafting_build.py:66-72`: `company_description` (segments+commentary),
`investment_thesis` (big_bets+commentary), `risks` (risks+big_challenges), `ceo_bio` (always ABSENT, owner AMGT-rj-8),
`recommendation` (guidance).

### 1.4 Transformations
- bronze -> in-memory text: `html_to_text` drops script/style/tags, unescapes entities, collapses whitespace
  (`fetch.py:173-190`); PDFs through `document.pdf_to_text` (`battery.py:1071-1073`).
- text -> sections: `document.cut(text, family)` (`document.py:715-744`); a key under 1,500 chars or unmatched is
  `FAILED` with a reason (`:67`, `:720-724`).
- sections -> excerpt: risk + mdna only on EDGAR (`fetch.py:383-400`); `document.sections_to_excerpt` for other families
  joins risk + mdna + **officers** (`document.py:747-784`) -- so a Yuho excerpt carries the officer table, an EDGAR one
  does not.
- source -> analysis: **model call** `analyze.anthropic_call` (`analyze.py:321-345`), model `claude-opus-5` (`:60`),
  two passes: pass 1 with API citations ON (prose), pass 2 JSON over pass 1's text (`analyze.py:9-21`). Six item classes
  (`:131`) plus a thesis driver; uncited items are HELD.
- analysis -> drafting: `drafting_build.draft()` (`drafting_build.py:281-319`), no model call; verbatim gate against the
  cited passage; a sentence with no verbatim run is HELD.
- source -> silver: `fetch.persist` (`fetch.py:482-519`) -- RESOLVED to silver, UNRESOLVED to state. **Only the
  battery CLI calls it** (`battery.py:1360`). `batch.run_group` writes UNRESOLVED to state (`batch.py:405-414`) and the
  analysis + drafting via `write_outputs` (`:435`), but **never persists a RESOLVED source object** -- `write_outputs`
  stopped writing it at M2 (`analyze.py:1514-1520`) and no caller in `batch.py` or `analyze.main` took the job over
  (INFERRED from the absence of any `persist(` call outside `fetch.py`/`battery.py`). A live `batch --write-pool` run
  would land analyses whose cited source has no silver row.

### 1.5 Component map
| component | fields read | API side | portal side |
|---|---|---|---|
| **Thesis** (primary) | `drafting/v1`: `sections[].sentences[].{text, generated, evidence, verbatim_check, quoted_spans}`, evidence passage text, `thesis_driver`, `held_uncited`, provenance `{accession, form, filing_date, source.document_sha256, model, analyzer_version, dropped}` | `read_drafted_sections` `lib/research/api/scoped_amgt.py:1627-1692` (sentence rebuild `:1661-1671`), block `:1592-1624`, merged in `read_thesis_bundle` `:2043`; UNRESOLVED reason from state `:1954-1981`, `:2052-2055`; `as_of_date` `:2064`; route `/security/{key}/thesis` `:3867-3868` | `portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx:145-216` (status `:182-188`, driver `:191-196`, provenance `:201-206`, sections `:210-215`); types `types.ts:582-601` |
| **Thesis "big thing" chart** | `thesis_driver.{series, unit, points, source_passage_id}` joined to the model block's fiscal figures | `thesis_driver_chart` `scoped_amgt.py:2066`, `:2076-` | `components/ThesisDriverChart.tsx`, mounted `ThesisTab.tsx:165` |
| **Header description** (the page header above the tabs; not the Lead Panel list) | `company_description` sentence 1 when Bloomberg's description mnemonic is absent | `read_description` `scoped_amgt.py:2967-2990` on the overlay payload `:1943` | `components/HeaderBrief.tsx:41-55`, `:129` |
| **Exec Mgmt** | `officer_section.{item, text}` from `filing_source` silver, parsed OFFLINE into `management/v1` | builder `lib/research/management/roster.py:1085-1149` (silver read), `:1206-1234` (parse); served by `read_management` `scoped_amgt.py:2507`, `:2067` | `tabs/ExecManagementTab.tsx:154`, `:161-190`, `:229-230` (`source_item`, officers, the Bloomberg-fallback label) |
| **Lead Panel list** | NONE | -- | `components/LeadPanel.tsx` reads no filings field |
| **Peers** | NONE | -- | -- |
| **Model** | NONE directly (the Model tab reads the model block, `ModelTab.tsx:10`); the filing's thesis driver is joined to Model figures on the Thesis tab only | -- | -- |
| silver `filing_source` / state | NOT read by any API route except the state `reason` (above); the page reads the legacy `drafting/v1` gold | `_read_filing_source_object` `scoped_amgt.py:1954` | -- |

### 1.6 Gaps and hazards
- **Bronze retention is not happening.** 0 bronze objects on all three filings channels. `document_sha256` points at bytes
  kept nowhere, so no parse can be re-run (the CRO plan s.5.2 called this the one change that cannot wait).
- **Silver lineage is fake-ish.** `bronze_key` = the legacy `.source.json` key; `fetched_at` = the move time, and the
  `date=` partition is the move date (09-22), not the 09-15..09-19 fetch dates. C-SILVER-PARQUET wants the fetch date.
- **12 of 13 SEC rows predate the battery:** `family`, `language`, `period_end`, `battery`, `verified_site` are absent,
  and `officer_section` has no `status`.
- **Keying.** Silver record key and state partition are the ticker-derived `security_key`; bronze is keyed by CIK
  (entity-stable). Two listings on one CIK share one analysis written under each key (`batch.py:432-436`). A composite-FIGI
  re-key must rewrite silver, state and the legacy prefixes; the SEC bronze keying survives it.
- **CUSIP-free/ADR hazards:** the ticker guard refuses a foreign ticker that collides with a US one (CSL -> Carlisle,
  measured in state). Step 1 only matches `ticker_root`, so every non-US ordinary share falls to step 2 (needs a
  Bloomberg CIK, which only SEC registrants have).
- **Item 1 Business is never cut**, so the business description the Thesis/header needs comes only from MD&A/segments
  prose.
- **Stale analyses:** the sampled served analysis (SAP) carries analyzer 1.0.0 contracts (ASCII-folded passages, no
  language field); the other 11 were written 09-16/17, before the rk-40 contract, and were not opened -- consistent with the PRD's "stale analyses stay stale" (`AMGT_RESAPP_PRD.md:782-784`).

---

## CHANNEL 2 -- ISSUER SITE / INVESTOR RELATIONS (battery step 4) and other company-document ingestion

### 2.1 Channel
- **Mechanism:** a bounded, priority-queue HTTP crawl of the company's own site, `battery._step4_company_site`
  (`lib/research/filings/battery.py:974-1185`). No browser, no search engine: the SERP seam `search_fn` is declared and
  NOT wired (`battery.py:1251-1253`).
- **How it finds the IR site -- seeds, in try order** (`:976-988`): (1) Bloomberg `COMPANY_WEB_ADDRESS`
  (`keys["web_address"]`); (2) EDGAR submissions `website` / `investorWebsite`, only if step 1 or 2 read a submissions
  payload; (3) the exchange listing page from `EXCHANGE_LISTING_PAGES` -- **one entry, ASX only**
  (`https://www.asx.com.au/markets/company/{ticker_root}`, `:93-95`).
- **Crawl rules:** max 40 pages, depth 3, 2 s delay, 25 MB document cap (`:974-975`). Priority 0 = a link whose URL or
  anchor matches the annual-report vocabulary (`annual report`, `annual securities report`, `statutory`, `10-K`, `20-F`,
  `integrated report`, the Yuho title; `:101-109`, `:232-240`); 1 = an IR-looking page (`investor`, `ir/`,
  `shareholder`, `finance`, `financial`, `library`; `:219-229`); 2 = other allowed pages. Host allow rule: seed host,
  same registrable domain, host containing the seed label, or a host containing `investor` / `ir` (`:193-207`); the
  public-suffix list is 16 hard-coded entries (`:121-125`). A bare `.pdf` with no vocabulary match is never a candidate
  (`:238-239`).
- **Accepted document:** any candidate or PDF that passes the ONE acceptance test (`:386-430`): (a) the normalized legal
  name is a substring of the first 8,000 characters, and a 20-char LEI found there must equal Bloomberg's; (b) period end
  within 18 months; (c) `document.detect_family` returns a known family AND `cut()` gets at least one item OK.
  Families: `10-K`, `20-F`, `ANNUAL-REPORT` (headline "Annual Report" + one of "Directors' Report" [curly apostrophe
  only], "Financial Report", "Operating and Financial Review", "Remuneration Report"), `YUHO` (the Japanese title)
  (`document.py:60`, `:263-307`).
- **Navigation pages are never stored** (`battery.py:1061-1066`). Every candidate document tried -- winner or loser --
  goes to bronze when `--write-bronze` is set.
- **Document id:** `doc-` + the first 16 hex of sha256(document bytes) (`battery.py:1068`, `:1169`). The CRO plan
  proposed hashing the canonical URL instead (`PLAN_..._20260921.md` s.5.3); the code hashes the BYTES.
- **`verified_site`:** the winning document's host, unless its registrable domain is an exchange's, then null with a
  reason (`:1151-1166`). On an EDGAR win it is the submissions `investorWebsite`, else `website` (`:815-830`).
- **Trigger:** manual battery CLI only; resumable per step and per crawl via `--cache-dir` (`:917-935`, `:1220-1241`).

### 2.2 Storage
| layer | key | live |
|---|---|---|
| bronze (form b) | `issuer-site/harvest/bronze/document/security_key=<slash-safe k>/doc-<sha16>/<vendor file name>` (`harvest/filings.py:131-137`; file name = last URL path segment, `battery.py:966-971`) | 0 |
| silver | `issuer-site/harvest/silver/filing_source/date=.../part-*.parquet` -- the SAME 24 columns as SEC | 1 row |
| state | shared `amgt/harvest/state/filing_attempt/` | (Keyence's stale marker) |
| legacy | `filings/v1/6861_JP_Equity/doc-1defdb68a7ffd3b7.source.json` (965,303 B) | 1 |
| analysis / drafting in S3 | none for Keyence | 0 |

### 2.3 Field dictionary -- the one live issuer-site record (Keyence, from the silver parquet)
Typed columns: `security_key "6861_JP_Equity"`, `status RESOLVED`, `accession "doc-1defdb68a7ffd3b7"` (the document id
reused as the accession half of the record key), `accession_raw / form / filing_date / primary_document` null (arrow type
`null`), `family "YUHO"`, `language "ja"`, `entity_name` str(12), `period_end "2026-03-20"`, `url` = the PDF URL on the
issuer's `.co.jp` host (str 66), `document_bytes 940557`, `document_text_chars 72775`, `parser_version
"opal-filings-fetch/2.0.0"`. Nested in `object_json`: `filing_identity {source "battery", step 4, route "company-site",
key <the PDF URL>}`, `battery.attempts[4]` (step 1 ticker `6861` not in the 10,438-row table; step 2 Bloomberg CIK
field BAD_FLD; step 3 ESEF 404; step 4 passed), `entity_evidence` ("legal name ... matched on the cover; LEI absent from
the document"), `verified_site {host, url_root, step 4, source "winning-document-host", evidence}`, `excerpt {items: the
three Yuho headings in Japanese, item_keys [risk, mdna, officers], item_chars {risk 3592, mdna 57002, officers 40000},
truncated_items [officers], text str(100623)}`, **`officer_section: null`**.

### 2.4 Transformations
PDF bytes -> `document.pdf_to_text` (PyMuPDF reflow) -> `detect_family` / `cut` -> `sections_to_excerpt` (risk, mdna,
officers) -> `build_battery_source_object` (`fetch.py:286-343`). The step-4 winner hard-codes `officer_section: None`
(`battery.py:1182`) even though `cut()` produced an OK officers section.

### 2.5 Component map
- **Thesis:** would be the same path as channel 1 -- but Keyence has no analysis or drafting in S3, so the page serves
  ABSENT for it today.
- **Exec Mgmt:** **NONE from the issuer document.** `roster.py:1211-1217` reads `officer_section`, which is null for every
  step-4 winner, so the roster falls to the Bloomberg `COMPANY_EXEC_OFFICERS` fallback -- which is what rk-106 measured
  on 6861 (commit `2aa734b2d6`). The Yuho officer-table parser exists (`roster.py:904-1000`) and is unreachable from
  this route.
- `verified_site.host` feeds the management / Lusha domain work (other channel map); no page component reads it.
- Lead Panel, Peers, Model: NONE.

### 2.6 How ad hoc it is -- and every other company-document ingestion found
- The crawl is generic code, but its reach is set by hard-coded lists: ONE exchange (ASX), 16 public suffixes, English
  + one Japanese title in the vocabulary, four English annual-report markers. It has been exercised on 3 names (CAT,
  CSL, Keyence); CSL fails (crawl cap), Keyence passes.
- **No press-release, newsroom, RSS or blog ingestion exists for this app** (searched `lib/`, `integrations/`,
  `infra/aws/lambda/`, `data/` for press release / newsroom / investorWebsite / issuer-site / blog / rss). The only
  other IR artifact is `lib/research/coverage/ir_scan.py:1-51` -- a SERP query builder ("<name> investor relations") and
  a parser over a fixture, **built, not run**, no network; plus two recorded SAP SERP rows used as rules fixtures
  (`lib/research/rules/source.py:46-59`, `lib/research/lists/build_lists.py:65-68`). News articles are the chatter
  channel's (another map).

### 2.7 Gaps and hazards
- Bronze keyed by the ticker-derived `security_key`, not by the issuer or URL: a FIGI re-key orphans it, and one issuer
  under two listings stores the same PDF twice.
- The silver `accession` column holds a `doc-` id for this vendor: a reader that treats it as an SEC accession
  (`analyze.source_from_pool` sorts accessions as strings, `analyze.py:1439`) can pick the wrong winner when one name has
  both an EDGAR row and a `doc-` row ("doc-..." sorts after digits, so it always wins).
- ANNUAL-REPORT markers and all vocabulary are English, plus one Japanese title: a German / French / Dutch / Italian /
  Spanish / Nordic / Chinese annual report returns family UNKNOWN and fails test (c) (`document.py:286-307`), so the
  company-site step cannot win on any non-English, non-Japanese document.

---

## CHANNEL 3 -- ESEF / UKSEF by LEI (filings.xbrl.org) -- built, not wired (brief)

- Battery step 3 (`battery.py:864-909`): GET `https://filings.xbrl.org/api/entities/<lei>/filings`. 404 = not held;
  a non-empty `data[]` is RECORDED as an attempt and **never accepted** -- "acceptance path ... UNEXERCISED ... recorded,
  not run" (`:898-909`). It never downloads a filing package, so it never writes bronze (`:1255-1257`).
- Writers exist with no production caller: `bronze_esef_filing` and `esef_filing_fetched`
  (`harvest/filings.py:140-153`), key `filings-xbrl/harvest/bronze/filing/lei=<lei>/<document id>/<vendor file name>`,
  content type `application/zip`. Silver would route to vendor `filings-xbrl` (`:74-79`). Live objects: 0.
- LEI source: Bloomberg `LEGAL_ENTITY_IDENTIFIER` (`battery.py:534`), or nothing on the crosswalk path (`:438-471`).
- Hazard: for an EU/UK-listed IEFA name this is the natural primary source (ESEF annual financial reports are mandatory
  for EU regulated-market issuers), and it is the one step that does nothing. No `ESEF` family exists in the cutter, so
  even a downloaded package would fail test (c).

---

## CHANNEL 4 -- TRANSLATION METHODOLOGY

### 4.1 Every place language is detected or translated (exhaustive over `lib/research`, `integrations/`, `portal/src`)
| place | what | file:line |
|---|---|---|
| language detection | script-share rule, no library: `ja` if kana share > 0.02; `zh` if CJK > 0.3; `ko` if hangul > 0.02; `en` if ASCII letters > 50% of letters; else `unknown`. First 40,000 chars. | `lib/research/filings/document.py:315-365` |
| detection call sites | battery acceptance (every attempt records `language`), EDGAR path, analyzer fallback | `battery.py:412`, `fetch.py:417`, `analyze.py:1313-1327` |
| analyze-in-original | a non-`en` language adds a CRITICAL rule: write every finding in that language, quote with the script's own marks, do not translate | `analyze.py:201-232` (`_LANGUAGE_NAMES` has ja/zh/ko only, `:219`), applied `:396-408` |
| Unicode passages | passages NFC, never ASCII-folded; `non_ascii_chars` recorded (precondition (i)) | `passages.py:25-34`, `:55-62`, `:180-223` |
| character-level verbatim | runs over scripts without spaces graded by characters when CJK share > 0.3 | `drafting_build.py:290-298`; `drafting/verbatim.py:23-30` |
| **translation stage** | `translate_output(analysis)` | `lib/research/filings/translate.py:125-201` |
| drafting carry-through | copies `text_original`, `text_translated`, `translation` onto each drafted sentence, after the gate ran on the original | `drafting_build.py:307-317` |
| Yuho roster | keeps the Kanji name, parses the Japanese officer table | `management/roster.py:904-1000`, `:81`, `:534` |
| portal | **no** translation or language handling anywhere in `SecurityAnalysis` (the only hit is a CSS class) | `portal/src/pages/SecurityAnalysis/**` |
No translation library or service (DeepL, Google, langdetect) is imported anywhere in the searched trees.

### 4.2 What translates, with what, and how
- **Service:** the Anthropic API through `analyze.anthropic_call` -- model `claude-opus-5` (`analyze.py:60`), streaming,
  `effort "low"`, `max_tokens 8000` (`translate.py:153-154`), prompt `rj6-translate/1` (`:46`, text `:52-62`) wrapped in
  the untrusted-document clause. Key from the environment only (`analyze.py:328-333`).
- **One call per document.** Input: a numbered list of every served item's `text` across the six classes, plus the thesis
  driver's `series`, `unit`, `why` (`translate.py:136-146`). Output: a JSON array of the same length; a count mismatch
  records `translation {translated: false, failed: true, reason, usage}` and leaves every item original-only (`:159-166`).
- **English makes no call:** `translation = {"skipped": "english"}` (`:131-134`).
- **Written fields (on the ANALYSIS object, in place):** per item `text_original`, `text_translated`, `translation
  {translated: true, source_language, translator {model, prompt_version}, translated_at, passage_ids}` (`:170-180`); on
  the driver `series_translated`, `unit_translated`, `why_translated`, `text_translated`, `text_original`, `translation`
  (`:182-196`); document-level `translation {translated, source_language, count, usage}` (`:198-200`).
- **Controls:** VERBATIM-CHARS, NEIGHBOUR, MUTATION, TABLE-DERIVED + NUMBER-CONTROL (`:279-379`), RELOCATE (a translation
  must NOT re-locate in the original, `:382-399`). The PRD's evidence line records Keyence: 70 of 71 findings verbatim,
  controls refused 70/70 and 68/68, 0 of 71 translations re-locate (`AMGT_RESAPP_PRD.md:1830-1833`).

### 4.3 Where original vs translated text is stored -- and the contracts
- **Stored in S3: nowhere.** `translate.py` is a standalone CLI (`:27`, `:402-466`) that writes to a LOCAL `--out`
  path only. `translate_output` has **no caller** in `analyze.py`, `batch.py` or any other production module (searched).
  The only translated object ever made (Keyence, `.scratch/keyence/6861_JP_Equity.translated.json`, cited in the rk-40
  proof `deliverables/0.9.0_WK_AMGT_RESAPP~42/...proof_of_spec.json:183`) is not in S3 and not on this box's `.scratch/`.
  The sampled served analysis (SAP) carries no `translation` or `language` key; the other 11 were not opened, but all
  12 are EDGAR filings in English, so the stage would skip them regardless.
- **Tier placement:** translated text lives on the analysis object, and the analysis is **GOLD** by the harvest code's own
  statement (`harvest/filings.py:14-15`, `:34-36`). Bronze keeps the original bytes (C-BRONZE-AS-RECEIVED,
  `AMGT_RESAPP_PRD.md:910-920`) -- except that no filings bronze is actually written. Silver `filing_source` carries
  only the ORIGINAL-language excerpt and `language`; there is no translated column and no translated silver table. So
  translation is a gold-only derivation, which is consistent with C-FILINGS-TRANSLATION's "ANALYZE THE ORIGINAL;
  TRANSLATE THE OUTPUT" (`PRD:788-805`): nothing upstream of the analysis is ever translated.
- **Contract gap 1 -- the API drops the translation.** `read_drafted_sections` rebuilds every sentence with five keys
  only -- `text, generated, evidence, verbatim_check, quoted_spans` (`scoped_amgt.py:1663-1671`) -- so
  `text_translated` / `translation` never leave the API even when present. `thesis_driver` passes through whole
  (`:1690`), so the driver's translated fields WOULD reach the page. The portal type `DraftedSentence` has no
  translation field (`types.ts:582-591`), and nothing renders the PRD's required label "a translation, never the
  filing's words" (`PRD:797-799`).
- **Contract gap 2 -- the header serves original-language prose.** The description fallback serves
  `company_description` sentence 1's original `text` (`scoped_amgt.py:2983`); the `_describes_business_test` phrases are
  English (`:2346-2380`), so a Japanese sentence fails rule (b) and is not served -- ABSENT rather than wrong.
- **Contract gap 3 -- the pipeline order.** The PRD places the stage "after the cutter and the passage map, before
  analysis" for detection, and translation after analysis (`PRD:792`); the code has detection in place but no pipeline
  step that runs translation, so `translation` in the stage table is still "none -- not built" (`PRD:1780`) in practice.
- **Roster names:** kept in the original script (`roster.py:81`, `:534`), matching `PRD:800-801`; no English rendering
  step exists.

### 4.4 The IEFA hazards (non-US universe) -- the ones that decide backfill
1. **Latin-script languages are detected as English.** `detect_language` only knows ja/zh/ko; German, French, Dutch,
   Italian, Spanish, Swedish, Danish, Norwegian, Finnish text has well over 50% ASCII letters and returns `en`
   (`document.py:344-356`). Consequences, all silent: the analyzer gets NO language rule (`analyze.py:397`), and
   `translate_output` skips with `"english"` (`translate.py:131-134`). The contract's "a wrong detection is visible"
   (`PRD:793`) is not met for these languages -- the shares are printed, but every share looks English.
2. **No cutter for non-English, non-Japanese documents.** Families are 10-K, 20-F, English ANNUAL-REPORT, YUHO
   (`document.py:60`). A Geschaeftsbericht, rapport annuel / document d'enregistrement universel, jaarverslag, or a HK/China
   annual report is family UNKNOWN and fails the battery (test (c)). Only EDGAR filers (20-F in English) and
   English-language annual reports can resolve today.
3. **ESEF, the natural EU source, is a no-op** (channel 3).
4. **The multi-name battery resolves nothing.** For N > 1 names, keys come from `keys_from_crosswalk`
   (`battery.py:1449`), which hard-codes `legal_name`, `cik`, `lei`, `web_address`, `domicile` to None (`:459-471`).
   Step 1's name guard then always fails (`_entity_test` refuses without a legal name, `:288-295`), steps 2-3 have no key,
   and step 4 has no seed except an ASX listing page. Only the single-name `--bloomberg` path reads real keys
   (`:1411-1413`). A fleet backfill through today's multi-name CLI would mint UNRESOLVED markers for every name.
5. **State is stale by construction for the IEFA set.** 178 of 180 `filing_attempt` markers are the pre-battery
   "no cik" marker; the battery has run on 2 names. The markers are write-once with SKIP-HELD / CHANGED-HELD
   (`harvest/filings.py:315-391`), so a re-run whose outcome changed exits 2 and does not overwrite -- a backfill has to
   decide what to do with these 178 first.
6. **Chinese Hong Kong / Taiwan names:** `zh` has no `_LANGUAGE_NAMES` entry beyond "Chinese"; there is no zh family
   and no zh cutter headings.
7. **English edition rule not implemented:** the PRD says an English document replaces translation only when same FY
   and same family (`PRD:802-803`). No code compares a Japanese Yuho to an English annual report; the crawl takes the
   first document that passes.

---

## SUMMARY (component view)

| component | filings / IR / translation fields it reads today | status |
|---|---|---|
| Thesis (primary) | `drafting/v1` sentences + evidence passages + thesis driver, built from `filings/v1/*.analysis.json` (model `claude-opus-5`, 2 passes) over risk (1A / 3.D) + MD&A (7 / 5) | SERVED for 12 English EDGAR names; ABSENT for the rest with the state `reason` |
| Lead Panel (header) | `company_description` sentence 1, only when Bloomberg's description is absent | fallback only |
| Exec Mgmt | `officer_section` (Item 10 / Item 6 / Yuho officers) from silver, parsed offline into `management/v1` | EDGAR only; null for every issuer-site win, so Keyence uses the Bloomberg fallback |
| Model | none directly; the thesis driver joins Model figures on the Thesis chart | -- |
| Peers | none | -- |

SUMMARY
- Live: 13 SEC and 1 issuer-site (Keyence) rows in silver `filing_source`; 0 bronze on SEC, issuer-site and ESEF; 180 state markers (178 are pre-battery "no cik"); 12 legacy analyses and 12 drafting documents, all built from English EDGAR filings. The sampled analysis (SAP) is at analyzer 1.0.0.
- Silver `filing_source` has 24 columns; everything nested (excerpt text, officer_section, battery, verified_site) is only in `object_json`. `bronze_key` points at the legacy `.source.json`, and `fetched_at` / `date=` record the M2 move time, not the fetch time.
- Items cut: risk (10-K 1A / 20-F 3.D) and MD&A (7 / 5) are analyzed; officers (10 / 6) are kept separately for Exec Mgmt. Item 1 Business is never cut.
- IR crawl: a bounded 40-page crawl seeded from Bloomberg's web address, EDGAR website fields and the ASX listing page only. Documents are named `doc-<sha16 of bytes>`. No press-release, blog or RSS ingestion exists; `ir_scan.py` is built but not run.
- ESEF by LEI records that filings exist and never accepts one. Its writer has no caller.
- Translation: one `claude-opus-5` call per document translates the analyzer's OUTPUT only (C-FILINGS-TRANSLATION). The stage is a standalone CLI with no production caller, and 0 translations are stored in S3. Translated text belongs on the gold analysis; bronze and silver stay in the original language.
- The API strips `text_translated` from drafted sentences (`scoped_amgt.py:1663-1671`), and the portal has no translation field or label.
- Biggest IEFA hazard: `detect_language` labels German, French and every other Latin-script language as `en`, so translation is silently skipped. The cutter knows only English and Japanese families, so European-language annual reports fail the battery.
- A multi-name battery run cannot resolve any name, because crosswalk keys carry no legal name, CIK, LEI or web address.
- `batch.py` never persists a RESOLVED source to silver after M2. The Keyence step-4 winner drops `officer_section`, which forces the Bloomberg roster fallback.
