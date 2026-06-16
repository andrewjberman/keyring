# OPLMCP ~B: .01 repo re-sync + .03 Terraform skeleton -> CLOSED-503 (live-verified)

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, COORDINATE

**Agent:** 0.7.0_AE_CloudOps~B (2nd AE lane, spawned by CTO 142452Z for OPLMCP .01/.03; parallel to base-lane GCONTR)
**Date:** 2026-06-16
**Window:** session start (~14:36Z) -> 15:41Z

## Summary

Stood up the M365 MCP gateway (NFRA_OPLMCP) per PRD §10. Two sub-streams, both shipped:
- **OPLMCP.01** in-repo RE-SYNC of the iterated Desktop gateway (the original migration landed 8b0e7d241).
- **OPLMCP.03** Terraform infra skeleton APPLIED to a CLOSED-503 state and live-verified.

The EC2 code-deploy + its IAM were correctly deferred to .02 (a real §10.3-vs-§10.6 IAM-scope inconsistency I surfaced rather than unilaterally widening) -- CTO + COO both endorsed.

## What I did

### OPLMCP.01 - repo re-sync (COMPLETE)
- Ground-truthed Desktop (`C:\Users\AndrewBerman\Desktop\m365-mcp-gateway`) vs in-repo (`infra/aws/ec2/m365-mcp-gateway/`). Of 5 drifted files, only **IT_REQUEST.md + README.md** were genuine Desktop iterations; **config.py / identity.py / make_diagram.py** drift was migration-time `ruff format` + F401 (identity.py's `time`/`Optional` verified unused in both) -> kept the repo's lint-clean forms, did NOT regress.
- Fixed `deploy/m365-mcp-gateway.service` bind `--host 127.0.0.1 -> 0.0.0.0` (§10.5); on post-commit verify caught + fixed a stale tunnel comment + a non-ASCII em-dash in that AWS-running file (§10.1).
- **Health-check (§10.3-4) resolved with NO app change**: `app/server.py` already has `Route("/health")` -> `JSONResponse({"ok":True})` (200), and `GuardMiddleware` guards only `_GUARDED_PREFIXES=("/mcp","/login")`, so `/health` is reachable unauthenticated by the ALB health check. CTO-confirmed.
- CTO revised the Desktop docs AGAIN after my first sync (IT_REQUEST -> full-envelope scopes; README -> single-source) -> re-pulled both. Kit (`.tools/m365-mcp-kit`) byte-identical (no-op). EC2_MANIFEST entry present.

### OPLMCP.03 - TF skeleton -> CLOSED-503 (COMPLETE)
- Re-targeted the superseded tunnel stub into the locked ALB+OIDC model. Authored `main.tf` (re-targeted EC2/IAM/SG + S3 backend + default_tags) + `alb.tf` (SGs, ALB, TG, HTTPS listener default=fixed-response 503, HTTP->443 redirect) + `dns.tf` (Route53 ALIAS) + `outputs.tf`. SG cycle avoided via alb-egress-to-VPC-CIDR (data.aws_vpc) rather than a cyclic gw-SG ref.
- **Independently live-re-verified** every §10.2 input (not just CTO census): VPC `vpc-0cc0c6a75e54605e3` (172.31.0.0/16), ALB subnets `subnet-039d04cfaee66a5f6`(1a)+`subnet-0febae1196d1873e5`(1b) both public/distinct-AZ, cert `cf2d3e43...` ISSUED with SAN `*.opalinvest.dev`, zone `Z054626637UVVD9T5GO6` public + NO existing `mcp.*` record. Greenfield: 0 ALB/TG/SG/instance/role collision.
- `terraform validate` OK; plan = **12 add / 0 change / 0 destroy**. Committed before apply (Rule 2).
- JOINT GATE: CTO GO (architecture/AC1/§10, 145222Z) + COO operational concurrence (152858Z). Then AE-autonomous `safe-apply` (no Andrew gate -- recoverable).
- Opened deploy-completion ledger -> `safe-apply` (HALTGT passed) the saved `tfplan` -> **Apply complete: 12 added** -> closed all 5 legs -> ledger CLOSED.

## Deployment Sequence + Verification (AE)

```
1. deploy_ledger.py open  oplmcp03-closed503 (5 legs)         [apply-start]
2. safe-apply.sh -chdir=...m365-mcp-gateway apply tfplan      Apply complete! Resources: 12 added, 0 changed, 0 destroyed.
3. terraform plan -detailed-exitcode                          No changes. (exit 0)  [L3]
4. curl https://mcp.opalinvest.dev                            HTTP=503  TLS_verify=0  body="M365 MCP gateway - OIDC auth not yet configured"  [L4]
   nslookup mcp.opalinvest.dev                                -> 54.175.54.94 (ALB)
5. aws elbv2 describe-listeners                               DefaultAction=fixed-response/503, SSL=TLS13-1-2-2021-06, cert cf2d3e43
   aws iam list-attached-role-policies/list-role-policies     AmazonSSMManagedInstanceCore ONLY, 0 inline   [F5 authoritative]
   aws elbv2 describe-target-health                           i-01d75...:8080 = unused/NotInUse (correct -- no listener forward yet)
6. EC2_MANIFEST _status -> PROVISIONED (commit adadd5499)
7. git tag -a m365-mcp-gateway-v1.0.0 + push --follow-tags
8. deploy_ledger.py close oplmcp03-closed503                  all 5 legs proven; CLOSED
```

## Live AWS resources (handoff)

| Resource | ID |
|---|---|
| ALB | `arn:...loadbalancer/app/m365-mcp-gateway/62a54b61dc4634dd` (dns `m365-mcp-gateway-1854602644.us-east-1.elb.amazonaws.com`) |
| HTTPS listener (.02 swap target) | `arn:...listener/.../4751a29f69442c23` |
| Target group | `arn:...targetgroup/m365-mcp-gateway-tg/4e86dec91ed511dd` |
| Nano EC2 | `i-01d75141177c88b96` (t4g.nano, SSM-idle, SSM-core IAM only) |
| Gateway SG | `sg-0897ab38bfe095dfd` |
| Route53 ALIAS | `mcp.opalinvest.dev` -> ALB (zone `Z054626637UVVD9T5GO6`) |
| IAM role | `m365-mcp-gateway-role` (AmazonSSMManagedInstanceCore only) |

## MCP traffic

~15 messages handled. Significant: CTO joint-gate GO (145222Z) + endorse-defer (145904Z); COO operational concurrence (152858Z, re-sent to ~B 153438Z); CVO globgrph Item-2b thread (acked + routed, then CVO-retracted -- P1s already fixed 8d1ca4ea9/deployed 06-15, NOT my lane, never context-switched). RAVC2 OPLMCP.03 COMPLETE sent COO+CTO (154056Z/154105Z).

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| `comp-kuzu` | greenfield m365 node check | PASS | 0 m365 nodes (expected); graph CURRENT (nightly derive committed 02:02:25Z) |
| `comp-blast m365-mcp-gateway` | post-.01 | PASS | no nodes / bounded (greenfield) |
| `comp-iam gaps` | after iam.tf | PASS | 0 missing among modeled services |
| `comp-iam service m365-mcp-gateway` | pre + post apply | PARTIAL | index-blind to the not-yet-derived service ("No service matching"); live `aws iam` authoritative per F5 (SSM-core only, 0 inline) |
| `comp-surface-check` | rode safe-commit | PASS | every commit: no critical surface touched |

**What worked:** comp-kuzu's provenance header confirmed graph currency (and incidentally that the CVO globgrph nightly self-heal ran). Live `aws iam`/`elbv2 describe` were the authoritative fence checks (F5 -- verify own change against live AWS, never the graph).
**What failed:** nothing blocking.
**Gap found:** `comp-iam service` / `comp-blast` / `comp-kuzu` are all **greenfield-blind to a freshly-deployed service** -- the m365 node only materializes after a `comp-aws derive` run picks up the live EC2/ALB/role. There is no "register a just-deployed service into the comp graph immediately" path short of a derive; for a fresh deploy, live-AWS describe is the only ground truth at apply-time. Expected behavior, recorded for awareness (the node will appear at the next nightly derive).

## Files Modified

See commit messages: `66a9a353b` `a2fe54360` `0c767fa8c` (.01 re-sync: IT_REQUEST/README/.service), `3cc05e1a1` (.03 main/alb/dns/outputs.tf + lock), `fbd5116c7` (.02-prep: deploy-to-ec2.sh + EC2_MANIFEST deploy_script/_status), `adadd5499` (EC2_MANIFEST -> PROVISIONED). Tag `m365-mcp-gateway-v1.0.0`. Ledger `org/critical_paths/change_management/20260616T1530Z_oplmcp03-closed503_deploy_completion.md`.

## Blockers

None. The CTO+COO joint gate on the apply was a normal review gate (cleared 152858Z), not a block. .02 is IT-gated (Andrew issuing the finalized IT_REQUEST) -- a planned external dependency, not a blocker on me.

## Current State

NFRA_OPLMCP .01 + .03 COMPLETE. The M365 MCP gateway public endpoint `https://mcp.opalinvest.dev` is LIVE and returns a 503 fixed-response over a valid wildcard-cert TLS connection -- the CLOSED-503 state. All infra (ALB + listener + TG + EC2 + 2 SGs + Route53 ALIAS) exists; the nano EC2 is SSM-idle with SSM-core IAM only; the listener does NOT forward (fixed-response) and carries NO authenticate-oidc -- the gateway is never exposed unauthenticated. NFRA cost ~$20-26/mo (ALB-dominated), registered in the RAVC2. comp graph node materializes at the next comp-aws derive.

## Next Steps

- **[OPLMCP.02 -- AE + Andrew/IT, IT-gated]** One coherent go-live leg: scoped `s3:GetObject` (artifact prefix) + secrets-read IAM, `MOCK_GRAPH=0`, gateway code-deploy (`deploy-to-ec2.sh` already STAGED at `fbd5116c7`, S3->SSM), `verify-ec2.sh` parity, the `authenticate-oidc` listener default-action swap (swap target = `https_listener_arn ...4751a29f69442c23`), and update `app/config.py` + `.env.example` GRAPH_SCOPES from the read-only set to the consented FULL ENVELOPE (PRD §11). Unblocks on Andrew's IT app-reg send + reply.
- **[Post-v1 hardening -- banked]** alb-SG egress tighten to the gw-SG via a separate `aws_security_group_rule` (CTO note-1); §10.9 private-subnet + NAT to drop the public IP; Verified-Access JWT signature-verify (the PRD pre-prod TODO).
- **[0.7.0_AE_CloudOps base lane]** GCONTR TO-2 continues independently (separate lane).
