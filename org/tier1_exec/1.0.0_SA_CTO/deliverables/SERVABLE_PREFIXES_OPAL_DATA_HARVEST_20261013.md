# SERVABLE_PREFIXES -- `opal-data-harvest`, harvest V1 for asset managers (`1.0.0_SA_CTO~DELL1` v1 2026-10-13 ~18:3xZ; v2 measured by `2.0.0_SA_COO~W1`; v3 = v2 with the CTO rulings F1-F5 applied, ~18:5xZ; v3 updated ~19:1xZ for Andrew's Bloomberg word)

**For:** site Z's NFRA_MCPINDEX round (catalog rows) and NFRA_OPLGTW (the asset-manager research grant), through `0.0.0_AB_MSTR`. Cluster direction
`org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL1_20261013.md` O3.

**The V1 rule** (cluster ruling, section 1.4 item 6; Andrew may widen it): serve DERIVED layers and article LINKS only, never raw publisher text. The ruling names
the served layers: packs, chatter, scores, management, filings outputs.

**What changed in v2:** v1 classed every prefix from its name and opened no object. v2 opened ONE object (or one Parquet footer) per top-level prefix and per
`amgt/harvest/gold/` table, and recorded the field NAMES and types only (no value was printed or copied). Counts are unchanged (11 SERVE, 13 WITHHOLD); the
differences are one narrowed row (8), one class now read (23), and five measured flags on SERVE rows (section "Flags") that are the CTO's calls, not decided here.

## How this was read

- `aws s3api list-objects-v2 --bucket opal-data-harvest --delimiter /`, 2026-10-13 ~18:2xZ and again ~18:4xZ: **24 top-level prefixes, 24 classified below**
  (the v1 count and the v2 count agree, one page each, 24 of 24 under the 1,000-key page).
- Content read: one object per prefix, the first key returned (a SAMPLE of 1, never a census of the prefix). `packs/` was sampled on 4 of 105 names.
- **Claim vocabulary:** MEASURED = a field name or size read from an object; INFERRED = the prefix name, layer and owning code only. Where a row says MEASURED, the
  sample is the one object named in the evidence table, so it bounds the row to that object's class and no further.

## The 24 prefixes

| # | prefix | content (measured where marked) | class | V1 |
|---|---|---|---|---|
| 1 | `packs/` | one prefix per covered name (105); MEASURED on 4 names: `input_ledger.json` only (input_class, source, outcome, stamp, detail) | derived (input ledger) | **SERVE** |
| 2 | `scores/v1/` | per-name scores; MEASURED: divergence, `peers_v`, `inputs.model_block_key` | derived from the Bloomberg model block | **SERVE (F2 answered by Andrew-direct ~19:0xZ: cloud data is available to the team, BBG terms do not apply)** |
| 3 | `management/v1/` | management outputs (FWD-17 roster); MEASURED: roster, `lusha_enrichment`, `ceo_public_profile` (url, title, snippet) | derived, with vendor and web fields | **WITHHOLD until the view exists; then SERVE (F4 ruled: view without `lusha_enrichment`, RESAPP's writer)** |
| 4 | `filings/v1/` | MEASURED: `<accession>.source.json` carries `excerpt.text` (70,023 chars) and `<accession>.analysis.json` carries `passage_map[].text` (549 passages) | derived items plus verbatim SEC filing text | **SERVE as is (F1 ruled: SEC filings are public documents, not publisher text)** |
| 5 | `posture/v1/` | posture judgments; MEASURED: verdict, reason, and `membership` (books, weight_by_book) | derived (model-book membership inside) | **SERVE (F5 ruled)** |
| 6 | `peers/v1/` | peer sets; MEASURED: measures, country map, `csc_columns` | derived from the Bloomberg model block | **SERVE (F2 answered by Andrew-direct ~19:0xZ: cloud data is available to the team, BBG terms do not apply)** |
| 7 | `publication-links/v1/` | per-name article links; MEASURED (291 B): security_key, company, ticker, article_key, publisher, first_discovered_at. **No url, no title** | article link INDEX | **SERVE as the index (F3 ruled: the derived link view is a staged enrichment item and joins it when built)** |
| 8 | `amgt/harvest/gold/` -- ONLY these six tables: `article_security_mention`, `article_sentiment`, `chatter_daily`, `chatter_event`, `chatter_window`, `candidate_universe` | MEASURED: counts, tiers, scores, tone, hashes, keys; `chatter_event` carries `lead_headline` (string) | derived (the chatter) | **SERVE (these six only)** |
| 9 | `identity/v1/` | security identity; MEASURED: crosswalk residue, cross-references | reference (lookup) | **SERVE** |
| 10 | `crosswalk/v1/` | the identity crosswalk; MEASURED: security_key, bloomberg, display_ticker | reference (lookup) | **SERVE** |
| 11 | `universe/v1/` | the covered universe; MEASURED: names with `books` and `weight_by_book` | reference (lookup, model-book membership inside) | **SERVE (F5 ruled)** |
| 12 | `amgt/harvest/bronze/`, `amgt/harvest/silver/` | MEASURED: bronze `research-report-extract/extract.json` holds `paragraphs[].text`; silver `research-report` holds metadata only (author, fund, sector, period) | raw report text (bronze); report metadata (silver) | WITHHOLD |
| 12b | `amgt/harvest/gold/` -- the other seven tables: `research-backlog`, `research-continuation`, `research-dossier`, `research_dossier`, `research-fund-form`, `research-model-typecast`, `research-sector-template` | MEASURED: `passages` (sector-template), `citations` (continuation), `fields.*.value/absent` (dossier) -- report-derived text; class of the rest not read | report-derived, unclassed | WITHHOLD (v1's whole-prefix SERVE admitted these) |
| 13 | `amgt/harvest/state/` | MEASURED: filing_attempt, freshness_snapshot, pull_log | operational | WITHHOLD |
| 14 | `wsj/harvest/` (bronze, silver) | MEASURED: silver `article` carries `text`, `body_blocks`, `title`, `url` | raw publisher text | WITHHOLD |
| 15 | `barrons/harvest/` | same shape as 14 (silver `article`; bronze `article`, `news_listing`) | raw publisher text | WITHHOLD |
| 16 | `ft/harvest/` | same shape as 14; collection held on Andrew's word | raw publisher text | WITHHOLD |
| 17 | `seeking-alpha/harvest/` | MEASURED: silver `article` (publishOn, themes, ...), bronze `analysis`, `article`, `news`, `report`, `symbol`; state `job_record` | raw publisher text | WITHHOLD |
| 18 | `issuer-site/harvest/` | MEASURED: silver `filing_source` (url, document_sha256, document_text_chars); no text column | issuer page metadata | WITHHOLD |
| 19 | `sec/harvest/` | MEASURED: bronze `company_tickers`; silver `filing_source` (metadata, `object_json`) | SEC text and metadata (public domain) | WITHHOLD in V1. **The first widening candidate:** see call C-SEC |
| 20 | `publications/v1/` (`barrons/`, `bbg/`, `ft/`, `sa/`, `wsj/`) | MEASURED: url, title, `body_blocks`, `text` (4,616 chars in the sample) | raw publisher text | WITHHOLD |
| 21 | `bloomberg/harvest/`, `raw/` (`raw/bloomberg/`, `raw/seekingalpha/`) | MEASURED: `raw/bloomberg` histdata mnemonics; `raw/seekingalpha` symbol payload | raw vendor data | WITHHOLD (Bloomberg's licence as well as the V1 rule) |
| 22 | `derived/` (`model_block/`, `model_block_fye/`) | MEASURED: figures (mnemonic, value, vintage, source), cases | derived from Bloomberg | **SERVE (Andrew-direct ~19:0xZ, as rows 2 and 6)** |
| 23 | `drafting/v1/` | MEASURED: AI-drafted `sections[].sentences[]` and `evidence_records[].passage` (verbatim SEC filing passages, 774 chars in the sample), `quoted_spans` | derived (AI-drafted) with verbatim SEC passages | WITHHOLD per the CTO (rows 23 to 24 stay WITHHOLD). NOTE for the CTO: this is the same class as `filings/v1` (F1 served it), so the reason is no longer licence or publisher text; the row waits on a word that it is plumbing or serves |
| 24 | `lib/local-publications/`, `social/v1/_measurement/` | MEASURED: a code archive (.zip); a vendor-job cost and delivery measurement | not data | WITHHOLD |

**Count now (v3, after Andrew's Bloomberg word), 24 of 24 rows:** 11 SERVE now (rows 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 22; row 8 is six tables), 1 SERVE when its view
exists (row 3), 12 WITHHOLD (rows 12-21, 23, 24; row 12b is the split of row 8). C-BBG is answered. C-SEC is closed by F1 as to `filings/v1` (row 19 stays WITHHOLD as
plumbing). Open at Andrew in one line: whether his word also lifts the V1 derived-only rule for raw articles and raw vendor responses.

## Flags -- measured findings the CTO decides (each row stays as the ruling put it until the CTO says)

**v3: all five are ruled (section "CTO RULINGS" at the end); the table keeps the measured finding, the rulings carry the decision.**

| id | finding (MEASURED) | rows | the call |
|---|---|---|---|
| F1 | `filings/v1` objects embed verbatim SEC filing text (`excerpt.text`, `passage_map[].text`). Row 19 withholds the same text under `sec/harvest/` as "the first widening candidate". The ruling serves "filings outputs", so the intent is the DERIVED items, not the text | 4, 19, 23 | C-SEC: one word from Andrew covers all three, OR the grant for row 4 is cut to a derived-only view. A prefix grant cannot split `analysis.json` (its `passage_map` is inside the derived file) |
| F2 | `scores/v1` and `peers/v1` are computed from the model block (`inputs.model_block_key`, `peers_v`), which row 22 withholds for the Bloomberg licence. The two reasonings disagree | 2, 6, 22 | C-BBG: serve scores and peers and withhold the block (v1), OR hold rows 2 and 6 with row 22 until the licence is read |
| F3 | `publication-links/v1` records carry no url and no title; the url lives only in `publications/v1` and the silver articles, both WITHHOLD. An asset manager would receive article keys, not links | 7 | Whether a derived link view (url, publisher, date, no body) is cut as an enrichment item, or the keys are enough for V1 |
| F4 | `management/v1` carries a vendor field (`lusha_enrichment`) and a third-party web snippet (`ceo_public_profile.snippet`). The Lusha licence's redistribution scope is unread | 3 | Serve as is, or strip the two fields at the producer |
| F5 | `posture/v1` and `universe/v1` carry Opal's own model-book membership (`books`, `weight_by_book`: DIVZ, IDVZ, PFDE, PFOE) | 5, 11 | Confirm asset managers may see book membership; the negative arm (non-research principal refused) already covers outsiders |

Also noted, not a verdict change: `chatter_event.lead_headline` is a publisher headline string inside a SERVE table (row 8). If a headline counts as raw
publisher text, the producer drops the column; if it counts as the article link's title, it stays.

## The grant, as the V1 rule needs it

- Grant an asset-manager principal `s3:GetObject` on the SERVE-NOW prefixes ONLY, as prefix conditions: `packs/`, `filings/v1/`, `posture/v1/`, `publication-links/v1/`,
  `identity/v1/`, `crosswalk/v1/`, `universe/v1/`, `scores/v1/`, `peers/v1/`, `derived/` whole, and row 8 as the six table prefixes `amgt/harvest/gold/<table>/`, never `amgt/harvest/gold/`. `management/v1/` is
  added when its view prefix exists and is named here. No bucket-wide read, and no `ListBucket` outside those prefixes.
- **Negative arms (FWD of O3):**
  - the same principal is refused on a WITHHOLD prefix (`wsj/harvest/`) and on a withheld gold table (`amgt/harvest/gold/research-dossier/`);
  - a non-research principal is refused on `packs/`.
- Every catalog row names its prefix exactly as above. A new top-level prefix is WITHHOLD until classed here.
- First catalog act per SERVE row: read one object and confirm the class (v2 has done it once per row; the sample is 1).

## Evidence (field names only; no value was printed)

| row | object read (key under `s3://opal-data-harvest/`) | size |
|---|---|---|
| 1 | `packs/1299_HK_Equity/input_ledger.json` (and the first key of `ASML_NA_Equity`, `BABA_US_Equity`, `COST_US_Equity`: the same single file) | 4,277 B |
| 2 | `scores/v1/2317_TT_Equity.json` | 3,432 B |
| 3 | `management/v1/ASML_NA_Equity/2026-09-18.json` | 1,698 B |
| 4 | `filings/v1/ASML_NA_Equity/000162828026011378.source.json` and `.analysis.json` | 73,776 B and 376,279 B |
| 5 | `posture/v1/ASML_NA_Equity/2026-09-16.json` | 4,548 B |
| 6 | `peers/v1/1299_HK_Equity/2026-10-11T0707Z.json` | 49,806 B |
| 7 | `publication-links/v1/COST/barrons/55682270...json` | 291 B |
| 8 | Parquet footers of `article_security_mention`, `article_sentiment`, `chatter_daily`, `chatter_event`, `chatter_window`; JSON of `candidate_universe` | 1 part each |
| 12b | `research-backlog`, `research-continuation`, `research-dossier`, `research_dossier`, `research-fund-form`, `research-model-typecast`, `research-sector-template` (first key of each) | 1 object each |
| 12 | `amgt/harvest/bronze/research-report-extract/.../extract.json`; `amgt/harvest/silver/research-report/...parquet` footer | 72,797 B; 39,382 B |
| 14-17 | the first silver `article` Parquet footer of wsj, bloomberg, barrons, ft, seeking-alpha | 28-125 KB |
| 18-19 | `issuer-site/harvest/silver/filing_source/...parquet` and `sec/harvest/silver/filing_source/...parquet` footers; `sec/harvest/bronze/company_tickers/...json` | 283,596 B; 808,344 B; 800,703 B |
| 20 | `publications/v1/sa/5666ee64...json` | 10,205 B |
| 21 | `raw/bloomberg/992_HK_Equity/20260916T201811Z/histdata.json`; `raw/seekingalpha/BA_US/20260911T040253Z/symbol.json` | 6,963 B; 17,945 B |
| 22 | `derived/model_block/1299_HK_Equity/20260926T001811Z/model_block.json` | 262,166 B |
| 23 | `drafting/v1/COST_US_Equity.json` | 89,893 B |
| 24 | `lib/local-publications/0.1.0/6aef3ceee43976dc/local-publications-0.1.0.zip`; `social/v1/_measurement/2026-09-15.json` | 143,769 B; 12,088 B |
| 9-11 | `identity/v1/2026-09-17-coverage-residue-crossref.json`; `crosswalk/v1/2026-09-15.json`; `universe/v1/2026-09-15.json` | 47,229 B; 188,380 B; 185,928 B |

**Not measured:** the other objects under each prefix (a sample of 1 per row); the Parquet bodies (footers only); whether any pack beyond the four sampled holds
more than `input_ledger.json`; the Bloomberg and Lusha licence terms; which principals exist at NFRA_OPLGTW.

## Owners

- The list: AMGT_HARVST (`2.0.0_SA_COO~W1`), with AMGT_RESAPP for `packs/`.
- The rulings F1-F5 (section "CTO RULINGS" below) and the Andrew-direct on Bloomberg: `1.0.0_SA_CTO~DELL1`.
- The derived link view (url, title, publisher, date, no body; F3): AMGT_HARVST, a staged enrichment item for the first issuance after the round-84 L10, not cut mid-round.
- The management view without `lusha_enrichment` (F4): AMGT_RESAPP's management writer, as an added output.
- The catalog rows and the grant: site Z, NFRA_MCPINDEX and NFRA_OPLGTW, under `1.0.0_SA_CTO~Z`.

-- 1.0.0_SA_CTO~DELL1 (v1), 2.0.0_SA_COO~W1 (v2 measured; v3 rulings applied)

## CTO RULINGS on F1-F5 (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~18:4xZ), on `2.0.0_SA_COO~W1`'s measured v2 @cbf1689562

- **F1, the filing text: SERVE `filings/v1` as is.** Andrew's V1 rule withholds raw PUBLISHER text. An SEC filing is a public regulatory document, not a publisher's
  article. The excerpts and passages are the analysis's own evidence, and splitting them out would break the derived file. `sec/harvest/` (the bulk raw store) stays WITHHOLD
  as plumbing, not on licence grounds. Andrew may still narrow this.
- **F2, Bloomberg-derived scores and peers: HELD for Andrew** (one card).
  - Rows 2, 6 and 22 all rest on the Bloomberg model block. Bloomberg's terminal licence is per user, so serving its derived values to asset managers' own Claude
    sessions is a licence question this seat cannot read.
  - Until he answers, rows 2 and 6 are WITHHOLD with row 22.
- **F3, links without urls: CUT a derived link view** as AMGT_HARVST's enrichment item: url, title, publisher and date per article, no body. That is what "article
  links" means. `publication-links/v1` serves in V1 as the index, and the view joins it when built.
- **F4, the Lusha field: SERVE `management/v1` through a view WITHOUT `lusha_enrichment`.** The Lusha licence's redistribution scope is unread. The view is cut at the
  producer side by AMGT_RESAPP's management writer, as an added output, never by editing the served object in place. `ceo_public_profile` (a public web snippet with its
  url) serves. Until the view exists, row 3 is WITHHOLD.
- **F5, model-book membership: SERVE.** Asset managers are Opal staff, and the grant's negative arm keeps it from anyone else.

**V1 count after the rulings:**
- **SERVE now:** `packs/`, `filings/v1/`, `posture/v1/`, `publication-links/v1/`, `amgt/harvest/gold/` (the six chatter tables), `identity/v1/`, `crosswalk/v1/` and
  `universe/v1/`.
- **SERVE when its view exists:** `management/v1/`.
- **HELD for Andrew:** `scores/v1/`, `peers/v1/` and `derived/`.
- **Everything else stays WITHHOLD.**

-- 1.0.0_SA_CTO~DELL1

## ANDREW-DIRECT ~19:0xZ: the Bloomberg hold is LIFTED

> Regarding Call 7, any data in our AWS cloud is available to our team. BBG Terms do not apply to materials in our cloud.

Record: `ANDREW_DIRECT_20261013_190xZ_CLOUD_DATA_AVAILABLE_TO_TEAM_BBG_TERMS_NOT_APPLICABLE.md`.
- **F2 is answered.** `scores/v1/`, `peers/v1/` and `derived/` (`model_block/`, `model_block_fye/`) are now SERVE.
- **Still WITHHOLD under the V1 rule** (raw text and raw vendor responses, not licence): rows 12 to 21 and 23 to 24.
- **Open in one line at Andrew:** whether his answer also lifts the V1 derived-only rule for raw articles and raw vendor responses.

**V1 count now:**
- **SERVE:** `packs/`, `scores/v1/`, `filings/v1/`, `posture/v1/`, `peers/v1/`, `publication-links/v1/`, `amgt/harvest/gold/` (the six chatter tables), `identity/v1/`,
  `crosswalk/v1/`, `universe/v1/` and `derived/`.
- **SERVE when its view exists:** `management/v1/`.
- **Everything else stays WITHHOLD.**

-- 1.0.0_SA_CTO~DELL1
