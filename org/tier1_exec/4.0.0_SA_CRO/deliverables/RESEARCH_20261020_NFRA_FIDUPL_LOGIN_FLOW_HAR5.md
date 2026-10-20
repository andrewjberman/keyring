# RESEARCH 2026-10-20 -- NFRA_FIDUPL: the current login flow (HAR 5 + screenshots), the 403 cause, the OTP route

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Supersedes** the login steps in `RESEARCH_20261020_NFRA_FIDUPL_LOGIN_DOM_FROM_HAR2.md`.
**Sources:** Andrew's fresh working sign-in `wealthcentral.advisorchannel.com5.har` (off git) and his five sequential screenshots,
2026-10-20 ~12:23 ET. Names, counts, length classes, statuses only; no values, cookies-content or tokens.

## 1. The current flow, measured (5 steps)

1. **Login** (`/auth/login`): Username (pre-filled, `#userInput`), Password (`#passwordInput`), **Log in** button.
2. **Verify interstitial** -- heading "To verify it's you, we'll send a temporary code to your phone", shows **one** number,
   `(XXX) XXX-3066` (the Quo line the box reads), and **two buttons: "Text me the code" and "Call me with the code"**, plus "Try
   another way" and "Cancel". **There is NO number picker** -- the Quo number is the only number on file. The cell clicks **"Text me
   the code"**.
3. **Code entry** -- "Enter the code we just sent to your phone", "We sent the code to (XXX) XXX-3066", a Security code field, **Submit**,
   Resend code.
4. **Submit the Quo code** -> lands on the Home Experience ("Good afternoon, Andrew", Book of Business $1.563B, 4,962 accounts).

**This corrects the HAR-2-derived factor page.** It is not a `bwc-radio-group` + "Generate code". It is two buttons. The signin cell's
factor step must click the **"Text me the code"** button (text match), then fill the Quo code.

## 2. The API calls behind it (ecaap)

- Password: POST `/user/factor/password/authentication` (body `username`, `password`) -> **200** here.
- Factor state: GET `/user/factor/otp/state` -> 200.
- **"Text me the code"** -> POST `/user/factor/otp/sms/authentication` (body `phone`, `template`) -> 200. **This sends the SMS to the
  ...3066 Quo line** (the only number), so the box then reads it via the Quo API.
- Code submit -> PUT `/user/factor/otp/sms/authentication` (body `securityCode`) -> 200.
- Then `/ssc/platform-authorization/api/v2/authorize` and `/container/home`.

## 3. Why the box 403s at the password POST -- it is a device-trust verdict

The working password POST carries the cookie **`ATT`** (plus `ATCTO`, the Akamai `_abck`/`bm_*` set, and the Adobe analytics set).
`ATT` is the device/session trust token. It is earned by the **Fidelity device-fingerprint flow**: HAR 5 shows **~40 GET calls to
`cfa.fidelity.com/-PE7DGk...` (204)** firing before the password POST, alongside `online-metrix.net` (ThreatMetrix). Andrew's real
browser passes that fingerprint, gets a trusted `ATT`, and the password POST returns 200.

The box (attempt 6) runs the same `cfa.fidelity` beacons (its trace shows them), sends the same header names and body keys, and
redirect-info now passes -- but the password endpoint returns **403 "Not Authorized"**. With the credential confirmed good by Andrew's
hand sign-in, the remaining difference is the **device verdict**: a headless browser on an AWS datacenter IP is scored untrusted, so its
`ATT` is not honoured at the authentication step. The earlier landing check (redirect-info) is more lenient than the password check.

**Confidence: high that this is device-trust, not credential or a missing header name** -- credential verified, request structure
matches, the discriminator is the `ATT`/fingerprint verdict.

## 4. REC (fork a/b/c, revisited with this evidence)

1. **Headed real browser + persistent profile on the box (the estate pattern), FIRST.** Run a real headed Chrome (not headless) with a
   persisted user-data-dir, so the `cfa.fidelity` fingerprint and `ATT` behave as a normal browser's. This is how the Orion inf-exporter
   and the BD boxes pass their anti-automation. Cheapest change that targets the actual cause.
2. **If still flagged, non-datacenter egress (fork b).** The AWS datacenter IP is a large part of the risk score; the BD 49F box used a
   residential proxy for the same class. Combine with (1).
3. **A hand-seed from Andrew's own machine (fork c) likely does NOT transfer.** `ATT` is bound to the device fingerprint and IP, so
   copying Andrew's cookies to the box will not carry trust. A hand sign-in done **on the box's own browser profile** (via a remote
   session to the Linux box) could seed the profile, but the box is Linux and the device layer probes RDP/VNC -- so (1)+(2) are cleaner.

**Fastest path: switch the sign-in to a headed real browser with a persistent profile (1); if the password POST still 403s, add
non-datacenter egress (2).** Neither needs Andrew.

## 5. Not measured

- Whether a headed profile alone clears the verdict without egress change (the next box run settles it).
- The `ATT` value or the fingerprint payload (never read).
