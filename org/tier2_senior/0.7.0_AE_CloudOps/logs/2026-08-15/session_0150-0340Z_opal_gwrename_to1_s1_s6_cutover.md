# 0.7.0_AE_CloudOps -- session 2026-08-15 0150-0340Z -- OPAL_GWRENAME.TO-1 S1-S6 live cutover (m365 -> opal-gateway)

**archetype:** DEPLOY

**Authority:** Andrew-direct 2026-08-15 VERBATIM *"Ok let's get this whole thing done, no one is online but
you so if you need other agents instantiate them now with relevant instructions."* -> MSTR TO draft ->
COO adoption @8dfa20c274 + GO 015633Z. Spec: `docs/runbooks/opal-gateway-rename-cutover-runbook.md`
@c0e8ead091 (LD-0414/LD-0415). Driver/verifier 2.0.0_SA_COO; arch/integration/push 0.0.0_AB_MSTR.

## Outcome

**CUTOVER COMPLETE, S1-S6, in-session.** Every live-plane name is `opal-*`; `mcp.opalinvest.dev`
serves the new tree on the new ALB; consent state migrated; old plane retired (secrets in 30d
recovery). Deploy-completion ledger `org/critical_paths/change_management/20260815T0230Z_opal-gwrename-s3-cutover_deploy_completion.md`
OPENED 0230Z / CLOSED 0336Z. Proof-of-spec `deliverables/PROOF_OF_SPEC_OPAL_GWRENAME_TO-1_20260815.json`
VALID (12/12 GW rows). Final census: 0 m365 on all 14 surfaces, denominators printed, COO-reproduced.

## What happened, stage by stage (commits all mine, UNPUSHED -- MSTR holds the push)

- **S1** additive: 4 secret twins (sha256 4/4 MATCH, in-memory) + S3 tree copy (38/38). COO-validated.
- **S2** @a7312b946b: var.name flip, default_tags, 8 lambda literals, secrets.tf/secrets-iam.tf repoint,
  CBD on ALB+TG, deploy-to-ec2.sh unpinned with ART DERIVED from $SERVICE (kills the producer class,
  MSTR's addition), EC2_MANIFEST key. State surgery (backup -> rm x4 -> import x4 at 0-diff). Plan
  40/7/35, `aws_instance.gw` IN-PLACE (stop-condition CLEAR). user_data edit @3e8c3522f1 executed per
  MSTR conditional then REVERTED @f6031fd6f7 per converged ruling (in-place hides a STOP/START, an
  Andrew-reserved act). CRLF revert artifact caught on the sanity re-plan (0-diff after LF restore).
- **S3** apply #1 rc=1: **SG-replacement deadlock** (destroy-first vs live ENI) after the old listeners
  had already been destroyed -> **~35 min full outage** on mcp.opalinvest.dev, disclosed same minute to
  COO+MSTR. Rolled FORWARD (rollback was no longer a restore path): CBD on both SGs @e0e4c62fba,
  apply #2 rc=0, post-plan "No changes". H1 OIDC client_secret re-set IMMEDIATELY on the new listener
  (in-memory from opal-gateway-login, ClientId cross-checked); unauth curl 302 -> Entra. WAF assoc read.
  IAM simulate 5 allowed + negative control implicitDeny (separate invocations).
- **S4** three deploy attempts: #1 died on BARE jq locally (masked error); #2 reached the box and the
  fresh venv **crash-looped on unpinned mcp 2.0.0** (fastmcp removed) -> old unit restarted on-box, pin
  mcp==1.28.0 from the live old venv @81615fbd3e (+ bounded readiness wait replacing the ACTIVATING-rc=3
  false-negative); #3 green ON-BOX (active, /health, /mcp 401, 9/9 md5, mcp 1.28.0) though the wrapper
  rc=1 on its own bind-race curl. Pre-fixes @90b89562bc: unit-file CONTENT still pointed 4 literals at
  /opt/m365 (renamed at P0, content not); old unit holds :8080 so stop-old-first guard (runbook's
  new-before-old order physically unsatisfiable, COO amended). Manifest recorded manually (Rule 8).
- **GW-12** (added by MSTR/COO): the deploy orphaned the per-user Microsoft token cache (non-regenerable
  consent state, only at old /opt). SSM agent went ConnectionLost ~0310-0320Z (likely nano OOM from
  venv builds); MSTR ruled NO REBOOT (convenience vs blind :8080 race); agent self-recovered; units read
  APPLIED (opal enabled / m365 disabled -> boot deterministic), 4 blobs cp -a, restart, MSTR oracle
  whoami = full Graph payload (COO corroborated).
- **S5** GW-6 re-scoped (all MCP paths bypass ALB OIDC via prio-10; cold seat tests the NEW-SESSION
  claim, H1 stays DESIRED-grade): 2 cold seats PASS bracketing the copy. Census 0 m365 live.
- **S6** secrets scheduled 30d (never force) + controls; 38 S3 objects deleted, 0 remain; 2 log groups
  deleted; on-box insurance cache copy (md5 4/4) then old unit file + /opt/m365 (142M) removed; state
  key migrated @25202b96e1 with ETag-verified in-bucket backup, plan "No changes" after.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-to | OPAL_GWRENAME.TO-1 | OK | race-free per-session TO context |
| comp-find -i m365 | infra/aws/terraform/opal-gateway | 71 hits / 25 files | the S2 edit list (3 pages); + var.name usage census |
| comp-iam service | m365-otp-liveness, m365-ms-ingest-liveness | 3 UNRESOLVABLE-RESOURCE each | floor only (sns/ses/secretsmanager resource-unmodeled); grounded on simulate-principal-policy per Rule 22a |
| comp-blast | m365-mcp-gateway | AMBIGUOUS-SUBJECT refusal (correct) -> ALB arn | downstream alb-sg; upstream = route53 mcp record -> confirmed auto-repoint model |
| aws iam simulate-principal-policy | opal-gateway-role x6 | 5 allowed / 1 implicitDeny (negative control) | ONE --resource-arns per call, controls separate |
| proof-of-spec-check | PROOF_OF_SPEC_OPAL_GWRENAME_TO-1 | VALID 12 rows 0 violations | |

**What worked:** comp-blast's refusal on an ambiguous name was the right behaviour; comp-find paged census
built the S2 edit list exactly. **What failed / gap:** comp-iam cannot see resource-level grants (known);
NO comp-tool models Terraform replacement ORDERING -- the SG deadlock class is invisible to plan and to
every comp-tool tonight (gate candidate: lint aws_security_group without create_before_destroy in a module
carrying a persistent aws_instance). comp-pipescript/comp-validate N/A (no data pipeline touched).

## Banked follow-ups (surfaced, NOT chased -- owners to route)

1. BARE `jq` in `infra/aws/ec2/safe-ec2-deploy.sh` + `deploy-to-ec2.sh` (Rule 16 dangerous absentee; masks as "Service not found").
2. t4g.nano undersized for on-box venv builds -- cost the SSM control plane ~10 min (Rule 5 spirit); no SSM-agent restart guard.
3. Wrapper false-negative layer #2 (ACTIVATING rc=3) -- fixed in-script; candidate for the EC2 deploy standard.
4. requirements.txt: other unpinned deps carry the mcp-2.0.0 class of risk.
5. Cleanup rulings needed: old TF state key + backup (2 objects), on-box `/home/ec2-user/.token_cache.pre-s6`, 36 history blobs.
6. user_data /opt literal: needs Andrew's stop/start word; TRIP-CONDITION on any instance replacement; Entra-CA egress-IP check FIRST.
7. Lambda SOURCE dirs `infra/aws/lambda/m365-*` (repo homes, P0-class).
8. Stray `org` dir inside my inbox top-level (wrong-cwd artifact).
9. MSTR's named class: five "enumerate-some-members" gaps in one runbook (SG CBD, artifact filename, unit-file literals, step 9, on-box state) -- worth a runbook-authoring checklist item: "what STATE lives on the box?"

## Files modified (this session, my author line)
infra/aws/terraform/opal-gateway/{main,alb,secrets,secrets-iam,otp-liveness,ms-ingest,waf,dns,audit-lake,taxsma_gateway_iam,otp-alert-sqs}.tf ·
infra/aws/ec2/opal-gateway/{deploy-to-ec2.sh,requirements.txt,deploy/opal-gateway.service} · infra/aws/ec2/EC2_MANIFEST.json ·
org/critical_paths/change_management/20260815T0230Z_opal-gwrename-s3-cutover_deploy_completion.md ·
org/tier2_senior/0.7.0_AE_CloudOps/deliverables/PROOF_OF_SPEC_OPAL_GWRENAME_TO-1_20260815.json · this log · TO-1 status flip.
