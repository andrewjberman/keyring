# Deploy Completion Record
**Date opened:** 2026-10-09T13:35:34.510572+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T134945Z
**Deploy:** TO30 svc-irpt reader window for dell2's SERVED READ ledger irpt-ycdgen-served-read-20261009; ADD now; REMOVE at G2 'R done' or ADD+30m without waiting, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 13:34:08Z (816 B; negative control: NOT set-equal to ADD, differing in exactly the 2 dell2 elements). Signed ADD put with --block-public-policy 13:37:33-13:37:36Z. Read-back SET-EQUAL to signed ADD (944 B; negative control: NOT set-equal to BEFORE, the same 2 places inverted); cloudops-dell2-agent-user occurrences 2, cloudops-dell1-agent-user 0. Simulated GetSecretValue against the live policy: dell2 allowed, dell1 explicitDeny, walker user/Andrew_Berman allowed -- exactly the three the order requires, so no revert. NO GetSecretValue call made. REMOVE due at G2 'R done' or 14:07:36Z; this seat holds the clock, alarm armed for 14:04:30Z. | CLOSED 20261009T134259Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2's 'R done' or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 13:44:52Z (negative control: NOT set-equal to BEFORE, 2 dell2 elements). Signed BEFORE put with --block-public-policy 13:45:37-13:45:41Z on G2's REMOVE-NOW (relay 107980), 22 minutes before the ADD+30m hard close. Read-back SET-EQUAL to signed BEFORE (negative control: NOT set-equal to ADD, same 2 places inverted); cloudops-dell2-agent-user occurrences 0, dell1 0. Simulated: dell2 explicitDeny, dell1 explicitDeny, walker user/Andrew_Berman allowed. AC1 WalkerReadsByExplicitArn present. NO GetSecretValue call made. Window open 13:37:36Z-13:45:41Z, 8 min 5 s. | CLOSED 20261009T134945Z |

## Log

- 20261009T133534Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261009T134259Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 13:34:08Z (816 B; negative control: NOT set-equal to ADD, differing in exactly 
- 20261009T134945Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 13:44:52Z (negative control: NOT set-equal to BEFORE, 2 dell2 elements). Signed BE
- 20261009T134945Z CLOSED -- all 2 legs proven
