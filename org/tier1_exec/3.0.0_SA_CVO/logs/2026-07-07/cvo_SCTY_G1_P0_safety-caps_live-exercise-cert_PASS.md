# CVO Live-Exercise-Cert — SCTY G1 (blast-radius cap) + P0 (token-revoke kill-path): PASS

**Date:** 2026-07-07T06:40Z
**Agent:** 3.0.0_SA_CVO
**Gateway:** https://mcp.opalinvest.dev (box i-07dccb1615503ac99, /opt/m365-mcp-gateway). Deployed by 0.7.0~A (L1-L3 closed). This = L4 (CVO live-cert). Andrew-named safety-caps (first-moves B).
**Method:** LIVE exercise on the deployed box via SSM (throwaway test identity cvo-cert@opalinvest.com; canary fn stands in for the Graph POST -> zero real send; test-only revoke lists cleaned). NOT config-read.
**Baseline (pre-deploy):** NO blast-cap + NO token-revoke = uncapped/unrevocable. The certs prove the net-new safety.
**Verdict:** PASS -- both caps BITE live. = 2 of Andrew's 3 named first-moves CVO-certified DONE.

## P0 -- token-revocation kill-path (exercised on-box)
- P0.1 revoke-jti: minted test token -> validate PASSES (before). `python -m app.revocation revoke-jti <jti>` -> re-validate = **DENIED "invalid_token: token has been revoked"**. Live, hot-reloaded, no restart. The leaked-token kill-path WORKS.
- P0.2 revoke-user: token A (old) valid -> `revoke-user` -> token A **DENIED** (iat<cutoff); a FRESH token B (iat>cutoff) stays **VALID**. Cutoff-based revoke correct (denies the leaked window, not a permanent ban).
- Verify-before-cleanup: the deny-lists contained ONLY the cvo-cert throwaway identity (no production entries) -> cleaned safely (both files removed, confirmed absent).

## G1 -- blast-radius cap + G3 confirm (exercised: decision + END-TO-END no-send)
Caps (blast_cap._SEED_CAPS): standard=25 recipients / master_admin=200.
(a) DECISION exercise -- blast_cap.evaluate(tool,args,tier,confirmed), 6 scenarios ALL PASS:
  - send_email 26/standard unconfirmed -> confirm (blast_cap_exceeded); 26/standard CONFIRMED -> allow; 25/standard -> allow; 201/master -> confirm; reply_email/standard -> confirm (confirm_on_irreversible); send_channel_message/MASTER -> confirm (safety-not-authz, even master).
(b) END-TO-END _run exercise (canary fn = the send path; 0 = NO SEND) -- the load-bearing no-send, EXERCISED not source-read:
  - #3 send_email 26 unconfirmed -> confirm_required=True, code=blast_cap_exceeded, **SEND-fn-called=0** (the Graph POST lambda is NEVER reached -- structurally-and-exercised NO SEND).
  - #4 send_email 26 CONFIRMED -> proceeds, SEND-fn-called=1 (the sanctioned second factor bypasses the cap).
  - #5 send_email 25 unconfirmed -> proceeds, SEND-fn-called=1 (under-cap = no friction).
Integration (tools.py _run, source-confirmed + exercised): blast_cap.evaluate runs AFTER G2-guard, BEFORE _user_token()/fn(token); a confirm decision returns {confirm_required} + audit.log_call "confirm_required" (NO "ok" send record) and never reaches graph.call POST /me/sendMail.

## Verdict
G1 + P0 = PASS. The blast-radius cap BITES (>cap/uncountable -> confirm_required, send-fn NOT called = NO SEND) with the second-factor + no-friction-under-cap both working; the token-revocation kill-path WORKS (revoke-jti denies live, revoke-user denies old/keeps fresh, hot-reloaded). L4 closes -> 2 of Andrew's 3 named safety-cap first-moves CVO-certified DONE. Additive to the SCTY-certed enforce/validate paths (intact). Clean-up done (no test artifacts left on the box).
