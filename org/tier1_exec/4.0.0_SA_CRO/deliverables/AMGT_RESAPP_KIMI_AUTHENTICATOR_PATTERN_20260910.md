# The bd-49f Kimi authenticator -- the reusable pattern for Seeking Alpha sign-in

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10
**Ask (Andrew, verbatim):** *"find the bd-49f authenticator runner code because it has some Kimi
Computer Vision function which may be necessary for managing Seeking Alpha."*
**Found:** `infra/aws/ec2/bd-49f-auto-login/bd_49f_auto_login.js` (604 lines, author
`0.6.0_AE_PartnerETL`, project `ADVI_BDAPIMIG.P1`). Live as EC2 `bd-49f-auto-login`
(`i-0fa1846f04ed7e337`, drift=DECLARED). Sibling: `infra/aws/ec2/bd-cot-auto-login/`.

> ⚠ **NAME COLLISION, read before searching:** "Kimi" is badly overloaded in this estate.
> `OPAL_KIMIPIPELINE` is a **separate semantic-pipeline program** (2,218 hits repo-wide). The
> computer-vision auto-login use is a different thing entirely, and lives only under
> `infra/aws/ec2/bd-*-auto-login/` and `tools/astn_wsjft/scripts/harvest_ft_session.js`.

---

## 1. WHAT IT ACTUALLY DOES

A Playwright-driven **perceive-act state machine** that signs into Black Diamond
(`bdreporting.com`) unattended, clears MFA, and **parks the fresh session back into Secrets
Manager**. Two Kimi vision primitives drive it:

**(a) `classifyState(page, kimiKey, otpEntered)` -- the vision STATE CLASSIFIER.**
Screenshots the page, base64s it, and asks Kimi-VL to answer with **exactly one token**:
`LOGIN | MFA_OTP | LOGGED_IN | MODAL | UNKNOWN`. That token is the state machine's input -- the
driver does not parse the DOM to know where it is, it *looks*.

**(b) Vision GRID-LOCALIZE -- "pixel coords of a described element".** Give it a description, get
back coordinates to click. The source names its origin explicitly: *"the harvest_ft
grid-localization primitive"* -- i.e. **it was built for the FT session harvester and already
generalised once.** This is the captcha / click-through primitive.

## 2. THE WIRING -- every input is a SECRET-ID, never a value

```
BD_CREDENTIALS_SECRET_ID = blackdiamond/49f/credentials        -> {username, password}
BD_KIMI_SECRET_ID        = astn/kimi/api-key                   -> the Kimi API key
BD_PROXY_SECRET_ID       = astn/brightdata/residential-proxy    -> resi proxy, "ALWAYS-ON"
BD_SESSION_SECRET_ID     = blackdiamond/49f/session             <- fresh session bundle WRITTEN back
BD_OTP_ADAPTER(graph|teams|none), BD_OTP_MAILBOX, BD_GRAPH_SECRET_ID
BD_KIMI_MODEL            = kimi-k2.6
```

**Three things worth noticing:**
1. **It uses the SAME residential proxy secret as ASTN FT** (`astn/brightdata/residential-proxy`).
   One proxy, two authenticators -- consistent with Andrew's no-proliferation ruling.
2. **The OTP is fetched from EMAIL via Microsoft Graph** (`BD_OTP_ADAPTER=graph` + `BD_OTP_MAILBOX`).
   The loop is fully closed: it can receive its own verification code.
3. **`astn/kimi/api-key` is a secret I had not surfaced** in the earlier credential inventory --
   that sweep grepped `bright|brd` only, so it was outside the pattern rather than absent.

## 3. THE ROE -- CTO-ruled, CVO-verified, NON-NEGOTIABLE

> *"observe-act-only. NEVER log/persist credential or OTP VALUES (no console of password/code/cookie
> value; no debug-dump of the OTP email/body)."*

Credentials arrive via a local file the orchestrator pulls from SM; the OTP is **in-memory,
single-use**; the ONLY persisted artifact is the session bundle. Screenshots are debug-safe by
construction -- the post-username shot shows a masked password, the MFA shot shows only a masked
destination. **Any SA adaptation inherits this ROE unchanged.**

## 4. THE HARDENING -- these are paid-for lessons, do not re-learn them

- **KIMI-HEALTH GUARD (0.6.2, 2026-07-02).** A `kimiVision` REJECT used to kill the whole attempt,
  and a RESOLVE-EMPTY fell silently to `UNKNOWN` -- so a **Kimi-side outage presented as an
  invisible all-UNKNOWN loop across every attempt**, indistinguishable from a genuinely ambiguous
  screen. Fix: separate CALL FAILURE from AMBIGUOUS SCREEN, log them distinctly, retry the call
  once, then fall through to DOM.
- **DOM-FALLBACK classifier.** Cheap `locator().count()` probes and URL shape, no vision, for when
  vision blanks. **Reuses the same selectors the LOGIN/MFA handlers already target**, so a DOM
  signal recovers a step rather than merely reporting one.
- **The cot-run bug.** Kimi read *"Please Wait... 186 Items Ready"* as a verify screen. Fixed with
  tight discriminators plus a **completion bias**: once an OTP has been submitted, app content is
  `LOGGED_IN`, never `MFA_OTP`.
- **"A hang is not a THROW or an 'end'."** A socket that connects and never responds fires neither
  `error` nor `end`, so the promise hangs forever, the step budget blows, **and the health guard's
  retry never runs.** Timeouts are mandatory, not defensive.
- **LOGGED_IN is gated on `otpEntered`** so a mid-login DOM blip cannot set rc=0 prematurely; the
  identity cookie stays the authoritative success signal and vision only advances the machine.

## 5. WHY THIS MATTERS FOR AMGT_RESAPP

Andrew's SA design is **one-shot/crawl `https://seekingalpha.com/symbol/{TICKER}`**. Public SA pages
may need nothing more than the `one_shotter` zone. **But anything paywalled needs an authenticated
session, and a cookieless unlocker provably cannot ride one** (measured on FT: the Unlocker ignores
custom cookies, the Scraping Browser sandboxes injection). The estate's answer to that problem is
exactly this file.

**The transferable stack, already built and proven twice (FT, Black Diamond):**

```
  our own Playwright/Chromium
    -> egressing through astn/brightdata/residential-proxy   (clean IP, passes bot-walls)
    -> Kimi-VL classifies the screen + localizes elements to click
    -> OTP, if any, pulled from email via Graph
    -> fresh session bundle PARKED in Secrets Manager
    -> the scheduled fetch RIDES the parked session, never logs in inline
```

**Andrew's SA credentials are now stored to slot into exactly this shape:**
`seeking-alpha/credentials` (created 2026-09-10, tagged `service=seeking-alpha, kind=site-login`).
Its sibling `seeking-alpha/session` is the parked-session slot when the harvester is built --
mirroring `blackdiamond/49f/{credentials,session}` and `astn/ft/{credentials,session}`.

## 6. NOT MEASURED

- **Whether SA's login is captcha-gated at all**, and if so with what. FT is hCaptcha; SA is
  unverified. This decides whether the vision layer is needed or whether a plain form-fill suffices.
- Whether `bd-49f-auto-login` is **currently running** (the instance is DECLARED and present; its
  schedule state was not read).
- The `kimiVision()` function body itself -- the HTTP call shape and model parameters were inferred
  from call sites and the env contract, **not read**.
- `astn/kimi/api-key` **liveness** -- not tested.
