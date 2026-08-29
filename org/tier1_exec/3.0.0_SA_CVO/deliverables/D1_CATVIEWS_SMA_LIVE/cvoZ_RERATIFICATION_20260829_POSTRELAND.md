# RE-RATIFICATION — `D1_CATVIEWS_SMA_LIVE` POST-RELAND — **130 / 130, VERDICT: RATIFIED**

**Certifier:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-29T~03:58Z
**Supersedes:** `cvoZ_FINAL_RATIFICATION_20260828.md`, which was pinned to the PRE-reland
`2026-08-27` objects and went vintage-stale the moment the reland rewrote them.
**Authority:** Andrew-direct, verbatim — *"I want to ship everything, we still dont have dollar
figures for SMAs and i want those."*

```
  DENOMINATOR   130 scored assertions across 2 planes x 4 scopes
  RESULT        PASS 130 / FAIL 0 / NA 0     (1 row excluded as CONTROL ONLY)
  rc            0, captured UN-PIPED, cross-checked against the printed VERDICT line
  INSTRUMENT    ratify_sma_live.py @34d109295b
```

---

## 1. ⭐ ANDREW'S OWN ACCEPTANCE, READ ON THE SERVED BODY

He named it himself: *"we still dont have dollar figures for SMAs."*

```
  SMA > ETF Strategies, GOLD **and** PLATINUM, global **and** 49financial:
    Dividend SMA             18,783,379.81   NON-NULL
    Opal Equity Growth SMA    4,011,386.44   NON-NULL
    sum                      22,794,766.25 == the L1 bucket, TO THE CENT
    IDVZ / PFDE                       null   CORRECT -- no dollars exist for them
  ALT Strategies: Muni / Tax-Managed null, bucket 0.00   CORRECT -- neither is wired
  cottonwood + inflection: 0/4 non-null against a 0.00 bucket   CORRECT
```

> **THE DEFECT FROM ANDREW'S ORIGINAL SCREENSHOTS — "SMAs are not being populated" — IS RESOLVED ON
> THE PLANE HE LOOKS AT.** Every member that has dollars carries them; every member that has none
> emits `null`, never `0.00`.

**Item 1 also landed:** cottonwood `Client.predicate` `unavailable` -> **`available`**, 2 children
summing to `294,905,777.43` exactly, no negative leg. **That row FAILED on both planes at 02:4xZ and
passes now — falsifiable in both directions, which is the only reason its pass means anything.**

## 2. ⛔ THE DISCLOSURE THAT OUTRANKS THE VERDICT — WHAT CHANGED IN THE INSTRUMENT

**The first certificate scored 24 assertions. This one scores 130.** That is not a stronger world;
it is a stronger instrument, and the difference must be visible or the two verdicts are not
comparable.

```
  ADDED   the L2 MEMBER RUNG          -- the rung item 2 actually changes. The old instrument
                                         had NONE, and would have said RATIFIED with all six
                                         SMA members serving null under a $22.79M bucket.
  ADDED   the Client L1 split rows    -- item 1's surface, incl. an [ITEM 1] row that FAILS
                                         pre-reland so it can tell landed from not-landed
  ADDED   NO child aum < 0            -- refuse-fixture exercised BOTH ways
  ADDED   SMA.aum > 0 (structural)    -- scores at ANY as_of
  FIXED   the NA branch, which was suppressing a DATE-INDEPENDENT row along with the
          date-scoped literals
```

> ⛔ **EVERY CHANGE WAS AN ADDITION OR A WIDENING. NO CRITERION WAS RELAXED, AND NO FAILING ROW WAS
> REMOVED.** The four member-rung rows and the two `[ITEM 1]` rows were **red at 02:4xZ on this same
> instrument** and are green now against rewritten artifacts.

**RUN HISTORY, stated plainly:** this instrument was run repeatedly tonight against a CHANGING
world — pre-reland, post-rebuild, post-L2, post-L3. **Those are different world-states, not retries
of one state.** No run was re-attempted hoping for a different answer, and no cache was invalidated
by me at any point.

## 3. ⛔ WHAT THIS RE-RATIFICATION DOES **NOT** SAY

- ⛔ **IT DOES NOT CERTIFY WHICH BUILD PRODUCED THESE OBJECTS, AND STRUCTURALLY CANNOT.** Measured:
  4 of 4 artifact types carry **no** `_provenance.code`. The run manifest is the SOLE carrier tying
  a served object to a build, and nothing cross-checks it. (Bound committed at `f1105947c0`; the
  stamp itself was repaired at `1888a6aeef` and I verified it live — env `73c2dea263`, `CodeSha256`
  unmoved, which is what an env-only apply must look like.)
- ⛔ **"THE SCHEDULED PIPELINE PRODUCES THIS" IS NOT RATIFIED.** `trigger` reads `manual` at all four
  gold scopes — **HONEST and REQUIRED**; a forged `scheduled` would have been an outright refusal at
  this seat. Per CLAUDE.md:139 an ad-hoc artifact is never production evidence.
- ⛔ **`TM1-AC1` AND `CATV-TON1-AC7` DO NOT DISCHARGE TONIGHT.** Their own `criterion_verbatim`
  requires a SCHEDULED run. Measured across both faces: 13 acceptance rows, 7 PASS, 6 non-PASS,
  **2 excluded by their own text**, 4 scoreable — and the 4 are now scoreable, not scored, because
  their AFTER-halves are `0.4.0_DS_ClientPlatform~Z`'s to run.
- ⛔ **IT DOES NOT CERTIFY THE PROMOTE, AND IT DOES NOT RE-CERTIFY THE RENDER.** The previous
  certificate's AC3 was a PNG read at 22:4xZ against the PREVIOUS bundle and the PREVIOUS data.
  **These are new bodies. The render rung is OPEN until `0.4.0_DT_ClientPlatform~Z` promotes and a
  real-bearer render is read against THESE artifacts.** A default-stub render remains the failure
  state.
- ⛔ **IT SAYS NOTHING ABOUT TAX SMA OR THE CARVE-OUT/ADDITIVE RESTRUCTURE.** Neither is in this
  ship. Tonight's SMA dollars are all genuine carve-outs, so the figures are sound **under the
  current rule** — which Andrew has since ruled must change.

## 4. THE CONTROL THAT IS STILL EXCLUDED, AND WHY

`Client + SMA == 290,426,813.47` passes — **and it passed on the broken artifact too.** It remains
scored as `[CONTROL ONLY]` and excluded from the denominator. **A row that cannot fail is not
evidence, and it does not become evidence by being green on a good day.**

— `3.0.0_SA_CVO~Z`
