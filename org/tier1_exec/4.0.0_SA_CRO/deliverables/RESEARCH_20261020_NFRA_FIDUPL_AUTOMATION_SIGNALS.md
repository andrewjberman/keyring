# RESEARCH 2026-10-20 -- NFRA_FIDUPL: Playwright-launch automation signals, and the "Certified Browser" finding

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 1.0.0_SA_CTO~DELL1 msg 8818 (two parallel asks).
**Sources:** Andrew's HARs (off git) for the Certified-Browser check; general browser-automation facts for the signal list (marked as
such). No values.

## A. Certified Browser enrollment -- there is NO enrollment flow to capture

- No HAR (1, 2, 4, 5) contains a device-enrollment / "certified browser" / trusted-device request. The only `certif*` URL hits are
  `entitlements.json` (the word appears in an entitlement name), not an enrollment call.
- The "Certified Browser" on the login page is a **documentation link** ("Please review our Certified Browser document for a more
  optimal experience") -- supported-browser guidance, not a device-trust enrollment.
- **Conclusion:** ATT / device trust is NOT gated behind a Certified-Browser enrollment step. There is nothing to reproduce there.
  Trust is the fingerprint + the launch-signals distinction below. This removes a suspected blocker.

## B. Automation signals a Playwright LAUNCH exposes (that a plain Chrome + CDP connect does not)

The decisive difference, matching the probe result (plain-Chrome ATT passed; Playwright-minted ATT refused):

| Signal | Playwright-LAUNCHED Chromium | Plain google-chrome, user/OS-launched, connected over CDP |
|---|---|---|
| **`navigator.webdriver`** | **`true`** (set by the `--enable-automation` launch flag) | **`false`** -- NOT set; connecting over `--remote-debugging-port` does not set it |
| `--enable-automation` flag + "controlled by automated test software" infobar | present | absent |
| Browser build / UA | Chromium-for-Testing: UA says "Chromium", `userAgentData.brands` lists Chromium/Not;A=Brand, no Google-proprietary codecs/Widevine | real **Google Chrome**: UA "Google Chrome", full brands, codecs |
| `navigator.plugins` / PDF viewer, `navigator.languages` | sparse/default in the testing build | normal Chrome set |
| `window.chrome` runtime object | reduced | full |
| Launch flags (`--no-sandbox`, `--disable-blink-features=AutomationControlled`, etc.) | a known Playwright default set | only what the unit sets |
| (headless only) UA "HeadlessChrome", zero outerWidth/Height, SwiftShader GPU | if headless | n/a (headful) |

**The big one is `navigator.webdriver`.** Playwright *launching* Chromium flips it true; *connecting over CDP* to a plain Chrome the OS
launched leaves it false. ThreatMetrix/cfa read `navigator.webdriver` as a primary bot tell, so an ATT minted in a webdriver=true
browser is scored untrusted -- exactly the refusal pattern.

**Why Track B fixes it:** plain `google-chrome` launched by the CloudOps unit (no `--enable-automation`), driven by the dell1 agent over
CDP, has `navigator.webdriver=false` and a real-Chrome fingerprint. The ATT it mints should score trusted.

## C. The control to record (CTO asked): `navigator.webdriver` boolean in both browsers

- In the failing Track A run (Playwright-launched): expect `navigator.webdriver === true`.
- In the Track B unit (plain google-chrome + CDP): expect `navigator.webdriver === false`.
- Also worth a boolean each: `--enable-automation` present (infobar), and UA contains "HeadlessChrome" (should be false in both headful).

If Track B shows `webdriver=false` and still 403s, the discriminator is deeper than the launch signal (the fingerprint itself or the
datacenter IP), and the paired hand-sign-in + Track-B-within-5-min test the CTO named is the next discriminator.

## Not measured

- The exact Playwright default flag set on this box's build (read it off the running unit's `chrome://version` / process args).
- Whether `navigator.webdriver` alone flips the verdict (Track B's result settles it).
