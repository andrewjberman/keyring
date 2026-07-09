# Deploy Completion Record
**Date opened:** 2026-07-09T07:32:48.111876+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T073657Z
**Deploy:** CREDENTIAL-PLANE FIRM-SEP BELT: DenyCrossFirmSecrets on opal/bd/* for the 3 secret:opal/* wildcard holders (CTO amended ruling 072532Z + APPLY-GO 073214Z; COO GO)
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commit + push the 3 belt resources | hash pushed | 696b34f84 pushed to CLOUD | CLOSED 20260709T073248Z |
| L2 | activation | safe-apply(HALTGT) shared-infra -- belt on opal-portal-lambda-role (PUBLIC authorizer) | 1-add/0-change/0-destroy | shared-infra safe-apply(HALTGT) of the saved gated plan: 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Belt on opal-portal-lambda-role (the shared role behind 11 Lambdas incl. the PUBLIC authorizer). | CLOSED 20260709T073656Z |
| L3 | activation | safe-apply(HALTGT) portal-auth -- belt on opalinvest-auth-lambda-role | 1-add/0-change/0-destroy | portal-auth safe-apply(HALTGT): 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Belt on opalinvest-auth-lambda-role. | CLOSED 20260709T073656Z |
| L4 | activation | safe-apply(HALTGT) news-pipeline -- belt on news-ingestion-lambda-role | 1-add/0-change/0-destroy | news-pipeline safe-apply(HALTGT): 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Belt on news-ingestion-lambda-role. NOTE: a first apply attempt failed cleanly ('Failed to load plan file') because I had saved plan TEXT, not -out binaries -- nothing was applied; verified the belt was absent from all 3 live roles before re-planning to disk and applying the saved gated plans. | CLOSED 20260709T073656Z |
| L5 | verify | DENY-TEST exercised: explicitDeny on opal/bd/credentials AND opal/bd/cottonwood/credentials for all 3 roles; yang stays implicitDeny (the discriminator) | 3x2 explicitDeny + yang implicitDeny | DENY-TEST EXERCISED (simulate-principal-policy, single-resource-per-call per the CVO multi-ARN gotcha). PRE-BELT BASELINE captured first so the flip is provable, not assumed: all 3 roles = allowed on BOTH bd secrets. POST-BELT: opal-portal-lambda-role, opalinvest-auth-lambda-role, news-ingestion-lambda-role each return explicitDeny on BOTH opal/bd/credentials AND opal/bd/cottonwood/credentials (6/6). Roles not explicitDeny on both: 0. DISCRIMINATOR: yang-pipeline-lambda-role, deliberately unbelted (its wildcard is us-east-2-scoped), stays implicitDeny on both -- so 3x explicitDeny vs 1x implicitDeny proves THE BELT is the deciding control, not default-deny. explicitDeny is the correct criterion for a Deny-ADD (group-3 shape); asserting implicitDeny (the Allow-removal shape) would have false-RED a correct change -- the inverted-criterion trap CTO mis-applied in the original ruling and owned. | CLOSED 20260709T073656Z |
| L6 | verify | NO COLLATERAL DENY: the USED prefixes still allowed (opal/auth/jwt-public-key, opal/external-apis, opal/openai/news-trending) + behaviour-exercise portal_data_proxy's fail-silent output | used prefixes allowed; proxy output non-degraded | NO COLLATERAL DENY, exercised. Every USED prefix still allowed: opal-portal-lambda-role -> opal/auth/jwt-public-key + opal/external-apis + opal/openai/news-trending all allowed; opalinvest-auth-lambda-role -> jwt-public + jwt-private allowed; news-ingestion-lambda-role -> opal/external-apis + opal/openai/news-trending allowed. BEHAVIOUR EXERCISE of the fail-silent consumer: invoked opal-portal-data-proxy (StatusCode 200, no FunctionError) and scanned its fresh log stream for the exact silent-degradation signal '[keyword_intelligence] Error getting OpenAI key' -> 0 occurrences. HONEST BOUNDING: an empty {} payload may not have exercised the keyword-intelligence code path at all, so the log-absence is WEAK evidence on its own. The load-bearing evidence is (a) the capability simulate showing opal/openai/news-trending still allowed for that role, and (b) the structural fact that a Deny scoped to opal/bd/* cannot reach opal/openai/*. Recorded as capability-proven + behaviour-corroborated, not behaviour-proven. | CLOSED 20260709T073656Z |

## Log

- 20260709T073248Z OPENED by 0.5.0_AE_OpalETL with 6 leg(s)
- 20260709T073248Z LEG L1 closed: 696b34f84 pushed to CLOUD
- 20260709T073656Z LEG L2 closed: shared-infra safe-apply(HALTGT) of the saved gated plan: 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' B
- 20260709T073656Z LEG L3 closed: portal-auth safe-apply(HALTGT): 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Belt on opalinvest-auth-la
- 20260709T073656Z LEG L4 closed: news-pipeline safe-apply(HALTGT): 'Apply complete! Resources: 1 added, 0 changed, 0 destroyed.' Belt on news-ingestion-l
- 20260709T073656Z LEG L5 closed: DENY-TEST EXERCISED (simulate-principal-policy, single-resource-per-call per the CVO multi-ARN gotcha). PRE-BELT BASELIN
- 20260709T073656Z LEG L6 closed: NO COLLATERAL DENY, exercised. Every USED prefix still allowed: opal-portal-lambda-role -> opal/auth/jwt-public-key + op
- 20260709T073657Z CLOSED -- all 6 legs proven
