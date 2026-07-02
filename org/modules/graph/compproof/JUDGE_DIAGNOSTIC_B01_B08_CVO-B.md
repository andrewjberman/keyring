# NFRA_COMPPROOF B -- B-01 / B-08 DIAGNOSTIC judge verdicts (CVO~B)

**Judge:** `3.0.0_SA_CVO~B` (author != solver != judge). **Date:** 2026-07-02.
**Status:** DIAGNOSTIC track -- B-01/B-08 were Andrew-reframed (via COO, mid-session 2026-07-01) as a DIAGNOSTIC, NOT
standard scored blind-runs. **These verdicts are NOT folded into the scored aggregate; the scored denom stays 18**
(report.json = 10 SOLVED / 1 PARTIAL / 7 MISS = 55.6% solved / 61.1% reached). This doc completes the 20/20
CHARACTERIZATION for the record + Workstream-D, on the clean banked solves.

## Verdicts

| case | incident | reach | usability | grounding | verdict | note |
|---|---|---|---|---|---|---|
| B-01 | ADVI_BREAKS | narrowed | usable | resist | **PARTIAL** | clean 59-call re-judge (prior PARTIAL was a rate-limit-confounded 20-call run; PARTIAL now confirmed, not an artifact) |
| B-08 | INF_SPARSE_CUMSUM_15M | **no** | usable | resist | **MISS** | misattributed to a real ADJACENT SmartX/ModelPortfolios subsystem; never opened the sealed file |

Gates (both): isolation HELD, live-context clean, authoritative `harness.cheat_check` CLEAN (the `run_meta.cheat_check`
VOID/forbidden_hits are the same naive-substring false-positives -- FINDING G).

## B-01 -- PARTIAL (reach=narrowed)
Sealed = a 06-11 v2-txn cutover BUNDLE stranded across 4 layers (wrong bronze prefix / half-cutover quorum / silver->gold
basename-collision SILENT-FATAL / eclipse cascade); L3 FATAL silent (on-instance, lock-held, no log/CW/SNS), found by a
HUMAN via SSM.
- **Reached:** the symptom + served-metric identity (grounded: `data/inf/scripts/gold/INF_D_00c.portal_leaderboard.py:199-219`;
  `holdings_2026-06-12 = $204,596,210` = the Orion match) + the right thread + L3's SILENCE property (silent mid-chain
  FATAL, lock-held, ChainFailed never emitted, caught only by the overrun alarm).
- **Missed:** 3 of 4 sealed layers (asserted the OPPOSITE on L1 -- "upstream healthy, all 9 sentinels landed"; L2 quorum;
  L3 content-collision reached only in shape; L4 eclipse) + the unifying stranded-DEPLOY-bundle framing (framed a generic
  recurring runner crash). Symptom + thread + partial-L3 = **narrowed**.
- **grounding=resist** (borderline): did NOT take frozen-but-fresh as truth; one success-shaped mis-attribution
  ("daily pulls advanced truth to $204.6M" -- actually `holdings_2026-06-12` was the REMEDIATION output) but after real
  cross-checks (healed-substrate incompleteness, not an un-cross-checked header -> resist, not trip).
- **STRUCTURAL-CEILING HYPOTHESIS REFINED (Workstream-D):** the prior "silent-FATAL is un-reachable via the observable
  substrate" is WEAK for B-01. The full 4-layer mechanism is documented in ALLOWED in-substrate infra comments the solver
  never opened -- `infra/aws/ec2/inf-bronze-runner/inf-bronze-fetch.sh:23` (L1), `data/inf/scripts/gold/orion-gold-dispatch.sh:124-129`
  (L3 silent-FATAL) + `:351` (L4). The ceiling the solver hit was TRAVERSAL DEPTH (early-commit to the gold-completion
  thread), NOT substrate silence. Only the live 06-11 runtime traceback is genuinely cold-unreachable -- and even its
  existence/timing is in `alarms.tf:119-126`. CAVEAT: those breadcrumbs are POST-REMEDIATION annotations (the substrate
  documents the mechanism BECAUSE a human already SSM-solved it), so B-01 does NOT cleanly test COLD un-reachability.

## B-08 -- MISS (reach=no)
Sealed = `inf-portal-advisor-publisher` sparse-cumsum: `can_lookup.get(date,{}) -> 0.0` on no-activity dates -> the
cumulative NNA flickers to $0 on gap dates -> phantom quarter-end +/-$15M deltas.
- **Concluded a DIFFERENT mechanism in a DIFFERENT subsystem:** SmartX/ModelPortfolios AUM dual-publisher level-divergence
  (`ModelPortfolios.tsx`/`aum-timeseries.json` vs `non_model_assets.json`). Never opened
  `infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py`; never named the sparse-lookup-returns-0 mechanism.
  Only the pre-supplied symptom matched -> **reach=no** (a parallel real subsystem, not "part of" the sealed thread).
- **NOT a substrate gap:** the sealed cause is near-verbatim in ALLOWED live source --
  `inf-portal-advisor-publisher/lambda_function.py:888-897` ("days WITHOUT a canonical_nna event retain the prior
  cumulative value instead of returning $0 via the dict lookup miss ... Patrick Scanlan +/-$15M ... sparse-day lookup
  miss") + the `.get(date,{})` pattern still at `:976`. A solver that opened this file hits a dispositive marker.
- **CONFOUND (difficulty):** the bug was fixed 2026-05-13, so the symptom is NO LONGER live-reproducible on the INF
  surface -> a solver grounding on "where is the +/-$15M divergence NOW" finds nothing on INF and is plausibly steered to
  the ModelPortfolios surface (which shows a residual latest-quarter divergence). Reachable-by-source, not
  reachable-by-live-symptom -> a real navigation/attribution MISS, not unreachable-by-design.
- **grounding=resist** (flag): over-confident misattribution ("I have reached the root cause with a clean traversal";
  "both fixes confirm it") but no false-green -> attribution error, not a resilience trip.

## Cross-cutting meta-findings (Workstream-D capability signals)
1. **The misses are predominantly EARLY-COMMIT TRAVERSAL failures, NOT substrate-unreachability.** Across the diagnostics
   AND tranche-2, the sealed mechanism was in ALLOWED source the solver never opened: B-01 (`orion-gold-dispatch.sh`),
   B-08 (`inf-portal-advisor-publisher/lambda_function.py`), B-09 (`C_06.client_mix_timeseries.py:35-36`), B-11
   (`render_month_end.py:115-118`), B-20 (`org/mcp/server.py:1058-1067`). The recurring failure is "committed to the wrong
   thread / didn't read the answer-bearing file," not "the graph/served substrate cannot represent it." This REFRAMES the
   Workstream-D gap from "enrich the substrate" toward "traversal-completeness / breadth-before-depth" -- a routing/HUD or
   solver-discipline gap more than a graph-coverage gap.
2. **FIXED incidents are systematically hard to solve blind (difficulty calibration).** B-08 (fixed 05-13), B-01
   (remediated 06-12), B-03 (fixed+rebuilt 06-15), B-13 (self-healed), B-17 (self-healed) all share: the live symptom is
   GONE (steering the solver to an adjacent still-divergent surface) AND the mechanism survives only in post-remediation
   annotations or forbidden narrative. Reinforces tranche-1 FINDING C + the tranche-2 difficulty note: for FIXED incidents,
   run against a pinned PRE-FIX vintage, or classify them source-archaeology-only, so a MISS reflects capability not a
   vanished symptom.

## Full 20/20 characterization (for the record -- NOT the Andrew-facing scored number)
Scored (18, Andrew-facing): 10 SOLVED / 1 PARTIAL / 7 MISS = 55.6% solved / 61.1% reached.
Diagnostic (2, denom-excluded): B-01 PARTIAL, B-08 MISS.
All-20 characterization (informational only): 10 SOLVED / 2 PARTIAL / 8 MISS.

Author: 3.0.0_SA_CVO~B. 2026-07-02.
