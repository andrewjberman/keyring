# Deploy-completion ledger — gateway server rename `m365-gateway` -> `opal-gateway`

**Opened:** 2026-07-31 ~01:45Z (at deploy-start, per CLAUDE.md NEVER#6)
**Owner:** `0.7.0_AE_CloudOps~Z` (site Z) · **Service:** `m365-mcp-gateway`, instance `i-07dccb1615503ac99`
**Code commit:** `042f96d44` (committed + pushed BEFORE deploy, Deployment Rule 2)
**Deploy path:** `infra/aws/ec2/safe-ec2-deploy.sh m365-mcp-gateway infra/aws/ec2/m365-mcp-gateway/deploy-to-ec2.sh` (Rule 7 — never the service script directly)

**Authorization:** Andrew-direct, relayed by `0.0.0_AB_MSTR~Z` `20260731T014056Z`, VERBATIM:
> *"just sort out the gateway split, i dont care i can reinstall it on alyssas computer or give her
> instruction to reauthenticate or whatever"*

Discharges the hold I placed at `20260730T223838Z`. The hold was correct and is retired by the
sovereign, not by peer override.

## What this deploy DOES and DOES NOT do — stated because the premise moved twice

- **DOES:** change `serverInfo.name` in the MCP handshake from `m365-gateway` to `opal-gateway`,
  and ship an 18-line comment at `tools.py:37` recording the measured key-vs-name fact.
- **DOES NOT:** change any client-visible tool name. **The `mcp__<prefix>__` segment comes from the
  client's REGISTRATION KEY, not this string** — measured 3/3 (`m365`→`mcp__m365__`,
  `opal-agent-comms`→`mcp__opal-agent-comms__*` with hyphens intact, `playwright`→`mcp__playwright__*`).
  Bloomberg would still land as `mcp__m365__*` after this ships.
- **The comment is the durable half.** The misleading string is what produced the wrong section-3
  premise; deleting it silently would leave the trap for the next reader.

## Pre-deploy checks (measured, not assumed)

| Check | Result |
|---|---|
| Drift between `deployed_commit` `c390d1c6a` (2026-07-15) and HEAD, scoped to the gateway tree | **Exactly ONE commit: `042f96d44`, 1 file, +18/-1.** No hitchhiking changes — the deploy ships only the intended change |
| `commit-gate.sh` on `tools.py` | PASS |
| Live traffic on this endpoint | **Real and current** — 55,878 audit records; andrew 54,976 (through today), alyssa 895 (through today). Deploying a live OAuth endpoint, not an idle one |
| Deploy window | ~01:45Z, lowest-traffic window of the day |

## Legs

| # | Leg | Status |
|---|---|---|
| 1 | ledger opened at deploy-start | **DONE** |
| 2 | code committed + pushed before deploy (`042f96d44`) | **DONE** |
| 3 | drift check — only the intended commit in range | **DONE** |
| 4 | deploy via `safe-ec2-deploy.sh` (Rule 7) | PENDING |
| 5 | **LIVE-PLANE verify** — the RUNNING gateway's `serverInfo.name`, not the deploy script's rc | PENDING |
| 6 | ledger CLOSED in-session | PENDING |

## Rollback

Redeploy the parent commit (`042f96d44^`) via the same wrapper. The change is a single string plus
comments — no schema, no state, no data migration. Nothing to unwind beyond the redeploy.

## NOT in this deploy (split, per MSTR `20260731T014056Z`)

- **Client registration key `m365` -> `opal`** — MSTR owns this device's `~/.claude.json`; Andrew
  owns Alyssa's machine by his own word. Per-device config, not a deploy.
- **`teams-assist/SKILL.md` literals** — MSTR, converting to BARE tool names rather than
  re-hardcoding `mcp__opal__`. Verified support: **zero** permission-allowlist entries encode the
  prefix (`.claude/settings.json`, `settings.local.json`, `~/.claude/settings.json` all 0), so bare
  names carry no hidden dependency. Bare names are also correct in BOTH key states simultaneously,
  which removes the transition ordering constraint rather than managing it.
