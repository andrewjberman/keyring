# AMGT_HARVST: what the standing collection was to be, what each fetcher reaches and on whose word, and what a daily sweep would draw

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z (msg 31626, the design fork on the 30-day news feed).
**Written:** 2026-10-08 ~08:4xZ. From the repository and its records only. No vendor call, no S3 read. The one
command run was the backfill driver's `--dry-run`, which prints `NETWORK CALLS: 0`.

## Answer in five lines

1. **The brief and PRD specify NO standing collection.** They specify a backfill and an on-demand run, and they put
   "any cadence or schedule" outside the project, reserved to Andrew.
2. **Andrew did describe a standing local collector once, on 2026-09-14,** and then held its cadence the next day
   until a validation report. That hold has never been lifted in any record I found.
3. **Every collection word since has been per-use:** one run, one publisher set, one occasion.
4. **A daily sweep would draw about 35 to 40 articles a weekday** across the five sources. That is the store's own
   steady rate, so a sweep does not make the 30-day feed deeper. It makes it current and covers names never run.
5. **The three empty names are not caused by the missing sweep.** Caterpillar and CSL are not in the collector's
   universe at all, and AIG's stored name is truncated to a string no headline carries.

## 1. What the brief and PRD say the standing collection was to be

| Source | Text | What it makes of a standing collection |
|---|---|---|
| PRD section 2, OUT (`AMGT_HARVST_PRD.md:1071`) | "any cadence or schedule, which stays Andrew's" | outside the project |
| PRD section 2, IN (`:1063-1064`) | "the site Z backfill driver (a run the operator starts; not a schedule)" | the only collector in scope is hand-started |
| FWD-9 (`:229-240`) | each company's history since 2026-01-01, "running it again adds nothing" | a backfill |
| FWD-10 (`:244-267`) | "one on-demand run on the cloud harvester" from a stored long-lived token | on-demand; the end state is cloud, the box "until the local job matures" |
| FWD-14, FWD-15 (`:328-362`) | 50+ articles per security since January; a driver that survives interruption | backfill depth and a backfill driver |
| FWD-17 (`:387-403`) | tone and counts for rolling 30, 90 and 365-day windows ending at T-1 | **a consumer that assumes fresh articles, with no producer of them named** |
| `C-HV-EGRESS` (`:959-965`) | "Any live fetch from a publisher is vendor egress and runs only on Andrew's per-use word" | a schedule cannot run under this contract as written |
| `config.json` | `recurring_schedule_enabled: false`, `daily_start_time: null`, `automatic_uploads_enabled: false`, `jobs_per_run: 1` | the switch exists and is off |

So the gap the evidence shows is in the specification itself: FWD-17 added rolling windows on 2026-10-02 and nothing
added the collection that keeps a rolling window fed.

## 2. Andrew's words on the mechanism and cadence, in order

| Date | Record | His words | Effect |
|---|---|---|---|
| 2026-09-14 | `4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260914_DOWJONES_HARVEST_W.md` | "i think this whole operation needs to be handled local on this device with some kind of local cron job that cycles through the various platforms for the various securities in a polite manner so no rate limiting" | **the one description of a standing collector:** local, scheduled, cycling publisher by security, paced |
| 2026-09-15 | `..._20260915_HARVEST_REMEDIATION_LOOP_W.md` | "ping me, and we will decide the mechanism of how the data is pulled. I suspect it is A.) Too aggressive to pull 5+ articles from every single ticker from every single platform every single day ... B.) ... articles have to be keyed on some kind of stable key so we dont keep pulling the same ones" | **cadence HELD.** The mechanism and pace are his to decide after validation. Carried in `org/ref/LIVE_ARMS.md` as "the collection mechanism and cadence RESERVED to Andrew" |
| 2026-09-30 | PRD FWD-10 source | "rest api pulls through dedicated shapes per publication, ideally running entirely on a lambda ... Maybe its a local job until it matures" | the transport and the host, not a cadence |
| 2026-10-01 | `4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261001_034xZ_...` | "the process for backfill on these companies be a local, sitez Box process"; "50+ articles per security going back to January" | the backfill, local |
| 2026-10-03 | `2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261003_17xxZ_...` | "it is inappropriate for agents to adjust our data engineering operations without my explicit directive ... We will discuss internally on how to proceed with further data collection after review" | collection paused; a schedule built on inference would be exactly what this forbids |
| 2026-10-04 | `1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_204xZ_...` | "yes" to "one universe-scope run per publisher" | ONE run per publisher. The record itself says it "does NOT word a recurring cadence" |
| 2026-10-05 | `2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261005_025xZ_...` | "Dont attempt FT until I return because our system cannot handle it autonomously yet, the rest of the publications are good to go" | ft held; the other four proceed, for that run |
| 2026-10-06 | `2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261006_183xZ_...` | "proceed where we are getting results (bloomberg barrons and wsj) and we deal with FT later"; "SA shouldnt need Bright Data ... logging in via google credentials, then in the browser window using the same session" | ft deferred; sa moves to the in-tab route |

Two things in the 09-15 word already answer part of the design: his own doubt that every ticker on every platform
every day is right, and his requirement that a held article is never pulled twice. The second is built
(`C-HV-BRONZE-AS-RECEIVED`: "A held article is never re-fetched").

## 3. What each fetcher reaches, and under which word

From `lib/opal_data_harvest/publishers.py` `REGISTRY` and `discovery.py` (docstrings and registry values read).

| Source | Listing (how it finds articles) | Grain of the listing | Body | Egress | Standing word |
|---|---|---|---|---|---|
| sa | `/api/v3/symbols/{sa_symbol}/news`, body taken from the listing | **per security** | in the listing | native in-tab, persistent profile, no proxy (Andrew 2026-10-06 ~19:2xZ) | per-use; 10-05 "good to go" for that run |
| bbg | search `nemo-next/api/search/query?query={company}`, at most 3 pages and 20 new bodies a job; date-ordered discovery uses the monthly news sitemap, about 6,900 items a month | search is per security; **the sitemap is per publisher** | `/article/api/story/id/{id}` JSON | native | per-use; resumes "with Andrew present to hand-solve its challenge" (CTO ruling quoted in the 10-06 record) |
| wsj | `/search?query={company}`; date-ordered discovery uses the monthly sitemap, about 2,800 to 3,100 items a month | search is per security; **the sitemap is per publisher** | page-embedded JSON | native | per-use; as bbg |
| barrons | `/search?query={company}` | per security | `/articles/api/articles/{slug}` JSON | native; automatic slider verification qualified | per-use; as bbg |
| ft | `ft.com/search?q={company}` | per security | page JSON-LD; premium-labelled teasers skipped | native | **held**: "deal with FT later" |

The driver's own budget line, from its dry run today: universe 234; each source "4320 requests/day (pacing
86400/(15s minimum + 10s jitter/2) = 4320; no per-publisher daily cap in config or contracts)". So the only limit in
code is pacing. No publisher has a stated daily cap.

## 4. What a daily sweep would draw per day

### Articles

The evidence file's Table A counts stored articles by the day they were PUBLISHED. Mean per weekday, from that table:

| Period | bbg | wsj | barrons | sa | ft | All five | Weekend day |
|---|---|---|---|---|---|---|---|
| 2026-07-13 to 08-28 (35 weekdays) | 15.1 | 3.7 | 0.2 | 13.4 | 0.5 | 32.9 | 6.5 |
| 2026-09-08 to 10-02 (19 weekdays) | 14.9 | 2.6 | 8.6 | 10.4 | 0.3 | 36.8 | 5.0 |

The last 30 days hold 714 articles (bbg 288, wsj 52, barrons 162, sa 207, ft 5), which is the "about 700 a month".

**The rate is flat from July to October.** bbg reads 15 a weekday in both periods. So the last 30 days are not thin
compared with the months before them: about 35 to 40 a weekday is what this universe, this matcher and these per-job
caps yield. A daily sweep would add roughly that many new articles a day, no more. The one place the store IS thin
is its trailing edge: 2026-10-06, 10-07 and 10-08 hold 6, 1 and 0. That edge is what "no daily sweep" costs.

Barrons rising from 0.2 to 8.6 is collection reach changing (its history before September was not collected),
not publishing changing.

### Requests

| Shape of sweep | Requests a day | Against the pacing budget of 4,320 per source |
|---|---|---|
| Per security, per source, as the backfill runs today (234 names x 1 listing request, plus bodies) | about 234 listing requests per source, plus about 15 bodies on bbg, 9 on barrons, 3 on wsj; about 1,170 listing requests in all | 5 to 6% of each source's pacing budget; about 80 minutes a source at the configured pace |
| Per publisher, from the sitemap (bbg, wsj): one current-month file, matched to all 234 names locally, then the matching bodies | 1 listing request plus bodies | negligible |

For scale against what has actually run in a day (Table C, jobs finished): bbg 107 on 10-07, wsj 158 and barrons 188
on 10-05. A 234-job sweep per source is 1.2 to 2.2 times the busiest day so far, every day.

**The sitemap route already exists for bbg and wsj** (`discovery.py`, HVST-ae-5) and is the cheaper shape for a
sweep: the listing is per publisher, so one fetch serves every name. sa, barrons and ft have per-security listings
only in the registry. `discover` takes one company's query; I did not trace whether the sitemap is fetched once per
job or cached across jobs.

## 5. What a sweep would not fix

| Finding in the evidence | Cause, measured | Fixed by a sweep |
|---|---|---|
| Caterpillar 0, CSL 0 | Neither has a record in the collector's identity file. The universe is 234; the crosswalk holds 237; the three missing keys are `CAT_US_Equity`, `CSL_AU_Equity` and `6861_JP_Equity` (measured 2026-10-07, `HARVST_AZ1_BRAND_ALIAS_SOURCES_20261007.md`) | no: they are never asked for |
| AIG 0 | Its stored company name is `American International Group I`, cut off mid-word. Search and slug matching both use that string | no: the query cannot match |
| Depth per name | per-job caps (bbg 3 pages and 20 new bodies; `candidate_limit` 20) and the legal-name matcher (130 of 234 names need two or more slug words) | no |
| An unattended run | bbg's bot check still needs Andrew's hand (round 49 ADDENDUM 3); FWD-11, the unattended run, is the project's closing condition and is not DONE | **a scheduled sweep depends on FWD-11** for bbg, and on the ft hold lifting for ft |

## 6. Calls for the ruling

1. **A schedule is Andrew's word, not a design choice.** The PRD puts it out of scope, `C-HV-EGRESS` makes every
   fetch per-use, his 09-15 hold reserves mechanism and pace, and his 10-03 word forbids changing data operations
   without his directive. The design can be ruled and built with the switch off; turning it on is a card for him.
   The card can quote his own 09-14 description back to him, with the measured draw.
2. **Which shape.** Per publisher from the sitemap where one exists (bbg, wsj), per security elsewhere, is the
   smallest draw. It also answers his 09-15 doubt about every ticker on every platform every day.
3. **Which sources on day one.** bbg needs a hand today (round 49 ADDENDUM 3) and ft is held by him. For sa, wsj
   and barrons I found no record saying whether a run completes unattended; that is a read for the issuer before
   any of the three is scheduled.
4. **The three empty names and the depth caps are separate cells**, already partly owned (the alias cell az-1, the
   truncated-name class I raised yesterday, the identity file's three missing keys).

## What bounds this

- Counts in section 4 come from one worker's evidence file (`BK1_PER_SOURCE_PER_DAY.md` @0ae995ac2b); I computed
  the means from its Table A and did not re-derive the table from the store.
- Table A counts what is STORED, so it understates what the publishers published about these names wherever a
  backfill was capped or never ran. The flat rate is evidence about the collector's yield, not about the news.
- Request counts for a per-security sweep assume one listing request a job. bbg allows up to 3 pages, so its real
  figure is between 234 and 702.
- I searched the Andrew-direct records for September and October by file name and by cadence words. 127 files
  mention the harvest; I read the six named in section 2 and the two quoted in the PRD. A cadence word in a record I
  did not open is not excluded.
- I did not read the project's STATUS or the current round's task orders, so work already cut toward a sweep is not
  covered here.
