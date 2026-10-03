# FT sign-in routes: hCaptcha solvers, challenge-free sign-in, licensed full text -- web research (DRAFT)

**Author:** the web-research fork of `4.0.0_SA_CRO~Z`. **Asked by:** `1.0.0_SA_CTO~Z` msg 28696 (AMGT_HARVST FWD-11 ft limb, row
Z-C-S62). **Read:** 2026-10-02, about 19:3x-20:1xZ.

**Method:**
- Public web pages only, through the harness's WebSearch and WebFetch.
- No account was created and no form was submitted. No vendor API was called and no solver was tested.
- `help.ft.com`, `www.ft.com`, `developer.ft.com` and `web.archive.org` refused this tool's fetch. FT's own pages are therefore
  cited through third parties: university library guides, press, and Wikipedia.

**Claim tags:**
- `vendor-claimed`: the vendor's own page, or a vendor's marketing.
- `vendor-docs`: the vendor's own current API documentation. This is the strongest evidence of what is offered TODAY.
- `independently-reported`: press, library guides, reviewers and forums. Forum posts are the weakest, and are marked as forums.
- `FT-documented`: FT's own text, quoted by a third party.
- `inferred`.

**"Vendor"** means an external party whose API or service Opal would call. Calling one needs Andrew's word, unless it is listed
in `org/ref/VENDOR_EGRESS_WHITELIST.yaml` (today that is NopeCHA only).

---

## (a) hCaptcha solver services -- current stated support

**Headline: as of 2026-10-02, none of the five major solver vendors' own API documentation lists hCaptcha.** Third-party blogs
from 2026 still claim hCaptcha Enterprise support for some of them. Their own docs say otherwise. A forum and a blog both report
that hCaptcha sent cease-and-desist letters to solver vendors in late 2024. hCaptcha's own terms prohibit automated solving by
any user of the service.

| # | service | hCaptcha listed today? | method | stated price /1,000 | stated success | jurisdiction | URL | read | tag | vendor |
|---|---|---|---|---|---|---|---|---|---|---|
| a1 | **2Captcha** | **NO.** The API docs list 42 types (reCAPTCHA v2/v3/Enterprise, Turnstile, DataDome, Arkose, GeeTest, Amazon and others). hCaptcha is absent, with no deprecation note. | human workers + AI | n/a for hCaptcha (a blog cites "~$2.99/1,000" for hCaptcha, unverified) | none stated | not established | https://2captcha.com/api-docs | 10-02 | vendor-docs | yes |
| a2 | **CapSolver** | **NO** in its current docs. The getting-started list is ImageToText, reCAPTCHA v2/v3, AWS WAF, VisionEngine, GeeTest, MTCaptcha, DataDome, Turnstile, Cloudflare Challenge and BotDeflector. hCaptcha and hCaptcha Enterprise are absent; the old hCaptcha doc URL returns 404. | AI token | n/a. Blogs claim "$0.80/1,000 hCaptcha" and "8-15 s for hCaptcha Enterprise" (pixelscan, 2026-04-24), which contradicts the vendor's own docs. | none in docs | not established | https://docs.capsolver.com/en/guide/getting-started/ ; https://pixelscan.net/blog/hcaptcha-bypass/ | 10-02 | vendor-docs (absent); the blog is independently-reported | yes |
| a3 | **Anti-Captcha** | **NO.** The apidoc lists reCAPTCHA (and Enterprise), FunCaptcha, GeeTest, Turnstile, Prosopo, Friendly Captcha, Amazon WAF, Altcha and image types. No hCaptcha task and no deprecation note. A blog (pixelscan, 2026-04) claims a "strong track record with hCaptcha Enterprise". | hybrid human + AI | n/a | none | not established | https://anti-captcha.com/apidoc | 10-02 | vendor-docs (absent) | yes |
| a4 | **CapMonster Cloud** (ZennoLab) | **NO, explicitly.** Its client package doc (July 2026) says hCaptcha "is currently **not** being solved by the service -- `createTask` with an `HCaptchaTask`/`HCaptchaTaskProxyless` payload is immediately rejected with `ERROR_TASK_NOT_SUPPORTED`". | AI | n/a | n/a | not established | https://packagist.org/packages/cap_monster/client | 10-02 | vendor-docs (client library) | yes |
| a5 | **NopeCHA** (VEW-1, whitelisted) | **NO.** The developers page lists the Recognition API (FunCAPTCHA, AWS WAF, GeeTest, Lemin, reCAPTCHA, text), the Token API (**Turnstile, reCAPTCHA v2/v3 only**) and the extension (reCAPTCHA, FunCAPTCHA, AWS WAF, Turnstile, text). hCaptcha appears in none. The extension's latest release is 0.6.2-rc.2 (Aug 2026). | AI | plans $4.99-$99.99/month | none | not established | https://developers.nopecha.com/captcha/ ; https://nopecha.com/pricing ; https://github.com/NopeCHALLC/nopecha-extension | 10-02 | vendor-docs | yes (whitelisted) |
| a6 | **Ocilar** | **NO evidence of hCaptcha.** The only public trace found is a PyPI SDK described (in search snippets) as solving the SAT Mexico and IMSS Mexico captchas. The PyPI page did not render. HARVST measured 503 today. | API | not found | none | not established (Mexico-focused, inferred) | https://pypi.org/project/ocilar/ | 10-02 | independently-reported (snippet) | yes |
| a7 | **Bright Data Web Unlocker / Browser API** | **Not stated.** The docs say Web Unlocker "solves CAPTCHAs" but list no types; pricing is per 1,000 successful requests (CPM), not per captcha. A blog (pixelscan, 2026-04) claims hCaptcha Enterprise at "3-15 s". **Opal already holds a Bright Data residential secret** (`astn/brightdata/residential-proxy`). Its use on site Z was held for Andrew's word. | managed unblocker (proxy + browser + solver) | CPM, not per captcha (blog: "per GB ~$2-5") | none in docs | US/Israel (inferred, not read) | https://docs.brightdata.com/scraping-automation/web-unlocker/features | 10-02 | vendor-docs (types not stated) | yes |
| a8 | **Self-hosted open source** (`hcaptcha-challenger`, `hcaptcha-solver`) | Claim to solve hCaptcha image challenges with vision models. | local model | compute only | none verified | n/a | https://sourceforge.net/projects/hcaptcha-challenger.mirror/ ; https://pypi.org/project/hcaptcha-solver | 10-02 | independently-reported | **no external vendor** (but it is code that solves the challenge) |

**The industry context, with its evidence grade:**
- **Takedowns.** "Many solvers have been hit with cease-and-desist takedowns for violating hCaptcha's terms" (olostep blog,
  2026-07-14, https://www.olostep.com/blog/hcaptcha-solver). Forum and Medium posts say most public hCaptcha Enterprise APIs got
  cease-and-desist letters in late 2024, "including NopeCHA and NextCaptcha which pulled support"
  (https://www.blackhatworld.com/seo/which-captcha-solvers-still-can-solve-h-captchas.1710056/). Both are
  `independently-reported`; the forum is weak. **It is consistent with a1-a5's vendor docs today, so the absence is not a doc
  lag.** INFERRED.
- **hCaptcha's terms** (last updated 2025-11-17, https://www.hcaptcha.com/terms; `vendor-docs` of the CAPTCHA owner) bind "all
  users of the Services". They prohibit performing "any task with the use of Internet bots, web robots, bots, scripts, or any
  other form of artificial intelligence" (s.7) and using "artificial intelligence to complete any portion of any task ... which
  requires human intelligence" (s.2).
- **hCaptcha Enterprise** offers "Passive" and "99.9% Passive" no-CAPTCHA modes and risk scores (https://docs.hcaptcha.com/faq).
  So FT's interstitial can fire on a risk score with no visible puzzle a solver could attack. INFERRED from the feature list.

---

## (b) FT sign-in paths that avoid the challenge

| # | route | what is documented | cost | URL | read | tag | vendor |
|---|---|---|---|---|---|---|---|
| b1 | **FT enterprise / corporate licence with SSO (SAML) sign-in** | Organisations' users click "SSO Sign In" and authenticate at their own identity provider, "without entering a separate FT username and password" (Newcastle, since Sept 2020). Users "need to log on to the SSO portal every 180 days" to keep access (Manchester/WUSTL guides, via search snippet; the Manchester page itself is behind its own SSO). FT Enterprise Tools (launched 2018) is the admin platform for enterprise-licence users. **The sign-in hop then happens at OPAL's identity provider, not on FT's challenged form.** Whether FT's Security Verification still fires on the session after SSO is NOT documented. | Corporate licence: 10+ users; "costs per subscription decreases as more are purchased" (2009). FT Professional now prices by **engaged readers** (ftstrategies, undated). No published price. | https://libhelp.ncl.ac.uk/faq/46479 ; https://guides.libraries.emory.edu/stay-connected/financial_times ; https://www.jinfo.com/go/sub/article/74643 ; https://inpublishing.co.uk/articles/brewin-dolphin-selects-ft-corporate-licence-13943 ; https://ftstrategies.com/en-gb/insights/an-engagement-based-pricing-model-to-accelerate-growth | 10-02 | independently-reported (FT-documented, quoted by libraries) | FT itself (a licence, not a third-party API) |
| b2 | **IP-range authentication** on an institutional licence | One university "set up using just IP based access with option to register personally by email" after FT declined to change its SSO for them (2020). It shows FT HAS granted IP-based access on a negotiated licence. | negotiated | https://lists.daasi.de/hyperkitty/list/fim4l@lists.daasi.de/message/JQLUGEXAO77I3FWDWXZEKUQQYBDIXNIN/attachment/3/attachment.html | 10-02 | independently-reported | FT (licence) |
| b3 | **Sign in with Google / Apple** | The FT sign-in screen offers "email and password ... and sign-in options using Google and Apple" (screens captured 2026-01-28). The FT app reportedly allows a passwordless email option or a Google account (search snippet, unverified). This moves the password step to Google or Apple, but the FT-side Security Verification can still fire. INFERRED. | none | https://lazyweb.com/canvas/flows/financial-times/sign-in | 10-02 | independently-reported | Google/Apple (identity, not a solver) |
| b4 | **Email magic link / one-time code** | NOT shown on the web sign-in flow (b3 source: email+password, Google, Apple only). The app "passwordless" claim is a snippet only. | -- | as b3 | 10-02 | independently-reported (absence) | -- |
| b5 | **Remember-me / FTSession cookie lifetime** | **Not documented anywhere reachable.** Cookiepedia lists ft.com cookies, but no lifetime for the session cookie was retrievable. HARVST's measured 24-75 min under keep-alive is the only figure on record. | -- | https://cookiepedia.co.uk/cookie/386266 | 10-02 | could not establish | -- |
| b6 | **Device limits / session revocation** | Not established. Library guides say only "you may need to reauthenticate your account after a period of time" (UCSD) and "you may not share your account with anyone else". | -- | https://ucsd.libguides.com/marketresearch/FT | 10-02 | FT-documented via library | -- |

**The strongest (b) route: b1, the FT corporate licence with SSO.**
- It is FT's own sanctioned path.
- The credential step leaves FT's challenged form.
- The documented re-authentication is every 180 days, not every 24-75 min.
- Whether a licensed SSO session still meets the hCaptcha interstitial on automated reads is the unknown. A licence term on
  automated access (b1 + c1) is the way to settle it with FT.

---

## (c) Licensed routes to FT full text -- no sign-in automation

| # | route | FT full text? | lag | cost / terms published | URL | read | tag | vendor |
|---|---|---|---|---|---|---|---|---|
| c1 | **FT for Developers APIs** | The Headline API is headlines only, click-through for full text (2014). The **Datamining API** lets developers "retrieve and host FT articles on their own servers". The **Access API** "displays full text FT articles co-mingled with content from other publishers". All "require a subscription to the Financial Times" and a key from developer.ft.com. HARVST got a 403 "Access to this API has been disallowed" on 09-22 without one. | real time (inferred) | licence; price not published | https://en.wikipedia.org/wiki/List_of_news_media_APIs ; https://inpublishing.co.uk/articles/ft-launches-customisable-api-6355 | 10-02 | independently-reported (developer.ft.com not fetchable) | FT (a licence) |
| c2 | **Bloomberg Terminal** | **YES for FT corporate-licence holders:** "FT customers with a corporate licence ... access Financial Times journalism via the Bloomberg Professional service". Without the licence, "headlines of FT articles that link through to FT.com" (announced 2010-12-06). Opal's site-Z terminal serves reference data today; its news entitlement was never tested (this seat, 09-30). | real time | needs the FT corporate licence; the Terminal is already held | https://www.mediapost.com/publications/article/140620/None ; https://www.journalism.co.uk/ft-makes-content-available-on-bloomberg-professional/ ; https://talkingbiznews.com/2010/12/page/11 | 10-02 | independently-reported (bloomberg.com press page 403) | Bloomberg (held) |
| c3 | **Factiva** (Dow Jones) | YES, the text-only FT; FT.com from 2000, print from 1981. A **30-day rolling embargo** applies, lifted only for academic-licence holders. | 30 days | Factiva subscription; not published | https://edesiderata.crl.edu/resources/financial-times (search snippet; the page's TLS failed) ; https://blogs.cranfield.ac.uk/library/ft-factiva (timed out) | 10-02 | independently-reported | yes |
| c4 | **Nexis / Nexis Uni** (LexisNexis) | YES, "with a one-month embargo". | 30 days | subscription | https://swansea-uk.libanswers.com/E-Resources/faq/281951 | 10-02 | independently-reported | yes |
| c5 | **ProQuest** (International Newsstream / ABI/INFORM / One Business) | YES, with the same one-month embargo (Swansea). One Business lists FT among its newspapers (Aberdeen guide, Dec 2023). | 30 days | subscription | https://swansea-uk.libanswers.com/E-Resources/faq/281951 ; https://www.abdn.ac.uk/library/documents/guides/qgbus001.pdf | 10-02 | independently-reported | yes |
| c6 | **LSEG Workspace** | **NOT verified.** Sources name Reuters and Dow Jones news; no source found carries FT full text on Workspace. | -- | -- | https://en.wikipedia.org/wiki/Eikon | 10-02 | could not establish | yes |

**Embargo exception:** "FT has an agreement in place with LexisNexis, EBSCO, Bloomberg and Factiva to lift the 30 day embargo for
any clients with the academic license in place" (CRL e-desiderata, via search snippet). That is an ACADEMIC licence. Whether a
corporate licence lifts it is not established.

**FT's terms on automated access:**
- **NOT quoted verbatim:** `help.ft.com/legal-privacy/terms-and-conditions` and its copyright policy refused this tool, and no
  third party quoted the automated-access clause.
- What third parties quote:
  - "You may not share your account with anyone else";
  - "FT.com resources are intended for your personal, educational use. Commercial use is not permitted" (UCSD, an academic
    licence's terms, https://ucsd.libguides.com/marketresearch/FT).
- FT's stated posture: its director of global public policy calls AI scraping "a breach of UK copyright law" and says AI firms
  resist licensing "because they don't want to pay" (Press Gazette, 2025-02-05,
  https://pressgazette.co.uk/media_business/copyright-ai-ft-right-wrong-opt-out-exemption/).
- **INFERRED:** FT's consumer terms are very likely to bar robots and scraping, as peer publishers' do. Argus Media, for example,
  bars "any 'robot', 'bot', 'spider', 'scraper'" (https://www.argusmedia.com/ft/terms/). This needs the verbatim read below.

---

## Could not establish

- The verbatim FT terms and copyright-policy clauses on robots, scraping and text and data mining. The read needs a browser on
  an Opal machine at `help.ft.com/legal-privacy/terms-and-conditions/` and `/copyright-policy/`.
- The FTSession cookie's lifetime, and any remember-me behaviour.
- Whether a licensed SSO or IP-authenticated session still triggers FT's hCaptcha interstitial on automated reads.
- FT corporate licence and Datamining API prices (not published), and whether a corporate (not academic) licence lifts the
  aggregators' 30-day embargo.
- Bright Data Web Unlocker's supported captcha types (not listed), and Ocilar's product scope (its PyPI page did not render).
- Whether any vendor that lists hCaptcha off-docs (forum claims) works. Untested by design: a test is a vendor call.
- LSEG Workspace FT carriage.
