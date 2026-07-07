# Deploy Completion Record
**Date opened:** 2026-07-07T06:17:48.042668+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260707T064438Z
**Deploy:** SCTY safety-caps: MCPGUARD G1 blast-radius-cap+G3-confirm + PREMCP P0 token-revocation kill-path -> LIVE m365-mcp-gateway EC2 (Andrew-direct named first-moves, CTO arch-gate 054249Z, COO deploy-lane GO 061535Z).
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD 463a3d339 (G1+P0, 5 files) pushed origin/CLOUD | hash pushed | 463a3d339 (G1 blast_cap.py+tools.py+config; P0 revocation.py+oauth_as.py+config; 5 files) committed + pushed origin/CLOUD (branch -r --contains: origin/CLOUD) | CLOSED 20260707T061810Z |
| L2 | activation | safe-ec2-deploy.sh m365-mcp-gateway (Rule 7/12: tarball->S3->SSM-pull->restart m365-mcp-gateway.service) | SSM deploy Success + service restarted | safe-ec2-deploy.sh m365-mcp-gateway SUCCESS: tarball->S3->SSM-pull->restart. Deploy output: systemd 'active', /health {ok:true}, 'AS metadata serves', '/mcp unauth -> 401'. server.py+oauth_as.py md5'd on box. Manifest recorded 35f9b1088 (deployed_by corrected to 0.7.0_AE_CloudOps~A). | CLOSED 20260707T062412Z |
| L3 | verify | gateway service HEALTHY post-restart (systemd active + a read tool works + blast_cap/revocation modules import on-box) | service active + read-tool OK | On-box SSM verify (i-07dccb1615503ac99): app/blast_cap.py (6782B) + app/revocation.py (6265B) PRESENT; '.venv/bin/python -c from app import blast_cap, revocation' -> 'OK: modules import' (no import errors); systemctl is-active -> 'active'. My commit 463a3d339 confirmed ancestor of the deployed 49cde81a (git merge-base). Service healthy + new modules load. | CLOSED 20260707T062412Z |
| L4 | verify | CVO LIVE-cert PASS: (G1) mass-send>cap -> confirm_required NOT-sent; (P0) revoke-jti -> validate DENIES live; blocklist-user -> refresh DENIED | CVO PASS artifact (live req/resp evidence) | CVO live-cert PASS (both caps BITE live, exercised not config-read, box i-07dccb1615503ac99, throwaway identity, no-real-send canary, lists cleaned): P0 revoke-jti->DENIED 'invalid_token: token has been revoked' (hot-reload no-restart) + revoke-user old-DENIED/fresh-VALID; G1 blast_cap.evaluate 6/6 + END-TO-END _run canary #3 send_email-26-unconfirmed->confirm_required + SEND-fn-called=0 (Graph POST never reached = structural no-send proven), #4 confirmed->proceeds, #5 <=25->proceeds. CC COO. | CLOSED 20260707T064437Z |

## Log

- 20260707T061748Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20260707T061810Z LEG L1 closed: 463a3d339 (G1 blast_cap.py+tools.py+config; P0 revocation.py+oauth_as.py+config; 5 files) committed + pushed origin/CLOU
- 20260707T062412Z LEG L2 closed: safe-ec2-deploy.sh m365-mcp-gateway SUCCESS: tarball->S3->SSM-pull->restart. Deploy output: systemd 'active', /health {o
- 20260707T062412Z LEG L3 closed: On-box SSM verify (i-07dccb1615503ac99): app/blast_cap.py (6782B) + app/revocation.py (6265B) PRESENT; '.venv/bin/python
- 20260707T064437Z LEG L4 closed: CVO live-cert PASS (both caps BITE live, exercised not config-read, box i-07dccb1615503ac99, throwaway identity, no-real
- 20260707T064438Z CLOSED -- all 4 legs proven
