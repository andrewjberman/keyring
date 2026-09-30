# HARVST production cloud collection: findings and proposed design

Author: 4.0.0_SA_CRO~Z. September 30, 2026, ~18:0x UTC. Task: Andrew-direct ~17:2xZ, routed whole to this seat
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_172xZ_HARVST_CLOUD_HEADFUL_NOPECHA_REST_API_LONG_LIVED_TOKENS_TO_CRO.md`).
Research and design only; nothing built, started or changed.

## 1. Can NopeCHA be the all-in-one captcha solution? No.

The challenge each publisher actually served is compared with NopeCHA's own documentation (developers.nopecha.com/captcha
and nopecha.com/api-reference, read 2026-09-30).

| Publisher | Challenge observed | NopeCHA |
|---|---|---|
| wsj, barrons (Dow Jones) | DataDome captcha / slider (today's Phase A; `ANDREW_DIRECT_20260915_NOPECHA_BARRONS_W.md`) | **Not supported** |
| bbg | PerimeterX/HUMAN press-and-hold (`0.9.0_WK_AMGT_HARVST~65/o5_run1.txt:3-6`) | **Not supported** |
| ft | "Security Verification" interstitial today; hCaptcha at login (`tools/astn_wsjft/ARCHITECTURE.md`) | hCaptcha and Cloudflare Turnstile **supported** (token API); Cloudflare's managed challenge **not supported** |

NopeCHA documents reCAPTCHA v2/v3, hCaptcha, Cloudflare Turnstile, FunCAPTCHA, GeeTest, AWS WAF, Lemin and text
captchas. Opal's NopeCHA account is live (Starter, measured 2026-09-15). It can serve FT's login captcha at most. The
repository already solves that one another way (Kimi-VL in `tools/astn_wsjft/scripts/harvest_ft_session.js`).

## 2. Why the jobs keep hitting pages at all: two separate mechanisms

1. **Sign-in expiry.** When a stored token lapses, the harvester re-signs in through the login page, and login pages
   carry captchas. Long-lived tokens fix this. Measured from the stored bundles (cookie names and expiry only):
   - **bbg** already has one: session captured 2026-09-11, `session_id`, `session_key` and `_user-token` valid to
     **2027-09-11** (345 days left).
   - **ft**'s bundle (`astn/ft/session`, last changed 2026-09-10) is stored without expiry data.
   - **wsj and barrons** have no Secrets bundle at all. Their tokens live only in an encrypted file on this Windows box,
     so no cloud host can use them today, and wsj needed a re-sign-in at 04:45 UTC today.
2. **Bot scoring on the API calls themselves.** This is independent of the token. bbg's press-and-hold fired at
   04:40 UTC today **with the year-valid token and no credentials entered**: the REST request itself was challenged.
   Scoring follows the client (IP reputation, TLS fingerprint, request rate), so a long-lived token is necessary but not
   sufficient. Moving the pulls to a plain EC2 address would likely score worse, because data-centre IPs are the least
   trusted class.

So Andrew's model is right (long-lived tokens plus REST shapes, with no crawler), and it needs one more piece: an egress
the publishers' bot scoring accepts.

## 3. What already works in Opal's cloud (prior art, measured)

- **ASTN_WSJFT, the CEO's daily WSJ/FT brief:**
  - **How it runs:** EventBridge at 3 AM ET, then an orchestrator Lambda, which starts a transient EC2 box
    (`astn-wsjft-scraper`, t3.medium, last launched 2026-09-30 07:00 UTC), runs the fetch over SSM, then always stops
    the box.
  - **WSJ:** fetched through **Bright Data Web Unlocker**, with no sign-in.
  - **FT:** fetched through Opal's own Chromium on a parked session, a residential proxy and stealth settings, from the
    same egress as the sign-in.
  - **Yield** (`s3://opal-data-astn/raw/`, which keeps 14 days, read ~17:5x UTC): WSJ every day from 2026-09-15 to
    2026-09-30, **12-18 articles a day, today included**; FT on 09-24 (18) and 09-26 (7) only. This is the one route
    that returned WSJ today.
- **Session-box pattern** (`infra/aws/terraform/investor-reporting/ycharts/`, `infra/aws/ec2/bd-49f-auto-login/`):
  Amazon Linux 2023 with Xvfb and Playwright, invoked through SSM. Credentials are read from Secrets by name, the fresh
  bundle is written back to Secrets, and an authenticated probe is the only success test. The YCharts box
  (`irpt-ycharts-runner`, t3.medium) is running now.
- **HARVST's own per-publication REST shapes** already exist (`lib/opal_data_harvest/contracts.json`,
  `publishers.py`): bbg JSON story API, wsj `__NEXT_DATA__`, barrons article JSON, ft JSON-LD.

## 4. Proposed production design (Andrew's shape, built from existing parts)

One small always-available or transient EC2 harvester host, the pattern ASTN and YCharts already run:

1. **Token keeper, per publication.** Each run probes the stored token with the publication's own `auth_check`
   (`contracts.json`). If valid, it goes straight to the REST pulls. If invalid, it re-signs in on the same host (Xvfb
   and Playwright, credentials from Secrets) and writes the bundle back to Secrets. **All four bundles live in Secrets**,
   including wsj and barrons, which leave the local encrypted file.
2. **REST pulls through the per-publication shapes**, on the same host and the same egress as the sign-in (the ASTN
   lesson on IP consistency). A pull moves to Lambda only where a measured probe shows the publication does not
   challenge that egress, which serves Andrew's "ideally entirely on a lambda" where it holds.
3. **Egress: one managed residential egress for all pulls.** Opal already holds a Bright Data account, used by ASTN and
   the Black Diamond boxes.
4. **Challenge handling by type:**
   - FT's login hCaptcha: NopeCHA's token API or the existing Kimi-VL solver.
   - DataDome (wsj, barrons), PerimeterX (bbg) and Cloudflare's managed challenge (ft): NopeCHA cannot serve them. The
     only proven cloud route is Bright Data Web Unlocker (WSJ daily in ASTN).
   - If a challenge fires and neither route clears it, the job parks with the publisher named. It never retries in a
     loop.
5. **Schedule:** EventBridge, then an orchestrator Lambda that starts, runs and stops the host (ASTN's orchestrator
   shape), paced per publication.
6. **Consolidation:** ASTN's box and the HARVST host do the same job for overlapping publishers (WSJ, FT). One host with
   one token store is the no-duplicate shape. ASTN's product (the CEO brief) keeps its own outputs.

## 5. Stated plainly: the risk in the challenge-passing piece

Unlockers, stealth browsers and captcha solvers get past controls the publishers put in front of their sites. Using
them on Opal's paid subscriber accounts risks those accounts being flagged or closed, and likely conflicts with the
publishers' terms. The durable answer is licensed access: Dow Jones Factiva or DNA for WSJ and Barron's, a licensed FT
content API (FT's API refused Opal's unlicensed call with 403), and Bloomberg news through a data licence. Each is a
spend decision for Andrew. The design above works today and matches what ASTN already does. The licensed routes remove
the challenge problem instead of fighting it.

## 6. Decisions this design needs from Andrew

1. **Egress:** a managed residential egress (Bright Data) as the standard for HARVST's REST pulls?
2. **DataDome and PerimeterX:** Bright Data Web Unlocker for wsj, barrons and bbg, since NopeCHA cannot solve them?
3. **One host:** consolidate ASTN's scraper and HARVST onto one harvester host and one token store?
4. **Licensed access:** request pricing for Factiva/DNA, FT's content API and Bloomberg news, to replace challenge-passing
   over time?

## Not claimed

FT's token lifetime (the bundle has no expiry data); whether any publication accepts REST pulls from a Lambda address
(unmeasured); Bright Data Web Unlocker's success rate on Barron's and bbg (only WSJ is proven, in ASTN); the cost of any
option.
