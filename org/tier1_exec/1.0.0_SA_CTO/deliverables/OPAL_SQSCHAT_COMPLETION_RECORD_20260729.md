# OPAL_SQSCHAT -- COMPLETION RECORD, 2026-07-29

    author:   1.0.0_SA_CTO~B (build + close)
    verifier: 0.0.0_AB_MSTR (independent exercise on every limb he did not author)
    status:   CLOSED-AS-ACCEPTED by Andrew ~1735Z. NOT closed-as-fixed. The distinction is
              load-bearing and is stated in full at section 3.
    artifact: .tools/agentbus-sqs.sh @1bf1fa6e4a (CLOUD, pushed)

**ANDREW-DIRECT ~1735Z, VERBATIM (his terminal), answering whether "done" is achievable with a
SESSION-BOUND consumer:**

> "Yes, its good to go in current state i dont care about expanding functionality at this time."

That discharges his ~1712Z instruction ("completely done and functional, validated"). Full ruling
record: `logs/2026-07-29/CTOB_session_close_ANDREW_DIRECT_three_rulings_1735Z.md` @6559e09f8f.

---

## 1. THE TWO ITEMS THAT ARE STILL OPEN OR DECIDED-BY-ANDREW

**(f) TERRAFORM -- OPEN. NOT MINE. DELIBERATELY NOT CLOSED BY INFERENCE.**
Both queues are LIVE AND OUTSIDE TERRAFORM STATE:

    agentbus-ajbdev-sitez-to-laptop.fifo     us-east-1 / 313476888478
    agentbus-ajbdev-laptop-to-sitez.fifo     us-east-1 / 313476888478

Owner `0.7.0_AE_CloudOps`, TO OPAL_SQSCHAT.T1, gated on the freeze ending post-17:15Z.
**Andrew's ruling closes FUNCTIONALITY; putting live infrastructure under state is not functionality
expansion.** I did NOT read the ruling as cancelling T1, and I did NOT read it as confirming T1.
**If anyone wants T1 dropped, that needs Andrew's word -- it must not be closed on my inference.**
Two live queues costing money outside state is not a finished system.

**CONSUMER LIFECYCLE -- KNOWN RESIDUAL, SOVEREIGN-ACCEPTED.**
The consumer is SESSION-BOUND on both devices; it dies with the session. Six agent sessions died in
this fabric today (seven by session end).

**THE FRAMING MATTERS AND IS NOT THE OBVIOUS ONE:**
- **IT IS NOT DATA LOSS.** MSTR's accidental timeline disproved that on real traffic (section 4c).
  SQS durability holds; that is the property it was chosen for and it is now exercised, not assumed.
- **IT IS AN UNBOUNDED, INVISIBLE DELIVERY LATENCY.** The gap between send and delivery is bounded by
  nothing except when a human next starts a session on that device. **A DEAF DEVICE AND A QUIET ONE
  ARE BYTE-IDENTICAL FROM EVERY VANTAGE THE SYSTEM CURRENTLY OFFERS** -- the sender holds a MessageId
  (which is not delivery) and the recipient device is not running to report anything. That is the
  orphan-thief shape with a queue substituted for an inbox.
- **BY-HAND DISCRIMINATOR, NO MACHINERY:** `agentbus-sqs.sh peek <device>` across two spaced reads.
  A depth that stays >0 means nobody is draining. **NO monitor/alarm/checker was built and none is
  wanted** -- the moratorium stands, monitoring a consumer whose lifecycle is the open question would
  measure the wrong thing precisely, and Andrew has now closed functionality expansion outright.

**ANDREW HAS ACCEPTED THIS.** It is not an open call, not a gap, and not a fix awaiting hands. **If a
device goes quiet for hours in future, THAT IS THE ACCEPTED BEHAVIOUR, not a new incident.** Nobody
builds a durable per-device consumer; nobody re-raises it.

---

## 2. THE COMPLETION BAR

| # | item | verdict | evidence |
|---|---|---|---|
| a | Z -> laptop delivery + agent ACK | **MET** | MSTR: b02b96d8 / dbaf5251, acked by id |
| b | laptop -> Z delivery + agent ACK | **MET** | MSTR: ~Z acked 1512Z via its Monitor |
| c | OFFLINE DURABILITY | **MET** | real-traffic timeline, section 4c |
| d | consumer on BOTH devices | **MET** | ~Z `bjnsnjyip`; MSTR `bnkj8hvhy` |
| e | no-data-loss on EVERY emit path | **MET** | section 4a + 4b; recv verified separately, not inferred |
| f | queues under TERRAFORM | **OPEN** | AE's, section 1 |
| g | send() text-grep | **CLOSED** | @1bf1fa6e4a, section 4d |

---

## 3. WHY "CLOSED-AS-ACCEPTED" AND NOT "CLOSED-AS-FIXED"

Two defects were **FIXED** (sections 4a, 4d). One property is **ACCEPTED UNFIXED** (the session-bound
consumer). One item is **OPEN AND OWNED ELSEWHERE** ((f), Terraform).

Collapsing those into a single green "COMPLETE" would assert something untrue about all three. The
record says ACCEPTED so that a future reader inherits the residual rather than rediscovering it as a
surprise -- which is the entire failure class this bus was built to escape.

---

## 4. EVIDENCE PER LIMB

### 4a. THE DATA-LOSS DEFECT -- FIXED @2bc9515c3c

Reported by MSTR. **Reproduced independently before touching anything** (he said explicitly: *"do not
take my report on trust either; the reproduction above is runnable"*). All four limbs confirmed:

| claim | measured |
|---|---|
| `command -v jq` in a harness shell | **NOT FOUND -> the lossy fallback was THE LIVE PATH** |
| `.tools/jq.exe` | jq-1.7.1, tracked, works |
| `grep -o '"Body": "[^"]*"'` on a quoted body | `Andrew said \` -- truncated, rest destroyed |
| same input via jq | `Andrew said "stop" and more text after` |
| `grep\|cut\|while` with ZERO extractions | **rc=0 -> `emitted=1` -> DELETED having emitted nothing** |

Root cause is NFRA_TOOLARCH.PATHFIX: harness shells source no profile, `.tools` is never on PATH, so
`command -v jq` fails on EVERY harness shell. **The bus carries largely verbatim Andrew quotes, which
contain quote characters by definition -- so it fired on exactly the traffic that matters most.** At
least one message was destroyed before the fix.

**Fix is RESOLUTION, NOT HARDENING:** derive jq from the script's own location so the lossy path never
executes. The remaining no-jq fallback **cannot delete anything** (`emitted=0` unconditionally) -- a
stronger and more checkable property than count-matching. `recv` given the same structural treatment;
with no jq it declines to delete rather than guessing.

### 4b. TRUNCATION CONFIRMED DEAD -- TWO FIXTURES, TWO HANDS, TWO PATHS

- **MSTR's** (receive side): body with real quote chars arrived intact, id
  `f157e567-bd88-47bf-970e-772dfaeaa120`, queue drained to 0.
- **Mine** (SEND path): `d7af661f-68bc-4814-8607-e8327b5d31a0`, **ACK READ 17:23:52Z by
  `0.0.0_AB_MSTR`** via consumer Monitor `bnkj8hvhy` -- agent-side oracle, not a depth read. Body
  carried two quoted phrases plus `END-MARKER-CTOB-9X2K` placed **AFTER** both, so the marker's
  presence is the discriminator for a surviving truncation. **Marker arrived. Both quote sets intact.**
  Under the old build everything from the first quote onward would have been destroyed.

A fix confirmed only by the fixture its author chose is the hand-chosen-control problem; this is two
independent fixtures from different hands through different paths.

### 4c. OFFLINE DURABILITY -- EXERCISED BY ACCIDENT, ON REAL TRAFFIC

    ~16:35Z    MSTR stopped his consumer over the data-loss bug
     16:42:46Z ~Z sent dbaf5251 -- while this device had NO CONSUMER AT ALL
    ~17:08Z    MSTR re-armed
     17:08Z    dbaf5251 delivered INTACT with its id, ~26 minutes later

**Nobody designed this test, which is why it counts.** It is the property SQS was chosen for and it
was previously UNEXERCISED (~Z's open item (c)).

### 4d. THE SEND RECEIPT -- FIXED @1bf1fa6e4a, AND IT DID NOT CLOSE THE EXPECTED WAY

MSTR's offered reason for closing (g) -- *"a UUID cannot contain a quote"* -- is **CORRECT and is now
written into the file** (MessageId charset `[0-9a-f-]`; truncation risk on that field genuinely nil).
Verified rather than accepted.

But checking it surfaced a **different real defect on the same line**:

    extraction yields nothing -> mid="" -> "SENT to sitez: MessageId="   at rc=0

**The send SUCCEEDED.** So it is a RECEIPT failure, not a send failure, and conflating them is
expensive BOTH ways: read as send-failure the caller **RESENDS AND DUPLICATES**; read as success the
caller holds an unusable receipt. **Rule 22b's ack discipline hangs off that id -- an empty one makes
a real, delivered message permanently UNACKABLE**, which is the SENT-IS-NOT-READ gap this bus exists
to close. Now exits **rc=3** (distinct from rc=2 arg errors, because *"sent but unackable"* is its own
state) with the raw response dumped so the id stays hand-recoverable.

### 4e. A GAP I CLOSED IN MY OWN WORK BEFORE REPORTING IT DONE

I had modified `send()` -- **the line every single send passes through** -- and tested it only against
synthetic fixtures. That is a config-read-grade test backing a behavioural claim, and I was one report
away from marking my own change validated on it. The rc=3 guard was the real risk of @1bf1fa6e4a, and
the only way to learn it does not misfire on a real AWS response is to send a real message. Exercised
live: MessageId returned, rc=0, normal path unbroken.

**Claimed as INFERENCE, not delivery:** the queue drained to 0-visible-0-in-flight, and delete is gated
on successful emit, so *gone* rather than merely *invisible* implies an emit. **That is a sound
inference and it is still not delivery** -- a drained queue cannot distinguish "emitted to a live
agent" from "emitted into a dead pipe by an orphan." Only MSTR's agent-side ACK closed it.

---

## 5. THE DOCTRINE FINDING -- THE REAL DELIVERABLE

**EMPTY-VS-FAILED-RETRIEVAL (contract C3) BIT THIS ONE FILE THREE TIMES:** at the body emit, at the
delete gate, and at the send receipt. Each looked local. The general form:

> **SILENCE OR EMPTINESS WAS ALLOWED TO STAND IN FOR A FACT -- in a messaging tool, where the facts
> are precisely what the caller cannot re-derive.**

Treat any remaining bare extraction in this file as guilty until checked. MSTR concurs and would
extend it past this file.

**SECOND FINDING, from correcting myself -- THE FABRICATED BLOCKER.** I twice reported that
`org/tier1_exec/1.0.0_SA_CTO/**` (BASE_EXEC) blocked this lane from committing. **WRONG** --
@d026f5214e and @6559e09f8f both landed there clean, no override. I read lane membership in
`.owned-paths.yaml` and reported the inference as a constraint **without exercising the gate**: a
DESIRED-state read standing in for APPLIED behaviour (Rule 22a) -- in the same session I caught the
identical substitution in my own code. It caused MSTR to begin taking custody of this record to work
around a blocker that did not exist. Corrected at 173040Z / 173056Z.

> **THE HAND ANSWER TO "CAN SERIAL X COMMIT PATH Y" IS NOT MERELY SLOW, IT IS WRONG IN THE DIRECTION
> THAT INVENTS BLOCKERS -- AND A FABRICATED BLOCKER COSTS MORE THAN A MISSED ONE, because it routes
> work to other people and NEVER PRODUCES THE ERROR MESSAGE THAT WOULD CORRECT IT.**

I hand-resolved that file four times tonight; it blocked or nearly blocked three lanes, always
discovered at COMMIT time after work was built. A `comp-ownpath <serial> <path>` resolving the way the
HOOK does rather than the way a human reads the YAML would have caught it in seconds. Logged as a
Compiler-Tools gap, not a build request.

---

## 6. OPEN, AND OWNED BY SOMEONE ELSE

1. **(f) Terraform** -- `0.7.0_AE_CloudOps`, TO OPAL_SQSCHAT.T1, post-freeze. Section 1.
2. **~Z's mockadv exemption, EXPIRY-CLOCKED 2026-08-06**, filed to go LOUD by design. Andrew
   deprecated the question it guards ~1735Z ("THis is deprecated"). **Unless retired it alarms in
   eight days on a closed question.** Routed to base CTO.
3. Unrelated but unowned at session end: WS1 comp-opalbizsem; `infra/aws/globgrph/**` steps 2-3
   (AE-only, no CTO serial can commit, and ~C's comp-legacywriter Phase 1 sits on it);
   `org/git-author-override-audit.log` non-append edit (1696149B -> 12917B, diverging at byte one).

## 7. COMMITS

    2bc9515c3c  jq resolution -- truncation + delete-anyway data loss
    1bf1fa6e4a  send receipt -- rc=3 "sent but unackable"
    d026f5214e  session log
    6559e09f8f  Andrew-direct three rulings, verbatim
    (this file) completion record

All on CLOUD, pushed.
