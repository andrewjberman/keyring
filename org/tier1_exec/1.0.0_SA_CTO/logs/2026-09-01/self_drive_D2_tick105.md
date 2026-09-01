# /self-drive D2 — tick 105

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` (:07/:37) · **UTC:** 2026-09-01 ~07:5xZ
**Ticks covered:** 104–105 (104 was quiet on the register and wrote nothing, per §5)
**Carrier:** `org/XXX.md` line 633 @`e706f59f62` · **Paired:** `/drive` @ `2.0.0_SA_COO`, cron `b8ac5fba`

---

## Scope

```
D2 -> 10 project(s)   device: laptop   open TOs: 22 (unchanged across 103/104/105)
COMPLETION TEST: 2 of 10 complete -> NOT DONE
  UNMEASURED position: OPAL_ADVIPOINTERS (null dep_stage; tick-103 route to the register owner
  has not returned — carried, not re-pitched)
```

## The ruling this tick owed and paid

90937 §5 deferred the emitter/render-path design question **pending a classification the driver did
not have.** That classification landed and the ruling issued at 90976.

### RULED: the question dissolves — neither branch

The call was framed as *either* redesign the render path around 4 leaves *or* rule that 3 more
families must emit. **Neither.** The three families the render path needs were **already designed to
emit and they crash.**

```
UNMET-PRECONDITION  6   FIVE ARE UNHANDLED CRASHES — rc=1, raw traceback, NoSuchKey.
                        No refusal string, no reason, no authority.
                        activity_{rel,acct} · allocation_{rel,acct} · performance_relationship
                    +1  roster_relationship — unmet, NOT the crash class
RULED-REFUSAL       1   transactions_relationship — sovereign deferral, genuinely a design decision
```

**Root cause, read at `perfrp_emit_core.py:113-115` by this seat rather than inherited:** `_read_gold`
interpolates the literal as-of into a partition path and hands it to a direct S3 get, **bypassing the
port's staged aliasing to ask for a partition the port already knows is absent.** No fallback, no
handler — so an absent partition surfaces as an unhandled exception rather than a declared refusal.
**One mechanism, five families.**

**All three leaves the render path is missing are in that crash class**, so one producer fix unblocks
all three empty panels. Lane is DS by rule 13; the implementation is the lane's, not this seat's.

### ⛔ Why the label was dangerous rather than untidy

A crash and a sovereign deferral produced **the same status string**. The manifest showed seven
considered decisions where there was one decision and five bugs. The live branch an hour earlier was
**redesigning an entire render path around four leaves to accommodate five crashes wearing a design
decision's name.**

⭐ **The default did the work, not the judgement.** 90937's rule — *a refusal nobody can cite is an
unmet precondition by default* — resolved five of seven mechanically. **The classification could not
be argued into the flattering answer**, which is the property worth keeping.

## Other verdicts and acts, ticks 104–105

- **Tick 104's systemic call adjudicated (CVO).** REC adopted **with a correction this seat should
  have made**: routing both halves as one architecture finding risked **the immediate half inheriting
  an architecture timeline.** One push fixes the visible symptom; submodule push semantics is a slower
  conversation. Split in the allocation.
- **Mixed-vintage question closed by the consumer, not by this seat.** `AdvisorBookView.tsx:664-667`
  documents the divergence as *deliberate since 08-28* — reconciliation was considered and refused,
  because forcing one as-of "would present two different measurements as one." **The ruling this seat
  was preparing would have ordered a publish to fix something that was designed.**
- **Not ruled, named:** `roster_relationship` is unmet but not a crash, and sits nearest
  `ADVI_ROSTERCOLS`' six unavailable columns. **Nobody has looked.** No connection is inferred from
  adjacency — that inference is what this tick's ruling spent an hour undoing.

## RESERVED cards still at Andrew

- D3's order relative to D8 (the scope limb).
- Whether the flow-ingestion defect widens the ruled 22 (carried from the CVO terminal, not duplicated).

## Instrument finding

**Six broker sends were refused tonight with "body is EMPTY".** Isolated this tick: an identical
message **fails with a printf-style format specifier in the body and succeeds without it.** Content is
lost between the caller and the broker; the broker's guard catches it rather than delivering a blank.
Not a fabric defect — a caller-side hazard for any seat pasting code into a message.

## Compiler Tools

`directives-check.py --json` (scope + completion denominators) · `comp-find` (emitter registry
location; refusal-token census) · direct source reads of `perfrp_emitters.py:43` and
`perfrp_emit_core.py:108-116` · a python completion scan over the 10 member JSONs. No `head` on any
census; every push-state claim by `ls-remote`.

**State:** `ARMED` · next tick on the cron.
