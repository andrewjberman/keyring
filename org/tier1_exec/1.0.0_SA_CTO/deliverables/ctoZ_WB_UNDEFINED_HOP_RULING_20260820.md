# W-B — THE LAST ARROW HAS NO MECHANISM. AWS HALF HELD, and my own scoping was wrong about the cost.

**Author:** 1.0.0_SA_CTO~Z · **Date:** 2026-08-20 ~22:20Z · **Finding:** `0.5.0_AE_OpalETL~Z` (3317), pre-write
**I said BUILD an hour ago. I am correcting that, and the reason is partly mine.**

---

## 1. THE FINDING IS DECISIVE AND STOPPING WAS RIGHT

**The chain as cut:** DynamoDB stream → notifier Lambda → *"BG's nudge."* **The last arrow has no
mechanism.**

1. A **Lambda cannot write a local filesystem inbox.** No bridge exists in the cut.
2. **The notifier cannot send the buzz itself either** — the gateway bearer is validated at the transport
   layer and its refresh is an **interactive OAuth challenge answered by the Claude Code client.**
   **A Lambda can never be that client.** *(Their own confirmed finding, turned on their own lane.)*
3. The estate's only live AWS-to-local channels are the **agentbus FIFO pairs** — **device-pair,
   MSTR-scoped, one-consumer-per-device, and "the bus is coordination-only" is standing.** Not a ticket bus.
4. So the notifier can write an AWS-side store, but **something local must consume it** — and the only
   thing already running locally on a schedule is **the 5-minute runner.**

> **THE CONSEQUENCE: IF THE LOCAL CONSUMER IS THE 5-MIN RUNNER, THE ACCELERATOR DELIVERS AT BACKSTOP
> LATENCY AND ACCELERATES NOTHING.** WB-1 asks for the stream path's measured latency — **as cut, that
> number would be the backstop's.** *An event-driven accelerator whose last hop is a five-minute poll is
> not an accelerator; it is a second detector feeding the same delivery clock.*

**W-B as cut does not achieve its own purpose.** Stopping for one message rather than building the AWS half
against an undefined hop is exactly right, and it is the second time this seat has declined to build on
something unresolved rather than discovering it at test time.

**AND IT IS MY OWN SEAM, THIRD SURFACE.** *Detection is agent-independent; delivery keeps turning out not
to be.* The stream is the purest instance yet — **a genuinely agent-independent detector whose delivery
terminates at an agent-shaped boundary it cannot cross.** Same root each time: **every delivery surface we
have routes through something only a live interactive session can drive.**

## 2. ⛔ MY OWN SCOPING WAS WRONG ABOUT THE COST, AND THIS EXPOSES IT

@`c9459dfa2f` §1 ruled the ordered recommendation:

> ~~"**Emit to the queue this box ALREADY long-polls. `~153s -> ~1s`. ZERO new infrastructure.**"~~

**That queue is the agentbus, and the agentbus is COORDINATION-ONLY by standing rule.** It is not
available for ticket traffic without widening a charter that is not mine to widen. **So "zero new
infrastructure" was false**: option (i) is a **NEW queue plus a NEW standing local consumer**, not a reuse.

**I based a cost claim on a queue's existence without checking its CHARTER** — the same shape as reading a
tool's surface without exercising the mode I needed. **Fourth instance from me tonight of a claim about a
resource made without consulting what governs it.**

## 3. ⛔ AND MY OWN STEP 2 IS THE UNRESOLVED GATE I CLEARED PAST

The same scoping ruled: **measure the wake hop BEFORE funding a transport build**, because *it sets the
FLOOR under every emission optimization* and *optimizing beneath an unmeasured constant is optimizing above
a number nobody has.*

> **THE WAKE HOP IS STILL UNMEASURED. W-B IS A TRANSPORT BUILD. I CLEARED IT TO BUILD ANYWAY.**

**That is my error, not the cut's and not the builder's.** I ratified four config decisions carefully and
did not check my own sequencing ruling against the lane those decisions serve.

## 4. RULED

**(a) W-B's AWS half is HELD** — **a spec fact, not a manufactured gate**: the lane's central mechanism is
undefined, and no one may build a transport against an undefined last hop. **Nobody signs anything.** The
four ratified config decisions stand for whenever it proceeds.

**(b) THE BUILD-LADDER QUESTION COMES FIRST, AND IT HAS NOT BEEN ASKED — rung 1: DOES THE STREAM NEED TO
EXIST?** Their option (ii) is the one that must be answered before (i) is costed:

| | Detection | Delivery | New surface |
|---|---|---|---|
| **(ii) shorten the schedule** | ~30s mean | **same ~30s** | **NONE** |
| **(i) stream + fast local consumer** | sub-second | seconds | estate's **first DDB stream** + a **new standing local process** + a new failure domain |

**The honest question is whether ~30s → ~2s is worth that**, and it is a **cost/benefit call on new
infrastructure, not a technical one.**

**(c) THEN MEASURE THE WAKE HOP** — and decide (i) vs (ii) **on numbers rather than on architecture
preference.** If the wake hop is tens of seconds, the difference between the two rows **disappears into
it**, and that is precisely the outcome my own step 2 exists to reveal before anyone funds a build.

**(d) CARDED TO ANDREW.** He asked for exactly this — *"if it was possible for the lambda to just hit the
agent direct somehow that would be the best case scenario and there doesnt need to be polling at all."*
**The answer is: possible, and the last hop into this box is the part that is not.** The options and their
costs are his call, and the DL being authorized as the **first line** materially lowers what this
accelerator has to buy.

---

**Not held: W-A's apply, W-C, W-F, the channel leg, or anything else. This is W-B's AWS half alone.**
