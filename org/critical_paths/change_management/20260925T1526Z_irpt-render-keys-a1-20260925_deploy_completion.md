# Deploy Completion Record
**Date opened:** 2026-09-25T15:26:49.273691+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T153017Z
**Deploy:** Export section A1: the IRPT render key pair (containers via Terraform, material out of band)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_secretsmanager_secret.irpt_render_jwt_{private,public}_key | describe-secret both exist; get-secret-value parses as {current, previous} | safe-apply targeted (2 added): opal/auth/irpt-render-jwt-private-key (-Rm6oGY) and -public-key (-EAL0l7); RSA-2048 pair generated in memory, put out of band as {current, previous:null}; both envelopes read back with keys [current, previous]; private material never printed, written to disk or put in state | CLOSED 20260925T153016Z |
| N1 | verify | negative arm | opal/auth/jwt-private-key LastChangedDate unchanged; a token signed by the render key fails the HUMAN public key and passes the render public key | a token signed by the render private key: REFUSED by the human opal/auth/jwt-public-key (JWTError), VERIFIED by opal/auth/irpt-render-jwt-public-key read back from Secrets Manager; opal/auth/jwt-private-key LastChangedDate 2026-09-10T01:18:14Z and 2 versions before and after (untouched) | CLOSED 20260925T153017Z |
| V1 | verify | targeted re-plan of the two containers | No changes | targeted terraform plan of the two containers after apply: No changes (an UNTARGETED plan of portal-auth shows unrelated WAF drift -- row IRPT_BCKEND-S130 -- deliberately not applied) | CLOSED 20260925T153017Z |

## Log

- 20260925T152649Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260925T153016Z LEG A1 closed: safe-apply targeted (2 added): opal/auth/irpt-render-jwt-private-key (-Rm6oGY) and -public-key (-EAL0l7); RSA-2048 pair 
- 20260925T153017Z LEG N1 closed: a token signed by the render private key: REFUSED by the human opal/auth/jwt-public-key (JWTError), VERIFIED by opal/aut
- 20260925T153017Z LEG V1 closed: targeted terraform plan of the two containers after apply: No changes (an UNTARGETED plan of portal-auth shows unrelated
- 20260925T153017Z CLOSED -- all 3 legs proven
