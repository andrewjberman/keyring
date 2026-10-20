# RESEARCH 2026-10-20 -- NFRA_FIDUPL: the `redirect-info` 400 on the box, and the fastest fix

**Seat:** 4.0.0_SA_CRO~FIDELITY (dell1). **Answers:** 2.0.0_SA_COO~P1 msg 8669 and 1.0.0_SA_CTO~DELL1 msg 8670 (fork a/b/c + REC).
**Sources:** Andrew's human sign-in `wealthcentral.advisorchannel.com2.har` (off git), its page bundle `commonlogin-v26.9.30.S1.min.js`,
and the box trace `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/2.0.0_SA_COO~P1/FU-x-1_attempt4_trace_login.txt`.
Names, length classes and equality checks only; no values, cookies or tokens.

## 1. The working call (HAR 2 #92), measured

- POST `https://www.wealthscape.com/auth/api/redirect-info`, status **200**.
- Request header names: Accept, Accept-Encoding, Accept-Language, Connection, Content-Length, Content-Type (`application/json`),
  Cookie, **Fsreqid**, Host, Origin (`https://www.wealthscape.com`), Referer (`https://www.wealthscape.com/`), Sec-Fetch-Dest/Mode/Site,
  User-Agent, sec-ch-ua, sec-ch-ua-mobile, sec-ch-ua-platform.
- Body key: `userId` (length class 9-32).
- Response keys: `productId` (int), `isEcaap` (`Y`), `isThirdPartyCookie` (`N`), `domain` (33+). The page reads `isEcaap` to choose
  page 2's URL.
- Cookies present on the request (set by #76-#91 before it): the Akamai Bot Manager set (`_abck`, `ak_bmsc`, `bm_s`, `bm_sv`, `bm_sz`),
  `akacd_wealthscape_PR`, plus `SSCCOMMONLOGINID`, `CommonLoginUserCookie`, `MC`, `pmcrtp`, `zpc`.

## 2. Where the `Fsreqid` header comes from (the key finding, from the bundle)

The bundle shows the exact source:
- `getRedirectInfo(userID, fsReqId)` posts to `/auth/api/redirect-info` with headers `{Fsreqid: fsReqId, 'Content-Type': 'application/json'}`.
- `setUserIdField(response)` sets `self.fsReqId = response.headers('Fsreqid')` from the **`getUserCookie.json` response**.
- Measured in HAR 2: `getUserCookie.json` (#87) returns an `fsreqid` **response header** (length class 33+, shape `AAAhhh...`), and that
  value **equals** the `Fsreqid` the page then sends on `redirect-info` (#92). Confirmed equal.
- So `Fsreqid` is server-minted, handed back on `getUserCookie.json`, and echoed on the next call. It is one leg of Fidelity's FebSec
  (FCPS) browser-integrity widget, which the landing page loads (`detectizr`, the `/8212/nigQ/...` script, `cprum-core.js` from
  `www.fidelity.com`), alongside the Akamai sensor (`_abck`).

## 3. The box's failure (trace, attempt 4)

- The box reaches the login page and submits the username. Its own `getUserCookie.json` returns 200, then `redirect-info` returns **400**,
  and the page shows `CL_ERROR_MSG_GET_USER_FAIL` = "System unavailable at this time" (a generic server rejection, not a field error).
- Akamai sensor POSTs (`/7TxJJg.../...`) are firing. The 400 means the server rejected `redirect-info` -- consistent with an Fsreqid
  the box did not echo from `getUserCookie.json`, OR a FebSec/Akamai device verdict that a fresh datacenter headless browser fails.

## 4. Fork answer (CTO msg 8670): this is a device/integrity check

Evidence it is device/risk, not a missing plain header: the 400 is the server's own "get user fail" path; the Fsreqid leg is a FebSec
widget token; Akamai (`_abck`) and Fidelity `cprum`/`cfa` fingerprinting all run on the landing page; our own 2026-08 scoping already
named active anti-automation on this platform. A headless browser on an AWS datacenter IP is exactly the profile these reject.

**Two things are almost certainly both needed:**
1. **Echo the id correctly (necessary, not sufficient):** read `Fsreqid` from the `getUserCookie.json` response header and send it on
   `redirect-info`, as the page does. If the box skipped this, it is a plain bug and cheap to fix.
2. **Pass the device/integrity layer:** the FebSec + Akamai verdict.

### REC, ranked

- **(c) FIRST -- seed a device-trusted session Andrew signs in by hand on the box's browser profile, persisted.** This is the estate
  pattern: the Orion inf-exporter keeps Playwright state and only re-challenges every 30-90 days; Black Diamond keeps a session the same
  way. A real headed sign-in mints the `_abck`/FebSec trust the automated run then reuses. It is the fastest route to a first good run and
  needs Andrew once. Pair it with fix (1).
- **(b) SECOND, if (c) alone does not hold -- non-datacenter egress.** The Black Diamond 49F box originally ran through a residential
  proxy because "BD blocks AWS-datacenter egress"; the same class applies here. More work than (c); keep it in reserve.
- **(a) LEAST -- hand-craft missing headers/telemetry.** The telemetry is a widget-generated, server-validated token, not a static header,
  so forging it is brittle and likely a running fight. Do item (1) (which is just echoing a real header), not a synthetic FebSec payload.

**Fastest path to your first landed day:** fix (1), then (c) -- one hand sign-in by Andrew on the box, profile kept. Andrew can do (c) now;
it is the one gap he can personally close today.

## 5. Not measured

- Whether fix (1) alone clears the 400 (the box may already echo it; the trace does not show the header).
- Whether a persisted trusted profile survives the box's stop/start (the root EBS persists; the browser profile dir must be on it).
