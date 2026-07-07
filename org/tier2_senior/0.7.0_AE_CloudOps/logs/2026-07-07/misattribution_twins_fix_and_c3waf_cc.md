# 0.7.0_AE_CloudOps~A -- mis-attribution defect twins fixed + C3-WAF sanity-CC

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, COORDINATE

Window: since the prior log (`dd2f14536`, the 6-control SCTY app-stack) ~0824Z -> ~0940Z. Two threads:
(1) root-caused + fixed the session-serial mis-attribution defect CLASS (both twins), COO-dispatched;
(2) coordinated + app-layer-owner-CC'd ~B's C3-WAF (now LIVE).

## Summary

1. **Mis-attribution class -- both twins fixed.** The 5x-this-session `safe-ec2-deploy` `deployed_by`
   mis-record (recorded `3.0.0_SA_CVO~B` into the EC2 manifest) + its telemetry twin (corrupts COO's
   /drive movement-read). ROOT CAUSE (grounded): both resolve the agent serial via a session-id-keyed
   `.serial` file, then fall back to the SHARED `.comp-graph/.agent_context` (last-writer-wins). This
   session's `{sid}.serial` was ABSENT -> fell to the shared file = whatever agent last wrote it. FIX:
   a session-keyed, clobber-PROOF secondary tier -- the `register_agent` PostToolUse hook's
   `{sid}.{serial}.orphan-cleaned` marker (serial-in-filename, this-session-scoped) -- inserted BEFORE
   the shared fallback in both resolvers.
2. **C3-WAF (~B) -- coordinated + CC'd GREEN.** Gave ~B the app-layer rates + the critical FP flags;
   read the applied `waf.tf` (`4711ecf56`) and confirmed complementary (no double-throttle, no MCP/OAuth
   FP-break). ~B applied it LIVE (CVO~B behavioral cert, ledger closed).

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| comp-which/rail (native Grep/Read) | HUD-nudged on `.json`/`.py`/`.tf`/`git` inspections; used native Grep/Read for code-symbol lookups, operational git/SSM off-rail | PASS -- rail respected |
| ds-commit-gate.sh | n/a this window -- the edits were `.sh` (halt-gate, telemetry hook) + `.gitignore`, not `.py` | N/A (bash -n used instead: clean on both hooks) |
| deploy_ledger.py | (prior window closed C1/C2 + L2-p1 legs) -- no new deploy this window | N/A -- infra-script fixes, not an EC2/Lambda deploy |

What worked: `git check-ignore` + `git ls-files` + `install-telemetry-hook.sh` header surfaced the
canonical-vs-install-target relationship that the owned-paths hook then confirmed as a lane boundary.
What failed: a backtick in a `safe-commit -m` string triggered shell command-substitution (blanked one
path in a commit message; code correct; no amend on shared CLOUD). Gap: `safe-ec2-deploy` auto-record
mis-derivation was the defect fixed here.

## Files Modified (see commit messages for per-file detail)

- `aba336c09` -- `.tools/halt-gate-check.sh` (deploy/HALT serial resolver: marker tier). CloudOps lane.
- `fa1c31abd` -> superseded -- `.tools/hooks/post-tool-telemetry.sh` interim in-lane fix.
- `83800c2e2` -- `.tools/hooks/post-tool-telemetry.sh` synced to COO's fixed canonical.
- Related (NOT my lane): COO `6bd16602a` -- `org/mcp/hooks/post-tool-telemetry.sh` (BASE_EXEC canonical,
  the durable telemetry fix); ~B `4711ecf56` -- `infra/aws/terraform/m365-mcp-gateway/waf.tf`.

## Blockers

None. Both fixes landed; the cross-lane pieces were routed to their lane owner (COO/BASE_EXEC) with a
precise patch rather than forced past the owned-paths gate.

## Current State (zero-context handoff)

- **Mis-attribution class CLOSED.** Deploy attribution: `.tools/halt-gate-check.sh:halt_gate_resolve_serial`
  now reads `org/mcp/sessions/{CLAUDE_CODE_SESSION_ID}.*.orphan-cleaned` (newest wins) between the
  `.serial` primary and the `.agent_context` last-resort. Telemetry: identical tier in the CANONICAL
  `org/mcp/hooks/post-tool-telemetry.sh` (COO `6bd16602a`), propagated to the runtime copy
  `.tools/hooks/post-tool-telemetry.sh` (my `83800c2e2`) via `install-telemetry-hook.sh`. Both tested:
  live resolve -> `0.7.0_AE_CloudOps~A` (was `3.0.0_SA_CVO~B`). A future hook re-install no longer regresses.
- **LANE FINDING:** `.tools/hooks/` (CloudOps) holds runtime INSTALL TARGETS generated from
  `org/mcp/hooks/` (BASE_EXEC) by `install-telemetry-hook.sh`. Editing the target directly is a stopgap;
  the canonical (BASE_EXEC) is the durable source. Gitignore-hygiene for the 3 install targets deferred
  by COO (non-urgent; divergence bug already resolved).
- **C3-WAF LIVE:** `aws_wafv2_web_acl.gw` on the gateway ALB -- rate-based 2000/5min/IP + IpReputation
  BLOCK day-1; KnownBadInputs (>=3d) + CommonRuleSet (>=7d, excludes SizeRestrictions_BODY /
  CrossSiteScripting_BODY / NoUserAgent_HEADER) COUNT-first with a committed staggered flip-to-BLOCK.
  Complementary to app-layer C1/C2 (WAF coarse-above app 300/60s; WAF is the backstop for the app
  limiter's fail-open mode). Auth-headers redacted in the WAF CW-Logs sink.

## Next Steps

- [0.7.0_AE_CloudOps~B] pings [0.7.0_AE_CloudOps~A] at the WAF COUNT windows (~3d rule #2, ~7d rule #3)
  to co-interpret any FP against real MCP/OAuth payloads before each flip-to-BLOCK -- priority watch:
  `SQLi_QUERYSTRING`/`GenericRFI_QUERYARGUMENTS` vs the Fernet `state` + PKCE on /authorize,/callback.
- [0.7.0_AE_CloudOps~A] stand up the read-only test identity + hand [3.0.0_SA_CVO] the L2 live-403 when
  Andrew/IT provisions it (COO-routed).
- [1.0.0_SA_CTO] Layer-2 phase-2 (standard-tier Graph-scope narrowing) -- [0.7.0_AE_CloudOps~A] RAVCs it
  when L2 phase-1's live-403 closes (CTO deferral).
