# POSITIONING MULTI-TENANCY — PATTERN ANALYSIS (R4), and the ONE question the spec turns on

**Author:** `1.0.0_SA_CTO~Z` · 2026-08-27 ~19:0xZ
**Discharges:** ANDREW-DIRECT ~18:5xZ **R4** (*"the patterns that govern these things need to be
deeply analyzed"*). Verbatim record: `ANDREW_DIRECT_20260827_1855Z_POSITIONING_MULTITENANT_PATTERNS.md`
@`dc18f5a855` (ON ORIGIN).
**All citations at portal `origin/DEV`.** R5 (the spec) and R6 (breakage validation) follow this;
**R5 cannot be honestly written until §4 is answered.**

---

## 1. THE ESTATE HAS **FOUR** MULTI-TENANCY PATTERNS, AT FOUR GRAINS

Measured across the 6 files that reference the firm-gating API:

| # | pattern | grain | mechanism | call sites |
|---|---|---|---|---|
| **A** | **ROUTE** | a whole page | `isPathAllowedForFirm(firmId, path)`, deny-default `?? false` | `App.tsx:303` (nav item), `ProtectedRoute.tsx:57` (route + redirect) |
| **B** | **ROW / DATA-FILTER** | records within a page | `isEmailFromFirm(row.initiator_email, firmId)` | `TradeSubmission/HistoryTab.tsx:55` |
| **C** | **SERVED-PLANE SCOPING** | the payload itself | `/api/scoped/.../{firm}/{leaf}` — **the firm is IN THE PATH** | `adviKeyRepoint.ts:142`, the AdvisorIntelligence endpoint family |
| **D** | **FEATURE / MODE** | a capability inside a page | `modesFor(firm)` over `MODE_FIRM_ALLOWLIST` | `Positioning/shared/modeAccess.ts` — **NEW today (TO-4)** |

⚠ **A, B and D are CLIENT-SIDE. Only C withholds bytes.** That distinction is the whole analysis.

## 2. WHAT POSITIONING ACTUALLY DOES TODAY — MEASURED, NOT ASSUMED

```
models    -> /api/general/positioning/positioning_data.json      (Positioning.tsx:16)
etfs      -> /api/general/etfs/positioning_data.json             (Positioning.tsx:17)
satellites -> satellitesToPositioningShape(positioningData)      (Positioning.tsx:225)
                                                                  ^ DERIVED CLIENT-SIDE from models

query keys: ['positioning-data'] · ['etf-positioning-data'] · ['holdings-attribution']
            NO FIRM IN ANY OF THEM
```

⛔ **`api/general/` = ANY AUTHENTICATED USER; `api/scoped/` = VARIES BY JWT CLAIMS** (the 2026-02-25
architecture decision, and confirmed live: `api/scoped` appears in 10 files, `api/general` in 21).
**Positioning is entirely on the general plane.**

>> **THEREFORE: THE SATELLITES NUMBERS ARE COMPUTED IN THE BROWSER FROM A PAYLOAD SERVED TO EVERY
   AUTHENTICATED USER OF EVERY FIRM. `modesFor` HIDES THE PILL. IT DOES NOT WITHHOLD THE DATA.** A
   non-Cottonwood user who fetches `/api/general/positioning/positioning_data.json` directly has
   everything needed to compute the satellite blends themselves. <<

**This is exactly what `SAT-c-3` declared** — *"a VISIBILITY gate, not an authorization boundary ...
the underlying models payload is already served to this viewer; satellites are arithmetic over it"* —
**and it reserved the other reading for a different design and a different review.**

## 3. ⭐ THE PATTERN ANDREW IS ASKING FOR **ALREADY EXISTS IN THE ESTATE**

**AdvisorIntelligence is the worked example of true multi-tenancy**, and it uses **three** mechanisms
together — which is the finding, because Positioning has **one**:

```
1. SERVED PLANE   /api/scoped/advisor-intelligence/platinum/advi/${firm}/${leaf}   firm IN THE PATH
2. CACHE KEY      queryKey: ['advisor-intelligence', 'timeseries-overview', firmOverride]
                  queryKey: ['firm-leaderboard', firmOverride]
3. ROUTE GATE     FIRM_ALLOWED_PATHS / isPathAllowedForFirm
```

**POSITIVE CONTROL for the cache-key limb:** 4+ query keys in the estate DO carry `firmOverride`, so
this is an established convention the codebase already follows — **Positioning simply does not.**

>> **THE GOVERNING PATTERN, STATED: a firm-specific FEATURE needs the gate at the plane where the
   guarantee is made. UI gating (D) delivers a UI guarantee. Only served-plane scoping (C) delivers
   a data guarantee — and C is inert without the cache key, because React Query would otherwise hand
   one firm's cached payload to the next identity on the same client.** <<

## 4. ⛔ THE ONE QUESTION, AND IT IS ANDREW'S — R5 CANNOT BE WRITTEN WITHOUT IT

His words: *"available on Cottonwood's page, **but nobody else**."*

| reading | means | status today | work required |
|---|---|---|---|
| **(a) VISIBILITY** | no other firm SEES the satellites UI | ✅ **SHIPPED** (TO-4, conforms to R1–R3) | validation only (R6) |
| **(b) ACCESS** | no other firm can OBTAIN the satellites data | ❌ **NOT SATISFIED, and unreachable by any client-side gate** | move to `api/scoped/`, firm in path, firm in cache key, server-side check |

**These are not degrees of the same thing.** (b) is a different plane, a different owner (AE holds
serving/IAM), and a security review rather than a rendering one. ⚠ **"Nobody else" reads naturally as
(b) — and I am NOT inferring it**, because the same sentence also says *"available on Cottonwood's
PAGE"*, which is (a)'s vocabulary. **The sentence is genuinely ambiguous between them and only he can
settle it.**

## 5. R6 — BREAKAGE VECTORS ALREADY IDENTIFIED (independent of §4's answer)

1. ⛔ **THE CACHE KEY IS THE TRAP IF (b) IS EVER BUILT.** Moving the artifact to `api/scoped/`
   **without** adding the firm to `queryKey` would let React Query serve one firm's cached payload to
   a different identity on the same client. **The estate's own convention (`firmOverride` in the key)
   is the mitigation and Positioning does not follow it.** Auto-Rule 2 binds any TO introducing this.
2. **`modesFor`'s `null` arm fails closed** — verified. An identity-service outage denies rather than
   grants. Correct, and it must survive any (b) rework.
3. **`gateSlugsResolve()` is a spelling assertion, NOT a coupling** — ⚠ **I first read its
   `FIRM_ALLOWED_PATHS` import as the feature gate deriving from the route table and was WRONG.** The
   gate is an independent `MODE_FIRM_ALLOWLIST`; the import only asserts the slug still names a known
   firm, turning a silent typo into a test failure. **Good design. Recorded because I nearly filed it
   as a defect.**
4. **Pattern D is NEW and currently has ONE instance.** Whether it becomes the estate's convention for
   per-firm features, or is absorbed into C, is a design decision this spec must make explicitly
   rather than by accretion.

## 6. WHAT I AM NOT DOING

- **Not choosing between (a) and (b).** That is R5's premise and it is sovereign.
- **Not promoting to PROD.** My `/open-calls` CALL 1 proposed promoting TO-3+TO-4 together; this
  directive says multi-tenancy *"needs to be sorted out"*, which sits badly against promoting the
  point solution tonight. **Flagged, not decided — he did not mention the promote.**
- **Not amending `ETFS_SATELLITES`.** Its round 1 is certified and closed; this is a new project
  under Rule 27.

---

# AMENDMENT 1 — 19:0xZ. TWO FACTS FROM `0.4.0_DE_ClientPlatform~Y`, ONE OF WHICH **BOUNDS A CLAIM I MADE**

Supplied by the seat that BUILT the gate, explicitly **not** adjudicating §4 and **not** claiming
R4/R5/R6 — *"those are a CTO act ... these facts are cheaper to hand over than to re-derive."*
**Correct routing, and both facts change this document.**

## A. THE PAGE IS SHARED BY ALL FOUR PARTNER FIRMS — THIS SHARPENS THE PROBLEM STATEMENT

```
FIRM_ALLOWED_PATHS -- /positioning is ALLOWLISTED FOR:
  49financial YES · inflection YES · cottonwood YES · demo YES   (+ opal-capital, internal)
  DENOMINATOR: 4 of 4 partner firms.
```

>> **SO THE PAGE IS NOT COTTONWOOD'S — ONLY THE FEATURE IS.** Andrew's *"available on Cottonwood's
   page"* describes **a shared page carrying a firm-specific feature**, which is precisely the
   multi-tenancy problem he asked to be sorted out. **Pattern A (route gating) cannot express this at
   all** — it is page-grained, and the page is deliberately shared. **That is why Pattern D had to be
   invented, and it is the structural argument for treating D as a first-class estate pattern rather
   than a satellites one-off.** <<

## B. INDEPENDENT CONFIRMATION OF §2, BY A DIFFERENT ROUTE

They measured that **satellites is arithmetic over the already-fetched models payload — no separate
fetch**; `satelliteAdapter` consumes the `positioningData` the page already holds. **I reached the
same conclusion from the ENDPOINT PLANE (`api/general/` + no firm in any query key); they reached it
from the ADAPTER.** Two instruments, one verdict — corroboration, not repetition.

## C. ⛔ AND THE BOUND ON MY OWN §2 — I ASSERTED "ANY AUTHENTICATED USER" FROM A CONVENTION

My §2 reads *"`api/general/` = ANY AUTHENTICATED USER"*, resting on the 2026-02-25 architecture
decision. **`0.4.0_DE_ClientPlatform~Y` flags a comment on `getPositioningData` reading
*"DEMO: Using public endpoint (no auth)"* — and REFUSES to relay it as measured**, which is right:
*"a comment is a claim about a vintage, not about the running system."*

**What they DID read at source:** `apiRequest` (`api-client.ts`) attaches `Authorization: Bearer`
**whenever an access token exists**, so the CLIENT always sends one. **Whether the SERVED ROUTE
REQUIRES it at the edge is a server-side fact on the AE/serving plane and is UNMEASURED.**

>> ⛔ **THEREFORE MY §2 IS BOUNDED, AND IN THE UNSAFE DIRECTION: the exposure is AT LEAST
   "every authenticated user of every firm" and MAY be "anyone at all". I stated the floor as though
   it were the ceiling.** For a question that may resolve into a security review, understating the
   exposure is the wrong error to make. <<

**REQUIRED IF §4 RESOLVES TO (b) ACCESS — and it is the FIRST act, before any redesign:** measure at
the EDGE whether `/api/general/positioning/positioning_data.json` requires a bearer. ⚠ **Do NOT let
the comment stand in for that measurement in either direction** — it is equally capable of being
stale-and-wrong about a route that IS protected.

---

# AMENDMENT 2 — 19:0xZ. **THE EDGE MEASUREMENT IS IN. MY ORIGINAL CLAIM STANDS; MY AMENDMENT-1 CEILING IS FALSIFIED.**

`0.0.0_AB_MSTR~Z` ran the serving-layer read (their lane) within minutes of Amendment 1 naming it.

```
NO auth header      -> HTTP 401  {"error":"Missing or invalid Authorization header"}
VALID RS256 bearer  -> HTTP 200  8088 bytes  application/json
CONTROL bogus token -> HTTP 401  {"error":"Invalid or expired token"}   <- a DISTINCT message
CONTROL bad path    -> HTTP 401  (auth enforced BEFORE path resolution)
```

⭐ **THE TWO 401s DIFFER, AND THAT IS THE LOAD-BEARING DETAIL: the edge distinguishes MISSING from
INVALID, so it is VALIDATING the token, not merely checking a header exists.** A single
undifferentiated 401 would have been equally consistent with a dumb presence check.

## WHAT THIS DOES TO MY OWN TWO CLAIMS

| my claim | verdict |
|---|---|
| §2: *"`api/general/` = ANY AUTHENTICATED USER"* | ✅ **CONFIRMED — by a DIFFERENT instrument** (live HTTP) than the architecture doc I reasoned from |
| Amendment 1: *"MAY be anyone at all"* | ❌ **FALSIFIED. The ceiling is NOT "anyone"; it is exactly the floor I first stated.** |

⛔ **AMENDMENT 1 WAS RIGHT TO BOUND THE CLAIM AND WRONG IN ITS SPECULATIVE CEILING.** The edge
behaviour genuinely was unmeasured and saying so was correct; **inventing a worst case to sit in that
gap was not, and it is the mirror of the error it was correcting.** Understating exposure and
overstating it are both mis-sizing a sovereign option. **Recorded as mine.**

**AND THE CODE COMMENT IS FALSE AGAINST THE SERVED ARTIFACT** — `portal-proxy.ts:1090-1097` claims
*"PUBLIC DATA (DEMO): No auth required"*. It never was true as written: `apiRequest` attaches a
bearer whenever one exists, and the edge rejects the request without one. ⭐ **`0.4.0_DE_ClientPlatform~Y`
flagged it and REFUSED to relay it as measured — had it been quoted as evidence, an option in front
of Andrew would have been sized against a fiction.**

## ⭐ THE CONSEQUENCE FOR §4 — **OPTION (b) IS MATERIALLY SMALLER THAN §4's TABLE IMPLIES**

**There is already a real, token-validating auth boundary at the edge.** So (b) is **NOT** "build
authentication for this endpoint" — it is **"add FIRM-SCOPING to an endpoint that already
authenticates"**, i.e. the AdvisorIntelligence pattern applied to an existing protected route:
`api/scoped/` + firm in the path + firm in the query key.

>> **§4's table stands, but its (b) column was priced too high. The missing control is
   FIRM-DISCRIMINATION, not AUTHENTICATION — and that is a smaller, better-understood change with a
   worked example already in the estate.** <<

---

# AMENDMENT 3 — 19:0xZ. ⭐ **ANDREW HAS RULED ON THIS QUESTION TWICE BEFORE. HIS OWN WORDS ARE THE BEST EVIDENCE IN THIS DOCUMENT.**

Found by running the **Auto-Rule 5 pre-authoring check before registering a new project** — *does this
already exist?* **It nearly did.** Three candidate projects existed; none is a duplicate, and **two
are directly-on-point sovereign precedent I had not consulted.**

## A. `ADVI_FIRMSEP` — **ANDREW-DIRECT 2026-05-07, VERBATIM**

> *"I want to make sure that we are properly splitting these based on firm-id... **containment of
> data in those cached layers is paramount**"*
> *"third partner **Cottonwood** coming in sooner than later, these kind of fixes should be handled
> the sooner the better."*

**AND THE AUDIT UNDER IT NAMES THE FULL PATTERN — this is the answer to R4, in the estate's own
record:**

```
/api/scoped/advisor-intelligence/*  cache policy `opal_scoped_advisor_by_firm`
  - firm QUERY STRING in the cache key
  - X-Firm-Id HEADER in the cache key
  - >> X-Firm-Id IS JWT-INJECTED, NOT REQUEST-DERIVED <<   <- the security-critical property
```

⭐ **THAT THIRD LINE IS THE ONE MY §3 WAS MISSING.** The pattern is not merely "firm in the path +
firm in the query key" — it is **firm in the CDN cache key, sourced from the JWT so the client cannot
assert it.** A client-supplied firm would make the whole structure decorative.

⚠ **`ADVI_FIRMSEP` is INACTIVE / ON HOLD, and its Phase 3 is "Cottonwood live ship, gated on
Cottonwood credentials + bucket creation."** **Cottonwood is now live** — it holds a firm id and is
in `FIRM_ALLOWED_PATHS`. **That hold may be dischargeable, and nobody has looked.** Surfaced, not
chased.

## B. `MDPF_SCOPED` — **ANDREW-DIRECT 2026-05-28, and it is CLOSED COMPLETE**

> *"split Model Portfolios apart by partner using **the EXACT same pattern as Advisor Intelligence**"*

**A sibling page, the same problem, ruled the same way, SHIPPED and closed 2026-06-03.**

>> **SO: MY §3 CONCLUSION — "AdvisorIntelligence is the governing pattern" — WAS REACHED
   INDEPENDENTLY FROM SOURCE, AND HE HAD ALREADY RULED IT TWICE.** That is corroboration of the
   analysis by the strongest available authority, and I should have found it FIRST rather than
   re-deriving it. <<

## C. ⛔ WHAT THIS IS AND IS NOT EVIDENCE OF — THE LINE MATTERS

**IT IS:** strong evidence of standing intent — he has twice chosen served-plane firm scoping, once
using the words *"containment of data ... is paramount"*, once naming **Cottonwood** specifically as
the reason to act early.

⛔ **IT IS NOT a ruling on Positioning.** `ADVI_FIRMSEP` governs the **ADVI** surface and its cached
layers; `MDPF_SCOPED` governs **Model Portfolios**. **Neither names the Positioning page, and
relaying them as though they did would be exactly the widening this estate forbids** — a relayed
ruling inherits its document's scope, and I am carrying the scope with it.

**BEARING ON §4:** the precedent leans toward **(b) ACCESS** — *"containment of data in those cached
layers is paramount"* is not a UI-visibility sentiment. **But §4 remains HIS to settle**, because the
one thing neither precedent establishes is whether the Positioning payload is in the class he meant.

---

# AMENDMENT 4 — R6 BLAST RADIUS. ⛔ **`positioning_data.json` IS NOT A POSITIONING-PAGE ARTIFACT, AND THIS PARTLY OFFSETS AMENDMENT 2.**

**MEASURED — the `['positioning-data']` React Query key is SHARED BY FOUR CONSUMERS:**

```
src/pages/Positioning/Positioning.tsx:188         the Positioning page
src/pages/Attribution/Attribution.tsx:35          THE ATTRIBUTION PAGE          <- a different page
src/components/ModelPortfolioModal.tsx:133        A SHARED MODAL                <- reused surface
src/pages/DataRefresh/rollbackInvalidation.ts:58  THE CACHE-INVALIDATION LIST   <- hardcoded copy
```
**Artifact consumers: 7 files.** **Firms reaching `/positioning` today: 4 of 4 partners** —
`49financial`, `inflection`, `cottonwood`, `demo` (+ internal).

## WHAT THIS DOES TO OPTION (b), HONESTLY IN BOTH DIRECTIONS

⚠ **AMENDMENT 2 SAID (b) WAS "MATERIALLY SMALLER" BECAUSE AUTH ALREADY EXISTS. THAT REMAINS TRUE AND
IS NOW ONLY HALF THE PICTURE.** The AUTH work is small; **the BLAST RADIUS is wider than the
Positioning page**, and I would have under-priced (b) in the opposite direction had I stopped at
Amendment 2.

1. ⛔ **MOVING THE ARTIFACT TOUCHES ATTRIBUTION AND A SHARED MODAL, NOT JUST POSITIONING.** Any
   `api/scoped/{firm}/` move is a **three-surface change**, and Attribution was never in scope of
   Andrew's sentence.
2. ⛔ **THE SHARED KEY IS A LIVE COUPLING, NOT A FUTURE HAZARD.** §5.1 framed the cache key as a risk
   *if* (b) is built. **It is worse: because four consumers share ONE key, scoping Positioning's
   fetch without scoping Attribution's would put two different payloads under one key** — a
   cross-page collision, not merely a cross-firm one.
3. ⛔ **`rollbackInvalidation.ts:58` HARDCODES `['positioning-data']`.** If the key gains a firm
   dimension and that list is not updated, **invalidation silently stops matching** — and a cache
   that never invalidates is exactly how stale cross-firm data would persist. **The invalidation
   list is a SECOND CARRIER of the key**, and this session has now found four instances of one
   obligation living in two carriers.
4. **All four partner firms reach `/positioning` today**, so a scoped artifact is needed **per firm**,
   not just for Cottonwood — or the other three lose the page.

>> **NET: (b)'s AUTH limb is small; its BLAST-RADIUS limb is larger than the page Andrew named. Both
   corrections are mine and they run in opposite directions — I am stating them together rather than
   letting the flattering one stand alone.** <<

**BRANCH-INDEPENDENT VALUE:** items 2 and 3 are **defects today**, regardless of how §4 resolves. A
shared cache key across four consumers with a hardcoded duplicate in the invalidation list is worth
recording whether or not anything is ever firm-scoped.

-- `1.0.0_SA_CTO~Z`
