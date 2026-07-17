# Session Log -- 0.2.0_DT_PortfolioAnalytics -- 2026-07-17 ~2000-2351Z
**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, SCRIBE
**Project:** OPAL_TAXSMA_PT2 (Andrew-direct: return to TAXSMA / the scoped BD table for Alyssa)

## Window summary
From Andrew's two source files (Yang-call transcript + HAR) to a LIVE, governed, least-privilege BD
reporting pull landing first bronze -- plus the registry/onboarding architecture briefed to CTO.

## What happened (arc)
1. ASSESSED tax-pt2 scoped-BD-table + Alyssa-MCP-IAM (both phases): BD bronze + Schwab silver mature,
   BD silver dims cured (07-16), scoped table NOT built, read-path net-new. Andrew corrections banked
   (Schwab HAS the fee data / BD is defensive; scoped table = few-fields/anonymized/keyed by acct#;
   per-employee scoped IAM = email->ARN assume-role). 2 committed deliverables.
2. Andrew settled sourcing = BD-pull via the Cottonwood REST pattern scoped 49F -> DESIGN-SCOPE BRIEF.
   CTO registered OPAL_TAXSMA_PT2 (@a80840fb1), ruled serve-layer = gold dim_taxsma_report (my rec),
   named me on WS-1 (bronze) + WS-4 (gateway IAM).
3. WS-1 ENDPOINT FINDING @638c91bea (read-side de-risk of Manav's HAR): the portfolioreporting/api/*
   endpoints pull off our EXISTING 49F .bd.identity session via GET /session/token (distinct token,
   same cookie). No second login box.
4. WS-1 producer BUILT DRY -> DEPLOYED FAIL-CLOSED -> LIVE. dry_test PASS (bodies match HAR to the
   field, raw 17a, DRY_RUN=1 egress-refuse-in-code). CTO plan-gate PASS (4 conds); deployed inert
   (DRY_RUN=1) on his gate; 22a APPLIED evidence (5 separate simulate). Andrew granted STANDING egress
   ("Yes, the egress word is standing for production pulls") -> DRY_RUN 1->0 flip -> Chiles invoke ->
   first live bronze. CTO GO-LIVE CONFIRMED.
5. WS-4 gateway-IAM PLAN -> CTO plan-gate PASS w/ 4 binding conds (namespace invariant, re-id-mapping
   outside prefix, WS-3-anonymization-verified, 22a applied+exercised w/ conditioned-ListBucket 3rd control).
6. Discovered + captured the BD-REVISION CONTRACT PROPERTY (BD revises closed-period figures: netGains
   drifted 0.03pct while realized held to the cent) -> bronze partitions by pull_date + pull-asof metadata.
7. REGISTRY + /tax-newacc ONBOARDING BRIEF @e43e9d0de -> issued to CTO for a new PRD + TOs direct (not
   COO). NON-NEGOTIABLE (Andrew): resolution EXACT on account number from Alyssa's docs, NEVER fuzzy.

## Deployment Sequence + Verification (WS-1, actual)
- opal-assets-bd49f-reporting-pull: source committed (dd9ce841f) -> build-upload (VERIFIED) -> source-map
  -> plan (7-add/0-change/0-destroy FULL, no -target, COND-1) -> safe-apply FAIL-CLOSED (ea7990eb4;
  7 added/0/0) -> 0-diff -> tag opal-assets-v0.27.0. Then egress flip (913f1bd3e) -> safe-apply (1 changed)
  -> 0-diff.
- Rule-22a APPLIED (5 SEPARATE one-resource simulate on opal-assets-bd49f-reporting-pull-role):
    PutObject bronze/reporting_* -> allowed | PutObject bronze/fees -> implicitDeny |
    PutObject silver/xref -> implicitDeny | GetObject schwab/fact_ult -> implicitDeny |
    PutObject opal-data-cot -> explicitDeny (fence).
- EXERCISED: Chiles invoke StatusCode 200, landed 3; ListObjectsV2 verify (key+ETag+Size, not Head):
    reporting_performance/2026-07-17/..._22596361_2026-06-30.json  5,280,465 B
    reporting_costbasis/...  689,120 B | reporting_allocation/...  430,123 B
  sizes == live-verify sizes (byte-for-byte raw 17a); metadata pull-asof=2026-07-17. Ledger CLOSED @96348bb35.

## Files Modified
see commit messages: b372e7f7e, dc0fb3700, 638c91bea, dd9ce841f, 454dedf0e, f559cbc51, 456678434,
ea7990eb4, 960fabdad, 913f1bd3e, 96348bb35, e43e9d0de. New producer:
infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/ (+ TF bd49f_reporting_pull.tf).

## Blockers
None. (WS-1 fully unblocked + live; WS-4 apply correctly HELD on CTO conds + WS-3 gold prefix.)

## Current State
- WS-1 LIVE: opal-assets-bd49f-reporting-pull deployed @opal-assets-v0.27.0, DRY_RUN=0 (standing egress),
  manual-invoke-only (no schedule). First Chiles bronze at blackdiamond/49f/bronze/reporting_{feed}/
  2026-07-17/. Producer role least-privilege (22a-proven). discover_accounts() still a STUB (Chiles
  passed explicitly) -- the registry (new PRD) replaces it.
- WS-4: IAM plan PASS w/ 4 conds; apply HELD on WS-3 gold + conds.
- Registry/onboarding: brief @e43e9d0de at CTO for new PRD + TOs.

## Next Steps
- [1.0.0_SA_CTO] register the registry/onboarding PRD + write the 5-WS TOs (direct, not COO) from the brief.
- [0.2.0_DT] implement the registry WS as TOs land (I own most); the exact-account-number resolver (D2)
  + the account-api-vs-sanctioned egress-scope decision (D3) are the load-bearing pieces.
- [0.4.0_DS_ClientPlatform] WS-2 silver against the live Chiles bronze (COO released the trigger); build
  against the BD-revision contract (silver keys on schwab_account, window, pull_asof).
- Follow-on: WS-5 schedule (standing daily pull); Bump/Macy resolution via the registry's exact resolver.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-grep / comp-glob | Cottonwood pattern + TF + taxonomy discovery | PASS | located cot_bronze_ingest template, monolith grammar, fence policy |
| comp-iam | NOT used for the WS-1 role verdict | N/A | Rule 22a: comp-iam FAILS GREEN on new (action,resource) -- used the LIVE simulate-principal-policy (5 separate calls) instead, the correct instrument |
What worked: the live simulate (5 separate one-ARN calls) proved (action,resource) least-privilege where
comp-iam would false-green. The HAR read-side de-risk closed the endpoint mechanism before any live call.
What failed: nothing material. Gap found: account-number->internalId resolution is unsolved for accounts
absent from the xref (Bump/Macy) -- surfaced as the registry PRD's D2 (exact-number, no fuzzy).
