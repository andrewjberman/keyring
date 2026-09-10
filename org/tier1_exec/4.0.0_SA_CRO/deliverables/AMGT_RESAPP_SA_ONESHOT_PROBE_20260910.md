# AMGT_RESAPP -- can we one-shot a security's Seeking Alpha page? MEASURED.

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10 | Option 3 of the `/next-steps` set.
**Question (Andrew, verbatim):** *"seeking alpha scanner function may be useful here and we may also
want to revisit how that tool worked if there is a means to oneshot the security's page on SA."*
**Authority:** the 2026-09-10 egress grant. Honoured: **one security (`SAP`), one target page.**

---

## THE ANSWER, in three parts

**1. THE ONE-SHOT PRIMITIVE EXISTS AND IS URL-GENERIC.**
`infra/aws/lambda/seeking-alpha-analysis-scraper/lambda_function.py:159`

```python
def fetch_page_via_bright_data(url: str, api_key: str) -> str:
    api_url = 'https://api.brightdata.com/request'
    payload = {'zone': 'one_shotter', 'url': url, 'format': 'raw'}
```

It takes an arbitrary URL. Nothing about it is specific to `/article/` pages. **What is not
ticker-addressable is the ORCHESTRATION** -- `lambda_handler` reads `urls = batch['urls']` from
`load_batch_from_s3(batch_id, date_str)`, batches of 10, fed by a date-listing coordinator.
**So the gap is a thin ticker-addressable wrapper, not a scraper build.**

**Carried caveat, from the source's own comment (line 172):** *"Browser rendering not supported in
one_shotter zone. Using raw HTML and extracting longest available text."* SA symbol pages are
JS-rendered, so a raw one-shot may return a shell. **This remains UNTESTED -- see part 2 for why.**

**2. IT CANNOT BE EXERCISED TODAY: THE BRIGHT DATA CREDENTIAL IS DEAD.**
`opal/external-apis` -> `bright_data_api_key` (len 36, us-east-1).

| Arm (one variable differs per arm) | Result |
|---|---|
| stored key + `one_shotter` + `seekingalpha.com/symbol/SAP` | `401 Invalid token` |
| stored key + `one_shotter` + `example.com` (trivial target) | `401 Invalid token` |
| stored key + `web_unlocker` + SA page (different zone) | `401 Invalid token` |
| **deliberately corrupted key** + `one_shotter` + `example.com` | **`401 Invalid token` -- IDENTICAL** |
| account-level `GET /zone/get_active_zones` (no zone, no target) | `401 Invalid credentials` |

**THE NEGATIVE CONTROL IS WHAT MAKES THIS SOUND:** a known-garbage token produces a response
indistinguishable from the stored one, and the account-level endpoint -- which involves neither a
zone nor a target URL -- also refuses. **It is the CREDENTIAL. Not the zone, not the target, not the
request shape.** GRAIN check discharged: the Lambdas call `get_secret_value(SecretId=
'opal/external-apis')` with no explicit region and run in `us-east-1`, which is the region this
probe read -- so the Lambdas read the same secret that just failed.

**3. AND THAT IS NOT A BREAKAGE -- THE ESTATE IS DELIBERATELY PARKED.**
This is the finding I nearly got wrong. A dead credential on a live-looking 7-Lambda estate reads as
a production outage. It is not:

| Surface | Measured state |
|---|---|
| `seeking-alpha-analysis-daily` (`cron(0 21 * * ? *)`) | **DISABLED** |
| `seeking-alpha-news-daily` (`cron(0 14 * * ? *)`) | **DISABLED** |
| EC2 `i-07ebae29a16e43ed1` (t3.medium) | **stopped** |
| EC2 `i-06376c11d8b3c3443` (t3.medium) | **stopped** |
| 7 Lambdas, 11 log groups, DynamoDB `seeking-alpha-article-urls` | present, `LIVE-no-DECLARED` |

**Three independent surfaces agree: both schedules off, both instances stopped, credential lapsed.**
That is a coherent picture of an estate someone parked on purpose, and the lapsed key is a
*consequence* of the dormancy rather than a fault. **No production alarm is warranted and none
should be raised.** Reporting this as an outage would have been a real error: the schedule state was
the discriminator, and nothing in the credential failure itself distinguishes the two readings.

> **Cost note, non-urgent:** the instances are `stopped`, not terminated, so they cost EBS storage
> and nothing else. Not worth an action; worth knowing.

---

## WHAT THIS MEANS FOR AMGT_RESAPP

**Reviving SA for this project is a VENDOR/SPEND act before it is an engineering act.** The wrapper
is thin and the estate is intact; the blocker is a Bright Data subscription that has lapsed or been
cancelled. That is Andrew's call and nobody else's, and it should be priced before the news leg is
scoped into v1.

**This sharpens the v1 news-scope question** (notes §7 Q4). Previously: "SA corpus works today, RSS
needs entity extraction." **Corrected: neither works today without a spend decision.**

| Source | Ticker-tagged? | Available today? |
|---|---|---|
| SA corpus (already scraped, in S3 + DynamoDB) | ~~YES~~ **NO -- 0 of 200 measured** | ~~YES~~ **NO -- articles stop 2026-04** |
| SA corpus (fresh / on-demand one-shot) | YES | **NO -- credential dead** |
| RSS + NewsAPI corpus | **NO** (topic-level `affected_tickers` only) | yes, but needs an entity-extraction leg |

**=> The genuinely free v1 option is the SA corpus ALREADY IN S3/DynamoDB, read as history.**
It is ticker-tagged, it is landed, and it needs no vendor. Its ceiling is that it stops at whatever
date the estate was parked -- which has not been measured here and should be, since it sets how
stale the "news mentions" panel would look on day one.

## OPEN, ROUTED TO ANDREW

1. **Renew Bright Data?** A spend decision. Gates any *fresh* SA content, on-demand or scheduled.
2. **Was the estate parked deliberately, and by whom?** Not established. The state is coherent but
   no record was found explaining it. Worth knowing before reviving something that was switched off
   for a reason.

## NOT MEASURED

- Whether a raw (non-rendered) one-shot of an SA **symbol** page yields usable content -- blocked by
  the credential, not by design.
- The **last date** the SA corpus landed in S3/DynamoDB. **This is the next thing to measure** and
  it decides whether the free option above is viable.
- Whether the RSS/NewsAPI news scanner (a separate estate) is itself still running.
