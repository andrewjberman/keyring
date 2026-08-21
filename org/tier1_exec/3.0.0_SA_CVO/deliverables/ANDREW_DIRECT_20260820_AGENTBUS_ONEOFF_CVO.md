# ANDREW-DIRECT: one-off /agentbus at the CVO seat (2026-08-20 ~2100Z, laptop CVO terminal)

**VERBATIM:** *"This is a oneoff we dont usually run this but I want the MSTR~Z on the other fabric
to send you a message on the subject so you can run it just for now"* — as the argument to `/agentbus`.

**Scope (his words, applied to my seat only):** a ONE-OFF — not a standing CVO arm, not a change to
the XXX.md 1b-F CVO rows (which carry no `/agentbus`). The purpose is to receive ONE message from
`0.0.0_AB_MSTR~Z` "on the subject" and run it.

## What was measured and done (the honest sequence)

1. `/agentbus` Step 1: device measured **laptop** by workspace path (never assumed).
2. Step 2: `watch` armed under the Monitor tool → **REFUSED rc=3** naming pid 3996525.
   **Identified at source (Windows process table, not MSYS `ps`): `0.0.0_AB_MSTR` base's live
   consumer** (`agentbus-consumer.py`, born 00:17 ET 2026-08-20, parent `agentbus-sqs.sh watch`
   pid 17932; MSTR LIVE on the broker, log: "watcher + bus consumers live").
3. **The refusal IS success per the skill's own law:** one consumer per device; SQS is exactly-once,
   a second consumer would STEAL the message at random with no trace on the losing side. **I did
   NOT arm a second consumer and did NOT set `AGENTBUS_DEVICE` to cross-consume** — no orphan-thief,
   no split queue, no stolen mail.
4. **Delivery path for the one-off, chosen because it moves nothing:** MSTR base's consumer receives
   `0.0.0_AB_MSTR~Z`'s message → relays content + MessageId to me over local MCP (same device, same
   minute) → I ack the MessageId back to sitez under MY serial (Rule 22b) → I run the subject.
   MCP to `0.0.0_AB_MSTR` requesting the relay (with the consumer-handover alternative offered at
   their discretion as lock holder); bus send to sitez telling `0.0.0_AB_MSTR~Z` the path.
5. Queue peeked (non-consuming) at ~2105Z: depth 0 — the message had not yet been sent (or had
   already been taken by MSTR's poller; either way the relay ask covers it).

**Why this record exists:** a future reader of `/agentbus` history will see a CVO arm attempt and a
refusal on the same minute; this states the rule was honored, not worked around, and the one-off
ran through the existing single consumer. Per the skill: *"If you get the refusal, that is success
— a consumer is already running and you are reachable. Do not work around it."*

— 3.0.0_SA_CVO
