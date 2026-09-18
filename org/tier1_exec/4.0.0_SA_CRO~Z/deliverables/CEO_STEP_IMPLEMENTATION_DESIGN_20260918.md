# CEO step (Exec Management brief s.9) -- exploration, prototype and implementation design

From: a subagent of `4.0.0_SA_CRO~Z`, 2026-09-18 ~19:2xZ. Scope: Andrew's addendum ~18:4xZ in
`ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md`. Spend used: **10 of 10 Bright Data SERP requests,
US$0.5644 of the US$5 model cap** (8 calls to `claude-opus-5`). No Lusha call, no `mcp__brightdata__*` tool,
no S3 write, no repo edit, no commit, no message to another agent. Scratch work, raw captures and scripts live in
this folder (`ceo_step_exploration/`).

Code vintage for every `file:line`: workspace HEAD `375d618487`, portal HEAD `625a08887b`. Every cited file is
unmodified in the working tree at that HEAD (measured with `git status --short` over the cited paths).

Tags: **MEASURED** = read from a live response, a run of this folder's scripts, or source at the vintage above.
**INFERRED** = reasoned, not run.

---

## 0. The answer in one screen

1. **The "opaque redirect wrapper" label is stale. MEASURED on both dates.**
   - On 15 Sep, row AMGT_RESAPP-Z-W22-S1 found 10 of 10 organic links on one query in the form
     `https://www.google.com/goto?url=CAES...` (`INVESTIGATION_v1.md:5117-5125`).
   - Today, 50 of 50 organic links across 6 successful responses are direct destination URLs. That includes a
     byte-for-byte repeat of the exact legacy BA query, whose 2 links are both on `www.boeing.com`.
   - The wrapper form still appears in non-organic blocks: 12 occurrences, in `knowledge` and similar.
   - A wrapper is opaque offline (a protobuf blob with no URL inside), but **one un-followed GET to Google
     resolves it**: `302 Found`, `Location: https://en.wikipedia.org/wiki/Kelly_Ortberg` (1 of 1 tried).
   - So "the links do not expose a readable host" was never a property of the zone. The module never tried to
     resolve its links, and the form changes between dates.
2. **The estate primitive is wrong in both directions. MEASURED.**
   - `serp_brightdata` returned `[]` on 4 of 10 requests, and none of those 4 was an empty search: 3 were vendor
     captcha failures and 1 was a config error.
   - The one genuinely empty search (a person who does not exist) returned **9 URLs**, because Google dropped the
     quotes and answered a different query.
   - A vendor failure arrives as **HTTP 200 with a 0-byte body**; the failure shows only in headers.
3. **The curation step works, and the verbatim check discriminates. MEASURED over 3 CEOs and 4 runs.**
   - Every proposed fact whose status was recorded re-located verbatim: 101 of 101 (4 more were not recorded).
   - In the negative control, 163 of 163 one-word mutants of the kept quotes were rejected.
   - All the drops came from an identity rule that was too strict: 19 verbatim facts on 3 correctly identified
     pages. The rule is corrected below.
4. **For a common name, the role term in the query is what makes identity work. MEASURED on Halliburton.**
   - `"Jeff Miller" "Halliburton"` returned 0 of 9 results about him. They were obituaries of people surnamed
     Halliburton, a foundation blog, and another employee's LinkedIn.
   - `"Jeff Miller" Halliburton CEO` returned 9 of 9 (plus one contact broker, dropped).
5. **Model cost, measured: US$0.126 to US$0.173 per CEO (mean US$0.141).** That is about US$4.2 to US$5.7 at 33
   names. The SERP dollar price is UNMEASURED: no response header or estate record I searched carries it.

---

## 1. The instrument, measured

### 1.1 How the key and zone reach the process (MEASURED, source)

- The key is `comp-secrets get find-insure/bright-data/api-key` (opaque, 36 characters).
- The zone config is `comp-secrets get find-dualbiz/bright-data/serp`, a JSON object with keys
  `api_key_secret, endpoint, zone`: zone `serp_opal`, endpoint host `https://api.brightdata.com`, and
  `api_key_secret` naming the key secret above.
- The caller exports them as `BRIGHT_DATA_API_KEY` / `BD_SERP_ZONE`.
- `enrich._serp_module` (`enrich.py:370-381`) injects them into `serp.py`'s caches, so `serp.py:213-242` makes
  no Secrets Manager call.
- The probe (`probe_serp.py`) loaded the module exactly that way. It wrapped `urllib.request.urlopen` so that each
  query was **one production-path request**, capturing the full body, HTTP status and headers alongside what
  `serp_brightdata` returned. A ledger (`serp_ledger.jsonl`) counted every request before sending it and refused
  at 10.

### 1.2 All ten requests (MEASURED, `serp_q01..q10*.json`)

| # | query (form) | HTTP | x-brd-status | body | secs | `serp_brightdata` returned | truth |
|---|---|---|---|---|---|---|---|
| 1 | `site:boeing.com "Robert K. Ortberg"` (legacy, production form) | 200 | 200 | 6,998 B JSON | 28.0 | 2 urls | OK, 2 organic, both on boeing.com |
| 2 | `"Robert K. Ortberg" boeing.com chief executive officer` (W22-S1's own diagnostic, production form) | 200 | **502** | **0 B** | 55.5 | **[]** | **FAILED: captcha** |
| 3 | `"Robert K. Ortberg" "Boeing"` +gl=us&hl=en | 200 | 200 | 45,004 B | 9.2 | 10 | OK |
| 4 | `"Christian Klein" "SAP"` +gl/hl | 200 | 200 | 44,468 B | 7.0 | 10 | OK |
| 5 | `"Jeff Miller" "Halliburton"` +gl/hl | 200 | 200 | 15,261 B | 48.0 | 9 | OK (0 of 9 about him) |
| 6 | `"Jeff Miller" Halliburton CEO` +gl/hl | 200 | **502** | **0 B** | 10.0 | **[]** | **FAILED: captcha** |
| 7 | same as 6, immediate retry | 200 | 200 | 60,383 B | 11.1 | 10 | OK |
| 8 | `"Qwzxvor Plorbnikast" "Halliburton" "zq7731kx"` +gl/hl | 200 | **502** | **0 B** | 5.2 | **[]** | **FAILED: captcha** |
| 9 | same as 8, immediate retry | 200 | 200 | 24,041 B | 4.3 | **9 urls** | **EMPTY**: `spelling.original_empty: true`, query rewritten |
| 10 | `"Christian Klein" "SAP"`, zone `serp_opal_no_such_zone_probe` | **400** | none | 45 B `zone "..." not found` | 0.1 | **[]** | **FAILED: config** (raises `HTTPError`) |

### 1.3 What a response carries (MEASURED)

- **Content-Type:** `application/json` even with `"format": "raw"`. The zone returns parsed JSON by default, so
  no `brd_json` flag is needed.
- **Top-level keys:** `general, input, navigation, organic, pagination`, plus whichever of `knowledge, overview,
  people_also_ask, related, short_videos, spelling` the page had.
- **`organic[]` item keys:** `link, title, description, display_link, source, rank, global_rank, icon,
  snippet_highlighted_words, extensions`, and on video results `duration, duration_sec, image, image_url,
  image_base64`. **`serp_brightdata` keeps only `link`** (`serp.py:273-281`) and discards the title, snippet,
  source and rank an agent needs to judge relevance.
- **`general`** carries `query`, `detected_query`, `results_cnt`, `gl`, `language`, `country`, `timestamp`.
- **`num` is stripped.** Every request got header `x-brd-serp-warn: ... removed: num`, so `serp.py:257`'s
  `num=10` does nothing.
- **Locale defaults to Japan.** The production form (request 1) ran with `general.gl: "JP"`,
  `language: "en-JP"`, `country: "Japan"`. Adding `&gl=us&hl=en` gave `gl: "US"`, `language: "en"` on every
  request that carried it.

### 1.4 Link form: direct or wrapped (MEASURED)

- **Organic links:** 0 of 50 wrapped (requests 1, 3, 4, 5, 7, 9). All are direct destination URLs.
- **Wrappers in other blocks:** 12 `google.com/goto?url=` strings across the response bodies, for example
  `knowledge.description_link` in request 3.
- **Decoding offline:** the blob is 103 bytes starting `08 01 12 63` (protobuf). It has no printable run of 6 or
  more characters and no "http". **It cannot be decoded offline.**
- **Resolving by request:** one `curl` without `-L` to the wrapper returned `HTTP/1.1 302 Found`,
  `Location: https://en.wikipedia.org/wiki/Kelly_Ortberg`. **1 of 1 resolved.**
- **Why the 15 Sep objects read "none on the IR host".** Row W22-S1 recorded 10 of 10 organic links in wrapper
  form that day. The host test (`enrich.py:434`, identical at `deb16ee7d3`) is a substring test, and "boeing.com"
  does not appear inside an opaque blob. **The zone's link form changed between 15 and 18 Sep, or varies by
  request (INFERRED; two dates observed).** Either way, the design must resolve wrappers rather than assume
  either form.

### 1.5 Failed versus empty (MEASURED)

| outcome | how it arrives | what today's primitive does | what `enrich.py` then records |
|---|---|---|---|
| vendor failure (captcha) | HTTP 200, **0-byte body**; headers `x-brd-status-code: 502`, `x-brd-error-code: captcha`, `x-brd-error: redirect location was rejected` | `json.loads("")` raises, then `break` (`serp.py:269-272`), then `[]` | NOTHING_FOUND (`enrich.py:436-439`) -- **wrong** |
| config failure (bad zone) | HTTP 400, body `zone "<z>" not found`, no x-brd headers, `HTTPError` | `except Exception: break` (`serp.py:264-268`), then `[]` | NOTHING_FOUND -- **wrong** |
| genuinely empty | HTTP 200 JSON with `spelling.original_empty: true` and `general.detected_query != general.query`; `organic[]` is **non-empty**, holding results for Google's rewritten query | returns those URLs (9 here) | would treat unrelated company pages as results -- **wrong** |
| ok | HTTP 200 JSON, `x-brd-status-code: 200`, `detected_query == query`, `organic[]` non-empty | returns links only | -- |

- **Failure rate today:** 3 of 9 requests to the real zone failed on captcha. Both immediate retries succeeded
  (2 of 2).
- **Is a failed request billed?** UNMEASURED. No billing header is present.
- **Does a literal `organic: []` happen?** Not observed in 7 successful responses. INFERRED: with the company
  named in the query, Google rewrites rather than returning nothing, so "nothing about this person" has to be
  decided by the identity test, not by the result count.

---

## 2. The prototype, per CEO

**Pipeline** (`curate.py`). Everything runs from the captured SERP sets; no further SERP call is made.

1. **Candidates.** Organic records carrying title, snippet, link, host and source, with wrappers resolved and
   duplicates removed. **Contact-broker hosts are dropped before anything sees them.**
2. **Call A (identity triage).** Over the SERP records only. Each result is judged SAME_PERSON, DIFFERENT_PERSON,
   COMPANY_ONLY or UNCERTAIN, given a source kind, and marked fetch or not.
3. **Fetch.** A direct HTTP GET of every kept result (no vendor): HTML to text, or PDF to text with `pypdf`. The
   contact scrub (`contact_scrub.py`) runs on the page text before the model sees it. The page must contain the
   surname.
4. **Call B (extraction).** Over surname-centred windows of each readable page. For each page: an identity quote,
   a "why kept", and facts, where **a fact is a topic label plus a verbatim quote and nothing else**. There is no
   paraphrase field, so the model has nowhere to add knowledge.
5. **Verify.** Every quote goes through the Thesis panel's own `lib.research.filings.passages.Locator`
   (`passages.py:82-120`: quote-map, casefold, whitespace collapse, minimum 12 characters) against the full page
   text.

- **Model:** `claude-opus-5`, effort `medium`, JSON-schema structured output, streamed.
- **Names:** BA and SAP use the name on the filing roster. HAL's roster is UNRESOLVED-SOURCE with 0 officers, so
  its name was supplied for the prototype; in production it would come from card 1's Bloomberg fallback roster.

### 2.1 SAP -- Christian Klein (query 4)

- **Triage:** 10 of 10 results SAME_PERSON, 5 marked for fetch.
- **Fetch:** 4 readable: `de.linkedin.com` (32,166 characters, a plain GET), `en.wikipedia.org`, `sap.com`
  leadership, `morganstanley.com`. Unreadable: stratechery.com, **HTTP 429**.
- **Facts:** 24 proposed, **24 verified, 0 dropped.** No identity failures.
- **Model cost:** US$0.1262 (12,720 in, 2,502 out).

Abridged output:

- **official_bio** `https://www.sap.com/about/company/leadership/christian-klein.html` (7 facts)
  - tenure: "Joined SAP: 1999 Appointed to Executive Board: 2018 Current Executive Board term expires: 2030"
  - current_role: "In his role, Klein holds the overall responsibility for the corporate strategic direction,
    management, and performance of SAP."
- **reference** `https://en.wikipedia.org/wiki/Christian_Klein` (8)
  - prior_role: "Klein started his career at SAP in 1999 as a student."
  - tenure: "Since October 2019, both Christian Klein and Jennifer Morgan were co-CEOs of SAP SE."
- **professional_profile** `https://de.linkedin.com/in/christian-klein` (4)
  - current_role: "As Chief Executive Officer and chairman of the Executive Board of SAP SE, I am responsible
    for the strategic direction, management, and performance of SAP."
  - other: "Walldorf, Baden-Wurttemberg, Deutschland". **This is a personal location line; see s.3.5.**
- **news_profile** `https://www.morganstanley.com/insights/videos/exceptional-leaders/sap-CEO-christian-klein` (5)
  - tenure: "When Christian Klein took the helm as the sole CEO of SAP in early 2020, he made headlines, ..."

### 2.2 Boeing -- Robert K. Ortberg (query 3; two runs)

- **Triage:** 10 of 10 SAME_PERSON, 8 marked for fetch, **identical in both runs**.
- **Fetch:** 6 readable, including the Senate testimony PDF (2 pages). Unreadable: bloomberg.com and nytimes.com,
  both **HTTP 403**.
- **Facts:** run 1 had 28 proposed and 24 verified; run 2 had 23 proposed and 20 verified.
- **Drops:** in both runs, the Senate testimony page was dropped whole by the old identity rule. In run 2 its
  identity quote was "Written Testimony of Robert K. Ortberg Senate Committee on Commerce, Science &
  Transportation" (surname yes, "Boeing" no). **Its 3 facts all re-located verbatim.**
- **Model cost:** US$0.1377 and US$0.1272.

Abridged output (run 2):

- **reference** `https://www.encyclopediadubuque.org/index.php/ORTBERG,_Robert_K._(Kelly)` (8)
  - education: "Robert received a bachelor's degree in mechanical engineering from the University of Iowa in
    1982."
  - prior_role: "Ortberg joined Rockwell Collins Inc. in 1987."
- **news_profile** `https://www.upi.com/Top_News/US/2024/07/31/Boeing-board-new-CEO-Ortberg/4141722429750/` (4)
  - prior_role: "Ortberg has 35 years of aerospace executive experience. He started as an engineer with Texas
    Instruments in 1983, then joined Rockwell Collins in 1987."
- **news_profile** `avitrader.com` (4) and `gbp.com.sg` (1)
  - tenure: "Robert K. Ortberg as been elected as Boeing's new President and Chief Executive Officer,
    effective August 8, 2024". **The source's own typo is kept, which is what verbatim means.**
- **professional_profile** `vectorshift.ai` (3)
  - prior_role: "Following Rockwell Collins' integration into United Technologies, he served as CEO of Collins
    Aerospace and later as a special advisor to RTX Corporation."
- **Found but not read:** bloomberg.com/profile/person/15126894 ("Kelly Ortberg, Boeing Co: Profile and
  Biography", HTTP 403); nytimes.com (HTTP 403).

### 2.3 Halliburton -- Jeff Miller (the common-name case; queries 7 and 5 combined, 19 candidates)

- **Contact broker dropped by host before triage:** 1 (`zoominfo.com`). Its snippet carried **masked** contact
  fields. The first text scrub missed masked forms; it was widened and all saved files were re-scrubbed, leaving 0
  email-shaped tokens.
- **Identity triage, split by query:**
  - `"Jeff Miller" Halliburton CEO`: **9 of 9 SAME_PERSON**.
  - `"Jeff Miller" "Halliburton"`: **0 of 9**. Five were DIFFERENT_PERSON: three obituaries of people surnamed
    Halliburton, the Grant Halliburton Foundation blog, and another Halliburton employee's LinkedIn. Four were
    COMPANY_ONLY: the company's Wikipedia article, company history, company Facebook, company X.
  - **The collision here was the company name doubling as a surname**, not a second Jeff Miller.
- **Fetch:** 8 readable of 8, including `linkedin.com/in/jeff-miller-b391a372` (11,802 characters, a plain GET).
  The YouTube page gave only 241 characters (the title).
- **Facts:** 30 proposed, 14 kept, 16 dropped.
- **All 16 drops came from 2 pages dropped whole by the old identity rule**, and **16 of 16 of their facts
  re-located verbatim.** The two pages were the person's own Wikipedia article and `halliburton.com/en/authors/
  jeff-miller`. Their identity quotes used a pronoun or a title line ("He is the chief executive officer ... of
  Halliburton ..."), so they lacked the surname.
- **Model cost:** US$0.1734 (15,465 in, 3,843 out).

Abridged output:

- **official_bio (company host)** `https://www.halliburton.com/en/about-us/halliburton-leadership` (4)
  - prior_role: "Since joining Halliburton in 1997, Miller has served in several roles, including Chief
    Operating Officer, Senior Vice President of Business Development, ..."
  - education: "Miller holds a Bachelor of Science in agriculture and business from McNeese State University in
    Lake Charles, Louisiana, and a Master of Business Administration from Texas A&M University."
- **news_profile** `worldoil.com` (2)
  - board_or_outside_role: "Noble Corporation has appointed Jeff Miller to its board of directors, ..."
- **"official_bio" per the model, but a third-party host:** `business.rice.edu` (4) and `adipec.com` (3). These
  repeat the company boilerplate: 3 duplicate quotes across items.
- **interview_or_talk** `youtube.com/watch?v=_lAaySqe3gw`: a link with 0 facts; identity was quoted from the
  page title.
- **professional_profile** `linkedin.com`: 1 fact, topic "other", "Houston, Texas, United States". **A personal
  location line; see s.3.5.**

### 2.4 Totals and controls (MEASURED)

| | SAP | BA r1 | BA r2 | HAL | total |
|---|---|---|---|---|---|
| candidates | 10 | 10 | 10 | 19 | -- |
| broker hosts dropped | 0 | 0 | 0 | 1 | 1 |
| triage SAME / DIFF / COMPANY_ONLY | 10/0/0 | 10/0/0 | 10/0/0 | 9/5/4 | -- |
| fetched / readable | 5/4 | 8/6 | 8/6 | 8/8 | 29/24 |
| facts proposed | 24 | 28 | 23 | 30 | 105 |
| facts kept (as run) | 24 | 24 | 20 | 14 | 82 |
| facts dropped by the verbatim check | 0 | 0 | 0 | 0 | **0** |
| facts dropped by the old identity rule (all re-located) | 0 | 4 (not recorded) | 3 (3 of 3 re-locate) | 16 (16 of 16 re-locate) | 23 |
| contact strings in the kept output | 0 | 0 | 0 | 0 | 0 |
| model US$ | 0.1262 | 0.1377 | 0.1272 | 0.1734 | 0.5644 |

- **The verbatim check discriminates** (`verbatim_control.py`). The 58 kept quotes of the final SAP, BA r2 and HAL
  profiles all re-locate. **163 of 163 one-word mutants are rejected:** drop 57/57, swap 54/54, splice 52/52.
- **A deterministic identity anchor** (`identity_offline.py`): the surname and company token must fall within N
  characters in the fetched text. It needs no model.
  - Positive arm: 17 of 18 identity-confirmed pages pass at N=300. The miss is the Senate PDF at 313, so **18 of
    18 pass at N=500**.
  - Negative arm: **4 of 4 readable DIFFERENT_PERSON pages fail it.** None of them contains "Miller" at all. The
    fifth was unreadable (HTTP 403).
  - The 2 COMPANY_ONLY pages that pass (the company's Wikipedia article and its X account) do name *this* Jeff
    Miller as CEO. So the anchor settles *identity*, and *relevance* stays the model's call.
- **Not measured:** a page about a *different* Jeff Miller that also names Halliburton nearby. The company term in
  the query suppressed such pages, so none appeared.

---

## 3. Implementation design

### 3.1 The search primitive -- structured, FAILED distinct from EMPTY

**Change point:** `data/find/dualbiz/scripts/serp.py:245-286`.

It has **three production callers** (MEASURED census of every `*.py` in the repo):
- `serp.py:47` (`serp_search`, which feeds `harvest_query` and the FIND_DUALBIZ sweeps at `:175`, `:198` and
  `:308`);
- `data/find/dualbiz/scripts/casec.py:80`;
- `lib/research/management/enrich.py:430`.

The first two expect `list[str]`, so **do not change `serp_brightdata`'s return type.** Instead:

- **Add** `serp_brightdata_records(query, max_pages=1, gl="us", hl="en", retries=2) -> dict` beside it.
  - The request is the same POST to `https://api.brightdata.com/request` with zone `_bd_serp_zone()` and
    `"format": "raw"`.
  - The URL is `https://www.google.com/search?q=<q>&gl=us&hl=en`. **Drop `num=10`**, which Bright Data strips
    (MEASURED 10 of 10).
  - Classify each attempt from the measured shapes in s.1.5:

    ```
    FAILED  <- transport exception | HTTP >= 400 | x-brd-status-code != 200 | x-brd-error present
               | 0-byte body | body not JSON
    EMPTY   <- JSON parses AND (organic == [] OR spelling.original_empty is true)
    OK      <- otherwise
    ```

  - **Retry policy:** retry only a FAILED attempt whose `x-brd-error-code` is `captcha` or whose status is 5xx,
    up to `retries` times with a short backoff (MEASURED 2 of 2 immediate retries succeeded). Never retry an HTTP
    4xx (a config error).
  - **Returns:**
    ```
    {status: OK|EMPTY|FAILED,
     failure: {kind: VENDOR|CONFIG|TRANSPORT|UNPARSEABLE, http_status, brd_status, brd_error_code, brd_error}|null,
     attempts: [{http_status, brd_status, brd_error_code, seconds}],
     query, detected_query, query_rewritten, original_empty, gl, results_cnt,
     records: [{rank, link, link_form: DIRECT|WRAPPED_RESOLVED|WRAPPED_UNRESOLVED, host, title, snippet,
                display_link, source}]}
    ```
  - `records` holds whatever `organic[]` holds, with `snippet` taken from `description`. On EMPTY with a rewrite
    the records are kept but flagged: they answer `detected_query`, not `query`.
  - **Contact keys:** run `enrich.scrub` over the parsed body, and **exempt `general.mobile`**. It is a device
    flag the stem scrub removes (MEASURED: it was the only key removed, on every successful body).
- **Wrapper resolution** is a separate helper: one GET without redirect-following, reading `Location`
  (MEASURED 1 of 1). It is applied only to `google.com/goto?url=` links. A failure leaves the link
  `WRAPPED_UNRESOLVED`, which is the only way the "links unreadable" state can now arise.
- **`serp_brightdata` becomes a wrapper:** `[r["link"] for r in serp_brightdata_records(...)["records"]]`.
  - It prints a `WARN:` line on FAILED, so FIND_DUALBIZ's captcha silence becomes visible without a change to its
    contract.
  - Whether FIND_DUALBIZ should *stop* on FAILED is its owner's call. **Lane note for the L4:** `serp.py` belongs
    to the FIND_DUALBIZ pipeline, not AMGT_RESAPP, so this edit needs that owner's lane.

### 3.2 The curation step -- where it sits

- **New module `lib/research/management/ceo_search.py`.** It keeps `enrich.py` readable and gives the step its
  own tests.
  - `ceo_profile(ceo, company, verified_domain, serp=None, model=None, fetcher=None) -> dict`
    1. **Not searched.** No CEO: return `NOT_SEARCHED` with `reason_code: NO_CEO_ON_ROSTER`, or
       `ROSTER_UNRESOLVED` when the roster is empty.
    2. **Query.** `"<search name>" <company short name> CEO` (s.3.4). Call `serp_brightdata_records`. FAILED
       returns `SEARCH_FAILED` with the failure record. EMPTY (original_empty) returns `NOTHING_FOUND`,
       `reason_code: ORIGINAL_EMPTY`.
    3. **Brokers.** Drop contact-broker hosts. A deny list is the floor; the better form is an allow-list by
       source kind (s.5, risk 6).
    4. **Call A**, identity triage over the SERP records. If 0 results are SAME_PERSON or UNCERTAIN, return
       `NOTHING_FOUND`, `reason_code: NO_RESULT_ABOUT_PERSON`, with the triage counts.
    5. **Fetch** SAME_PERSON results marked for fetch, directly with a browser UA; PDF via `pypdf`. Contact-scrub
       the text. Apply the **identity anchor**: surname and company token within 500 characters in the page
       text. A page that fails goes to `not_kept` with that reason.
    6. **Call B**, extraction over surname-centred windows (each a substring of the page text, capped at 7,000
       characters per page as prototyped).
    7. **Verify** with `passages.Locator`. A fact whose quote does not re-locate is dropped and counted. **The
       identity quote must re-locate, but need not itself carry the surname and company**: that job moves to
       the deterministic anchor in step 5. MEASURED: the old rule dropped 3 of 18 correctly identified pages and
       19 verbatim facts.
    8. **Status.** `CURATED` if at least one item is kept. `UNREADABLE` if results were about the person but no
       page could be read and verified. Results about the person that could not be read go to `found_not_read`
       with the reason (HTTP 403, 429 or 999, or `WRAPPED_UNRESOLVED`).
  - **Deterministic post-processing:**
    - `source_kind == official_bio` only when the host is the **verified company domain** (brief s.8.2) or a
      subdomain of it. Any other bio page is `third_party_bio`. MEASURED: the model labelled 2 of 3 HAL
      third-party hosts `official_bio`.
    - Duplicate facts are removed by normalised quote, with the official host first and the others listed as
      "also stated at". MEASURED: 3 duplicate quotes across HAL's boilerplate bios.
    - A final contact check runs over the serialised block: 0 or the object is not written, the same discipline
      as `validate` at `enrich.py:460-472`.
- **Call site: `enrich.py:532-536`.** Replace `document["ceo_public_profile"] = ceo_public_profile(...)` with
  `document["ceo_profile"] = ceo_search.ceo_profile(find_ceo(officers), ...)`.
  - Keep `find_ceo` (`enrich.py:384-388`). With card 1, it must also read a `BLOOMBERG_FALLBACK` roster's
    officers.
  - Resolve every dependency **before** the first billable call, as `enrich.py:507-512` already requires after
    row W22-S2.
  - Retire `ceo_public_profile` (`enrich.py:391-453`) and `_serp_module`'s use for it.
  - The `SERP:` print line at `enrich.py:666-669` changes to print `ceo_profile.status`, the reason and the
    counts.
- **Batch.**
  - `batch.py:128` already routes through `build_document`, so it needs no change.
  - The key comment at `run_batch.cmd:7-8` gains `ANTHROPIC_API_KEY`, exported from
    `comp-secrets get anthropic-api-key --reveal` in the same call, the way `analyze.py:34` and `:226` describe.
  - The module never reads a secret store itself.
- **Model call.** It uses the one-seam form of `analyze.py:219-243` (`anthropic_call`: streamed,
  `output_config`) so tests stub it. It adds `output_config.format` JSON schema, and it checks `stop_reason`
  before parsing (prototype: 8 of 8 `end_turn`).

### 3.3 The block -- `ceo_profile` replacing `ceo_public_profile`

**Schema change points:** `lib/research/management/management.schema.json`
- `:14` (required list): swap `ceo_public_profile` for `ceo_profile`.
- `:65-67` (the property).
- `:142-160` (the `ceo_profile` definition). Its text at `:155-158` also carries the "opaque redirect" claim this
  exploration found stale.

The schema stays closed (`additionalProperties: false`) with the same `not` clauses against email, phone and
mobile at the block and item levels.

```
ceo_profile:
  status:       CURATED | NOTHING_FOUND | UNREADABLE | SEARCH_FAILED | NOT_SEARCHED
  reason_code:  null (CURATED) | NO_CEO_ON_ROSTER | ROSTER_UNRESOLVED | STEP_NOT_CONFIGURED
                | ORIGINAL_EMPTY | NO_RESULT_ABOUT_PERSON | NO_PAGE_READABLE
                | VENDOR_FAILURE | CONFIG_FAILURE | TRANSPORT_FAILURE
  reason:       one sentence, the module's own words
  ceo_name, name_source (FILING | BLOOMBERG_FALLBACK), company, role
  search: {instrument, query, detected_query, query_rewritten, original_empty, gl, hl,
           attempts[{http_status, brd_status, brd_error_code, seconds}], results_returned, searched_at}
  triage: {model, prompt_version, same_person, different_person, company_only, uncertain, broker_dropped}
  items[]:  {url, host, title (the page's SERP title), source_kind (official_bio | third_party_bio |
             professional_profile | reference | interview_or_talk | news_profile), why_kept,
             identity: {anchor_distance_chars, quote, verified: true},
             read: {http_status, content_type, chars, sha256_16, fetched_at},
             facts[]: {topic, quote, char_range}}         <- the quote IS the fact; no paraphrase field
  found_not_read[]: {url, host, title, source_kind, reason}   <- links only, never facts
  counts: {results, about_person, pages_read, facts_proposed, facts_verified, facts_dropped_unverified,
           contact_strings_scrubbed}
  cost:   {serp_requests, fetches, model_input_tokens, model_output_tokens, model_usd}
  generated_at
```

**Fact topics:** `current_role, prior_role, tenure_or_appointment, education, board_or_outside_role,
stated_view_or_priority`. **No `other`.** MEASURED: 3 `other` facts were produced, 2 of them personal location
lines from LinkedIn and 1 a lead sentence.

**Two axes, not six categories.** The brief's s.9.2 item 6 list (official bio, professional profile, prior roles,
board and outside roles, interviews and talks, news profiles) mixes a SOURCE axis with a FACT axis. That breaks
Rule 24 (iii), one axis per intent. One page usually carries several fact topics: HAL's Rice page had prior
roles, education and board roles. So `source_kind` sits on the item and `topic` on the fact, and the tab can
group either way.

### 3.4 The identity test

- **Query form: `"<search name>" <company short name> CEO`.**
  - MEASURED: without the role term, the common-name query returned 0 of 9 results about him; with it, 9 of 9.
  - For distinctive names, the quoted-pair form was already 10 of 10 (BA, SAP).
- **Name form.** OPEN, INFERRED. The roster's legal name worked for "Robert K. Ortberg". Roster forms such as
  "EDWARD P. DECKER", "R. Lane Riggs" and "Eddie Yongming WU" may lose recall to an exact phrase with a middle
  initial. The L4 should settle between the roster name, given name plus surname, or the quoted surname with the
  company and role. The SERP budget did not allow measuring this.
- **Company short name:** strip legal suffixes (The / Inc / Corporation / Company / SE / plc / Holding(s) /
  Group) from the crosswalk entity name. INFERRED; the prototype used hand-shortened names.
- **Layer 1, triage (model, SERP records only):** SAME_PERSON / DIFFERENT_PERSON / COMPANY_ONLY / UNCERTAIN. The
  prompt forbids memory: a record that does not itself tie the name to the company is not SAME_PERSON. MEASURED:
  it separated 5 of 5 other-person results and 4 company-only results on HAL.
- **Layer 2, page anchor (deterministic):** surname and company token within 500 characters in the fetched text.
  MEASURED: 18 of 18 positives, 4 of 4 readable negatives rejected.
- **Layer 3, identity quote (model, verified):** a passage that re-locates verbatim, shown on the page as the
  reason the item belongs to this person.
- **Uncovered:** a *different* person with the same name at the *same* company or in the same industry. Layers
  2 and 3 would pass such a page, so only layer 1 guards it, and that is unmeasured (s.5, risk 3).

### 3.5 Contact data

- **Pre-triage:** contact-broker hosts are dropped (MEASURED: zoominfo.com appeared, with masked email, phone and
  mobile in its snippet).
- **Page text:** scrubbed before the model sees it, for emails, phones and labelled contact fields, **including
  masked forms** (`contact_scrub.py`).
- **Model:** the prompt forbids quoting contact details.
- **Before any write:** a deterministic check over the serialised block, where 0 is required. MEASURED: 0 in all
  four outputs.
- **Location lines:** "City, Region, Country" lines from a personal profile are not in the forbidden set, but
  they are not career facts either. Dropping the `other` topic removes the measured cases. **The L4 should say
  whether residence is ever shown.**

### 3.6 Adapter

- **`scoped_amgt.read_management` (`:2305-2371`):** add `"ceo_profile": document.get("ceo_profile")` to the block
  at `:2366-2368`, served verbatim.
- **`ceo_profile_reading` (`:2264-2302`):** replace it with a reader keyed on `ceo_profile.status` and
  `reason_code`, so no sentence is parsed any more (today it regex-parses `basis` at `:2272` and `:2290`). Delete
  the claim at `:2282-2284`, "on this SERP zone returned links are opaque redirect wrappers". That claim is
  measured false today and was never true of the links as such.
- **Legacy objects** (the 12 served today still carry `ceo_public_profile`) map honestly, per brief s.4 item 1:

| legacy object | reads |
|---|---|
| `status: RESOLVED` | CONFIRMED_LEGACY_LINK |
| `absence_class` NOTHING_FOUND whose basis names no search (7 objects) | NOT_SEARCHED with the basis as reason |
| the 4 searched 15 Sep objects, with no `absence_class` field | SEARCHED_LINKS_UNREADABLE_LEGACY, citing row W22-S1 |

- **Tests:** `lib/research/api/tests/test_generation_and_pool_routes.py:439-462` and
  `lib/research/management/tests/test_management.py:422-454` pin today's behaviour and must be rewritten.

### 3.7 The tab

- **`portal/src/pages/SecurityAnalysis/types.ts:667-684`:** replace `CeoPublicProfile` and `CeoProfileReading`
  with a `CeoProfile` type mirroring s.3.3.
- **`ManagementBlock` (`:712-713`):** gains `ceo_profile`.
- **`ExecManagementTab.tsx`:** replace the `CeoProfile` component at `:70-93`, including the wrong
  "links ... do not expose a readable host" sentence at `:84-87`, and its header claim at `:15-19`. The new
  component renders by status:

| status | what the page shows |
|---|---|
| **CURATED** | Items grouped by `source_kind`, official bio first. Each shows the host, a link, the title and "why kept". Its facts are **verbatim quotes in quotation marks** with a topic label, so a reader sees these are the source's words. A collapsed "found but not read" list shows links with their reason. A one-line provenance footer gives the query, the date and "N of M facts re-located verbatim". |
| **NOT_SEARCHED** | "CEO profile: not searched -- <reason>" (no CEO on the roster, roster unresolved, step not configured). |
| **NOTHING_FOUND** | "Searched <query> on <date>: <reason>." Either "no page matched the exact name" (ORIGINAL_EMPTY) or "<n> results, none about <name> at <company>" (NO_RESULT_ABOUT_PERSON). |
| **UNREADABLE** | "Searched: <n> results about <name>, none could be read (<reasons>)", with the links listed unread. |
| **SEARCH_FAILED** | "The search did not complete (<vendor or config error>, <attempts> attempts) -- this is not evidence that nothing exists." |

- **The harness:** `__harness__/tabs.harness.cjs:273` and the five `tabsFixture.*.json` read
  `ceo_profile_reading`, so they change too.
- **Verification:** portal law (`portal/CLAUDE.md`) requires `/frontend-dev` screenshot verification before
  commit.
- **Served output:** this moves served output, so it needs the CTO+COO never-widen pair (brief s.4 item 1).

### 3.8 Contract amendment -- replacing `enrich.py:13-15`

Proposed text, for the same amendment as cards 1 and 2 (ratified-text half, CVO signs):

> - the CEO's public profile is ONE Bright Data SERP search for the CEO's name with the company and the role
>   (`serp_brightdata_records`: one page, gl=us, up to two retries on a vendor failure, never on a configuration
>   error), followed by a curation step: a model keeps only the results about THIS person at THIS company in THIS
>   role (judged from each result's own title and snippet, never from the model's memory), the kept pages are
>   fetched directly, a page is used only when its own text names the person within 500 characters of the
>   company, and every fact shown is a quote that re-locates VERBATIM in the fetched page
>   (`lib/research/filings/passages.Locator`); a fact that does not re-locate is dropped and counted, and the
>   model adds nothing of its own;
> - the block carries its status -- CURATED, NOTHING_FOUND, UNREADABLE, SEARCH_FAILED or NOT_SEARCHED -- and its
>   reason; a failed search is never recorded as an empty one, and a query Google rewrote is never read as an
>   answer to the query that was sent;
> - "official biography" means a page on the company domain verified by the filings battery; any other
>   biography is a third-party biography;
> - the NO-CONTACT-DATA rule extends to every page this step reads: contact-broker hosts are never fetched, page
>   text is scrubbed before any model sees it, and the written block is checked for contact strings before it
>   is stored.

---

## 4. Cost per CEO, measured -- and at 33 names

| component | per CEO | basis |
|---|---|---|
| SERP requests | 1 query; **about 1.5 requests** expected with retries | MEASURED: 3 of 9 real-zone requests failed on captcha, and 2 of 2 retries succeeded. Whether a failed request is billed is UNMEASURED. |
| SERP US$ | **UNMEASURED** | No price header in any response. No price in `*.md` across the repo or in the AMGT_RESAPP ledger (searched). The account's billing console is the instrument. |
| page fetches | 5 to 8 GETs, **US$0** | MEASURED: SAP 5, BA 8, HAL 8. 3 of 21 unreadable (403, 403, 429). Direct HTTP, no vendor. |
| model: call A (triage) | US$0.030 to 0.047 (2.8k to 4.0k in, 0.6k to 1.1k out) | MEASURED, 4 calls |
| model: call B (extraction) | US$0.096 to 0.126 (7.8k to 11.5k in, 1.9k to 2.7k out) | MEASURED, 4 calls |
| **model total** | **US$0.126 to 0.173, mean US$0.141** | MEASURED, 4 runs, `claude-opus-5` at US$5 / US$25 per MTok, effort medium |
| wall time | about 40 s model + 4 to 55 s SERP + fetches | MEASURED |

**At 33 names:** model **about US$4.66** (33 x 0.141; range US$4.16 to US$5.72), SERP about 33 to 50 requests at
the plan's unmeasured unit price, fetches free. INFERRED: cost scales with how much the pages say, not with the
name count alone. HAL, with 19 candidates and 8 pages, was the most expensive.

---

## 5. Risks and open questions, ranked

1. **Vendor failures are common and silent today.**
   - MEASURED: 3 of 9 captcha failures, each returned by the estate primitive as `[]`.
   - Until s.3.1 lands, every CEO result from that primitive is unreliable in both directions. That includes the
     served NOTHING_FOUND objects. It is also why the four 15 Sep "searched" objects cannot be trusted either
     way.
   - Whether failed requests are billed is unmeasured.
2. **The link form is not stable across dates.**
   - MEASURED: wrapped on 15 Sep, direct on 18 Sep.
   - The resolver needs one extra GET to google.com per wrapped link. It is proven on 1 of 1 and unproven at
     volume; Google may captcha that GET too.
3. **Identity against a same-name, same-industry namesake is unmeasured.**
   - Only layer 1 (model triage) guards it. The company-term query suppressed such pages, so this run could not
     test it.
   - The L4 should add a planted-namesake case to the step's test fixtures.
4. **Readable pages are not guaranteed.**
   - MEASURED: bloomberg.com and nytimes.com returned 403; stratechery.com returned 429.
   - An unlocker would likely read them, but Andrew's cost ruling (`docs/architecture/FIND_DUALBIZ_PRD.md:47`:
     never route through `one_shotter`, `serp_opal` only) makes that **his call**. They are shown as "found but
     not read" meanwhile.
5. **Fetching LinkedIn directly.**
   - MEASURED: 2 of 2 LinkedIn profiles were readable by a plain GET today (32,166 and 11,802 characters).
   - That is a terms-of-service and robustness question: LinkedIn commonly answers 999. Lusha already supplies the
     LinkedIn URL for matched officers. **Recommend: LinkedIn is link-only, never fetched, unless Andrew says
     otherwise.**
6. **Contact data enters through snippets and pages, not only fields.**
   - MEASURED: ZoomInfo's snippet carried masked email, phone and mobile, and the first regex scrub missed the
     masked forms.
   - Recommend an **allow-list of source kinds and hosts by class** over a growing broker deny list.
7. **Model labels that should be facts of the host.**
   - MEASURED: `official_bio` was wrong on 2 of 3 HAL hosts. Settle it deterministically from the verified
     domain, which makes the official-biography category depend on brief s.8.2.
8. **Prompt injection via page text.**
   - Verbatim-only display bounds the damage: nothing the model writes is shown except `why_kept` and labels.
     But a hostile page can still supply a quote about itself.
   - The identity anchor and triage limit which pages get that chance. INFERRED; untested.
9. **Name and company forms in the query** (s.3.4). Unmeasured beyond these three names.
10. **Cost.** About US$4.7 of model spend at 33 names is measured and small. The SERP unit price is the unknown
    to read from the account before any scale.

**Open for Andrew or the L4:**
- (a) Show "found but not read" links on the page? Recommend yes, labelled; they are links, never facts.
- (b) LinkedIn fetch policy (risk 5).
- (c) Unlocker for 403 and 429 pages (risk 4, his cost ruling).
- (d) Name form in the query (s.3.4).
- (e) Whether residence or location lines are ever shown (s.3.5).
- (f) Whether the running three-name validation exercises this step. That is still his open question from the
  addendum, and it is not answered by this exploration.

---

## 6. Files in this folder

| file | what it is |
|---|---|
| `probe_serp.py`, `run_probe.sh` | the SERP probe (production path, urlopen wrapped, 10-request ledger) and its secret-exporting runner |
| `serp_q01..q10_*.json`, `serp_ledger.jsonl` | the 10 raw captures, contact-scrubbed (0 email-shaped tokens left), and the request ledger |
| `curate.py`, `contact_scrub.py` | the curation prototype and the masked-form contact scrub |
| `ceo_profile_SAP.json`, `ceo_profile_BA.run1.json`, `ceo_profile_BA.json`, `ceo_profile_HAL.json` | the four outputs with ledgers, kept items, not-kept reasons and usage |
| `pages/*.txt` | the 18 read pages' scrubbed text, for re-verification |
| `model_spend.jsonl` | 8 model calls with usage, US$0.5644 total |
| `identity_offline.py`, `verbatim_control.py` | the deterministic-anchor test and the verbatim negative control |
| `read_served.py`, `served_profiles.json` | the read-only census of the 12 served management objects' CEO blocks |
