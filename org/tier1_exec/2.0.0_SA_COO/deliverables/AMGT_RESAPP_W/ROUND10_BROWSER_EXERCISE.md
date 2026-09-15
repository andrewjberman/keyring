# AMGT_RESAPP round 10 -- THE BROWSER HALF OF `AMGT-ri-3` (row `Z-S72`): the served route, driven by the instrument no worker holds

**By** `2.0.0_SA_COO~W`, 2026-09-15 01:3x-01:5xZ. **Graded by** `3.0.0_SA_CVO~W` as `AMGT-ri-3`'s judgment criterion AC6.
**Status:** COMPLETE on form (i) below -- Parts A and B. The deployed adapter's own response (form ii) is captured by
`AMGT-ri-4`/`ri-3` after the mount and is ADDED here when it lands; nothing in this file waits on it.

## THE INSTRUMENT, STATED PLAINLY (Rule 22: name the instrument and what it is not)

- **A real browser** (Playwright, Chromium) against **a real dev server**: vite 7.3.5 on `[::1]:5175` (this device binds
  the v6 loopback only; `127.0.0.1` is CONNREFUSED -- the reading round 9 recorded), serving the view worktree
  `C:/tmp/portal-resapp-view` moved to **`refs/drains/ri-1-portal` @ `9aef3734`**, which is `a845a8be75` (the whole
  Security Analysis page) plus `0.9.0_WK_AMGT_RESAPP~16`'s repair of the error/empty boundary. `VITE_AUTH_API_URL` empty.
- **The auth session is STUBBED AT THE BROWSER TRANSPORT.** `POST /auth/refresh` is answered by Playwright with
  `{accessToken, user: {email dev@opalcapital.com, role admin, firmId opal-capital, userType Dev, ...}}` -- the exact shape
  `AuthContext.tsx:parseClaims` parses. No credential was used, requested or stored. WHY NOT `window.__devBypass`: the bypass
  sets React state and `localStorage.accessToken` but never the api-client's `tokenIssuedAt`, so the FIRST data request runs
  the client's proactive refresh (`api-client.ts:ensureFreshToken`, token older than 10 minutes), the real edge answers 401,
  and `attemptTokenRefresh` hard-navigates to `/login` and clears the token (`api-client.ts:73-76`). Measured twice at this
  seat before the stub: `/login`, `bodyBytes 2918`, `POST /auth/refresh -> 401` on both loads.
- **Every `/api/scoped/amgt/*` response is served at the browser transport from the ADAPTER'S OWN HANDLER
  (`lib/research/api/scoped_amgt.py`, the module the Lambda vendors) RUN LOCALLY at this seat against the LIVE
  `opal-harvest-security-metrics` table and the LIVE `opal-data-harvest` bucket** -- form (i). The mount is not yet applied
  in this round (`AMGT-ri-4` lands it), so the deployed Lambda could not serve. Each response is saved beside this file as
  `adapter-local.<route>.<key>.json` with its status code, and their sha256s are printed in the session log. The adapter's
  controls fired locally: no `x-firm-id` header -> **401** `missing edge-injected X-Firm-Id`; today's partition -> **row_count 0**
  (before `ri-2`); `as_of=2026-09-12` -> **row_count 10**, the last day the deployed producer wrote.
- What is REAL: the router, `ProtectedRoute`, `AuthContext`, react-query (retry 2, staleTime 5 min), `LeadPanel`,
  `RankedList`, `StarredList`, `SecurityOverlay`, `ThesisTab`, the check-face badge -- the code the page ships; and the
  rows and figures, which are the live table's and the live bucket's. What is NOT: the edge, the deployed Lambda, a
  person's session. The REALIZED bar (a person seeing this through the live edge) is a person's act and is not claimed.
- **THE CACHE TRAP:** the app persists react-query to localStorage; a second load served a prior arm's payload without
  touching the transport. Every capture below follows `localStorage.clear(); sessionStorage.clear()` on `/login`, and the
  transport log beside it is the proof the request went out.

## PART A -- THE BOUNDARY DISCRIMINATES ON THE SERVED ROUTE (`ri-1`'s repair, on the route)

| arm | transport (stubbed, logged) | rendered state | `body.innerHTML` | screenshot |
|---|---|---|---|---|
| ERROR | `GET .../rankings/trending/chatter?limit=10 -> 503` **three times** (react-query's two retries, then settled) | `Read failure -- the ranked names could not be read.` / `This request did not return, so the rows the producer may have written for this combination were NOT read. Whether any rows exist for today is UNKNOWN from this screen -- nothing here is a statement about the producer. Try again, and if it keeps failing the read path itself is broken.` / `Error reported by the read:` + the 503's message. **Zero "daily job".** | **26,044 B** | `ROUND10_BROWSER_arm-error-503.png` |
| EMPTY | `-> 200` once, `{axis TRENDING_CHATTER, resolution CROSSED/MEASURED, rows [], row_count 0}` | `Served by the producer partition TRENDING_CHATTER (movement dimension: MEASURED).` / `No ranked names for TRENDING_CHATTER yet -- the daily job has not written a row for today's date.` **Zero "read failure".** | **25,768 B** | `ROUND10_BROWSER_arm-empty-200.png` |

The two states differ by the whole sentence a person reads. Negative control: the same page at `a845a8be75` rendered these
two arms byte-identical (`AMGT_RESAPP_ROUND9_CVO_RENDER_20260914_Z.json`, `error_equals_empty: true`).

## PART B -- POPULATED, NAVIGATION, MARKING (`ROUND10_BROWSER_partB.json` is the machine record)

| step | what the page did | measured |
|---|---|---|
| **Populated list** | `-> 200`, the adapter's 10 real rows for `as_of 2026-09-12` | 10 `<li>` rendered, all ten tickers on screen (`2317 TT`, `9433 JP`, `992 HK`, `ASML NA`, `BA US`, `BABA US`, `BBSE3 BZ`, `BP/ LN`, `COST US`, `Enel IM`), each `chatter 0/100 (0 mentions)` -- the honest all-zero case (the article store is empty), `Served by the producer partition` line present; **37,015 B**. `ROUND10_BROWSER_arm-populated.png` |
| **Navigation: click the ranked row `BABA US`** | the page passed `row.ticker` = `BABA US` to `/security/BABA%20US/overlay` and `/thesis`; the adapter answered `identity_status UNRESOLVED`, 0 header figures, 0 fiscal figures | overlay mode entered (list gone, head `BABA US`), **25,867 B**; the Thesis tab renders **no figures and no marker**. `ROUND10_BROWSER_arm-overlay-baba-us.png`, `ROUND10_BROWSER_arm-thesis-baba-us.png`. **FINDING, row `Z-S95`:** the producer writes Bloomberg tickers and no `security_key`; the page navigates on the ticker; the security routes resolve the canonical key. Navigation from the Lead Panel does not reach the figures. |
| **Navigation: search `BABA_US_Equity`** (the panel's own search box) | `/security/BABA_US_Equity/overlay` -> identity MEASURED, 13 header figures; `/thesis` -> 183 fiscal figures, 13 header figures, 196 check-face entries | `BABA US Equity` / `ALIBABA GROUP HOLDING-SP ADR` on screen; figures `PX_LAST`, `SALES_REV_TURN`, `IS_EPS` by fiscal year; **40 `PROVISIONAL` markers as text beside their figures** (PASS renders as a coloured icon without a text node -- the screenshot carries both); **211,179 B**. `ROUND10_BROWSER_arm-thesis-baba-us-equity.png` |

**FWD-9's marking:** each figure in the Thesis tab is rendered beside its check-face verdict (`checkFor(data.check_face, figure)`
in `ThesisTab.tsx:98/:114`), the marker being the round-4 `CheckFaceBadge`; 40 PROVISIONAL markers are visible as text on the
resolved key. **The marking is beside the figure, not beside the source evidence sentence** -- whether that meets the row's
"prove FWD9 marking beside its source evidence" is the CVO's grade, not this seat's.

## WHAT THIS RECORD SETTLES AND WHAT IT DOES NOT

Settled: the boundary discriminates on the served route (A); the assembled route renders a populated list from the producer's
real rows and the resolved key's figures with markers (B); the navigation path a person would take from a ranked row does NOT
reach the figures (B, `Z-S95`). Not settled: the live edge, the deployed Lambda (until `ri-4`), a person's session, today's
rows (until `ri-2`). Nothing was promoted, pushed, or moved; the gitlink stays `e85f6eb84f`; the view worktree is clean after
the run (`public/__exercise` staging removed).
