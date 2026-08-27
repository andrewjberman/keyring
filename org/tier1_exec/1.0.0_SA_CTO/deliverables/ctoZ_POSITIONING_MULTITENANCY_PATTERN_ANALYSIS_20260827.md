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

-- `1.0.0_SA_CTO~Z`
