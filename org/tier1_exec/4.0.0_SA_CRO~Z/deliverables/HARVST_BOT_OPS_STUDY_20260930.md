# HARVST bot-operations study: why the publishers challenge us

Author: 4.0.0_SA_CRO~Z. September 30, 2026, ~18:1x UTC. Andrew-direct (verbatim in
`HARVST_CLOUD_COLLECTION_DESIGN_20260930.md`, "Andrew's answers"): *"we just need better bot ops, we have passed these
before, i think the issue needs to be studied. I.e., are we having problems because were making 100 requests a second,
in other words, are we trying to do too much out the gate?"* Local evidence only: the harvester's event ledger
(`.runtime/opal-data-harvest/events.jsonl`, 560 events, 2026-09-15 to 2026-09-30, of which 296 are per-request `http`
records with timestamps and statuses) and the stored `bloomberg/session` bundle (cookie names and expiry only; no value
printed). Output: `.runtime/opal-data-harvest-rate-study.txt`.

## Answer: volume is not the cause. Cold starts on stale bot-trust cookies are.

### 1. The request rate is already low

| Publisher | Requests (15 days) | Days active | Most in any 60 s | Most in any 10 min | Median gap |
|---|---:|---:|---:|---:|---:|
| bbg | 102 | 5 | 5 | 27 | 21.7 s |
| sa | 61 | 5 | 4 | 31 | 20.0 s |
| wsj | 59 | 3 | 4 | 19 | 21.8 s |
| barrons | 52 | 3 | 4 | 17 | 20.9 s |
| ft | 22 | 3 | 4 | 13 | 20.3 s |

The pacing never approaches 100 a second. It holds near one request every 20 seconds.

### 2. Failures come at the start, not after a burst

Of 26 rejections (401 or 403), the ones on the Bloomberg and FT search endpoints are almost all the first request of a
session after hours or days of silence:
- **bbg:** 11 of 16 had no request in the prior 10 minutes. Gaps before them ran from 16 minutes to 7.8 days.
- **ft:** 3 of 3 were first requests, after gaps of 12 hours to 7.9 days.
- **wsj and barrons:** their 401s land on `/search` as the 2nd or 3rd request of a session.

Successes sit inside warm sessions. Requests in the prior 10 minutes, same publisher:

| Publisher | Successes (median / max) | Failures (median / max) |
|---|---|---|
| bbg | 8 / 26 | 0 / 14 |
| ft | 8 / 12 | 0 / 0 |
| wsj | 8 / 18 | 1 / 1 |
| barrons | 4 / 16 | 1.5 / 4 |

Failures had **less** recent traffic than successes. That is the opposite of a rate problem.

### 3. The mechanism, measured on Bloomberg

The stored `bloomberg/session` bundle (captured 2026-09-11 05:13 UTC) mixes two kinds of cookie:
- **Login:** `session_id`, `session_key` and `_user-token` expire **2027-09-11** (345 days left).
- **PerimeterX bot-trust:** `_px3`, `_px2` and `_pxde` expired **2026-09-11 05:17-05:18 UTC, about four minutes after
  capture**. The site's own sensor script, running in a real page, re-issues them.

Every cold REST call since 09-11 has therefore carried a valid login and an expired trust token, and PerimeterX answers
that with press-and-hold. Calls inside a session opened by a real browser minutes earlier carried fresh trust tokens,
which is how "we have passed these before": the 09-22 17:xx UTC runs, for example, followed browser work. DataDome
(wsj, barrons) works the same way with its `datadome` cookie. Those bundles are encrypted locally and were not opened
for this study, so for them this is inferred, not measured.

### 4. Two habits that make it worse

- **Retrying into a challenge.** On 2026-09-27 bbg was retried every ~16 minutes (gaps 960-967 s) from 21:40 to 23:02
  UTC, six challenges in a row, each on the same stale bundle. Repeated challenged hits teach the bot manager that this
  client is a bot.
- **The first request is the most protected endpoint.** Jobs open cold on the search APIs (`/nemo-next/api/search/query`,
  `/search`), where almost every failure lands. Article endpoints inside a warm session succeed.

## What better bot operations looks like (no captcha solving, no unlocker)

1. **Warm the session before the pulls.** Each run opens the publisher in a real browser on the same egress, loads an
   ordinary page and lets the site's own scripts run, which refreshes the trust cookies. It then hands the fresh cookies
   to the REST pulls within the trust window (minutes for PerimeterX). This is ordinary browsing, not a challenge solver.
2. **Keep the session warm while pulling.** Pull while the trust cookies are fresh, and re-warm when they near expiry
   instead of letting a REST call present a stale one.
3. **Stop at the first challenge.** A challenge parks that publisher until the next warm-up. No fixed-interval retries
   into it.
4. **Ramp gently.** Open with a page load, then an article read, and only then search, keeping the ~20 s pacing.
5. **One stable egress and client.** Warm-up and pulls come from the same IP and browser identity (the ASTN lesson on
   IP consistency). On the site Z box that is its own connection. On EC2 it would be the Bright Data residential IP
   (Andrew, answer 1).

## Fit with Andrew's direction

A local job on the site Z box ("perpetually on, and a local device ... local has more visibility ... Maybe its a local job
until it matures in process") suits this. The box has the browser, the stored sessions and the event ledger that made
this study possible. The warm-up step is where the headful browser belongs. The REST shapes stay as they are.

## Not claimed

That warming alone clears every challenge: FT's interstitial and the Dow Jones 401s (which may be login expiry rather
than DataDome) are not separated here. The DataDome cookie lifetimes are not measured. No live test was run: the next
step is one bounded warm-then-pull trial per publisher, recorded in the same ledger.

## Live trial 1 (Andrew: "Yes do it"), 2026-09-30 18:10-18:23 UTC, this box's own connection

Script `scripts/harvest_botops_trial.py`, one process per publisher. Log `.runtime/harvest-botops-trial-20260930/<pub>.jsonl`
(statuses, signatures, hit counts, trust-cookie minutes-to-expiry; no article text, no cookie values). Steps: warm-up in
headed Google Chrome with the stored session, then REST with the production client (curl_cffi, Chrome impersonation) on
the warm cookies, re-tested at +6 and +12 minutes.

| Step | bbg | wsj | barrons | ft |
|---|---|---|---|---|
| Warm-up homepage in Chrome | loaded, **no challenge**; fresh `_px3` with **5.2 min** life | loaded, no challenge; fresh `datadome`, `cf_clearance` | loaded, no challenge; fresh `datadome` | loaded, no challenge |
| Auth check (REST) | 200 | 200 | 200 | (none defined) |
| Search (REST, warm cookies) | **403 PerimeterX** | **401 DataDome** | **401 DataDome** | **200, 26 hits** |
| Article (REST) | not reached | not reached | not reached | **200** |
| +6 min search, stale / live cookies | 403 / connection reset | 401 / 401 | 401 / 401 | 200 / 200 |
| +12 min: browser reload | **challenged (PerimeterX)** | **challenged (DataDome)** | **challenged (DataDome)** | no challenge; search 200 |

Findings:
1. **FT is fixed by the warm-up alone.** Its REST pulls pass for at least 12 minutes after one warm start, with stale or
   fresh cookies. FT uses only Cloudflare's `__cf_bm`.
2. **bbg, wsj and barrons recognise the outside client itself**, not just stale cookies. Seconds-old trust cookies did
   not help. The production client impersonates Chrome 146 on macOS while this trial sent the browser's Chrome 154
   Windows user agent. That mismatch is one candidate cause; trial 2 separates it.
3. **A refused outside call poisons the browser session behind it.** The same browser that loaded unchallenged at +0 was
   challenged on a plain reload at +12 minutes, after two or three refused REST calls. For bbg the next REST call had its
   TCP connection reset. Mixing a browser session with an outside client on these three publishers is worse than doing
   nothing, and retry loops (the 09-27 pattern) compound it.
4. The PerimeterX trust cookie (`_px3`) lives about 5 minutes and is re-minted by page activity (5.4 min after the
   +12 reload).

Trial 2 (`scripts/harvest_botops_trial2.py`) is scheduled after a 70-minute cool-down (~19:35 UTC) for bbg, wsj and
barrons. In one warm session it tests (A) REST calls issued from inside the tab, (C) a plain browser navigation to the
search page, and last (B) the outside client with a self-consistent identity.
