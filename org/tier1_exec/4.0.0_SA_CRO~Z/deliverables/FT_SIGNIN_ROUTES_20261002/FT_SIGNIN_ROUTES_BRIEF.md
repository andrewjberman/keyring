# ft sign-in for AMGT_HARVST FWD-11: which routes work today -- research brief for the CTO's design fork


> **ANDREW-DIRECT 2026-10-03 ~17:3xZ (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261003_17xxZ_RELEASE_ALL_QUARANTINE_NO_DATA_OPS_CHANGES_WITHOUT_DIRECTIVE.md` @4d393e3521):**
> "We have permissions in place, it is inappropriate for agents to adjust our data engineering operations without my
> explicit directive. Release any quarantine that may have been initiated in any capacity."
> This file reads the publishers' CONSUMER terms. It does not account for the permissions Opal holds, which this seat did not
> see. It is research only: no agent changes data collection, storage or serving on the basis of it without Andrew's explicit
> directive.

**Author:** 4.0.0_SA_CRO~Z. **Asked by:** 1.0.0_SA_CTO~Z, msg 28696 (row Z-C-S62; round-37 analysis ruling 3). **Date:** 2026-10-02
~20:2xZ.
**Evidence:**
- `WEB_RESEARCH.md` beside this file: public web pages read 19:3x-20:1xZ, every row with its URL and a claim tag;
- `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_H/round37/ROUND37_DRAIN_END_PACKET.md` section 4 (the measured route
  census);
- `lib/opal_data_harvest/contracts.json` (the ft contract).

**Not done:** no account created, no form submitted, no vendor API called, no solver tested. Each of those is a vendor call that
needs Andrew's word.

## Answer

1. **Route (a), a captcha solver, is empty today on the vendors' own documents.**
   - None of 2Captcha, CapSolver, Anti-Captcha, CapMonster Cloud or NopeCHA lists hCaptcha in its current API documentation.
   - CapMonster says outright that hCaptcha "is currently not being solved" (`ERROR_TASK_NOT_SUPPORTED`).
   - Ocilar shows no public trace of hCaptcha.
   - So option (b) of row Z-C-S62, "another solver", has no documented candidate to card. Option (a), the 11-01 Ocilar
     re-check, rests on a vendor with no evidence of hCaptcha at all.
2. **The working route is a licence, not a technique.** An **FT corporate licence** carries four things:
   - SSO sign-in at Opal's own identity provider, re-authenticated every 180 days per the library guides, against today's
     24-75 minutes;
   - Premium content, which this account cannot read today;
   - FT full text inside the **Bloomberg Terminal**, which Opal already holds;
   - access to FT's **Datamining API**, which exists for retrieving and hosting FT articles on the licensee's own servers. This
     is the one route where FT itself permits automated collection.
   It is Andrew's money call, and the price is not published.
3. **Until then, option (c), accept ft at its depth (3 of 89 pairs, 62 stored), is the honest interim.** Every other option
   either waits on nothing or buys nothing.

## The route census

| # | route | how it was measured | status today | cost | external vendor? |
|---|---|---|---|---|---|
| M1 | NopeCHA Token API | HARVST round 37, live call | discontinued (error 19), Z-W92-S18. Its docs now list only Turnstile and reCAPTCHA (WEB a5). | plan $4.99-99.99/month | yes; VEW-1 whitelisted |
| M2 | NopeCHA hCaptcha recognition | HARVST round 37, live call | 400 "outdated format", Z-S66. No NopeCHA product lists hCaptcha (WEB a5). | same | yes; VEW-1 |
| M3 | NopeCHA browser extension | HARVST round 37, in the ft profile | did not clear in 150 s, Z-W90-S21. The extension's docs do not list hCaptcha (WEB a5). | same | yes; VEW-1 |
| M4 | Ocilar | HARVST round 37, live call (Andrew's per-use word) | 503, hCaptcha "coming", Z-W92-S19. The only public trace is a Mexico-government captcha SDK (WEB a6). | not found | yes; not listed |
| M5 | Hand-solved session + keep-alive | HARVST rounds 35-37 | dies at 24 min (aj-4) and 75 min (ai-2), Z-W92-S20. `FTSession_s` is server-held and never re-issued (`contracts.json` ft.session_lifetime). | staff time | no |
| W1 | 2Captcha | read of its current API docs | hCaptcha absent from 42 listed types (WEB a1) | n/a | yes |
| W2 | CapSolver | read of its current docs | hCaptcha absent; the old hCaptcha doc URL returns 404 (WEB a2) | n/a | yes |
| W3 | Anti-Captcha | read of its current apidoc | hCaptcha absent (WEB a3) | n/a | yes |
| W4 | CapMonster Cloud | its client package doc, July 2026 | hCaptcha "not being solved", explicitly (WEB a4) | n/a | yes |
| W5 | Bright Data Web Unlocker | its feature docs | "solves CAPTCHAs" with no types named. Opal already holds a Bright Data residential secret, whose site-Z use is held for Andrew's word (WEB a7). | priced per 1,000 requests | yes |
| W6 | Self-hosted open-source solvers (`hcaptcha-challenger`) | public repos | claims, unverified | compute | no vendor, but it is code that solves the challenge, under the same hCaptcha terms (below) |
| L1 | **FT corporate licence + SSO** | library guides quoting FT (WEB b1) | SSO since 2020; re-authenticate every 180 days. **Not established:** whether FT's interstitial still fires on automated reads after SSO. | negotiated; FT Professional prices by engaged readers | FT itself, a licence |
| L2 | IP-range authentication | one institution's report (WEB b2) | FT has granted it on a negotiated licence | negotiated | FT itself |
| L3 | **FT Datamining API** | press and API lists (WEB c1); developer.ft.com refused the fetch | the licensed route to retrieve and host FT articles; needs an FT subscription and a key. Our 09-22 403 was keyless. | licence; not published | FT itself |
| L4 | **Bloomberg Terminal** | 2010 announcement (WEB c2) | FT full text for FT corporate-licence holders; headlines only otherwise. The site-Z Terminal's news entitlement has never been tested. | the licence; the Terminal is already held | Bloomberg, already held |
| L5 | Factiva, Nexis, ProQuest | library guides (WEB c3-c5) | FT full text behind a **30-day embargo**, lifted only for academic licences | subscription | yes |
| L6 | Sign in with Google/Apple | screens captured 2026-01 (WEB b3) | moves the password step off FT. The FT-side check can still fire (inferred). | none | identity only |

## Why the solver class is closing, not just unlisted

- **Takedowns:** a 2026 blog and a weaker forum report that hCaptcha sent cease-and-desist letters to solver vendors in late 2024,
  and that NopeCHA pulled support. That fits W1-W4 and M1-M3 exactly, so the absence is not a documentation lag. INFERRED.
- **hCaptcha's own terms** (updated 2025-11-17) bind "all users of the Services". They prohibit tasks done "with the use of
  Internet bots ... scripts, or any other form of artificial intelligence" (s.7) and AI completing any task that "requires human
  intelligence" (s.2).
- **hCaptcha Enterprise has "Passive" modes driven by a risk score,** so FT's interstitial can fire with no puzzle for a solver to
  attack. INFERRED from the feature list. It also fits M3 timing out.

## Two things the CTO should see before ruling

1. **FT's terms on automated access are unread.** `help.ft.com` refused the research tool.
   - What is on record: FT's public-policy chief calls AI scraping "a breach of UK copyright law" (Press Gazette, 2025-02-05).
     Library guides quote "commercial use is not permitted" for an academic licence, and peer publishers bar robots outright.
   - **This bears on the ft limb as built (automated reads on a consumer subscription), not only on the solver question.**
   - The verbatim read needs a headed browser on an Opal machine at `help.ft.com/legal-privacy/terms-and-conditions/` and
     `/copyright-policy/`. It is one read, and the CTO can assign it.
2. **NopeCHA's renewal on 10-31** (round-37 packet 6.6) buys nothing for ft: no NopeCHA product lists hCaptcha. Whether it still
   serves bbg (Turnstile or reCAPTCHA) is that limb's question, not this one's.

## Recommendation (the CTO rules; Andrew words the money)

- **Rule (c) now:** ft at its depth (62 stored), STOP_FT kept. That ends the BLOCKING class on a measured fact rather than a wait.
- **Card ONE item for Andrew:** an FT corporate licence quote that names the Datamining API and FT-on-Bloomberg. The licence makes
  limb (1) a credentialed key or SSO instead of a challenge, and lifts the Premium coverage limit.
- **One free check, no vendor:** does the held Bloomberg Terminal show FT headlines today, which is the no-licence state? That
  says whether Opal holds a licence nobody has wired. The `integrations/bloomberg/READ_HERE.md` budget rules apply. The owner is
  the CTO's pick.
- **Do not card another solver.** None documents hCaptcha today, and a test of one is itself a vendor call.

## Not claimed

- Any FT price.
- That SSO or IP authentication removes the interstitial for automated reads: no source states it.
- The FTSession cookie's documented lifetime.
- Whether Opal already holds any FT licence beyond this subscriber account.
- Forum claims that some vendor solves hCaptcha off-docs (untested by design).
- LSEG Workspace carriage of FT.
