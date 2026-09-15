# Barron's / NopeCHA compatibility investigation

Seat: `4.0.0_SA_CRO~W`. Recorded 2026-09-15 05:46 UTC.
Channel: direct user messages in this Codex session; exact message timestamps unavailable.

## Andrew-direct instructions, verbatim

> see if our nopeCHA api would work on Barron's

> need to know what type of captcha barrons is using then you check nopeCHA API docs and find the matching solution and call type

## Measured result

The captured Barron's challenge is **DataDome Slider**. The local screenshot
`.runtime/opal-data-harvest/barrons-repair-before.png` shows the slide-right
verification widget. The encrypted response
`.runtime/opal-data-harvest/barrons-reuse-contract-1.dpapi` contains a challenge
URL whose host/path are `geo.captcha-delivery.com/captcha/`. Token-bearing
query parameters were neither printed nor sent to NopeCHA.

DataDome's primary documentation identifies this provider's Slider and its
`*.captcha-delivery.com` response-page domain:

- https://docs.datadome.co/docs/datadome-captcha
- https://docs.datadome.co/changelog/last-call-on-required-change-for-users-of-csp-directive-frame-src

NopeCHA's current supported CAPTCHA list and complete public API reference
contain **no documented DataDome recognition or token endpoint/call type**:

- https://developers.nopecha.com/captcha/
- https://nopecha.com/api-reference/

The superficially similar documented route is
`POST /v1/recognition/geetest`, followed by GET on the same endpoint with the
job ID. It accepts GeeTest puzzle imagery and returns a horizontal placement
percentage. This is a different provider and is not evidence of DataDome
compatibility. The existing repository shared helper uses the hCaptcha Token
API (`Token.solve(type="hcaptcha", ...)`), also a different provider.

At 05:46:09 UTC, one authenticated `GET https://api.nopecha.com/v1/status`
using AWS Secrets Manager `nopecha/api-key` (us-east-1) returned HTTP 200:
Starter, Active, credit 1970, quota 2000. Only allowlisted account fields were
printed. Evidence: `.runtime/opal-data-harvest/nopecha-barrons-compatibility.json`.

External instruments: official documentation via web tool; account status via
Python requests. No solver job submitted, no publisher request, no credential
login, no session replacement, no recurring collection activated in this check.

Conclusion: **No matching documented NopeCHA call was found for Barron's
observed DataDome Slider.** This establishes a documented compatibility gap;
it does not assert that an undocumented/private vendor feature cannot exist.
Independent Barron's verification remains unproven; prior passage remains
human-assisted. Production collection mechanism and cadence remain Andrew's
decision. No production code was changed for an unsupported call.

## Inbox 23033

Read the exact root-level notification from `2.0.0_SA_COO~W`, dated
20260915T054428Z. It relays Andrew's verbatim instruction:

> The whole sitez fabric has free egress this session

Source record: COO `ANDREW_DIRECT_20260915_0542Z_WHOLE_SITEZ_FABRIC_FREE_EGRESS_THIS_SESSION.md`
at `dfa63b6d92` (LOCAL). The message asks for no reply and preserves the
harvest cadence reservation and Barron's human-assisted provenance. Applied
as information for this live session; no additional work order inferred.

Push state: LOCAL; this seat does not push.
