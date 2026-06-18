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
- **recompute_fork (the candidate-rich deviation class):** NOT yet enumerated -- needs the FLOWS_TO kind=recompute/guarded per-cohort/firm asymmetry pass (the likely AC4 novel-candidate source). PENDING in the scorer build.

## AUTH_CANON
- **Raw census:** API_ROUTE 77 + ServedURL 45, ALL with `TRIGGERS`-outbound = 0.
- **Suppression gate (the point of the class):** a naive `missing_auth_edge` scorer files 122 RED. ALL are cleared by suppression: `FP_API_LAMBDA` (API_GW->Lambda INVOKES edges absent, 0 API_GW outbound) + `FP_LEDGE` (Lambda@Edge fires on CloudFront viewer-request, not a TRIGGERS edge). -> **census-clean vs suppression: 0 filed RED** (demonstrates AC3/AC4 "0 double-fire of known FPs"). This is the graph TRIGGERS-modeling gap, NOT an auth-bypass.
- A genuine `missing_auth_edge` requires a DIFFERENT signal than the (unmodeled) TRIGGERS edge -- e.g. a served route reaching S3 with no auth on the *behavior* via comp-routes, not the graph TRIGGERS. Scorer-scoping finding.

## DEPLOY_CANON
- **Census:** 20 S3 buckets carry runner (EC2/LAMBDA/ECS) READS edges -- but these are DATA reads at BUCKET grain (opal-data-*), not `code/`-prefix reads.
- **Scoping finding:** the canon DEPLOY motif `(S3 'code/' prefix)-[READS]->(runner)` is NOT scorable on the canonical graph as-is -- the graph models S3 at bucket grain, no `code/`-prefix nodes. `orphan_code_prefix` / `runnerless` need the **deploy-ledger cross-ref** leg the canon's `graph_source` names ("canonical ... + deploy-ledger cross-ref"), not the canonical graph alone. PENDING in the scorer build.

## PIPELINE_CANON
- NOT yet censused -- interior (`bronze->silver->gold->platinum`) lives in the **comp-pipescript** flow graph, not the canonical DB. Needs the comp-pipescript leg. PENDING.

## Remaining to AC4 (the scorer build block)
1. Python scorer tool (org/modules/graph/debtscan/) -- reads kuzu_nessie_db via the kuzu lib AFTER a comp-kuzu freshness-assert (NOT a subprocess to comp-* -- Windows bash-launcher constraint, banked); + comp-pipescript for the PIPELINE interior; emits the per-class scorecard + candidate list; applies twin_shadow_guard + suppression SEPARATELY.
2. SERVED_LINEAGE recompute_fork enumeration + DEPLOY ledger-cross-ref + PIPELINE comp-pipescript = the three places a NOVEL true deviation (AC4) can surface (SERVED_LINEAGE's 4 dangling + AUTH's 122 are pre-dispositioned/suppressed).
3. comp-manifest-check registration of the scorer as a canonical graph-call.
4. RAVC2 to COO (CC CTO+CVO) with the >=1 novel candidate for CVO adjudication.
