# Seeking Alpha: an autonomous, network-corroborated login mechanism, proven end to end

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-11 | **For:** Andrew; `1.0.0_SA_CTO~Z` (L4), `2.0.0_SA_COO~ZZZ` (L5)
**Authorization:** Andrew-direct at this terminal, live throughout ("run SA live now", "test the REST fetch with this session").
**Scripts:** `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_harvest_session.py` (harvester), `.../sa_rest_fetch.py` (REST consumer).
**Parked artifact:** Secrets Manager `seeking-alpha/session`, updated 2026-09-11T02:13:39Z, VersionId `3882be57-6a3e-4693-8a7a-2c768bf28af1`, 54 cookies.

---

## 1. What this is

A Playwright-driven login flow for `seekingalpha.com` that reaches a completion bar stricter than "the
UI looks logged in": it requires an actual **network event that serves the identity artifact**, not
just a post-hoc read of the browser's cookie jar. Andrew's own bar, verbatim: *"it is not done until
there is some network change and a jwt served or something."* Once that bar is met, the harvested
session is parked to Secrets Manager and a separate, browser-free REST client rides it.

This run (2026-09-11, unassisted -- first fully autonomous pass, no manual intervention) went
`ANON -> LOGIN -> LOGGED_IN` with no bot wall at all, then proved the REST path live:

| Call | Result |
|---|---|
| `sa_rest_fetch.py check` | `authorized=True`, active Annual subscription |
| `sa_rest_fetch.py symbol RTX` | `sa_id=601510`, name "RTX Corporation" |
| `sa_rest_fetch.py report RTX` | real `virtual_analyst_report`, dated 2026-09-10, 5,975 report chars + 1,968 ratings chars |

All three rode the one parked session -- zero re-logins.

## 2. The captcha-defeat mechanism (`sa_harvest_session.py`)

PerimeterX's "Press & Hold" wall is the recurring obstacle here. Two live-observed properties drove
the design, both from Andrew watching runs directly, not from documentation:

- **The fill bar de-fills if held too long** -- there is a target window, not "longer is safer."
- **The true completion marker is a checkmark appearing in the center of the bar**, not just "the bar
  looks full." A whole-widget fill signal can plateau on the color sweep alone whether or not a
  checkmark ever actually appears.

Kimi vision (`kimi-k3`, `api.moonshot.ai`) is measured at 10-20s per call and is far too slow to close
a loop against an animation that runs in a few seconds, so the two problems are split:

- **Locating the button** is Kimi's (or DOM's) job, done once per wall occurrence.
- **Releasing at the right instant** is a purely local pixel-diff loop with zero network calls
  (`press_and_hold_adaptive`): it screenshots a small crop of the widget every ~150ms and tracks two
  signals against a pre-press baseline -- a whole-crop diff (the fill sweep) and a center-region-only
  diff (the checkmark). The PRIMARY release trigger is a sharp, localized jump in the center signal;
  the whole-crop signal peaking is kept only as a fallback if a checkmark is ever too subtle to resolve
  at this crop's resolution.
- **The widget is re-located fresh on every occurrence**, searching every open Playwright page in the
  context (DOM first, vision fallback) rather than assuming it stays on the page or at the point it was
  found last time -- PerimeterX's own escalation can put a challenge (or the next one -- a Gmail sign-in,
  an hCaptcha, anything) on a page/popup that didn't exist a moment ago. The main harvest loop itself
  checks for a newly-appeared page every step and switches its working page to it; this is generic to
  whatever the next challenge turns out to be, not special-cased to the press-and-hold widget.
- **A repeated wall right after completing one is treated as normal**, not an error -- Seeking Alpha is
  observed to sometimes ask twice.
- **A perceptual-hash cache** (`_img_hash`/`_hamming`, an 8x8 average-hash with Hamming-distance
  tolerance) skips a Kimi call entirely when the screen hasn't visibly changed since the last poll --
  measured live: a repeated bot-wall screen was correctly recognized from cache with zero Kimi calls.
- **20-second Kimi timeout** (was 60s) with the existing 2-attempt retry, and the model default is
  `kimi-k3` (was `kimi-k2.6`, ~8x slower on identical vision-grounding tasks, measured separately on
  the Google OAuth path -- see below).

Caveat, stated plainly: the checkmark-detection release logic has not yet fired on a live run -- the
2026-09-11 unassisted run went straight to LOGGED_IN with no bot wall at all. It is built and reasoned
through from direct observation, not yet proven against a real occurrence.

## 3. The network-level completion oracle

A cookie-jar read after the fact cannot tell you an identity cookie was actually *served by the
network* during this run versus set some other way. `sa_harvest_session.py` now listens on every
response (`page.on("response", ...)`, attached to every page/popup that ever opens, not just the
first) and records the network EVENT of an auth artifact arriving -- a `Set-Cookie` for one of the
site's identity cookies (`user_id`, `session_id`, `user_remember_token`, `user_cookie_key`), a
JWT-shaped bearer token in an `Authorization` header, or one in an xhr/fetch JSON body. Only presence,
kind, field name, URL and length are ever logged -- never a value.

**A real bug was found and fixed inside this mechanism.** The first live run under this oracle showed
identity cookies present in the jar with **zero** corroborating network events -- a result that should
not have been possible if the listener were sound. Cause: `Response.headers` is a dict that collapses
duplicate headers, and `Set-Cookie` is exactly the header that legitimately repeats (one response can
set several cookies in separate headers). The fix was `Response.header_values("set-cookie")`, which
Playwright's own docs confirm preserves every occurrence individually. The very next live run caught it
correctly: three `Set-Cookie` events on `POST https://seekingalpha.com/api/v3/login_tokens`, naming
`user_id`, `user_cookie_key`, and `user_remember_token` -- the same endpoint the old code had been
silently missing.

Completion is gated on this evidence, not just the jar snapshot: when identity cookies appear, the
harvester waits briefly for a corroborating network event before accepting, and if none ever arrives it
still proceeds but logs loudly that the run's evidence is the weaker jar-only kind. This provenance
travels with the parked bundle as `network_auth_corroborated` and `network_auth_events` (kind/name/url
only), so any downstream consumer of a parked session can see which kind of evidence backs it.

## 4. The REST consumer (`sa_rest_fetch.py`)

Rides the parked session -- never logs in inline. Contract (measured, documented in its own header and
in `AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md`): the jar must carry the full PerimeterX
cookie set (not just the identity four), every request needs a per-page `Referer`, and the fetch must
egress through the Bright Data residential proxy (native IP gets PerimeterX-blocked after roughly ten
calls). A `403` with `blockScript` in the body is the re-harvest signal, not an auth failure. A separate
bug -- a missing `verify=False` on the `curl_cffi` session, needed because the residential proxy SSL-bumps
traffic -- was found and fixed in this already-committed script earlier in this investigation.

Verbs proven live this session: `check`, `symbol <ticker>`, `report <ticker>` (the `virtual_analyst_report`
modal's actual data source).

## 5. Script manifest

| Path | Role |
|---|---|
| `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_harvest_session.py` | Browser login harvester: Kimi-vision state classification, adaptive checkmark-keyed press-and-hold, cross-page widget search, network-auth oracle, session parking. |
| `org/tier1_exec/4.0.0_SA_CRO/scripts/sa_rest_fetch.py` | Browser-free REST consumer riding the parked session (residential proxy egress). |

## 6. Related mechanisms built the same session (separate accounts/sites -- not this brief's subject)

- `org/tier1_exec/4.0.0_SA_CRO/scripts/captcha_sentinel.py` -- the shared event-driven
  perceive-classify-dispatch engine (full-OS-screen capture via `mss`, continuous Kimi classification,
  per-state dispatch) that this SA work shares its underlying vision/caching techniques with.
- `org/tier1_exec/4.0.0_SA_CRO/scripts/google_oauth_handler.py` -- a Google sign-in handler
  (`officialmadeaux@gmail.com`) using a turn-invariant Kimi tool-calling navigation loop for Google's
  own variable-shape 2-Step Verification flow, with Quo (quo.com) as the SMS-code reader. This is where
  the kimi-k3 speed measurement and the read/write call-splitting pattern were first proven, then
  ported into `sa_harvest_session.py` above. Still blocked on Google's own delay before a newly-added
  phone number becomes usable for verification -- unproven end-to-end on the SMS-read path.
- `org/tier1_exec/4.0.0_SA_CRO/scripts/ft_harvest_session.py`, `.../ft_rest_fetch.py`,
  `.../wsj_rest_fetch.py` -- Financial Times and WSJ session/REST harvesters, a separate investigation
  (`AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md` and the FT/WSJ diagnostic work), not
  part of this mechanism.
