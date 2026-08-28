# RATIFICATION — `D1_CATVIEWS_SMA_LIVE` — **AC1 · AC2 · AC3 · AC5 RATIFIED**

**Certifier:** `3.0.0_SA_CVO~Z` · **Issued:** 2026-08-28T~22:4xZ
**PRD:** `docs/architecture/D1_CATVIEWS_SMA_LIVE_PRD.md` @`f0ac3a5db9`
**Authority:** Andrew-direct — *"I want this entire product done in this session … finished pipeline,
finished frontend display, and new promote with all of it live"*; reland gate *"yes reland once all
fixes are in."*

```
AC1  gold, 4 scopes, at the S3 BODY              RATIFIED
AC2  platinum, 4 scopes, at the SERVED BODY      RATIFIED   (+ body as_of, key is UNDATED)
AC3  PROD render, REAL bearer, screenshot READ   RATIFIED at global (bound in §4)
AC4  dollar conservation                         CONTROL ONLY — NOT SCORED (degenerate)
AC5  served bundle                               RATIFIED   (hash + content, both legs)
```

---

## 1. WHAT IS TRUE ON PRODUCTION NOW

**The $22,794,766.25 of SMA that the served plane was reporting to advisors as an affirmative
"A TRUE ZERO" is now correctly allocated, served, and rendered.**

```
  GOLD + PLATINUM, both planes, all four scopes, read at the BODY:
    global       SMA 22,794,766.25   Client 267,632,047.22   absent_reason ABSENT
    49financial  SMA 22,794,766.25   Client 267,632,047.22   absent_reason ABSENT
    cottonwood   SMA 0.00            absent_reason PRESENT      <- Direction B INTACT
    inflection   SMA 0.00            absent_reason PRESENT      <- Direction B INTACT
    platinum body as_of == 2026-08-27 at all four -> it PROPAGATED, not a stale object at
    the same undated key.  (my added stop-condition 5, DISCHARGED)
  RENDER, PROD /portfolios, Global (All), real RS256 bearer, PNG READ:
    ASSET CATEGORY VIEWS  As of 2026-08-27
      Models $1.80B (Custom $51.90M · Primary $1.75B) · SMAs $22.79M · Client, no fee box
      "Fixed Income" draws VIOLET in both legends (D-3, canonical not positional)
  BUNDLE:  index-Ce258d2k.js -> index-BMmU0cpj.js, Last-Modified 22:29:35Z
           "Fee split unavailable" 1 -> 0   with "Asset Category Views" 1 -> 1 as the control
```

## 2. ⛔ THE DISCLOSURE THAT OUTRANKS THE VERDICT

**AC1/AC2 attempt 1 read NOT RATIFIED. Attempt 2 passed because I CHANGED MY OWN CRITERION — the
artifacts were byte-identical between runs.** The 24 substantive rows passed on attempt 1; all four
failures were mine.

I asserted `"adhoc" in _provenance.trigger` **against the ARTIFACT**. Measured at source:
```
  consolidator :1469-70  artifact kind enum is EXACTLY  scheduled | s3-marker | manual
               :1148     RUN MANIFEST -> "trigger": trigger             (whole dict; 'adhoc' IS here)
               :1398     ARTIFACT     -> "trigger": trigger.get("kind")  (KIND ONLY -> 'manual')
```
**I read the MANIFEST's shape onto the ARTIFACT — a GRAIN error, and I required a value the producer
CANNOT EMIT.** That is a criterion a correct build cannot satisfy: the exact class I spent the
evening certifying against. `0.7.0_AE_CloudOps~Z` caught it independently and named the split more
precisely than I had; `2.0.0_SA_COO~Z` sent the same warning. **Three seats, and the one who was
wrong held the instrument.**
The correction is to the WORDING, not a relaxation. Negative control run BEFORE re-scoring:
`manual` ACCEPT · `s3-marker` ACCEPT · **`scheduled` REFUSE · `aws.events` REFUSE · `None` REFUSE.**

## 3. ATTEMPTS AND CACHE — per the binding disclosure rule

```
  AC1/AC2   attempts 2   criterion changed between them (§2). NO invalidation. NO world retry.
  AC3       attempt  1   first-attempt pass. Bearer minted once, spent on this act.
  AC5       attempt  1   first-attempt pass.
  EDGE      no invalidation performed at any point, by me or (per 14392) needed:
            bundle is self-invalidating by content-hash; the data object measured X-Cache MISS.
```
**A pass after N retries would have been evidence a cache expired. These are first-attempt passes,
except AC1/AC2 where what changed was my criterion and I have said so in the verdict itself.**

## 4. ⛔ WHAT THIS RATIFICATION DOES **NOT** SAY

- **IT DOES NOT CERTIFY THE PROMOTE.** The payload was **16 commits; 4 are ours** (`1.0.0_SA_CTO~Z`,
  14371). The other 12 — ADVI_PERFRP ×8, Positioning per-book dates, a docblock, merges — are
  **UNVERIFIED BY ME. Unverified is NOT doubted:** I have no finding against any of them and no
  reason to suspect them. **I did not look**, and an absence of examination must never be reported in
  language resembling an absence of defects.
- **THE 49financial RENDER IS NOT MEASURED BY ME.** I rendered Global (All) only. The data is
  ratified at 49financial (AC1/AC2); the *render* at that scope is inference from a shared component,
  and `0.4.0_DE_ClientPlatform~Z` holds the pixel plane independently.
- ⛔ **"THE SCHEDULED PIPELINE PRODUCES THIS" IS NOT RATIFIED AND CANNOT BE TONIGHT.**
  `trigger = manual` is HONEST and REQUIRED — a forged `aws.events` would have been an outright
  refusal — but per CLAUDE.md:139 an ad-hoc artifact is never production evidence. **Monday
  2026-08-31's scheduled fire settles it, and must be scored STRUCTURALLY:** AC1's literal is
  market-valued (`opal_div_sma` + `opal_growth_sma`, ~$170–250k/trading-day drift) and **would FAIL
  Monday's correct artifact.**
- **AC4 is excluded from scoring**, not passed: it is satisfied by the pre-fix artifact.

## 5. THE INSTRUMENT'S OWN RECORD

Seven defects were found in this ratifier **by exercising it**, none visible from reading it. Every
one would have fired at acceptance: a broken fetch scored as a refusal (its negative control PASSED
while it had never read an object); a blacklist where a positive expectation belonged; a guessed
platinum bucket **and** key shape; a trigger assertion on the wrong plane; an ungated date-scoped
literal; the `adhoc`/`manual` grain error; and a **piped `$?` that reported rc=0 on a NOT-RATIFIED
run** — which `1.0.0_SA_CTO~Z` then made binding on every step-5 run.
> **The last one is the one to keep: a correct instrument, a correct verdict, and the operator
> reading a different number than the one it produced.**

— `3.0.0_SA_CVO~Z`
