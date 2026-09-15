# Connect social discovery and SERP to the RESAPP header feed

Author: `4.0.0_SA_CRO~W`. 2026-09-15 06:21 UTC.
Authority: Andrew's scoped progress/gap review at `76ab87a06e`.
Recipient: `1.0.0_SA_CTO~W`; suggested scope for the next COO cut.

## Gap

The original social plan starts with an X cashtag search, but its module has
no HTTP client and no measured query contract. The current official vendor
documentation distinguishes discovery by profile from discovery by keyword.
The S13 cut should select an actual supported input method before treating
a dataset ID as a callable cashtag search.

Local evidence: `lib/research/social/measure.py:155-218`,
`lib/research/social/schema.json`, `validator.py:77-94`,
`data/find/dualbiz/scripts/serp.py:245-286`, and prior-art audit `1906df40bd`.

## Documented routes, not live account tests

Official Bright Data documentation read 2026-09-15 06:19-06:21 UTC:

| Intended input | Documented selector and fields |
| --- | --- |
| X official-account posts | `/datasets/v3/scrape`, dataset `gd_lwxkxvnf1cynvib9co`, `type=discover_new`, `discover_by=profiles_array`, profile `url` inputs. This finds posts from selected profiles, not the broader cashtag conversation. |
| Reddit discussion search | `/datasets/v3/scrape`, dataset `gd_lvz8ah06191smkebj4`, `type=discover_new`, `discover_by=keyword`, inputs `keyword`, `date`, `num_of_posts`. A bounded `num_of_posts` is necessary; omission is documented as all matches. |
| Asynchronous collection | `/datasets/v3/trigger` is the generic asynchronous request route. Persist the returned job/snapshot identity and retrieve that result through the documented delivery flow; do not resubmit discovery on every polling cycle. |

Sources:

- https://docs.brightdata.com/api-reference/scrapers/social-media-apis/twitter-posts-discover-by-profiles-array
- https://docs.brightdata.com/api-reference/scrapers/social-media-apis/reddit-posts-discover-by-keyword
- https://docs.brightdata.com/api-reference/rest-api/scraper/asynchronous-requests
- https://docs.brightdata.com/api-reference/scrapers/social-media-apis/overview

The X endpoint inventory reviewed lists URL/profile/username methods, not a
keyword-post discovery method. This is a documented capability boundary,
not proof that an undocumented/private route cannot exist. Account access,
actual delivery schema, cost, latency, recency and cashtag relevance remain
to be measured. No vendor extraction was submitted by this audit.

## Proposed connection shape

1. **One canonical identity input:** use the identity crosswalk requested in
   `RESAPP_CONNECTION_BRIEF_IDENTITY_20260915_W.md@b90bfdd20d`. Corporate
   account URLs come from the existing map with their evidence status;
   broad discussion uses company-qualified search and an aboutness check.
2. **Persist the collection job:** source, dataset/input method, exact query
   and time window, result cap, start/end time, returned job ID, completion
   status and cost evidence. Poll/resume a submitted job rather than turning
   retries into additional paid jobs. A submission timeout with unknown
   outcome is distinct from a confirmed failed job.
3. **Raw before derived:** store the returned structured records and a
   sanitized retrieval receipt, then normalize social posts with stable
   `platform:post_id` identities and separate security associations. Do not
   insert Reddit or X values into the publication v1 schema's five-publisher
   enum or pretend a short social post is a 120-word article.
4. **Two separate judgments:** whether the account is the company's own
   official account, and whether the post discusses this security. The
   current validator conflates these: an unresolved official-account status
   blocks attachment even for a relevant third-party discussion. Separate
   those fields/rules and retain the original post's author and URL.
5. **One header response, typed items:** merge admitted publication and
   social references for display, retaining source kind, stable identity,
   posted/publication time, retrieval time, provenance and qualification.
   Keep scheduled collection separate from a page read.
6. **Chatter has a named instrument:** retain publisher counts, social post
   counts and SERP samples separately before choosing any composite. A
   capped SERP page count or a failed search is not total daily mentions.
   A change of query engine/window/cap needs a method version so historical
   comparisons do not silently mix unlike observations.

## Bounded acceptance for S13's first real measurement

- One security, one declared supported method, a stated result cap and
  time window; measure actual delivery, quality, latency and cost.
- Positive relevant post plus an ambiguous ticker/unrelated post control;
  the latter must not become an admitted company item merely from a match.
- A relevant non-official author can appear as third-party discussion;
  an unverified corporate account is not displayed as confirmed official.
- Replaying a saved job result creates no duplicate item/association.
- Failure, zero matches, stale matches, capped results and still-running
  collection remain separate states in the input ledger and header.
- The normalized schema and reader are added to the shared harvest library
  archive with reproducible package/readback evidence after implementation.

The current session's vendor-egress authorization exists; the old plan's
permission explanation does not supply the missing client. These checks
can establish a usable feed contract without enabling a recurring sweep of
89 securities. Production cadence remains Andrew's decision.

Push state: LOCAL. This brief is design work, not a live-feed claim.
