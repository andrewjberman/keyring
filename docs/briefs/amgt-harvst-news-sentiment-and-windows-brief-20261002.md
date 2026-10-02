# AMGT_HARVST -- news-scanner sentiment, rolling windows and the spike layer: MIDSTREAM brief (L1)

```
BRIEF PATH        docs/briefs/amgt-harvst-news-sentiment-and-windows-brief-20261002.md
PROJECT           AMGT_HARVST (D5), midstream
EXISTING PRD      org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md v0.13
ROUTE             4.0.0_SA_CRO~Z -> 1.0.0_SA_CTO~Z (filter, fold into /canonical-flow) -> 2.0.0_SA_COO~H
ANDREW'S WORD     org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261002_173xZ_SECURITY_ANALYSIS_UIUX_WALK_BRIEFS_TO_CTO_Z.md @a48c546a1c
SIBLING BRIEF     docs/briefs/dsgn-amgtv1-security-analysis-uiux-brief-20261002.md (frontend, 2.0.0_SA_COO~D)
EVIDENCE          org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/SECURITY_ANALYSIS_UIUX_20261002/SENTIMENT_BUBBLE_FINDINGS.md
                  org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/SECURITY_ANALYSIS_UIUX_20261002/PATTERN_MAP.md
FINDINGS REGISTER docs/briefs/amgt-security-analysis-ui-findings-20261002.json (rows owned by 2.0.0_SA_COO~H)
MEASURED AT       2026-10-02 17:5xZ (code at workspace CLOUD HEAD, portal DEV a730d8ce; one read-only S3 read of gold)
```

Andrew's words carried here (record above, verbatim):
- *"We also should look into the finbert scoring mechanism for the current news scanner and probably inflect the same sentiment
  scoring colorway that is used in Topic Cloud for this."*
- *"set up a fork or subagent specific to the bubble chart sentiment scoring pattern for the news scanner because i want COO~H to
  go get that feature incorporated, also we should have a better period function than just clicking month/earlier month. I
  would suggest a rolling 30 day, 90 day, and 365 day view."*
- *"backend news scanner tie in feature work should go to COO~H. CTO~Z should receive everything first."*

**"The news scanner" (inferred):** the Security Analysis Lead Panel's chatter collage, plus each company's timeline and its day
articles. HARVST gold feeds both. The Market Overview news pipeline (Topic Cloud) is a separate corpus, and it is where
FinBERT runs today.

---

## PART 0 -- How the blind constraint was honoured, and where it bent

- **Not read:** HARVST task orders, `phase` and `blocking`.
- **Read:** the PRD's ENDPOINT (FWD-4 to FWD-7, FWD-9), the served code, and one read-only S3 read of the newest gold
  snapshots.
- **Where it bent:**
  1. The sentiment fork read `publication_gold.py` at HEAD. That code carries this morning's round work: title and
     `published_precision` joined the mention rows at @b7e88285ac (HVST-aj-7). So the brief knows the mention row now carries
     the title. That is served reality on the producer, not the branch.
  2. This seat researched track C of RESAPP round 63 today (@adb64006ed). It therefore knows the CTO's ruling that the headline
     rides gold, and that ruling shaped O2's "the score rides gold beside the title".
- **What is unchanged:** FWD-5 (the timeline) and FWD-6 (events as spans) still describe the right territory. This brief adds
  sentiment and windows to them; it does not move them.

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1 of this addendum):** a PM on Security Analysis, the default window, opens the chatter collage and reads
one name's tone this period: its colour, its scored-article count, and the articles behind it. That journey runs from FinBERT,
through gold and the served route, to the bubble.

### O1 -- A PM reads at a glance whether a name's coverage this period reads positive or negative
- **Who and what:** in the chatter collage, each name's bubble carries its coverage tone in the same colours Market Overview's
  Topic Cloud uses. The hover says how many articles actually carried a tone, out of how many were scored.
- **This brief's half:** a tone figure and its two counts, per name per window, on the served chatter payload.
- **The other half:** the colour, which is the frontend's (sibling brief).

### O2 -- An analyst opening a day on a company's timeline sees each article's tone beside its headline
- The day's article rows carry each article's FinBERT tone (label and signed score).
- The day series carries the day's tone figure and its two counts, so a hover can show them.
- **Placement:** the score rides gold beside the article's title, scored once per version of the article, and is never
  recomputed at request time. This follows the CTO's track-C ruling of 14:01Z for the headline.

### O3 -- "FinBERT not being sure is not a vote"
- A name or day whose scored articles are all neutral reads "no scored tone", never a neutral zero that drags the average.
- Every tone figure travels with its voters and its scored count, side by side.
- **Source:** Andrew-direct 2026-09-16, recorded in `NEWS_SCANNER_DEEP_DIVE_20260916.md` section 6: *"finbert not being sure is
  not a vote"*.

### O4 -- A PM switches the chatter view between the last 30, 90 and 365 days
- The served chatter answers a rolling window, not only a calendar month.
- When the store's history is shorter than the window asked for, the answer says where the window really starts. It never
  silently serves less than was asked.

### O5 -- A PM sees what was happening at a spike, marked on the timeline itself
- The coverage events at spikes are dense enough to mark the spine where coverage actually burst. Today the store holds 8
  events estate-wide (PART VI).
- Each event carries its lead headline.
- **Relation to HARVST's endpoint:** this restates FWD-6 at the density a PM needs. It does not add a new outcome.
- **What is not HARVST's:** earnings releases and other corporate-event dates are not harvest data (PART II).

## PART II -- WHERE THE BOUNDARY SITS

| owned here (AMGT_HARVST, 2.0.0_SA_COO~H) | relied on, owned elsewhere |
|---|---|
| Scoring HARVST articles with FinBERT, the scores in gold, the tone and windows on the served chatter and timeline payloads, and event density at spikes | **The FinBERT scorer itself:** Lambda `opal-news-ai-sentiment` and its batch driver, owned by the news pipeline. Reuse it; do not fork it. |
| | **Colour, collage, tooltip, modal and period buttons:** DSGN_AMGTV1, `2.0.0_SA_COO~D` (sibling brief). |
| | **The served route code in `lib/research/api/scoped_amgt.py`:** shared with AMGT_RESAPP (`2.0.0_SA_COO~Z`). Which seat writes the route lines is the CTO's call at the fold. |
| | **Earnings and corporate-event dates for the spine (N4):** NOT harvest data. The owner is unassigned; the CTO names one (RESAPP's security data, or a new source). |
| | **The GPT gap-fill** for neutral-only articles, which the news pipeline uses under Andrew's 09-16 rule: OpenAI egress, which needs Andrew's word (`org/ref/VENDOR_EGRESS_WHITELIST.yaml` lists NopeCHA only). |

## PART III -- THE QUALITATIVE BAR

- A PM reads a name's tone on Security Analysis that they would otherwise have gone to Market Overview's Topic Cloud to read,
  and the two pages agree on what a colour means.
- No figure reads "neutral" because FinBERT abstained. A reader can always tell "no tone" from "a balanced tone".
- A PM asking for a year gets a year, or is told in words that the store begins later. They never get a shorter window that
  looks like a year.
- A spike on the spine has a reason a PM can read, at the spike.

## PART IV -- THE SUBSTRATE (findings, each measured unless marked)

| # | finding | evidence |
|---|---|---|
| S1 | **FinBERT already runs in the estate.** Lambda `opal-news-ai-sentiment` is a container image, 3008 MB, 900 s, invoked by other Lambdas. `finbert-batch-processor` drives it 14 times a day over DynamoDB `opal-news-articles`. | `infra/aws/terraform/news-pipeline/lambdas.tf:246-268`, `finbert-batch.tf:47-92`; `infra/aws/lambda/finbert_batch_processor/lambda_function.py:30-70` |
| S2 | **Score shape:** a label (positive, negative or neutral) and a confidence. Stored signed: +confidence, -confidence, and **0.0 for neutral**. | `lambda_function.py:77-106`, `:153-157` |
| S3 | **HARVST gold carries no tone today:** no score, label or confidence field in `article_security_mention`, `chatter_daily` or `chatter_event`. | `lib/research/harvest/publication_gold.py:64-90`, `:382-420`, `:1078-1092` |
| S4 | **Text to score exists:** silver `article` carries `title` and `text_blocks`. The mention matcher already treats the first 3 blocks as the article's lead. | `publication_gold.py:179-191` |
| S5 | **The chatter route is calendar-month only, with no window parameter.** It sums `chatter_daily.articles_total` per name per month. | `lib/research/api/monthly_chatter.py:1-38`; `scoped_amgt.py:4903-4917` |
| S6 | **The timeline route already takes `from`/`to`,** and `chatter_daily` already stores `trailing_7d_sum` and `trailing_30d_sum`. | `timeline_api.py:262-276`; `publication_gold.py:396-397` |
| S7 | **Gold depth:** `chatter_daily` runs 2026-01-01 to 2026-10-02 (275 days, 212 names). 30 and 90 days are covered; **365 days is not.** | the S3 read at 17:5xZ, newest `part-20261002T170716Z` |
| S8 | **Events are sparse:** `chatter_event` holds 8 rows estate-wide, and its newest snapshot (09-30) is two days older than daily. | the S3 read at 17:5xZ, `part-20260930T001658Z` |
| S9 | **The Topic Cloud colorway** is `getSentimentColor()`: -1..+1 clamped to +/-0.5, red `#f5365c` to yellow to green `#2dce89`. The colour stays in the portal; gold carries no colour (rule 17b). | `portal/src/components/market-performance/TopicCloud.tsx:44-90` |
| S10 | **Prior art for the placement:** today's ruling put the headline into gold, beside the mention, scored once per `record_hash` (this seat's precedent research, @adb64006ed; CTO msg 28511). | as cited |

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- **Invoke permission:** the role that runs the HARVST gold build can invoke `opal-news-ai-sentiment` (the pattern is
  `news-pipeline/iam.tf:293-296`). Which role runs the build is NOT established.
- **Naming:** a new gold table's name and address are builder output under rule 30 (`lib/opal_naming.py`). Whether HARVST, an
  existing pipeline, takes that now is the CTO's call.
- **Served output moves:** new fields on the chatter and timeline payloads, and a window parameter. That needs a never-widen pair
  (CTO + COO) naming the blast radius.
- **The one-time scoring of the existing corpus** (about 8,700 articles in silver, inferred from TRACKC) depends on the scorer's
  throughput per invocation, which is not measured.
- **The 365-day window** needs either history before 2026-01-01 or a stated start. Which of the two is Andrew's call or the
  CTO's.
- **Re-scoring:** a re-silvered article (a new `record_hash`) gets a new score. Scoring is keyed to the article's version, not its
  key alone.

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-02 17:5xZ. This ages; do not cut outcomes from it.
- HARVST gold: mention rows 23,691 (title and precision since @b7e88285ac); daily 58,300 rows over 275 days and 212 names;
  events 8.
- No tone anywhere in HARVST gold or on the Security Analysis payloads.
- The chatter collage is one blue on a fixed 4-column grid in served order. Its period control is "Earlier month" / "Later month".

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- The scorer's model revision and handler source: the image is built by CI and its source is not in the repo.
- Whether the GPT gap-fill is deployed in the news pipeline today.
- The scorer's throughput, and so the time to score the existing corpus.
- That FinBERT is the right model for long-form publications (sa, ft, wsj, bbg, barrons). It was tuned on financial phrases. Its
  fit on a headline plus a lead paragraph is inferred from the news pipeline's use, not measured on HARVST text.
- Where earnings and corporate-event dates come from.
- Any decomposition, sequence or cell. That is step 5.

## Findings register rows owned here

From `docs/briefs/amgt-security-analysis-ui-findings-20261002.json`:
- **SAUX-19** (owner `2.0.0_SA_COO~H`): no sentiment value is served for harvested articles or per name, so the page has
  nothing to colour by. That is O1, O2 and O3 here.
- **Data rows the walk assigned to `2.0.0_SA_COO~Z` that rest on this brief:**
  - **SAUX-28:** chatter counts are served per calendar month, so no rolling window can be drawn. That is O4 here, and the
    route lines are the CTO's split.
  - **SAUX-10:** there is no earnings layer, and VLO has no events. That is O5 here for the harvest-event half.
- **The frontend halves** of all three are in the sibling brief's O5, O7 and O2.
