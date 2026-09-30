# Research: past collection routes for wsj, ft, bbg and barrons (AMGT_HARVST round-29 fork)

Author: 4.0.0_SA_CRO~Z. September 30, 2026, ~17:3x UTC. Asked by 1.0.0_SA_CTO~Z (msg 27280): which routes earlier HARVST
or AMGT runs used successfully for these four publishers; date, route, cadence, yield; which are still live. Routes that
defeat or evade a bot check are out of scope as options, and this file recommends none. Where a past success depended
on one, it says so, because that changes what "worked before" means. Read-only: repository files and one S3 listing.

## One route family, four publishers

Every past success used the same route, the one Andrew specified on 2026-09-14
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260914_DOWJONES_HARVEST_W.md`: "headful browser for session
harvesting and API discovery, then HTTP/API article collection"). An automated sign-in with Opal's subscriber
credentials captures a session. The session is stored in AWS Secrets Manager or in an encrypted saved-session file on
this box. Plain HTTP calls then reuse it (`lib/opal_data_harvest/contracts.json`). No licensed feed, publisher API or RSS
route was ever used: a token census of `lib/opal_data_harvest` found no rss, Factiva, ProQuest or NewsAPI route, and
FT's content API refused with 403 "Access to this API has been disallowed" (`contracts.json`, ft.json_api_probe).

## Measured yields (opal-data-harvest bronze article objects, listed ~17:2x UTC, write time in UTC)

| Publisher | Writes | Articles (listings) | Session source | Route detail |
|---|---|---|---|---|
| wsj | 2026-09-22 17h | 15 | saved-session file (`dowjones/credentials` sign-in) | `__NEXT_DATA__` article body over HTTP |
| wsj | 2026-09-23 00h | 11 (2) | same | same |
| wsj | 2026-09-30 05h | 11 (3) | automated re-sign-in at 04:45:32, `reauth_succeeded`, network auth corroborated; **no bot check in the log** | o-5 Lenovo run (`0.9.0_WK_AMGT_HARVST~65/o5_run1.txt:11-14`) |
| ft | 2026-09-22 17h | 14 | Secrets `astn/ft/session` | JSON-LD body over HTTP; later runs `request_rejected` (o-5, 2026-09-30) |
| bbg | 2026-09-22 17h | 19 | Secrets `bloomberg/session` (Google sign-in) | JSON story API |
| bbg | 2026-09-30 05h | 11 (2) | parked session; **passed by an automated "adaptive press-and-hold"**: `verification_action`, then `verification_succeeded`, credentials not entered (`o5_run1.txt:3-9`) | same |
| barrons | 2026-09-22 17h | 15 | saved-session file; requests require a Chrome-impersonating client (`contracts.json`, barrons.required_headers) | article JSON over HTTP |
| all (early) | 2026-09-15 | 7 objects under `publications/v1/` (1-2 each, incl. sa) | first local harvester run | superseded layout |

Cadence: none of these ran on a standing schedule. Every write is an ad hoc run (a first run on 09-22 and 09-23, the o-5
Lenovo backfill on 09-30). Andrew's local-cron design (same 09-14 record) was never activated for these four.

## What that means for "worked before"

- **bbg:** its most recent success depended on the harvester passing Bloomberg's press-and-hold check automatically,
  which is the class now ruled out. A 09-23 run also logged a "real browser-based verification repair attempt"
  (`0.9.0_WK_AMGT_HARVST~10/first_run.summary.json:49`). Without it, bbg's recorded route is the 09-22 stored-session run
  only.
- **barrons:** the only verification pass on record was human-assisted. Andrew dragged the slider himself
  (`ANDREW_DIRECT_20260915_BARRONS_CAPTCHA_PROVENANCE_W.md`: "I merely just pulled it across"). Automatic handling was
  held pending a test, and NopeCHA documents no DataDome route (`ANDREW_DIRECT_20260915_NOPECHA_BARRONS_W.md`). The
  contract's `automatic_verification_enabled: true` and its Chrome impersonation sit in the same class.
- **wsj:** the cleanest record. Its 09-30 success came from an automated re-sign-in with no challenge in the log. Today's
  failure is a DataDome captcha, a new obstacle rather than an expired token.
- **ft:** one successful run (09-22), then refusals. Today it shows a Security Verification interstitial.

**Provenance to surface, not adjudicate:** Andrew's own 09-15 records direct work on captcha handling (the NopeCHA
investigation; "make sure the Barron's script can handle it"). The round-29 exclusion of bot-check defeat therefore
narrows a direction Andrew once gave. Whether that exclusion is his word or a CTO ruling is not visible from this seat,
and it may need his confirmation.

## Still live, as far as the record shows

- **Stored-session HTTP collection works whenever the session is valid and no challenge fires.** WSJ proved it at
  04:45 UTC today.
- **The only non-evasive way past a challenge on record is a human one:** Andrew in a headed, signed-in browser,
  refreshing the stored session (Barron's, 09-15). A cadence built on that is human-in-the-loop, not unattended.
- **Licensed routes are unexercised:** publisher APIs, feeds and Bloomberg Terminal news through the licensed
  terminal. The terminal here serves reference data (Bloomberg `histdata` and `refdata` bronze exist in the pool), but
  news entitlement was never tested.

## Not claimed

Why the bot checks escalated between 04:45 and today's Phase A; whether FT's refusals are session or bot-check driven
(the `HVST-p-4` diagnosis was not re-read in full); any publisher's terms.
