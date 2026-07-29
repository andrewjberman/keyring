# AGENTBUS inter-site trunk — git-transport MVP

**Status:** live-fire MVP, Andrew-authorized 2026-07-28. This is a working prototype of
**NFRA_AGENTBUS Port 2** (the intra-Andrew-device inter-site trunk) that runs over **git**
instead of the designed DynamoDB-table + `m365-mcp-gateway` EC2 MCP tools. It exists so the
two MSTR agents can collaborate cross-device **today**, and to de-risk the real build.
Canonical design: `docs/briefs/AGENTBUS_SCHEMA_SPEC_20260717.md` + `docs/architecture/NFRA_AGENTBUS_PRD.md`.

## Sites (this MVP)

| Site | Serial | Machine |
|---|---|---|
| **Z** | `0.0.0_AB_MSTR~Z` | the MSTR terminal (site Z) |
| **base** | `0.0.0_AB_MSTR` | Andrew's laptop (base) |

Both work out of the same repo on branch **CLOUD**.

## Transport (how it moves)

- **Send** = write one envelope file into `messages/`, `git add` + commit + **push** to `origin/CLOUD`.
- **Receive** = **pull** `origin/CLOUD`, then scan `messages/` for envelopes whose `to` is your serial
  (or `broadcast`) that you have not yet processed.
- It is **asynchronous, store-and-forward** — latency = the pull cadence. Site Z polls ~120s; base
  polls ~2 min (Andrew-set). This is structured email, not a live socket.

## The binding law — ACK IS FIRST-CLASS (schema spec §2, CLAUDE.md Rule 22b)

**SENT IS NOT READ.** A message with `"requires_ack": true` is **UNDELIVERED** until an `ACK`
envelope referencing its `msg_id` lands on the trunk. A git push succeeding is **not** delivery.
An unacked `STOP`/`RULING` past its `ack_deadline` → the sender's MSTR **escalates to Andrew**
(the only mandatory alarm; it fires on ABSENCE). A site's liveness is judged only from its own
emitted messages (DIGEST/ACK), never from git connection state.

## Envelope (every message — mirrors schema spec §3)

```json
{
  "msg_id":       "amb-<site>-<seq>",      // sender-assigned here (no bus); globally unique. Z uses amb-z-*, base uses amb-b-*
  "ts":           "2026-07-29T00:24:24Z",  // sender UTC (bus would assign; here the sender does)
  "from_site":    "Z",
  "from_serial":  "0.0.0_AB_MSTR~Z",
  "to":           "0.0.0_AB_MSTR",         // full serial | "broadcast"
  "kind":         "DIGEST",                // closed enum below; unknown kind = ignore + flag
  "body":         { },                     // per-kind, spec §4
  "refs":         ["<git-sha>", "LD-…"],   // the substance travels in git; the trunk carries pointers + what can't wait
  "requires_ack": true,
  "ack_deadline": "2026-07-29T01:24:24Z",  // required iff requires_ack
  "ttl":          "2026-08-05T00:24:24Z",
  "schema_v":     1
}
```

**Filename convention** (sortable + greppable): `<ts_compact>__<from_serial>__<to_serial>__<kind>__<msg_id>.json`
e.g. `20260729T002424Z__0.0.0_AB_MSTR~Z__0.0.0_AB_MSTR__DIGEST__amb-z-0001.json`.

## Kinds (closed enum — the six from schema spec §4)

`RULING` (verbatim sovereign instruction, `requires_ack` MANDATORY) · `CLAIM` (tree/deploy ownership
ASSERT/RELEASE; a conflicting ASSERT is rejected) · `HANDOFF` (a project crossing the boundary;
all state in `state_refs` git shas) · `DIGEST` (MSTR↔MSTR rollup + liveness; normally `requires_ack:false`)
· `STOP` (cross-site halt, `requires_ack` MANDATORY, shortest deadline; not in force until ACKed) ·
`ACK` (the delivery oracle — `{"acks_msg_id","verdict":"ACK|ACK-WITH-CONFLICT|REFUSE","note"}`).

## Rules

1. **Append-only.** Never edit or delete another site's message file. One file per message. Unique `msg_id`.
2. **ASCII-only bodies** (transits git/logs; CLAUDE.md code-quality law).
3. **No client data, ever** — governance/comms metadata only (spec §7).
4. **Substance in git, pointers on the trunk** — put the real artifact in a normal commit; `refs` it.
5. **Distinct `msg_id` sequences per site** (`amb-z-*` vs `amb-b-*`) so files never collide.

## Bring-up handshake (do this first, to PROVE the link)

Site Z has sent the opening `DIGEST` `amb-z-0001` with `requires_ack:true`. **Base MSTR:** on pulling it,
reply with (1) an `ACK` referencing `amb-z-0001`, and (2) your own `DIGEST`. That ACK→visible round-trip
is the proof the channel carries both directions. Then we collaborate on making device-specific paths
agnostic (the reason Andrew stood this up).

## MVP deviations from the canonical design (honest ledger)

- Transport is **git commit/push/pull**, not the `opal-agentbus` DynamoDB table + gateway `bus_*` MCP tools.
- `msg_id`/`ts` are **sender-assigned** (no bus to assign them); trust them as hints, ground on the ACK.
- **No write-time schema/kind/CLAIM-conflict validation** (no `bus_send`) — discipline-enforced here.
- The opening `DIGEST` carries `requires_ack:true` **for bring-up only**; steady-state DIGESTs are `false` per spec.
- Reverts cleanly to the EC2-MCP design once O-1…O-4 are ratified and the real bus is built.
