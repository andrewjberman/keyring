# Four-publication harvest: five-security live test on SiteZ

**Author:** 4.0.0_SA_CRO~W (Chief Research Officer)
**Date:** September 14, 2026, US Eastern (request timestamps are UTC, September 15)
**Authority:** [Andrew's instruction and live-test clarification](ANDREW_DIRECT_20260914_HARVEST_LOCAL_BACKFILL_REVIEW_W.md)
**Evidence:** [Live calls, script hashes, shapes, and local artifact hashes](HARVEST_LIVE_BATCH_EVIDENCE_20260914_W.json)
**Status:** LOCAL evidence and report; no push, bulk backfill, or recurring task.

## Result

Executed the existing publication clients live on this Windows SiteZ device for **BA, COST, HD, INTU, and VLO**, selected from the checked-in 89-name universe. Existing bucket objects are not evidence for these results. No production client was edited. Local harnesses called the existing functions and recorded the exact source hashes.

The test establishes useful access, but **does not establish a clean, complete four-publication article collection**. SA reports and news returned across the batch; analysis responses are fragments. FT can deliver substantial article HTML, but its extractor discards the body or accepts a subscription page. WSJ discovers company-linked news with variable latency, while its article extractor admits CSS. Bloomberg stopped at its challenge.

| Source | Live batch result | Body result |
|---|---|---|
| Seeking Alpha | 5/5 symbol resolutions, 5/5 reports, 25 news records, 10 analysis-list entries; 26 helper calls including account check returned | Five sampled analysis bodies have only 225-310 visible characters and end as introductory fragments. All five reports have 5,194-5,852 characters without detected HTML. News content is HTML within JSON. |
| Financial Times | 5/5 summary/profile pairs returned. All five captured company summary pages expose eight FT teaser links. | Corrected five-article sample: three byline-only outputs; one subscription-page output; one 70-second timeout. No accepted clean article from the existing extractor. |
| WSJ | 4/5 company-news calls returned initially; VLO recovered on one bounded repeat. Five feeds contain 504 entries before deduplication. | Five WSJ-host article calls returned, but all five outputs contain CSS (105-117 detected markers each). Full subscriber text is unproved. |
| Bloomberg.com | Account endpoint returned 200; first ticker call, BA:US, returned 403 with challenge JSON. Four other securities were not attempted after that block. | No article body collected. Existing session harvester ran with an eight-step cap and exited 1 without clearing the challenge. |

These denominators describe this selected batch, not forecast reliability for the other 84 names.

## Which scripts and briefs

The literal `*_harvest_session.py` files acquire authenticated browser sessions. Their companion `*_rest_fetch.py` files consume those sessions and pull publication data. The existing briefs explain that two-stage workflow:

- [Seeking Alpha auth brief](SEEKING_ALPHA_AUTOMATED_AUTH_MECHANISM_20260911.md): `sa_harvest_session.py` and `sa_rest_fetch.py`.
- [FT auth brief](FT_AUTOMATED_AUTH_MECHANISM_20260911.md): `ft_harvest_session.py` and `ft_rest_fetch.py`.
- [Bloomberg auth brief](BLOOMBERG_AUTOMATED_AUTH_MECHANISM_20260911.md): `bloomberg_harvest_session.py` and `bloomberg_rest_fetch.py`.
- [WSJ access brief](WSJ_DATA_ACCESS_MECHANISM_20260911.md): `wsj_rest_fetch.py`, using the documented Web Unlocker path; no parked WSJ login.
- [Endpoint reference](NEWS_PLATFORM_ENDPOINT_REFERENCE_20260911.md) and [backfill plan, including dated corrections](HARVEST_BACKFILL_PLAN_20260911_Z.md).

SA and FT consumed existing parked sessions; their browser session harvesters were inspected, not rerun. Bloomberg's browser harvester was exercised after its consumer failed, using a byte-identical runtime copy so any browser artifacts stayed local. It used `--max-steps 8`, without `--park`; its default RTX control query was outside the five-name batch. An internal network-auth flag became true, but the bot wall remained and no successful session bundle was produced. That flag is not a successful harvest.

Local execution still used the clients' existing remote Secrets Manager reads and proxy/Unlocker services. The collection worker and all new data outputs ran/stayed on SiteZ; this was not native-IP-only collection.

## What the returned data actually looks like

### Seeking Alpha

The five inferred SA symbols in the universe resolved live to the intended companies. Separate content kinds must remain separate:

- **Report:** JSON attributes including report dates, `response_content`, and ratings. The report text is Markdown-like and had no HTML tags detected.
- **News:** JSON `data[]` with IDs, publication time, title, flags, and HTML `content`. The 25 visible bodies span 273-9,847 characters after DOM text extraction. This size range does not certify completeness.
- **Analysis listing:** ID, title, and publication time; two entries per security in this test.
- **Analysis article:** title, publication time, HTML content and paywall flags. Visible lengths were BA 230, COST 276, HD 225, INTU 274, VLO 310. All returned `is_paywalled=false` and `is_locked_pro=false` despite partial text. The cause remains undiagnosed.

The report and analysis helper functions were called unchanged. News used the existing `get_json` function with the news URL shape documented by the existing integration. No cloud-writing ingestion entry point was invoked.

### Financial Times: access and extraction fail differently

The client makes HTTP GET requests for **HTML**, then emits extracted JSON. A REST-style call does not make the upstream article JSON-native.

The `quote()` helper returns titles, URLs and byte counts for summary/profile pages; it does not return their article links. For the article test, the harness retrieved the same summary pages using the existing `get_html()` helper, selected actual FT-host teaser links in document order, then called the unchanged `article()` helper.

| Company-page association | Text inside fetched article-body element | Existing helper output |
|---|---:|---|
| BA | 6,938 characters / 32 paragraph elements | 21 characters: byline only |
| COST | No response within 70 seconds | Timeout |
| HD | 17,328 characters / 62 paragraph elements | 38 characters: byline only |
| INTU | No article-body element; page title is Subscribe to read | 29,438 characters of subscription-page/script/style text accepted as article text |
| VLO | 5,112 characters / 29 paragraph elements | 84 characters: byline only |

The article regex stops at nested closing divs near the byline. Its fallback strips tags from the whole page, including script/style contents, rather than rejecting a missing article body. These are directly observed extractor defects. The INTU-linked premium article also demonstrates that the current account check does not establish access to every content tier.

FT teaser membership establishes company-page provenance, not that the article is primarily about the security. Some selected headlines concern broader industries or other companies; relevance needs explicit treatment.

### WSJ

The company page's embedded state yields a feed with headline, provider, article ID, publication date, URL, and significance/subscriber fields where present. BA/COST/HD/INTU/VLO counts were **140/107/106/102/49**. Providers include other Dow Jones publications, so these are not 504 WSJ-only articles. The body sample followed only WSJ-host links attributed to The Wall Street Journal.

The first VLO quote call failed; the repeat returned after **92.41 seconds**, and its article request took **62.74 seconds**. Original failure text was not retained because the helper includes vendor response snippets in exceptions; its HTTP status is therefore unknown. The failure was not treated as an empty feed.

Article outputs span 6,103-8,478 characters, but every one contains CSS declarations. The all-paragraph regex admits style contents and other page material. A large `text_chars` value does not prove substantive article text, and the documented public-content route does not establish complete subscriber articles.

### Bloomberg

A successful account response did not translate into a successful security-data request. The first ticker response was blocked; the bounded browser refresh also failed. This batch therefore has **one blocked ticker attempt and four unattempted names**, not five measured failures or zero news results. The existing consumer also lacks an article-body verb, so resolving the session alone would not complete the backfill workflow.

## Harness corrections and evidence limits

Two errors were in the test harness, not the publication scripts:

1. The initial SA setup failed before any publication request because the harness did not unpack `build_session()`'s tuple. Corrected before the reported run.
2. The initial FT link regex truncated Investors Chronicle URLs to FT-looking content IDs, producing three artificial 404s. Corrected to preserve full hosts and select FT teaser anchors. Those attempts remain in local evidence but are excluded from the corrected five-article result above.

These were current-snapshot probes: five SA news records, two analysis entries and one analysis body per name; one selected FT/WSJ article per available company feed. There was no historical date-boundary traversal, deduplication/restart test, overnight session endurance test, or foreign/ADR identifier test. Body-container counts are diagnostics, not independent full-text certification.

## Local storage and next batch

Local raw artifacts, client-returned payloads, diagnostic HTML and summaries are under:

`.runtime/codex-seats/4.0.0_SA_CRO~W/harvest-live-batch-20260914/`

The adjacent `harvest_batch_probe.py`, `harvest_article_probe.py`, and `harvest_followup_probe.py` document the exact calls. The committed evidence contains metadata and hashes; raw fetched content and browser artifacts remain local.

For an eventual fill, retain the repository's separation between immutable raw responses and clean derived records. A consumer record needs publisher/article ID, canonical URL, title, publication/fetch times, associated security IDs, body text or ordered content blocks, source hash, extractor version, and an explicit `full / partial / metadata_only / blocked / unknown` status. HTML/CSS and page shells must not qualify as clean body text. Publisher plus article ID/URL should identify an article; company associations can be many-to-many.

**Recommended next work:** correct FT's body selection and missing-body rejection; correct WSJ's article scoping/style exclusion and bounded transport retries; diagnose SA analysis truncation; resolve Bloomberg access and establish a news/body route. Then rerun these same five securities to compare results, followed by another five that exercise non-US/ADR mappings. Only after clean extraction and resumable date/page coverage are measured should this become an ongoing SiteZ job. Existing Windows scheduled-task patterns provide a local scheduling precedent, but this run does not test unattended reliability.
