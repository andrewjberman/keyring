# `modesFor(firm)` — RULE 24 FOUR-POSTULATE RECORD, and the viewer-firm source NAMED

**Author:** `1.0.0_SA_CTO~Z` · 2026-08-27 ~17:3xZ
**Discharges:** CVO certification **F2 (P1)** — *"`modesFor(firm)` IS A SCHEMA-AUTHORING ACT AND HAS
NO FOUR-POSTULATE RECORD ... Ask: a four-postulate record for `modesFor` before `SAT-c-1`/`SAT-c-2`
are cut into TOs. Owner: `1.0.0_SA_CTO~Z` (issuer)."*
**Also discharges `SAT-c-1`'s prerequisite** — *"THE VIEWER-FIRM SOURCE MUST BE NAMED BEFORE ANY GATE
IS WRITTEN ... a gate written against an unnamed source is INFERRED and non-actionable (Rule 22)."*
**Project:** `ETFS_SATELLITES` · **Directive:** D4 (SITEZ)

⚠ **WHY THIS IS A SEPARATE ARTIFACT AND NOT A TO SECTION.** `2.0.0_SA_COO~Z` deferred authoring it
for a reason this seat accepts and `3.0.0_SA_CVO~Z` recorded as CORRECT, not as an omission: *"a
four-postulate record over an unnamed source is the untestable-criterion shape this decomp already
refuses."* **So §1 (naming the source) is the precondition for §2 (the record), and §1 had to be
measured first.** That ordering is the whole content of the deferral.

---

## 1. THE VIEWER-FIRM SOURCE — NAMED, WITH VINTAGE

**All citations at portal submodule `origin/DEV` = `4ac152f8`.** ⚠ The local portal working tree is
`eaa094e6`, **2 commits behind**, and `src/lib/firmAccess.ts` **is one of the 5 files those 2 commits
touched** — so every citation below was read from `origin/DEV` via `git -C portal show`, not from the
working tree. *(Site-Z portal-staleness is a banked, recurring condition; this is it biting a live
citation.)*

### 1.1 The production path — the firm is **SERVER-DERIVED**, not client-asserted

```
portal/src/contexts/AuthContext.tsx
  :196-201   claims = parseClaims(meData.user)      <- meData from GET {API_BASE}/auth/me
  :348-354   same shape on the login path
  :354       FALLBACK on /auth/me failure:  claims = { firmId: null, ... }
  :583-588   canAccessFirm(firmId): internal 'opal-capital' -> true; else EXACT match
  :552,:575  the internal test IS  claims.firmId === 'opal-capital'

portal/src/lib/firmAccess.ts
  :18        const INTERNAL_FIRM_ID = 'opal-capital'
  :41        FIRM_ALLOWED_PATHS: Record<string, ReadonlySet<string>>
  :65,:73    'cottonwood' -> the set CONTAINS '/positioning'
  :99-106    isPathAllowedForFirm(firmId, path):
               if (firmId === INTERNAL_FIRM_ID) return true
               return FIRM_ALLOWED_PATHS[firmId]?.has(path) ?? false     <- DENY-ALL DEFAULT
```

>> **THE VALUE IS SERVER-DERIVED.** The client does not assert its firm; it calls `/auth/me` with the
   bearer token and the server returns the user record. **`SAT-c-2`'s "SERVER-DERIVED OR
   SERVER-VALIDATED, NEVER CLIENT-ASSERTED" is satisfiable on the existing mechanism** — this is not
   new plumbing at the *identity* layer. <<

### 1.2 The DEV-only override, named so nobody mistakes it for the production path

`AuthContext.tsx:499-538` — `devBypass(advisorRole?, firmRole?)` synthesises claims including
`firmId`, and `:540-545` exposes it as `window.__devBypass` **guarded by `import.meta.env.DEV`**. It
is not reachable in a production build. **Named here because a reader grepping `firmId` finds it and
could reasonably mistake it for a client-assertion hole.**

### 1.3 ⛔ THE THING THAT CHANGES THE DESIGN: `firmId` HAS A **NULL** STATE, AND IT IS A FAILURE STATE

`AuthContext.tsx:354` sets `firmId: null` when the `/auth/me` call **fails** — an authenticated
session whose firm is *unknown*, not *absent*.

**So the domain of `modesFor` is not "the set of firms". It is `firms ∪ {null}`,** and `null` means
*the identity service did not answer*, which is exactly the `UNKNOWN`-vs-`NO-MATCH` distinction D1's
`ND-e-1` exists to protect. **A `modesFor` written over "firms" alone has an uncovered member.**

⭐ **THE EXISTING CODE ALREADY GETS THIS RIGHT AND IS THE MODEL TO COPY:**
`isPathAllowedForFirm` ends `?? false` — **deny-all on an unknown key.** `modesFor` must fail the
same direction.

### 1.4 What is genuinely new — and `SAT-c-1`'s measured premise, re-verified

`SAT-c-1` states the Positioning directory carries **ZERO firm-id references**. **Re-measured at this
seat, and it holds as an operative claim:**

```
portal/src/pages/Positioning           11 files, 8 hits for /firm|tenant|orgId/i
                                       ALL 8 ARE PROSE -- README + code comments about the
                                       REMOVED 'AGG' column ("firm-wide AUM", "three partner firms")
                                       ZERO are a firm-id code reference.
POSITIVE CONTROL                       105 files under portal/src DO contain 'firm' (case-insensitive)
                                       -- so the matcher works and the zero is a TRUE ABSENCE.
```

⚠ **I initially scored the WRONG directory** — three paths match `*ositioning*` and `head -1` gave me
`portal/etl/pages/positioning` (1 file, 0 hits). A clean zero from the wrong plane. Recorded because
the correct answer and the wrong-plane answer were both "0".

>> **SO THE SEAM IS REAL: identity is solved, and the Positioning page has never consumed it.** <<

---

## 2. THE FOUR-POSTULATE RECORD (Rule 24)

**THE SCHEMA UNDER TEST:** `modesFor(firm) -> Set<PositioningMode>`. It is a predicate returning a
typed set, and Rule 24 binds: *"Outcome arrays, typed-result sets and predicates ARE schemas."*

**DECLARED DOMAIN:** *the viewer-firm identities this application can present a Positioning page to* —
which by §1.3 is `{'opal-capital', 'cottonwood', '49financial', 'inflection', …} ∪ {null}`.

| postulate | verdict |
|---|---|
| **(i) MECE over a DECLARED domain** | ⛔ **FAILS AS NAIVELY STATED, AND THIS IS THE FINDING.** The decomp's `SAT-c-2` reads *"Cottonwood + Opal see three pills; every other firm sees two."* **`null` IS NOT A FIRM, so it is not covered by "every other firm"** — the domain member that means *the identity service did not answer* has no declared image. **CE FAILS until `null` is covered.** ME holds: the branches are disjoint by construction (a firm is in the three-pill set or it is not). **REMEDY, and it is one line:** declare the mapping total over `firms ∪ {null}` with **`null -> the two-pill set`**, matching `isPathAllowedForFirm`'s `?? false` deny-default. **PASSES once total.** |
| **(ii) SAME GRAIN** | **PASSES.** Every domain member is a *viewer-firm identity*; every image is a *set of book-family modes*. Neither side mixes grains — a value like `'cottonwood-admin'` (firm × role) would break it and none is proposed. ⚠ **Role is a genuinely separate axis and lives elsewhere** (`firmRole`/`advisorRole` in the same claims object); folding it in here would be the (iii) failure below, one level up. |
| **(iii) INTENT COHERENCE** | **PASSES, and it is the postulate the whole `SAT-b-1`/`SAT-c-1` split exists to protect.** One intent: *which modes may this VIEWER see.* ⛔ It must NOT fuse with `PositioningMode`'s intent (*which book family is being displayed*). The decomp's own (iii) verdict on the mode axis says a value like `SATELLITES_COTTONWOOD` would fuse book-family with viewer-firm — **two intents on one axis.** `modesFor` is the correct home for the second intent **precisely because it is a different function, not a different enum value.** |
| **(iv) STATE COHERENCE** | **PASSES, and the asymmetry is worth stating rather than asserting.** Name which values one remedy does NOT move: **onboarding a new partner firm moves that firm's image only** (a `FIRM_ALLOWED_PATHS`-style data edit, per `firmAccess.ts:10` *"To onboard a new partner firm: add an entry"*). **Building the satellites mode moves `'cottonwood'` and `'opal-capital'` only.** **Fixing the identity service moves `null` only — and nothing else moves it.** Three remedies, three disjoint effects. No single remedy moves all members, which is what (iv) tests. |

### 2.1 WORD-BOUNDARY TOKEN CENSUS (Rule 24 requires it with the record)

Case-insensitive, word-boundary, over `portal/src` — **denominator 407 `.ts`/`.tsx` files:**

| token | hits | files | reading |
|---|---|---|---|
| `modesFor` | **0** | **0** | **NET-NEW. Collides with nothing.** |
| `satellites` | **0** | **0** | **NET-NEW.** |
| `PositioningMode` | 21 | 5 | the axis being extended — see §3 |
| `POSITIONING_MODES` | 5 | 2 | the pill-list array — see §3 |

**Both proposed names are unoccupied at 0 prior occurrence.** No sibling-shadowing of the kind that
forced `BUILD-GENERAL` over `BUILD-OTHER` in the proof-of-spec enum.

### 2.2 ⛔ A BOUNDARY THE RECORD MUST STATE — `SAT-c-3` IS LOAD-BEARING HERE

`SAT-c-3` declares this a **VISIBILITY gate, not an AUTHORIZATION boundary** — *"the underlying models
payload is already served to this viewer; satellites are arithmetic over it."*

**That is consistent with what §1 measures, and it constrains where `modesFor` may live.** The firm
VALUE is server-derived, but a mode DECISION computed in `bookSet.ts` is **client-side**. For a
visibility gate that is adequate. ⛔ **If the intent is ever an AUTHORIZATION boundary, this record
does not cover it** — that is a different design, a different review, and a server-side decision.
**Say which, and do not let the answer drift by default.**

---

## 3. ⛔ A SECOND FINDING, ON THE MODE AXIS — `SAT-b-1`'s ORACLE IS WRONG ABOUT ITS OWN FAILURE MODE

Not asked for by F2; found while measuring the census above. **It lands on `SAT-b-1` and it changes
what its TO must require.**

`SAT-b-1` names **six** declarations and its oracle says: *"a mode added to fewer than all six
declarations is a partial add and **fails at the one that was missed**."*

**MEASURED — there are EIGHT mode-keyed sites, not six, and only THREE fail loudly:**

```
COMPILER-ENFORCED (Record<PositioningMode, X> -- a missing key is a TypeScript ERROR):
  bookSet.ts:172   HOLDING_NOUN            Record<PositioningMode, string>
  bookSet.ts:210   CHARACTERISTIC_FIELDS   Record<PositioningMode, CharacteristicFields>
  bookSet.ts:347   MODE_LABELS             Record<PositioningMode, string>

SILENT -- a BINARY TERNARY that binds any new value to the *models* branch:
  bookSet.ts:80    declaredBooks     mode === 'etfs' ? ETF_BOOKS : MODEL_BOOKS
  bookSet.ts:156   capabilitiesFor   mode === 'etfs' ? {all false} : {all TRUE}
  bookSet.ts:105   resolveBooks      delegates to declaredBooks -- inherits it
  gridConfig.ts:45 portfolioNamesFor mode === 'etfs' ? [...books] : books.map(displayModelName)

SILENT -- an ARRAY LITERAL the compiler does not check for exhaustiveness:
  bookSet.ts:353   POSITIONING_MODES = ['models','etfs'] as const     <- THE PILL LIST
```

⛔ **THREE CONSEQUENCES, EACH OF WHICH SHIPS GREEN:**

1. **`POSITIONING_MODES:353` IS THE PILL LIST AND IS AN ARRAY LITERAL.** Adding `'satellites'` to the
   type at `:53` does **not** make the compiler ask for it here. **You can extend the type, satisfy
   all three `Record`s, get a clean `tsc`, and the pill never renders.** Feature silently absent.
2. ⛔ **`capabilitiesFor:156` IS THE DANGEROUS ONE AND IT CONTRADICTS `SAT-d-3` BY DEFAULT.**
   `SAT-d-3` declares satellites v1 capabilities `{benchmark:false, relative:false, customBlend:false,
   attribution:false}` — the ETF precedent. But the ternary gives any non-`'etfs'` value the **models**
   branch, which is **all TRUE**. **The UI would offer benchmark, relative, custom-blend and
   attribution on a mode that has none of them built** — four affordances with nothing behind them,
   and the decomp's own cell says the opposite. *A cell contradicted by a default is not a cell.*
3. **`SAT-b-1`'s list omits `declaredBooks`, `resolveBooks` and `portfolioNamesFor`** — which are
   exactly three of the five that fail **silently**. **The oracle checks the six it knows and every
   site it does not know about is one it cannot see missed.**

>> **SO THE ORACLE'S CLAIM — "fails at the one that was missed" — IS TRUE FOR 3 OF 8 SITES AND FALSE
   FOR 5.** For the five, `'satellites'` binds to the MODELS branch and renders **models data and
   models capabilities under a satellites label**. That is not a missing feature; it is a **wrong
   answer wearing the right label**, on a client-facing page. <<

**REQUIRED IN THE `SAT-b-1` TO:** enumerate all eight sites, classify each ENFORCED vs SILENT, and
**exercise the silent five** — a `tsc` pass is NOT evidence for them. Andrew's own instruction on the
mode axis stands: the flip must render, and Models mode must stay byte-identical.

---

## 4. WHAT THIS RECORD DOES NOT DO

- **It does not certify anything.** `3.0.0_SA_CVO~Z` certifies; this is the issuer discharging an
  owed authoring act. F2 named `1.0.0_SA_CTO~Z` as owner and this is that discharge, submitted for
  certification like any other artifact.
- **It does not name the satellite-registry maintainer.** That is `2.0.0_SA_COO~Z`'s deliberately
  unfilled slot and an **open call at Andrew**; `3.0.0_SA_CVO~Z` ruled it **not a gate** — a TO may be
  cut and built now; the maintainer name is a **SHIPPING** condition. ⛔ **Nobody may relay it as a gate.**
- **It does not decide `SAT-a-4`** (delivery form: served block vs portal-fetched vs build-time
  constant). That cell is `2.0.0_SA_COO~Z`'s call by the decomp's own class assignment.
- **§3 is a finding, not a cell edit.** The decomp is `2.0.0_SA_COO~Z`'s artifact; I do not edit it.

-- `1.0.0_SA_CTO~Z`
