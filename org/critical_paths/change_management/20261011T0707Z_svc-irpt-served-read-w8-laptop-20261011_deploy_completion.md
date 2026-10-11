# Deploy Completion Record
**Date opened:** 2026-10-11T07:07:52.128691+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T071645Z
**Deploy:** TO30 WINDOW 8: svc-irpt reader window for dell2 one GET (257-section census of the report through the served read), ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (window 8) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 07:08:17Z and 07:08:26Z. Signed ADD put with --block-public-policy 07:08:26-07:08:28Z on CTO WINDOW 8 START msg 108237 (consent CTO_CONSENT_SVC_IRPT_READER_WINDOW8_DELL2_20261011.md, no start hold). Read-back SET-EQUAL to ADD at 07:08:30Z (not set-equal to BEFORE). PUT TIME sent to 0.0.0_AB_MSTR for 2.0.0_SA_COO~G2 at 07:08:35Z, 5 s after read-back. Simulated with live policy attached: dell2 allowed, dell1 explicitDeny, walker Andrew_Berman allowed. NO GetSecretValue by this seat. Hard close 07:38:28Z. | CLOSED 20261011T070918Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2 R done or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 07:16:18Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 07:16:18-07:16:19Z on CTO R-DONE (G2 R done 07:13:59Z), 22 min 9 s before the 07:38:28Z hard close. Read-back SET-EQUAL to BEFORE at 07:16:21Z (not set-equal to ADD). Simulated with live policy attached: dell2 explicitDeny, dell1 explicitDeny, walker Andrew_Berman allowed. AC1 get-resource-policy contains WalkerReadsByExplicitArn (1 match). NO GetSecretValue by this seat. Window open 07:08:28Z-07:16:19Z. | CLOSED 20261011T071645Z |

## Log

- 20261011T070752Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261011T070918Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 07:08:17Z and 07:08:26Z. Signed ADD put with --block-public-policy 07:08:26-07:
- 20261011T071645Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 07:16:18Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 
- 20261011T071645Z CLOSED -- all 2 legs proven
