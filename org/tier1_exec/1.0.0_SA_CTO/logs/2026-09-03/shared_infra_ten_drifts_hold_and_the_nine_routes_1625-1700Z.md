# 1.0.0_SA_CTO -- 2026-09-03 16:25-17:00Z -- the lifecycle apply landed; ten drifts under it; a hold

Inputs (READ-acked): 2.0.0_SA_COO /drive tick 5 (93797): after ~K's target-scoped lifecycle apply (0/1/0; live two rules)
the unscoped control read 0/10/0 -- the users-table delete guard plus nine API route authorizations an unscoped apply
would strip; Andrew at the COO terminal questioned the ~K seat on NFRA_GLOBGRPH ("We are only working COMPEFFICACY and
CLDGRPH on this device"), then "We can let it continue" (@ee688a660b).

## Measured
- The plan file is UTF-16 (PowerShell redirect): a byte grep reads empty; decoded, the ten addresses are the users table
  plus nine module.apigateway_portal routes = the public v1 data endpoints and the two metadata/yang routes.
- The module declares NONE on twelve routes; live is CUSTOM (+ the module's own portal_jwt authorizer) on nine; the three
  left open are auth handshake + CORS preflight -- a deliberate hardening's shape.
- Direction: OUT OF BAND. Only shared-infra declares those keys (every TF root censused); origin/SITEZ does not touch
  routes.tf; the 2026-08-03 consolidation moved twenty other routes; the OPSEC channel/PRD do not name them. CloudTrail
  UpdateRoute is the instrument that would name the hand.
- origin/SITEZ already declares deletion_protection_enabled = true on opal_users_v2 (OPSEC OP-s-8) -> TO-USERS-DELPROT
  is superseded by the merge leg.

## Acts
1. HOLD opened as module owner (lane ANY, measured): org/critical_paths/change_management/
   20260903T1650Z_shared-infra-unscoped-apply-HOLD.md -- no unscoped apply until 0/0/0; every apply -target with its
   ledger + an unscoped re-plan as acceptance; closes on the 0/0/0 read.
2. Ruling to the issuer (93812): the lifecycle entry closes on disclosure (COO's amendment agreed); DELPROT superseded;
   the nine routes -> NFRA_OPSEC202609's loop on site Z via MSTR~Z as an outside remedy (declare what is LIVE), honouring
   Andrew's device-scope word; S2's L9 disposition = this hold + the two routed acts, no route.

## Open, with owner
- 0.0.0_AB_MSTR: the merge leg (dynamo.tf) and the relay to OPSEC.
- NFRA_OPSEC202609 (site Z): declare CUSTOM + authorizer on the nine routes; name the hand via CloudTrail.
- 1.0.0_SA_CTO: close the hold on the 0/0/0 read.
