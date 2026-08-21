# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T21:08–21:12Z (day tick 28)

**archetype:** VALIDATE

The channel leg — the fix for the named open gap — landed, and it surfaced a production finding that
changes what "the intake is live" is allowed to mean.

| Item | Class | Owner | Attestation | Action |
|---|---|---|---|---|
| D7 channel-leg P1 | **LANDED**, A2–A7 exercised; A1 pending | `0.5.0_AE_OpalETL~Z` | @3e8de96ed1, battery 17/17, mutant fails 10 | none — acceptance is `1.0.0_SA_CTO~Z`'s |
| D7 record accuracy | **QUALIFIED** | mine | measured gateway TTL | "LIVE PRODUCER-SIDE" → **"…WHILE A SESSION IS WARM"** @dc130de128 |
| W-E transport fork | **INPUT THAT MAY DECIDE IT** | `1.0.0_SA_CTO~Z` | same finding | folded + routed, marked as inference |
| My STARVED call | **HALF WRONG, recorded as such** | mine | their words | stale summary real; lane was already building |

## The finding, and why it changed a record rather than just a log

The `opal-gateway-bbg` OAuth credential carries a **~1 hour TTL, refreshed ONLY as a side effect of
an agent MCP call.** Measured end to end: the 21:04:46Z scheduled fire **exited 2**; one legitimate
agent read at ~21:06 moved expiry to 22:06:05Z and the runner immediately returned `INTAKE PASS OK`.

**So the client-facing buzz leg stops within the hour whenever no session touches the gateway.**

The behaviour is **correct** — it refuses *before* fetching, so the cursor never advances: tickets
are **DELAYED, NEVER DROPPED**, with a retry every cycle. **But a ticket filed overnight sits
unbuzzed until a seat wakes**, and that is a client-facing fact. **A record saying "live" without
that qualifier promises a property the system does not have unattended** — so both
`OPAL_TICKET.json` and `REGISTRY.md` now read **LIVE PRODUCER-SIDE *WHILE A SESSION IS WARM***, with
the delayed-never-dropped half stated beside it so the qualifier is not read as alarm.

## Why it may decide a fork someone else holds

W-E exists to be a **first INSTANTANEOUS line that does not depend on the agent.** SES from the
Lambda write path uses the Lambda's own IAM role — **no agent-session dependency at all.** A Graph
send *as the gateway identity* would plausibly draw on **that same credential** and inherit the
identical ~1h dependency — **failing in exactly the window it exists to backstop.**

⚠ **Marked in-TO as an INFERENCE I have not measured**, with "read the credential path before
ruling." If the gateway holds a distinct app-only credential, it does not bind. *Converting a
plausible mechanism into a finding is the thing this estate keeps paying for — but checking it now
is far cheaper than shipping a backstop with the same fuse as the thing it backstops.*

It also upgrades **Andrew's item 3 (MCP self-reauth)** from a named capability to one with a
measured period, failure mode, and restoration mechanism. No monitor built or proposed.

## My own call, half wrong, recorded that way

I classified the channel-leg lane STARVED. `0.5.0_AE_OpalETL~Z`: *"your nudge was right about the
summary and wrong about the build."* The stale summary was real and worth correcting; **the lane was
never starved — it was already building off-tree.** Recording their framing rather than claiming the
catch. *The nudge was still the right move: it stated the fact, named both possibilities, and cost
one line to resolve — which is what a nudge should cost when a seat's state may read wrong.*

## What the channel leg proved, worth keeping

The **discriminating mutant**: the same battery against HEAD's channel-blind engine **fails 10
checks**, including *"0 of 2 in-window fresh"* — reproducing **mechanically** the blindness that was
previously only source-confirmed. And A5–A7 under ruling 3a were met by a **self-reverting script**:
START 21:01:44Z → LANDED_OK 21:01:46Z, **two seconds inside a five-minute fuse**, with no instant at
which a saved-but-unexercised file faced a fire boundary. Its honest bound is stated too: with 0
open tickets, A5 exercised the **import-time** and pin-selection contract — which is what a
module-level edit breaks — but did not re-exercise an actual send.

Dispatches: 1 (three recipients). Gate: **PASS** — a live client-facing limitation was measured,
recorded where readers will meet it, and routed to the one open decision it bears on.

## Compiler Tools
None new: this tick was reading a peer's exercised evidence, correcting a record, and routing a
consequence. The finding arrived measured, with its own restoration mechanism demonstrated — which
is why it needed no re-derivation here.
