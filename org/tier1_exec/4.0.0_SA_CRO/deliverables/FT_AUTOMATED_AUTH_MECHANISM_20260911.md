# Financial Times: an autonomous, network-corroborated login mechanism, proven end to end

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-11 | **For:** Andrew; `1.0.0_SA_CTO~Z` (L4), `2.0.0_SA_COO~ZZZ` (L5)
**Authorization:** Andrew-direct at this terminal, live throughout ("Let's try NopeCHA", "run it live now").
**Scripts:** `org/tier1_exec/4.0.0_SA_CRO/scripts/ft_harvest_session.py` (harvester), `.../ft_rest_fetch.py` (REST consumer).
**Parked artifact:** Secrets Manager `astn/ft/session`, updated 2026-09-11T03:47:14Z, VersionId `9982f598-710e-4163-b9a0-9f817cd8f862`, 51 cookies.
**Vendor account:** NopeCHA (nopecha.com) Starter plan, key parked at Secrets Manager `nopecha/api-key`.

---

## 1. What this is

Same mechanism and same completion bar as the Seeking Alpha brief
(`SEEKING_ALPHA_AUTOMATED_AUTH_MECHANISM_20260911.md`): a login is not accepted as done until a real
**network event serves the identity artifact**, not merely a post-hoc cookie-jar read. Proven live,
2026-09-11:

| Call | Result |
|---|---|
| `ft_harvest_session.py --park` | Real login, `Set-Cookie: FTSession_s` on `accounts.ft.com/login`, session parked |
| `ft_rest_fetch.py check` | `authorized` |
| `ft_rest_fetch.py quote RTX NYQ` | Real tearsheet data: 120,481 + 124,369 bytes, through the residential proxy |

FT's obstacle is a real hCaptcha challenge on login (unlike Seeking Alpha's PerimeterX Press & Hold),
and getting to the result above took several real, load-bearing fixes -- documented below because each
one would silently recur on the next maintainer who touches this file.

## 2. hCaptcha: three approaches tried, in order, with what each one taught

**(a) Kimi vision, tile-by-tile classification -- MEASURED TOO SLOW, abandoned.** A clean isolation
test settled this rather than guessing: a simple single-target Kimi (`kimi-k3`) vision call returns in
~7s, but a prompt shaped like "classify every tile against an instruction, in detail" -- exactly
hCaptcha's real challenge shape -- timed out at a full 60s without ever completing, on three separate
live attempts. This is a genuine capability/latency limit for multi-object grid classification, not a
timeout-tuning problem. (A real bug was fixed in this path regardless before it was abandoned: the
retry loop treated a Kimi timeout the same as "no tiles match" and could report failure on a captcha
that had already auto-passed on its own while Kimi was still stuck retrying against a stale
screenshot -- fixed by checking "is the challenge frame already gone" both before and after every
solve attempt, not only after a click.)

**(b) The NopeCHA browser extension, loaded via `launch_persistent_context` -- MEASURED NEVER
ACTIVATED, abandoned.** The extension installs and shows ENABLED in `chrome://extensions` (confirmed
by screenshot), but `context.service_workers` and `context.background_pages` were empty both before
and during a live challenge, and it never visibly intercepted anything. Andrew's own correction
redirected this: *"i didnt install the chrome extension i didnt think we had to, i thought you could
just operate it via API solely"* -- correct, and the better design regardless (no browser-loading
fragility, a verifiable HTTP call instead of an opaque extension).

**(c) The NopeCHA Token API, called directly -- WORKS, proven live.** `POST /v1/token/hcaptcha` with
the page's real `sitekey` (read from the standard `data-sitekey` DOM attribute, not parsed out of the
challenge iframe's own asset-versioned URL) and the login page's URL; NopeCHA solves the ENTIRE
challenge on its own backend and returns a token, no browser interaction needed on their end at all.
Three further real bugs were found and fixed getting this to actually work, in the order they were
caught:

1. **The official example script's `nopecha.api_key = "..."` pattern is a dead assignment** against
   the installed `nopecha>=2.0` package. `nopecha/__init__.py` uses a module-level `__getattr__`
   (PEP 562) that intercepts *reads* of `Token`/`Balance`/`api_key` and lazily redirects to a
   deprecated `_v1_compat` shim -- but `__getattr__` never fires on a *write*, so the assignment just
   creates an orphaned attribute on the wrong object. The shim actually reads its key once, at first
   access, via `os.getenv("NOPECHA_API_KEY", "")`. Every call before this fix silently ran as an
   anonymous, IP-rate-limited free request -- never touching the paid Starter account at all, which is
   almost certainly why the very first live attempt failed with a generic "server did not accept job
   after 10 attempts" (an overloaded anonymous queue, not a real outage). Fixed by setting the
   environment variable instead; verified directly (`nopecha.Balance.get()` before the fix returned
   `{"plan": "Free", "credit": 100}`, after it returned the real `{"plan": "Starter", "credit": 2000}`,
   matching the account dashboard exactly).
2. **`Token.solve()` returns the raw response dict `{"data": "<token>"}`, not the bare token string**
   -- confirmed by reading the installed library's own source
   (`_v1_compat.UrllibAPIClient._request_get` returns `job_request.body` verbatim), contradicting what
   the official example script's own `print(token)` line implies. The first correctly-authenticated
   live run measured `token length=1` -- not a 1-character token, but the dict's ONE KEY -- and had
   silently injected a stringified dict into the page instead of the real token.
3. **Setting the `h-captcha-response` textarea's value alone was not enough for FT's specific
   integration to notice.** FT's widget carries `data-callback="onSocialSubmit"`; the site reads
   challenge completion via that JS callback firing, not by polling the textarea's DOM value. Fixed by
   also invoking `window[callbackName](token)` directly when such an attribute is found. This was the
   fix that produced the real login -- confirmed live via a diagnostic result line,
   `{"textareas_found": 1, "callback_name": "onSocialSubmit", "callback_invoked": true}`, immediately
   followed by the real `Set-Cookie: FTSession_s` network event and the page progressing on its own
   with no further click needed.

A fourth, unrelated crash was found and fixed in the same investigation: FT can independently
auto-redirect to a passkey-setup interstitial (`accounts.ft.com/passkeys/set-up`) right after a real
successful login, and that redirect once raced this harvester's own explicit navigation to
`www.ft.com`, throwing an uncaught Playwright "interrupted by another navigation" error that crashed
the whole run -- even though the identity cookie had already been served by then. Fixed by tolerating
that specific race rather than letting it kill the process.

## 3. The network-level completion oracle

Identical mechanism to the Seeking Alpha harvester, ported the same day: `page.on("response", ...)`
attached to every page/popup that ever opens, watching for a `Set-Cookie` naming `FTSession` or
`FTSession_s` via `Response.header_values("set-cookie")` (not the duplicate-collapsing `.headers`
dict), or a JWT-shaped bearer token. Completion waits briefly for this evidence before accepting a
bare cookie-jar read, and logs loudly when only the weaker jar-only evidence is available. This run's
real event: `Set-Cookie` for `FTSession_s` on `POST accounts.ft.com/login`, immediately after the
NopeCHA callback fired.

## 4. Script manifest

| Path | Role |
|---|---|
| `org/tier1_exec/4.0.0_SA_CRO/scripts/ft_harvest_session.py` | Browser login harvester: consent dismissal, NopeCHA Token API hCaptcha solve, network-auth oracle, session parking. |
| `org/tier1_exec/4.0.0_SA_CRO/scripts/ft_rest_fetch.py` | Browser-free REST consumer riding the parked session (residential proxy egress); article/listing/quote verbs. |

The NopeCHA browser extension tried in §2b (`github.com/NopeCHALLC/nopecha-extension`, release asset
`chromium_automation.zip`) is NOT kept in-repo -- 1.8MB of unused third-party bundle for an abandoned
approach is not worth it in history; re-download it if that path is ever revisited.

## 5. Open items

- The passkey-setup interstitial is tolerated (the crash it caused is fixed) but not yet *handled* --
  no code dismisses it if it blocks a later step. Not measured to matter for the REST path (the
  identity cookie is already served before the interstitial appears), but worth a dynamic,
  Kimi-driven dismiss handler (the same turn-invariant pattern already proven on the Google OAuth
  path) if a future run shows it actually blocking something.
- `MAX_HCAPTCHA_ROUNDS` and the now-unused Kimi tile-classification code path (`kimi_vision`,
  `MAX_HCAPTCHA_ROUNDS`) were superseded by the NopeCHA Token API but not yet removed from the file --
  a cleanup pass, not a correctness issue.
