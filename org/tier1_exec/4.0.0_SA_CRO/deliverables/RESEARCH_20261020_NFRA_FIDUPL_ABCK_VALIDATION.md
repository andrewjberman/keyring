# RESEARCH 2026-10-20 -- NFRA_FIDUPL: the _abck validation segment (Akamai behavioral verdict)

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 8854.
**Source:** Andrew's successful sign-in `wealthcentral.advisorchannel.com5.har` (off git). The `_abck` token is MASKED throughout; only
the short flag segments and their positions are shown.

## The structure (token masked)

`_abck` is 8 `~`-delimited fields: `TOKEN ~ [f1] ~ TOKEN ~ f3 ~ f4 ~ f5 ~ TOKEN ~ f7`. The three long fields (the sensor token) are
masked. The short fields are flags.

## The validation marker is FIELD INDEX 1 (the second field). Measured in HAR 5:

| Request | field[1] | reading |
|---|---|---|
| start #5 (carried-in cookie) | `-1` | not validated |
| **PASSWORD POST #47** | **`0`** | **VALIDATED** |
| home #92 | `-1` | (re-scored between calls) |
| post-login, ATT set #273 | `0` | validated |

Fields 3/4/5/7 are `-1` throughout in both states, so they do NOT discriminate. **Field index 1 is the Akamai behavioral verdict:
`0` = the session passed Akamai's human-behavior check; `-1` = it did not.**

**At the moment that matters -- the password POST -- Andrew's `_abck` field[1] = `0`.** That is why his password POST is accepted. The
box's refusals almost certainly carry field[1] = `-1` at the password POST.

## What the COO reads in the run-3 trace (exact position)

Split the `_abck` cookie SENT on the password POST by `~`; read **field index 1** (the second field) only. Expect:
- Andrew / success: `0`.
- The box / 403: `-1`.

If the box reads `-1` there, **Akamai's behavioral score is the blocker**, confirmed: the request reaches the password endpoint with an
unvalidated Akamai session.

## Implication for the fix (as the CTO framed it)

Akamai Bot Manager scores on behavior -- mouse movement, typing cadence, focus/blur, and the sensor POST (the `POST .../X3eR/...`
obfuscated endpoint) carrying that telemetry. To flip field[1] to `0` before the password POST, the drive must, on fakes:
- let the Akamai sensor script load and its sensor POST complete (do not block the obfuscated path);
- produce human-like input into the username/password fields (real mouse moves to the field, per-character typing with jitter, not
  `fill()` which sets the value instantly), then a short dwell before submit;
- submit only after the sensor POST that follows the typing has gone (so the fresh telemetry is scored).

This is the same class the data-harvest DataDome/PerimeterX solvers handle. It is independent of `navigator.webdriver` (already ruled
out) and of the browser build.

## Not measured

- Whether a single human-like pass reliably flips field[1] to `0` on the box's IP (the datacenter IP may still weigh the score). The
  paired hand-seed + Track-B test, and a drive that adds human-like input, settle it.
- The meaning of fields 3-7 (all `-1`; not load-bearing here).
