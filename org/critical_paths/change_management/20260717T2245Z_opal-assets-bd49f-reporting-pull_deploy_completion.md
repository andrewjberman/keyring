# Deploy-Completion Ledger -- opal-assets-bd49f-reporting-pull (OPAL_TAXSMA_PT2 WS-1)

**Status:** OPEN (infra applied; leg 6 HELD on COO standing-word + egress flip)
**Opened:** 2026-07-17T22:45Z
**Owner:** 0.2.0_DT_PortfolioAnalytics
**Lambda:** opal-assets-bd49f-reporting-pull (pipeline: opal-assets) + role/policies (7-add pure)
**Gate:** CTO WS-1 plan-gate PASS 223849Z (4 conditions). COO conds a/b/c 220432Z + landing-discipline.

## Scope (pure new-territory, 7 add / 0 change / 0 destroy -- FULL module plan, no -target, COND-1 confirmed)
BD reporting-pull producer role + scope-exact IO/secret policies + fence attachment + lambda + log group.
DEPLOYED FAIL-CLOSED (DRY_RUN=1) per CTO COND-2 -- infra lands INERT; enabling egress (DRY_RUN=0) is a
separate, gated, auditable TF flip, held for COO-confirmed STANDING egress word (Andrew's per-use word
cleared the one-time verify; standing production pulls need explicit scope confirmation).

## Legs
- [x] 1. TF committed (DRY_RUN=1 fail-closed)
- [x] 2. safe-apply (NEVER#5 ledger; this)
- [x] 3. full 0-diff
- [x] 4. tag + push --follow-tags
- [x] 5. Rule-22a APPLIED evidence (COND-3, WIDENED): simulate PutObject on the exact bronze/reporting key
        = allowed (separate positive control); never-widen negatives = implicitDeny on (a) a bronze NON-
        reporting key, (b) a silver/gold key (PutObject), (c) a read outside the two scoped prefixes. ONE
        --resource-arns per call, SEPARATE invocations (comp-iam FAILS GREEN on the new resource). -> CTO.
- [ ] 6. [HELD -- COO standing-word confirm] flip DRY_RUN=0 (TF) -> apply -> Chiles manual invoke =
        EXERCISED evidence (first live bronze, ListObjectsV2-verified) -> CTO + signal COO -> DS WS-2.

## Rollback
Pure-add: `terraform destroy -target` the 7 new resources (nothing pre-existing touched). Lambda inert
(DRY_RUN=1) so no egress occurred at deploy.

## Applied evidence (legs 1-5 DONE)
- safe-apply: 7 added / 0 changed / 0 destroyed; full 0-diff "No changes"; tag opal-assets-v0.27.0.
- Rule-22a APPLIED (5 SEPARATE one-resource simulate calls on opal-assets-bd49f-reporting-pull-role):
    PutObject bronze/reporting_* key            -> allowed        (positive control)
    PutObject bronze/fees_435407 (non-reporting)-> implicitDeny    (write scoped to reporting_* only)
    PutObject silver/dim_account_xref           -> implicitDeny    (silver is GET-only)
    GetObject schwab/08335338/fact_ult (outside)-> implicitDeny    (read scoped to the 2 prefixes)
    PutObject opal-data-cot (cross-firm)        -> explicitDeny    (the one_way_fan_in_fence)
  comp-iam FAILS GREEN on the new resource; these live-primitive results are the truth. Evidence -> CTO.
- NOTE: shared opal-assets CHANGELOG.json deploy-record entry NOT written (AE-only per COO) -- surfaced.

## HELD (leg 6): the EXERCISED evidence (DRY_RUN=0 flip + Chiles invoke -> first live bronze) awaits
COO's confirmation that Andrew's egress word is STANDING for production pulls (CTO COND-2 routed to COO).
