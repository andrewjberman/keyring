# OPLMCP.02 go-live -- deploy PLAN + ~B handoff (CTO-gated)

**Author:** 0.7.0_AE_CloudOps (base, plan-prep only -- NOT the cutover driver). **Driver:** 0.7.0_AE_CloudOps~B (dedicated OPLMCP lane, fresh-focus) OR base-next-window. **CTO gates this plan; COO has the handoff.** PRD: docs/architecture/NFRA_OPLMCP_PRD.md S10.8 + AC2 (line 100). Grounded 2026-06-23 (Explore fact-sheet; cites below).

## WHY a fresh driver (not me now)
.02 is a LIVE ALB OIDC auth cutover (mis-step = login down fabric-wide) + EC2 code-deploy + live-Graph AC2 gate -- a multi-hour, can't-strand, max-blast-radius deploy. Both leads + Andrew ruled: fatigued (~16h) does NOT run it. This plan is the running start so the fresh driver EXECUTES, not re-grounds.

## TRIPLE GATE before the cutover begins (all 3 required)
1. Outage fully cleared (the W1 deploy-completion lesson -- a live-auth cutover mid-drop strands the worst leg).
2. THIS plan CTO-approved (the driver RAVCs the CTO; CTO GOs; same as W1).
3. Fresh-focus driver (~B loaded, or base next-window) -- NOT a ~16-20h-fatigued agent.

## GROUNDED CURRENT STATE (module infra/aws/terraform/m365-mcp-gateway/)
- **ALB HTTPS listener** `aws_lb_listener.https` (alb.tf:89-106): CURRENT default_action = **fixed-response 503** (alb.tf:96-103). Cert `*.opalinvest.dev`. Output `https_listener_arn`.
- **Target group** `aws_lb_target_group.gw` (alb.tf:58-79): `m365-mcp-gateway-tg`, instance:8080, health `/health` 200-399. The .02 forward target. Currently NotInUse (no listener forwards yet).
- **EC2** `aws_instance.gw` = **i-01d75141177c88b96** (single persistent t4g.nano, no ASG; main.tf:148-180). user_data = box-prep only. Deploy = STAGED `infra/aws/ec2/m365-mcp-gateway/deploy-to-ec2.sh` (DO NOT RUN until .02) wrapped by `infra/aws/ec2/safe-ec2-deploy.sh m365-mcp-gateway`. Artifact `s3://opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway/`. `.env` currently absent -> deploy writes MOCK_GRAPH=1 if absent; .02 forces MOCK_GRAPH=0.
- **IAM** role `m365-mcp-gateway-role` (main.tf:129-136), profile `m365-mcp-gateway-profile`: **SSM-core ONLY** (main.tf:138-141). No S3/secrets grants yet. Output `instance_role_name` ("OPLMCP.02 attaches the secrets-read policy here").
- **Secrets**: `opal/mcp/m365-login` (arn ...m365-login-0yALU6, App-1/OIDC) + `opal/mcp/m365-graph` (arn ...m365-graph-WS5Dui, App-2/Graph) EXIST out-of-band; **ZERO TF references yet** (.02 adds data sources). `opal/mcp/m365-fernet` does NOT exist (.02 creates it; gateway .env.example:22-24 expects FERNET_KEY).

## THE PLAN -- 6 legs, in SAFE EXECUTION ORDER (not the PRD checklist order)

CRITICAL SEQUENCING (the can't-strand insight): the listener OIDC swap is the GO-LIVE moment and must be LAST -- AFTER the gateway is code-deployed + TG-healthy. Swap-before-code = ALB auths users into a dead/503 TG; code-before-swap = gateway runs but listener still 503s (unreachable). So:

**STEP A (TF apply #1 -- secrets + IAM, NO listener swap):**
- A1. Create the Fernet secret: `opal/mcp/m365-fernet` -- self-generated `cryptography.fernet.Fernet.generate_key()`, written to SM via boto3/CLI OUT-OF-BAND (value NEVER in TF/repo). (Same out-of-band pattern as the IT secrets.)
- A2. Add TF secretsmanager DATA SOURCES by ARN for login + graph + fernet (reference only, no value pulled into the listener here).
- A3. Go-live IAM = ONE inline policy on `m365-mcp-gateway-role`: `s3:GetObject` scoped to `arn:aws:s3:::opal-313476888478-lambda-artifacts/ec2/m365-mcp-gateway/*` + `secretsmanager:GetSecretValue` on the THREE ARNs (login, graph, fernet) ONLY. **comp-iam service m365-mcp-gateway + comp-iam gaps BEFORE apply** -- prove scoped (no bucket-wide, no wildcard-secret), no firm-bucket touch. (the W1 design->apply gate.)
- safe-apply (HALTGT) STEP-A TF. 0-diff verify. -> the EC2 can now read its artifact + the 3 secrets.

**STEP B (EC2 code-deploy -- NOT TF):**
- B1. Build + stage the artifact (`safe-ec2-deploy.sh m365-mcp-gateway`, S3 prefix `ec2/m365-mcp-gateway`).
- B2. The `.env`: MOCK_GRAPH=0, PUBLIC_BASE_URL=https://mcp.opalinvest.dev, App-2 (Graph) client_id/secret/tenant from `opal/mcp/m365-graph`, FERNET_KEY from `opal/mcp/m365-fernet`. (gateway reads secrets at runtime via the STEP-A IAM.)
- B3. `verify-ec2.sh` parity + **VERIFY the gateway is HEALTHY**: the TG `/health` check passes (200-399), the gateway started, reads secrets OK, MOCK_GRAPH=0. DO NOT proceed to STEP C until /health is green.

**STEP C (TF apply #2 -- the GO-LIVE listener swap):**
- C1. `aws_lb_listener.https` default_action: fixed-response 503 -> `authenticate-oidc` (App-1 = `opal/mcp/m365-login`: issuer/authorization_endpoint/token_endpoint/user_info_endpoint for tenant 6810043e-d171-4adc-9975-068b35e179da + client_id + client_secret) THEN `forward` to `aws_lb_target_group.gw`.
- C2. **TF-STATE-SECRET-VALUE CHOICE -- FLAGGED FOR CTO RULING:** authenticate-oidc requires `client_secret` (App-1). Options: (a) placeholder client_secret in TF + `lifecycle { ignore_changes = [...client_secret] }` + set the REAL secret post-apply via `aws elbv2 modify-listener` (real value NEVER in TF state -- cleanest hygiene, one manual post-apply step); (b) a `data "aws_secretsmanager_secret_version"` pulls it -> client_secret lands in TF state (encrypted at rest in the S3 backend). **AE RECOMMENDS (a)** (keeps the OIDC client_secret out of state entirely; CTO's "prefer CLI/post-apply" path). CTO rules.
- safe-apply (HALTGT) STEP-C TF. 0-diff verify. -> **GO-LIVE** (ALB now OIDC-auths -> forwards to the healthy gateway).

**STEP D (AC2 hard gate -- live, not infra-alone; PRD line 100/106):**
- D1. A REAL non-Andrew user authenticates at the ALB against Entra, reaches their OWN mail via `/me` + `/outlook` against LIVE Graph (MOCK_GRAPH=0).
- D2. PER-USER-SCOPE PROOF: demonstrably CANNOT reach another user's data. (This is the cert gate -- CVO has a verify plan: org/tier1_exec/3.0.0_SA_CVO/OPLMCP_cert_verify_plan_AC2_AC3_AC4_20260623.md.)

## DEPLOY-DISCIPLINE (the W1 pattern -- bind the driver)
- ONE deploy-ledger covering STEP A + STEP C (+ note the B code-deploy leg) -- opened at apply-start, both TF applies + the code-deploy are legs of ONE go-live; all finish-in-session or roll back + escalate loud (NEVER a stranded auth'd-but-dead gateway).
- comp-iam (STEP A) = the apply-gate proof. HALTGT on every safe-apply. 0-diff per apply. Tag (m365-mcp-gateway-vX) + push --follow-tags. Close the ledger when infra + code are live + /health green; AC2 (STEP D) is the post-deploy live-verify (event/manual, not a deploy-blocker leg but the AC gate).
- ROLLBACK: STEP C is the reversible-est line -- if AC2 fails or the gateway misbehaves, revert the listener default_action to fixed-503 (re-apply) = instantly un-expose, no user stuck in a broken auth. Keep that revert one command away.

## ~B HANDOFF -- running-start checklist
- [ ] Confirm outage cleared + you're fresh-focus.
- [ ] Read this plan + PRD S10.8 + AC2.
- [ ] Plan is CTO-GO'd (2026-06-23 -- see CTO RULINGS below); ~B's ONLY CTO checkpoint = RAVC the STEP-A comp-iam service+gaps + plan-diff BEFORE the STEP-A apply.
- [ ] Execute STEP A->B->C->D in order; STEP C (the swap) ONLY after STEP B /health green.
- [ ] deploy-ledger open->close; comp-iam pre-apply; HALTGT; finish-in-one-go; outage-window mind.
- [ ] RAVC CTO+COO at go-live + AC2 result; signal CVO for the cert.
- Secrets ARNs: login `arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/mcp/m365-login-0yALU6`, graph `...:secret:opal/mcp/m365-graph-WS5Dui`, fernet (you create). Tenant `6810043e-d171-4adc-9975-068b35e179da`. EC2 `i-01d75141177c88b96`. Listener `aws_lb_listener.https` (alb.tf:89-106). Role `m365-mcp-gateway-role`. TG `aws_lb_target_group.gw` (/health).

## CTO RULINGS + EXECUTION GATING -- PLAN GO'd 2026-06-23 (CTO)

CTO-GO on the full plan; A->B->C->D + listener-swap-LAST endorsed (the can't-strand design). Rulings folded so ~B inherits the GO'd plan -- ~B does NOT re-RAVC the whole plan; its only CTO checkpoint is the STEP-A comp-iam (below).

**RULING 1 (TF-state-secret) = (a):** placeholder client_secret in the TF authenticate-oidc block + `lifecycle { ignore_changes = [...authenticate_oidc...client_secret] }` + CLI-set the REAL secret post-apply via `aws elbv2 modify-listener` (value from opal/mcp/m365-login). The real OIDC client_secret NEVER enters TF state (matches PRD S6 strict secret-footprint; (b) data-source-into-state was REJECTED -- copies the secret into a 2nd store + widens read-surface). DOCUMENT the CLI-set as a RUNBOOK step -- **re-run it on ANY listener recreate** (ignore_changes means TF won't re-apply it). apply-placeholder -> immediate-CLI-set-real is ONE atomic STEP C (the brief dummy-secret window = the cutover seconds only).

**RULING 2 (ledger) = APPROVED:** ONE deploy-ledger wrapping STEP A (IAM+secrets apply) + STEP B (code-deploy leg, noted) + STEP C (listener swap = go-live); opened at A-start, **CLOSED at STEP C GO-LIVE-VERIFIED** (curl through the OIDC flow returns the gateway, NOT the 503). Finish A->C in the ONE fresh ~B session, or roll back (revert listener->503; gateway code stays) + escalate loud.

**EXECUTION GATING (~B, the fresh lane):**
- Triple-gate holds: outage-cleared + this plan-GO + fresh ~B driver.
- ~B RAVCs CTO the STEP-A comp-iam service+gaps + plan-diff BEFORE the STEP-A apply (the IAM = the security gate; CTO confirms no firm/Deny loosened + scoped to the 3 ARNs only, like W1). **This is ~B's last checkpoint to the CTO.**
- ~B owns the B->C gate: STEP B /health GREEN is the HARD precondition for STEP C swap (NEVER swap into an unhealthy TG).
- ~B RAVCs CTO + CVO at STEP C go-live-complete -> CVO runs AC2 (STEP D) on the SYNTHETIC test mailboxes.

**GO-LIVE EXPOSURE (note, not a blocker):** STEP C makes the infra LIVE (tenant users CAN auth at the ALB). Broad EMPLOYEE rollout (broadcasting the URL + onboarding) is GATED on AC2-pass + AC5 (PRD: no non-Andrew onboarding before AC5). The C->AC2 window has ONLY Andrew + the synthetic test users; the global KILL_SWITCH is the backstop. **DO NOT broadcast the URL until AC2+AC5 clear.**
