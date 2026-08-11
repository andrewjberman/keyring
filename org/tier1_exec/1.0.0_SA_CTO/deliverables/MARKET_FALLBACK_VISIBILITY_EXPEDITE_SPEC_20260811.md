# /market fallback VISIBILITY expedite — spec (Andrew-ruled "recs approved" ~2210Z, @d1baa0b631)

**Scope, his words:** make the fallback condition **VISIBLE IN PRODUCTION**. NOT a redesign of the
accessor. Rationale, verbatim: *"a silent wrong number on the default page is the one defect class
that reaches clients."*

**TWO BOUNDS, explicit and binding:**
1. ⛔ **EXPEDITE ≠ ALARM AUTHORIZATION. The moratorium is untouched.** Making an existing fallback
   path announce itself **in the UI and the logs it already writes** is inside the ruling. Building
   notification machinery around it — an alarm, an SNS topic, a monitor, a freshness checker, a
   watcher — is **NOT**, and needs his separate word.
2. ⛔ **NORMAL DEV → PROD PATH.** Nothing here authorizes a direct PROD act. Portal main worktree
   stays on `DEV` (verified: `portal` is on DEV); promotion runs the standard route.

## Grounded state (source-verified, `portal/src/api/endpoints/market.ts` @ DEV HEAD)

| line | today | consequence |
|---|---|---|
| `:219` | `console.warn('Tiered summary failed, falling back...')` — **unguarded** (its neighbours at :202/:207/:224/:228 are `import.meta.env.DEV`-wrapped) | fires in PROD, but **into a user's browser console — reaches no seat, aggregates nowhere** |
| `:239` | fallback returns `generated_at: new Date().toISOString()` | **the payload SYNTHESISES its own freshness** — the degraded response self-reports as current |
| footers | all six bind manifest `data_pkl`, not the artifact | April data would render under an August stamp |
| `:261` | terminal failure `console.error` + throw | total failure IS loud; **partial degradation is not** |

**Live status: ARMED, NOT FIRED** — primary healthy 2026-08-11; fallback target unwritten since
2026-04-15 (118 days). Exposure is conditional on a primary failure.

## The change (minimum that makes the condition visible; no accessor redesign)

**A. The response carries its own degradation state.** The fallback leg returns a field marking the
path taken — e.g. `source_tier: 'fallback'` alongside the existing `data_as_of` — so **the payload
stops claiming to be a primary response.** This is the load-bearing half: everything downstream can
only surface what the response admits.

**B. `generated_at` stops lying.** On the fallback leg, do NOT synthesise `new Date()`. Carry the
artifact's own date (`firstItemDataAsOf` is already read at `:238`) or omit `generated_at` rather
than fabricate it. **A synthesised freshness stamp on stale data is the defect itself, not a
symptom of it.**

**C. The surface shows it.** Where the page renders market returns, a degraded response renders a
visible state — the existing footer/stamp path is the natural home, since it already displays a
date. Minimum: the user sees that the data is a fallback and sees the **artifact's** date, not the
manifest's. **This is UI the page already renders — not new notification machinery.**

**D. Keep `:219`'s warn unguarded** (it already is) and let it carry the artifact date too. Free.

## Explicitly OUT of this expedite (rides the normal remediation queue)

The primary/fallback architecture · the 118-day-stale target's disposition (restore vs retire) ·
**footer-to-artifact binding as a general fix** — that is the whole page-family class W1–W3 mapped,
and it is a design call, not an expedite.

## Owner + route

Portal code, `DEV` branch, standard promotion. **No frontend seat on site Z** — this is the same
constraint as F-1/R1-cma, and the expedite does not create one. Route: assign to a portal-capable
seat via MSTR~Z, or Andrew names the seat. **Verification is a RENDERED check** (the
`/frontend-dev` screenshot discipline), because a degraded-state UI claim read from source is the
config-read-for-a-behaviour-claim class (Rule 22a).
