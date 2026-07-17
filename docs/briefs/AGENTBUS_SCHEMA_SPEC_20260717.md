# AGENTBUS — Inter-Site Agent Trunk: Schema Specification (v0.1 DRAFT)

**Author:** 0.0.0_AB_MSTR
**Date:** 2026-07-17
**Status:** DRAFT spec, Andrew-directed ("write a spec on this layout of the agentbus schema", MSTR terminal ~18:0xZ). Design seed ratified in-discussion same session. CTO architects the implementation PRD from this; TF-only deploy on the m365-mcp-gateway EC2.
**Companion context:** the two-machine parallelization strategy (one Tier-0 here, second Tier-1 fabric on Andrew's personal machine, division by estate tree + unrelated project groups; same `private-account` GitHub account, machine-scoped credentials, distinct serial namespace for site-B agents).

---

## 1. What AGENTBUS is, and is not

**IS:** the **inter-site trunk** — low-frequency, typed, high-consequence messaging between the two
machines' agent fabrics, hosted as a new integration on the existing `m365-mcp-gateway` EC2
(`mcp.opalinvest.dev`), inheriting its ALB OIDC front, Bearer auth at `/mcp`, tier entitlement, S3
audit lake, and `deploy-to-ec2.sh`/TF deploy discipline.

**IS NOT:** a replica of the local `opal-agent-comms` broker (port 7800). Intra-machine chatter
(watchers, heartbeats, RAVC ping-pong) stays local. Anything that would put >1 msg/min steady-state
on the bus belongs on the local broker or in git.

**Andrew's spec phrase, taken literally:** *"high-leverage high-signal minimal comms, probably in a
structured format."*

## 2. The binding design law: ACK is first-class (Rule 22b, cross-site)

**SENT IS NOT READ.** The local fabric's deepest recorded defect (orphan watchers manufacturing
REACHABLE for deaf serials; LD-0271, CLAUDE.md 22b) recurs at higher stakes on any cross-site bus.
Therefore, structurally:

- A message with `requires_ack: true` is **UNDELIVERED until an agent-side `ACK` message referencing
  its `msg_id` lands on the bus.** No producer-side or transport-side signal (write success, poll
  receipt, connection liveness) may ever be reported as delivery.
- Unacked `RULING` / `STOP` past `ack_deadline` → the sender's MSTR **escalates to Andrew**; this is
  the bus's only mandatory alarm, and it fires on ABSENCE, not on error.
- A site's liveness verdict derives **only from its own emitted messages** (HEARTBEAT/ACK), never
  from connection state.

## 3. Envelope schema (every message, no exceptions)

```json
{
  "msg_id":       "amb-<ulid>",              // bus-assigned, globally unique, sortable
  "ts":           "2026-07-17T18:05:00Z",     // bus-assigned server time (never client-supplied)
  "from_site":    "A",                        // registered site id (v1: "A" = primary, "B" = personal)
  "from_serial":  "0.0.0_AB_MSTR",            // full suffixed serial of the emitting agent
  "to":           "site:B",                   // "site:<id>" | "serial:<full>" | "broadcast"
  "kind":         "RULING",                   // closed enum, sec 4. Unknown kind = REJECT at write.
  "body":         { },                        // per-kind schema, sec 4. Validated at write.
  "refs":         ["<git-sha>", "LD-0305"],   // git shas / LD-RV ids / TO filenames grounding the msg
  "requires_ack": true,
  "ack_deadline": "2026-07-17T19:05:00Z",     // required iff requires_ack; sender-set
  "ttl":          "2026-07-24T18:05:00Z",     // hard expiry; expired msgs excluded from poll, retained in store
  "schema_v":     1
}
```

Rules: bus assigns `msg_id`+`ts` (client clocks are hints, never record); `refs` is how a 2-line bus
message stays 2 lines — **the substance travels in git, the bus carries the pointer + the verbatim
that cannot wait for a pull.** ASCII-only bodies (CLAUDE.md code-quality law; this transits AWS logs).

## 4. Kinds (closed enum — six, and the bar for a seventh is high)

### 4.1 RULING — sovereign/tier-0 instruction propagation (the killer app)
```json
{ "verbatim": "<Andrew's words, VERBATIM -- the phrasing IS the ruling>",
  "channel": "MSTR terminal | CTO terminal | <agent> session",
  "spoken_at": "~17:55Z 2026-07-17",
  "scope_note": "<surfaced scope, explicitly NOT adjudicated>",
  "supersedes_hint": ["AMEND-63"],
  "durable_record": "<git-sha or memory path -- REQUIRED; a ruling with no durable record is not sendable>" }
```
`requires_ack: MANDATORY true`. Receiving site's MSTR: record + broadcast locally per XXX.md law,
then ACK. This extends the record+broadcast law across the site boundary at real-time latency
(today's only carrier is git pull, minutes-to-hours).

### 4.2 CLAIM — tree/deploy ownership assertion (cross-site HALTGT substitute)
```json
{ "resource": "tree:inf | tree:portal | deploy:<pipeline> | schedule:<name>",
  "action": "ASSERT | RELEASE",
  "holder_serial": "...", "until": "<ts|standing>",
  "basis": "<LD/TO/ruling ref>" }
```
Conflict rule: a CLAIM ASSERT on a resource with a live non-released CLAIM from the other site =
**REJECTED at write** with the standing claim returned. Claims are the deploy-partition enforcement
the local HALTGT inbox checkpoint structurally cannot do cross-machine. Standing claims seed from
the ratified tree partition (companion doc).

### 4.3 HANDOFF — a project crossing the site boundary
```json
{ "project": "OPAL_XXXX", "direction": "A->B | B->A",
  "state_refs": ["<git-shas carrying ALL state>"],
  "open_items": ["..."], "gates": ["<who holds what word>"],
  "receiving_owner": "<serial>" }
```
`requires_ack: true`; the ACK names the receiving owner's serial = the new single-owner. A handoff
whose state is not fully in the `state_refs` commits is malformed by definition (no side-channel state).

### 4.4 DIGEST — MSTR<->MSTR periodic rollup (continuity)
```json
{ "roster": [{"serial": "...", "state": "WORKING|IDLE|BLOCKED", "on": "..."}],
  "projects_active": ["..."], "blockers_cross_site": ["..."],
  "last_pushed_sha": "<the site's git frontier>",
  "andrew_present_at": "A | B | none-observed" }
```
Cadence: session-start + every ~60min while live + session-close. `requires_ack: false`. The DIGEST
stream doubles as site liveness (sec 2) and as the disaster-continuity record — either MSTR can
reconstruct the other site's posture from the last DIGEST + git.

### 4.5 STOP — halt semantics, cross-site
```json
{ "target": "site:B | serial:<full>", "verbatim": "<the halt instruction>", "issuer": "andrew | 0.0.0_AB_MSTR" }
```
`requires_ack: MANDATORY true`, shortest deadlines on the bus (default 10 min). **A STOP is not in
force until ACKed, and the sender treats un-ACK as ESCALATE-NOW, not as delivered-probably** — the
local fabric's `[STOP]`-does-not-reliably-hard-block lesson (Rule 18), designed in rather than
rediscovered.

### 4.6 ACK — the delivery oracle
```json
{ "acks_msg_id": "amb-<ulid>", "verdict": "ACK | ACK-WITH-CONFLICT | REFUSE",
  "note": "<REQUIRED for ACK-WITH-CONFLICT / REFUSE -- e.g. latest+most-restrictive collision>" }
```
Only an agent session emits ACK. `ACK-WITH-CONFLICT` is the cross-site `latest + most-restrictive
binds` surface: the receiving MSTR does not adjudicate, it surfaces (both MSTRs escalate to Andrew).

## 5. Site registry + heartbeat (rides the same table)

```json
{ "site": "B", "label": "andrew-personal", "serial_block": "<ratified block, companion doc>",
  "trees_owned": ["portal", "..."], "mstr_serial": "0.0.0_AB_MSTR@B",
  "last_heartbeat_ts": "...", "last_digest_msg_id": "..." }
```

## 6. Storage + transport (v1, deliberately small)

- **One DynamoDB table** `opal-agentbus` (PK `MSG#<msg_id>` / registry rows `SITE#<id>`; GSI on
  `to`+`ts` for poll; TTL attribute wired to the envelope `ttl` for expiry-from-poll, items retained
  90d for audit). No SQS, no websockets, no fan-out infra.
- **Five MCP tools** on the gateway: `bus_send` (validates envelope+kind schema at write; REJECT on
  unknown kind / missing per-kind required fields / CLAIM conflicts), `bus_poll` (by site/serial,
  since-cursor, excludes expired), `bus_ack`, `bus_claim` (sugar over send with conflict check),
  `bus_digest` (sugar over send).
- **Delivery = poll-on-heartbeat:** each MSTR polls at session start + every N min (default 5) +
  on /watcher events. SSE push is v2; nothing in the schema changes for it.
- **Entitlement:** `min_tier` restricted to Tier-0/1 serials; every call lands in the existing
  `s3://opal-mcp-audit` lake. spawn/kill authority does NOT ride the bus (site-local, per
  constitution).

## 7. Hard exclusions (schema-enforced where possible)

1. **NO CLIENT DATA ON THE BUS. EVER.** Governance/comms metadata only — bd/cot/firm separation is
   never implicated by transport. Gate candidate: body-size cap (8KB) + a deny-lint on known
   client-data field names at `bus_send`.
2. No high-frequency traffic (heartbeat cadence floor 60s; per-site send rate cap).
3. No substance-in-body when a git ref can carry it — the bus is pointers + verbatims + claims.
4. No transport-derived liveness or delivery verdicts (sec 2).
5. No new kinds without a ratified spec bump (`schema_v` increments; unknown `schema_v` = REJECT).

## 8. Open items for the CTO PRD

- Site-B serial namespace + tree partition ratification (companion two-machine doc — arguably one PRD).
- Auth identity per site (second machine-scoped gateway credential; CloudTrail-distinguishable).
- `bus_send` validation implementation + the exercised-mutant test set (a REJECT that cannot fire is
  not a validator — Controls-over-Care).
- Escalation mechanics for unacked STOP/RULING (who pages Andrew, on which channel, exercised).
- V2: SSE push; RULING auto-fold into the receiving site's MEMORY.md trigger rows.
