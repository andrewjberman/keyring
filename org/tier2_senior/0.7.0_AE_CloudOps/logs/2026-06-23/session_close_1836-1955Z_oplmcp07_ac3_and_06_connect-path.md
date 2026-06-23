# Session Log (delta) — 0.7.0_AE_CloudOps~B — OPLMCP.07 AC3 + the .06 connect-path (live own-mail test)

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE, SCRIBE

**Window:** 2026-06-23 ~1836Z -> ~1955Z
**Serial:** 0.7.0_AE_CloudOps~B (OPLMCP lane)

## Summary

Drove OPLMCP.07 AC3 (pipescript gateway named-thread) to authored+verified, and -- triggered by Andrew's
LIVE "check my email via the gateway" -- diagnosed + designed the .06 connect-path (why Claude Code can't
connect to the live gateway), grounded it against the official MCP-auth spec, got CTO Model-B sign-off, and
handed the (security-critical, multi-day) AS build to a fresh-focus lane per the marathon-flag protocol.

## OPLMCP.07 AC3 -- pipescript gateway thread (DONE, committed-by-COO)

- Onboarded the gateway as the `m365-mcp` pipescript named thread: reconciled the STALE `m365-mcp-gateway-ec2`
  census entry (was ops-internal/none/explicit-out, "NOT PROVISIONED scaffold-only" from 06-15) -> in-scope /
  globgrph / producers(EC2+ALB/listener/TG) -> served(mcp.opalinvest.dev/mcp) -> frontend(Claude MCP clients).
- Extended `gen-estate-resolver.py` to read self-contained detail from a manifest entry (backward-compatible;
  for estate threads not in the lambda census). Fixed 3 pre-existing ruff violations (E401/E702/F811). ds-gate clean.
- Verified: `pipescript m365-mcp` resolves with full detail; `--resource m365-mcp-gateway` = 1 thread (no dup);
  `--validate` PASS.
- **owned-paths block (CORRECT):** estate-coverage-manifest/resolver/gen are lane=ANY_EXEC (CVO/CTO-authoritative,
  distinct from `pipescript_cli.py`=AE). I author-by-me / commit-through-exec -> COO committed my 3 verified files.
  (Banked: the AE-lane ruling was for the CLI, not the authoritative manifest DATA.)

## .06 connect-path -- LIVE own-mail test -> diagnosed + designed (DIAGNOSE)

Trigger: Andrew live "i'm andrew@opalinvest.com, let's check my email" via the gateway.
- PREREQ verified (SSM live): gateway requests User.Read+Mail.Read (config default), tenant 6810043e, App-2
  admin-consented, tools whoami + list_recent_email exist -> NO scope gap.
- FINDING (curl SOURCE-CONFIRMED): the ALB authenticate-oidc 302-redirects EVERY listener path to Entra
  (incl /mcp, /.well-known/oauth-*, even /health). Claude Code's MCP client needs 401+WWW-Authenticate +
  200-JSON discovery, gets a 302 -> never starts OAuth -> no popup. Andrew confirmed live: `/mcp` authenticate = no popup.
- GROUNDED Claude Code's hard reqs (claude-code-guide, official MCP-auth spec + cited GH issues #2527/#26675/
  #29934/#10439): DCR (RFC 7591) ALWAYS attempted + Entra has none + static client_id ignored; redirect hardcoded
  `http://localhost:PORT/callback` + Entra rejects HTTP. => Entra CANNOT be the direct AS Claude Code talks to.
- DESIGN = Model-B (CTO SIGNED OFF, PRD Addendum B): the GATEWAY is a full OAuth-AS facade (serve /.well-known x2 +
  /register[DCR] + /authorize + /token + PKCE; /authorize bridges to Entra via App-1/App-2 for the real login;
  gateway issues+validates its OWN token on /mcp; ALB path-rule forwards /mcp+/.well-known WITHOUT authenticate-oidc).
- CTO condition-2 (make-or-break) CONFIRMED source-grounded (token_broker.py): the per-user Graph relay already
  holds delegated access+refresh tokens via the App-2 auth-code flow (redeem_code + acquire_token_silent). Model-B's
  /authorize REUSES that auth-code flow -> NO OBO. .06 delivers "reads his mail" e2e, in-.06-scope.
- ENTRA-ASK = ZERO new config (Model-B: Claude Code registers with the GATEWAY; reuse App-1/App-2 + existing redirects).
- MARATHON-FLAG INVOKED + ACCEPTED (CTO+COO): the AS core (DCR/authorize/token/PKCE/Entra-bridge/issue+validate) is
  multi-day + THE security-critical auth entry-point -> build FRESH-FOCUS, not at session-tail (re-opened auth boundary
  >> handoff cost). Running-start brief committed (oplmcp06_connect-path_build_brief.md, 3e5912521); COO spawning a
  fresh ~C lane to build off it; I'm the gateway backstop. No interim (Andrew: "do it right").

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| pipescript --list / m365-mcp / --resource / --validate | m365-mcp-gateway | PASS | thread resolves w/ detail; 1 thread (reconciled, no dup); --validate PASS |
| comp-aws classes | (model) | INFO | confirmed aws_lb/listener/TG/route53 NOT modeled = AC2 scope (base-AE's lane) |
| ds-commit-gate | gen-estate-resolver.py | PASS | Rule-14 clean after fixing 3 pre-existing ruff violations |

**What worked:** pipescript resolved the onboarded thread cleanly; the curl grounding + claude-code-guide pinned the
.06 mechanism exactly (302-not-401, DCR/redirect walls). **What failed:** n/a. **Gap found:** comp-aws lacks the
ALB-stack classes (AC2, base-AE). Gateway-auth grounding used raw curl/SSM (operational deploy-verify of own infra,
F5) + source-reads (token_broker/identity/server) -- no comp-tool models the gateway's MCP-OAuth (off-graph, correct).

## Current State / Next Steps

- .02 backend GO-LIVE = DONE+accepted. .07 AC1 (comp-iam) + AC3 (pipescript) = DONE; AC2 (comp-aws 4 ALB classes) =
  base-AE in parallel. .06 connect-path = designed (Model-B, CTO-signed) + handed to a fresh ~C lane (brief 3e5912521).
- **[fresh ~C / COO-allocated]** build the .06 gateway OAuth-AS off the brief (coupled single deploy: gateway AS-code +
  ALB path-rule via safe-apply + deploy-ledger; CVO re-verifies unauth/mcp=401 + valid-Bearer=tools; Andrew re-connects).
- **[3.0.0_SA_CVO]** AC2 go-live cert: one-pass plan locked; pings me when synthetic mailboxes + AC5-go land -> I stand
  up the authed session (note: the live MCP-client path is .06-gated; AC2 own-mail real-user proof now waits on .06).
- **[0.7.0_AE_CloudOps~B]** gateway backstop for the ~C .06 build; charmap fix (safe-ec2-deploy) filed-after.

## MCP traffic

~30 messages (heavy live coordination). Significant: COO LIVE own-mail dispatch (Andrew); channel de-conflict (Andrew
in my terminal -> I lead gateway-decode, COO coordinates); CTO Model-B design-GO + 3 conditions -> SIGNED OFF (Addendum B);
COO+CTO marathon-flag ACCEPTED -> fresh ~C lane; my RAVCs (scope/ETA, condition-answers, handoff-brief, Entra-ask=zero).
