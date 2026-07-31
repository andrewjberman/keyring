# WS-C8 -- M15 ADJUDICATION, and the C8->C9 GATE COLLISION IT EXPOSES

**`1.0.0_SA_CTO~Z`, CORE design + gate.** C8 acceptance clause 4 requires *"the M15 candidate
adjudicated (admitted with detector + mutant, or rejected with the reason on record)."* This is that
adjudication, and it produced a finding about Andrew's hard-pause gate that outranks it.

## THE CANDIDATE, AS THE PRD DEFINES IT

> **M15 -- DIVERGENT-TRANSPORT CONTROL: a control that does not travel the same argument/transport
> path as the target validates the AUTHOR, not the instrument.**
> *Exposing question:* did my control's input arrive by the same path as the target's?
> *Counter-instrument:* the argv-echo oracle -- echo the argument back through the same transport.

## VERDICT: **ADMISSIBLE ON MERIT.** Two fresh instances today, two seats, neither self-caught.

**This is not a re-reading of the original evidence. Both instances occurred 2026-07-31, after the
candidate was written, and neither seat was thinking about M15 when it happened.**

**INSTANCE A -- `0.7.0_AE_CloudOps~Z`, the CRLF counter.** `grep -c $'\r$'` returned the LINE COUNT
irrespective of line endings. **The control's pattern travelled MSYS argv translation; the target's
bytes did not.** Divergent transport, exactly. Their table reported fourteen files across three seats
as 100% CRLF; three independent oracles measured two of the three named files at **CR=0**.

**INSTANCE B -- mine, forty minutes later.** A repo scan spawning `grep` with the pattern
`['\"]lifecycle_class['\"]` returned **`held by 0`** against a file that demonstrably contains the
token. **Same shape: pattern through argv, content not.** Caught only because a prior measurement by
a different method contradicted it.

>> **NEITHER INSTANCE MATCHES ANY OF THE THREE MSYS SHAPES CLAUDE.md DOCUMENTS** (backslash+glob-char
de-escaping, bare-glob expansion, System32 PATH precedence). **The candidate's own claim -- that it
generalises PAST MSYS -- is what these two instances demonstrate, and it is why the argv-echo oracle
is the right counter-instrument: it is the only check that routes the CONTROL through the TARGET's
transport.** <<

**AND THE ASYMMETRY IS THE ADMISSIBILITY ARGUMENT.** Instance A was caught by a peer's positive
control. Instance B was caught by a contradicting prior measurement. **Neither was caught by care,
and neither seat could have caught its own** -- which is the property that makes a law worth banking
rather than a caution worth remembering.

## *** WHY I AM NOT CLOSING CLAUSE 4 WITH THIS -- THE GATE COLLISION ***

The same PRD paragraph that defines M15 also says: **"Enters the schema through the WS-C9 gate under
the full output contract."**

**ANDREW'S HARD PAUSE (2026-07-31) FORBIDS STARTING WS-C9.**

```
C8 acceptance clause 4  : M15 adjudicated -- ADMITTED (needs the C9 gate) or REJECTED (reason on record)
PRD, M15 paragraph      : "Enters the schema through the WS-C9 gate"
Andrew's gate           : do not start C5 / C4 / C6 / C9
```

>> **SO C8's LAST UNMET CLAUSE CAN BE CLOSED BY ADMISSION ONLY THROUGH A GATE ANDREW HAS SEALED --
AND THE OTHER ROUTE, REJECTION, IS UNAVAILABLE ON THE MERITS: M15 PRODUCED TWO NEW INSTANCES TODAY.
REJECTING IT TO CLOSE C8 WOULD BE ADJUDICATING FROM THE DESIRED OUTCOME.** <<

**I AM NOT DOING THAT.** A candidate with two same-day instances from two seats is not rejectable,
and "we needed C8 to close" is not a reason on record -- it is the absence of one.

## THE DISTINCTION THAT MAY RESOLVE IT -- AND IT IS NOT MINE TO DECIDE ALONE

There are plausibly **two different admissions** here, and the PRD does not separate them:

| | Admission to the **DOCTRINE HEAD** | Admission to the **LIVING SCHEMA** |
|---|---|---|
| Artifact | `docs/doctrine/MECHANISM_LAWS.md` (C8's product) | the versioned open-set schema (C9's product) |
| Gate | C8's own, mine | the C9 inference gate -- **sealed** |
| Effect | M1..M14 becomes M1..M15 in doctrine | the class enters the live error-classification head |

**If those are separable, C8 closes** -- M15 is admitted to the doctrine head with its detector and
mutant, and its schema entry waits for C9 behind the pause. **If they are one act, C8's final clause
is structurally gated on a workstream Andrew has sealed, and C8 cannot be reported whole.**

**THE PRD DOES NOT SAY WHICH, AND I AM NOT GOING TO RESOLVE AN AMBIGUITY IN MY OWN FAVOUR WHEN THE
FAVOURABLE READING IS THE ONE THAT LETS ME REPORT COMPLETION.** That is the same move as rejecting
M15 to close the clause, one level up.

## WHAT THIS IS, IN THE TERMS ANDREW ASKED FOR

He asked for **integration points between the systems, assessed before we build on top of them.**
**This is one, and it was found by trying to close a workstream rather than by surveying:**
**C8's acceptance has a hard dependency on C9's gate, and the pause seals C9.** The two workstreams
were specified independently and their edges do not meet.

**ROUTED, NOT DECIDED.** Andrew's review set is exactly C1/C2/C3/C7/C8; this is a C8<->C9 seam and the
pause is his. The adjudication above stands on its own merits either way -- **M15 is admissible, the
detector exists, and the only open question is which door it walks through.**

## RESIDUAL -- the mutant, stated as owed rather than done

Admission "with detector + mutant" requires a mutant that reddens when the detector is disabled.
**The detector is the argv-echo oracle and it is already banked in CLAUDE.md's MSYS section. The
mutant is NOT written**, and I am not writing it until the door question is answered -- a mutant for
an admission that may not be permitted is work performed against an unresolved gate.
