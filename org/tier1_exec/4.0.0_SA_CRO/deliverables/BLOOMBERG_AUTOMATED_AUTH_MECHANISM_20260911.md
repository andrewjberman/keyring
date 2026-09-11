# Bloomberg.com: an autonomous, network-corroborated login mechanism, proven end to end

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-11 | **For:** Andrew; `1.0.0_SA_CTO~Z` (L4), `2.0.0_SA_COO~ZZZ` (L5)
**Authorization:** Andrew-direct at this terminal, live throughout ("why not toss Bloomberg in there as well").
**Scripts:** `org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_harvest_session.py` (harvester), `.../bloomberg_rest_fetch.py` (REST consumer).
**Shared modules:** `press_and_hold_lib.py`, `nopecha_hcaptcha_lib.py` (see §5).
**Parked artifact:** Secrets Manager `bloomberg/session`, VersionId `88157610-8dd9-48dc-b92b-19b53f56ea2c`, 63 Bloomberg-domain cookies.
**Google account:** `google/andrew-goldengate/credentials` -- a second, Bloomberg-dedicated Google account, distinct from `officialmadeaux` (Seeking Alpha's/general-purpose).

---

## 1. What this is

Bloomberg presented the widest variety of obstacles of any of the four platforms in one login flow:
a PerimeterX Press & Hold wall (shared with Seeking Alpha), a Google OAuth sign-in (shared mechanism
with the general `google_oauth_handler.py`), and its own consent/welcome modals -- appearing in an
**unpredictable order and combination** from run to run. This is what drove the architecture: rather
than a single-state-machine harvester like Seeking Alpha's or FT's, Bloomberg's is built as an
**order-independent module dispatcher** (Andrew-direct 2026-09-11: *"we should be able to make each of
these items we've fought for a 'module' that kimi can call dynamically ... order should not matter"*).

Proven live, fully unassisted, 2026-09-11:

| Step | Result |
|---|---|
| Terms/consent modal | Detected and dismissed |
| "Sign In" click | Correct |
| Sign-in-method modal (iframe) | Detected, "Continue with Google" clicked from inside the iframe |
| Google OAuth popup | Handled, closed itself on completion, recovered cleanly |
| Post-login welcome modal | Dismissed via vision fallback |
| Identity | `LOGGED_IN`, corroborated by a real network `Set-Cookie` event |
| `bloomberg_rest_fetch.py check` | Real account: `andrew@goldengate.dev`, active `BBG` subscription |
| `bloomberg_rest_fetch.py ticker RTX:US` | Real live quote: RTX Corp, $198.12, +0.29% |

## 2. The module-dispatch architecture

Every turn: screenshot unconditionally, check whether the page has already resolved (`LOGGED_IN` +
a new cookie), then check every module's `detect(page, ctx)` fresh, in a fixed PRIORITY order, and run
the `handle()` of the first one that matches. The priority order itself encodes real, hard-won lessons,
not an arbitrary list:

1. **`bot_wall`** -- a PerimeterX Press & Hold challenge, wherever it renders (see §3).
2. **`hcaptcha_nopecha`** -- an hCaptcha challenge, solved via the NopeCHA Token API (the same
   mechanism proven on FT, factored into a shared module, see §5).
3. **`google_oauth`** -- a popup already on `accounts.google.com`.
4. **`signin_iframe`** -- the sign-in method chooser, which turned out to live inside an iframe (§4).
5. **`google_button`** -- a top-level "Continue with Google" button, if one ever appears outside an iframe.
6. **`overlay_modal`** -- a GENERIC, content-agnostic dismiss handler, checked only once nothing more
   specific matched (§4.2).
7. **`sign_in_needed`** -- the plain header "Sign In" click, lowest priority.

**Why this order matters, concretely:** a dimmed-backdrop modal containing "Continue with Google" is
structurally identical to a plain "accept our terms" modal (both are a dark backdrop with a centered
white card). Andrew's own live observation caught the real bug this produces: *"it found the sign in
button, but then it brought up a modal to use google sign-in, and didnt realize the modal popped
up"* -- checking the generic dismiss handler first grabbed an ambiguous/wrong button (see §4.2) instead
of recognizing the modal's actual content. Content-specific modules must be checked before a generic
"is something covering the page" handler, precisely because a covering layer can also BE the thing you
need to interact with, not just something to clear out of the way.

## 3. The Press & Hold widget: three real behavioral fixes, all upstreamed to the shared module

Bloomberg uses the identical PerimeterX-style widget as Seeking Alpha. Three real, live-observed
behaviors were fixed in `press_and_hold_lib.py` -- the ONE shared module both `sa_harvest_session.py`
and `bloomberg_harvest_session.py` import, so every fix here applies to both sites (and any future one)
automatically, with no duplicated code:

1. **The fill bar de-fills if held too long** -- there is a target window, not "longer is safer"
   (found on Seeking Alpha, 2026-09-10).
2. **The true completion marker is a checkmark appearing in the widget's CENTER**, not the bar simply
   looking full -- a whole-widget fill signal can plateau on the color sweep alone whether or not a
   checkmark ever appears (found on Seeking Alpha, 2026-09-10).
3. **The bar can be actively pushed back toward zero WHILE STILL HELD** -- Andrew-direct 2026-09-11,
   confirmed as a property of the widget itself, not Bloomberg-specific: *"ive seen this exact same
   behavior in SA, its a function of the press and hold, so this instruction is relevant for any
   'press and hold' captcha module."* This is different from de-filling after release -- it requires
   physically releasing the mouse for a beat (0.4-0.8s), then pressing again, rather than continuing to
   hold through it or just picking a different release moment. Capped at 4 recovery cycles per attempt.

The widget can also be rendered inside its OWN iframe (isolating it from the host page's JS, a common
PerimeterX pattern) -- `detect_bot_wall` now searches every frame's own text, not just the top-level
page, after a live run showed the top-level-only check missing a wall that was clearly on screen.

## 4. The sign-in iframe: the real root cause, found by inspection, not guessing

**This was the single largest source of confusion across many live runs**, and it was resolved only
when Andrew inspected the real DOM himself and pasted it back:

```html
<div class="reg-ui-client__uverify-iframe-container">
    <iframe id="reg-ui-client__iframe" class="reg-ui-client__uverify-iframe"
            src="https://www.bloomberg.com/account/iframe/login" frameborder="0"></iframe>
</div>
```

The ENTIRE "choose a sign-in method" modal -- the email field, "Continue with Google/Apple/BBA" --
lives inside this iframe, loaded from a separate URL, appended at the very end of `<body>` (visually
centered, but last in DOM order -- Andrew: *"its a div at the very very bottom of the elements"*). Every
top-level `page.locator()` search this investigation had been running was silently querying the WRONG
document. The fix (`detect_signin_iframe` / `handle_signin_iframe`) uses `page.frame_locator()` to
pierce into that iframe's own content directly.

**4.1 -- a follow-on bug in the fix itself:** the first version checked bare DOM presence
(`.count() > 0`), which falsely fired when a NEW bot-wall modal appeared on top of the (now-hidden)
iframe -- the iframe element was still present in the DOM, just covered. Fixed by requiring `:visible`.

**4.2 -- the generic dismiss handler's own bug:** one real Bloomberg sign-in screen had FOUR buttons
containing the word "Continue" (a disabled bare email-continue, plus "Continue with
Google/Apple/BBA"). The generic `overlay_modal` dismiss handler's text-match list included bare
"Continue," which could grab the wrong (or disabled) button. Fixed by moving "Continue" to
last-resort priority and excluding any match that also names a known provider (Google/Apple/Facebook/
Microsoft) -- those belong to a dedicated module, checked earlier, by design.

**4.3 -- a generic, content-agnostic backdrop detector, per Andrew's own suggested heuristic:**
*"if there is a way to deterministically identify a central modal popup (e.g. through a dimming of the
rest of the page but bright loosely in the center, then that is a hint."* `detect_overlay_modal`'s
primary signal is now structural: a DOM element that is `position: fixed`/`absolute`, covers most of
the viewport, and has a dark, semi-transparent background color -- true regardless of what the modal's
text actually says. ARIA role and known dismiss-button text remain as fallbacks.

## 5. Two mechanisms factored into shared modules this session

- **`press_and_hold_lib.py`** -- the full checkmark/drain-aware adaptive release mechanism (§3),
  extracted from `sa_harvest_session.py` so Bloomberg could reuse it without duplicating hard-won logic
  or importing a script that runs a live login as a side effect of import.
- **`nopecha_hcaptcha_lib.py`** -- the NopeCHA Token API hCaptcha solver, extracted from
  `ft_harvest_session.py` (see `FT_AUTOMATED_AUTH_MECHANISM_20260911.md` for its own three real bugs:
  a dead `nopecha.api_key` assignment, the raw response dict vs. bare token string, and the
  `data-callback` invocation FT specifically needed). Wired into Bloomberg's dispatcher as the
  `hcaptcha_nopecha` module -- not yet exercised live against a real Bloomberg hCaptcha (only its
  Press & Hold wall has been observed so far), but ready if one appears.

## 6. The network-level completion oracle, and a real parking bug

Same mechanism as Seeking Alpha and FT: gate completion on a real network `Set-Cookie` event via
`Response.header_values()`, not a cookie-jar snapshot alone. Bloomberg's real identity cookies, now
confirmed and hardcoded (replacing an initial "record everything" approach that flooded stdout with
ad-tech noise): `_user-id`, `_user-token`, `_user-jwt`, `_user-role`, `_breg-uid`, `_breg-user`,
`_last-refresh`, `session_id`, `session_key`, `agent_id`, `gatehouse_id`.

**Real bug found and fixed:** a first successful login's FULL bundle (125 cookies including ~80
third-party ad-tech ones, plus 308 raw network-event records) exceeded AWS Secrets Manager's secret
size limit, and the park failed silently after a genuinely successful login -- the identity was
captured but never reached Secrets Manager. Fixed by parking a TRIMMED bundle: Bloomberg-domain
cookies only (every real identity cookie is Bloomberg-domain; third-party ones are never needed for
REST access) and a 10-event sample plus a count instead of the full event list. The full, untrimmed
bundle still writes locally for audit.

A `--manual` mode was also added (`bloomberg_harvest_session.py --manual --park`): disables all
automated clicking and only watches (polling the shared cookie jar plus a vision-confirmed
`LOGGED_IN` check) while a human drives the browser directly -- built for, and used during, exactly
this investigation's live debugging, and left in as a standing capability.

## 7. REST discovery -- found by sniffing real traffic, not guessing

Of roughly 110 XHR/fetch calls observed from a real authenticated page load, three are Bloomberg's own
first-party data APIs (documented in full, with parameters, in `bloomberg_rest_fetch.py`'s own
docstring and in the consolidated endpoint reference):

- `GET login.bloomberg.com/user-info` -- session/auth check. PROVEN: returns real account data
  (`andrew@goldengate.dev`, active `BBG` subscription).
- `GET www.bloomberg.com/nemo-next/api/tickers?ids={TICKER}:{EXCHANGE}` -- the per-symbol lookup.
  PROVEN: returned real live RTX Corp quote data.
- `GET www.bloomberg.com/bazaar/api/chart-news/{TICKER}:{EXCHANGE}?...` -- per-ticker news tied to the
  chart widget. NOT YET PROVEN -- a hand-built call with a naive timestamp guess 404'd, and the real
  request's full parameter set (at least one truncated in the sniff log) was not recaptured on two
  follow-up attempts. Documented honestly as unproven, not papered over.

No residential proxy was needed for any of these calls -- native IP served all of them cleanly,
unlike Seeking Alpha.

## 8. Script and module manifest

| Path | Role |
|---|---|
| `org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_harvest_session.py` | Browser login harvester: order-independent module dispatch, iframe-aware sign-in, network-auth oracle, trimmed session parking, `--manual` mode. |
| `org/tier1_exec/4.0.0_SA_CRO/scripts/bloomberg_rest_fetch.py` | Browser-free REST consumer riding the parked session; `check`/`ticker`/`news` verbs. |
| `org/tier1_exec/4.0.0_SA_CRO/scripts/press_and_hold_lib.py` | Shared PerimeterX Press & Hold defeat mechanism (checkmark + drain-recovery), used by both this file and `sa_harvest_session.py`. |
| `org/tier1_exec/4.0.0_SA_CRO/scripts/nopecha_hcaptcha_lib.py` | Shared NopeCHA Token API hCaptcha solver, used by both this file and `ft_harvest_session.py`. |

## 9. Open items

- The `hcaptcha_nopecha` module is wired but not yet exercised live against a real Bloomberg hCaptcha.
- The `chart-news` REST endpoint's full parameter set is unproven (§7).
- Bloomberg's own anti-bot defense showed clear escalation behavior after ~7-8 attempts in under an
  hour (the same pattern Seeking Alpha showed earlier the same night) -- treat repeated live attempts
  in a short window as a real cost, not a free retry.
