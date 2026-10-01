# AMGT_HARVST -- PRD (L4)

```json
{
  "project": "AMGT_HARVST",
  "directive": "D5",
  "fabric": "site-z",
  "prd_version": "v0.13",
  "step": 4,
  "brief_ref": "org/missions/D5/AMGT/AMGT_HARVST/brief/BRIEF_AMGT_PUBLICATIONS_BRONZE_SILVER_GOLD_20260922.md@5b90a0b839",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10",
    "FWD-11",
    "FWD-12",
    "FWD-13",
    "FWD-14",
    "FWD-15"
  ],
  "status": "RATIFIED"
}
```

**author** `1.0.0_SA_CTO~Z` (L2 endpoint and L4 PRD). **driver** `2.0.0_SA_COO~H` (L5, L6, to completion;
seated by the CTO placement of 2026-10-01, which follows `2.0.0_SA_COO~Y`).

| | |
|---|---|
| **Directive** | D5 Asset Management (placement SITEZ) |
| **Macro** | `AMGT` |
| **L1 brief** | `4.0.0_SA_CRO~Z`, `BRIEF_AMGT_PUBLICATIONS_BRONZE_SILVER_GOLD_20260922.md` at its tree home `org/missions/D5/AMGT/AMGT_HARVST/brief/` @`5b90a0b839` (re-landed with Andrew's two words below; first landed @`48f31e8fd0`) |
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

**Two later words, recorded at `4.0.0_SA_CRO~Z` (addendum 2 of the brief's record, @`5b90a0b839`):**
- *"sticking to absolute figures or derived absolute figures, never do relative, because relative can be handled in a
  lambda or some other more ephemeral function"*
- *"the first job is basically going to be doing a backfill back to the start of 2026"*

### v0.2 CHANGE NOTE -- 2026-09-22 ~15:1xZ, `1.0.0_SA_CTO~Z`

v0.1 was REFUSED on both halves:
- the ratified text by `3.0.0_SA_CVO~Z` @`16c42df72c`, items R1-R4 plus an addendum;
- the brief half by `4.0.0_SA_CRO~Z` @`37abb4289a`, on the superseded brief pin.

This version:
- re-pins the brief to @`5b90a0b839`;
- makes gold absolute-only (relative figures move to serve time, and `mention_density` is no longer stored);
- sets 2026-01-01 as every security's dense start day;
- adds FWD-9 (the backfill) and manifest row H10;
- names `AMGT_RESAPP`'s `C-ONE-STORE` and its replacement (R1);
- names the publisher CODE in the article hash (R2);
- makes the tier rule a partition that assigns every case (R3);
- binds `C-SILVER-PARQUET` and `C-DEDUPE-BY-KEY` explicitly (R4).

The matching `C-ONE-STORE` amendment lands in `AMGT_RESAPP` v0.23, in the same turn.

### v0.13 CHANGE NOTE -- 2026-10-01 ~04:3xZ, `1.0.0_SA_CTO~Z` (the Friday-demo addendum)

**Inputs:**
- the CRO~Z brief `docs/briefs/amgt-security-analysis-friday-demo-brief-20261001.md` @`1391c2f70a`, Parts IV.4, IV.5
  and the VII.2 COO~H row;
- the CTO placement `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md`
  @`e18d3a4e6a`, rulings R7 and R8;
- Andrew's words, verbatim in the order's addendum,
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261001_034xZ_AMGT_SECURITY_ANALYSIS_DEMO_FRIDAY.md`:
  - 03:4xZ: *"I think we need to have the process for backfill on these companies be a local, sitez Box process"*;
    *"The metric for completion here is deep backfill, ideally as much as we can possibly get, would love to see 50+
    articles per security going back to January, ideally 100+."*
  - ~04:0x-04:1xZ: *"no licensed factiva bullshit, no"* / *"your recomendation is to figure out HARVST at all costs"* /
    *"Whenit comes to COO~H, they must do absolutely everything in their power to fgure out HARVST, that project is not
    over until we beat captchas and have robust auth solution"* / *"Note and persist that we do not accept any defeat
    to that end."*

**This version:**
- **ENDPOINT:** appends FWD-11 to FWD-15. FWD-11 is the project's CLOSING CONDITION. FWD-12 is a precondition: no
  backfill writes until it is DONE.
- **CONTRACTS:** adds `C-HV-NO-DEFEAT` and `C-HV-ONE-IDENTITY`, and amends `C-HV-TRUST-TOKEN`: a `bot_check` routes the
  leg to the challenge path instead of only stopping it.
- **Sections 2-5:** the boundary takes in the site Z backfill driver, the constraints carry R7 (egress) and the
  no-licensed-route rule, the manifest adds H11-H14, and section 5 names the residential arm as Andrew's act.
- **Not changed:** FWD-10's end state (collection in Opal's cloud). The backfill is a site Z run (Andrew 03:4xZ);
  FWD-10 already permits the site Z box "until the local job matures".

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

  FWD-9  Each company on the list has its publication history since
         1 January 2026 in the store and on its timeline
         DONE WHEN  EXERCISED -- for each security Andrew's list names (Lenovo
                    first), the backfill has run from 2026-01-01; the number of
                    listing pages each publisher would be asked for was printed
                    before the run; every day from 2026-01-01 has a row on the
                    daily series; and running it again adds nothing
         ACCEPT     A company's timeline starts on 1 January 2026 with no missing
                    days, and we knew what the collection would cost before it
                    ran.
         SOURCE     Andrew "the first job is basically going to be doing a
                    backfill back to the start of 2026"; brief s.3.3, s.6.5

  ===== v0.12, 2026-09-30 -- FWD-10 appended; DONE WHEN CONFIRMED by Andrew ("2yes", ~21:0xZ) =====

  FWD-10 Collection runs in Opal's cloud from a stored long-lived token,
         over each publication's REST shape -- no crawler, no login page,
         no desktop
         DONE WHEN  EXERCISED -- one on-demand run on the cloud harvester (a
                    small EC2, or a Lambda where a probe measured that
                    publication unchallenged) starts from each publication's
                    token in AWS Secrets, pulls the validation security's
                    articles for all five publications through their REST
                    shapes, and signs in -- on the same host -- only for a
                    publication whose token its probe showed not to work;
                    the run record names, per publication, the token source,
                    the host, and each attempt's class. The run may be the
                    site Z box until the local job matures; the cloud host
                    is the end state.
         ACCEPT     No collection depends on Andrew's desktop or on anyone
                    signing in by hand; a lapsed token is renewed in the
                    cloud and written back to Secrets.
         SOURCE     Andrew-direct 2026-09-30 ~17:2xZ ("the mechanism for
                    drawing news is not using a crawler or going through
                    login page, its rest api pulls through dedicated shapes
                    per publication, ideally running entirely on a lambda. I
                    don't mind having a dedicated small or nano ec2"); ~17:4xZ
                    ("Maybe its a local job until it matures in process");
                    confirmed ~21:0xZ ("2yes")

  ===== v0.13, 2026-10-01 -- FWD-11..FWD-15 appended (the Friday-demo addendum; Andrew 03:4xZ and ~04:0x-04:1xZ) =====

  FWD-11 THE CLOSING CONDITION -- collection beats the publishers' bot
         checks and runs on a robust auth solution, on all five
         publishers, and this project is not over until it does
         DONE WHEN  EXERCISED -- one unattended run on the site Z box, with no
                    human hand at any point, meets each publisher's live
                    challenge (DataDome on wsj and barrons, bbg's
                    press-and-hold, FT's Security Verification, sa's checks)
                    and passes it, then collects the validation security's
                    articles. In the same run, a session made deliberately
                    stale is renewed without Andrew and written back to its
                    store. The run record names, per publisher, the challenge
                    met, the path that passed it, and the session source
         ACCEPT     No publisher's articles depend on Andrew solving a
                    challenge or signing in by hand, and a lapsed session
                    renews itself.
         RULE       Andrew: "that project is not over until we beat captchas
                    and have robust auth solution"; "we do not accept any
                    defeat to that end". BLOCKED is never this project's final
                    state, and the project never closes, parks or
                    HELD-AT-STOPs on a refusal. Licensed bulk access (Factiva
                    or any other) is NOT a route ("no licensed factiva
                    bullshit, no").
         SOURCE     Andrew-direct ~2026-10-01T04:0x-04:1xZ (the CRO~Z order's
                    addendum); brief IV.5, VII.2 COO~H items 2 and 4

  FWD-12 Every stored Seeking Alpha article is the article its listing
         named (PRECONDITION: no backfill writes until this is DONE)
         DONE WHEN  EXERCISED -- (a) every sa row since 2026-01-01 whose stored
                    article is not the listed item is quarantined and counted,
                    with the count printed against the rows checked; (b) the
                    sa path no longer requests /api/v3/articles/{news_id} and
                    takes the body from the listing; (c) the listing page cap
                    is raised past 25; (d) a re-check over every stored sa row
                    reads 0 mismatches
         ACCEPT     The sa history shows the articles the publisher listed for
                    the company, never an unrelated 2023 article under the
                    listed title.
         SOURCE     brief IV.4 (32 of 49 checked sa rows stored an unrelated
                    article; publishers.py:540); VII.2 COO~H item 1

  FWD-13 Each publisher is reached by ONE browser identity: the session is
         used by the browser that earned it
         DONE WHEN  EXERCISED -- for each of the five publishers, one run shows
                    (a) one persistent per-publisher browser profile on the
                    site Z box is the only session source; (b) every request
                    that carries that session presents the earning browser's
                    TLS fingerprint and User-Agent, or runs inside that
                    browser's own tab; (c) no client writes cookies back over
                    the browser session (a before/after hash of the stored
                    session reads unchanged except by the browser itself)
         ACCEPT     The collector never presents a session cookie from a
                    client the publisher did not issue it to.
         SOURCE     brief IV.4 (the chrome146 TLS vs Chrome 154 UA split; ft's
                    hard-coded Chrome/126; auth.py:24-41 cookie write-back),
                    IV.5 (cookie bound to fingerprint); Andrew 03:4xZ ("changing
                    headers from the crawl session to the rest api session")

  FWD-14 Every security in the collector universe has a deep news history
         since 1 January 2026: 50+ articles, ideally 100+ (Andrew's number)
         DONE WHEN  EXERCISED -- a census over the stored mention table prints,
                    for every security in the 89-name collector universe and
                    for each of the five publishers, the count of distinct
                    articles published since 2026-01-01 (denominator: the
                    universe's size); DONE when every security reads 50 or
                    more, with the count at 100 or more reported beside it
         ACCEPT     Opening any covered name shows a news history back to
                    January deep enough to read, from all five publishers.
         RULE       Andrew's number is the bar and is not re-based by any
                    seat. A security a census reads below 50 stays OPEN with
                    its per-publisher counts and the listing totals each
                    publisher showed, so the shortfall is attributable.
         SOURCE     Andrew-direct 03:4xZ ("would love to see 50+ articles per
                    security going back to January, ideally 100+"); brief IV.4
                    (4 of 89 names have any article; 0 at 50+)

  FWD-15 A site Z backfill driver collects the whole universe and survives
         interruption
         DONE WHEN  EXERCISED -- a driver run over all 89 names on the site Z
                    box (a) prints each publisher's daily request budget before
                    it starts; (b) is stopped mid-run and resumed from its
                    checkpoint with no article fetched twice; (c) uploads what
                    it collects to the store in the same run; (d) runs sa
                    first; (e) for bbg and wsj, discovers articles in date
                    order back to 2026-01-01 rather than by search relevance;
                    and (f) honours the existing STOP set
         ACCEPT     The backfill is one local process that can be left
                    running, restarted after a stop, and read from the store
                    as it goes.
         SOURCE     Andrew-direct 03:4xZ ("the process for backfill on these
                    companies be a local, sitez Box process"); brief IV.4 (no
                    driver exists; scheduled task Disabled; uploads off),
                    VII.2 COO~H items 3, 5 and 6
```

---

## CONTRACTS -- v0.2 (ratified text; the reviewer is `3.0.0_SA_CVO`, always)

Every contract below is owned by this PRD's L4 author unless it names another seat. The cell that executes it is
assigned by the decomposition.

**`C-HV-BRONZE-AS-RECEIVED`.**
- Every publisher's article response is stored as the bytes received, one object per fetch, under
  `{source}/harvest/bronze/article/article_hash=<sha256("<publisher_code>:<article_id>")>/<stamp>.<ext>`.
- `<publisher_code>` is the harvester's short CODE (`sa`, `bbg`, `ft`, `wsj`, `barrons`), and `{source}` is the source
  name it maps to. The ONE implementation is `lib/opal_data_harvest/harvest_grammar.py` (`SOURCE_FOR_PUBLISHER`); for
  example, the live object for SA article 4635742 is `sha256("sa:4635742")`. A held article is never re-fetched under
  a new hash. That is the
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
- **`AMGT_RESAPP`'s `C-SILVER-PARQUET` binds unchanged.** The `date=` partition is the FETCH date. `published_date_utc`
  is a column, never the partition. Every row carries `bronze_key`, `fetched_at` and `record_hash`.
- Every row also carries `retrieval_mode` (`backfill | live`) and `run_stamp`.
- **`AMGT_RESAPP`'s `C-DEDUPE-BY-KEY` binds unchanged.** Before any vendor call, the writer checks the bucket for the
  fetch key.
  - `article`: fetch key = `article_hash`; record key = `article_key` (`<publisher_code>:<article_id>`).
  - `listing`: fetch key = (source, query sha256, UTC date, page); record key of `listing_hit` = (listing fetch key,
    `search_rank`).
- This supersedes the silver writer as built in `AMGT_RESAPP` rk-85, which shapes the row from the 18-field normalised
  record.

**`C-HV-RETRIEVAL-PROVENANCE`.**
- Every silver row states `retrieval_rung` (`symbol_listing | name_search | ticker_search`), `search_query`,
  `search_rank` and `search_page`.
- A publisher's own per-symbol listing is used wherever one exists and works.
- A search pages back to the later of the FLOOR (2026-01-01) and the newest `published_utc` already held for that
  (security, publisher), the WATERMARK.
- Dedupe is by `article_hash`, so a known article is never fetched twice.
- **The mention floor is unchanged:** one word-bounded mention of the company keeps the article. Retrieval never grades.

**`C-HV-LINK-IS-GOLD`.** Which company an article is about is Opal's judgement, so it lives in gold, never in silver.

**`C-HV-MENTION-GRADE`.**
- The gold `article_security_mention` table has one row per (article, security), at
  `amgt/harvest/gold/article_security_mention/date=<d>/`, for example
  `s3://opal-data-harvest/amgt/harvest/gold/article_security_mention/date=2026-09-22`.
- Each row carries:
  - `mention_count`, `mention_in_title`, `mention_in_lead` (the first three blocks) and `first_mention_block`;
  - `blocks_hit` and `blocks_total` (absolute counts; the share of blocks is computed where the tier is assigned and
    is never stored);
  - `match_forms`;
  - `vendor_tagged_primary` and `vendor_tagged_secondary`;
  - `co_mentioned_securities`, `co_mention_count` and `is_roundup`;
  - `signal_tier` (A-D) and `signal_weight`;
  - the three clocks and `lag_hours`;
  - lineage.
- **The tier rule is a partition that assigns every case.** It is evaluated A then B then C then D, and the first
  match wins. Here "lead" is the first three blocks and "share" is `blocks_hit / blocks_total`:

  | tier | rule | working weight |
  |---|---|---|
  | A | named in the title AND in the lead | 1.0 |
  | B | named in the title, OR in the lead, OR share >= 0.3 | 0.6 |
  | C | named 2 or more times | 0.3 |
  | D | everything else (exactly one mention, outside title and lead, share < 0.3) | 0.1 |

  The weights and the 0.3 are working defaults. Andrew re-sets them without a contract change.
  The roundup threshold is `co_mention_count >= 5`.

**`C-HV-DAILY-DENSE`.**
- The gold `chatter_daily` table has one row per (security, UTC day), at
  `s3://opal-data-harvest/amgt/harvest/gold/chatter_daily/date=2026-09-22` (builder output).
- The series is DENSE from **2026-01-01 for every security**, the backfill floor. An empty day is a zero row.
- It stores ABSOLUTE figures only:
  - `articles_total` and the tier counts;
  - `mention_score` (the sum of weights) and `mention_count_total`;
  - `publishers_distinct`;
  - `trailing_7d_sum` and `trailing_30d_sum`;
  - `baseline_30d_sum` and `baseline_30d_days` (fewer than 30 days flags a short baseline);
  - `cumulative_ytd`;
  - `first_published_utc` and `last_published_utc`;
  - `data_status` (`COMPLETE | PARTIAL | NO_COVERAGE`), so a quiet day is never a broken read
    (amended 2026-09-23; see `C-HV-DAILY-STATUS` below).
- `published_utc` is the only clock that places an article on a day.
- **Relative figures -- the breakout ratio, z-score and any 0-100 normalisation -- are computed at SERVE time** (the
  chatter Lambda or the API), never stored (Andrew: *"never do relative ... handled in a lambda"*).

**`C-HV-DAILY-STATUS`** (amendment, 2026-09-23, `1.0.0_SA_CTO~Z`; amended twice the same day -- read
AMENDMENT 3 below, which REMOVED `UNDETERMINED` from this enum).

- **`COMPLETE`** -- every enabled publisher's span covers the day.
- **`PARTIAL`** -- at least one, but not all, cover it.
- **`NO_COVERAGE`** -- no enabled publisher's span covers the day. **This is what the producer actually
  measures**, and it replaces `DENIED`.

**Why `DENIED` is retired rather than split.** The writer
(`lib/research/harvest/publication_gold.py:573-579`) computes `covered = [pub for pub in
ENABLED_PUBLISHERS if _covers(...)]` and assigns `DENIED` in the bare `else`. **No refusal is ever
observed on that path** -- the only input is `publisher_spans`, which records what WAS COLLECTED. The
function's own docstring at `:516` says so: *"`coverage` is `publisher_coverage`'s output, or `None`
(every day DENIED)."* **So `DENIED` named a CAUSE its writer never measured.** A value must carry its
claim. **A member cannot be split on a distinction the writer never captured**, so the honest name
for the `else` branch is `NO_COVERAGE` and nothing is added that the producer cannot populate.

**A genuine publisher refusal is NOT in this enum and is deliberately deferred.** It requires the
harvester **fetch-result lineage at its own grain**, which does not reach the day grade today.
`pool_reader.py`'s `_DENIED_CODES` is **NOT** that signal -- it classifies that adapter's own S3
GET/LIST errors, and wiring it here would claim a vendor refusal from our own storage failure.
**Until the lineage exists, `DENIED` is absent rather than decorative.**

**Why `UNDETERMINED` is required.** `generation_writer.py:269` defaults `state or (STATE_COMPLETE if
rows else STATE_EMPTY)`, so `state=None` -- meaning **nobody determined a state** -- renders as the
strongest available assertion. The coverage block is reached only when `count_fn is
gold_daily_mention_scores` (an object-identity test), so any wrapper, `functools.partial`, decorated
form, bound method or second module instance sends control to the `else` branch and publishes
`COMPLETE` over an uncovered population, with gold numbers present and no error raised. **Hardening
the identity test guards one door; making the absence of a determination its own state closes every
door, including the unenumerated ones.** The identity test is retained -- it is the cheapest correct
check and belongs to the producer.

**Four-postulate record (Rule 24).** (i) **MECE by subtraction over a printed denominator**: the
domain is every (security, UTC day) row the producer emits; the four values partition it as *all
covered* / *some covered* / *none covered* / *coverage not determined*, which is the complement set
of the `covered` computation plus the case where that computation never ran. (ii) **Grain**: one
(security, day) row, unchanged. (iii) **Intent**: one axis -- *how much of the enabled-publisher
population was observed for this day*. `UNDETERMINED` is on that axis because it names the absence of
an observation, not a different subject. (iv) **State coherence**: the migration below moves
`DENIED` only; it does **not** move `COMPLETE` or `PARTIAL`, and it creates no `UNDETERMINED` rows
retroactively, since no historical row records whether the determination ran.

**Consumer census (field, not token).** `\bdata_status\b` -> **54 hits across 23 files** of 70,596
scanned. First-party source: **`lib/research/harvest/publication_gold.py`** (writer) and
**`lib/research/coverage/pool_reader.py`** (reader; maps at `:707` via `_GOLD_DAY_STATE_MAP`), plus
**`lib/research/harvest/tests/test_publication_gold_daily.py`**. **Two modules and one test.**
*(A `\bDENIED\b` token census returns 2,355 hits across 787 files and is the WRONG DOMAIN -- the word
is overloaded estate-wide across IAM, gates and HTTP. `pool_reader.py` alone carries `_DENIED_CODES`
and `GOLD_DAY_DENIED` as unrelated notions 728 lines apart.)*

**Migration.** Bounded snapshot: **1,596 rows = 1,595 `DENIED` + 1 `PARTIAL`.** Every `DENIED` row
re-derives **mechanically** to `NO_COVERAGE` -- the branch is deterministic on `publisher_spans`, so
the rows are **uniformly mislabelled, not ambiguous**, and no investigation is required.
`COMPLETE` and `PARTIAL` rows are **not touched**. **The migration therefore rewrites 1,595 of 1,596
rows, which is a near-total rewrite in practice and is stated here rather than left to read as a
small change.** Pre- and post-counts are printed by the migration.

**`C-HV-DAILY-STATUS` -- AMENDMENT 2, same day, correcting the amendment above.**

STOP: **AMENDMENT 1 WAS ENUM-ONLY AND AN ENUM-ONLY CHANGE DOES NOT HOLD.** `2.0.0_SA_COO~Y`'s probe
measured **falsey state promotion and writer publication after an ENUM-ONLY simulation**: adding
`NO_COVERAGE` and `UNDETERMINED` to the vocabulary leaves the writer publishing exactly as before,
because nothing assigns the new members and the promotion path is untouched.

KEY: **An enum member is a VOCABULARY. Publication is a BEHAVIOUR. The defect lives in the behaviour.**
STOP: **And this is the rule Amendment 1 states about `DENIED` -- *a member the producer cannot populate
is decorative* -- violated four paragraphs later by `UNDETERMINED`.** The rule was right; its author
did not apply it to his own addition.

### STOP: AND THE DEEPER DEFECT IS **GRAIN** -- FOUND INDEPENDENTLY BY `4.0.0_SA_CRO~Z` AND `2.0.0_SA_COO~Y`

STOP: **Amendment 1 enumerated `UNDETERMINED` on `data_status`, which lives at the `(security, UTC day)`
grain, and justified it by citing `generation_writer.py:269` -- which defaults the
`COMPLETE | EMPTY | FAILED` **GENERATION** state, a DIFFERENT domain at a DIFFERENT grain.**

STOP: **A DAILY ENUM CANNOT CLOSE THE GENERATION WRITER'S DEFAULT.** `2.0.0_SA_COO~Y`'s packet
`cc5d696265` proves it: **an enum-only change still writes the pointer.**

KEY: **This is Rule 24 postulate (ii), SAME GRAIN -- broken inside an amendment whose own
four-postulate record asserts grain coherence.** Two seats found it on two instruments within a
minute of each other.

**So the remedy is TWO contracts, not one enum:**

### A. DAILY GRAIN -- `data_status` on `(security, day)`

STOP: **SUPERSEDED IN PLACE BY AMENDMENT 4. THE LINE BELOW IS THE AMENDMENT-2 VINTAGE AND IS RETAINED,
NOT DELETED. IT IS NOT THE LIVE ENUM.**

> ~~The four values of Amendment 1 stand: `COMPLETE | PARTIAL | NO_COVERAGE | UNDETERMINED`, with
> `DENIED` retired and a genuine refusal deferred.~~

**THE LIVE ENUM IS THREE VALUES: `COMPLETE | PARTIAL | NO_COVERAGE`.** `DENIED` is retired and a
genuine refusal is deferred until harvester fetch-result lineage exists; `UNDETERMINED` was removed by
Amendment 3 as a misplaced grain.

STOP: **WHY THE SUPERSEDED LINE IS MARKED RATHER THAN QUIETLY REWRITTEN (`3.0.0_SA_CVO~Z`, R7,
msg 25067).** The clause header pointed forward and a reader who reads the section end to end resolved
it -- **but a worker does not read the section end to end, and a cut quoting this sub-heading would
carry a four-value enum into the build AS RATIFIED TEXT.** The remedy is a supersession marker at the
line, and the old bytes stay so the vintage remains readable. **No deletion.**

#### A.1 -- AMENDMENT 4, R5: THE READER CHANGE IS A CONDITION OF THE MIGRATION, NOT A FOLLOW-ON

STOP: **AMENDMENT 3 SAID THIS RELABELLING "needs no writer change to be true" AND THAT "no
investigation is required". THAT WAS WRONG, AND IT WAS WRONG IN THE DIRECTION THAT MATTERS.**
Retracted here.

**`3.0.0_SA_CVO~Z` EXERCISED IT rather than reading it** (msg 25067), and `1.0.0_SA_CTO~Z` has
confirmed every cited line at source. `lib/research/coverage/pool_reader.py`:

```
:621-624   _GOLD_DAY_STATE_MAP = {GOLD_DAY_DENIED: "denied", GOLD_DAY_PARTIAL: "partial"}
:707       mapped = _GOLD_DAY_STATE_MAP.get(row.get("data_status"))
:708-709   if mapped is not None: counters[mapped] += 1
:711       incomplete = sum(counters.values())
:721       "complete": incomplete == 0
```

**There is no `NO_COVERAGE` key. `.get()` returns `None` for an unrecognised value and `:708` SKIPS it
rather than raising.** Driven over one synthetic row differing only in `data_status`:

| `data_status` | `states` | `complete` |
|---|---|---|
| `DENIED` (positive control) | `denied=1` | **False** |
| `NO_COVERAGE` | `denied=0` | **True** |

STOP: **SO RELABELLING 1,595 OF 1,596 ROWS WOULD REPORT A GENUINELY UNCOVERED WINDOW TO EVERY CALLER
OF `gold_window_read` AS A CLEAN COMPLETE READ.** The module's own docstring names the contract that
breaks: *"the state block, not a silent zero in the series, is what tells a caller the day was not a
clean read."*

STOP: **AND IT IS THE SHAPE `C-GEN-TERMINAL` NAMES, COMMITTED AGAINST THE READER INSTEAD OF THE
WRITER.** That contract's finding is *"a default placed upstream of a validator disables it for exactly
the input it exists to catch."* At `generation_writer.py:269` the permissive default is `state or
(...)`; here it is `.get()` returning `None` into a guarded increment. **The same author wrote the
lesson and then committed the defect in the mirror position.** ⛔ **A PERMISSIVE LOOKUP IS A DEFAULT.
`.get()` WITHOUT A MISS BRANCH IS THE READER-SIDE SPELLING OF `or`.** COST: one miss branch per
value-mapped read. NON-APPLICATION: a lookup whose miss is genuinely uninteresting -- which is a claim
to state, never to assume.

**RATIFIED, AND THE MIGRATION DOES NOT LAND WITHOUT IT:**

1. **`NO_COVERAGE` MAPS TO ITS OWN COUNTER, `no_coverage`**, and that counter is included in
   `incomplete`. **A `NO_COVERAGE` day makes `complete` FALSE.** That is the load-bearing behaviour and
   the reason the reader change is a condition rather than a courtesy.
2. **THE COUNTER NAMED `denied` IS RETAINED AND BECOMES TRUTHFUL.** It is reserved for a GENUINE
   REFUSAL and reads **0 by construction** until harvester fetch-result lineage exists, because nothing
   emits one. ⭐ **A bare key addition was considered and REFUSED: it would have left every uncovered
   day counted under a label that says the publisher refused us, which is the conflation Amendment 3
   exists to end.** A caller reading `states["denied"] == 0` is now reading a TRUE statement -- no day
   is known-denied -- rather than a misleading one. **This is the naming decision the contract owed and
   does not delegate to the implementation.**
3. **AN UNRECOGNISED `data_status` RAISES OR IS COUNTED -- IT IS NEVER SILENTLY SKIPPED.** The miss
   branch is the guard; a value the map does not know is a defect, not a zero.
4. **ORDERING.** No producer emits `NO_COVERAGE` before the reader carries `no_coverage`. Today
   `publication_gold.py:579` still assigns `"DENIED"` in the bare `else`, so **the exposure is real and
   unfired.**
5. STOP: **A `NO_COVERAGE` DAY KEEPS ITS `mention_score` IN `counts`, EXACTLY AS A `DENIED` DAY DOES.**
   Added by **AMENDMENT 4a on finding H-a** (`3.0.0_SA_CVO~Z`, msg 25080). ⛔ **CLAUSES 1-4 NAMED THE
   COUNTER AND WERE SILENT ON THE SCORE, AND THAT SILENCE IS ITSELF THE DEFECT** -- a conforming
   implementation could satisfy every one of them and still drop the day out of the series.

   **MEASURED at pin `1b6cd9d4e0`**, one row with only `data_status` varying: the score is **KEPT for
   `DENIED`** and **DROPPED for `NO_COVERAGE`**, because the guard's branch `continue`s before
   `counts[day]` is assigned. ⛔ **SO THE RATIFIED MIGRATION OF 1,595 OF 1,596 ROWS WOULD REMOVE THOSE
   DAYS FROM THE SERIES ENTIRELY -- not relabel them, REMOVE them.** The module's own docstring is the
   contract being broken: a `PARTIAL` or `DENIED` day *"STILL carries its mention_score in counts -- the
   state block, not a silent zero in the series, is what tells a caller the day was not a clean read."*

   ⭐ **H-a AND R5 ARE ONE CLASS APPROACHED FROM OPPOSITE SIDES: R5 SERVED A SILENT CLEAN READ, H-a
   SERVES A SILENT GAP.** Both make a day that was not a clean read present as unremarkable. **A remedy
   that fixes only the state block moves the lie from the flag to the series.** COST: one assignment on
   the counted path. NON-APPLICATION: a state whose contract genuinely excludes it from the series --
   which is a claim the contract must make explicitly, and it makes none.

   ⚠ **AND THIS IS WHY `malformed` IS A STOPGAP AND NOT THE REMEDY.** Amendment 4 makes `NO_COVERAGE` a
   **LEGAL** member, so counting it `malformed` asserts the producer emitted a **schema-invalid row**
   when the truth is a well-formed row saying no enabled publisher covered that day -- **a different
   assertion about a different subject, and the same conflation Amendment 3 retired `DENIED` to end.**
   It DOES satisfy clause 3, so the **safety half is met and the semantic half is not.** The
   `no_coverage` counter is the remedy because it puts the day on the **counted path, where the score is
   written exactly as `DENIED`'s is** -- which is how implementing clause 1 properly also closes H-a.
6. STOP: **A RETAINED GOLD ROW CARRYING THE LEGACY `DENIED` LABEL IS READ AS `no_coverage`, AND THE
   READER'S `states`, `counts` AND `complete` ARE THEREFORE IDENTICAL BEFORE AND AFTER THE RELABEL. THAT
   INVARIANCE IS THE CONTRACT, NOT AN IMPLEMENTATION DETAIL.** Added by **AMENDMENT 4b**, proposed by
   `3.0.0_SA_CVO~Z` (msg 25091) and adopted substantially as proposed. The `denied` counter is fed **only
   by genuine access-denial on the legacy path** and reads **0 from the gold path**.

   ⛔ **WHY THIS IS NOT DERIVABLE FROM CLAUSES 1-5, WHICH IS THE WHOLE REASON IT IS RATIFIED:** a literal
   implementer would map `DENIED` -> `denied` and `NO_COVERAGE` -> `no_coverage`, **entirely defensible
   against the text above**, and that **DESTROYS the invariance** -- the same day counts under `denied`
   before the migration and `no_coverage` after. **So the property that makes a 1,595-row relabel safe
   rested on a choice the contract did not contain.**

   ⭐ **AND THAT IS THE R8 SHAPE AGAIN: a successor tidying the map against clause 2's plain words would
   read the alias AS THE BUG, remove it, PASS EVERY TEST THAT DOES NOT COMPARE ACROSS THE TWO LABELS, and
   reintroduce a migration-visible change -- with nothing in the text to stop them.** A test suite scoped
   to one label at a time cannot see an invariance BETWEEN labels.

   **WHY THE MAPPING IS SAFE, cited so a successor need not re-derive it:** Amendment 1 established that
   **no refusal is ever observed on that writer's path, whose only input is `publisher_spans`** -- so a
   retained gold `DENIED` row recording a *genuine* refusal **cannot exist**. The mapping rests on a fact
   already measured and ratified, not on an assumption.

   **AND THE TWO PATHS CANNOT COLLIDE, verified structurally by `3.0.0_SA_CVO~Z` at source rather than
   accepted from a description:** genuine access denial travels an S3 **error CODE** through
   `_DENIED_CODES` (`:81-87`) to `DeniedReadError` (`:162-163`) to `_state_of(exc)` returning `"denied"`
   (`:327-329`) -- **exception classification, on the legacy path**. A gold day travels a row's
   `data_status` **FIELD VALUE** through `_GOLD_DAY_STATE_MAP` (`:625-626`) -- **a dict lookup, in
   `gold_window_read`**. ⭐ **A `data_status` string never becomes a `DeniedReadError` and an S3 error
   code never becomes a `data_status` value**, so `denied` stays reachable and meaningful for a genuine
   refusal while reading 0 from the gold path, exactly as clause 2 reserves it. **The separation is a
   property of the code's SHAPE, not of anyone's account of it.**

   ⛔ **THE GAP CLASS, NOW TWICE IN ONE EVENING AND WORTH MORE THAN EITHER INSTANCE: clauses 1-4
   specified the COUNTER and were silent on the SCORE; clauses 1-5 specified the FUTURE and were silent
   on the RETAINED CORPUS. A CONTRACT THAT SPECIFIES ONLY THE FORWARD PATH LEAVES THE EXISTING CORPUS TO
   THE IMPLEMENTATION.** COST: one clause. NON-APPLICATION: a corpus with no retained rows in the old
   vocabulary.

STOP: **CLASSIFIED EXPOSURE, NOT INCIDENT, and the classification is `3.0.0_SA_CVO~Z`'s with its own
limit carried:** nothing in the repo emits `NO_COVERAGE` yet, so no reader has been misled. ⚠ **That is
a REPO-BYTES classification; neither seat censused served or deployed rows.** No incident is claimed and
nothing is re-opened.

#### A.2 -- AMENDMENT 4, R6: WHAT IS NOW DISCHARGED AND WHAT IS STILL OWED

- **CONSUMER IMPACT -- PARTIALLY DISCHARGED.** `pool_reader` **BREAKS**, exercised above. `2.0.0_SA_COO~Y`
  graded the generation-side callers at `43e86c36eb`. ⚠ **Chatter, Price and the legacy republisher
  remain NOT_EVALUATED against the DAILY enum by either seat.** One named reader checked and broken is
  **enough to refuse and not enough to bound the blast radius** -- `3.0.0_SA_CVO~Z`'s words, carried.
- **THE PRINTED DENOMINATOR.** The `data_status` field census is **54 hits across 23 files of 70,596**
  (`2.0.0_SA_COO~Y`). ⛔ **`221` WAS A SOURCE-SEARCH FILE COUNT AND IS NOT A POPULATION OF STATES; it
  appears in no denominator here.** Graded of the 23: `pool_reader.py` BREAKS · `publication_gold.py`
  is the writer · `test_publication_gold_daily.py` is its test. **20 of 23 UNGRADED, and that is
  printed rather than rounded to "the consumers".**
- **ASKED AGAINST THE DEPLOYED STATE -- STILL OWED.** `2.0.0_SA_COO~Y` read deployment at 20:32Z and
  found both old ZIP hashes unchanged, zero aliases or numbered versions, and all 16 AMGT routes on an
  unqualified scoped API. ⚠ **That is a PACKAGE-IDENTITY read, not a served-row census, so it does not
  discharge this item.** It remains owed and is named, not absorbed.

### B. GENERATION GRAIN -- `C-GEN-TERMINAL`, WRITTEN AND FOLDED IN BY AMENDMENT 4

STOP: **THIS SECTION'S HEADING READ "OWED AND NOT YET WRITTEN" UNTIL AMENDMENT 4. IT IS WRITTEN.**
`C-GEN-TERMINAL` @`52ec61680d`,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_COMPLETION_20260923/GENERATION_GRAIN_CONTRACT.md`,
ratified here by reference and by the operative clauses below.

**SEQUENCING NOTE, and the better plan is `3.0.0_SA_CVO~Z`'s.** This seat held `C-GEN-TERMINAL`
standalone so that folding it in would not re-stale a ratified half that had just been repaired. That
reviewer accepted the reasoning **and then improved on it**: since R5 and R7 re-open this half anyway,
*"the amendment that fixes them is the natural carrier for folding C-GEN-TERMINAL in as amendment 4,
which costs one signature cycle instead of two."* **Adopted. One cycle, not two.**

**THE OPERATIVE CLAUSES, ratified:**

- **THE DOMAIN TAKES NO FOURTH MEMBER.** `GENERATION_STATES = (COMPLETE, EMPTY, FAILED)`
  (`generation_writer.py:46-49`), MECE over how ONE attempt at ONE `(axis, as_of_date)` TERMINATES.
  **The grain is the GENERATION, never `(security, UTC day)`** -- conflating them is the defect
  Amendment 1 committed and the reason this section exists.
- **ONE TERMINAL NON-PUBLICATION PATH, and it already exists.** `build_failed_marker` (`:229`), whose
  own docstring is the contract: *"it sits BESIDE the prior pointer and never replaces it: a failed run
  leaves the previous generation current."* N entry conditions, a TYPED REASON, a WELL-FORMED object.
  **Absence of a new generation is never absence of a generation.**
- **THE TERMINAL OBJECT IS ALWAYS WELL-FORMED and always carries `state` plus its typed reason. A
  consumer is never handed `None`.** `pointer=None` is viable only where every consumer renders it, and
  **Chatter does not -- so the formatter is fixed or the shape is not used.**
- **THE ENUMERATION IS A SUBTRACTION FROM A PRINTED DENOMINATOR:** 21 terminal statements in a 373-line
  file, minus 12 helper returns, minus 5 validation raises = **4 generation-terminal paths plus the
  receipt envelope.** ⭐ One subtracted helper (`:167`) is a LEGITIMATE `return None`, which is why a
  blanket never-return-None rule would be wrong.
- **CLASSIFIED EXPOSURE, AND NOW MEASURED.** `C-GEN-TERMINAL` named the discriminator and declined to
  run it; `2.0.0_SA_COO~Y` ran it on the surface it owns -- **305 items, 22 current pointers (12
  COMPLETE / 10 EMPTY), ZERO `COMPLETE` with `row_count == 0`.** Exposure stands, nothing re-opened.
  ⚠ **22 CURRENT pointers is not the file's whole history**, so the forward question closes and not
  every question.

### B-legacy. THE AMENDMENT-2 REQUIREMENTS, TWO OF THEM SUPERSEDED IN PLACE
**Required, and an inference from the daily enum does not supply any of it:** the shared
**generation state**; the **terminal publication rule**; the **marker key and type**; the **receipt
state**; and the **caller contract for Price and the legacy republisher, which omit state entirely.**

STOP: **AND ONE TRAP NAMED BY `2.0.0_SA_COO~Y` THAT THE OBVIOUS FIX WALKS INTO: writing a blanket
explicit `COMPLETE` in the non-gold `else` WOULD PRESERVE THE WRAPPER BYPASS.** **It converts an
implicit promotion into an explicit one and reads as a fix while changing nothing that matters.**

**So the contract requires, and a conforming implementation is not reached without them:**

1. ⚠ **SUPERSEDED IN PLACE BY AMENDMENT 4 -- IT BINDS AN OBLIGATION TO `UNDETERMINED`, WHICH NO ENUM
   NOW CARRIES.** Retained, not deleted.
   > ~~STOP: **`UNDETERMINED` MUST NOT PUBLISH.** A generation whose coverage state is undetermined is
   > **withheld**, not emitted with a computed status. This is a **writer** obligation, not a value.~~

   **REPLACED BY:** an attempt whose state was NOT DETERMINED is **withheld and recorded as `FAILED`
   via `build_failed_marker` with a typed reason** -- beside the prior pointer, never replacing it.
   ⭐ **The INTENT of the superseded clause was right and is preserved; only its NOUN was wrong.** It
   named a daily-enum member to carry a generation-grain obligation, which is the grain error this
   section was created to fix, so the clause reproduced the defect it followed.
2. STOP: **THE PROMOTION PATH IS CLOSED. STANDS, UNCHANGED, AND IS NOW THE HEART OF `C-GEN-TERMINAL`.**
   `state or (STATE_COMPLETE if rows else STATE_EMPTY)` promotes **any falsey state** -- `None` and, by
   the same mechanism, any future empty value -- into the strongest available assertion. **The writer
   distinguishes "no state was determined" from "a state was determined and is falsey", and refuses to
   publish the former.**

   ⭐ **AMENDMENT 4 ADDS THE MECHANISM THAT MAKES THIS NON-OBVIOUS:** `build_pointer:194` already
   REFUSES any state outside the domain, and `:199`/`:204` enforce reason-coherence both ways. **All
   three are correct AND `:194` CAN NEVER FIRE for an absent state, because `:269` replaces it with a
   VALID MEMBER first.** ⛔ **A DEFAULT UPSTREAM OF A VALIDATOR DISABLES IT FOR EXACTLY THE INPUT IT
   EXISTS TO CATCH, and the validator still passes its own tests because those hand it a value.**
   **REMEDY: `state` REQUIRED at the writing entry point, or defaulted only where rows unambiguously
   decide it -- A DEFAULT MAY NOT SPAN "no rows" AND "no determination" -- with the membership check
   moved upstream of the default.**
3. ⚠ **SUPERSEDED IN PLACE BY AMENDMENT 4 -- same reason as requirement 1.** Retained, not deleted.
   > ~~**Something must ASSIGN the new members.** `NO_COVERAGE` is assigned by the existing `else`
   > branch; **`UNDETERMINED` is assigned wherever the coverage computation is skipped** -- including
   > the `count_fn is gold_daily_mention_scores` identity miss. **An unassigned member is decorative
   > and this contract does not admit one.**~~

   **REPLACED BY, and the surviving half is the sharper one:** `NO_COVERAGE` is assigned by the
   existing `else` branch at `publication_gold.py:579` **and is READ by `pool_reader`'s new
   `no_coverage` counter (A.1)** -- assignment without a reader was the R5 defect. **AN UNASSIGNED
   MEMBER IS DECORATIVE AND THIS CONTRACT DOES NOT ADMIT ONE; amendment 4 adds that AN UNREAD MEMBER IS
   WORSE THAN DECORATIVE, because it reads as a clean result.** The skipped-computation case is a
   generation-grain `FAILED` per requirement 1 as replaced, not a daily value.

⚠ **SUPERSEDED IN PLACE BY AMENDMENT 4, R8. THE BLOCK BELOW IS THE AMENDMENT-2 VINTAGE, RETAINED AND
NOT DELETED. `A.2` ABOVE IS THE LIVE ACCOUNTING.**

STOP: **AND IT CARRIED TWO LIVE CONTRADICTIONS, WHICH IS WHY IT IS MARKED RATHER THAN LEFT AS HISTORY**
(`3.0.0_SA_CVO~Z`, R8, msg 25069): its heading said three items gate L4-R while `A.2` supersedes that
accounting and says nothing about them ceasing to gate; and its last bullet asserted the **221-file
census IS the denominator** while `A.2`, **in the same ratified half**, states 221 *"appears in no
denominator here"*. ⛔ **THE CONTRACT ASSERTED BOTH, AND A WORKER QUOTING THE BULLET WOULD HAVE CARRIED
A RETRACTED FIGURE INTO THE BUILD AS RATIFIED TEXT.**

⭐ **WHY IT SURVIVED THREE SUPERSESSION MARKINGS, AND IT IS STRUCTURAL RATHER THAN CARELESS: THE FILE IS
NOT IN CHRONOLOGICAL ORDER.** `A.2` sits ABOVE the paragraph it supersedes and amendment 3 sits BELOW
both, so a LINEAR reader meets the correct accounting FIRST and the retracted one SECOND, with nothing
at the second saying it is spent. **A supersession marker has to sit on the SUPERSEDED bytes, never only
on the replacement** -- the replacement is not where the stale reader is standing. COST: one marker per
superseded passage. NON-APPLICATION: a file whose order IS chronological, where a later section is
self-evidently later.

> ~~**WHAT THIS AMENDMENT STILL OWES BEFORE L4-R, STATED RATHER THAN IMPLIED.** `3.0.0_SA_CVO~Z` set its
> terms before drafting; three are not yet satisfied and are named here with their owner:~~
>
> - ~~STOP: **CONSUMER IMPACT, NOT A CONSUMER LIST.** Amendment 1 names two modules and one test and
>   **grades none**. *"A consumer census that names three and grades none is a list, not an impact."*
>   **Each of Chatter, Price and the legacy republisher is graded BREAKS / DEGRADES / DOES NOT NOTICE.**
>   NOTE: Note also that those three are **logical consumers**, a different grain from Amendment 1's
>   **code modules** -- both are needed and neither substitutes.~~
> - ~~STOP: **ASKED AGAINST THE DEPLOYED STATE, NOT THE REPO.** Amendment 1 is written from repo bytes. **The
>   question is what PRODUCTION does today**, on the same re-basing the served-output incident forced:
>   an amendment is not reviewed as narrow in a plane where production already behaves otherwise.~~
> - ~~**MECE AS A SUBTRACTION FROM A PRINTED DENOMINATOR** -- `2.0.0_SA_COO~Y`'s **221-file bounded
>   census** stated as that denominator.~~

**THE CONTRACT CHOOSES, because R8 is right that it cannot state both.** `3.0.0_SA_CVO~Z` offered either
reading and asked for one; this is the ruling:

1. **CONSUMER IMPACT: tracked work, NOT a bar on L4-R.** `pool_reader` is graded BREAKS and the reader
   change is bound as a CONDITION of the migration by `A.1` clause 4, which is the obligation that
   actually protects callers. Chatter, Price and the legacy republisher stand **NOT_EVALUATED** against
   the daily enum and **an ungraded consumer is never an implied pass** -- but grading them is work owned
   by the lane holding each surface, not a precondition for ratifying correct text.
2. **THE DEPLOYED-STATE QUESTION: tracked work, NOT a bar on L4-R.** ⛔ **Making it a bar would hold a
   correct spec hostage to a measurement no seat can currently take** -- it needs a served-row census,
   and the 20:32Z read is package-identity only. **A bar nobody can clear is not a control, it is a
   stall**, and the served-output incident already showed what an unratified-but-correct contract costs.
3. **THE DENOMINATOR: `A.2` IS LIVE AND 221 IS RETRACTED.** The census is **54 hits across 23 files of
   70,596**, 3 graded and 20 ungraded. **221 was a SOURCE-SEARCH FILE COUNT and is not a population of
   states.**

⚠ **SO NOTHING IN THIS BLOCK GATES L4-R ANY LONGER, AND THAT IS A DELIBERATE RULING RATHER THAN AN
OMISSION.** All three items remain OWED as work, with their owners named, and none is closed by being
un-gated.

**UNCHANGED FROM AMENDMENT 1:** `DENIED` retired rather than split; a genuine publisher refusal
deferred until the harvester fetch-result lineage exists; migration scope **1,595 of 1,596 rows**,
`COMPLETE`/`PARTIAL` untouched.

---

**`C-HV-DAILY-STATUS` -- AMENDMENT 3, same day. `UNDETERMINED` IS REMOVED FROM THE DAILY ENUM.**

`3.0.0_SA_CVO~Z` refused Amendment 1 and asked the question that resolves this: **if the daily half
is offered separately, it must show what it fixes WITHOUT the generation change -- because today's
evidence says the answer may be "nothing."** Answered honestly, the two values split apart:

| change | does it stand alone? |
|---|---|
| **`DENIED` -> `NO_COVERAGE`** | **YES.** It corrects what **1,595 of 1,596 rows ASSERT** -- a reader currently infers a publisher refused us, where the truth is that nothing was collected. That is a real, measurable fix at the daily grain, and it needs no writer change to be true |
| **`UNDETERMINED`** | **NO.** Nothing at the daily grain assigns it. Its whole justification is the generation writer's promotion of a falsey state |

**So `UNDETERMINED` WAS NEVER A DAILY-GRAIN VALUE.** It was placed in the daily enum because that is
where the author was editing, and **that misplacement IS the grain defect both `2.0.0_SA_COO~Y` and
`4.0.0_SA_CRO~Z` detected** -- they were reading the symptom of an editing accident, correctly, as a
contract defect.

**RESULT:**
- **DAILY GRAIN (this clause) is now self-justifying and stands alone:** three values, `DENIED`
  retired, 1,595 rows relabelled truthfully. **Its justification no longer cites
  `generation_writer.py` at all.**
- **THE UNDETERMINED / NON-PUBLICATION OBLIGATION MOVES WHOLLY INTO THE GENERATION-GRAIN CONTRACT**
  (section B above), which remains **OWED AND UNWRITTEN**, together with terminal state, marker key
  and type, receipt state, and the Price and legacy-republisher caller contracts.

**This takes `3.0.0_SA_CVO~Z`'s shape 1 (SPLIT), and the daily half survives the test it set.**

**`C-HV-EVENT-SPINE`.**
- The gold `chatter_event` table (`s3://opal-data-harvest/amgt/harvest/gold/chatter_event/date=2026-09-22`, builder
  output) holds clustered runs of UTC days for one security.
- The working rule: tier A+B articles >= 2, from >= 2 publishers **each contributing at least one tier-A article**,
  merged across gaps of <= 1 day. *(L10 addendum, round 9, `1.0.0_SA_CTO~Z`: the publisher count is taken over tier-A
  articles only. The prior rule counted tier-B co-mentions, and round 9's L9 (`ADJUDICATION_v17` @`6073975682`) found 4
  of 12 events that were not coverage about their own security -- one Nvidia PC story became a Lenovo, Dell and
  Microsoft event with 0 tier-A articles. FWD-6's ACCEPT asks for "bursts of real coverage about the company"; this
  rule keeps exactly the 8 the L9 graded real.)*
- Each event carries its lead headline and its articles.
- *(L10 addendum, round 12, `1.0.0_SA_CTO~Z`, `ROUND_ANALYSIS.round12.md`):* **an event is ONE STORY, not one day.** The
  qualifying rule above (tier-A articles from >= 2 publishers, merged across gaps <= 1 day) applies to each story the
  grouper forms, so a day whose tier-A stories are about unrelated company events yields one event per qualifying story, or
  none. The lead is the story's own earliest tier-A headline. `event_id` carries the story so two events on one day never
  collide. **Calendar words (month and day names) never link two headlines.** Evidence: `3.0.0_SA_CVO~Z` L9 round 12
  (`ADJUDICATION_v20.md` @`19dfdd2579`): 6 of 8 served events are one company event; BA 08-26 is two unrelated stories whose
  tie no lead rule can break, and BA 09-08's deliveries pair linked on the single token "august".

**`C-HV-GOLD-REBUILDABLE`.** Gold is built from silver only. A rebuild from the same silver reproduces identical rows.

**`C-HV-ABSOLUTE-ONLY`.** No gold table of this project stores a relative figure: no ratio, share, z-score or
normalised score. Each is computed where it is served.

**`C-HV-AXIS-PROJECTION`.**
- This REPLACES, in `AMGT_RESAPP`'s ratified `C-ONE-STORE`, the read path of the chatter-axis producer and the coverage
  reader.
- Today they read the association from `publication-links/v1/` and the body from `publications/v1/` through one adapter.
- Once H5 (`chatter_daily`) and H4 (`article_security_mention`) land, both read THOSE gold tables through that same
  single adapter. The served chatter ranks (the DynamoDB TRENDING and BREAKOUT rows) become a projection of
  `chatter_daily`, with their relative figures computed at serve time, never a separate count.
- `publication-links/v1/` and `publications/v1/` retire under `AMGT_RESAPP`'s `C-FORMAT-SEQUENCE`: readers switched,
  writers stopped and the read grant removed, in ONE window, with that move's never-widen pair.
- Until then `C-ONE-STORE` binds as written.
- The matching amendment sits in `AMGT_RESAPP`'s `C-ONE-STORE` (v0.23).

**`C-HV-KEY`.** Every gold row carries `security_key`, and `composite_figi` wherever the crosswalk holds it (the working
key for research, Andrew 2026-09-22).

**`C-HV-EGRESS`.**
- Any live fetch from a publisher is vendor egress and runs only on Andrew's per-use word.
- The validation security is Lenovo (`992_HK_Equity`), under his trial word (one run per publisher).
- The 2026 backfill (FWD-9) runs per security, on Andrew's per-use word for that run, with the listing page count
  per publisher printed BEFORE the run under his quota word.
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

**`C-HV-RANK-DECLARED-SET` (v0.4, FWD-7's denominator).** The chatter rank is a partial rank over a DECLARED publisher set.
- Each generation declares its publisher set. **It is DERIVED, never typed:** every publisher in `ENABLED_PUBLISHERS`, minus any
  publisher whose collection, in the window, EITHER refused for the whole universe OR ran no UNIVERSE-SCOPE job (both read from
  the run records). A publisher has universe-scope collection when the UNION of its jobs' targets (`jobs[]`: publisher,
  security_key) across the window's run records covers the generation's universe, so a backfill run in batches qualifies
  (v0.8). A per-name trial,
  such as sa on ASML or bbg/wsj on Lenovo, is NOT one: it neither adds a publisher nor keeps one in. A publisher outside the set is
  named on the page as not searched. Config decides membership; the run records decide only exit. (v0.7 replaces v0.6's "ran no job
  at all". Under that rule, one trial held 189 of 191 names ineligible on a publisher that never searched them. That contradicts the
  partial-rank research this contract rests on: no estate surface withholds a whole product for one incomplete member.)
- **The census prints, per excluded name, which declared publishers it lacks** (v0.7).
- **An EMPTY declared set HOLDs** with `empty_reason` `NO_DECLARED_PUBLISHER`. Eligibility over an empty set is vacuous and is never
  scored (v0.6).
- A name is ELIGIBLE only if every publisher in the declared set covered every day of the window. Any other name is EXCLUDED
  with its reason (`PARTIAL_COVERAGE`, `NOT_SEARCHED`) and is never scored.
- Eligibility is decided BEFORE the no-signal test. An unsearched name is never read as a quiet one.
- The score counts only articles from publishers in the declared set. A found-only article (`C-HV-COVERED-VS-FOUND`) is
  served on the timeline and never scored, so one name's incidental extra source cannot outrank another's.
- Every generation prints its population: `{declared_publishers, universe, eligible, ranked, excluded: {reason: count}}` and
  the excluded names, through the shared `generation_writer.py`. The footer reads "Ranked N of U names; M not ranked (coverage
  incomplete)".
- FLOOR: 10 eligible names. Below it the generation HOLDs with an `empty_reason`, and the prior generation stays served.
- Grounds: `ledger/CTO_RULING_FWD7_DENOMINATOR_DECLARED_PUBLISHER_SET_20260930.md` (@`ddcc71fd2d`), on the research at
  `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/RESEARCH_PARTIAL_COVERAGE_RANKING_20260930.md` (@`784068f4c0`).

**`C-HV-COVERED-VS-FOUND` (v0.4).** A day row keeps two publisher sets, and neither stands in for the other.
- `publishers_covered_codes` is the set of publishers whose listing for that name ran over that day (SEARCHED).
- `publishers_found_codes` is the set of publishers whose articles that day serves, by whatever path found them (FWD-3 names
  the path per article).
- A publisher in the found set but not in the covered set reads as "found, listing not run", never as "not searched".
- Coverage marks (`data_status`, FWD-7 eligibility) read the COVERED set only. A found-only article never makes a day
  SEARCHED.


**`C-HV-TRUST-TOKEN` (v0.9, Andrew-direct 2026-09-30 ~12:5xZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_125xZ_OPEN_CALLS_RECS_APPROVED_TRUST_TOKENS_BACKOFF.md`).**
- Publisher credentials are read from AWS Secrets Manager. None is asked of Andrew, typed, or harvested by an agent.
- A run starts from the stored trust/session token of a prior successful run. A fresh sign-in or crawl runs ONLY when that token is
  shown not to work.
- **A rate limit is never read as token expiry.** A 429 or throttle response backs off and retries, and the token is kept. Only an
  auth failure that persists after backoff (a 401, or a 403 whose kept body says the session is invalid) marks the token expired.
- Every REST call retries with bounded exponential backoff plus jitter on rate-limit responses. Each attempt's status and wait is
  written to the run record, so a reader can tell throttling from expiry.
- **(v0.10, round-29 analysis; CVO~Z ADJUDICATION_v38 s.2) A bot check is never token expiry.**
  - Each attempt in the run record carries a class. `bot_check` is one of them.
  - A refusal is `bot_check` when its kept body matches a named signature. The list:
    - DataDome's `captcha-delivery.com` page;
    - FT's "Security Verification" interstitial;
    - bbg's press-and-hold challenge.
  - The record writes the matched signature's name beside the class.
  - A `bot_check` attempt never marks the token expired and never starts a sign-in or crawl.
  - It stops that publisher's leg: no retry is made against a check.
  - A new signature is added to the list when a kept body shows one, never inferred.
  - Expiry still reads as above: an auth failure that persists after backoff whose kept body matches no bot-check signature.
  - **(v0.11, CVO~Z msg 27289)** Every refusal keeps its body, bounded as ft's F1 is. A refusal with no kept body is `unclassified`,
    and `unclassified` is never expiry. A missing body cannot pass the signature test vacuously.
  - **(v0.13, FWD-11) A `bot_check` routes the leg to the CHALLENGE PATH; it no longer only stops the leg.** The amended rule:
    - The leg hands the challenge to the challenge path (`lib/opal_data_harvest/verification.py`, extended to every publisher)
      inside the SAME browser identity that met it (`C-HV-ONE-IDENTITY`).
    - A blind retry against a check stays forbidden. The challenge path is the only retry.
    - If the challenge path does not pass, the leg stops and the run record writes `bot_check` + `challenge_failed` with the
      signature. That is a result to work on, never a final state (`C-HV-NO-DEFEAT`).
    - Solving a challenge is not a sign-in. The trust-token order above is unchanged.

**`C-HV-ONE-IDENTITY` (v0.13, FWD-13).**
- Each publisher has ONE persistent browser profile on the site Z box, and it is the only source of that publisher's session.
- A request carrying the session either runs inside that browser's tab or presents that browser's TLS fingerprint AND
  User-Agent. No hard-coded User-Agent string is permitted on any publisher path.
- No client writes cookies back over the browser's stored session. Only the browser updates its own session.

**`C-HV-NO-DEFEAT` (v0.13, FWD-11; Andrew-direct ~2026-10-01T04:0x-04:1xZ).**
- AMGT_HARVST is not closed, parked, abandoned or reported BLOCKED as a final state until FWD-11 is DONE.
- A round whose collection is refused carries the refusal forward as the next round's input, never as the project's
  outcome.
- Licensed bulk access (Factiva or any other) is not a route.

---

## 2. THE BOUNDARY

**In:**
- the five publishers' retrieval (SA, Bloomberg.com, Barron's, WSJ, FT);
- bronze, silver and gold for them;
- the chatter projection;
- the timeline graph and its dissection on the security page;
- the desktop outbox upload;
- (v0.13) the challenge path for all five publishers, one browser identity per publisher, and the site Z backfill
  driver (a run the operator starts; not a schedule).

**Out:**
- non-English press for HK and JP names (the brief's call 5: UNRESOLVED-BY-DESIGN in this version);
- the social feed;
- SERP;
- every non-publication channel;
- any cadence or schedule, which stays Andrew's;
- any deletion.

## 3. CONSTRAINTS ON THE CUT

- No relative figure is stored in any gold table (`C-HV-ABSOLUTE-ONLY`).
- Build order follows dependency:
  1. bronze capture;
  2. silver from bronze;
  3. retrieval provenance and watermark;
  4. gold mention;
  5. daily;
  6. event;
  7. projection and page.
  The desktop upload is independent. The 2026 backfill (H10) runs after H1-H6, per security, on the word for that run.
- The mention floor may not be raised by any cell.
- A weight or threshold is a working default, stated in the deliverable, never invented as a constant elsewhere.
- Bloomberg's per-symbol `news()` call (`bloomberg_rest_fetch.py:119-123`) is tried once in the validation run, inside
  the cap. It is adopted or recorded UNRESOLVED with its reason.
- **(v0.13) FWD-12 comes first.** No backfill (H10, H14) writes to the store until FWD-12 is DONE, because the
  wrong-object rows already feed `chatter_daily`.
- **(v0.13, placement R7) Egress.** sa keeps the route it runs on today. No new residential (Bright Data) arm is opened
  for bbg, wsj, barrons or ft without Andrew's per-use word (section 5). Every other FWD-11/FWD-13 act proceeds without it.
- **(v0.13) No licensed route.** No cell proposes or builds licensed bulk access (Factiva or any other); Andrew ruled it
  out ~04:0xZ.

## 4. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

| # | surface | engine | depends on | outcome |
|---|---|---|---|---|
| H1 | bronze capture, articles and listings, 5 publishers | `lib/opal_data_harvest/publishers.py` (`raw_bytes` on every path), the rk-85 bronze writer | -- | FWD-1 |
| H2 | silver from bronze (`article`, `listing_hit`) | `harvest_grammar.article_silver_row` rebuilt to read bronze | H1 | FWD-2 |
| H3 | retrieval rungs, provenance, watermark | the harvester's discovery calls | H1 | FWD-3 |
| H4 | gold `article_security_mention` | a new gold producer over silver | H2, H3 | FWD-4 |
| H5 | gold `chatter_daily` (absolute only, dense from 2026-01-01) | same producer | H4 | FWD-5, FWD-7, FWD-9 |
| H6 | gold `chatter_event` | same producer | H5 | FWD-6 |
| H7 | the chatter projection (DynamoDB ranks from `chatter_daily`) | the chatter-axis Lambda | H5 | FWD-7 |
| H8 | timeline graph and dissection | the portal security page plus `scoped_amgt.py`; design spec first | H5, H6 | FWD-5, FWD-6 |
| H9 | desktop outbox upload into the new grammar | `lib/opal_data_harvest` uploader | H1, H2 | FWD-8 |
| H10 | the 2026 backfill run: floor 2026-01-01 plus watermark, page counts printed first, `retrieval_mode=backfill` | the harvester, H1-H6 end to end | H1-H6 | FWD-9 |
| H11 | sa wrong-object repair: quarantine, listing body, page cap | `lib/opal_data_harvest/publishers.py` (`:540`), `sa_rest_fetch.py` | H1 | FWD-12 |
| H12 | one browser identity per publisher: persistent profile, in-tab or matched TLS+UA transport, no cookie write-back | `lib/opal_data_harvest/auth.py`, the `*_rest_fetch.py` clients, the harvest sessions | H1 | FWD-13 |
| H13 | challenge path for all five publishers | `lib/opal_data_harvest/verification.py` (`contracts.json:80`) | H12 | FWD-11 |
| H14 | site Z backfill driver over 89 names: budget, checkpoint/resume, uploads on, sa first, date-ordered bbg/wsj discovery | a new driver over the harvester | H11, H12, H13 | FWD-14, FWD-15 |

## 5. CALLS THAT STAY ANDREW'S (the brief's s.8)

The build proceeds on the working defaults above. His word changes a value, not a contract:
- the tier weights;
- whether a tier-D passing mention counts in the axis (default: yes, at 0.1);
- the roundup threshold;
- the event thresholds;
- non-English press (out of this version);
- publisher terms on stored bodies (already his);
- (v0.13) a residential (Bright Data) egress arm on the site Z box for bbg, wsj, barrons or ft: his per-use vendor word
  (CLAUDE.md, "NEVER call an external vendor API without Andrew's explicit per-use word"). "At all costs" does not name
  that use (placement R7). FWD-11 and FWD-13 proceed without it.

**Ruled by Andrew, not open (v0.13):** automatic challenge solving stays on and is extended (FWD-11); licensed access
is not a route; the publisher-terms and legal risk the brief recorded (IV.5) is his accepted call and is not
re-litigated by any seat.

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
