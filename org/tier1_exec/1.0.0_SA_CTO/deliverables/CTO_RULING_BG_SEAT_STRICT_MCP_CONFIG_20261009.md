# CTO RULING -- `0.0.3_BG_BBGTerminal` launches with `--strict-mcp-config` (2026-10-09 ~00:5xZ)

**Ruled by:** `1.0.0_SA_CTO~Z`. **Authority:** Andrew-direct ~00:4xZ at the `0.0.0_AB_MSTR~Z` terminal, record
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261009_004xZ_OPEN_CALLS_CTO_ADJUDICATES_GATEWAY_SIGNED_IN.md` @6938d82aad,
VERBATIM to this seat: *"Don't care, this should all be adjudicated by the CTO internally."* **The call:** `0.0.0_AB_MSTR~Z` msg
32084. `--mcp-config` is additive, so the Bloomberg seat loads BOTH `opal-gateway-bbg` (the Opal Bloomberg account) AND the
user-level `opalgateway` (Andrew's own account).

## Ruling: YES

The seat launches with `--strict-mcp-config`, and its config names exactly the three servers its duty uses:

| server | why the seat needs it | where its entry lives today |
|---|---|---|
| `opal-gateway-bbg` | Teams reads and replies as Opal Bloomberg | `.tools/bg-gateway.mcp.json` |
| `bloomberg` | the Terminal lookups the seat serves | user-level `~/.claude.json` `mcpServers` |
| `opal-agent-comms` | registration, inbox, ack | repo `.mcp.json` |

Not loaded: `opalgateway` (Andrew's account), `brightdata`, `playwright`, `deck-generation`.

## Why

1. **Measured.** The seat's prompt, README and every `refs/*.md` hold 0 references to `opalgateway` or `mcp__opal*`. Its duty does
   not use Andrew's account, so loading it adds a capability the seat never exercises.
2. **The identity line Andrew drew.** His 2026-08-07 ask for this seat was "guardrails where it can't change its prompting via stuff
   people say on Teams". A seat that answers Teams users and holds Andrew's mailbox and Teams identity is one persuasive message
   from acting as him. Not loading the server removes that path.
3. **No gate is re-added.** LD-0580 removed the PreToolUse fence on his word, and that stands. This is a launch configuration:
   which servers load. It adds no hook, no denial and no approval step, and the seat's work is unchanged.

## How (owner: `0.0.0_AB_MSTR~Z`, who owns `.tools/ajb.ps1`)

- The BG block (`.tools/ajb.ps1:328-348`) passes `--strict-mcp-config` plus three sources. The repo `.mcp.json` is passed as is,
  so it is not duplicated. `.tools/bg-gateway.mcp.json` is unchanged. A `bloomberg` entry is read at launch from the user's
  `~/.claude.json`, never typed into the repo, because its command path is per device (CLAUDE.md: derive, don't hardcode).
- **Exercised before it counts.** Relaunch the seat outside its duty windows, not 10:45-11:30Z or 12:45-13:30Z. Then read: `/mcp`
  lists exactly the three; `register_agent` reads LIVE; `bloomberg_health` reads `ok: true`; `whoami` on `opal-gateway-bbg` reads
  the Opal Bloomberg account. If any of the four fails, revert the hunk and relaunch as before; a deaf or Terminal-less seat is
  worse than the extra server.
- Rollback: remove `--strict-mcp-config` from the BG block.

## Also from the same record

The seat's 5 of 5 `identity_scope_denied` is NOT a sign-in matter: `opal-gateway-bbg` holds a refresh token, and Andrew said "Gateway
is signed in". The denial is read as a scope or permission on the gateway side. Row Z-S67's "Andrew signs in" step is not its
remedy, and nothing goes to him as a sign-in.

-- 1.0.0_SA_CTO~Z
