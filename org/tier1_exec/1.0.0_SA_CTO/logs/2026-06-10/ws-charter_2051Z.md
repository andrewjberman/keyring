# ws-charter cycle — 2026-06-10 2051Z — 1.0.0_SA_CTO

**CLASS:** NOVEL (Andrew-direct authority via CVO relay)
**Commit:** ac3d90482

## Trigger
Inbox Monitor (bymhu8c4x) fired at 204703Z: 3.0.0_SA_CVO `[NEW MACRO] Please create NFRA_OPLMCP` — relaying an Andrew-direct ask to stand up a managing macro-project for the Opal M365 MCP property built+validated in the CVO Andrew-direct session. NOVEL gate satisfied (Andrew direction present, relayed by CVO; CVO explicitly leaves macro JSON/PRD authoring to CTO). HARD-BLOCK #7 (new project code) override path = NOVEL itself.

## Inbox classification
- 204703Z CVO `[NEW MACRO]` → ANDREW_DIRECTION → NOVEL authoring path (this tick).
- (startup read-dir) 174819Z DS RAVC2 Schwab ruling → already discharged (APPROVED 174930Z prior session).
- (startup read-dir) 174904Z MSTR CHARTERED hook → informational; future AC-review gated on AE post-NFRA pickup.

## Action
Authored the macro:
- `org/projects/NFRA_OPLMCP.json` — macro JSON (status active, P0, pods 1.0/0.7/3.0).
- `docs/architecture/NFRA_OPLMCP_PRD.md` — formal PRD: architecture decisions 1-7, in-repo ruling (sec.3), validation status (sec.4), sub-streams OPLMCP.01-.06 (sec.5), security+data-governance (sec.6), NFRA accounting (sec.7), AC1-6 closeout bar (sec.8).
- `org/projects/REGISTRY.md` — Active Projects row.

## CTO rulings (the two open decisions)
1. **In-repo vs separate property → IN-REPO** under NFRA_OPLMCP governance. Target: gateway `infra/aws/ec2/m365-mcp-gateway/`, Terraform `infra/aws/terraform/`, Lokka kit `.tools/m365-mcp-kit/`. Rationale: AWS infra (nano EC2 + ALB+OIDC + Secrets Manager) is bound by CLAUDE.md Rules 7-12; audit→lake governance is the repo's strength. Actual move = sub-stream OPLMCP.01.
2. **Data-egress governance → hard AC.** M365 content → Anthropic API gated by Claude for Work/Enterprise terms: lifted to AC5 (sign-off recorded before any non-Andrew onboarding) + dedicated sec.6. Per-user-delegated-identity = stop-the-line security boundary. AC2 requires live per-user-scope proof. Infra-alone explicitly NOT close.

## Dispatch
- → 3.0.0_SA_CVO (205101Z): macro stood up; verify pass welcome, natural target = OPLMCP.02 first live /me+/outlook (per-user scope + kill-switch + audit) post-IT.
- → 2.0.0_SA_COO (205110Z): decompose OPLMCP.01-.06 sequenced behind live NFRA queue (LD-0177); OPLMCP.01 + .03-scaffold parallelizable now, only .02 hard-gated on IT.
- → 0.0.0_AB_MSTR (205117Z): NOVEL authority-chain FYI; no MSTR action needed.

## Follow-on / next-cycle expected state
- Only external gate = Andrew/IT provisioning 2 Entra app registrations (5 values). Everything else in-fabric.
- CTO future obligation: review AE infra against PRD AC1-6 before any go-live; own OPLMCP.05 data-terms sign-off (hard close-gate).
- CVO owns downstream cert.
