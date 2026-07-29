# 0.4.0_DE_ClientPlatform — MDPF headline field-read + fallback census + codeMap verification + carried-point idiom (0200-0335Z)
**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, TRACE

## Window
Fresh session 0200Z (post fabric-reset launch) -> 0335Z. Tasking: MDPF_RESET_DIRECTIVE WO-3 follow-on
(CTO dispatch 015529Z + Amendments 2/3 + 0204Z cache clarification, all Andrew-sovereign) + CTO codeMap
dispatch 192358Z + COO carried-point ruling 023731Z + Andrew 0315Z post-promote sightings.

## Shipped (portal DEV, pushed; PROMOTED to PROD tonight per DT under CTO GO 023703Z + COO-recorded assent)
- `d0fb493e` fix(MDPF Global headline): the headline is a FIELD READ of `opal_aggregate_aua` at its
  last real point — the `:1170-1171` client composition (trend model sum + `non_model_assets.json`
  roll-forward) AND the `:1172 .latest` fallback DELETED, not bridged; `trendLastPoint` + the
  `modelAUM` reduce died with them. NO fallback retained: canonical unreachable => honest absence
  (`AUA_UNAVAILABLE` em dash) at both render sites (donut centre `:1535`, AUMGrowthMetrics
  `aumDisplayOverride`), never $0, never a recomposed number. Renders $1.95B (1,950,519,805.86
  @ 07-27) vs prior $1.91B.
- `1e4bdf14` follow-up: unused `readAllModelSeries` import dropped (the deletion's own signature;
  CI ESLint) + the `^`-anchored `SURFACE_ACK:` line carried IN the commit message (CI extracts from
  the pushed message; the local env ack does not travel — DT 024235Z, Andrew-direct 0244Z).
- Exercised before commit (ui-smoke, fixtures = live platinum artifact pulled from S3): happy path
  $1.95B; DISCRIMINATING CONTROL canonical-dead + all-four-legacy-alive => em dash (the state that
  painted DT's 403-window legacy 1.78b); all-dead => em dash + N/A. Screenshots in session scratchpad.

## Delivered (workspace CLOUD, pushed @ 68661972ab)
- `87b3ce7e2e` MDPF_FALLBACK_ROUTE_CENSUS_20260729.md (Amendment-3 D2): source-read denominator
  (10 fetch routes + 2 module caches + 5 fallback/derivation branch clusters + 1 zombie) +
  forced-failure exercise. Headline items: B1-B4 legacy `json/portfolios/*` feeders (charts/donut/
  quarters/bell-curve), C2 `endpoints/aum.ts` getAUMMetrics catch FABRICATES a zero AUM structure,
  C4 the `:849-894` legacy graceful-degrade trend branch (exercised live), C5 scope-less
  `getMdpfAggregateAUATimeSeries` zombie (0 callers), D1a-g remaining client derivations mapped to
  canonical fields / server-side gaps, B5 benchmarks/peers no-canonical-location design gap.

## Verifications (all accepted)
1. codeMap defect (CTO 192358Z): 1-of-7 re-confirmed live; RENDERED IMPACT: /attribution AGG (via the
   top-panel selector; SelectionTab's own selector filters AGG out `:347`) renders Intermediate's
   book verbatim — 13+ rows at 0.00, BIV 8.40 == INT view; /positioning IMMUNE (HoldingsTab pinned
   const 'Current' `:526`; server `current_holdings.AGG`; defective branch UNREACHABLE dead code).
   THIRD map found: FactorTilts `constants.ts:199` carries the CORRECT hyphenated map + zero-warn +
   normalization. Second defect class: 2 blend cohorts ($39.3mm) absent from every map + hardcoded
   5-code list. CTO rulings: interim = second-change member #2 (canonicaliser + N-of-N loud assert;
   blends = DECLARED EXCLUSION labeled, never client 50/50); durable = server-computed AGG in
   holdings_attribution_data.json (routed DS/publisher); dead-branch deletion rides the wave.
2. Andrew 0315Z sighting (1): Global trend 1.91b = CLIENT-SIDE confirmed to the cent
   (1,672,708,163.51 + 232,313,972.65 = 1,905,022,136.16 == DT trace; artifact carries
   1,950,519,805.86). Second-change member #1 per CTO resequencing (chart reads the artifact SERIES).
3. Andrew 0315Z sighting (2): Cottonwood trend frozen 07-22 = SERVER-SIDE confirmed (served platinum
   cottonwood `model_aua` last non-null 2026-07-22, nulls to 07-27, custody all-null — nothing
   fresher to truncate; heal = DS G7 re-key, no portal work).
4. Fabricated-zeros write-up to COO (own item, ruled catch-law: a fetcher's catch may return
   null/throw, NEVER a number): getAUMMetrics catch-zeros consumed by ModelPortfolios satellites +
   FactorTilts (silently weights on totalAUM=0 — pulled forward of the wave per COO).

## Built, HOLDING LOCAL (uncommitted; per COO STOP 030012Z + approved sequence)
Carried-point visual idiom per COO ruling 023731Z: new `readGlobalCarriedDates` in
pairedProvenanceRead.ts (the one guard-allowlisted module) reading PARTNER-LEG cohort_provenance —
never the rolled-up point_class (which reads 'measured' on all 3 carried frontier dates, the ruled
trap). Renders: neutral-slate ReferenceArea band + right-anchored label (daily chart), slate-outlined
DATE-EXACT period-end bar, legend chips, tooltip leg+as-of detail. Three classes preserved
(measured / carried / interpolated — never collapsed; carried wears the count-basis neutral idiom,
alarm vocabulary unspent). PREDICATE INCIDENT (disclosed to COO): first draft marked 'absent' legs
carried -> banded 400 of 450 dates (cottonwood pre-onboarding); caught by measuring the leg
vocabulary before review; also cut the wall-clock as_of<date fallback (NEVER#1 class). Final:
carried iff the producer's class string DECLARES it. Typecheck clean, lint 0 errors, provenance
guard PASS, exercised on live-artifact fixtures (band = exactly 07-23..07-27).
Awaiting: (a) DT landed/aborted report, (b) COO idiom OK -> then commit (SURFACE_ACK in-message) + push.

## MCP traffic
~20 messages handled. Significant: CTO dispatch 015529Z + Amendments 2 (015951Z) / 3 (020253Z) /
cache-clarification (020409Z); my headline report 023616Z (+DT/COO CCs); DT CI-red 024235Z ->
re-push confirm 024632Z; COO STOP 030012Z -> measured assent 030134Z -> COO approval 030214Z; COO
carried-point ruling 023731Z; fabricated-zeros write-up 024831Z; codeMap report 030946Z -> CTO
acceptance 031043Z; Andrew-sightings verdicts 031651Z; carried-point review package 033422Z.

## Blockers
None assumption-based. Two explicit external gates on the carried-point push (DT promote report +
COO idiom review), both evidence-cited above, both owners named.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-transform schema-check | ModelPortfolios | WARN | types-resolution only (types live in api modules, pre-existing); no MISSING props |
| provenance-read-guard (portal test) | src/** | PASS | ran at push + after the new reader; opal_aggregate_aua not a guarded field, cohort_provenance read added INSIDE the allowlisted module |
| ui-smoke (frontend-dev instrument) | /portfolios, /positioning, /attribution | PASS | 8 renders: happy-path, 2 forced-failure controls, AGG-click defect render, 3 carried-band iterations, hoverlast DOM tooltip read |
What worked: schema-check as the pre-edit gate; ui-smoke fixtures-from-live-S3 as the forced-failure
harness (Amendment 3's method executed literally). What failed: nothing; the comp-rail was not
needed for raw estate search (all reads scoped files or operational aws). Gap: none new — the
census itself documents the estate gaps.

## Current State (zero-prior-context handoff)
- Portal DEV == origin/DEV == `1e4bdf14` (PROMOTED to PROD tonight by DT). Working tree carries ONE
  uncommitted feature: carried-point idiom (src/lib/pairedProvenanceRead.ts + src/pages/
  ModelPortfolios.tsx), gates green, screenshot `scratchpad/mdpf_carried_final.png`, held for
  DT-report + COO-OK then commit/push with in-message SURFACE_ACK.
- Workspace CLOUD pushed @ `68661972ab` (census + this log's window).
- Second change (CTO-sequenced, NOT tonight): #1 Global chart trend -> artifact series field-read ·
  #2 FactorTilts catch-law fix · #3 codeMap interim (canonicaliser + loud N-of-N; blends declared-
  excluded + labeled) · + C2/C3 honest-error replacement, C5 zombie deletion, B1-B4 teardown,
  isLoading re-key (B2). Durable: server-side AGG (DS/publisher, CTO gate) + D1a/c server fields.
- Cottonwood chart heals on DS G7 re-key (post-fires) — no portal work.

## Next Steps
1. [2.0.0_SA_COO] carried-point idiom review (screenshot in scratchpad; heavier band border is a
   one-line change if wanted).
2. [0.2.0_DT_PortfolioAnalytics] promote landed/aborted report -> releases my portal push hold.
3. [0.4.0_DE_ClientPlatform] on both: commit + push carried-point, screenshot re-verify, report.
4. [1.0.0_SA_CTO] second-change GO when the window opens; census + verdicts carry the specs.
