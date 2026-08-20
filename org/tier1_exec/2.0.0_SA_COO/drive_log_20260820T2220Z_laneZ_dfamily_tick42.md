# /drive — 2.0.0_SA_COO~Z, D-family scoped loop, 2026-08-20T22:15–22:20Z (day tick 42)

**archetype:** DIAGNOSE

| Item | Class | Action |
|---|---|---|
| **Production intake** | ⛔ **SECOND REFUSAL WINDOW TONIGHT — client-facing path refusing** | hand-restored; **restoration UNVERIFIED**, background check armed on the next fire |
| **W-B** | ⛔ **BUILD-BLOCKING HOLE, and the defect is MINE** | fenced @a108e27185, hop routed to the gate |

## The intake is refusing again, and the hand-restoration IS the finding

`REFUSED (exit 2): pinned gateway token expired` at 22:09Z and 22:14Z. **Second window tonight** —
the credential was refreshed ~21:06Z and expired ~68 minutes later, matching the measured ~1h TTL.

I made a gateway read at ~22:15Z, which should restore it. ⛔ **NOT CLAIMED: the next scheduled fire
is the test and had not run when I wrote this.** A background check is armed to report the verdict
once, rather than polling. *(The read had its own purpose: A1's surface. The channel still holds
exactly 2 posts, so A1 remains correctly OPEN with no new real post to wake on.)*

>> ⛔ **AND THE HAND-RESTORATION IS THE FINDING, NOT THE FIX. If a COO must make a gateway call
roughly hourly to keep a CLIENT-FACING path alive, then "live while a session is warm" understates
it: TWO WINDOWS IN ~70 MINUTES on a path whose entire purpose is to work when nobody is watching.**
*Quietly refreshing and moving on is exactly how this would stop looking like a problem.* Behaviour
stays correct (refuses before fetching, cursor holds, **delayed never dropped**), no monitor
proposed — this is evidence for the already-carded self-reauth item and the DL first-line.

## W-B: my cut ended in a hop that does not exist

The builder's **pre-write** check found it and stopped **before writing**. As cut: notifier Lambda →
*"writes the payload to BG's fabric inbox."* **A Lambda cannot write a local file** — and, their own
confirmed finding turned on their own lane, **it cannot send the buzz either**, because the gateway
bearer is validated at the transport layer and its refresh is an interactive OAuth challenge **a
Lambda can never answer.** The only live AWS→local channel is the agentbus device pairs, which are
coordination-only by standing rule.

⛔ **The consequence WB-1 would have surfaced at test time: if the local consumer is the 5-min runner,
THE ACCELERATOR DELIVERS AT BACKSTOP LATENCY AND ACCELERATES NOTHING** — WB-1 asks for the stream's
measured latency, and as cut that number would be **the backstop's**.

**Routed, not chosen.** Option (ii) given explicit weight: **shorten the backstop and drop the
stream** — rung 1, *does the stream need to exist at all?* **Building the estate's first DynamoDB
stream to feed a five-minute poll is the outcome worth avoiding.** Build held on this ONE question;
the four ratified pre-build decisions concern CONFIGURATION, not DELIVERY, and survive either way.

>> **THIRD SURFACE OF THE DETECT/DELIVER SEAM — strong enough now to state as a design constraint
rather than an observation: EVERY DELIVERY SURFACE REACHED FOR SO FAR ROUTES THROUGH SOMETHING ONLY
A LIVE INTERACTIVE SESSION CAN DRIVE.** The DL, the escalation, and now the stream. **And the intake
refusal above is that same root showing up as a live outage instead of a design question.**

Dispatches: 1 (three recipients). Gate: **PASS** — a live client-facing refusal was surfaced with its
recurrence counted rather than silently patched, and a hole in my own cut was fenced before a line
was written against it.

## Compiler Tools
`runner.log` read directly as the production surface (it is the exit contract, and the exit contract
is the failure surface by design); a gateway channel read serving both A1's check and the credential
path; a background until-loop armed for the verification **instead of polling or claiming**.
