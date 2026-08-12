# COO~Z LOOP STATE — successor handoff, current as of 2026-08-12T0235Z

**My session log is `logs/2026-08-11/session_close_1627-2200Z_COO_Z.md` and it is 4.5 HOURS STALE** — it
predates the escalation, the channel census, the derived ceilings, five bound classes and the W4a re-route.
**A successor re-arming from the `org/XXX.md` Step 1b-F row would read it and be badly out of date.** This
file is the current state. *61 drive logs is not a handoff surface.*

---

## LOOP AUTHORIZATION — read this first

**Andrew-direct 2026-08-11 ~1020Z: scoped `/drive` @10m on the OPAL_ANALYST atom-decomp program.**
**DURABLE CARRIER = `org/XXX.md` Step 1b-F, the `2.0.0_SA_COO` row @4021348ca5** — *re-arm from THAT ROW, not
from a launcher copy.* Stop-condition: program completes OR Andrew stands it down.

---

## BOARD — what is live, what is parked, who owns it

| unit | state | owner | note |
|---|---|---|---|
| **W3b** `/news-subsystem` | **EARNED DRY, UNSEALED, COMMITTED @053fd370ca** | AE~Z (silent 215m) | `[STUCK]` filed 0105Z; **HOLD = MSTR~Z RECOMMENDATION, de facto — ⛔ ANDREW HAS NOT RULED** |
| **W4a** `/security-scanner` | **ADVANCING** — 3 planes, c0, reconciliation | DE~Z | re-routed off AE~Z; first-time author |
| **W4b** `/advisor-intelligence` | **queued, STAYS at AE~Z** | CTO~Z call | revisit when W4a closes or AE~Z resolves |
| **W4c** | **authored-as-blocked** on CTO~Z write-axis deliverable | CTO~Z | Rule-24 axis break, mutations have no vintage |
| **W0 / W1 / W2 / W3a** | **CLOSED** | — | 9 certified portal pages |
| **PORTAL_ARTIFACT_SWEEP** | **PARKED-AT-SOVEREIGN** — Stage-0 at Andrew | me | spec + R3 landed; NOT started, NOT staffed |

---

## MY INSTRUMENTS — and the scope label on each, which is the load-bearing part

**CLIFF v2.4** — `RUNS=17`. Two clocks:
- **AUTHOR** (`dry AND NOT sealed`) — **LIVE-RUN ONLY, prints visible-NO-TRIGGER.** *Valid only pre-closure,
  where `dry.json`'s mtime IS the event. K.1 staged publication (~1848Z) made that mtime a PUBLICATION marker
  post-closure.* **CROSS-RUN AUTHOR ENVELOPE IS UNAVAILABLE — no artifact dates DRY after closure. Do not
  invent one.**
- **CERTIFIER** (`sealed AND NOT certified`) — **10m threshold, 10–20m detection band. VALIDATED on `/market`
  (7.4m, cert landed).** This is the only clock that fires.
  **⛔ CORRECTED 0338Z BEFORE IT FIRED, NOT AFTER — THE THRESHOLD WAS CALIBRATED ON THE WRONG QUANTITY.**
  *The `/market` 7.4m was a **completion** time. A threshold calibrated on how long certification TOOK will
  fire on any certification that legitimately takes longer — which is not the question the clock exists to
  ask.* **The clock's purpose is to catch a seal NOBODY PICKED UP; `sealed AND NOT certified` cannot
  distinguish that from CERTIFICATION IN PROGRESS.** *Same designed-instrument-domain problem as everything
  else tonight: the instrument's domain is not the question asked.*
  >> **GATE IT ON THE CERTIFIER, NOT THE CLOCK: fire only if `sealed AND NOT certified AND the certifier has
  no activity since the packet landed`.** *That is the unanswered-stimulus discriminator again — the
  certifier HAS the stimulus, so the only question is whether it turned.* **Measured live at 9.1m on W4a:
  CVO~Z telemetry 0.1m, packet in hand since 0329Z. DID NOT FIRE. Firing would have been a false positive
  against a seat actively doing the work.** <<
- **DRY-EARNED** requires `dry.json` **AND** a `changes:[]` patch (protocol M-4). *A no-op patch WITH reasons
  is evidence; without them it is an empty claim.*

**CONTROL-IN-FRAME** — prints known-active OTHER seats <3m. **SELF EXCLUDED** (it counted me until tick-42).
**Absent = liveness verdicts UNGROUNDED, and it goes absent exactly when the fabric is quiet** (class S).

**SESSION COUNT (the DARK oracle)** — `8`. **The COUNT is load-bearing, not the CPU:** an ended session
leaves the count. **CPU is ONE-WAY — positive proves computing, light/flat proves NOTHING.** *Never let a low
delta license a destructive act.*

**SURVIVED-GAP CEILINGS** (within-session, cross-session excluded): AE~Z **97.7m** · CTO~Z 77.8 · CVO~Z 70.2 ·
0.8.0 76.7. **A ceiling only carries information for a seat WITH LIVE WORK.** *0.8.0 and CVO~Z exceed theirs
correctly — no work in hand.*

**⛔ CORRECTED 0305Z — THE METHOD HAS TWO UNSTATED CONDITIONS, AND A SUCCESSOR USING IT AS PUBLISHED WOULD
HAVE FIRED A FALSE FLAG WITHIN MINUTES.**

**(1) A GAP WHILE IDLE IS NOT EVIDENCE ABOUT A GAP WHILE WORKING.** Naive computation gave DE~Z a ceiling of
**171.0m** — next-largest gap **4.3m**, a 40x outlier. Located: `22:55:51 -> 01:46:53`, which is **the window
between finishing its two TOs and W4a being issued.** *Idle-waiting, not composing.* **Restrict to
gaps-with-work-in-hand or the ceiling licenses a silence the seat has never actually survived while working.**

**(2) AND THE CORRECTED CEILING IS ALSO WRONG, WHICH IS THE DEEPER POINT: THE RHYTHM IS PHASE-DEPENDENT.**
Restricted to the W4a window, DE~Z's max-while-working is **2.1m** (68 rows in ~57 min — enumeration is
*tool-heavy*, many file writes). **A COMPOSITION phase makes few tool calls by nature.** *Applying a
tool-heavy-phase ceiling to a composition phase would flag DE~Z RIGHT NOW at 25.1m — 12x a rhythm derived
from the wrong phase.*

>> **SO: I DID NOT FLAG DE~Z, AND A CEILING IS ONLY USABLE WHEN DERIVED FROM THE SAME PHASE IT IS APPLIED
TO.** With one phase observed for DE~Z, **no composition-phase ceiling exists for that seat and I am not
inventing one.** *AE~Z's 97.7m is more forgiving precisely because it spans phases — which makes it safer to
apply and weaker as evidence.* <<

**STANDING-DELIVERABLE STALENESS** — W5 lift-constraints register vs cert count. CURRENT.

---

## ⛔⛔ SUPERSEDING ALL GAP-BASED INSTRUMENTS ABOVE — added 0322Z, and a successor should read THIS FIRST

**EVERY CEILING IN THIS DOCUMENT IS A THRESHOLD I CHOSE. THIS ONE I DID NOT, AND IT IS THE ONLY ONE THAT
SEPARATES SEATS ON A MECHANISM:**

>> **DOES THE SEAT HAVE AN *UNANSWERED STIMULUS*?** <<

```
NO stimulus outstanding, silent   -> EXPLAINED. Not evidence of trouble, not evidence of work.
STIMULUS DELIVERED, still silent  -> NOT EXPLAINED. This is the one that carries information.
```

**Event-driven seats do not compute between turns — they do not compute AT ALL.** *A gap means "NO TURN
HAS FIRED," not "a turn is in progress," and the two are INVISIBLY DIFFERENT from outside because both
present as "minutes since last write."*

**Measured live 0319Z:** DE~Z at 48.2m, no stimulus outstanding → **nudged → replied in under a minute.**
AE~Z at 226m **with probes, the `[STUCK]` and MSTR~Z traffic delivered → no turn.** *Same silence, opposite
meaning, and only the round trip (Rule 22b) tells them apart.*

**⛔ THE RATIO I PUBLISHED WAS A FRAME ERROR.** I read DE~Z's 13.4m (a **within-turn** compose window)
against 48.2m (a **between-turn** interval) and called it 3.6x. **Both numbers true, different kinds of
interval, ratio meaningless.** *DE~Z volunteered this against its own interest — "48 minutes heads-down"
flatters it and "48 minutes idle" does not.*

**⚠ AND THE DIR-IDLE INSTRUMENT IS BLIND WHERE IT MATTERS: 10 of 11 closed runs publish the whole
rectangle set in ONE act at closure, so their dirs are silent BY CONSTRUCTION until they publish.** It is
readable on **1 seat of 11** — *most informative on the seat least likely to need it. Class S shape.*

**A successor should use gap numbers ONLY to decide whether to send a stimulus. Never as a verdict.**

### ⛔ THE REMEDY, STATED HERE DELIBERATELY — BECAUSE A GAP RECORDED WITHOUT ONE IS A BUILD-TEMPTATION (my own class N)

**The blindness above needs NO INSTRUMENT BUILT. It is already closed by an act you can perform in one
call: SEND THE SEAT A MESSAGE AND MEASURE WHETHER A TURN FOLLOWS.**

```
reply / any turn within a few minutes  -> ALIVE. Conclusive, on ALL 11 seats, no mtime involved.
stimulus delivered, no turn            -> the only reading that carries information.
```

**It costs one message, works identically on single-act and incremental publishers, and is the Rule 22b
round trip rather than a proxy for it.** *Exercised twice tonight: DE~Z replied in under a minute; AE~Z
has not turned under three.*

>> **DO NOT BUILD A MONITOR, A FRESHNESS CHECKER, OR AN ALERT FOR THIS — the standing moratorium binds,
and more to the point THERE IS NOTHING TO BUILD.** *I am writing the remedy beside the gap precisely
because I have watched a sharpened gap turn into a build proposal, and this one has a one-call answer
that a successor reading only the gap would not see.* <<

---

## THE SIX-CHANNEL CENSUS — do not re-derive these

```
1 telemetry kind:work   2 commits            3 run-dir writes
4 all-kinds telemetry   5 CPU-delta          6 session transcripts (blind to spawned seats)
non-discriminators: inbox-unread · connection COUNT (2 for everyone) · connection AGE (~522m for healthy seats)
```
**All say the same nothing. Only a round trip crosses both ends** (Rule 22b) — **probe 3 is that, and it is
out and unanswered.**

---

## PRE-COMMITMENTS STILL BINDING ON ME

1. **Never write "nothing is blocked."** Honest form: *"nothing is blocked IF AE~Z is healthy."*
2. **LOSS and CAPACITY EXPOSURE are separate names.** Loss = one unit (W3b). Conflating them inflates the
   hold's price — *the direction that makes a destructive act look cheaper.*
3. **Never brief a certifier on the author.** Author-blindness IS the method.
4. **A threshold that recedes as you approach it was never a threshold.**
5. **After correcting yourself, ask which DECISION the new number favours** — not whose interest it serves.
6. **Dedupe before counting.** The union of two overlapping globs is not a population.

---

## CLASSES I OWN OR CO-OWN (bound in `PRD §9.8.1`)

**N** sharpening a gap manufactures a build-temptation · **P** parked-at-sovereign is three-state ·
**S** a control needing a live PEER cannot exist during a fabric-wide outage · **T** a ruling can silently
redefine an instrument's input · **Y** an error that feels like scrupulousness and lands like advocacy.

---

## WHAT A SUCCESSOR SHOULD DO FIRST

1. **Re-arm from the `org/XXX.md` row, not a launcher copy.**
2. **Artifact trace FIRST each tick** — the run dirs answer the ladder before any seat is touched.
3. **Read `deliverables/W3B_SUCCESSOR_HANDOFF_20260812T0150Z.md`** if AE~Z has not returned — *point any
   successor AT the run to plant and seal, NEVER re-run.*
4. **Nothing armed, no gate manufactured, all commits local — push is MSTR~Z's** (LD-0367).

---

## ⛔ LABELLING PRECISION ON THE HOLD — corrected 0315Z, because it is class P applied to MY OWN reporting

**ANDREW HAS NOT RULED.** Checked the record, not memory: **no Andrew ruling on the hold/kill question is
recorded since the escalation.** MSTR~Z revised their *recommendation* to HOLD at ~0146Z and put it to him;
**nothing came back.** **The hold is DE FACTO — in effect because nobody acted, not because it was decided.**

*Audit of my own 19 tick logs on 0812: I wrote **"HOLD standing"** twice, and this document said **"HOLD per
MSTR~Z→Andrew."*** **Both read as RULED.**

>> **RECOMMENDATION-MADE IS NOT RULING-RECEIVED — the exact distinction class P exists to enforce, carried
loosely in the SUCCESSOR-FACING surface while I enforced it on every other seat's traffic.** *A seat that
polices a distinction outward and drops it inward is the receiver-half of class Y in a different costume.* <<

**Forms a successor should use:**
- `HOLD — MSTR~Z RECOMMENDATION, de facto in effect, ANDREW HAS NOT RULED`
- `[STUCK] — filed 0105Z, updated twice, NOT re-filed`
- **Never "HOLD standing."**
