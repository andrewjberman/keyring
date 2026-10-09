# Deploy Completion Record
**Date opened:** 2026-10-09T09:52:20.498008+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-84 (E2, round 41, cell DB-b-84): mint the svc-custody-statement RS256 service token and create ONE secret opal/investor-reporting/svc-custody-statement, under the signed never-widen pair -- COO half AMENDMENT 2 @a319fc74b8 (2.0.0_SA_COO~K2), CTO half GIVEN by 1.0.0_SA_CTO~DELL2 (msg 2440, signed against blob 323217e49c). Blast radius signed: ONE secret, ONE reader ARN on dell2's GetSecretValue allow-list (a LAPTOP act routed via 0.0.0_AB_MSTR~DELL2), no IAM user/group/roster change. Rollback: delete-secret with the DEFAULT recovery window (never force) and the ARN removed.
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B | verify | before-read, re-run at apply | all three hold: describe-secret opal/investor-reporting/svc-custody-statement returns ResourceNotFoundException; IB-pr-385 LIVE in irpt-export-render read from its release ledger; irpt-ycharts-generate live CodeSha256 starts tdpterTM (release 6b). Any one missing is a STOP. |  | OPEN |
| M | activation | mint RS256 from the CURRENT slot of opal/auth/jwt-private-key (memory only, never printed or written) and create the ONE secret | decoded claims equal pair section 1 EXACTLY (sub/name svc-custody-statement, userType/tier service, firmId cottonwood, iss opal-portal-auth, aud opal-portal-api; role/advisorId/allowedPages/allowedTabs/firmRole ABSENT), exp-iat <= 90 days, secret name passed through lib/opal_naming.py, and the create-secret ARN |  | OPEN |
| R | activation | the ONE reader ARN added to dell2's secretsmanager:GetSecretValue allow-list -- a LAPTOP 0.7.0_AE_CloudOps act, routed via 0.0.0_AB_MSTR~DELL2 | the laptop's applied answer, then simulate-principal-policy: allowed for cloudops-dell2-agent-user on THIS ARN and implicitDeny on an unlisted secret, one --resource-arns per call with a separate positive control |  | OPEN |
| V | verify | read-backs and the three criteria | MINT_RECORD.json written in deliverables/0.7.0_AE_CloudOps~DB2/, DB41-1-AC1/AC2/AC3 each PASS from p41_round41.py, and proof-of-spec-check.py reports the instance VALID |  | OPEN |

## Log

- 20261009T095220Z OPENED by 0.7.0_AE_CloudOps~DB2 with 4 leg(s)
