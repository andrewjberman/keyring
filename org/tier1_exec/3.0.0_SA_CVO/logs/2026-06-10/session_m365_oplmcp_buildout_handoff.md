# Session — M365 MCP property build-out (Andrew-direct) → handoff to CTO for NFRA_OPLMCP
**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE, COORDINATE
**Author:** 3.0.0_SA_CVO
**Date:** 2026-06-10
**Note:** This was an **Andrew-direct working session** in the CVO Claude Code session — a
design+build collaboration, NOT a CVO validation cycle. Logged at Andrew's instruction and
routed to CTO to spin up a managing macro-project. Artifacts live **outside** the repo (see
paths); a decision for CTO is whether to bring them in-repo.
**UPDATE 2052Z: handoff complete — CTO created NFRA_OPLMCP (ac3d90482); rulings + RAVC
close recorded in "Handoff outcome" below.**

---

## What this was

Andrew is standing up a shared way for Opal employees to reach Microsoft 365 (their own
email, OneDrive, SharePoint, calendar) from Claude. We scoped it from first principles,
then built and validated the front end. Most users are Claude Code (PowerShell); a GUI
path is a later option.

## What was built (artifacts on disk, OUTSIDE the repo)

1. **`C:\Users\AndrewBerman\Desktop\m365-mcp-kit\`** — lightweight **local** option: the
   Lokka (`@merill/lokka`) Graph MCP server + `/outlook` `/onedrive` `/sharepoint` skills +
   a `BOOTSTRAP.md` an agent self-executes to install. For power users / fast start.
2. **`C:\Users\AndrewBerman\Desktop\m365-mcp-gateway\`** — the **primary property**: a
   remote MCP **gateway** (Python, FastMCP Streamable HTTP, stateless) designed to run on a
   nano EC2 behind an access layer. Components:
   - Per-user **delegated OAuth relay** (MSAL confidential client; per-user refresh token,
     Fernet-encrypted at rest) — Graph enforces per-user scope; no app-only/tenant-wide.
   - **13 Graph tools** (mail read/search/draft/send w/ draft-then-confirm, calendar,
     OneDrive, SharePoint).
   - **Guard middleware** (pure ASGI): global `KILL_SWITCH` + hot-reload `blocklist.txt`,
     enforced before any tool runs.
   - **Audit** — every call → `audit.jsonl` (user / tool / redacted args / outcome / ts).
   - **Pluggable identity** providers: `alb_oidc` (default, AWS-native), `verified_access`,
     `cloudflare`, `tailscale`, `header` (dev). AWS-signed identity verified at the gateway.
   - `MOCK_GRAPH` mode (canned Graph) to validate the front end with zero Microsoft setup.
   - `infra/main.tf` (nano EC2 starter), systemd unit, `ACCESS_LAYER.md`, `IT_REQUEST.md`.
3. **`C:\Users\AndrewBerman\Desktop\m365_mcp_architecture.{png,svg}`** — architecture
   diagram for Andrew's IT call.
4. **`~/.claude/skills/draw/SKILL.md`** — a new `/draw` skill memorializing the house ASCII
   diagram style (user scope).

## Architecture decisions (the record)

1. **Delegated per-user OAuth, never application permissions.** "Shared server, NOT shared
   identity." Microsoft enforces each user sees only their own data.
2. **Primary = hosted gateway on a nano EC2 behind an access layer** (kill switch +
   per-user block + central audit). Local Lokka kit retained as the light option.
3. **AWS-native access layer = ALB + OIDC** (no Cloudflare/Tailscale). End users need **no
   AWS IAM** — they auth at the ALB against Entra. Verified Access is the device-aware
   upgrade path; SSM port-forward is a zero-infra option for the Claude Code crowd.
4. **Two Entra app registrations** = the only IT deliverable: App reg 1 "Login" (OIDC,
   wired into the ALB) + App reg 2 "Graph" (delegated scopes, creds held by the EC2).
   Five values back: Tenant ID + 2×(Client ID, Secret); admin consent on both.
5. **Telemetry/analytics explicitly descoped** (the consultant doc's ADX "Option 3" — a
   crazy-oversized cluster). If ever wanted, it's an AWS bronze feed (Lambda→S3→Athena),
   not Azure ADX.
6. **Data-governance flag:** M365 content flows to Anthropic's API — gated by Claude
   for Work/Enterprise terms. Flagged for Security; not an Azure setting.
7. Technical: MCP `streamable_http_path="/"` + `stateless_http=True` + **pure-ASGI**
   middleware (BaseHTTPMiddleware drops contextvars) so identity reaches tools in-task.

## Validation status (front-end leg — device → gateway)

**PROVEN** on Andrew's machine, mock backend, three ways:
- MCP Streamable HTTP transport — Claude Code client (`m365-dev`) shows `✔ Connected`;
  smoke client lists 13 tools and calls them.
- Access-layer identity (simulated header) propagates into every tool + the audit log
  (`user:` populated on each call; bodies redacted).
- Kill switch + blocklist deny; clearing restores. No server errors.

**PENDING (the backend leg — gateway → Graph):** IT provisions the 2 app regs → fill
`TENANT_ID`/`CLIENT_ID`/`CLIENT_SECRET`, flip `MOCK_GRAPH=0`, deploy nano EC2 + ALB+OIDC +
Secrets Manager (Terraform). Verified-Access JWT signature-verify is a marked pre-prod TODO.

## Recommendation to CTO — create NFRA_OPLMCP

Stand up a macro-project **NFRA_OPLMCP** ("Opal M365 MCP") to own + develop this property.
Suggested sub-streams:
- **Backend integration** — IT app-reg intake (5 values), flip mock off, first live `/me`
  + `/outlook` against real Graph.
- **Infra/deploy** — Terraform: nano EC2, ALB + `authenticate-oidc`, Secrets Manager, DNS/ACM.
- **Tool surface** — expand Graph tools/skills; OBO vs gateway-own-login decision.
- **Governance** — Claude-Enterprise data terms sign-off; audit.jsonl → lake (Athena).
- **Rollout** — GUI users later via the same remote MCP (no per-machine install).
- **Decision for CTO:** bring `m365-mcp-gateway` into the repo (under safe-deploy/IAM
  governance) vs. manage as a separate property. It currently sits on the Desktop, ungoverned.

## Handoff outcome (RAVC close)

Sent to CTO 204703Z → CTO created **NFRA_OPLMCP** at commit **ac3d90482** (macro JSON +
100-line PRD + REGISTRY Active row). I **independently verified** the commit + files (not
the summary). Loop closed (ack 205141Z).

CTO rulings (both accepted — they sharpen the handoff):
1. **IN-REPO.** Gateway migrates to `infra/aws/ec2/m365-mcp-gateway/` + Terraform +
   `.tools/m365-mcp-kit/` under Rules 7-12 + Secrets-Manager + audit→lake governance — as
   sub-stream **OPLMCP.01**, not at macro-creation. (Correct: the box holds per-user refresh
   tokens + a client secret; ungoverned-on-Desktop is not acceptable for that.)
2. **AC2 = live per-user-scope PROOF** — a real non-Andrew user reaches their OWN mail and
   demonstrably CANNOT reach another's; **infra-alone is explicitly NOT close.** My
   egress flag was lifted to hard **AC5 + sec.6** (Claude for Work/Enterprise data-terms
   sign-off recorded BEFORE any non-Andrew onboarding; per-user-delegated-identity-as-
   security-boundary written stop-the-line).

Sub-streams (CTO): OPLMCP.01 in-repo migration · .02 backend integration (first live /me +
/outlook) · .03 infra/deploy · .04 tool surface · .05 governance · .06 rollout.

**CVO verify-pass ARMED** (event-driven): first target = OPLMCP.02's first live `/me` +
`/outlook` once IT provisions the 2 app regs — verify (a) AC2 two-user scope proof, (b)
kill-switch + blocklist deny on the live path, (c) audit.jsonl captures real calls. Backend
is IT-gated; no rush.

## Open housekeeping
- Dev gateway server still running in the background on Andrew's machine (`m365-dev`
  registered, user scope). Harmless; shut down on request.
- Parked, unrelated: AE_CloudOps NFRA_GLOBGRPH ITEM-3 traversal-acceptance pairing (no
  urgency) — my CVO verifier pass still owed.

## Compiler Tools
N/A — this property lives **outside** the ajb_workspace repo/comp-graph (Desktop), so the
comp-* tools (which read the repo's compiler graph) have nothing to resolve against. If CTO
brings it in-repo under NFRA_OPLMCP, normal comp-* gating applies thereafter.

— 3.0.0_SA_CVO
