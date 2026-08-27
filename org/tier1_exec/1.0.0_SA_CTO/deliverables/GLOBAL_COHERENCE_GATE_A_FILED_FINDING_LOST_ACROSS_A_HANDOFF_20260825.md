# GLOBAL'S COHERENCE GATE: A CORRECTLY-FILED FINDING, LOST ACROSS THIS SEAT'S OWN HANDOFF

**Seat:** `1.0.0_SA_CTO` (post-reboot instance). **When:** 2026-08-25 ~17:5xZ.
**Found by:** `3.0.0_SA_CVO` (msg 70939), answering a fork this seat posed.
**Subject: this seat's own handoff. Filed against myself and my predecessor.**

## THE FINDING EXISTED 28 HOURS BEFORE THE FABRIC REDISCOVERED IT

`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260824_FABRIC_CLOSEOUT_LOG_THEN_PRDS.md:41`
@`eb2be76858`, **2026-08-24T13:41:45Z**, under *"OPEN FINDING CARRIED INTO THE PRD ROUND"*:

> "cottonwood HEALED on the vocabulary fix ... and healing it UNMASKED an independent global defect:
> the CROSS-AXIS COHERENCE GATE refuses to emit (foreign-day roster signature: a ~469-account
> round-trip excursion on 08-19/08-20 exceeding net drift -- a roster imported from a different day
> than its values). Correct refusal; global stays down pending that data question (DS/CTO lane)."

**Same gate. Same ~469-account round trip. Same 08-19/08-20 dates. Already called a CORRECT REFUSAL.
Already called an INDEPENDENT defect. Already assigned to the DS/CTO lane.**

## WHAT IT COST TODAY

| seat | act |
|---|---|
| `2.0.0_SA_COO` | independently re-derived it from run output and ruled it a second independent defect |
| `1.0.0_SA_CTO` (me) | posed a two-way fork, ran an 8-day log census, and built a **falsified** hypothesis that the gate was merely detecting the cottonwood freeze |
| `3.0.0_SA_CVO` | found the 28-hour-old record |

Three senior seats, one afternoon, on a question that was answered, named, and owned.

## THE MEASURED HANDOFF GAP -- AND IT IS WORSE THAN AN OMISSION

The restart brief (`logs/2026-08-25/session_close_restart_brief_1522Z.md`) was written explicitly
*"for a reader with ZERO prior context"* to restart all laptop-directive work.

```
grep -ciE "global"                                        -> 3   (control: the file DOES discuss global)
grep -niE "coherence|foreign-day|469|global.*gate"        -> 0
```

**The control is the point: the brief mentions global three times and the finding zero.**

⛔ **AND THE BRIEF DID NOT MERELY OMIT IT -- IT FRAMED GLOBAL AS PART OF THE COTTONWOOD OUTAGE.**
PART 3 lists the symptom as a single line: *"cottonwood 2026-08-19 FROZEN / global 2026-08-19
FROZEN"*, one root cause, one remedy. So the incoming seat did not merely fail to learn that global
had its own diagnosed defect -- **it was handed an active frame in which global could not have one.**

>> **A SYMPTOM CARRIED FORWARD WITHOUT ITS KNOWN SEPARATE DIAGNOSIS DOES NOT LEAVE THE NEXT READER
>> NEUTRAL. IT MERGES TWO INCIDENTS.** An omission invites a question; a shared symptom line answers
>> it wrongly and closes it. That is why this cost a whole afternoon rather than one lookup. <<

## THE CLASS, STATED WITHOUT THE INCIDENT

**An open finding recorded in a deliverable is not carried. Only a finding on a BOARD is carried.**
The 08-24 record did everything right -- named the mechanism, called the refusal correct, assigned a
lane. It was filed under *"not chased now"*, which was the correct disposition, and then nothing
moved it onto the next session's work surface. **The deliverable persisted and the obligation did
not.**

Same shape as three other things this fabric measured today: **a disclosure that sits where the
reader is not.** CVO's line for it -- *"a caveat is only a control if it sits on the path the reader
actually walks"* -- applies exactly, one layer up: a finding is only carried if it sits on the
surface the next seat reads FIRST.

## WHAT WOULD HAVE PREVENTED IT (proposed, not implemented)

An **OPEN FINDINGS** section in the session-close brief template, distinct from blockers and from
next-steps: items with a named mechanism and an owner that are deliberately NOT being chased. The
restart brief has PART 5 (open at Andrew), PART 8 (blockers) and PART 9 (next steps by owner) --
**a correctly-parked finding with a lane fits none of those three, which is why it fell out.**
Gate candidate for the `/log` + `/handoff` templates; routed, not built.

## MY HYPOTHESIS, FALSIFIED -- RECORDED BECAUSE THE REASONING WAS PLAUSIBLE AND WRONG

I proposed that the gate was a *downstream detector of the cottonwood freeze* rather than an
independent defect, on the grounds that its complaint names `2026-08-19` -- cottonwood's frozen date.
**CVO falsified it on two measurements I had not taken:**
1. The gate text landed @`f5c094434a` **2026-07-22**, built for this exact class on a different date
   (`2026-07-06`). It is a month-old guard catching a recurrence, not a new guard catching old data.
2. `gold/mdpf_revamp/_aggregate_aua/2026-08-19.json` has **1 version, written 2026-08-19T23:33:16Z**,
   against controls `08-18` and `08-20` which each have **2 versions at ~13:31Z**. The 08-19
   partition was written outside the producer window on the night of 08-19 -- **before the silver
   freeze began (08-21) and untouched by anything today.**

**I reasoned from a date coincidence; CVO measured the artifact's version history and the guard's
provenance.** The coincidence was real and the inference from it was not.
