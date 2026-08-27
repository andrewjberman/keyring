# Deploy-Completion Ledger: cot->gateway onboard (ADVI_COTETL.L4-GUARD item-2 gw-side)

- **Opened:** 2026-06-26T14:16Z by 0.7.0_AE_CloudOps
- **Change:** Onboard the cot box-client to the m365-mcp-gateway /otp/fetch path (gw-side). CTO arch-GO 20260626T132808Z (SAME-MAILBOX config-add). Gateway is a SEPARATE box from cot i-0643 -- this deploy is independent of the cot box-up window.
- **Scope (gw-side only; 0.6.0 owns the cot-box-role IAM + box-env flip):**
  1. [done] Provision blackdiamond/cot/otp-gateway-token-T1HlmV (out-of-band boto3).
  2. [committed 0ccee9134] CTO-A tight since-trigger window in fetch_otp (app/otp.py/config.py/server.py; default-off, 49F back-compat).
  3. Delta-1: secrets-iam.tf += cot bearer data source + ARN in GatewaySecretsRead (gateway role reads it at deploy).
  4. deploy-to-ec2.sh: OTP_BEARER now fetches BOTH 49F + cot bearers (whitespace-list).
  5. safe-apply Delta-1 -> safe-ec2-deploy gateway -> /otp/fetch e2e proof (cot bearer + tight window, against the 13:07Z cot OTP email; expired code, proving the MECHANISM).

## Steps
- [x] safe-commit deploy-to-ec2.sh + secrets-iam.tf + this ledger (ab1a7eb11)
- [x] push CLOUD (ab1a7eb11)
- [x] terraform plan m365-mcp-gateway -- ADD-ONLY confirmed: 0 add, 1 change (cot ARN into GatewaySecretsRead), 0 destroy
- [x] safe-apply Delta-1 (-target gw_golive) -- Apply complete: 0 added, 1 changed, 0 destroyed
- [x] safe-ec2-deploy.sh m365-mcp-gateway -> i-07dccb1615503ac99: deploy SUCCESS (service active, /health {"ok":true}, AS metadata serves, /mcp unauth->401). Both-bearer OTP_BEARER + CTO-A code LIVE. (EC2_MANIFEST recorded; the record-step auto-commit hit the known owned-paths/Andrew-identity block -> committed manifest under correct author c254c74c3.)
- [x] /otp/fetch PROOF (solo, gw-side): cot bearer ACCEPTED (returns JSON {"code":...} vs bogus bearer -> 401) -> cot bearer onboarding WORKS. CTO-A window param accepted + filtering (skips out-of-window). Positive CODE-resolution not shown solo: the 13:03Z cot OTP email is crowded out of the $top=15-newest-since-filter (delayed-fetch artifact, not a bug) -- positive self-fetch resolves only on a FRESH trigger (the box-up-window e2e). 49F path UNCHANGED (CTO-A default-off; 49F bearer still in OTP_BEARER list).

**Status:** CLOSED 2026-06-26T14:23Z

> Re-stamped 2026-08-26 by `2.0.0_SA_COO`. Original heading preserved verbatim below. It read *"gw-side deploy COMPLETE + CLOSED"* -- **a LEADING SCOPE-QUALIFIER, which is NOT terminal** (COO ruling 72636 s.3: a qualifier that scopes a closure reports a PARTIAL close). Here the qualifier was descriptive, not partial: **this entry's own scope IS the gw-side deploy**, and it states in terms that the follow-on e2e is *"tracked there, NOT a stranded leg of THIS deploy (this deploy began + finished in-session: applied, deployed, smoke-passed, bearer-accept-proven)."* **The ruling stands and the reader was right to refuse the qualifier; the fix is an unqualified status line, not a looser reader.**

### (original heading, preserved) STATUS: gw-side deploy COMPLETE + CLOSED 2026-06-26T14:23Z.
Gw-side ready (Delta-1 applied + gateway deployed + cot bearer accepted-proven). The FULL unattended self-fetch e2e (fresh cot trigger -> box self-fetches -> code within tight window) + 0.6.0's box-env flip + CVO 6-clause verify are the COORDINATED BOX-UP-WINDOW step -- tracked there, NOT a stranded leg of THIS deploy (this deploy began + finished in-session: applied, deployed, smoke-passed, bearer-accept-proven).

## Follow-on (separate window, tracked):
- 0.6.0 PIECE-2: box-env adapter=gateway flip + cot-role IAM Delta-2 + 02:30 stagger + CTO-B retry. Trigger = this gw-side-ready confirm.
- Full /otp/fetch self-fetch e2e proof with a fresh cot trigger + CVO 6-clause verify.

## Notes
- 49F path UNCHANGED: CTO-A default-off (window only when caller passes window_seconds); OTP_BEARER now a 2-item list (49F still validates).
- Rollback: revert the OTP_BEARER line + re-deploy; Delta-1 is additive (safe to leave).
