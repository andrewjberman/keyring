# AMGT -- THE ACCEPTANCE SURFACE for Andrew's completion test

**`/self-drive AMGT` tick 1, `1.0.0_SA_CTO~Z`, 2026-09-23.** Arming record @`7a939040d5`.

> **HIS TEST:** *"testing frontend (localhost:5174) and actually displaying relevant data for a
> security end to end on all functions."*

**This record converts that sentence into a MEASURED checklist with denominators.** Every figure below
is read from the repo, not recalled.

⛔ **AMENDED BEFORE ITS FIRST COMMIT.** The draft of this file carried a THIRD prerequisite that does
not exist -- a missing dev proxy -- and section 6 records why the error was invisible. It is corrected
in place rather than committed and superseded, because it was never published.

## 1. WHAT "ALL FUNCTIONS" IS -- MEASURED, NOT GUESSED

**ROUTE:** `/security-analysis` and `/security-analysis/:securityKey` (`portal/src/App.tsx`).

**THE UI SURFACE -- 5 TABS + 1 PERSISTENT PANEL:**
`ExecManagementTab` · `ModelTab` · `PeersTab` · `PostureTab` · `ThesisTab`, plus `LeadPanel`
(*"PERSISTENT: rendered once by `SecurityAnalysis.tsx`, above the tab bar"*).

**THE DATA SURFACE -- 11 EXPORTED API FUNCTIONS** (`portal/src/api/endpoints/amgt-lead-panel.ts`,
170 lines): `getLeadPanelRankings` · `getRankTimeSeries` · `getStarred` · `setStarred` ·
`requestRefresh` · `getSecurityOverlay` · `getThesisBundle` · `getPeerSet` · `getCoverageSet` ·
`printPackPath` · `requestPrintPack`.

⭐ **So "all functions" has a denominator: 6 UI surfaces backed by 11 API functions.** A render that
shows one tab with data satisfies **1 of 6**, and the test is not met by a page that merely loads.

## 2. ⛔ TWO PREREQUISITES -- AND THE SECOND WAS NAMED BY NOBODY

| # | prerequisite | state |
|---|---|---|
| **1** | **the served-output repair DEPLOYED.** Until then the API serves 179 sentences the ratified clause withholds, so a render displays inadmissible content | AUTHORIZED, **not ACTIVATED** -- needs a direct operator instruction in `2.0.0_SA_COO~Z`'s own session |
| **2** | ⛔ **AN IDENTITY WITH DEV **AND** ADMIN ENTITLEMENTS.** Both routes are wrapped `<ProtectedRoute requireDev requireAdmin>`, and the nav entry carries `requiresDev: true, requiresAdmin: true` | ⚠ **UNMEASURED AND UNOWNED** |

⭐ **Prerequisite 2 matters because of how it FAILS: `ProtectedRoute.tsx:105`/`:115` SILENTLY REDIRECT
an identity missing either claim to `/market`.** **So the tester sees a WORKING PAGE and never learns
they never reached the route** -- the failure does not announce itself as a failure at all. That is a
worse shape than a blank page, and it is why this row is stated as a prerequisite rather than a risk.

## 3. ⭐ THE INSTRUMENT ALREADY EXISTS -- AND ITS OWN DOCSTRING SAYS WHY IT IS NOT ENOUGH

**`portal/src/pages/SecurityAnalysis/__rendercheck__/renderCheck.tsx`** -- an **AMGT-re-1 deliverable**,
*"THE RENDER CHECK, ON THE REAL ROUTE AND THE REAL PRINT ACTION."* It mounts the real route, the real
`ProtectedRoute`, the real `AuthContext`, the real `QueryClientProvider` and the real
`<SecurityAnalysis />`, and drives `requestPrintPack()` -- the exact function the button's `onClick`
calls. ⭐ **No stand-in for anything.**

⛔ **But it names its own instrument, per Rule 22, and that is the finding:**

> *"It is a SERVER RENDER, `react-dom/server`'s `renderToStaticMarkup` ... **IT DOES NOT establish:
> anything that needs a live DOM (a real pointer click, an effect, a measured layout). No DOM
> implementation is installed in this portal"*

⛔⛔ **DATA FETCHING HAPPENS IN EFFECTS. A SERVER RENDER RUNS NO EFFECTS. So this instrument proves
WIRING and CANNOT PROVE "ACTUALLY DISPLAYING RELEVANT DATA" -- which is precisely the phrase Andrew's
test turns on.**

⭐ **The estate has already been burned one rung below this:** the docstring records that `rd-8`'s
render check was REFUSED by its adjudicator for rendering *"fixture components and a copied trigger
button rather than the actual route and action."* ⭐ **`re-1` fixed that by mounting the real route.
Andrew's bar is the NEXT rung: the real route, with real data, in a live browser.**

**CONSEQUENCE: the completion test needs a LIVE-BROWSER instrument** (a real DOM, effects running,
network in flight) **against `localhost:5174`.** The existing SSR harness remains valuable and is
NOT replaced -- it is the wiring control beneath the live test, and a live failure is diagnosed
faster when the SSR check is green.

## 4. THE PATH, WITH ITS ORDER

```
COO~Z half (needs the session-level sentence) -> CVO review -> deploy
                                                                  \
                                                                   -> live render at :5174
                                                                  /
  an identity holding dev + admin ------------------------------->
                                                -> grade 6 UI surfaces x real data -> DONE
```

⛔ **Both prerequisites are independent and both are required.** The repair without the entitlements
renders nothing; the entitlements without the repair render inadmissible content. **And the two
failures do NOT look alike** -- a missing entitlement redirects to a working `/market` page, which is
the one symptom a tester would not read as a failure.

## 5. HOW TO REACH THE PORT -- ONE FORM ONLY

The port is **5174** on Andrew's word, and only ONE invocation reaches it:

```
bun run dev:live --port 5174
```

- `dev:live` = `node scripts/dev-live.mjs`. `dev-live.mjs:12` defaults to 5173 and accepts 5174 only
  as the exact two-token form `--port 5174` (`:9-11` throws on any other shape); `:28` sets
  `strictPort: true`, so a busy port fails LOUDLY with no silent fallback.
- `CLAUDE.md`'s `bun run dev --port 5175` names the OTHER script (plain vite, no forced same-origin
  env). `vite.config.ts:40`'s *"Port 5173 discipline"* is a COMMENT in a `server` block that declares
  no `port` key and no `strictPort` -- **it binds nothing.**
- All three numbers are a DOC DEFECT to reconcile, not competing instructions.

⭐ **AND `dev-live.mjs` IS NOT A STANDALONE PROXY TABLE -- IT MERGES `vite.config.ts`.** `:1` imports
`createServer` from `vite`; `:23` calls it with `configLoader: 'runner'`; `:29-30` says so in its own
words (*"Override the remaining direct-API-Gateway targets in the shared config. The rest of that
config (HMR, aliases, rewrites, other proxies) is retained."*). Measured at EXERCISED by
`0.1.0_DE_MarketIntelligence` (msg 25011, 2026-09-23, @`10141b6d`) with the control that
discriminates it: the `/api/auth` -> `/auth` rewrite exists ONLY in `vite.config.ts:98` and
`dev-live.mjs` declares no rewrite, yet `POST /api/auth/login` through `dev:live` returns the auth
Lambda's `{"error":"Email and password are required"}` 400 while CloudFront REFUSES that same path
with a 403 -- so the `vite.config.ts` rewrite fired inside `dev:live`.

⛔ **CONSEQUENCE FOR THE NEXT SEAT: `vite.config.ts` IS load-bearing for the `:5174` surface.** A seat
acting on *"dev:live is insulated from vite.config.ts"* could delete or retarget an entry there and
break the completion-test route.

## 6. ⛔ THE RETIRED PREREQUISITE, KEPT BECAUSE OF HOW IT FAILED

The draft asserted a third prerequisite: **a missing `/api/scoped/amgt` DEV PROXY**, evidenced as
*"`amgt` occurrences in `portal/vite.config.ts`: ZERO"*. **The number was correct. The conclusion was
false.**

- The `:5174` route is `portal/scripts/dev-live.mjs`, and **its proxy table ends with a CATCH-ALL
  `/api` entry**, so `/api/scoped/amgt/*` is routed without ever naming `amgt`.
- `0.1.0_DE_MarketIntelligence` corroborated this on a DIFFERENT instrument -- an EXERCISED negative
  control, pre-change config on `:5176` against edited config on `:5174`, identical 401 bodies on
  both; the *"Invalid or expired token"* body on the PRE-CHANGE server proves a bogus bearer reached
  Lambda@Edge **through the catch-all**, so the catch-all forwards `Authorization` too.
- That seat was stood down (msg 25003), its commit is parked on local branch
  `amgt-dev-proxy-0.1.0_DE` (portal `a9460d1a`), portal DEV is UNTOUCHED at `b3d5f59b`, and the
  portal working tree is back at `10141b6d` with `vite.config.ts` byte-identical to `origin/DEV`.
  **Nothing was deployed and nothing on a shared branch needs reverting.**

⛔ **THE LESSON, and it cost an hour plus a spawned seat: A NAME CENSUS ANSWERS "IS THIS NAME
LISTED", NEVER "IS THIS PATH COVERED".** A zero occurrence count is a true statement about a
vocabulary and says nothing about routing, because a catch-all covers by SHAPE, not by name. ⭐ **The
discriminator is one request, not one grep** -- and it was available the whole time.
**COST: one exercised request against the running dev server.** **NON-APPLICATION: a proxy table with
no catch-all and no regex entry, where the name census IS the coverage question.**

## 7. WHAT THIS RECORD DOES NOT DO

⛔ Authorizes no deploy, no cutover, no grant, no entitlement change, no vendor call. **It measures
the surface and names what is missing.**

-- `1.0.0_SA_CTO~Z`. Commits LOCAL; push owed by `0.0.0_AB_MSTR~Z`.
