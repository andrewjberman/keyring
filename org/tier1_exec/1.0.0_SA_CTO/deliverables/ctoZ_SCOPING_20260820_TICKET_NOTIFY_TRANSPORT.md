# SCOPING — "CAN THE LAMBDA JUST HIT THE AGENT DIRECT?" (ticket notify transport)

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~20:45Z
**Trigger:** Andrew-direct at the `0.0.0_AB_MSTR~Z` console, two deliveries ~2035Z and ~2038Z, relayed with assessment.
**Status:** **SCOPING ONLY. Nothing built, nothing armed, no gate.** His word converts any of it.

**VERBATIM (~2035Z):** *"Would it be faster if we created an email distribution group that picks up tickets, and then graph api from the email hits the agent somehow? I think the email distribution group as a first-line, instant notification with the link is not a bad idea and should happen anyway, but maybe there is a bonus here whereby it's faster to hit the agent instantaneously off the graphAPI versus whatever mechanism we're running now."*

**VERBATIM (~2038Z):** *"if it was possible for the lambda to just hit the agent direct somehow that would be the best case scenario and there doesnt need to be polling at all. Could we do something like that"*

---

## THE DIRECT ANSWER TO THE DIRECT QUESTION

**Yes. It is possible, and the mechanism is native on both sides.** `0.0.0_AB_MSTR~Z` grounded the agent half
this turn: the harness Monitor tool has a **WebSocket source** — the agent holds a `wss://`, and every
server-pushed frame becomes a chat event, *"no shell, no polling."* The AWS half is API Gateway WebSocket +
`PostToConnection`. The ticket Lambda would write the row and push the frame **in the same invocation**:
sub-second, no interval anywhere.

**But it should not be the first thing we build, and the reason is arithmetic rather than preference.**

---

## WHERE THE TIME ACTUALLY GOES (from the water test's own clocks)

```
created  20:18:09.873Z
fire     20:19:46.16Z   <-  96.287s  WAITING FOR THE CADENCE BOUNDARY
posted   20:19:49.44Z   <-   3.28s   of actual work
                            ------
                            99.6s total     ->  96.7% is the poll interval
```

**97% of the latency is the 5-minute interval. The notification transport is the other 3%.**

⚠ **AND 99.6s UNDERSTATES IT — nobody should quote it as "the" latency.** That wait is one draw from
`uniform[0, 300]`. **Expected latency is ~153s; worst case ~303s.** We happened to sample below the mean.

**Every candidate route — email/Graph, a DDB stream, a queue write, a WebSocket — buys the same thing:
emission moves to ticket-create time.** They are identical on the 97% and differ only on the 3%. So this is
**not a latency choice. It is a reliability-and-lifecycle choice.**

---

## RECOMMENDATION — ordered by speed gained per unit of new machinery

### 1. Emit to the queue this box ALREADY long-polls. `~153s -> ~1s`. **ZERO new infrastructure.**

**Both halves are source-confirmed live at this seat, not proposed:**

- **Consumer, live and running since Aug 18:** `agentbus-consumer.py --queue-url .../agentbus-...fifo
  --device sitez`, **pid 6567**. `.tools/agentbus-sqs.sh:360` confirms the shape: *"long-poll 20s."*
- **Producer, one module and exactly two call sites:** `infra/aws/lambda/ticket_center/lambda_function.py:223`
  (`submit_form`) and `:256` (`create_ticket`), both already `_table.put_item(...)` with
  `ConditionExpression="attribute_not_exists(ticket_id)"` @`0968e3833f`. *(Tree/source plane — I did not read
  the deployed package.)*

**SQS long-poll is not an interval.** It holds the connection open and returns **the instant** a message
lands — push-shaped from the consumer's side at ~1s. This is **build-ladder rung 2** (the estate already has
it) against email's rung 7.

### 2. Measure the wake hop (`0.0.3_BG_BBGTerminal`'s sec11 S3) BEFORE funding any transport build.

**It sets the FLOOR under every emission optimization.** If the wake hop is 60s, then moving emission from
153s to 1s buys `153 -> 61`, not `153 -> 1`. **Optimizing emission beneath an unmeasured constant is
optimizing above a number nobody has.** `0.0.3_BG_BBGTerminal`'s S3 refuses to rank it, which is correct.
*This is a sequencing recommendation, not a hold — nothing is held on it.*

### 3. Add the WebSocket accelerator ONLY if the measurement says the last second matters.

**And never as the only path.** ⚠ **A push to a dead socket is GONE. SQS holds 14 days; a socket holds
nothing.** A WS-only design is a delivery path with no durable backstop — when the socket is dead the ticket
is simply never delivered, and **every producer-side probe reads healthy.** That is the orphan-watcher shape
and it is the same defect our own law already names: *a pipeline whose only trigger is another pipeline's
success has no schedule.* **WebSocket = ACCELERATOR. Durable queue + schedule = BACKSTOP.**

---

## WHY EMAIL IS THE WRONG TRANSPORT FOR THE *AGENT* PATH

**Route (email/Graph) is route (queue) plus two extra failure domains — it does not remove a hop, it adds
one.** This box has **no inbound public endpoint**, so a Graph webhook lands in cloud infra and *still* needs
the same last hop to the local seat. On top of that it adds:

1. **An unbounded mail-transport hop** — the one leg whose latency we do not control.
2. **A public webhook receiver** — new attack surface, new thing to operate.
3. **Graph subscription RENEWAL** — and this is the disqualifier. Change-notification subscriptions expire
   and must be renewed; **a renewal that silently fails leaves a green-looking receiver with a dead feed.**
   We have a live banked instance of exactly this class at exactly this seat: teams-watch token expiry, where
   *an idle seat stays deaf while every liveness instrument reads healthy.* **Adding a second
   subscription-lifecycle dependency to a path whose entire purpose is to not be deaf is self-defeating.**

---

## THE EMAIL DL FOR HUMANS — I recommend YES, and it needs one word from him

The DL **stands on its own merits** as a human first-line: a pointer with a link, arriving where people
already are. It is a genuinely good idea and is unaffected by everything above, because it is not the agent
path.

⚠ **It requires Andrew's explicit word.** The standing moratorium (CLAUDE.md, 2026-07-28) bans building
notification machinery unless he explicitly asks. **He is the one proposing it, and *"should happen anyway"*
reads to me as very close to that ask — but the interpretation of his word's breadth is his, not mine, so I
am surfacing rather than adjudicating.** One word converts it. **Nothing is held on this.**

**ONE BINDING CONSTRAINT IF IT IS BUILT: pointer + link ONLY. NEVER a second home for ticket state.**

And the reason is sharper than tidiness, because it is the *same defect* `3.0.0_SA_CVO~Z` raised on the
client projection **today**: **an email DL is an authorization surface with no authorization matrix.**
The P0 finding is that row-scope is not field-scope — the wire carries what the UI does not render. An inbox
is that problem with no controls at all: **Andrew's own C2/C3/C4 enumeration of what a client may see cannot
be enforced inside an inbox, and mail forwards.** A pointer + link carries no ticket fields, so it has no
field-projection problem to get wrong.

---

## TWO BOUNDS I AM CARRYING FORWARD, BOTH STATED AS UNMEASURED

1. **API Gateway WebSocket idle timeout (~10 min) and max connection duration (~2 hours) are
   `0.0.0_AB_MSTR~Z`'s recollection, NOT a measured read.** They set the keepalive and re-arm discipline and
   must be read from live service limits before any design commits.
2. **Whether the estate ALREADY has a WebSocket API anywhere is UNCHECKED** — `comp-estate` / `comp-routes`
   answer it, and rung 2 comes before rung 7.

**Checked rather than assumed** (`0.0.0_AB_MSTR~Z`): `RemoteTrigger`'s `create_webhook_trigger` does give a
webhook→agent path, **but it fires a claude.ai CLOUD run session** — not a wake of a seat holding this box's
gateway/Teams identity. **It does not serve the `0.0.3_BG_BBGTerminal` duty.**

---

## TWO THINGS NONE OF THIS FIXES — stated so the speed win does not paper over them

1. **No transport here hears a HUMAN ASKING A QUESTION in the channel.** They all announce *new tickets*.
   **The channel-leg P1 stands regardless and is the only leg that hears conversation.** Complements, not
   substitutes.
2. **No transport wakes a seat that is not running.** At 2am the question is not how fast the message
   arrives — it is whether anyone is there. That is the process-truth-gated summons pattern (is the seat
   alive; spawn if not), and it is a **separate** piece of work from every option above.
