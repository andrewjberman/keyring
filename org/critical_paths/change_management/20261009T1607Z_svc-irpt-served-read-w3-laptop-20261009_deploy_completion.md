# Deploy Completion Record
**Date opened:** 2026-10-09T16:07:20.557106+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T163657Z
**Deploy:** TO30 AMENDMENT 2 WINDOW 3: svc-irpt reader window for dell2's third served read, ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m without waiting, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (window 3) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 16:06:10Z (816 B; negative control NOT set-equal to ADD, exactly the 2 dell2 elements; also confirms window 2's REMOVE stayed landed, measured live). Signed ADD put with --block-public-policy 16:08:43-16:08:46Z on the issuer's GO 108033 after G2's 'ADD now' 15:56:55Z. Read-back SET-EQUAL to signed ADD (944 B; negative control NOT set-equal to BEFORE, same 2 places inverted); cloudops-dell2-agent-user occurrences 2, cloudops-dell1-agent-user 0. Simulated GetSecretValue against the live policy: dell2 allowed, dell1 explicitDeny, walker user/Andrew_Berman allowed -- exactly the three required, so no revert. NO GetSecretValue call made. Put time relayed to G2 via 0.0.0_AB_MSTR 16:11:49Z. REMOVE due at G2 'R done' or 16:38:46Z; ADD+27m alarm armed for 16:35:46Z. | CLOSED 20261009T161303Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2's 'R done' or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 16:32:07Z (negative control NOT set-equal to BEFORE, the 2 dell2 elements). Signed BEFORE put with --block-public-policy 16:33:03-16:33:06Z on G2's R DONE at 16:22:49Z (relay 108043), 5 min 40 s before the 16:38:46Z hard close. Read-back SET-EQUAL to signed BEFORE (negative control NOT set-equal to ADD, same 2 places inverted); cloudops-dell2-agent-user occurrences 0, cloudops-dell1-agent-user 0. Simulated: dell2 explicitDeny, dell1 explicitDeny, walker user/Andrew_Berman allowed. AC1 WalkerReadsByExplicitArn present. NO GetSecretValue call made by this seat. Window 3 open 16:08:46Z-16:33:06Z, 24 min 20 s; G2's two in-memory reads landed before its 16:22:49Z R DONE. | CLOSED 20261009T163656Z |

## Log

- 20261009T160720Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261009T161303Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 16:06:10Z (816 B; negative control NOT set-equal to ADD, exactly the 2 dell2 el
- 20261009T163656Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 16:32:07Z (negative control NOT set-equal to BEFORE, the 2 dell2 elements). Signed
- 20261009T163657Z CLOSED -- all 2 legs proven
