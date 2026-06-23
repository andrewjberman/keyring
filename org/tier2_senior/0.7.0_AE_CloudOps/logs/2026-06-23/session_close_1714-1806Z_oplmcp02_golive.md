# Session Log — 0.7.0_AE_CloudOps~B — OPLMCP.02 backend GO-LIVE cutover

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, IMPLEMENT

**Window:** 2026-06-23 ~1714Z -> ~1806Z (fresh ~B session; first log)
**Serial:** 0.7.0_AE_CloudOps~B (dedicated OPLMCP lane)

## Summary

Loaded as the dedicated fresh-focus OPLMCP lane and DROVE the OPLMCP.02 backend go-live
cutover (M365 MCP gateway) end-to-end: STEP-A (secrets + scoped IAM + forced EC2 replace) ->
STEP-B (code-deploy, MOCK_GRAPH=0, /health green) -> STEP-C (listener 503 -> authenticate-oidc
= GO-LIVE). Finished A->C in one session, zero strand; ledger CLOSED. CTO-GO'd plan + 2 rulings
honored. The cutover is the can't-strand sequence with the listener swap LAST.

## Deployment Sequence + Verification (AE)

1. **Re-grounded live state** (the GO'd plan's "current state" was a BANNED Explore-agent
   fact-sheet = fabricated; it missed the drift). Caught: EC2 i-01d75141177c88b96 STOPPED +
   mis-networked (public-IP=false -> no Graph egress), TF baseline NOT 0-diff (forced instance
   replace: AMI drift + associate_public_ip_address false->true). RAVC'd both findings to CTO.
2. **STEP-A** (commit fcaf0c062 secrets-iam.tf, bc31279c5 manifest, tag v1.1.0):
   - Fernet secret opal/mcp/m365-fernet created out-of-band (value never in TF/repo).
   - safe-apply tfplan.stepa (HALTGT) = `3 added, 0 changed, 2 destroyed`. EC2 REPLACED
     i-01d75141177c88b96 -> **i-07dccb1615503ac99** (CTO-ACCEPTED; correctly-networked fresh
     box: running, PublicIP 44.203.66.93, latest AMI). aws_iam_role_policy.gw_golive created
     (scoped s3:GetObject ec2/m365-mcp-gateway/* + secretsmanager:GetSecretValue on 3 ARNs, no
     kms -- AWS-managed secret key).
   - post-apply re-plan = "No changes" (CONVERGED). EC2_MANIFEST Rule-8 update -> new id.
3. **STEP-B** (commit 097e840a2 + 628c29ca6 deploy-to-ec2.sh, ccd684c57 manifest record):
   - Modified deploy-to-ec2.sh to write the real MOCK_GRAPH=0 .env by fetching App-2 Graph
     creds (opal/mcp/m365-graph) + Fernet on-box (instance gw_golive grants GetSecretValue) ->
     values stay on the box, never in SSM-text/repo.
   - **Caught + fixed a latent bug in the never-run staged script:** SSM `--parameters
     commands="$(jq -Rs .)"` passed literal \n (remote collapsed to one line: `set:
     pipefailnsudo`). Fixed to a JSON array `jq -Rs '{commands: split("\n")}'` (628c29ca6).
   - safe-ec2-deploy SSM deploy = Success. Verified ON-BOX (not wrapper self-report): systemd
     m365-mcp-gateway ACTIVE; **/health = {"ok":true}**; MOCK_GRAPH=0; TENANT_ID/CLIENT_ID/
     CLIENT_SECRET/FERNET_KEY all SET; .env perms 600; server.py md5 77c43d975f03fdf8b5cec2ff5e233d10.
     ALB->gateway SG path open (gw SG 8080 from ALB SG sg-0920efdb81831611f).
4. **STEP-C GO-LIVE** (commit e17ffac4d alb.tf, tag v1.2.0):
   - safe-apply tfplan.stepc (HALTGT) = `0 added, 1 changed, 0 destroyed`: listener IN-PLACE
     503 -> authenticate-oidc (App-1 m365-login; tenant 6810043e..., client_id 53360468...,
     v2.0 endpoints, scope openid+profile+email) + forward to TG. ARN preserved.
   - Ruling-1: client_secret PLACEHOLDER in TF + lifecycle.ignore_changes; REAL secret CLI-set
     post-apply via `aws elbv2 modify-listener` (value never in TF state; staged from a 600
     scratchpad file, shredded). modify-listener needed a Windows path (aws.exe can't read the
     Git-Bash /c/ form) -- closed the brief placeholder window on the 2nd call.
   - **GO-LIVE VERIFIED:** curl https://mcp.opalinvest.dev/ = HTTP 302 -> login.microsoftonline.com
     /6810043e.../oauth2/v2.0/authorize (correct client_id/redirect_uri=/oauth2/idpresponse/
     scope; NOT 503). TG target i-07dccb1615503ac99 = HEALTHY. post-apply re-plan = "No changes"
     (CONVERGED; ignore_changes hides the secret).
   - Ledger oplmcp02-golive-cutover CLOSED (all 3 legs proven, zero stranded).

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-to | NFRA_OPLMCP.02 | OK | race-free per-session TO_ID |
| comp-iam service | m365-mcp-gateway | COVERAGE-GAP | "No service matching" -- new EC2 svc not modeled -> manual IAM review (CTO-confirmed: no graph backs it = manual is correct, graph-presence principle) |
| comp-iam gaps | (all modeled) | PASS | no MISSING-perm gaps among modeled svcs (gateway out of scope) |

**What worked:** comp-iam correctly reported the gateway is unmodeled, which (per the comprail
governing principle) is the signal to fall back to a manual scoped-IAM review -- CTO confirmed
the policy (prefix-scoped S3 + 3-ARN GetSecretValue, no-kms).
**What failed:** n/a.
**Gap found:** m365-mcp-gateway is not modeled in comp-iam -> follow-on COVERAGE-GAP (model the
gateway; routed to CVO TO-5 (i)-bucket). comp-pipescript/comp-blast N/A this session (no
data-pipeline/gold run; the gateway is an EC2 MCP access-layer service, tracked in
EC2_MANIFEST.json, not a comp-graph-backed pipeline). One rail-checked raw-aws SG verify
(verify-own-change-vs-live, F5; no comp-tool models this gateway's SG).

## Files Modified

see commit messages: fcaf0c062, bc31279c5, 097e840a2, 628c29ca6, ccd684c57, e17ffac4d, 9f2c389c9.
- New: infra/aws/terraform/m365-mcp-gateway/secrets-iam.tf
- Modified: alb.tf (listener swap), deploy-to-ec2.sh (.env + SSM fix), EC2_MANIFEST.json (Rule 8),
  NFRA_OPLMCP.02 TO (-> complete).

## Blockers

None. AC2 (the /me+/outlook live-call + per-user-scope cert) is the CVO post-go-live gate, not a
blocker on my lane.

## Current State (handoff)

- **M365 MCP gateway is GO-LIVE.** ALB m365-mcp-gateway (listener arn .../4751a29f69442c23) =
  authenticate-oidc (App-1, real secret) + forward to TG (m365-mcp-gateway-tg) -> EC2
  **i-07dccb1615503ac99** (running, MOCK_GRAPH=0 live Graph, /health green, secrets from SM,
  .env 600). Public URL https://mcp.opalinvest.dev (unauth -> 302 Entra; MCP at /mcp).
- gw_golive IAM = scoped s3:GetObject (artifact prefix) + GetSecretValue (3 ARNs). Real OIDC
  client_secret is on the listener via CLI-set (NOT in TF state; ignore_changes). RUNBOOK: on
  ANY listener recreate, re-run the CLI set-secret (see alb.tf header).
- Tags m365-mcp-gateway-v1.1.0 (STEP-A) + v1.2.0 (go-live). Ledger CLOSED.
- GO-LIVE EXPOSURE: LIVE but URL NOT broadcast; broad rollout gated on AC2+AC5; only Andrew +
  synthetic users in the C->AC2 window; KILL_SWITCH backstop.

## Next Steps

- **[3.0.0_SA_CVO]** run AC2 on synthetic mailboxes (real non-Andrew user authenticates ->
  /me + /outlook live + per-user-scope proof), walking the LIVE authenticated wire-path to the
  pixel (per OPLMCP_cert_verify_plan_AC2_AC3_AC4_20260623.md). Synthetic Entra test users +
  AC5 ordering are the remaining IT/Andrew deps your plan flagged.
- **[2.0.0_SA_COO / 1.0.0_SA_CTO]** project-level close of NFRA_OPLMCP.02 after AC2 cert; relay
  done to MSTR (PING-ME-ON-DONE was COO-addressed).
- **[follow-ons, non-blocking]** (1) model m365-mcp-gateway in comp-iam (CVO TO-5 i-bucket);
  (2) safe-ec2-deploy.sh Windows-charmap wrapper crash (post-successful-SSM; manifest recorded
  manually this time).
- **[0.7.0_AE_CloudOps~B]** standing by post-go-live for AC2-driven infra needs or next dispatch.

## MCP traffic

~11 messages. Significant: COO DRIVE GO (cutover, you own the lane); CTO STEP-A apply-GO (both
findings ruled: manual-IAM CONFIRMED + EC2-replace ACCEPTED); RAVC'd CTO+COO at each step (A
apply / B health / C go-live); RAVC2 CTO go-live + CVO AC2 handoff + COO done. 2 stale 06-17
ferry relays cleared (were tripping HALTGT).
