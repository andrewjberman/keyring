# Deploy Completion Record
**Date opened:** 2026-10-09T14:18:13.594516+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T143823Z
**Deploy:** TO30 AMENDMENT 1 RETRY: svc-irpt reader window for dell2's served read of REQ-5e4149d2, ledger irpt-ycdgen-served-read-20261009; REMOVE at G2 'R done' or ADD+30m without waiting, this seat holds the clock; no GetSecretValue
**Authored by:** 0.7.0_AE_CloudOps~CTL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 0.5h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| ADD | activation | svc-irpt secret resource policy set to the signed ADD file (retry) | Live BEFORE set-equal at the start; signed ADD put with --block-public-policy; read-back ADD set-equal; dell2 allowed, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed BEFORE at 14:17:11Z (816 B; negative control NOT set-equal to ADD, exactly the 2 dell2 elements). Signed ADD put with --block-public-policy 14:19:47-14:19:50Z. Read-back SET-EQUAL to signed ADD (944 B; negative control NOT set-equal to BEFORE, same 2 places inverted); cloudops-dell2-agent-user occurrences 2, cloudops-dell1-agent-user 0. Simulated GetSecretValue against the live policy: dell2 allowed, dell1 explicitDeny, walker user/Andrew_Berman allowed -- exactly the three required, so no revert. NO GetSecretValue call made. Put time relayed to G2 via 0.0.0_AB_MSTR 14:23:02Z. REMOVE due at G2 'R done' or 14:49:50Z; ADD+27m alarm armed at 14:46:50Z. | CLOSED 20261009T142437Z |
| REMOVE | activation | svc-irpt secret resource policy restored to the signed BEFORE file at G2's 'R done' or ADD+30m | Live ADD set-equal at the start; signed BEFORE put with --block-public-policy; read-back BEFORE set-equal; dell2 explicitDeny, dell1 explicitDeny, walker allowed; no GetSecretValue | Live start SET-EQUAL to signed ADD at 14:34:14Z (negative control NOT set-equal to BEFORE, the 2 dell2 elements). Signed BEFORE put with --block-public-policy 14:35:05-14:35:09Z on G2's R DONE at 14:26:19Z (relay 107997), 14 min 41 s before the 14:49:50Z hard close. Read-back SET-EQUAL to signed BEFORE (negative control NOT set-equal to ADD, same 2 places inverted); cloudops-dell2-agent-user occurrences 0, cloudops-dell1-agent-user 0. Simulated: dell2 explicitDeny, dell1 explicitDeny, walker user/Andrew_Berman allowed. AC1 WalkerReadsByExplicitArn present. NO GetSecretValue call made by this seat. Retry window open 14:19:50Z-14:35:09Z, 15 min 19 s; G2's one read landed ~14:26:12Z inside it. | CLOSED 20261009T143823Z |

## Log

- 20261009T141813Z OPENED by 0.7.0_AE_CloudOps~CTL with 2 leg(s)
- 20261009T142437Z LEG ADD closed: Live start SET-EQUAL to signed BEFORE at 14:17:11Z (816 B; negative control NOT set-equal to ADD, exactly the 2 dell2 el
- 20261009T143823Z LEG REMOVE closed: Live start SET-EQUAL to signed ADD at 14:34:14Z (negative control NOT set-equal to BEFORE, the 2 dell2 elements). Signed
- 20261009T143823Z CLOSED -- all 2 legs proven
