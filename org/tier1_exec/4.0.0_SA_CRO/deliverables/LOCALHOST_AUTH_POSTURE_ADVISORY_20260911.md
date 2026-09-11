# Localhost authentication: retain the CloudFront entry restriction and make development use it reliably

**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Date:** 2026-09-11, observations approximately 10:25–10:33 EDT
**Authority:** Andrew's investigation/advisory request in `ANDREW_DIRECT_20260911_LOCALHOST_AUTH_POSTURE_ADVISORY.md` at `b3a3187c7c`.
**Status:** Advisory delivered. No application, proxy, authentication, secret, or infrastructure changes made by this investigation.

## Finding

The original **Forbidden** is the expected rejection of a development client calling the auth API Gateway directly. NFRA_OPSEC202609 OP-s-3 requires actual auth requests to pass through CloudFront, which injects the origin-verification header. The fix is to put the development client through that existing path.

Last night's fix **did happen**, but it changed a gitignored environment file on one checkout. The underlying shared default was left in place. A fresh clone or worktree without that local file still falls back to the direct gateway.

The later **Failed to fetch** is a different observation. At approximately 10:25 EDT this desktop had no listener on 5173, and curl could not connect. A new Vite process subsequently appeared, serving the `d13-visual-elevation` worktree on IPv6 loopback port 5173. A fresh, isolated browser then exercised the live form successfully through the local proxy, receiving the expected credential rejection for a nonexistent account. A restart interruption is consistent with the changed banner, but the original failing browser request was not captured; its precise cause is not proven.

## The record of last night's fix

`org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-09-11/portal_localhost_auth_403_origin_gate.md`, committed at `85e4d54232038b4e58fd518abecf85838e9597f7` at 02:10:17 EDT, documents:

1. Direct auth calls returned `403 {"error":"Forbidden"}` before credential validation.
2. CloudFront and the already-existing Vite `/auth` proxy reached credential validation.
3. The operator's checkout received `VITE_AUTH_API_URL=` in `portal/.env.local`, and Vite was restarted.
4. The browser then posted to `http://localhost:5173/auth/login` and received the expected 401 for a nonexistent account.
5. Moving the setting into tracked development defaults remained **recommended, not applied**.

The `/auth` proxy itself predates OP-s-3: portal commit `89ecfd89` added it on August 31 for D12 MFA/session parity. The September 1 DE3 browser log records a real MFA/session exercise at that historical version. That historical positive test is not a current authenticated-session test.

History search included `comp-find` over 105,659 inbox files for `localhost` (310 matching lines), scoped source searches, and a filesystem search of executive/senior records. The incident was in the DT log; this investigation did not find a separate September 10/11 inbox handoff about its localhost remedy, excluding its own broadcasts. An unsupported glob scope and absent log directories produced zero-file searches; those zeros were not used as absence evidence.

## Current measurements and their limits

| Probe | Observed result | Meaning |
|---|---|---|
| Main checkout `.env.local` | Empty `VITE_AUTH_API_URL`; last write 01:55:45 EDT | Last night's local setting remains present here. |
| Current worktree `.env.local` | Empty `VITE_AUTH_API_URL`; last write 10:21:34 EDT | The running worktree also now carries a local setting. Its author/cause was not established. |
| Port 5173 at about 10:25 EDT | No listener; curl connection failure | There was a local availability gap on this desktop. |
| New process | PID 27556, created 10:25:50 EDT; Vite executable under `.worktrees/d13-visual-elevation/portal/`; listener `::1:5173` | A new serving process appeared during investigation. No process was started or stopped by this seat. |
| Served AuthContext module | `MODE=development`, `VITE_AUTH_API_URL=""` | Current served code uses same-origin auth. This is stronger than reading a different checkout's env file. |
| Direct gateway `OPTIONS /auth/login`, localhost origin | 200; exact localhost ACAO and credentials allowed | Preflight works; it does not prove that the subsequent POST clears the origin gate. |
| CloudFront `OPTIONS /auth/login`, same headers | 200 | Preflight also works through the intended entry. |
| Direct gateway `POST /auth/login`, body `{}` | 403, `{"error":"Forbidden"}` | The origin gate refuses the direct route before field validation. |
| CloudFront `POST /auth/login`, body `{}` | 400, `{"error":"Email and password are required"}` | Request passed the origin gate and reached input validation. |
| Fresh Playwright/Edge browser, live localhost login form, nonexistent `.invalid` account | `POST http://localhost:5173/auth/login` 401; alert `Invalid email or password` | Current browser path reaches the credential check; neither reported banner reproduced. |
| Same fresh browser, no session | `/auth/refresh` 401 | Correct refusal without a refresh cookie; **not** proof of successful session persistence. |

The browser used a new context and a deliberately nonexistent account, never Andrew's credentials or existing browser session. No authenticated dashboard/data access, MFA delivery, refresh success, or tenant-isolation claim is made. The default Playwright Chromium executable was unavailable; installed Edge was used successfully. The worktree portal HEAD observed was `748384e4641dbcea998e652f04ae29e21d112ae0`.

## Recommended implementation

### 1. Make same-origin auth the default in every checkout

- Add `VITE_AUTH_API_URL=` to tracked `portal/.env.development`, and align `.env.example` with that default.
- Replace the hardcoded execute-api fallback in **both** `portal/src/contexts/AuthContext.tsx:76` and `portal/src/api/api-client.ts:17` with an empty/same-origin default. Prefer one shared resolver so login, MFA, refresh, and API retry do not diverge.
- Keep the existing `/auth` proxy to the approved CloudFront distribution. Existing `/api/auth` compatibility can remain while its callers are enumerated.
- Detect a developer override pointing auth back to the direct gateway at startup and report the offending **configuration key and destination**, without exposing secrets or waiting for an opaque login failure.
- Restart the exact serving process after env changes, then verify the browser's posted URL. Check shell-level and mode-specific overrides as well as `.env.local`.

This closes the fresh-worktree failure as well as the specific one-line omission. The main checkout currently works only because an ignored file supplies the otherwise-missing setting.

### 2. Align the rest of the development proxy with the protected entry

The inspected `portal/vite.config.ts` contains five direct-gateway proxy entries:

| Local prefix | Current direct target |
|---|---|
| `/api/scoped/partners` | Portal API Gateway `7k3ed8px20` |
| `/api/partners` | Portal API Gateway `7k3ed8px20` |
| `/api/scoped/data-refresh` | Portal API Gateway `7k3ed8px20` |
| `/api/scoped/security-scanner` | Portal API Gateway `7k3ed8px20` |
| `/api/private/portfolio` | Portfolio API Gateway `f61h681z9g`, stage `/prod` |

Route these through their existing CloudFront behaviors, preserving prefix precedence and required path/stage semantics. `comp-routes behaviors` reports matching declared CloudFront behaviors; this is **source/desired-plane evidence**, not a live-distribution or authorized-response proof. Verify the actual deployed mappings before changing each route. A successful login alone cannot establish that all dashboard requests use the protected entry.

Keep these invariants: origin verification at the backend, JWT/MFA and firm authorization, existing cookie attributes, TLS verification, and CloudFront's ownership of the origin secret. The development proxy forwards the user's normal request; it does not mint an identity or acquire the origin secret. Keep workstation access loopback-only unless an explicit LAN-development requirement is approved. Avoid wildcard CORS/host settings as a remedy.

### 3. Make local availability and failure reporting observable

- Set actual `server.port: 5173` and `server.strictPort: true`; the current file has a port-discipline comment but neither option, and `package.json` currently runs bare `vite`.
- Have the canonical dev launch report the serving checkout, PID, port, mode, and sanitized effective auth destination. It must fail explicitly on a port conflict and check listener readiness before announcing a usable URL.
- Preserve actionable proxy/server logs. Distinguish a transport failure from a returned HTTP rejection in the development UI; retain the backend's deliberately generic security responses.
- Verify server lifetime when its launching terminal/agent ends. Do not treat a past detached launch or a green historical log as proof that a listener exists now.

This is a bounded improvement to the existing dev workflow, not a new continuously running monitor.

## Acceptance evidence before calling the remedy complete

1. Start a fresh checkout/worktree **without `.env.local`**: the served login/MFA/refresh URLs must remain same-origin. Exercise a stale direct-gateway override and verify a clear configuration error.
2. Repeat the negative controls: direct gateway remains 403; CloudFront/local proxy reaches field/credential validation; deliberately wrong origin proof remains rejected in the established OP-s-3 battery.
3. With an approved test identity, exercise login → MFA → dashboard → full reload/refresh → logout. Confirm cookie attributes and that a partial MFA challenge grants no session.
4. With properly scoped test identities, exercise the five migrated proxy families and negative firm/authorization cases. Observe CloudFront routing and verify response type; an SPA HTML fallback is a failure, not an API success.
5. Test occupied port, process exit/restart, fresh browser tab, and proxy upstream failure. The displayed state and startup output must agree with actual listener/request evidence.

Implementation belongs with the portal owner coordinated by CTO/COO; this advisory issues no task order. No origin-secret rotation or production policy relaxation is indicated by the measured results.

## Reference semantics checked against primary documentation

- [Vite environment loading](https://vite.dev/guide/env-and-mode): env files are read at startup; existing process env has highest priority; mode-specific files outrank generic files. This corrects last night's log's broad statement that `.env.local` overrides `.env.development`. `VITE_*` values are client-exposed and must not carry the origin secret.
- [Vite server options](https://vite.dev/config/server-options): `strictPort`, host binding, and proxy settings define the local server behavior.
- [CloudFront custom origin headers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/add-origin-custom-headers.html): CloudFront can add origin headers while the origin rejects requests missing its expected value.
- [Browser fetch behavior](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch): HTTP error responses resolve to a Response; transport/CORS failures can reject the promise. The two reported banners therefore require separate observations.

## Publication and compiler limits

Push state **LOCAL**. Last origin/CLOUD measurement during preparation: `86d2d0835fddce0f67a998376a4c096e8693a16c`, read with `git ls-remote`; this seat never pushed. The direction record is local commit `b3a3187c7c`.

`comp-which` preceded investigation; `comp-routes behaviors` supplied the desired routing map, and `comp-find` located source/history with denominators. One bare-shim regex containing `|` failed shell parsing; subsequent compiler searches used literal patterns, with scoped `rg --no-ignore` for ignored inbox/log files. Compiler coverage did not establish runtime health; bounded HTTP probes and the fresh browser did.
