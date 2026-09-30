# HARVST bot-operations playbook: the steps for 2.0.0_SA_COO~H

Author: 4.0.0_SA_CRO~Z. September 30, 2026, ~19:5x UTC. Andrew-direct: *"We want to get as much information as posisble on
how to sort this out so all COO~H has to do is go through the motions"*. His target shape: *"a cronjob process on
sitez box ... very slow paced and natural. like one request per minute ... 5a-8a ET ... hits every single ticker on
every single publisher ... if it has to rerun logins ... or do a challenge then we gotta run the challenge"* (the
local-job words are verbatim in `HARVST_CLOUD_COLLECTION_DESIGN_20260930.md`). Evidence: `HARVST_BOT_OPS_STUDY_20260930.md`
(ledger study plus live trials 1-3); scripts in `scripts/harvest_botops_trial*.py`; logs in
`.runtime/harvest-botops-trial-20260930/`.

## What the trials established (2026-09-30, this box's own IP)

| # | Finding | Evidence |
|---|---|---|
| 1 | Request volume is not the cause: the harvester already paces ~20 s | ledger: at most 4-5 requests a minute per publisher |
| 2 | Cold starts on stale trust cookies trigger challenges | 11/16 bbg and 3/3 ft rejections were first requests after long idle; `_px3` lives ~5 min |
| 3 | A real-browser warm-up loads every homepage unchallenged and mints fresh trust cookies | trial 1, 18:10 UTC, all four |
| 4 | **FT is solved by the warm-up**; its REST client then passes for 12+ minutes | trial 1: search 200 (26 hits), article 200, +6 and +12 min 200 |
| 5 | bbg (PerimeterX), wsj and barrons (DataDome) refuse the outside REST client even with seconds-old cookies | trial 1 |
| 6 | **Every refused automated request degrades the IP.** After the refusals, the browser session was challenged on reload (+12 min), bbg reset connections, and within ~90 min a fresh anonymous browser was challenged on the bbg and wsj homepages | trial 1 +12 min; trials 2, 3 and 3b |
| 7 | The flag is on the IP, not on the cookies or the login | trial 3: stripped bot cookies still challenged; trial 3b: no cookies at all still challenged |

**Not yet established** (the IP was already flagged when tested): whether bbg, wsj and barrons accept REST calls issued
**from inside** a warm browser tab when the IP is clean. That is step 1 below.

## The steps

**0. Protect the IP (always).**
- Never send bbg, wsj or barrons a request from an outside HTTP client. Only FT, which uses Cloudflare only, takes the
  curl client.
- At the first challenge or 401/403 from a publisher, stop that publisher for the day. No retries, no cooldown loops
  (the 09-27 pattern retried every 16 minutes into the challenge).
- Do not run ad hoc collection or tests against these three from this box outside the job window.

**1. First-light trial (once, before the job goes live), 05:00 ET, before any other traffic from the box:**
- (a) one anonymous homepage load per publisher: challenged means the IP has not recovered, so stop and record.
- (b) warm-up with the stored session in headed Chrome (homepage, 20 s).
- (c) one search issued from inside the tab (`fetch`, `credentials:'include'`), then one article the same way.

Use `scripts/harvest_botops_trial3.py` for (a) and (b) as the starting point, adding (c) from
`harvest_botops_trial2.py` arm A. The result decides the collection method per publisher:
- in-tab REST passes: collect through the tab (step 3a);
- in-tab REST fails but navigation passes: parse the rendered page (step 3b);
- both fail on a clean IP: a different egress is needed. Andrew approved the Bright Data residential IP on an EC2 box.

**2. Daily job shape (Andrew's):** a scheduled task on the site Z box, 05:00-08:00 ET, one request per minute per
publisher. The job:
- runs the publishers in parallel lanes;
- has one headed Chrome context per publisher, kept open for the whole window so the site's own scripts keep the trust
  cookies fresh;
- runs a warm-up page load at the start of each lane and after any idle over ~4 minutes, inside the ~5-minute
  PerimeterX window.

**3. Collection per publisher:**
- ft: the warm-up, then the existing REST shapes (`lib/opal_data_harvest/publishers.py`, curl client) from the same box.
- bbg, wsj, barrons, per step 1's result:
  - (3a) the same REST shapes issued from inside the warm tab;
  - (3b) navigation to the search and article pages in the tab, parsing the embedded JSON the contracts already
    name (wsj `__NEXT_DATA__`, barrons article JSON, bbg story JSON).
- Ramp each lane gently: homepage, then one article, then search. Search is the most protected endpoint.

**4. Sessions:**
- Keep login cookies (bbg's are valid to 2027-09-11).
- Do not rely on replaying stored bot-manager cookies (`_px*`, `datadome`, `cf_clearance`, `__cf_bm`); the open browser
  refreshes them.
- On a verified logout or login redirect, re-sign-in with the existing harvesters
  (`org/tier1_exec/4.0.0_SA_CRO/scripts/*_harvest_session.py`).

**5. Challenges (Andrew: "we gotta run the challenge"):**
- The challenge path is the existing repair route (`lib/opal_data_harvest/verification.py`).
- Andrew's own words recorded earlier are the authority for automating it. This playbook adds no solver.
- Run it at most once per publisher per day. If it does not clear, stop that publisher for the day (step 0).

**6. Observability:**
- Every request, warm-up and challenge is written to the existing event ledger
  (`.runtime/opal-data-harvest/events.jsonl`).
- The first-light probe result is recorded each morning, so IP health is a measured daily series.

## Side effect to know about

The flag sits on this box's public IP, which may be the office's shared connection. A person browsing bbg, wsj or
barrons from the same network may see these challenges until the reputation recovers.
