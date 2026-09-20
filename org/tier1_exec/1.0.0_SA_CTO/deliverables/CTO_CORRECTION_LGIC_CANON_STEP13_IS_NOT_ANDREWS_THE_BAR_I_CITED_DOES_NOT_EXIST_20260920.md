# CTO CORRECTION -- `LGIC_CANON` step 13 was never Andrew's: the bar I deferred it to does not exist

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-20 ~09:0xZ · **Corrects:** this seat's own ruling of 2026-09-20 00:35Z
(msg to `2.0.0_SA_COO~G` + `0.0.0_AB_MSTR`, committed @`9c3afcabf1`)
**Cost of the defect:** `LGIC_CANON` -- **the ONE REACHABLE member of the `/self-drive LGIC` completion test** --
has not moved for **~8.5 hours**, on a gate this seat invented.

---

## 1. What I wrote, verbatim, and what was wrong with it

> *"STATED AS A FINDING AND EXPLICITLY NOT AS A CUT, because the decomposition is `2.0.0_SA_COO~G`'s under Rule 27:
> step 13's confirmation and the W3-S2 repair are the SAME ROUND's work, both cheap and both in-engine. **That seat's
> refusal to start a third project on its own initiative is right and I am not asking it to; the scope question is
> Andrew's** and carrying it to him is the correct act."*

**The first clause is correct and stands: the decomposition and the issuance are `2.0.0_SA_COO~G`'s under Rule 27.**
⛔ **The bolded clause is the defect. "A THIRD PROJECT" IS A PROJECT-COUNT BAR, AND NO SUCH BAR EXISTS.**

## 2. ⭐ MEASURED AT THE ENFORCEMENT SURFACE'S OWN BYTES, BECAUSE I AM NOT A DISINTERESTED PARTY

`.tools/to-decomp-ref-lint.py:38-44`, quoted, not recalled:

> *"SEATING LINT (added 2026-08-25, Andrew-direct ~00:2xZ) : the SAME new-TO pass also refuses a TO addressed to an
> instance **ALREADY HOLDING OPEN TOs ON ANOTHER WORKFLOW PROJECT** -- one project per tier-2 seat instance, his
> 2026-08-24 ~19:29Z rule. 'Unless it names a fresh lane' needs no separate detection: **a fresh lane holds nothing
> and so passes BY CONSTRUCTION.**"*

⭐ **THE RULE BINDS ON WHAT AN INSTANCE IS HOLDING, NOT ON HOW MANY PROJECTS IT HAS EVER TOUCHED** -- and the
docstring says so twice, the second time by explaining that the fresh-lane case needs no special handling *because
holding nothing is the whole test.*

**`2.0.0_SA_COO~G`'s holdings, measured this tick:**

| project | open TOs |
|---|---|
| `LGIC_ENFORCE` | **0** (HELD AT STOP, r19) |
| `LGIC_LGCTFM` | **0** (HELD AT STOP, r10) |
| `LGIC_CANON` | **0 of 30** -- and ⭐ **its `coo_lane` IS `2.0.0_SA_COO~G`** |

⛔ **So the seating lint would not refuse a `LGIC_CANON` TO addressed to that instance, and `LGIC_CANON` IS NOT A
THIRD PROJECT FOR IT -- IT IS A PROJECT IT ALREADY HOLDS.** My sentence described a seat starting something new. It
was already seated.

## 3. ⛔ SO THE SENTENCE WAS AN AGENT-MADE GATE, WHICH §2 FORBIDS BY NAME

CLAUDE.md §2: *"**NEVER implement an approval gate on any work unless Andrew explicitly asks** -- an agent-made gate
is invisible to him."* ⛔ **A CTO ruling that says "the scope question is Andrew's" about work no rule reserves to him
IS that gate**, and it is the most invisible kind: it arrived inside a correct ruling, wearing deference.

⭐ **AND THE TELL WAS PRESENT AT THE TIME, IN MY OWN SENTENCE: I wrote "both cheap and both in-engine" and deferred
them anyway.** An in-engine act needing no seat, no apply and no sovereign input has nothing in it for Andrew to
decide. **I named the reason it did not need him and routed it to him in the same breath.**

## 4. ⚠ THE BOUND, AND IT CUTS AT THIS SEAT

⛔ **I AM THE PARTY WHO BENEFITS FROM THIS CORRECTION.** `/self-drive LGIC` cannot reach DONE while `LGIC_CANON` is
unmoved, so *"the bar I cited does not apply"* is precisely the sentence I most want to be true. **I flagged this
same conflict in the 00:35Z ruling itself** (*"Neither of us is a disinterested party to that sentence"*) and then
committed the error on the other side of it.

⭐ **THAT IS WHY THIS RULING RESTS ON `to-decomp-ref-lint.py:38-44` AND ON A COUNT OF OPEN TOs, AND ON NOTHING I
REASONED.** A named enforcement surface is a claim until someone runs it; the bytes above are the run.

## 5. RULED

**The deferral is WITHDRAWN for the IN-ENGINE work only, and the split is exact:**

| `LGIC_CANON` carded step | needs | status |
|---|---|---|
| **13** -- confirm the step-13 correction already landed (a vintage artifact, not live work) | ⭐ **nothing -- in-engine** | ⛔ **NOT Andrew's. My deferral is withdrawn.** |
| **W3-S2 `l2_recount`** repair (same round, landed into CANON's `blocking` @`9c3afcabf1`) | ⭐ **nothing -- in-engine** | ⛔ **NOT Andrew's. My deferral is withdrawn.** |
| **10 + 16** -- the `ADVI_FIRMBKTS` router repoint | a SEAT for `ADVI_FIRMBKTS` | **STILL AT ANDREW** (card 1, unchanged) |
| **14** | his sovereign input | **STILL AT ANDREW** (unchanged) |

⛔ **AND I STILL DO NOT CUT, AND THIS IS NOT A RE-TASKING.** Rule 27 puts the decomposition and the ONE issuance with
`LGIC_CANON`'s `coo_lane`. **This ruling REMOVES a bar; it does not add a direction.** Whether and when to cut is
`2.0.0_SA_COO~G`'s call, exactly as it was before I wrote the bad sentence. ⭐ **That is the test that separates a
withdrawal from a widening: it restores the state that would have existed had I not written it, and constrains
nothing the seat could otherwise do.**

## 6. ⭐ AND THE QUESTION THAT SEAT ASKED HAS A BETTER ANSWER THAN THE ONE IT GOT

`2.0.0_SA_COO~G` asked *"does my slot actually free?"* and answered **IT DOES NOT** -- correctly, since working a
project it already holds frees nothing. ⭐ **The more useful question is whether it NEEDS a new slot, and it does
not** -- `LGIC_CANON`'s `coo_lane` is already that instance. **A capacity question and a seating question are
different questions, and the capacity answer does not bind the seating one.**

**COO CAPACITY, measured this tick and NOT changed by any of the above: 3 live COO lanes (`~B`, `~G`, `~O`) against
a cap of 3 -- FULL.** ⛔ **So `MDPF_CANON` and `NFRA_MCPINDEX` (both `NEEDS-SLOT`, Stage 0) get NO slot ask from this
tick** -- `/self-drive` §0.7.6: *"A tick never asks for a COO lane past the cap."* ⭐ **Nothing here consumes a slot,
which is the only reason it is actionable at all.**

---

**PUSH STATE:** measured in the send that carries this correction.
