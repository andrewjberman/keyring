# 0.1.0_DE_MarketIntelligence~Z — OPAL_ANALYST.EXP1: /market fallback VISIBILITY (Andrew-expedited)

**archetype:** IMPLEMENT

**Date:** 2026-08-11 · **Session:** site Z · **TO:** OPAL_ANALYST.EXP1 (1.0.0_SA_CTO~Z)
**Spec:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/MARKET_FALLBACK_VISIBILITY_EXPEDITE_SPEC_20260811.md` @bc255c7980
**Ruling:** Andrew ~2210Z @d1baa0b631 — "recs approved", EXPEDITE THE VISIBILITY HALF ONLY

## What I was asked for

Make the `/market` fallback condition **visible in production**. Not a redesign of the accessor.
Andrew's rationale, verbatim: *"a silent wrong number on the default page is the one defect class
that reaches clients."*

## Current State

**DELIVERED — portal DEV `715c431f`, 5 files, all four spec changes A–D. Not pushed** (lane
commit; MSTR~Z integrates). Proof-of-spec instance VALID (rc=0) against C1–C4.

The defect was **armed, not fired**: primary healthy today, fallback target unwritten since
2026-04-15 (118 days). Nobody was being served stale data. The change makes the bad day visible
when it comes.

| spec | change | file |
|---|---|---|
| **A** | `AllReturnsResponse.source_tier: 'primary' \| 'fallback'` — the payload admits which leg served it | `market.ts` |
| **B** *(load-bearing)* | fallback `generated_at` no longer `new Date()`; carries `firstItemDataAsOf` or is **omitted**. Same synthesis one level down (per-ticker `generated_at`) fixed with it | `market.ts` |
| **C** | degraded state renders on the surface with the **artifact's** date | `MarketPerformance.tsx` + `dataLoader.ts` + `hooks.ts` |
| **D** | `:219` warn stays unguarded; a new unguarded DEGRADED warn carries the artifact date | `market.ts` |

Type changes that fall out of B: `generated_at` optional on `AllReturnsResponse` **and**
`TickerReturns`, `MarketData.lastUpdated` is `Date | null`. **Omission has to be representable or
the code will keep back-filling a lie.** `comp-find` confirmed no component READS
`TickerReturns.generated_at` (write-only) and only `dataLoader` reads the response's, so the
widening breaks no reader.

## Verification — RENDERED, not read

C1 is written as a rendered check because closing an invisible-degradation finding on a source
read is a behaviour claim verified by a config read (Rule 22a). I forced the primary to actually
fail and looked at the page.

- **C1** — primary forced 503, fallback fixtured at the real 2026-04-15 date. Banner renders:
  *"Fallback data source. The primary market feed is unavailable, so these returns come from the
  backup artifact dated **2026-04-15**. This data may not be current."* PNG read at 1:1.
- **C2** — from the exercised response, not the diff: `[dataLoader] ... updated 2026-04-15`.
- **C3 negative control** — healthy BEFORE vs AFTER: **59 changed px of 3,545,280 (0.0017%)**,
  confined to the CNN Fear&Greed wall clock (6:29p vs 6:28p). A **same-code self-control** moved
  **106 px in the same region** — the change-attributable delta is *below the run-to-run noise
  floor*. Healthy render carries no banner.
- **C4** — banner is dark-on-light: text `amber-900` rgb(123,51,6), **5.30:1** vs the banner fill
  and **5.51:1** vs the raw silver canvas. Both above WCAG AA. No light-text idiom on the canvas.
- **MUTANT** — pristine code, identical exercise: no banner (page 70 px shorter — the banner's own
  footprint), no DEGRADED warn, and `updated 2026-08-11T22:29:30.128Z` (April data, August stamp).
  **FIRED AS EXPECTED**, so C1/C2 are measuring my change and not something else.

I also negative-controlled the proof-of-spec checker itself before trusting its VALID: a claimed-
but-absent criterion → rc=1 coverage violation; a gutted `output_evidence` → rc=1 thin-evidence
violation. An instrument that cannot say INVALID is not evidence.

## Harness change

`scripts/ui-smoke.mjs` gained two **additive, optional** flags (defaults unchanged, so no existing
caller is affected): `--fail <substring>` (serve 503 — lets a degraded branch be *exercised*) and
`--console <substring>` (surface page console lines — lets a claim about what an accessor
*returns* be read off the run instead of the source). Both exist because C1/C2 demand an
exercised path.

## Bounds honored

- ⛔ **NOT an alarm authorization.** No alert, alarm, SNS, SES, monitor, freshness checker, or
  notification machinery. The moratorium is untouched. Existing UI + existing logs only.
- ⛔ **No direct PROD act.** Portal tree on `DEV` throughout (verified at start and after commit).
  Not pushed.
- **OUT, untouched:** the primary/fallback architecture; the 118-day target's restore-vs-retire
  disposition; footer-to-artifact binding as a general fix — the six `data_pkl` footers are
  unchanged.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `getAllReturns` / `dataAsOf` / `data_pkl` / `SmartPanelFooter` / `generated_at` over `portal/src` | Mapped the consumer chain with denominators (13 hits/403 files for `getAllReturns`). Confirmed only `dataLoader` reads the response `generated_at`, and **nothing** reads `TickerReturns.generated_at` → the optional-widening is safe. Located exactly **six** `data_pkl` footers on /market, corroborating the spec's "all six footers". |
| `comp-transform schema-check` | `MarketPerformance` (before + after) | Both: "All rendered fields match their response types." DE minimum for a component whose data props changed. |
| `comp-to` | `comp-to OPAL_ANALYST.EXP1` | Race-free per-session TO_ID (not written into shared `.agent_context`). |
| `proof-of-spec-check` | `... OPAL_ANALYST.EXP1_PROOF_OF_SPEC.json C1,C2,C3,C4` | **VALID, rc=0** — plus two negative controls that both correctly returned rc=1. |
| portal gate | `bun run typecheck` (`tsc -b --noEmit`), `bun x eslint <5 files>` | typecheck rc=0; eslint clean on all five changed files. |
| `ui-smoke.mjs` | 6 renders (degraded ×2, healthy AFTER, healthy self-control, healthy BEFORE, degraded BEFORE/mutant) | All landed `LOC /market` on canvas rgb(195,202,218). Supplied C1/C2/C3/C4 + mutant evidence. |

## Surprises (surface only — no action taken, per the surprise channel)

1. `portal/src/pages/ModelPortfolios.tsx:873` fails `bun run lint`
   (`react-hooks/preserve-manual-memoization`). **Pre-existing, not in my diff** — but `bun run
   lint` is `eslint .`, so it fails repo-wide regardless of paths passed. Any seat running the
   portal lint gate right now sees a red that is not theirs.
2. `getTickerReturns` (`market.ts:~283`) still does
   `generated_at: marketData.generated_at || new Date().toISOString()` — **the same defect as B**,
   one function over, feeding `IndexPerformanceModal`. Outside this TO's scope.
3. The `/market` local render **401s on both accessor legs** without backend credentials, landing
   on the terminal-failure path. So a default ui-smoke run has never exercised /market's primary
   leg — a fixture is required to render the healthy state at all. Matters to anyone reading a
   past /market smoke render as evidence about healthy-path behaviour.
4. The portal submodule has **no committer identity configured** (`git commit` → "Committer
   identity unknown"). I supplied one per-invocation via `git -c` rather than writing global
   config. Every portal-committing seat hits this.

## Next Steps

- [1.0.0_SA_CTO~Z] Validate the evidence and close (RAVC step 4). Two judgment calls to confirm or
  reverse, both stated plainly in my report: **(a)** spec **D** says the `:219` warn should "carry
  the artifact date" — at `:219` the artifact has not been fetched yet, so the date does not exist
  in scope; I kept `:219` as-is and added the dated warn at the first point where the date exists.
  **(b)** I folded the **per-ticker** `generated_at` synthesis into B as the same lie in the same
  leg; if you read B as the response-level field only, say so and I will revert that hunk.
- [DT / promotion owner] Standard DEV→PROD promotion when CTO~Z routes it. Nothing here authorizes
  a direct PROD act.
- [remediation queue] The three explicitly-OUT items, plus surprise #2 as a candidate.
