# 0.4.0_DE_ClientPlatform — repoints + read census + carried deletion + count field-read fix (0415-0530Z delta)
**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, VALIDATE, SCRIBE

## Window drivers (all Andrew-direct, recorded verbatim in the cited MCP messages)
As-of-line escalation at my terminal -> "run it direct to CTO" (042253Z) -> "all of the repoints need
to happen now... the genuine gap relayed to CTO immediately" (042530Z) -> CTO GO 042528Z + contract
043156Z/043555Z (THREE types per scope, Q1 one-timeseries) + derive-sanction 043631Z + repoint-now
nudge 043710Z -> COO carried-label reversal 042749Z + release 044951Z -> CTO quarterly fork
ratified server-side 045111Z -> CTO count-discrepancy order 051301Z.

## Shipped (portal DEV; f6c11812 PROMOTED as v2.1.150, 42b0f524 PROMOTED as v2.1.151; cfc1e879 +
## 70166741 on DEV awaiting DT promote #4)
- `42b0f524` (LIVE): Global bell curve re-pointed to platinum/mdpf/global/account-distribution.json
  via the mdpf family route; legacy getAccountDistribution/clearAccountDistributionCache RETIRED
  (zero callers). All four scopes now on the canonical distribution family.
- `cfc1e879`: (a) donut slices + account counts = field reads of the canonical global by_model at
  last real points (ratified SELECTION sanction; vintage-coherent with the headline; no-fallback:
  canonical absent => empty donut; caught own missing-dep bug pre-push). (b) carried "at declared
  cadence" treatment FULLY DELETED (band, bar outline, chips both charts, tooltip phrasing, + the
  stale DATA SOURCE sentence) -- machinery preserved in pairedProvenanceRead.ts per COO; page-side
  consumption removed. Quarterly per-model cells stay on labeled legacy per the ratified
  server-side fork (DS~A building platinum aum-metrics x3 scopes).
- `70166741` (CTO order 051301Z): Total Holdings and BOTH unfunded footnotes become FIELD READS
  (total.account_count = 7,597; total.excluded_unfunded_count = 49). RETIRED: the 2026-06-05
  sleeve-level client ADD (7,597+183 blend counts = the rendered 7,780) and the cross-artifact
  subtraction (legacy metrics 7,854 - 7,597 = the rendered 257). DistributionStats type extended
  with the publisher's optional stated fields. The sleeve-level business quantity ARGUED to CTO for
  a producer-side disposition (Andrew's own 06-05 semantic; never silently dropped).

## Delivered records
- READ CENSUS (CTO 044907Z, accepted 045111Z): 9 network reads enumerated with denominator;
  contract-key mapping; ZERO-READERS statements for BOTH retirements (legacy aum-timeseries -- A2
  write-kill safe; underscore twins -- AE~A sweep safe); benchmarks x2 + peers x1 named
  out-of-contract; quarterly derivability honestly argued AGAINST self (client cross-date deltas =
  producer territory; ratified).
- CORRECTION OF RECORD (052523Z + DT/COO variants): my 7,780/257 announce mis-ATTRIBUTED derived
  render values to the artifact; fixture-vintage hypothesis refuted (fixture WAS the served
  object); COO's "code is right, will render 7,597" premise also corrected (the tile derived).
  Lesson stated: a screenshot number is a RENDER fact, not an artifact fact -- say which you quote.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-surface-check (pre-commit blocking) | ModelPortfolios.tsx + aum.ts x3 commits | PASS w/ SEV1 ack | anchored in each pushed message |
| provenance-read-guard | src/** | PASS | after donut by_model reads (paired reader) |
| ui-smoke | /portfolios x6 + PROD origin x1 | PASS | happy/forced-fail per change; PROD read auth-walled (skeleton only) -- pixel closed by Andrew's own smoke |
| aws s3 ls platinum/mdpf (rail-checked) | presence census | PASS | grounded the canonical set before asserting to Andrew; found global account-distribution EXISTS + aum-metrics cottonwood-only |
What worked: measuring the platinum tree BEFORE answering Andrew (corrected my own half-wrong claim);
exercising fixes with the SERVED artifact as fixture. What failed: my announce attributed derived
render numbers to the artifact (corrected on record); first stamp attempt UTC-midnight off-by-one
(prior window, carried the lesson). Gap: sleeve_level_count + global/49f/inf aum-metrics +
benchmarks/peers canonicalization -- all named server-side, CTO routing.

## Current State (zero-prior-context)
- PROD: v2.1.151 (42b0f524). DEV ahead: cfc1e879 + 70166741 awaiting DT promote #4 (one promote,
  both oracles stated to DT 052541Z). Portal tree CLEAN on DEV.
- MDPF Global page reads: aggregate-aua-timeseries (all AUA surfaces incl donut slices/counts) +
  account-distribution (bell curve, counts, unfunded) BOTH canonical platinum; aum-metrics legacy
  ONLY for per-model quarterly cells + labeled "Model detail as of 2026-07-23" (dies on DS~A's
  platinum extension); benchmarks/peers out-of-contract, untouched.
- Carried machinery: pairedProvenanceRead.readGlobalCarriedDates intact, zero page consumers.
- Workspace CLOUD synced through the 0415Z log push; this log to commit.

## Next Steps
1. [0.2.0_DT_PortfolioAnalytics] promote #4 (cfc1e879 + 70166741); oracles in 052541Z.
2. [0.4.0_DS_ClientPlatform / DS~A] cottonwood G7 re-key P0 + platinum aum-metrics x3 -> quarterly
   cells re-point (mine, on exists-signal) + carried frontier self-clears.
3. [1.0.0_SA_CTO] sleeve-level count producer disposition + benchmarks/peers canonicalization.
4. [0.4.0_DE_ClientPlatform] standing: fix-lane hot through DT's promote.
