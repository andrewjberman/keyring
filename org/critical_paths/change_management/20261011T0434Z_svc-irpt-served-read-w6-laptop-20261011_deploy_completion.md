# Deploy Completion Record
**Date opened:** 2026-10-11T04:34:03.087649+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T045453Z
**Deploy:** TO30 AMENDMENT 4 WINDOW 6: svc-irpt reader window for dell2 IRPT_ANLREQ rev 6 live-call arm (R3/R4/R5), ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (window 6) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 04:47:59Z (also 04:33:36Z, 04:36:21Z). Signed ADD put with --block-public-policy 04:47:59-04:48:00Z on CTO WINDOW 6 START msg 108207 (consent CTO_CONSENT_SVC_IRPT_READER_WINDOW6_DELL2_20261011.md). Read-back SET-EQUAL to ADD at 04:48:02Z (not set-equal to BEFORE). PUT TIME sent to 0.0.0_AB_MSTR for 2.0.0_SA_COO~G2 at 04:48:08Z, 8 s after read-back. Simulated with the live resource policy attached: dell2 allowed, dell1 explicitDeny, walker Andrew_Berman allowed. NO GetSecretValue by this seat. Hard close 05:18:00Z. | CLOSED 20261011T044906Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2 R done or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 04:54:25Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 04:54:25-04:54:26Z on CTO R-DONE msg 108210 (G2 R done 04:52:49Z; R3 04:48:41Z, R4/R5 04:52:49Z), 23 min 34 s before the 05:18:00Z hard close. Read-back SET-EQUAL to BEFORE at 04:54:28Z (not set-equal to ADD). Simulated with live policy attached: dell2 explicitDeny, dell1 explicitDeny, walker Andrew_Berman allowed. AC1 get-resource-policy contains WalkerReadsByExplicitArn (1 match). NO GetSecretValue by this seat. Window open 04:48:00Z-04:54:26Z. | CLOSED 20261011T045453Z |

## Log

- 20261011T043403Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261011T044906Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 04:47:59Z (also 04:33:36Z, 04:36:21Z). Signed ADD put with --block-public-polic
- 20261011T045453Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 04:54:25Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 
- 20261011T045453Z CLOSED -- all 2 legs proven
