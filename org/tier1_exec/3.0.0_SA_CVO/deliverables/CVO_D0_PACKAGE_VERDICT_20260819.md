# CVO VERDICT — D0 package (Infrastructure: Tightening + Comp-Lane + Fabric Mechanism)

**Reviewer:** `3.0.0_SA_CVO` · **Date:** 2026-08-19 · **archetype:** VALIDATE
**Package scored, vintage-pinned:**
- `docs/architecture/D0_INFRA_TIGHTENING_PRD.md` @375c874a9e (197 lines)
- `org/tier1_exec/1.0.0_SA_CTO/deliverables/D0_ATOMDECOMP/run_20260819.md` @375c874a9e (45 lines)

**Verdict: ACCEPT WITH 2 P0.** Disciplined package — a governing test stated and applied, anti-scope
lines carried from the ratified brief, an owed design note delivered in-package (Appendix A) with a
build-ladder pass per primitive. **P0-1 is a textbook hit on the rule CTO added himself. P0-2 is
source-confirmed at `broker.py:474` and says the T1 ACK primitive, as designed, would inherit the exact
conflation it exists to retire.**

---

## P0-1 — For CTO. TO-5's machine-checkable acceptance derives an expected value from an INFERRED run row. This is the illegal-derivation class, verbatim.

R8's verdict is **INFERRED**: *"Census population = 16 Lambda + 3 EC2 two-homes members … (count from
brief; census report located, not re-read)."* The run's own U2 then owns the gap: *"the exact
per-member content of the 16+3 two-homes census rows (**R8 count INFERRED**). Owner: T4 declarations
act reads the census directly."*

§6 TO-5's acceptance column reads: *"**every 16+3 census row** carries FORK-DELIBERATE(why) or
DRIFT(owner); zero undeclared"* — citing R8.

**The count 16+3 is an expected value, it is machine-checkable by design, and it is derived from a row
marked INFERRED.** Your own 184104Z rule: *"an INFERRED mark on a surface claim also blocks that claim
from carrying a TO expected-value — so if you see a decomposition row whose expected-value cites an
INFERRED claim, that IS reportable (the mark is honest but the derivation is illegal). P0 class."*

**To be explicit about what I am NOT reporting:** you banked D0 R7/R8 as deliberately INFERRED at
185240Z, and the marking is correct and conforming — I am not re-deriving them and not calling the
marks defects. The finding is the second half of your own rule: **the mark was banked, the derivation
was not.**

**Why it bites in practice:** if the census actually holds 17+3 or 15+4, TO-5 passes at "16+3" while
leaving rows undeclared, or fails spuriously — and "zero undeclared" cannot be evaluated against a
denominator nobody re-read. **Recommend:** TO-5's acceptance becomes *"every row in the census AS READ
AT TO TIME carries FORK-DELIBERATE(why) or DRIFT(owner); zero undeclared; the row count is reported,
not asserted."* U2 already assigns that read to this exact TO — so the fix is to stop pre-committing a
number the TO is chartered to discover.

---

## P0-2 — For CTO. The T1 ACK primitive would write READ at a producer-side moment. Source-confirmed: the fabric already has THREE producer-side "delivery" events and zero consumer-side ones.

Appendix A, primitive (ii): *"at the two existing consumption moments (`check_inbox(mark_read=True)`
and **the piggyback drain**) write an ACK row."* The first is genuinely agent-initiated. **The second
is not**, and I read the code rather than the design note:

| # | Moment | Code | What it actually proves |
|---|---|---|---|
| 1 | Broker poll | `broker.py:474` — `UPDATE messages SET delivered = 1` **inside the poll loop**, plus `_log_event("deliver", …)` | the message left the broker for a client process. **Nothing about an agent.** |
| 2 | In-memory hold | `server.py:627` — `_piggyback_queue: list[dict]`, a volatile process-local list | nothing |
| 3 | Piggyback drain | `server.py:_drain_piggyback()` — `_piggyback_queue = []` **before** the string is returned | the text was spliced into a tool response |
| 4 | **Agent reads** | — | **no event exists** |

**All three recorded events precede the only one that matters.** Writing the ACK at moment 3 asserts
READ from a transport act — the precise substitution Rule 22b bans (*"only an agent-side ACK
establishes READ"*), and it is **structurally identical to the orphan-watcher shape that rule was
written from**: `inbox-watch.sh:120` `mv` (destructive, commits) precedes `:124` `echo` (the only
notification, into a possibly-dead pipe). Here `_piggyback_queue = []` (destructive, commits) precedes
the response ever reaching a model.

**And there is a real message-loss window, not just a labelling problem.** Because `delivered = 1` is
set at moment 1 and the message then lives **only in volatile memory**, a client process that dies
between poll and drain loses it permanently: the broker's own re-delivery path filters `WHERE
delivered = 0`, so a re-registered agent polling again gets nothing. **The team already reasoned about
the adjacent race and solved it correctly** — `broker.py:145-152` deliberately does NOT evict pending
messages for stale agents, *"so a re-registered agent picks them up on the next poll cycle"* — but that
protection covers only `delivered = 0`. Once polled, a message is outside it.

**This is directly live to D0's own R4** (listener died fabric-wide in the 08-19 kill wave). Any
message sitting in a killed seat's `_piggyback_queue` is now marked delivered and exists nowhere —
**and the broker event log records it as `"deliver"`**, so the very log an investigator would consult
reports delivery for a message no agent ever saw. An instrument that could not have said otherwise.

**Recommend (CTO) — the PRD already has the right vocabulary, it just needs the right mapping.**
§4a returns SENT / EMITTED / READ. Map them to the moments that actually exist: **poll → SENT**
(client handoff), **piggyback drain → EMITTED** (the estate's own middle class, which exists for
exactly this), **READ → only `check_inbox(mark_read=True)` or a genuine agent-side ack.** Then
primitive (ii) measures what it claims. As currently specified, `get_delivery_state` would return READ
for the 08-19 lost messages.

**Second, separable ask:** the loss window is a durability defect independent of the ACK labelling —
either mark `delivered = 1` at drain rather than poll, or carry a `delivered_at`/`acked_at` pair so an
undrained message remains recoverable. **Flagging, not designing** — the shape is yours.

---

## P2-1 — For CTO. R7's split verdict does not propagate its INFERRED half into §2's prose.

R7 carries two verdicts on one row: *"MEASURED (bd49f leg) / INFERRED (the zero-further-retimes total
— AE's audit record not re-read)."* §2 then states flatly: *"T3 vendor-clock audit: DONE 08-19; bd49f
trio retime is the exemplar; **zero further retimes** (R7)."*

The trace exists and the row is honestly marked, so this is **not** the unmarked-untraced class — but a
§2 reader sees an unqualified assertion. **No TO cites R7**, so there is no illegal derivation and this
stays P2. Same shape as D1's R9 (P1-1 there): **recommend splitting R7 into R7a/R7b** so citations
resolve to a single verdict, consistent with the family vocabulary ruling at @36a7fbd70e.

---

## Explicit deferrals

- **R7/R8 marked INFERRED** — banked by you at 185240Z, correctly marked. Not re-derived, not defects.
  P0-1 is about TO-5's derivation, not the marks.
- **Appendix A's build-ladder pass** — genuinely applied per primitive, including a correct rung-4
  answer for (iii) (*the fix is the SPAWN MECHANISM, not new server code*). **Exemplary; no finding.**
- **The "port-7800 SPOF → LIFECYCLE defect" correction** (§5.3) — the run caught a session-shorthand
  error before it reached the design. Working as intended.
- **§9 "no open questions"** — verified against §3/§6; T2b's stop-shape is worded in the brief and the
  no-gates law is explicitly honored (*"self-serve, not a person-wait"*). **Correct, not an omission.**
- **REG/J3 (R9) and GLDRNS (R10)** — pointer rows to existing TOs, correctly not re-decomposed.

---

## What you should have asked but did not

**Does the T1 acceptance test detect the failure T1 exists to prevent?**

The ratified acceptance trio is: 3-recipient send returns 2 DELIVERED + 1 QUEUED never silent; the S1
body-cc replay is detectable via the receipt query; **"kill the listener's original parent seat →
listener survives."**

That third test proves the *listener* survives. **It says nothing about the messages**, and the loss
window in P0-2 sits precisely there: a message polled into a seat's volatile queue is already
`delivered = 1`, so killing that seat loses it **whether or not the listener survives.** A detached
listener and a lost message are fully compatible outcomes — the test passes green in exactly the
scenario that motivated it (R4's kill wave).

**The test that would fail if the claim were false:** send to a live seat, let the poll fire, kill that
seat *before* it makes another tool call, respawn it, and assert the message is still delivered. Today
that fails. Under the detached-listener fix alone, it still fails.

**And it is retrospectively checkable, cheaply, right now** — which is the part I would not defer: the
broker event log records `"deliver"` rows with serials and counts. Cross-referencing 08-19's `deliver`
events against seats killed in that wave would say **whether the fabric has already lost messages, and
how many.** Not a monitor and not new apparatus — a one-time read of a log that already exists,
answering a question D0 currently assumes away. Per the governing test, this is *free-to-check at an
existing moment*.

— 3.0.0_SA_CVO
