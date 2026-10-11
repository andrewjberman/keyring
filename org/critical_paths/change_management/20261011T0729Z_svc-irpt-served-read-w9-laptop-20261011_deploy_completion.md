# Deploy Completion Record
**Date opened:** 2026-10-11T07:29:12.660728+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T073738Z
**Deploy:** TO30 WINDOW 9: svc-irpt reader window for dell2 one GET (held-characteristics coverage count k of N through the served read), ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (window 9) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 07:29:44Z and 07:29:56Z. Signed ADD put with --block-public-policy 07:29:57-07:29:59Z on CTO WINDOW 9 START msg (consent CTO_CONSENT_SVC_IRPT_READER_WINDOW9_DELL2_20261011.md, no start hold). Read-back SET-EQUAL to ADD at 07:30:01Z (not set-equal to BEFORE). PUT TIME sent to 0.0.0_AB_MSTR for 2.0.0_SA_COO~G2 at 07:30:07Z, 6 s after read-back. Simulated with live policy attached: dell2 allowed, dell1 explicitDeny, walker Andrew_Berman allowed. NO GetSecretValue by this seat. Hard close 07:59:59Z. | CLOSED 20261011T073104Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2 R done or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 07:37:09Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 07:37:09-07:37:11Z on CTO R-DONE msg 108257 (G2 R done 07:34:44Z), 22 min 48 s before the 07:59:59Z hard close. Read-back SET-EQUAL to BEFORE at 07:37:12Z (not set-equal to ADD). Simulated with live policy attached: dell2 explicitDeny, dell1 explicitDeny, walker Andrew_Berman allowed. AC1 get-resource-policy contains WalkerReadsByExplicitArn (1 match). NO GetSecretValue by this seat. Window open 07:29:59Z-07:37:11Z. | CLOSED 20261011T073738Z |

## Log

- 20261011T072912Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261011T073104Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 07:29:44Z and 07:29:56Z. Signed ADD put with --block-public-policy 07:29:57-07:
- 20261011T073738Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 07:37:09Z (not set-equal to BEFORE). Signed BEFORE put with --block-public-policy 
- 20261011T073738Z CLOSED -- all 2 legs proven
