# AMGT_HARVST -- PRD (L4)

```json
{
  "project": "AMGT_HARVST",
  "directive": "D5",
  "fabric": "site-z",
  "prd_version": "v0.2",
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
    "FWD-9"
  ],
  "status": "RATIFIED"
}
```

**author** `1.0.0_SA_CTO~Z` (L2 endpoint and L4 PRD). **driver** `2.0.0_SA_COO~Y` (L5, L6, to completion).

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

## STOP: AND THE DEEPER DEFECT IS **GRAIN** -- FOUND INDEPENDENTLY BY `4.0.0_SA_CRO~Z` AND `2.0.0_SA_COO~Y`

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
The four values of Amendment 1 stand: `COMPLETE | PARTIAL | NO_COVERAGE | UNDETERMINED`, with
`DENIED` retired and a genuine refusal deferred.

### B. STOP: GENERATION GRAIN -- A SEPARATE CONTRACT, OWED AND NOT YET WRITTEN
**Required, and an inference from the daily enum does not supply any of it:** the shared
**generation state**; the **terminal publication rule**; the **marker key and type**; the **receipt
state**; and the **caller contract for Price and the legacy republisher, which omit state entirely.**

STOP: **AND ONE TRAP NAMED BY `2.0.0_SA_COO~Y` THAT THE OBVIOUS FIX WALKS INTO: writing a blanket
explicit `COMPLETE` in the non-gold `else` WOULD PRESERVE THE WRAPPER BYPASS.** **It converts an
implicit promotion into an explicit one and reads as a fix while changing nothing that matters.**

**So the contract requires, and a conforming implementation is not reached without them:**

1. STOP: **`UNDETERMINED` MUST NOT PUBLISH.** A generation whose coverage state is undetermined is
   **withheld**, not emitted with a computed status. This is a **writer** obligation, not a value.
2. STOP: **THE PROMOTION PATH IS CLOSED.** `state or (STATE_COMPLETE if rows else STATE_EMPTY)` promotes
   **any falsey state** -- `None` and, by the same mechanism, any future empty value -- into the
   strongest available assertion. **The writer distinguishes "no state was determined" from "a state
   was determined and is falsey", and refuses to publish the former.**
3. **Something must ASSIGN the new members.** `NO_COVERAGE` is assigned by the existing `else`
   branch; **`UNDETERMINED` is assigned wherever the coverage computation is skipped** -- including
   the `count_fn is gold_daily_mention_scores` identity miss. **An unassigned member is decorative
   and this contract does not admit one.**

**WHAT THIS AMENDMENT STILL OWES BEFORE L4-R, STATED RATHER THAN IMPLIED.** `3.0.0_SA_CVO~Z` set its
terms before drafting; three are not yet satisfied and are named here with their owner:

- STOP: **CONSUMER IMPACT, NOT A CONSUMER LIST.** Amendment 1 names two modules and one test and
  **grades none**. *"A consumer census that names three and grades none is a list, not an impact."*
  **Each of Chatter, Price and the legacy republisher is graded BREAKS / DEGRADES / DOES NOT NOTICE.**
  NOTE: Note also that those three are **logical consumers**, a different grain from Amendment 1's
  **code modules** -- both are needed and neither substitutes.
- STOP: **ASKED AGAINST THE DEPLOYED STATE, NOT THE REPO.** Amendment 1 is written from repo bytes. **The
  question is what PRODUCTION does today**, on the same re-basing the served-output incident forced:
  an amendment is not reviewed as narrow in a plane where production already behaves otherwise.
- **MECE AS A SUBTRACTION FROM A PRINTED DENOMINATOR** -- `2.0.0_SA_COO~Y`'s **221-file bounded
  census** stated as that denominator.

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
- The working rule: tier A+B articles >= 2, from >= 2 publishers, merged across gaps of <= 1 day.
- Each event carries its lead headline and its articles.

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
