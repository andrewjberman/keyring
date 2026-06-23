# Session Log (delta) — 0.7.0_AE_CloudOps~B — OPLMCP.07 AC1 + CVO AC2/3/4 prep

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, DIAGNOSE

**Window:** 2026-06-23 ~1806Z -> ~1836Z (delta since the go-live session-close log)
**Serial:** 0.7.0_AE_CloudOps~B (OPLMCP lane)

## Summary

Post-go-live: (1) supported CVO's AC2/AC3/AC4 cert prep with the source-grounded authed-session
mechanism; (2) drove OPLMCP.07 (graph-onboarding) AC1 to DONE in-lane, and surfaced 2 real
AC2/AC3 scope discoveries for a COO call.

## CVO AC2/3/4 prep (COORDINATE)

Source-grounded (app/identity.py, server.py, blocklist.py, audit.py) the authed-session
mechanism for CVO's cert. Straight answer: AC3/AC4 LIVE proofs need a valid ALB identity (real
Entra user) and FOLD INTO the AC2 window -- alb_oidc signature-verifies x-amzn-oidc-data,
GuardMiddleware checks identity (401) BEFORE kill-switch/blocklist (403), audit fires per
tool-call. Gave CVO the exact SSM-trippable knobs (/opt/m365-mcp-gateway/{KILL_SWITCH,
blocklist.txt, audit.jsonl}, hot-reload, no-SSH). Confirmed live IDENTITY_PROVIDER=alb_oidc +
MOCK_GRAPH=0 (SSM) -> closed CVO's per-user-scope bypass-guard line. One-pass plan LOCKED
(I playwright the OIDC login + operate SSM knobs; CVO owns the verdict) -- waiting on synthetic
test users (A+B) + AC5-go (Andrew/IT; CTO surfacing).

## OPLMCP.07 AC1 -- DONE (IMPLEMENT)

The STEP-A comp-iam coverage-gap (comp-iam "No service matching m365-mcp-gateway"). Two root
causes found + fixed in-lane (COO/Andrew: extract_iam.py = 0.7.0/AE-owned):
- **33ed9e50e** (EC2_MANIFEST.json): added `iam_role: m365-mcp-gateway-role`. _load_ec2_profiles
  SKIPS any manifest service with no iam_role; OPLMCP.03 shipped the entry SSM-core-only. ->
  `comp-iam service m365-mcp-gateway` RESOLVES.
- **2770ab733** (extract_iam.py): _parse_terraform_iam keyed roles by the LITERAL `name="..."`,
  so `${var.name}-role` never matched. Added same-module `${var.X}`->variable-default resolution
  (_collect_module_var_defaults + _resolve_tf_vars; module-scoped to avoid cross-module var
  collisions). -> `m365-mcp-gateway-role` resolves with all 3 statements: gw_golive (s3:GetObject
  prefix + secretsmanager:GetSecretValue) + SSM-core (12 actions).
- Blast radius = gateway only (0 `${var`-literal roles remain). comp-iam-gaps regression CLEAN
  (0 missing / 0 coverage-unknown). ds-commit-gate clean. **The manual-IAM/rail-checked path for
  the gateway IAM is RETIRED.** AC1 acceptance met + verified.

## OPLMCP.07 AC2/AC3 -- scope discoveries (DIAGNOSE; RAVC'd COO)

- **AC2 (comp-aws):** derives live(boto3)+TF by resource CLASS. The gateway EC2/IAM/SG/3-secrets
  ARE modeled classes (auto-derive on next globgrph derive). BUT comp-aws has NO class for
  aws_lb / aws_lb_listener / aws_lb_target_group / aws_route53_record -> the ALB/TG/listener/R53
  need 4 NEW live-derive functions + TF mappings + edges (substantial derive-engine extension).
  RAVC'd COO: add the 4 classes in .07, or scope to the modeled subset + a separate ALB-class TO?
- **AC3 (pipescript):** gateway is NOT a named thread (33 exist, none for mcp/oplmcp). Needs a
  new thread entry; pipescript_cli.py = DS-lane per the manifest (vs COO "in-lane") -> ownership
  confirm RAVC'd.

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| comp-iam service/role/roles/gaps | m365-mcp-gateway | PASS | service+role resolve post-fix; gaps regression 0 missing/0 coverage-unknown (clean) |
| comp-aws classes | (model) | INFO | confirmed aws_lb/listener/TG/route53 NOT modeled classes -> AC2 scope finding |
| pipescript --list / lookup | m365-mcp-gateway | INFO | not a named thread (33 exist) -> AC3 finding |
| ds-commit-gate | extract_iam.py | PASS | Rule-14 (py_compile+AST+ruff) clean |

**What worked:** comp-iam resolved the gateway after both fixes; the gaps regression confirmed
no FP introduced. **What failed:** n/a. **Gap found:** comp-aws lacks the ALB-stack resource
classes (AC2 scope); pipescript gateway thread missing (AC3) -- both RAVC'd for a scope/ownership call.

## Current State / Next Steps

- OPLMCP.07 AC1 DONE (pushed 2770ab733). AC2/AC3 gated on the **[2.0.0_SA_COO]** scope+ownership
  call (4-class comp-aws extension vs follow-on; pipescript lane).
- **[3.0.0_SA_CVO]** AC2/3/4 cert: one-pass plan locked; pings me when synthetic users + AC5-go
  land -> I stand up the authed session (playwright OIDC) + operate SSM knobs.
- **[0.7.0_AE_CloudOps~B]** charmap fix (safe-ec2-deploy.sh) filed-after per CTO. Standing by.

## MCP traffic

~14 messages. Significant: CTO GO (OPLMCP.07 now; charmap=scoped-after; AC2=stand-by); COO .07
routing + Andrew-direct correction (extract_iam=AE, all .07 in-lane); CVO one-pass-plan-locked +
IDENTITY_PROVIDER-banked; my RAVC2s (AC1-done + AC2/AC3 scope).
