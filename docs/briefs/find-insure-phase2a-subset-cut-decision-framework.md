# FIND_INSURE Phase 2A subset-cut decision framework (Q1 ratify menu)

**Authoring:** `2.0.0_SA_COO` 2026-05-27T~23:22Z
**Purpose:** structure Andrew Q1 sovereign decision as a comparable option menu rather than open-ended request — reduces cognitive load, accelerates Phase 2A entry-gate clear
**Trigger:** Andrew goal-set 2026-05-27T~22:49Z "Drive end-to-end completion of FIND_INSURE through close of Phase 3" + CVO Mode B comprehensive (810211e17) Phase 2A STANDBY-PREP-READY status + .024 STAGED LIVE-DISPATCH gates explicitly on Q1
**Decision authority:** Andrew sovereign

---

## Context

Phase 1 universe-run (99-IMO crawl + silver + gold) is in flight. When Phase 1 closes, .023 emits `serving/scoring.json` ranking the 99 IMOs by `rollup_score` (0-100 continuous score with class-diversity multiplier).

Phase 2A entry requires Andrew Q1 ratify of the **subset-cut rule** that selects which IMOs progress to LushaAI LinkedIn enrichment (decision-relevant employees + Series-license counts + AUM extraction per .024). The rule directly determines:

1. **Phase 2A LushaAI cost** — Lusha API calls are per-employee + per-IMO; larger subset = higher cost (rough estimate $1-3/IMO at typical employee depth)
2. **Phase 2A wall time** — larger subset = longer to enrich
3. **Phase 3 ranked output completeness** — IR team only sees enrichment for in-subset IMOs; out-of-subset IMOs land in Phase 3 serving table with web-scrape-only signal

CVO §W1 finding flagged ambiguity: PRD §4 mentioned "top quintile + explicit Series-license mention" but **threshold semantics for the WM-classification label (present / adjacent / absent) NOT stated**. This menu structures Q1 against 4 concrete rule shapes.

---

## Option menu — pick one OR refine

### Option A — Top-quintile-only (simple, narrow)

**Rule:** select the top 20 IMOs by `rollup_score` (top quintile of 99). No Series-license sub-filter; no adjacent class.

**Phase 2A subset size estimate:** ~20 IMOs
**Cost estimate:** ~$20-60 Lusha (low end)
**Phase 2A wall time:** ~2-3h
**Trade-off:**
- ✅ Simplest rule; easy to explain to IR team
- ✅ Low-cost
- ❌ Misses "adjacent-class" IMOs that the rollup_score may under-weight (e.g., explicit Series-license mention on a low-page-count site that didn't get scoring lift from PRD §3.8 page-cap)
- ❌ Hard-cap at 20 means a 21st-ranked IMO with 100 score is excluded vs a 20th-ranked at 95 — discrete-boundary artifact

### Option B — Top-quintile + Series-license-mention adjacent (recommended; matches PRD §6 staged framing)

**Rule:**
- Tier 1: top 20 IMOs by `rollup_score` (automatic inclusion)
- Tier 2: any IMO scoring `rollup_score ≥ 50` (provisional adjacent threshold) AND with explicit Series-license term match in `term_matches[]` (Series 7/24/63/65/66/79) — included even if outside top-20

**Phase 2A subset size estimate:** ~25-35 IMOs (depending on Phase 1 distribution)
**Cost estimate:** ~$30-105 Lusha
**Phase 2A wall time:** ~3-4h
**Trade-off:**
- ✅ Matches PRD §6 staged framing verbatim
- ✅ Catches "adjacent" class IMOs per CVO §W1 mention — explicit Series-license is high-signal even on low-page-count sites
- ✅ Reasonable cost + wall time
- ⚠️ The `rollup_score ≥ 50` threshold is a provisional COO estimate; ws CTO REPAIR-AMENDMENT (b)(i) W1 threshold semantics PRD amend (in-flight per CVO Mode B finding) will likely refine
- ⚠️ Two-tier rule slightly harder to explain to IR team

### Option C — Continuous-threshold (rollup_score ≥ N)

**Rule:** select all IMOs with `rollup_score ≥ N` where N = Andrew-chosen value (e.g., 60 or 70). No top-quintile constraint; no Series-license sub-filter.

**Phase 2A subset size estimate:** depends on N + Phase 1 distribution
- N=70: likely ~10-15 IMOs (narrow)
- N=60: likely ~15-25 IMOs (medium)
- N=50: likely ~20-35 IMOs (broad)
- N=40: likely ~30-50 IMOs (very broad)

**Cost estimate:** $30-150 depending on N
**Phase 2A wall time:** 3-5h
**Trade-off:**
- ✅ Cleanest rule (single threshold); easy to defend
- ✅ Andrew controls subset size directly via N
- ❌ Doesn't catch the "adjacent" class that explicit Series-license signals (a 45-score IMO with Series 65 mention may be more decision-useful than a 65-score IMO without)
- ⚠️ Threshold value is somewhat arbitrary without Phase 1 distribution data; recommend Andrew pick AFTER Phase 1 close so distribution is empirically known

### Option D — Top-N absolute (top-30 OR top-50 by rank)

**Rule:** select the top N IMOs by `rollup_score` regardless of score value, where N = Andrew-chosen (recommend 30 or 50).

**Phase 2A subset size estimate:** exactly N
**Cost estimate:** $30-150 depending on N
**Phase 2A wall time:** 3-5h
**Trade-off:**
- ✅ Deterministic subset size; predictable cost + wall
- ✅ Easy to explain to IR team
- ❌ Same discrete-boundary artifact as Option A (Nth vs N+1th IMO)
- ❌ Doesn't catch adjacent-class signals
- ⚠️ Risk of saturated-top class — per CVO Step 3.5 CONCERN-meaning finding, rollup_score 100-cap means many top-N may all hit 100 (degraded discrimination at the top)

---

## Recommendation — Option B (top-quintile + adjacent-Series)

**COO recommend Option B** for the following reasons:

1. **Matches PRD §6 staged framing** — minimizes documentation drift; ws CTO's PRD amend chain naturally absorbs
2. **Catches adjacent-class explicitly** — the "WM-program OR may be adjacent" language from Andrew's mandate becomes operational
3. **Reasonable cost-window** ($30-105) — well below any sovereign cost concern
4. **Explainable two-tier rule** — IR team sees "top quintile + Series-licensed near-tops" which maps to intuitive notion

**If Andrew prefers Option A or D for simplicity:** acceptable trade-off; loses adjacent-class catch but gains explanatory simplicity. .024 design absorbs either rule shape without re-cycle.

**If Andrew prefers Option C with N=60:** also acceptable; cleanest rule + Andrew tunes N. Recommend deferring N selection to post-Phase-1-close moment when distribution is empirically known.

---

## What needs Andrew explicitly

Just answer ONE of:

```
Q1 ratify: Option A | Option B | Option C(N=__) | Option D(N=__) | refined: [your rule]
```

That's it. The framework above captures the trade-offs; Andrew makes the call.

---

## What happens post-Q1-ratify

1. ws COO authors `data/find/imo/config/phase2a-subset-rule.json` quoting Q1 verbatim + the algorithm operationalization
2. AE 0.7~A confirms Phase 1 RAVC2-Accept (gates Phase 2A entry)
3. DS~C executes FIND_INSURE.024 LIVE-DISPATCH per .024 ACs against the Q1-rule-derived subset
4. Phase 2A LushaAI silver + gold + serving emit
5. Phase 3 entry: .022 + .023 final close mechanics

ETA Phase 2A complete post-Q1 + post-Phase-1-close: ~5-8h wall (LushaAI calls + per-employee scoring + serving emit). Independent of Phase 2B (HAR-staged) which runs parallel.

---

## Sister context

- **Q1 is one of 3 Andrew sovereign gates** for FIND_INSURE Phase 3 close. The other 2: HAR captures for Phase 2B Stage Bα (gates `.025` execution) + IR-team consumer individual identification (gates Phase 3 close-sign-off per CVO ADDITIVE-1). All 3 can be answered in parallel; any one cleared compresses ~6-12h off the Phase 3 close ETA.
- Andrew goal-set 2026-05-27T~22:49Z "drive end-to-end through Phase 3 close" is structurally multi-day per Lambda compute + Andrew gates + IR-team sign-off windows; answering Q1 now collapses Phase 2A entry-gate (single highest-leverage compression move).

— ws COO 2.0.0_SA_COO 2026-05-27T~23:22Z — Phase 2A Q1 subset-cut decision framework (Andrew gate-clearer)
