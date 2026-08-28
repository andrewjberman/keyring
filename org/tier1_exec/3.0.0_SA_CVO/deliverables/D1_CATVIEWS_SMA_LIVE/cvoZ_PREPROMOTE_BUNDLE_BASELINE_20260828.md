# PRE-PROMOTE SERVED-BUNDLE BASELINE -- `D1_CATVIEWS_SMA_LIVE` AC5

**Captured:** `3.0.0_SA_CVO~Z` 2026-08-28T~21:5xZ, **BEFORE** the DEV->PROD promote.
**Why now:** this is **perishable**. Once the promote lands, "what PROD served beforehand" is no
longer measurable, and AC5's before/after collapses to a single-sided reading.
**Origin:** `https://opalinvest.dev` · **PROD ref at capture:** `origin/PROD d4a048fd52`

---

## THE BASELINE

```
  index.html   HTTP 200   1068 B
  assets/index-Ce258d2k.js           Last-Modified: Fri, 28 Aug 2026 05:34:00 GMT
  assets/vendor-nivo-Bb-sNNXU.js     Last-Modified: Fri, 28 Aug 2026 05:34:01 GMT
  assets/vendor-query-CYvCHQ1I.js    Last-Modified: Fri, 28 Aug 2026 05:34:01 GMT
  assets/vendor-react-BxOhVy9d.js    Last-Modified: Fri, 28 Aug 2026 05:34:01 GMT
  assets/vendor-recharts-Cy1TERGQ.js Last-Modified: Fri, 28 Aug 2026 05:34:01 GMT
  assets/vendor-ui-DNo35gXc.js       Last-Modified: Fri, 28 Aug 2026 05:34:01 GMT

  POSITIVE CONTROL  7 asset refs found in index.html  (fetch + grep demonstrably work)
  NEGATIVE CONTROL  bogus token -> 0                  (the grep can return zero)
```
The 05:34 GMT stamps independently corroborate the `d4a048fd` promote (v2.1.170, authored ~05:2xZ) --
a second instrument agreeing with the merge message rather than repeating it.

## ⭐ THE DISCRIMINATOR THIS BASELINE BUYS, AND IT BEATS A STRING MARKER

**The chunks are CONTENT-HASHED** (`index-Ce258d2k.js`). Therefore:

> **A promote that changes any application code MUST produce a DIFFERENT `index-*.js` hash in
> `index.html`. If the hash is unchanged after the promote, NOTHING SHIPPED** -- regardless of what CI
> reported.

This is marker-independent and immune to the minification trap that makes string probes unreliable
(banked: a pattern search whose *positive control also reads zero* is a broken instrument).
**Post-promote check:** re-fetch `index.html`; the entry-chunk hash must differ from `Ce258d2k`, and
`Last-Modified` must be after the promote time. Both, not either.

## ⛔ WHY NO STRING MARKER IS NAMED HERE YET -- AND THIS IS DELIBERATE

AC5's stronger form ("the served bytes contain the fix") needs a marker only the new code has. **I
cannot pick one yet and picking one now would be wrong:**
- `text-amber-200` was the obvious candidate and **it is present in BOTH `2858e7f5ff` and
  `4dde6df344`** -- pre-existing, so as a marker it would yield a FALSE PASS.
- The `ModelPortfolios.tsx` delta is **entirely comments**, which minification strips.
- The one real added string, `"Fee split unavailable"`, sits on **exactly the surface D-4 is about to
  remove** -- an in-flight target.

>> **The marker must be chosen from the FINAL commit set, after `0.4.0_DE_ClientPlatform~Z` lands.**
   Choosing from a moving tree is the "a render taken from the shared checkout is a SNAPSHOT, not a
   ref" failure, and it would bake an invalidated marker into an acceptance check.

## SCOPE

- This is a BASELINE, not a verdict. It certifies nothing.
- It does **not** establish that `opalinvest.dev` is the only served origin; it is the origin this
  estate's banked render procedure uses, and that is the claim made.
- Served CODE is still not the visual RENDER with real data for an authenticated user. AC3 remains a
  separate rung requiring a REAL bearer -- **a default-stub render is the FAILURE state.** The
  exercised mint path is confirmed available (`portal/.frontend-dev/auth/` present: README +
  credentials + login-constitution) and was **deliberately NOT consumed**: TTL is 900s, so
  mint-then-render is ONE act, performed at ratification.

-- `3.0.0_SA_CVO~Z`
