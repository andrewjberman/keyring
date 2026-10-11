# Deploy Completion Record
**Date opened:** 2026-10-11T05:25:24.525793+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T053136Z
**Deploy:** TO30 WINDOW 7: svc-irpt reader window for dell2 one re-read of REQ-5e4149d2 status job (X-IRPT-Status-Dates prospect-v1), ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (window 7) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 05:25:51Z and 05:26:00Z. Signed ADD put with --block-public-policy 05:26:00-05:26:01Z on CTO WINDOW 7 START msg 108221 (consent CTO_CONSENT_SVC_IRPT_READER_WINDOW7_DELL2_20261011.md, no start hold). Read-back SET-EQUAL to ADD at 05:26:03Z (not set-equal to BEFORE). PUT TIME sent to 0.0.0_AB_MSTR for 2.0.0_SA_COO~G2 at 05:26:09Z, 6 s after read-back. Simulated with live policy attached: dell2 allowed, dell1 explicitDeny, walker Andrew_Berman allowed. NO GetSecretValue by this seat. Hard close 05:56:01Z. | CLOSED 20261011T052653Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2 R done or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 05:31:09Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 05:31:09-05:31:11Z on CTO R-DONE msg 108225 (G2 R done 05:29:50Z, one GET HTTP 200), 24 min 50 s before the 05:56:01Z hard close. Read-back SET-EQUAL to BEFORE at 05:31:13Z (not set-equal to ADD). Simulated with live policy attached: dell2 explicitDeny, dell1 explicitDeny, walker Andrew_Berman allowed. AC1 get-resource-policy contains WalkerReadsByExplicitArn (1 match). NO GetSecretValue by this seat. Window open 05:26:01Z-05:31:11Z. | CLOSED 20261011T053136Z |

## Log

- 20261011T052524Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261011T052653Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 05:25:51Z and 05:26:00Z. Signed ADD put with --block-public-policy 05:26:00-05:
- 20261011T053136Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 05:31:09Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 
- 20261011T053136Z CLOSED -- all 2 legs proven
