# Deploy Completion Record
**Date opened:** 2026-10-09T17:56:00.968281+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T181249Z
**Deploy:** TO30 AMENDMENT 3 WINDOW 5: svc-irpt reader window for dell2's IRPT_ANLREQ.TO-APPLY-Y1 AMENDMENT 6 sequence (R3 owner GET on cottonwood, W1, R4 on REQ-5e41, W2, R done), ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m without waiting, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (window 5) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 17:54:59Z (816 B; negative control NOT set-equal to ADD, exactly the 2 dell2 elements; also confirms window 3's REMOVE stayed landed, measured live). Signed ADD put with --block-public-policy 17:57:39-17:57:43Z on the issuer's GO 108070 (CTO yes 108068, addendum 91d0d7982c). Read-back SET-EQUAL to signed ADD (944 B; negative control NOT set-equal to BEFORE); cloudops-dell2-agent-user occurrences 2, dell1 0. Simulated: dell2 allowed, dell1 explicitDeny, walker allowed -- the three required, so no revert. NO GetSecretValue call made. RELAY DEFECT, recorded: the put time went to MSTR at 18:01:39Z, 139 s AFTER G2's R DONE at 17:59:20Z -- written but too late to serve the sequence; G2 worked off the live grant 97 s after the put. Ordering fault, not delivery. | CLOSED 20261009T181249Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2's 'R done' or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 18:04:26Z (negative control NOT set-equal to BEFORE). Signed BEFORE put with --block-public-policy 18:05:35-18:05:37Z on G2's R DONE 17:59:20Z (relay 108077), 22 min 6 s before the 18:27:43Z hard close. Read-back SET-EQUAL to signed BEFORE (negative control NOT set-equal to ADD); cloudops-dell2-agent-user occurrences 0, dell1 0. Simulated: dell2 explicitDeny, dell1 explicitDeny, walker user/Andrew_Berman allowed. AC1 WalkerReadsByExplicitArn present. NO GetSecretValue call made by this seat. Window 5 open 17:57:43Z-18:05:37Z, 7 min 54 s; G2's two in-memory reads landed ~17:57:5xZ (R3) and ~17:59:1xZ (R4) inside it. | CLOSED 20261009T181249Z |

## Log

- 20261009T175600Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261009T181249Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 17:54:59Z (816 B; negative control NOT set-equal to ADD, exactly the 2 dell2 el
- 20261009T181249Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 18:04:26Z (negative control NOT set-equal to BEFORE). Signed BEFORE put with --blo
- 20261009T181249Z CLOSED -- all 2 legs proven
