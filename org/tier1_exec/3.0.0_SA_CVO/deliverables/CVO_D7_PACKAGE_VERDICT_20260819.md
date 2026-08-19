# CVO VERDICT — D7 package (Opal Ticketing Intake Workflow)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D7_TICKETING_INTAKE_PRD.md` @375c874a9e (159 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D7_ATOMDECOMP/run_20260819.md` @375c874a9e (55 lines)

**Verdict: ACCEPT WITH 1 P0 + 2 P1.** The strongest of the two packages read so far. Scan denominators
printed in the run's own section; boundaries state what was NOT done and why; the security finding
(R6) is carried visibly into §7 rather than absorbed; the build is correctly narrowed to ONE primitive
by tool enumeration. The P0 is a check that cannot see its target, not a wrong conclusion.

---

## P0-1 — For CTO. The §6 existence check for the PRD's ONE build is structurally unable to see the artifact it is checking, because the gateway's source is not repo-resident.

§6 TO-B's existence check reads: *"primitive absent from live surface (R8) — genuinely NEW code in an
EXISTING service."* R8's own scope is narrower than that conclusion: it measures *"no group-mailbox/DL
primitive in the **registered tool surface**"* — an **MCP-registration-layer** observation. §4.1 then
places the build at the **EC2 app layer** (`opal-gateway`, `/opt/m365-mcp-gateway`, deployed
S3→SSM). **Those are different layers, and a capability can exist in the app without an MCP tool
exposing it.**

**I tried to resolve it myself and could not — which is the actual finding.** Measured this session:
`comp-find --name "*m365*gateway*"` → **4 hits / 26,859 files, ALL of them docs or change-management
records — zero source files.** `comp-find "groups/|group_mailbox|shared_mailbox|conversations"` over
`infra/aws/ec2` → **MEASURED ZERO over 347 files in scope.** The gateway app is not in the repo.

So protocol §6's three acceptable existence-check forms (`git log -- <path>`, `Read <path>`,
`comp-pipescript io`) **cannot answer this question at all** — they are repo-scoped, and the artifact
is not. D7's tool-surface enumeration was not laziness; it was the only repo-available proxy. But it
is a proxy, and **§6 exists precisely to catch "the file you are about to declare-NEW already exists
in usable form"** (its founding case, ADVI_INFETL.PERFDIM-CREATOR, was exactly that). As performed,
the check cannot catch the failure it was written to catch.

This is Rule 22a's own distinction: reading a staged/registered artifact proves what is THERE, never
what the service actually implements; **applied truth for EC2 code is an on-instance read.**

**Recommend (CTO) — cheap, and it rides a trip already planned:** TO-A already goes to the box via SSM
to read gateway app-permission state (U2). Add one line to TO-A: grep the DEPLOYED gateway app for an
existing group/shared-mailbox read path, and make TO-B's existence check cite THAT result rather than
R8. Same trip, no new leg. It is the difference between *extend* and *duplicate*.

**Honest scoping:** TO-B already gates on TO-A, so the sequencing gives a natural place to catch this
— but only if someone asks the question, and §6 as written does not. I rank it P0 because COO
dispatches TO-B from this §6 and the check is not protocol-conforming.

**Protocol gap worth ruling on separately (you own the protocol):** §6's existence check assumes
repo-resident artifacts. For S3-deployed EC2 services it is inapplicable as written, and the estate
has more of these than this PRD. Recommend a fourth acceptable form: an on-box SSM read.

---

## P1-1 — For CTO. The intake trigger is an agent loop on a box, which is not a schedule — and this is the failure mode that is silent.

§3 specifies *"Polling (EventBridge-less, **agent-loop cadence on the box**) keeps v1 deterministic and
inside the moratorium."*

The moratorium reasoning is correct and I am not challenging it — **no new notification machinery** is
right, and the Teams buzz is Andrew-specified. But *"no alert infrastructure"* and *"what triggers the
producer"* are different questions, and CLAUDE.md rules them oppositely: alerts are banned, while **a
production pipeline MUST have a schedule**, because a producer whose only trigger is another process's
liveness *"freezes silently and invisibly."*

An agent-loop cadence has exactly that shape. **Agent loops die with their session, and the estate's
own record is that nobody notices**: the LD-0367 window clock died with its session on 08-07 and went
unnoticed for three days; `/govern` and the CVO~Z SYSPARITY crons are session-only and expire, which is
why their carrier rows shout about re-arming. Here the payload is **client requests** — if the loop
stops, mail keeps arriving, no ticket is created, and every surface stays green because nothing failed.

**Escalation condition, stated so it is not over-read:** for the **TO-E water test** on one firm's DL,
an agent loop is fine — it is an exercise with a human watching. It becomes **P0 the moment intake is
relied upon**, which is the same instant a client's request depends on it.

**Recommend (CTO):** name the v1 trigger explicitly as exercise-only in §3, and register the
production trigger as a decision owed before reliance (Andrew's own ruling permits event-driven *as an
accelerator* but requires a schedule). **This is a trigger question, not an alarm — do not let the
moratorium answer it**, since reaching for "we'll notice" is precisely the reflex the schedule rule
replaces.

---

## P1-2 — For CTO. Verdict vocabulary: an undeclared value again, AND the D-family has no shared vocabulary across packages.

Two distinct problems, one fix:

1. **In-package:** the run header (`:19-21`) declares **MEASURED / MEASURED-RECORD / INFERRED**. Row 8
   uses **INFERRED-ABSENT** — undeclared. It is clearly an INFERRED subtype and the row is honest, but
   it is the row the entire PRD's one build rests on (see P0-1), so its class matters.
2. **Cross-package:** D2's run calls this class **`MEASURED-AT-RECORD`**; D7's calls it
   **`MEASURED-RECORD`**. Same author, same day, same concept, two spellings — and D2 never declared
   its value at all while D7 did. **There is no shared verdict vocabulary across the D-family**, so
   any downstream reader or tool comparing run rows across packages sees two classes where there is one.

**The fix already exists in your own D7 header, authored the same day** — and it is why this is P1 here
and P0 on D2. D7 states the rule IN the artifact: *"INFERRED (no direct evidence — **cannot carry a TO
expected-value**)."* That single clause is exactly what D2's run lacks. **Recommend: promote D7's
header to the family standard and apply it to all ten runs.** One vocabulary, declared once, with the
expected-value bar stated in-artifact.

---

## Explicit deferrals

- **R6 ticket-API authorization finding** — correctly scoped OUT in §1, carried visibly in §7 Q3, with
  the honest note that v1 stays internal-only so intake does not widen the exposure class. **Standing
  at Andrew since 08-12; not mine to re-adjudicate and not a D7 defect.** Reported here only so it is
  not lost between packages.
- **§5.2 / §5.3 conformance** — both present, dispositions in protocol form (Confirmed/Changed/
  Surfaced). No finding.
- **U1–U4 open items** — properly owned, each routed to TO-A or an Andrew one-liner, none blocking
  authoring. **Conforming, not defects.**
- **"No estate GraphQL implementation" (run denominators, 99 hits all vendored pygments)** — noted as
  relevant to D6, not scored here.

---

## What you should have asked but did not

**Who holds the intake duty when the Analyst is not running — and how would anyone find out?**

§4.2 assigns intake to the Analyst as *"a named ticketing-center manager responsibility,"* and §4.5
puts the SLA log in *"the Analyst's persistent memory + ticket events."* The **receipt** timestamp —
the first of the three SLA legs, and the only one that proves we saw a request at all — exists
**nowhere but the Analyst's own memory** until a ticket is created. The other two legs (claim,
complete) live in the ticket's events array, i.e. in DynamoDB.

So a mail that arrives and is never turned into a ticket leaves **no trace in any durable store**. The
SLA log cannot show it, because the log begins at ticket creation. The DL still holds the mail, but
nothing in the system knows it was owed a ticket. **The one failure the SLA log structurally cannot
measure is the one it exists to prevent** — and it is the same shape as P1-1, one layer up: the
producer's silence is indistinguishable from an empty inbox.

The cheap closure is a cursor, not a monitor (moratorium-safe): §4.1's read is already cursor-based, so
**persist the cursor durably and off-box**, and let receipt-count-vs-tickets-created be derivable after
the fact by anyone who asks. That is a record, not an alarm. Worth deciding before TO-E, because a
water test that passes on one firm's DL will not surface it.

— 3.0.0_SA_CVO
