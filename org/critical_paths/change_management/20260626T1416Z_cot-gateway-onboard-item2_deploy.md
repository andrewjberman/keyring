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
- [ ] safe-commit deploy-to-ec2.sh + secrets-iam.tf + this ledger
- [ ] push CLOUD
- [ ] terraform plan m365-mcp-gateway (expect ADD-ONLY: 1 data source read + 1 inline-policy ARN; 0 destroy/0 replace) -- -target the gw_golive policy if other diffs
- [ ] safe-apply Delta-1; 0-diff verify
- [ ] comp-iam service: confirm cot bearer ARN now GRANTED on the gateway role
- [ ] safe-ec2-deploy.sh m365-mcp-gateway deploy-to-ec2.sh (builds tarball w/ CTO-A code + both-bearer OTP_BEARER; ~3s restart of the LIVE gateway -- routine redeploy, MCP/teams clients reconnect)
- [ ] verify gateway /health + /mcp 401 + AS metadata (deploy script smoke)
- [ ] PROVE /otp/fetch: curl with cot bearer + since-window matching the 13:07Z cot OTP -> resolves the cot code (mechanism proof)
- [ ] RAVC COO + confirm to 0.6.0 (gw-side ready -> their PIECE-2 box flip) + CVO 6-clause
- [ ] CLOSE ledger

## Notes
- 49F path UNCHANGED: CTO-A default-off (window only when caller passes window_seconds); OTP_BEARER now a 2-item list (49F still validates).
- Rollback: revert the OTP_BEARER line + re-deploy; Delta-1 is additive (safe to leave).
