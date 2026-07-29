# PROPOSAL — NFRA_AGENTBUS Port 2 transport: SQS, standalone, off `m365-mcp-gateway`

**Author:** `0.0.0_AB_MSTR~Z` · 2026-07-29
**Status:** PROPOSAL — routes to **CTO** (arch-gate per PRD A.5) + **AE** (build)
**Authority for the workstream:** Andrew-direct handoff 2026-07-29 ~0435Z (device-portability + agentbus standing-up to `~Z`)
**Amends:** `docs/architecture/NFRA_AGENTBUS_PRD.md` Amendment A (2026-07-17, LD-0306)
**Deliberately NOT edited by me:** the PRD itself. A.5 puts the schema/validation design under CTO arch-gate. This proposes; CTO disposes.

---

## 0. Why this exists — and read §1 before §2

I was handed a direction ("a dedicated `opal-agentbus` on SQS — no port, no ALB, no inbound
reachability, IAM-signed only; explicitly NOT reusing `m365-mcp-gateway`") and asked to spec it.

**That direction contradicts a standing PRD amendment in two places, and collides with a standing
Andrew moratorium in a third.** Writing the SQS spec without surfacing that would be
manufacturing a silent conflict between two Andrew-direct instructions issued twelve days apart.
So §1 is the conflict register. §2 onward is the spec.

---

## 1. CONFLICT REGISTER — three collisions, all verified against source

### C-1. Transport: Amendment A says **DynamoDB**; the new direction says **SQS**

`NFRA_AGENTBUS_PRD.md` A.0 table, Port 2 row: *Transport = **DynamoDB** (`opal-agentbus`,
poll-on-heartbeat)*. A.3 WS-1 specifies the table shape (PK `MSG#`/`SITE#`, GSI `to`+`ts`, TTL
wired to envelope `ttl`).

**Why this is resolvable cleanly, not a reversal:** `org/tier0/ledger/LD-0306.md` carries
`requires_andrew_ratification: true` and **`ratified_by: null`**. A.4 **O-4** is explicit —
*"build does not begin without Andrew's yes on this as PRD'd."* **Port 2 was never ratified and
was never built.** So this supersedes an *unratified design*, which is an amendment, not a
rollback of a decision anyone relied on. Nothing is deployed to migrate.

### C-2. Host: Amendment A puts Port 2 on `m365-mcp-gateway`; the new direction removes it

A.0: *"Two DISTINCT bus ports on the shared `m365-mcp-gateway` EC2."* A.1 makes that host part of
the **common spine** of both ports.

**The new evidence that moved this** (measured 2026-07-29, post-dating A by 12 days):
`m365-mcp-gateway` (`i-07dccb1615503ac99`) sits in the **default VPC**
(`vpc-0cc0c6a75e54605e3`) behind an **internet-facing ALB open `0.0.0.0/0` on 80+443**, answering
anonymous requests (302). The EC2's own SG is correct (8080 from the ALB SG only). **So
app-layer auth is the only control — there is no network boundary.**

> **HONEST SEPARATION OF CONCERNS, and I want CTO to see it before choosing:**
> **that measurement indicts the HOST, not the STORE.** A DynamoDB table addressed directly
> via the AWS API — *not* fronted by the gateway — would ALSO have no inbound reachability, no
> port and no ALB, and would satisfy every stated security property. **"Get off
> `m365-mcp-gateway`" and "use SQS instead of DynamoDB" are two separable decisions, and the
> security finding only forces the first.** I recommend SQS on transport-fit grounds (§3), not
> on security grounds — claiming security requires SQS would be overclaiming, and would make a
> weak argument load-bearing.

### C-3. The "ONE mandatory alarm" in A.3 WS-3 is now BANNED

A.3 WS-3 specifies: *"The ONE mandatory alarm: unacked RULING/STOP past `ack_deadline` ->
sender's MSTR escalates to Andrew (fires on ABSENCE). **AC-5:** an unacked STOP past its
deadline produces a live Andrew-page."*

`CLAUDE.md` carries a **standing moratorium, Andrew-direct 2026-07-28** — eleven days after A —
verbatim: *"We need to establish a moratorium on blindly creating alerts and SES and so on
unless I explicitly ask for it."* Latest + most-restrictive binds, so **WS-3's alarm and AC-5
are prohibited as written.**

**This is NOT a request to drop the requirement.** The moratorium's own text says: *"A finding
still lands as a GATE or an OWNED BLOCKING ITEM (TRIGGER_LAYER doctrine) — that is unchanged;
what is banned is reaching for notification machinery as the deliverable."*

**Proposed re-expression (§6):** the unacked-STOP condition becomes a **blocking gate on the
sender's own next action**, not a page. See §6. **O-2 in A.4 (escalation channel) is
answered by being deleted** — there is no channel to choose because there is no notification.

---

## 2. Scope — Port 2 only, and the trap I was warned about

**Port 2 = CROSS-DEVICE, SAME PRINCIPAL.** Andrew's two machines, one GitHub account, one AWS
account, one IAM user. **No trust boundary is crossed.**

**The 5-control Port-1 model is OUT BY CONSTRUCTION** (already ruled in A.2, restated so a
future reader does not re-import it): no partition (nothing to partition from), no DLP egress
strip (both sides are the same person), no read-only/propose default, no ACTION-vs-DATA authz
across a boundary Andrew owns both sides of, no signed cross-principal attribution.

**If Port 2 ever needs to carry cross-principal traffic, that is Port 1's problem, not a Port-2
mode.** The ports do not blur.

**What Port 2 security IS:** per-device IAM principal (CloudTrail-distinguishable) + SQS
resource policy + SSE + the audit lake. That is the whole model, and it is proportionate.

---

## 3. Why SQS fits a message trunk better than a table (transport-fit, not security)

| need | SQS | DDB-direct |
|---|---|---|
| "has this been consumed" | native: receive → visibility timeout → delete | you build tombstones + a GSI |
| poison message containment | native **DLQ** after N receives | you build a retry counter |
| ordered, exactly-once per pair | native **FIFO** + `MessageDeduplicationId` | you build sequencing |
| long-poll without hammering | native `WaitTimeSeconds: 20` | you poll on an interval |
| retention | 14d max (envelope `ttl` is authoritative anyway) | TTL attribute, more flexible |
| **queryable history** | **NO — a consumed message is gone** | **YES** |

**The one place DDB genuinely wins is history**, and it matters: a queue has nothing to
re-read, so "what did base send me last Tuesday" is unanswerable from SQS alone. **§5 resolves
this by keeping the git trunk as the durable record** — which the handoff already ordered to
stay, for exactly this reason. SQS carries *delivery*; git carries *history*. That split is the
design, and it is cleaner than making one store do both jobs badly.

---

## 4. The design

### 4.1 Queues — one per DIRECTION, FIFO

```
opal-agentbus-to-base.fifo     # Z  -> base   (base consumes)
opal-agentbus-to-z.fifo        # base -> Z    (Z consumes)
opal-agentbus-dlq.fifo         # shared DLQ, maxReceiveCount 5
```

Direction-per-queue, not one queue with filtering: **a consumer that can only see its own queue
cannot accidentally consume the peer's mail**, and the IAM policy becomes trivially scoped
(§4.3). One extra queue is cheaper than one subtle bug.

- **FIFO**, `ContentBasedDeduplication: false` — dedup on the envelope's own `msg_id` passed as
  `MessageDeduplicationId`. A resend of the same `msg_id` is idempotent by construction.
- `MessageGroupId` = the site-pair (`base-z`). Single group = strict global ordering, which is
  what RULING/STOP semantics need.
- `VisibilityTimeout: 60s` · `ReceiveMessageWaitTimeSeconds: 20` (long-poll) ·
  `MessageRetentionPeriod: 14d` (max; envelope `ttl` remains authoritative).
- **SSE:** `SqsManagedSseEnabled: true`. A KMS CMK adds key-scoping value only across a trust
  boundary; there is none here (§2). Note it and move on.

### 4.2 Envelope — UNCHANGED, and that is deliberate

The typed envelope and the **six closed kinds** (`RULING` / `CLAIM` / `HANDOFF` / `DIGEST` /
`STOP` / `ACK`) from `AGENTBUS_SCHEMA_SPEC_20260717.md` carry over **verbatim**. The transport
changed; the schema did not. A.4 **O-3** (is the six-kind enum complete for v1?) is unaffected
and still Andrew's to confirm.

Body cap stays **8KB** (well inside SQS's 256KB), keeping A.3 AC-2 intact.

### 4.3 IAM — per-device principal, one scoped statement each

**Today both devices authenticate as IAM user `Andrew_Berman` with two different access keys.**
That is CloudTrail-distinguishable (per `accessKeyId`) and independently revocable, which is
what A.2 asked for — but it is **not** separately *authorizable*: both keys carry identical
permissions, so IAM cannot stop Z from draining base's queue.

**Recommended:** two IAM roles/users, `opal-agentbus-site-base` and `opal-agentbus-site-z`, each
with exactly one statement:

```
site-z  : sqs:SendMessage      on opal-agentbus-to-base.fifo
          sqs:ReceiveMessage   on opal-agentbus-to-z.fifo
          sqs:DeleteMessage    on opal-agentbus-to-z.fifo
          sqs:GetQueueAttributes on both
```
…and the mirror for base. **Send to the peer, receive from your own — never the reverse.**

> **NOT a distrust control** (§2 — there is no distrust). It is **blast-radius containment**:
> if one device is lost, the revoked principal could never have read the other direction, and
> the CloudTrail story is unambiguous rather than inferred.
>
> **Rule 22a applies to whoever builds this:** `comp-iam` models `(action)`, never
> `(action, resource)` — it will report `[GRANTED]` for a queue it has never seen. Verify with
> `aws iam simulate-principal-policy --resource-arns <exact queue ARN>`, **ONE `--resource-arns`
> per call**, positive control as a **separate invocation**, and never use it to check whether
> an action name is real (`accessanalyzer validate-policy` is the oracle for that).

### 4.4 Read path — poll, not a monitor

`bus_poll` long-polls the device's own inbound queue at **session start, on `/watcher`, and on
demand**. It is a **read of a transport**, not a background monitor, and it builds no
notification machinery — §6 keeps it that way.

**ACK stays first-class (Rule 22b, and A.1 binds it to both ports).** A successful
`SendMessage` is **SENT, never READ**. A `requires_ack` message is UNDELIVERED until a
matching `ACK` envelope referencing its `msg_id` arrives on the reverse queue. **No transport
signal — not a 200, not a message-id, not a delete — is ever reported as delivery.** This is the
one property I would fail the build over: it is the exact error class that produced the 7h17m
orphan-watcher incident and base's "amendment landed" claim that had not.

---

## 5. The git trunk STAYS — not as a fallback, as the history tier

The handoff is explicit and I agree without reservation: **the git trunk keeps working and
nothing gates on the SQS build.** Beyond that, it is not redundant with SQS — it is the half SQS
structurally cannot do (§3):

- **SQS = delivery.** Ordered, deduped, consumed-once, ephemeral.
- **git trunk = history.** Durable, diffable, reviewable, and already carrying
  `amb-z-0001..0009` / `amb-b-0001..0007`.

Recommended steady state: **envelopes are written to the git trunk AND sent on SQS.** The trunk
write is the record; the SQS send is the doorbell. If SQS is unavailable, the trunk alone is
exactly today's proven behaviour, which is a real property and not a consolation.

---

## 6. WS-3 re-expressed under the moratorium — a gate, not a page

**Original (now prohibited):** unacked RULING/STOP past `ack_deadline` → page Andrew.

**Proposed:** the condition becomes a **blocking item on the SENDER**, surfaced where the sender
already looks, with no notification machinery built:

1. `bus_poll` returns an `unacked_past_deadline` list — data in a response the agent already reads.
2. An unacked **STOP** past deadline is a **BLOCKING ITEM in the sender's own session**: the
   sender may not report the STOP as delivered and may not proceed as if the peer is halted.
   That is the TRIGGER_LAYER "owned blocking item" the moratorium explicitly preserves.
3. The condition lands in the **audit lake** as a record, not a notification.
4. **Escalation to Andrew happens the way everything else does — an agent tells him.** No page,
   no SNS, no SES, no CloudWatch alarm.

**This deletes A.4 O-2** (which channel pages Andrew): there is no channel because there is no
page. **AC-5 is replaced** by: *an unacked STOP past deadline is REPORTED BY `bus_poll` and
BLOCKS the sender's completion path — exercised, both directions.*

---

## 7. Acceptance criteria — each EXERCISED, never config-read

Inherits A.3's discipline. **A REJECT that cannot fire is not a validator.**

- **AC-1 validator is a control.** Unknown `kind`, unknown `schema_v`, missing per-kind required
  field, and CLAIM conflict each REJECT — each proven by an **exercised mutant**.
- **AC-2 no client data.** 8KB cap + client-data field deny-lint, **positive-controlled** (a lint
  that has never rejected anything has never been tested).
- **AC-3 ACK-only delivery — THE load-bearing test.** A `requires_ack:true` message whose
  `SendMessage` **succeeded** reads **UNDELIVERED** in `bus_poll` and in every liveness view
  until its ACK lands. *The test that fails if transport-success is ever treated as delivery.*
- **AC-4 CLAIM = cross-site HALTGT.** An ASSERT on a resource holding a live unreleased CLAIM
  from the other site is REJECTED with the standing claim returned — **both directions**.
- **AC-5′ (replaces AC-5).** Unacked STOP past deadline is reported by `bus_poll` and blocks the
  sender's completion path — exercised, both directions. **No notification asserted.**
- **AC-6 IAM is scoped, not merely present.** `site-z` **cannot** `ReceiveMessage` on
  `opal-agentbus-to-base.fifo`. Verified on the **live primitive** with one `--resource-arns`
  per call and an isolated positive control — never from a `comp-iam` verdict alone (Rule 22a).
- **AC-7 DLQ catches a poison message.** Exercised by sending one, not by reading the config.

---

## 8. What I need decided, and by whom

| # | item | owner |
|---|---|---|
| **D-1** | **Ratify Port 2 at all** — LD-0306 is `ratified_by: null` and A.4 O-4 blocks the build. **Nothing below starts without this.** | **ANDREW** |
| **D-2** | **C-1/C-2: SQS standalone vs DDB-direct-off-gateway.** The security finding forces *off the gateway*; it does not force *SQS*. §3 argues SQS on transport-fit, §5 covers the history gap. | **CTO** (arch-gate, A.5) |
| **D-3** | **C-3: accept the gate-not-page re-expression** (§6), deleting A.4 O-2. | **CTO**, Andrew if he wants the page anyway (moratorium is his to lift) |
| **D-4** | **Per-device IAM principals** (§4.3) vs staying on two access keys of one user. | **CTO** + **AE** |
| **D-5** | **A.4 O-1** (Site-B serial namespace / WS-0 topology) is still open and still gates everything. | **ANDREW** + MSTR |
| **D-6** | **A.4 O-3** — six-kind enum complete for v1? Unaffected by transport. | **ANDREW** |
| **D-7** | Build execution: TF-only, taxonomy-conformant (`{resource}-role`, region co-located, single scoped statement) per A.5. | **AE** |

## 9. What I am NOT doing

- **Not editing the PRD.** CTO arch-gates it (A.5).
- **Not building it.** The handoff is explicit: *spec it, route it* — the SQS build is a CTO/AE
  dispatch.
- **Not gating anything on it.** The git trunk works today and keeps working.
- **Not building any alert, alarm, SNS topic, SES send, notification, freshness checker or
  monitor** (§6), standing moratorium 2026-07-28.
