# Canon-Motif Scorecard -- FIRST-PASS census (NFRA_DEBTSCAN TO-D3)

**Author:** 0.7.0_AE_CloudOps | **Date:** 2026-06-18 | **Status:** FIRST-PASS (3 of 4 classes census-probed via comp-kuzu; full Python scorer-tool + PIPELINE class + AC4 novel-candidate adjudication PENDING)
**Canon:** org/modules/graph/canon-patterns.yaml v0.1 (ef6110129) | **Suppression:** org/modules/graph/debtscan/suppression_v1.yaml (18 active)
**Freshness:** comp-kuzu canonical, Nessie HEAD CURRENT (pin==marker), snapshot 3470176063981055398 (built 2026-06-18T13:13Z). 0 mutations.

> Honesty note: this is the census GROUND-TRUTH gathered while building the scorer, NOT the final scorer output. The actual deliverable (the registered Python scorer tool + the >=1 CVO-verified NOVEL deviation for AC4) is the remaining build block. Twin-shadow and suppression clearances are kept SEPARATE per the canon.

## SERVED_LINEAGE_CANON
- **DOMINANT motif:** resolved-served `(ServedURL)-[SERVED_FROM]->(backing S3 node)` = **29/45 instances (64%)** -- clears the >=60% dominant threshold.
- **OUTLIER tail (16):** two sub-shapes:
  - 4 `dangling_served` -- `/api/general/{positioning/model, sentiment/articles, sentiment/aaii-history, sentiment/aaii-latest}.json`. **NOT a novel deviation:** P4-ground-truthed (this session) as absent-object stale-FE URLs; the canon itself names these "VISIBLE-unresolved, not a false edge" -> KNOWN-DISPOSITIONED.
  - 12 family-deferred -- non-`/api/general` (`/api/private/*`, `/api/scoped/*`, `/aum/summary`, `/returns/etf-periods`, `/v1/sentiment/*`). Await the extract_routes follow-on (CTO 1f939f219 covers /api/general only); expected-unresolved, not a deviation.
- **recompute_fork enumeration DONE:** FLOWS_TO kinds = recompute/guarded 482 / passthrough 337 / rename 142. Of the 482 recompute/guarded, only 23 carry a non-null `condition` (the genuine guarded-fork pool; the other ~459 are field-read prop-access resolved via TypeChecker getSymbol, condition=null -- not cohort forks). Of the 23, firm-identifier symmetry test: `inflection_wealth_management` = 4 hardcoded conditions, `49financial`/`cottonwood`/`demo` = 0/0/0 -> ASYMMETRIC. **=> AC4 CANDIDATE (below).**

## *** AC4 CANDIDATE (novel canon-deviation, ADVISORY -> CVO adjudication) ***
- **Class:** SERVED_LINEAGE_CANON / recompute_fork -- the canon's `cross-firm conditional asymmetry` incident-anchor.
- **Finding:** the `_shared/` AdvisorIntelligence tabs inline-hardcode an inflection-only name-display fork -- `advisor_id === 'inflection_wealth_management' ? 'Unassigned' : name` -- at AdvisorsTab.tsx:374, AdvisorsTab.tsx:420, ClientsTab.tsx:291 (3 source sites -> 4 FLOWS_TO recompute/guarded edges to LeaderboardEntry#name + ClientsTab:291#name). Source-ground-truthed (git -C portal grep), not just a graph artifact.
- **Asymmetry (the deviation):** ONLY inflection is special-cased; 49financial/cottonwood/demo have 0 equivalent name-forks. So it is NOT a symmetric designed per-firm twin (twin_shadow_guard does NOT clear it).
- **NUANCE (honest, for adjudication):** a DECLARED per-firm framework EXISTS (`_shared/hooks/useTenantLayout.ts` dispatcher + `CanonicalFirmId` type '49financial'|'inflection'|'cottonwood'|'opal-capital'|'demo' + per-firm LAYOUT configs). This name->'Unassigned' rule does NOT route through it -- it's an inline magic-string fork, undeclared IN THE FRAMEWORK. So the canon-deviation = "an asymmetric per-firm fork expressed inline rather than via the existing declared per-firm config." NOT asserted as a clean bug.
- **Gates:** twin_shadow_guard = NOT cleared (asymmetric). suppression_v1 = NO match (the 18 active FP classes are graph-modeling-gaps / IAM-Deny / Day-0 auth -- none cover a render-fork asymmetry; DAY0_ADVISOR_INTELLIGENCE_AUTH_NONE is API_ROUTE auth, a different type+concern). => files ADVISORY (0 mutations), routes to CVO.
- **For CVO/CTO (canon author):** adjudicate -- is the inflection name->'Unassigned' an intentional display rule that SHOULD be declared as a tenant-config flag (debt: inline magic-string vs the declared framework), or acceptable as-is? AC4 = this candidate CVO-verified as a true deviation (or replaced if CVO rules it FP -> then suppression_v1 gains a new class).

## AUTH_CANON
- **Raw census:** API_ROUTE 77 + ServedURL 45, ALL with `TRIGGERS`-outbound = 0.
- **Suppression gate (the point of the class):** a naive `missing_auth_edge` scorer files 122 RED. ALL are cleared by suppression: `FP_API_LAMBDA` (API_GW->Lambda INVOKES edges absent, 0 API_GW outbound) + `FP_LEDGE` (Lambda@Edge fires on CloudFront viewer-request, not a TRIGGERS edge). -> **census-clean vs suppression: 0 filed RED** (demonstrates AC3/AC4 "0 double-fire of known FPs"). This is the graph TRIGGERS-modeling gap, NOT an auth-bypass.
- A genuine `missing_auth_edge` requires a DIFFERENT signal than the (unmodeled) TRIGGERS edge -- e.g. a served route reaching S3 with no auth on the *behavior* via comp-routes, not the graph TRIGGERS. Scorer-scoping finding.

## DEPLOY_CANON
- **Census:** 20 S3 buckets carry runner (EC2/LAMBDA/ECS) READS edges -- but these are DATA reads at BUCKET grain (opal-data-*), not `code/`-prefix reads.
- **Scoping finding:** the canon DEPLOY motif `(S3 'code/' prefix)-[READS]->(runner)` is NOT scorable on the canonical graph as-is -- the graph models S3 at bucket grain, no `code/`-prefix nodes. `orphan_code_prefix` / `runnerless` need the **deploy-ledger cross-ref** leg the canon's `graph_source` names ("canonical ... + deploy-ledger cross-ref"), not the canonical graph alone. PENDING in the scorer build.

## PIPELINE_CANON
- **Censused via comp-pipescript** (25 named threads / 134 sub-threads; the pipeline interior lives in the pipescript flow graph, not the canonical DB). SCORER-DESIGN FINDING: the PIPELINE class DELEGATES to pipescript (query-don't-rebuild, Rule 20) -- pipescript already enumerates producers->served->frontend + emits DEBT flags (orphan-candidate / frontend-orphan / reachable) per thread, CVO-ground-truthed. The scorer consumes those flags rather than re-deriving pipeline reachability.
- **DOMINANT motif:** full-chain mounted-reachable (producers->served->frontend resolves), the modal in-scope shape.
- **OUTLIERS (orphan_stage):** pipescript's explicit-out/DEBT-flagged threads (~27 explicit-out + ~4 unreviewed across the 25). Example: MA-08-yang-generate-volatility = orphan-candidate/frontend-orphan (served json/yang/volatility_data.json STALE 180B since 2026-01-14, superseded by the live MA-05; no portal consumer). These are ALREADY pipescript-surfaced + CVO-ground-truthed -- KNOWN, not novel.
- **TWIN-SHADOW:** advi-bd / advi-inf / advi-cot are DESIGNED firm-twins (parallel pipelines, same motif) -> cleared, not deviations. Observability legs (yang-canon-interlock drift-check, no portal artifact by design) are explicit-out-by-design, not orphans.
- **No NEW novel candidate from PIPELINE** beyond what pipescript already flags -> the novel AC4 candidate remains the SERVED_LINEAGE recompute_fork. (4-class first-pass census now COMPLETE.)

## Status to AC-close
- DONE: 4-class first-pass census COMPLETE (SERVED_LINEAGE + AUTH + DEPLOY + PIPELINE). AC2 candidate list produced. AC3 census-clean-vs-suppression demonstrated (AUTH 122 -> 0 filed). AC4 candidate FOUND + routed to CVO (the recompute_fork cross-firm asymmetry) -- 185909Z, RAVC2 to COO 185929Z. 0 mutations, HEAD-current throughout (AC4 freshness).
- IN FLIGHT (long-pole, parallel): CVO AC4 adjudication of the candidate (true-deviation -> AC4 MET; FP -> new suppression_v1 class + I enumerate another).
- REMAINING for full TO-close: the scorer packaged as a registered Python tool (org/modules/graph/debtscan/) -- reads kuzu_nessie_db via the kuzu lib AFTER a comp-kuzu freshness-assert (NO Python->comp-* subprocess on Windows, banked) for SERVED_LINEAGE/AUTH; DELEGATES PIPELINE->pipescript + DEPLOY->deploy-ledger (query-don't-rebuild); applies twin_shadow_guard + suppression SEPARATELY; emits this scorecard format -> comp-manifest-check register. Then full RAVC2-to-close (CC CTO+CVO) on the CVO verdict + the registered tool.
- SCORER ARCHITECTURE (validated by this first-pass): per-class source -- SERVED_LINEAGE + AUTH = comp-kuzu (canonical); DEPLOY = deploy-ledger cross-ref (canonical graph is bucket-grain, can't score code-prefix->runner); PIPELINE = pipescript debt-flags (don't re-derive reachability). The tool is a thin orchestrator over the canonical query surfaces + the two gates, NOT a monolithic re-extractor.
