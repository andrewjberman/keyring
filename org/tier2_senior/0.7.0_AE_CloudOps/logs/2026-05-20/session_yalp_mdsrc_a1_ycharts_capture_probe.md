# AE 0.7.0 Session Log -- 2026-05-20 -- YALP_MDSRC.A1: YCharts headless-capture WAF probe

**Agent:** 0.7.0_AE_CloudOps (base lane)
**Trigger:** /loop watchdog cadence -- A1 unblocked when DS 0.1.0 cleared the seat
**Status:** YALP_MDSRC.A1 COMPLETE -- probe brief shipped.

---

## TL;DR

YALP_MDSRC.A1 = the YCharts headless-capture WAF probe (my own WS-4 design doc S6 recommended
it). Determines empirically whether the AWS WAF JS-challenge clears headless (Branch A) or
needs attended capture (Branch B), and measures the session-cookie TTLs for the WS-4 cron.

Verdict: **Branch A VIABLE** -- headless Chromium acquired a valid `aws-waf-token` on a YCharts
app page, no challenge interstitial, no block. Deliverable:
`docs/briefs/mdsrc-ycharts-capture-probe-20260520.md`.

## 1. Seat coordination

A1's fresh login/probe creates a YCharts session that, under the single-concurrent-session
constraint (WS-1 Finding 2), would evict any live session. COO flagged DS 0.1.0's ~5h YCharts
recon window; I MCP'd DS 0.1.0 for an explicit seat-clear -- they confirmed CLEAR (recon + A2
spec + S5COMM all RAVC4-closed, no follow-up probing). Ran A1 after that clear.

## 2. The probe -- a Playwright-under-bun transport blocker, worked around

Playwright's own browser transports both HANG under `bun` on this host:
- `chromium.launch()` (pipe transport) -- timed out at 180s launching chrome-headless-shell;
  retried with the full chromium-1223 chrome.exe + `--no-sandbox` -- timed out at 60s.
- `chromium.connectOverCDP()` (ws transport) -- retrieved the WebSocket URL then hung on the
  `ws connecting` handshake (30s timeout).

Root cause: there is no real Node runtime on this host -- `which node` resolves to a
`bun`-node shim (`AppData/Local/Temp/bun-node-*/node.exe`). Playwright's bundled `ws` CDP
client does not complete the handshake under bun's node-compat.

Worked around it: launched `chrome.exe` separately (`--headless=new
--remote-debugging-port=9222 --no-sandbox --user-data-dir=.runtmp/a1_chrome_profile`), then
drove it with **raw CDP over bun's native `WebSocket`** (`Page.enable` / `Network.enable` /
`Runtime.evaluate` / `Network.getAllCookies`). bun's native WebSocket completes the CDP
handshake fine; only Playwright's bundled `ws` hangs. Probe scripts are throwaway, in
`.runtmp/`, not committed.

## 3. Results

Three URLs probed headless:

| URL | awswaf SDK | aws-waf-token acquired | challenge/block | rendered |
|---|---|---|---|---|
| `/account/login/` | no | no | no | yes (real login form) |
| `/` (homepage) | no | no | no | yes |
| `/dashboard/` | YES | **YES** | no | yes |

**AC1 -- Branch A VIABLE.** The awswaf SDK engages on YCharts app pages (`/dashboard/`), not
the login page or homepage. On `/dashboard/` headless Chromium ran the challenge JS and
acquired a valid `aws-waf-token` -- no interstitial, no block. The WAF challenge is solvable
headless.

**AC2 -- cookie TTLs:**
- `aws-waf-token`: expiry epoch 1779671348 = 2026-05-25T01:09:08Z; acquired ~2026-05-21T01:09Z
  -> TTL ~96h (4 days).
- `ycsessionid`: NO `Max-Age`, NO `expires` (HAR Set-Cookie + CDP `expires:-1`) -- pure
  session cookie; server-side `SESSION_COOKIE_AGE` governs, not client-visible.
- `csrftoken`: `Max-Age=31449600` (~1yr).
- Cron implication: WS-4's daily pre-emptive capture sits inside the ~96h aws-waf-token TTL
  (4x headroom); `ycsessionid` having no client TTL hardens the WS-4 Q2 conclusion that the
  freshness gate must be the active probe, not a stored timestamp. No WS-4 cadence change
  needed.

## 4. Carry-forward to TO-C1

(Detailed in the brief Section 4.) Branch A confirmed; the production capture mechanism needs
a real Node runtime (or the raw-CDP approach) -- bun+Playwright does not work here; the
capture script must hit an app page to trigger the awswaf SDK; `ycharts/credentials` holds a
cookie bundle not username/password.

## Compiler Tools

| Phase | Tool | Result |
|---|---|---|
| 1/2/3 | (none) | Documented-none per the TO mandate + PRD Section 10 -- YCharts is external, not comp-graph-modeled; the probe is throwaway test code, not a pipeline script. Evidence base is the live headless CDP probe + the captured HAR. No production code committed. |

## Current State

| Item | Status |
|---|---|
| YALP_MDSRC.A1 | COMPLETE -- Branch A viable; probe brief shipped; RAVC2 to COO + CC CTO |
| YALP_MDSRC.004 / .006 | COMPLETE + accepted earlier this session |
| ADVI_INFALM.001 / ADVI_INFGRO.009 P2 | COMPLETE + closed earlier this session |
| AE queue | empty -- no pending TOs |

## Next Steps

1. TO-C1 (YCharts credential pipeline) -- if Q1 resolves to session-scrape, this is AE-lane;
   it consumes the A1 Branch-A verdict + the carry-forward notes (real-Node runtime, app-page
   WAF trigger, credential-format reconciliation).
2. No open AE work pending; /loop watchdog continues.

## Commits this session (A1 portion)

| Commit | Scope |
|---|---|
| (this commit) | YALP_MDSRC.A1 -- capture-probe brief + TO complete + session log |
