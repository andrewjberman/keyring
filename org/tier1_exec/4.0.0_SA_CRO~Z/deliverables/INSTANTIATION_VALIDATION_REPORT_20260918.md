# Validating new-security instantiation on three uncovered names

**Run by** an Opus subagent of `4.0.0_SA_CRO~Z`, 2026-09-18, under Andrew-direct ~16:5xZ ("sure set a subagent at opus
model in this session to go pursue that"; scope recorded in `ANDREW_DIRECT_20260918_16xxZ_THESIS_NO_RERUN_AND_FILINGS_BATTERY.md`).
**Committed by** `4.0.0_SA_CRO~Z`: the subagent's harness refused report files, so its final report is reproduced here
as delivered. The only edits are HTML entities decoded to plain characters, and headings. Code vintage SITEZ HEAD
`496f4ce43b`. Everything is MEASURED unless marked INFERRED or SURVEY; SURVEY means a read-only code survey by an
Explore subagent, cited by file:line but not re-run.

**Scratch folder** (session scratchpad, not committed):
`...\d60f6524-dc92-4e15-937e-45e7685911cb\scratchpad\instantiation_validation\`. Scripts `s01`-`s20` each have a
`.out.txt`; source objects in `sources/`, analyses and drafts in `analysis/`, downloaded documents in `docs/`, and the
design-A demo in `s16c_designA_custom.json`.

**Limits held:**
- **No S3 or DynamoDB write.** From s09 on, AWS was reached only through a proxy that refuses write verbs; its test
  refused both `s3.put_object` and `Table.put_item`.
- **No commit, no Lusha or Bright Data call.** Spend $2.45 of the $12 cap.
- **One accidental repo write, undone.** The peers engine's `--dry-run` rewrote a tracked cache file (D24). The
  subagent restored the committed bytes. **Re-verified by `4.0.0_SA_CRO~Z`:** `git status` and `git diff` on
  `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~21/candidate_universe.json` are empty, and the
  committed blob is 1,000,578 bytes.

---

## 1. The three names, and the not-covered check

| name | Bloomberg | why this name |
|---|---|---|
| Caterpillar | `CAT US Equity` (USD 369bn) | Large US company that files a 10-K |
| CSL Ltd | `CSL AU Equity` (AUD 84bn) | English report found only on the company's own site (battery step 4). No SEC annual report (its SEC ID carries only ADR paperwork); Australia has no ESEF regime. |
| Keyence | `6861 JP Equity` (JPY 18.6tn) | Its statutory annual report (the Japanese "Yuho") exists only in Japanese -- every IR-library link ends `_ja`, FY57 included. Its English "Annual Report 2026" is a different, thinner document (section 3), so the original is used. |

Dropped: Kweichow Moutai (publishes an English FY2025 annual report); anyone named in the 89 crosswalk records,
UNRESOLVED rows included (Nestle, for example, is present by folder name).

**Not-covered check** (`s02_notcovered.out.txt`); the Boeing column is the positive control:

| check | CAT | CSL | 6861 | Boeing |
|---|---|---|---|---|
| crosswalk 2026-09-15, token scan of all 89 records | 0 | 0 | 0 | 1 of 89 |
| `filings/v1/` exact prefix; token scan over 202 keys | 0; 0 | 0; 0 | 0; 0 | 4 |
| `derived/model_block/` (47 keys) | 0 | 0 | 0 | 10 |
| `drafting/v1/` (12 keys) | 0 | 0 | 0 | 2 |
| `management/v1/` (14 keys) | 0 | 0 | 0 | 2 |
| `posture/v1/` (33), `publication-links/v1/` (7), `raw/bloomberg/` (79) | 0 | 0 | 0 | 2 / keyed by bare root / 9 |
| `universe/v1` 2026-09-15 (256 names) and 2026-09-16 (250) | 0 | 0 | 0 | -- |

---

## 2. Stage-by-name grid

SERVED-LOCAL = the estate producer ran and its output exists in scratch only. UNRESOLVED = ran and could not produce,
reason given. NOT-RUN = not run, reason given. NOT-EXERCISED = outside this task's authorization. The last column
answers: what makes this stage run for a new security today?

| stage | CAT | CSL | Keyence | trigger for a new name |
|---|---|---|---|---|
| identity (crosswalk) | SERVED-LOCAL from a scratch coverage row; the served (pool) crosswalk resolves UNRESOLVED | same | same | **None.** Needs a ONE PAGER workbook folder in OneDrive, then 4 manual runs. 4 corpus folders already have no record: Alphabet, Eli Lilly, Quanta Services, UnitedHealth. |
| universe row + filing identity | UNRESOLVED with the estate SEC cache (false "no ticker 'CAT'", D1); SERVED-LOCAL with an extended cache: EDGAR, SEC ID 18230, 10-K | row served; filing identity none (SEC ticker CSL is Carlisle, correctly refused) | row served; filing identity none | None (manual; newest version is 16 Sep) |
| Bloomberg model block | SERVED-LOCAL (205 figures, FY2016-2025) | SERVED-LOCAL; FY2026 missing (D4) | SERVED-LOCAL (203 figures, 2 unresolved); FY2026 missing | None. Hardcoded 3-name list, no dry-run. An on-demand request route exists, but its consumer is started by hand (SURVEY). |
| filings battery | step 1 wins (live SEC table) | step 4 wins; test (c) fails on the estate cutter | step 4 wins (original); test (c) fails on the estate cutter | Only step 1 exists in code, and it reads a stale projection. The batch task is disabled and cannot launch. |
| source object | SERVED-LOCAL (estate `fetch.py`) | UNRESOLVED (no parser) -> SERVED-LOCAL via a scratch PDF cutter | UNRESOLVED (0 characters cut) -> SERVED-LOCAL via a scratch cutter | same as the battery |
| passages | SERVED-LOCAL (311 passages, 96.1% coverage) | raw PDF lines 9.3%; block reflow 91.6% | reflow 92.4%, but ASCII folding keeps 6.8% of characters | inside the analyzer |
| translation | n/a | n/a | not built in the estate; design A demonstrated in scratch (section 4) | none |
| analysis | SERVED-LOCAL, $0.6478, 83 of 83 items cited | SERVED-LOCAL, $0.4940, 77 of 81 cited | UNRESOLVED, corrupt: $0.5619, Japanese stripped, second pass truncated | manual `analyze.py` or the disabled batch |
| drafting (verbatim check) | 39 of 39 PASS, 17 of them vacuous | 40 of 40 PASS, 16 vacuous | 0 served, 40 dropped; the page adapter reads INVALID | as analysis |
| driver chart | ABSENT, correct refusal (decimals can never verify, D17) | ABSENT | ABSENT | derived at read time |
| management roster | UNRESOLVED (wrong item cut; its table format is unparsed) | **Falsely RESOLVED:** 6 "officers" named "Executive Vice" / "Senior Vice" (D20) | UNRESOLVED (kanji names erased) | disabled weekly task (SURVEY) |
| management enrichment | NOT-EXERCISED. `domains.json` lists 5 names, none of these, so no vendor call would fire anyway. | same | same | a `domains.json` entry |
| peers | UNRESOLVED: computes over 2,850 candidates but the subject is unresolved in the pool; rewrote a repo cache (D24) | NOT-RUN, same dependency | NOT-RUN | None |
| posture | UNRESOLVED, verdict absent (identity in neither universe nor crosswalk) | NOT-RUN (INFERRED same) | NOT-RUN | None; also reads the model block from a repo folder, not the pool (D7) |
| scores | UNRESOLVED: reads the pool crosswalk directly (33 names) | same | same | None |
| description | SERVED-LOCAL, but the text served is a segment-sales sentence (D23) | same | ABSENT (drafting INVALID) | read time; `CIE_DES` not pulled |
| chatter / news | harvesting NOT-EXERCISED (publisher egress not authorized); harvester population 89 names, 0 of 3 present; chatter dry-run: **CAT ranked #10 on Trending with 0 articles** | considered, 0 articles | **ranked #2 on Trending with 0 articles** | Chatter Lambda daily 10:00 UTC over the pool universe: the **only** scheduled stage |
| price | SERVED-LOCAL (3 of 3 price series); identity resolved 0 of 3 | Trending rank 1 (+12.51) | listed on Breakout at -0.041, a falling name | None (manual; population is a repo file) |
| movement lists | follow chatter and price | same | same | those producers |
| page adapter | Thesis served through local reads (4 of 5 sections, 15 header + 190 yearly figures); through the pool it reads nothing | same | Thesis INVALID | n/a |

**Reading the grid:** every stage except the chatter Lambda needs a person to run it. Every reader behind the page keys
on the pool crosswalk and universe, so a name fully produced elsewhere still shows nothing until its identity lands in
the pool.

---

## 3. Battery log

Acceptance test: (a) the right entity; (b) fiscal year ended on or after 2025-03-18; (c) a document family the cutter
and roster can parse. Language is recorded, not tested. Step 3: `filings.xbrl.org` returned 404 ("Entity not found")
for all three; the research note shows the same endpoint returning filings for 6 other names, so 404 means not held.

### CAT

| step | route and key | result | (a) | (b) | (c) | lang |
|---|---|---|---|---|---|---|
| 1, estate | cached SEC projection, `CAT` | MISS: "table (10422 rows) carries no ticker 'CAT'" is **false** (D1) | | | | |
| 1, live | live SEC ticker table (10,438 rows) | SEC ID 18230, CATERPILLAR INC; latest 10-K filed 2026-02-13 for the year to 2025-12-31 | PASS (name and SEC ID match Bloomberg) | PASS | PASS: risk 53,455 characters; MD&A cut at 80,000 of 103,449 | en |
| 2 | Bloomberg SEC ID 0000018230 | same 10-K | PASS | PASS | PASS | en |
| 3 | LEI `WRJR7GS4GTRECRRTVX92` | 404 | | | | |

**Winner: step 1 (live table).**

### CSL

| step | route and key | result | (a) | (b) | (c) | lang |
|---|---|---|---|---|---|---|
| 1, estate | `CSL` | MISS | | | | |
| 1, live | `CSL` | Carlisle Companies (SEC ID 790051): refused as a collision | FAIL (wrong company) | | | |
| 2 | Bloomberg SEC ID 0001274152 | "CSL LTD": 11 filings, all ADR/registration paperwork, no annual report | PASS | FAIL | | |
| 3 | LEI `529900ECSECK5ZDQTE14` | 404 | | | | |
| 4 | web search | ASX filing PDF on investors.csl.com: 175 pages, results notice plus the Annual Report | PASS on name, ABN and ASX code; the LEI is not in the document | PASS (year to 2026-06-30) | estate FAIL (D8, D9); scratch cutter PASS | en |
| 5 | ASX | NOT-RUN: the step-4 PDF is the ASX filing itself (INFERRED same bytes) | | | | |

**Winner: step 4.** Bloomberg's web-address hint (`www.csl.com.au`) is not where the report is hosted
(`investors.csl.com`).

### Keyence

| step | route and key | result | (a) | (b) | (c) | lang |
|---|---|---|---|---|---|---|
| 1 | `6861` | MISS in both the estate cache and the live table | | | | |
| 2 | Bloomberg SEC ID | field not applicable to this security | | | | |
| 3 | LEI `529900M7PQBS7A89DZ11` | 404 | | | | |
| 4 | IR library | FY57 Yuho, year 2025-03-21 to 2026-03-20: 78 pages, filed 2026-06-15 | PASS: the cover's English name matches Bloomberg; Japanese regulator code E01967; no LEI in the document | PASS | estate FAIL (0 characters cut); scratch PASS | ja |
| 4, English edition | Annual Report 2026 in English, 32 pages, same year | not an edition of the Yuho: 2-page risk factors, 2-page shareholder letter, no MD&A, board list of 11 names with titles only, no role dates | PASS | PASS | FAIL for the roster and MD&A | en |
| 5 | EDINET API | NOT-RUN: needs a subscription key | | | | |

**Winner: step 4, the Japanese original, translated.**

---

## 4. Translation, measured on Keyence

### Without a translation stage (the estate analyzer, unchanged) -- it fails closed, but the analysis claims 100% cited while corrupt

- **Passage text:** ASCII folding (`passages.py:67-79`) keeps 6.8% of the characters; 7 of 28 passages are stored empty.
- **Findings** lose their Japanese quotes but still read 73 of 73 cited, e.g. "The company discloses that , i.e. no
  objective target indicator is set." The driver becomes "Overseas net sales ()".
- **Second pass** truncated at its output cap (12,000 of 12,000 tokens, `analyze.py:444`); items came from the fallback
  path. That pass cost $0.3758, twice the first.
- **Drafting:** 0 sentences served, 40 dropped; the page adapter reads the document as INVALID.
- **Citations:** all 74 spanned the whole excerpt; on plain-text Japanese the citations API's sentence chunking collapsed
  to one chunk (D16).
- **Verbatim helper** splits on spaces, so a Japanese sentence is one token: it found a run in 0 of 68 findings. On
  Japanese the check can only pass vacuously.
- **Units:** "381,431 million-yen" parses as `381431` with the unit dropped.
- **Roster:** kanji names become blank.

### Design A in scratch: analyze the original, translate the output (the estate's own model-call functions plus one language rule; no repo edit)

1. **First attempt ($0.1755):** plain-text document, findings requested in Japanese. Every citation was again the whole
   document, so its attribution check was vacuous -- caught on a length check, not counted.
2. **Fixed attempt ($0.2041):** the document sent as 40 pre-cut passages, with no ASCII folding.
   - 72 citations, each naming exactly 1 passage; 72 of 72 cited texts are in the original.
   - Of 71 findings, **70 PASS**: each contains a verbatim run of 12 or more characters inside the one passage it
     cites; 0 misattributed; 1 short, flagged paraphrase.
   - Controls: each passing finding pointed at the neighbouring passage, **70 of 70 refused**; one-character mutations
     of verified runs, **68 of 68 refused**.
3. **Translation of the output ($0.1120):** 71 of 71 lines translated, each carrying `translated: true`, the source
   language, the translator and prompt version, and a timestamp, with the original sentence and passage id beside it.
   **0 of 71 translations relocate in the original** -- the check is provably against the filing.

**Verdict:** the verbatim-against-original check held under design A. It needed three things the estate lacks:
passages that keep Unicode; citation blocks pre-cut to the passage map; and a character-level verbatim rule for
languages written without spaces. The clean design-A path cost **$0.32** for Keyence, against about $0.65 for an
English 10-K on the estate path. The stage belongs after the cutter and passage map and before analysis; language
detection belongs there too, and the estate has none.

---

## 5. Defects and gaps, by stage

**Identity and universe**
- **D1** `build_universe.py:503-508` with `deliverables/0.9.0_WK_AMGT_RESAPP~19/sec_ticker_cik_cache.json`: the cache
  holds only 33 tickers, but a miss is reported as absence from the full 10,422-row SEC table. Nothing in the repo
  rebuilds the cache.
- **D2** `crosswalk.py:70-73`: identity comes only from a repo coverage file built by a manual OneDrive scan. Adding a
  folder triggers nothing; 4 folders are already unregistered.
- **D3** `scores/run_scores.py:81-88` reads the pool crosswalk directly, bypassing the local override
  (`AMGT_CROSSWALK_PATH`). At `:228-229` and `:252`, its dry-run prints "written_count 33" with nothing written.

**Model block and posture**
- **D4** `model_block_pull.py:100-101`: the history end date is hardcoded to 2025-12-31, so FY2026 is excluded for
  every name.
- **D5** `model_block_pull.py:53`: 3 hardcoded securities and no dry-run. At `:246` the ledger write goes around the S3
  client it was given (`ledger.py:64-66,87`).
- **D6** `model_block_pull.py:57-73`: the header field list has no `CIE_DES`, although Bloomberg returned it for all
  three names.
- **D7** `posture/packs.py:40-42,63-67`: posture reads model blocks from a repo folder holding 3 real names, not from
  the pool.

**Battery and source**
- **D8** `fetch.py:103-152,336-338`: only 10-K and 20-F are handled; no PDF, company-site or regulator adapter.
- **D9** `fetch.py:128`, with the open-ended cut at `:316-323`: the bare "riskfactors" fallback cut 70,000 characters of
  a patient story from CSL's report under 20-F rules -- a wrong-object excerpt that would pass as a section.
- **D10** `fetch.py:115-123`: Item 10 wins even when it only cross-refers to Item 1D. CAT's officer section is 27,766
  characters of cross-reference text.
- **D11** No language detection in `fetch.py`, `passages.py` or `analyze.py` (all read in full).

**Passages**
- **D12** `passages.py:146,174`: one paragraph per line, and any line under 60 characters counts as a heading. Raw PDF
  text gives 9.3% coverage for CSL and 1.8% for Keyence.
- **D13** `passages.py:67-79`: ASCII folding silently erases Japanese and Chinese characters.

**Analysis**
- **D14** `analyze.py:444`: the second pass truncates on Japanese output.
- **D15** `analyze.py:551-555`: non-ASCII quotes are stripped from findings while the counts still say 100% cited.
- **D16** `analyze.py:285-293`: a plain-text document gives whole-document citations on Japanese.
- **D17** `analyze.py:634,651-663`: the number matcher accepts whole numbers only. CAT's "1.8 billion" is in the text but
  can never verify. Units are also dropped (`:596-608`).

**Drafting**
- **D18** `drafting_build.py:85-128`: a sentence with no quoted span passes vacuously (CAT 17 of 39, CSL 16 of 40). On
  Japanese, every sentence would.
- **D19** "Verbatim" means verbatim after ASCII folding: 2 of CSL's 24 quoted spans match only after "(R)" and plain
  dashes replace the original symbols.

**Management**
- **D20** `roster.py:97-99,118-119`: capitalized title words are accepted as a person's name. CSL reads RESOLVED with 6
  "confirmed" officers called "Executive Vice" or "Senior Vice"; the real CFO and interim CEO are missed.
- **D21** `roster.py:17-26`: none of the three supported layouts reads CAT's "Name (age) Role (year)" table (0
  candidates, even on the correct section).
- **D22** `roster.py:157-171`: kanji names are erased. A scratch parse of the Japanese table found 12 of the 12
  declared officers, and the English report gives English spellings for 11 of them.

**Description, peers, chatter, price, batch**
- **D23** `scoped_amgt.py:2574-2592`: the description line is taken from segment and commentary findings -- CAT is
  described as "Construction Industries' total sales were $25.060 billion in 2025...". At `:2261` it looks only for
  `CIE_DES`.
- **D24** `peers/universe.py:569-578`: a stale cache is rebuilt and written even under `--dry-run`. It rewrote the
  tracked `deliverables/0.9.0_WK_AMGT_RESAPP~21/candidate_universe.json` (restored). Any seat's peers dry-run will do the
  same until the committed cache is refreshed.
- **D25** The chatter axis ranks zero-article new names on Trending (Keyence #2, CAT #10) -- the Lead Panel F2 defect
  reaching every new name.
- **D26** `price_axis_pull.py:142-163`: the population comes from a repo file and identity from the pool universe, so 0
  of 3 names got a key. At `:135-138` and `:336-367`, a dry-run writes into the repo's `~6` folder (redirected).
- **D27** `filings/batch.py:198`: the dry-run announces 243 unresolved objects, but the real run writes 23 (it skips
  rows with no identity at `:232-235`).

---

## 6. Spend

| name | stage | USD |
|---|---|---|
| CAT | analysis (0.4429 + 0.2049) | 0.6478 |
| CSL | analysis (0.3038 + 0.1902) | 0.4940 |
| Keyence | estate baseline, unchanged | 0.5619 |
| Keyence | design A, first attempt (not counted) | 0.1755 |
| Keyence | translation, first try; reply unparsed because of the script, wasted | 0.1397 |
| Keyence | translation of the first-attempt findings | 0.1184 |
| Keyence | design A, fixed attempt | 0.2041 |
| Keyence | translation of the fixed-attempt findings | 0.1120 |
| **Total** | | **2.4534 of the $12.00 cap** |

Other egress: 6 EDGAR requests; 3 `filings.xbrl.org` requests; 3 PDF downloads from company sites; 5 Bloomberg calls
(1 identity, 3 model blocks, 1 price history).

---

## 7. What the instantiation process needs, ranked

1. **A single "add a security" step that puts identity into the pool.** Every reader behind the page keys on the pool
   crosswalk and universe, so all three produced names still read UNRESOLVED; 4 corpus folders already sit
   unregistered. One Bloomberg call returned every key the battery needs: name, exchange, LEI and SEC ID.
2. **Fix battery step 1 before adding any US name.** Query the live SEC table, or rebuild the cache per name, and stop
   reporting a cache miss as absence. The estate's own step 1 misses Caterpillar; the live table with the existing name
   guard resolves CAT and correctly refuses CSL.
3. **A document layer for non-EDGAR reports: PDF reflow plus a section cutter per document family**, with test (c) as a
   real gate and no bare "riskfactors" fallback. Step 4 found the right, current document for both international names
   and nothing in the estate can cut either; coverage goes from 9.3% and 1.8% to 91.6% and 92.4% with reflow; the 20-F
   rules produced a 70,000-character wrong-object excerpt.
4. **Unicode evidence plus a translation stage, built as design A**, with pre-cut citation blocks and a character-level
   verbatim rule. Unchanged, the estate keeps 6.8% of Japanese text, cites the whole document, and cannot verify.
   Design A passed 70 of 71; both controls refused every case; 0 of 71 translations relocated. Cost $0.32 per name.
5. **Make the management roster correct before it scales:** a check that a title is not a name, a layout per document
   family (US "Name (age) Role (year)", Australian leadership pages, the Japanese table), and Unicode names. CSL got a
   confidently wrong roster, CAT's standard table was missed, and every Keyence name was erased; the Japanese table is
   parseable (12 of 12 in scratch).

**Also cheap to fix:** the hardcoded FY end date (D4); `CIE_DES` not pulled while a segment figure is served as the
description (D6, D23); posture reading a repo folder (D7); a peers dry-run that writes a repo file (D24); zero-article
names ranked on Trending (D25); decimal chart values that can never verify (D17).
