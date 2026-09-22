# AMGT_HARVST -- PRD (L4)

```json
{
  "project": "AMGT_HARVST",
  "directive": "D5",
  "fabric": "site-z",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "org/missions/D5/AMGT/AMGT_HARVST/brief/BRIEF_AMGT_PUBLICATIONS_BRONZE_SILVER_GOLD_20260922.md@48f31e8fd0",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8"
  ],
  "status": "RATIFIED"
}
```

**author** `1.0.0_SA_CTO~Z` (L2 endpoint and L4 PRD). **driver** `2.0.0_SA_COO~Y` (L5, L6, to completion).

| | |
|---|---|
| **Directive** | D5 Asset Management (placement SITEZ) |
| **Macro** | `AMGT` |
| **L1 brief** | `4.0.0_SA_CRO~Z`, `BRIEF_AMGT_PUBLICATIONS_BRONZE_SILVER_GOLD_20260922.md` at its tree home `org/missions/D5/AMGT/AMGT_HARVST/brief/` @`48f31e8fd0`, byte for byte the deliverable @`fefee2f360` |
| **Andrew's words** | the brief's record @`ac8a4965c4` (retrieval, structure, bronze/silver/gold, gold metrics, the timeline); the project record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_144xZ_AMGT_HARVST_NEW_PROJECT_COO_Y_DRIVES.md` @`e279a48e4e` ("make a new project for this called AMGT_HARVST ... have COO~Y drive it to completion") |
| **Sibling** | `AMGT_RESAPP` (the Security Analysis page). This project owns the publication channels; that one owns the page's other channels and the Lenovo trial |

### The problem, in Andrew's words (from the brief's record)

*"when searching for the tickers on the various channels, we are picking up literally any time they are mentioned and as
a result it is much lower signal."* *"Bronze we simply need to know what we're getting. Silver we need to make sure that
these things are organized in clean queryable format with no fidelity loss, just standard typing. Gold is where we start
to get into mention count, and other analytical factors."* He asked for *"a timeline graph of all mentions where we can
dissect them at any point"*, categorised by strength of signal (*"how much the security is mentioned in them, is it
mentioned in headline?"*) and by time.

**Measured by the brief on this desktop's 84 links** (3 securities, 5 publishers):
- 19 of 84 mention the company exactly once.
- 38 of 84 never name it in the title.
- The Chatter axis weights all 84 at 1.0.

The mention stays the floor, which is his tolerance. The grade goes in gold.

---

## ENDPOINT (step 2, /endpoint --forward)

`FWD-n` ids are PERMANENT and never reused. `DONE WHEN` is the bar, not the current state. Each outcome is provable by an
act a seat can take on demand; none is a wait.

```

  FWD-1  Every article we collect can be read again exactly as the publisher
         sent it
         DONE WHEN  EXERCISED -- for one run on the validation security, every
                    article from each of the five publishers, and the listing
                    page that found it, is re-opened from our store and matches
                    what was received, byte for byte
         ACCEPT     For any article we hold, we can show the publisher's own page
                    or response as it arrived, not only our cleaned copy of it.
         SOURCE     brief s.4.1, s.5; Andrew "Bronze we simply need to know what
                    we're getting"

  FWD-2  Everything a publisher tells us about an article is kept, in a clean
         queryable form, with nothing lost
         DONE WHEN  EXERCISED -- every field present in the received article
                    (including language, paywall flags, the publisher's own
                    ticker tags, sentiment, themes and summary where sent)
                    appears typed in the queryable table, rebuilt from the
                    stored original, and a query by company and date returns it
         ACCEPT     Someone can query the articles by company, publisher and
                    date and see every detail the publisher sent, without
                    anything having been summarised away.
         SOURCE     brief s.5; Andrew "clean queryable format with no fidelity
                    loss, just standard typing"

  FWD-3  For any article, we can say how we found it
         DONE WHEN  EXERCISED -- every stored article states whether it came
                    from the publisher's own list for that company or from a
                    search, with the search words and its position in the
                    results; a second run the same day fetches no article we
                    already hold
         ACCEPT     Asked why an article is attached to a company, we can show
                    how it was found, and re-running collection does not pull the
                    same articles again.
         SOURCE     brief s.3.3

  FWD-4  For any article and company, we can say how strongly the article is
         about that company
         DONE WHEN  EXERCISED -- every (article, company) pair carries whether
                    the company is in the headline, in the opening, how often it
                    is named, how much of the article names it, which other
                    covered companies it names, and a strength grade; the grade
                    is re-derived from the stored text and matches
         ACCEPT     For any article, someone can see at a glance whether it is
                    about the company or mentions it in passing.
         SOURCE     brief s.6.1; Andrew "how much the security is mentioned in
                    them, is it mentioned in headline?"

  FWD-5  An analyst sees a timeline of mentions for a company and can open any
         point to the articles behind it
         DONE WHEN  EXERCISED -- an analyst has opened a company's timeline, picked
                    a day, and read the articles behind it listed strongest first
         ACCEPT     On a company's page there is a day-by-day line of how much
                    it was written about; clicking any day shows the articles
                    behind that day, strongest first.
         SOURCE     brief s.6.2, s.6.4; Andrew "a timeline graph of all mentions
                    where we can dissect them at any point"

  FWD-6  The company's news events show up as spans on that timeline
         DONE WHEN  EXERCISED -- the timeline for the validation security shows
                    at least the event runs the stored articles support, each
                    with its lead headline, and opening one lists its articles
         ACCEPT     Bursts of real coverage about the company appear as marked
                    events with a headline, not just as spikes in a count.
         SOURCE     brief s.6.3 (the event spine; the record's addendum)

  FWD-7  The ranking of companies by chatter uses how strongly they were
         written about, not how many times they were named
         DONE WHEN  EXERCISED -- the chatter ranks on the page are computed from
                    the graded daily table, and a company named once in passing
                    in many articles no longer outranks one that was the subject
                    of a few
         ACCEPT     The "most talked about" list reflects coverage about the
                    company, not incidental mentions.
         SOURCE     brief s.6.2 (the axis base); field map A (all mentions count 1.0)

  FWD-8  Articles already collected but never delivered reach the store
         DONE WHEN  EXERCISED -- every article and link held only on the
                    collecting desktop is in the store, with none duplicated
         ACCEPT     Nothing we already collected is stranded on one machine.
         SOURCE     field map A (83 bodies, 84 links, 0 uploaded); brief s.1
```

---

## CONTRACTS -- v0.1 (ratified text; the reviewer is `3.0.0_SA_CVO`, always)

Every contract below is owned by this PRD's L4 author unless it names another seat. The cell that executes it is
assigned by the decomposition.

**`C-HV-BRONZE-AS-RECEIVED`.**
- Every publisher's article response is stored as the bytes received, one object per fetch, under
  `{source}/harvest/bronze/article/article_hash=<sha256("<publisher>:<article_id>")>/<stamp>.<ext>`. That is the
  builder's output, for example `s3://opal-data-harvest/wsj/harvest/bronze/article/article_hash=<h>`.
- The form per publisher:
  - Seeking Alpha, Bloomberg and Barron's: the JSON response.
  - WSJ and FT: the HTML page. The JSON embedded in the page is extracted in silver, never before bronze.
- The listing or search response that found the article is stored too, under
  `{source}/harvest/bronze/news_listing/date=<d>/...`, for example
  `s3://opal-data-harvest/seeking-alpha/harvest/bronze/news_listing/date=2026-09-22`.
- Each object records `received-form` in its S3 metadata.
- `AMGT_RESAPP`'s `C-BRONZE-AS-RECEIVED` binds here unchanged; this contract adds the three publishers whose bytes are
  kept by nothing today, and the listing.

**`C-HV-SILVER-FROM-BRONZE`.**
- The silver `article` table (`{source}/harvest/silver/article/date=<d>/part-<stamp>.parquet`, for example
  `s3://opal-data-harvest/wsj/harvest/silver/article/date=2026-09-22`) is built ONLY from bronze, and is replayable
  from it.
- Every vendor field present in bronze is kept with standard typing (string, int, bool, timestamp, list, struct).
  Nothing is filtered or summarised.
- Silver carries three clocks, never substituted for one another:
  - `published_utc`, `published_offset_min`, `published_date_utc` and `published_precision`;
  - `fetched_at`;
  - `first_discovered_at`.
- The listing hits land in `{source}/harvest/silver/listing_hit/date=<d>/`, for example
  `s3://opal-data-harvest/seeking-alpha/harvest/silver/listing_hit/date=2026-09-22`.
- This supersedes the silver writer as built in `AMGT_RESAPP` rk-85, which shapes the row from the 18-field normalised
  record.

**`C-HV-RETRIEVAL-PROVENANCE`.**
- Every silver row states `retrieval_rung` (`symbol_listing | name_search | ticker_search`), `search_query`,
  `search_rank` and `search_page`.
- A publisher's own per-symbol listing is used wherever one exists and works.
- A search pages only back to the newest `published_utc` already held for that (security, publisher).
- Dedupe is by `article_hash`, so a known article is never fetched twice.
- **The mention floor is unchanged:** one word-bounded mention of the company keeps the article. Retrieval never grades.

**`C-HV-LINK-IS-GOLD`.** Which company an article is about is Opal's judgement, so it lives in gold, never in silver.

**`C-HV-MENTION-GRADE`.**
- The gold `article_security_mention` table has one row per (article, security), at
  `amgt/harvest/gold/article_security_mention/date=<d>/`, for example
  `s3://opal-data-harvest/amgt/harvest/gold/article_security_mention/date=2026-09-22`.
- Each row carries:
  - `mention_count`, `mention_in_title`, `mention_in_lead` (the first three blocks) and `first_mention_block`;
  - `blocks_hit`, `blocks_total` and `mention_density`;
  - `match_forms`;
  - `vendor_tagged_primary` and `vendor_tagged_secondary`;
  - `co_mentioned_securities`, `co_mention_count` and `is_roundup`;
  - `signal_tier` (A-D) and `signal_weight`;
  - the three clocks and `lag_hours`;
  - lineage.
- The tier rule and the weights are working defaults, re-set by Andrew's word without a contract change:

  | tier | rule | weight |
  |---|---|---|
  | A | title and lead | 1.0 |
  | B | lead, or density >= 0.3 | 0.6 |
  | C | 2+ mentions elsewhere | 0.3 |
  | D | one passing mention | 0.1 |

  The roundup threshold is `co_mention_count >= 5`.

**`C-HV-DAILY-DENSE`.**
- The gold `chatter_daily` table has one row per (security, UTC day), at
  `s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=2026-09-22` (builder output).
- The series is DENSE: an empty day is a zero row.
- Each row carries tier counts, `mention_score`, publisher breadth, trailing 7- and 30-day sums, the prior-30-day
  baseline mean and SD, `breakout_ratio`, `z_score` and `data_status` (`COMPLETE | PARTIAL | DENIED`), so a quiet day is
  never a broken read.

**`C-HV-EVENT-SPINE`.**
- The gold `chatter_event` table (`s3://opal-data-harvest/amgt/harvest/gold/chatter_event/date=2026-09-22`, builder
  output) holds clustered runs of UTC days for one security.
- The working rule: tier A+B articles >= 2, from >= 2 publishers, merged across gaps of <= 1 day.
- Each event carries its lead headline and its articles.

**`C-HV-GOLD-REBUILDABLE`.** Gold is built from silver only. A rebuild from the same silver reproduces identical rows.

**`C-HV-AXIS-PROJECTION`.**
- The Chatter axis's served ranks (the DynamoDB TRENDING and BREAKOUT chatter rows) become a projection of
  `chatter_daily`, never a separate count.
- Changing what they serve is a served act and takes a never-widen pair.

**`C-HV-KEY`.** Every gold row carries `security_key`, and `composite_figi` wherever the crosswalk holds it (the working
key for research, Andrew 2026-09-22).

**`C-HV-EGRESS`.**
- Any live fetch from a publisher is vendor egress and runs only on Andrew's per-use word.
- The validation security is Lenovo (`992_HK_Equity`), under his trial word (one run per publisher).
- Uploading articles already held on the desktop is not egress.
- Stored subscriber bodies stay under `AMGT_RESAPP`'s standing terms question, which is his.

**`C-HV-BOUNDARY`.**
- This project owns the publication channels' retrieval, bronze, silver and gold, the chatter projection, and the
  timeline view.
- `AMGT_RESAPP` owns the rest of the page and the Lenovo trial.
- The trial's one publications pass (its stage 9) is EXECUTED by this project's harvester once `C-HV-BRONZE-AS-RECEIVED`
  and `C-HV-SILVER-FROM-BRONZE` land, so there is ONE pass, not two. The trial reads the result.

**`C-HV-DESIGN-SPEC-FIRST`.** No `.tsx` for the timeline until its design spec is approved. This is `AMGT_RESAPP`'s rule,
applied here.

---

## 2. THE BOUNDARY

**In:**
- the five publishers' retrieval (SA, Bloomberg.com, Barron's, WSJ, FT);
- bronze, silver and gold for them;
- the chatter projection;
- the timeline graph and its dissection on the security page;
- the desktop outbox upload.

**Out:**
- non-English press for HK and JP names (the brief's call 5: UNRESOLVED-BY-DESIGN in this version);
- the social feed;
- SERP;
- every non-publication channel;
- any cadence or schedule, which stays Andrew's;
- any deletion.

## 3. CONSTRAINTS ON THE CUT

- Build order follows dependency:
  1. bronze capture;
  2. silver from bronze;
  3. retrieval provenance and watermark;
  4. gold mention;
  5. daily;
  6. event;
  7. projection and page.
  The desktop upload is independent.
- The mention floor may not be raised by any cell.
- A weight or threshold is a working default, stated in the deliverable, never invented as a constant elsewhere.
- Bloomberg's per-symbol `news()` call (`bloomberg_rest_fetch.py:119-123`) is tried once in the validation run, inside
  the cap. It is adopted or recorded UNRESOLVED with its reason.

## 4. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

| # | surface | engine | depends on | outcome |
|---|---|---|---|---|
| H1 | bronze capture, articles and listings, 5 publishers | `lib/opal_data_harvest/publishers.py` (`raw_bytes` on every path), the rk-85 bronze writer | -- | FWD-1 |
| H2 | silver from bronze (`article`, `listing_hit`) | `harvest_grammar.article_silver_row` rebuilt to read bronze | H1 | FWD-2 |
| H3 | retrieval rungs, provenance, watermark | the harvester's discovery calls | H1 | FWD-3 |
| H4 | gold `article_security_mention` | a new gold producer over silver | H2, H3 | FWD-4 |
| H5 | gold `chatter_daily` | same producer | H4 | FWD-5, FWD-7 |
| H6 | gold `chatter_event` | same producer | H5 | FWD-6 |
| H7 | the chatter projection (DynamoDB ranks from `chatter_daily`) | the chatter-axis Lambda | H5 | FWD-7 |
| H8 | timeline graph and dissection | the portal security page plus `scoped_amgt.py`; design spec first | H5, H6 | FWD-5, FWD-6 |
| H9 | desktop outbox upload into the new grammar | `lib/opal_data_harvest` uploader | H1, H2 | FWD-8 |

## 5. CALLS THAT STAY ANDREW'S (the brief's s.8)

The build proceeds on the working defaults above. His word changes a value, not a contract:
- the tier weights;
- whether a tier-D passing mention counts in the axis (default: yes, at 0.1);
- the roundup threshold;
- the event thresholds;
- non-English press (out of this version);
- publisher terms on stored bodies (already his).

**Ruled by the L4 author** (a design fork the brief researched): silver is built FROM BRONZE, not from the normalised
record, because the vendor fields gold needs (tags, language, paywall) exist only there.

## 6. WHAT THIS PRD DOES NOT CLAIM

- It has not exercised Bloomberg's per-symbol `news()` call.
- The 84-link sample is three US pilots; Lenovo's shape will differ, and the validation run measures it.
- The weights and thresholds are defaults, not findings.
- Nothing here changes `AMGT_RESAPP`'s ratified contracts except `C-HV-SILVER-FROM-BRONZE`, which supersedes that
  project's rk-85 silver shape for the five publishers, and `C-HV-BOUNDARY`, which moves the trial's stage-9 execution
  here.

-- `1.0.0_SA_CTO~Z`
