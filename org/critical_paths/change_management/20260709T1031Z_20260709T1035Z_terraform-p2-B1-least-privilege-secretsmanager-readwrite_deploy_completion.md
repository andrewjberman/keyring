# Deploy Completion Record
**Date opened:** 2026-07-09T10:31:05.921005+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260709T121100Z
**Deploy:** Phase B1: detach SecretsManagerReadWrite from market-update-lambda-role + opal-news-lambda-role; replace with role-scoped GetSecretValue. Closes cot+inf cross-firm credential WRITE reach.
**Authored by:** 0.5.0_AE_OpalETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| tf-market-overview | verify | market-overview: detach SecretsManagerReadWrite + add market_update_secrets_scoped | terraform re-plan shows No changes | apply: 1 added, 0 changed, 1 destroyed. Post-apply re-plan: 'No changes. Your infrastructure matches the configuration.' Live IAM: SecretsManagerReadWrite ABSENT from attached; inline market-update-secrets-read PRESENT. | CLOSED 20260709T104423Z |
| tf-news-pipeline | verify | news-pipeline: detach SecretsManagerReadWrite + add opal_news_secrets_scoped | terraform re-plan shows No changes | apply: 1 added, 0 changed, 1 destroyed. Post-apply re-plan: 'No changes.' Live IAM: SecretsManagerReadWrite ABSENT; inline opal-news-secrets-read PRESENT (alongside cross-firm-secret-deny + invoke-trending-publisher, untouched). | CLOSED 20260709T104423Z |
| denytest-implicitdeny | verify | comp-denytest --from-plan --baseline: implicitDeny 4/4 vs pre-apply allowed baseline + discriminator | tool output | comp-denytest --from-plan --baseline, rc=0 PASS on BOTH roles. Change type DERIVED from plan (DETACH -> allow-removal -> expected implicitDeny; author declared nothing). 4/4 implicitDeny (market-update + opal-news x cot/orion creds, PutSecretValue) against a pre-apply baseline recording all 4 as 'allowed' -- so the negative is falsifiable, not vacuous. | CLOSED 20260709T104423Z |
| also-allowed | verify | opal/external-apis + layer3-curation + openai-api-key still allowed (no collateral deny) | tool output | rc=0 PASS. market-update-lambda-role GetSecretValue opal/external-apis -> allowed. opal-news-lambda-role GetSecretValue opal/openai/layer3-curation -> allowed AND openai-api-key -> allowed. CONTROL: cot-exporter-ec2-role GetSecretValue cot/credentials -> allowed (no collateral damage to cot's own reader). Writes gone even on their OWN secret: market-update PutSecretValue opal/external-apis -> implicitDeny (read-only achieved). | CLOSED 20260709T104423Z |
| behaviour-legb | verify | OUTPUT exercise: aggregator /macro NO mock signature; generator error still proxies not OpenAI-API-key-not-configured | invoke payloads | PASS. (3) aggregator /macro: post == pre == 200 {'events': []}, ZERO mock signature (no 'CPI (Consumer Price Index)' / 'FOMC Meeting') -> the real FRED path still ran; a denied read would have returned fabricated data. (4) generator: post body still 'Client.__init__() got an unexpected keyword argument proxies' -- the DOWNSTREAM crash -- and NOT 'OpenAI API key not configured' -> the secret read still succeeds. NOT-PROVABLE (stated, not passed): the log-line assertion. These functions have NO CloudWatch log groups in any region, and market-update-lambda-role is implicitDeny on logs:PutLogEvents in us-east-1 (its only logs grant is us-east-2). NOT-YET-EXERCISED (stated, not passed): opal-news-layer3-curation was NOT invoked (it writes DynamoDB + invokes the publisher); its read is LOUD (raise); its next scheduled run proves it. | CLOSED 20260709T104423Z |
| cvo-cert-lega | verify | CVO comp-firmsep-sweep --write-only: allowed NONE on all 4 firm creds | CVO cert | CVO cert: org/tier1_exec/3.0.0_SA_CVO/deliverables/CERT_terraform-p2-B1-least-privilege-write-root-lega_20260709.md. Authoritative comp-firmsep-sweep on both B1-touched creds -- orion/credentials + blackdiamond/cot/credentials each 180/180 simulated, no-verdict:0, allowed:NONE, NON-OWNER:NONE, PASS; the 2 over-granted Lambdas now implicitDeny. opal/bd/{cottonwood,credentials} NONE (already NONE pre-B1, not in delta). Compact-loop no-verdict=1 was a transient simulate throttle, resolved to 0 by the tool's paced run (service-linked roles ruled out, account count 0). Behaviour-leg open items (log-assertion NOT-PROVABLE market-update; opal-news-layer3-curation NOT-YET-EXERCISED) stated + 0.5.0-owned, NOT asserted resolved. KMS low-risk-by-artifact (KmsKeyId:None) + exercise-confirmed. | CLOSED 20260709T120628Z |

## Log

- 20260709T103105Z OPENED by 0.5.0_AE_OpalETL with 6 leg(s)
- 20260709T104423Z LEG tf-market-overview closed: apply: 1 added, 0 changed, 1 destroyed. Post-apply re-plan: 'No changes. Your infrastructure matches the configuration.'
- 20260709T104423Z LEG tf-news-pipeline closed: apply: 1 added, 0 changed, 1 destroyed. Post-apply re-plan: 'No changes.' Live IAM: SecretsManagerReadWrite ABSENT; inli
- 20260709T104423Z LEG denytest-implicitdeny closed: comp-denytest --from-plan --baseline, rc=0 PASS on BOTH roles. Change type DERIVED from plan (DETACH -> allow-removal ->
- 20260709T104423Z LEG also-allowed closed: rc=0 PASS. market-update-lambda-role GetSecretValue opal/external-apis -> allowed. opal-news-lambda-role GetSecretValue 
- 20260709T104423Z LEG behaviour-legb closed: PASS. (3) aggregator /macro: post == pre == 200 {'events': []}, ZERO mock signature (no 'CPI (Consumer Price Index)' / '
- 20260709T121100Z CLOSED -- all 6 legs proven
