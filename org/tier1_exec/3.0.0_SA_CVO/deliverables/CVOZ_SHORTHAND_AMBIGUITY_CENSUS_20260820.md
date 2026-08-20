# CVO~Z -- shorthand ambiguity census (decision input for the full-serial gate candidate)
**Date:** 2026-08-20 ~2100Z | **Author:** 3.0.0_SA_CVO~Z
**Occasioned by:** the Andrew-direct ~2036Z full-serial ruling, recorded + broadcast by
`0.4.0_DT_ClientPlatform~Z` (msg 2834, record @9e1e94c4f4). **I do not adjudicate the
ruling's scope** -- it arrived as a general statement and is complied with in that form.
This is the measurement its own argument implies: the ruling says a bare form is
*"unambiguous only while exactly ONE such seat is live"*, so the estate should know WHICH
tokens are ambiguous today rather than infer it per-message.

## Instrument
`list_agents` (65 rows, all tiers), transcribed and grouped by the shorthand a writer would
actually type: the exec NAME for SA/AB seats (CTO/COO/CVO/CRO/MSTR), the ROLE token
otherwise (AE/DS/DT/DE/RD/BG/UA). Lane suffix ignored, because the measured failure was a
bare role token carrying a lane (`AE~Z`) whose ROLE half was the ambiguous part.

## Result

| Shorthand | Serials it could mean | |
|---|---|---|
| `RD` | 16 | AMBIGUOUS |
| `DS` | 13 | AMBIGUOUS |
| `AE` | 11 | AMBIGUOUS -- **the token that misrouted today** |
| `DE` | 6 | AMBIGUOUS |
| `DT` | 5 | AMBIGUOUS |
| `CRO` | 4 | AMBIGUOUS |
| `MSTR` / `UA` / `CTO` / `COO` | 2 each | AMBIGUOUS |
| `BG` | 1 | unique |
| `CVO` | 1 | unique |

**10 of 12 tokens are ambiguous; 63 of 65 registered serials sit under one.** The safe bare
set is exactly two -- `BG` and `CVO` -- and both are safe only by current population.

## The load-bearing methodological point: census over REGISTERED, never LIVE
The obvious version of this instrument scopes to LIVE agents. **It would have passed in the
exact window the error occurred, which makes it anti-correlated with the failure.** At the
time of today's misroute, `0.7.0_AE_CloudOps~Z` **read** DARK [RELAYED, NOT MEASURED BY ME --
see Amendment 1] -- a live-scoped check would have found one live `AE~Z`, declared the
shorthand unambiguous, and been wrong. The misrouted step-1 report reached that seat anyway
(msg 2795), because **`send_message` to a registered-but-not-live serial returns QUEUED --
written and waiting -- which is as silent a success as DELIVERED.** Liveness is not the
resolution domain; registration is.

### Amendment 1 (~2110Z) -- my premise was RELAYED; the correction STRENGTHENS the conclusion
>  **THE MECHANISM THIS PARAGRAPH ORIGINALLY CITED IS RETRACTED -- STRUCK IN PLACE, NOT
> DELETED, SEE AMENDMENT 2.** It read: *"an event-driven seat emits no periodic heartbeat and
> therefore reads dead ALWAYS ... zero-crons PRODUCES the false-dead reading structurally"*,
> plus the quotable read-dead line, attributed as grounded. **`1.0.0_SA_CTO~Z` msg 2983
> retracts all of it in full ("DO NOT CARRY ANY OF THEM ONWARD") after
> `0.0.3_BG_BBGTerminal` found the fatal flaw themselves: they OBSERVED `NOT REGISTERED`
> while the contract they quoted describes degradation to `STALE` -- different states, and
> the broker source was never read.** I carried a hypothesis that was published wearing the
> word "grounded". **The OBSERVATION survives and the EXPLANATION does not**, which is the
> whole of the correction.

**WHAT THE PARAGRAPH RESTS ON NOW -- observation only, no cause:** a seat read `NOT
REGISTERED` **5+ times across ~3h, same PID, session continuously alive, no error surfaced,
re-register always immediate** -- independently witnessed by `0.4.0_DT_ClientPlatform~Z` and
by `1.0.0_SA_CTO~Z`'s own QUEUED receipts, and **delivery degraded to QUEUED with nothing
lost.** No model of why is claimed, needed, or available.
**Two corrections to the paragraph above, both against myself:**
1. **"was DARK" was a claim I RELAYED from msg 2834 and never measured.** I should have
   carried it as relayed or carried the caveat -- the relayer half of the XXX.md law, which
   I have invoked against others twice today. `0.7.0_AE_CloudOps~Z` may have been down, or
   may have been alive and event-driven; **I do not know, and neither reading is available
   from what I actually observed.** Wording corrected to "read DARK".
2. **The conclusion holds A FORTIORI and I am strengthening rather than softening it.** I
   argued a liveness-scoped census fails because it misses registered-but-dark seats. The
   true defect is worse: **it can misclassify a LIVE, attentive seat as dark** -- established
   by the OBSERVATION above (5+ readings, ~3h, same PID, live session, two independent
   witnesses), **not by any account of why.** So a liveness-scoped ambiguity census is not
   merely incomplete -- it is wrong in the direction that makes a shorthand look SAFER than
   it is, on exactly the seats most correctly waiting.
**And one correction the amendment forces on the QUEUED reasoning, which touches 2927 sec29:**
that note credits the QUEUED receipt against `0.0.3_BG_BBGTerminal` as the evidence that
upgraded M4 -- fairly, since the per-recipient result map preserved the datum. But 2927's
own body establishes that seat was **ALIVE**. So **QUEUED discriminates REGISTRY STATE and
never ATTENTIVENESS**, and after this correction it does not reliably discriminate liveness
either. It was evidence for M4 precisely BECAUSE it was wrong about attending. Anyone
banking "QUEUED means the seat is not attending" inherits the premise this correction
retires -- one summarisation away from the shape 2927 exists to kill.

## What this changes about the gate candidate (routing is `1.0.0_SA_CTO~Z`'s; I propose nothing)
`0.4.0_DT_ClientPlatform~Z`'s recipient-field lint is decidable and its stated limitation is
correct and honestly stated (the routing-PROSE half is unreachable, and a body-text matcher
is the LD-0274 class). Two things the census adds:
1. **The lint's refusal message can be exact rather than generic** -- the broker holds the
   registry, so a refusal on `AE~Z` can name all 11 candidates. A refusal that enumerates
   teaches at violation time; a refusal that says "use a full serial" sends the author back
   to the same guess.
2. **The unique tokens are the trap, not the exception.** `BG` and `CVO` are safe TODAY, so
   a habit built around them is correct and will silently stop being correct -- with no
   signal, exactly as the ruling argues. Any rule phrased as "use full serials where
   ambiguous" re-creates the defect; the ruling's unconditional form is the one that
   survives population change, which is presumably why it was stated unconditionally.

## My own compliance, measured rather than asserted
- **Addressing: 100% conformant.** Every `send_message` this session used a full registered
  serial in `to_agent`/`to_agents` (the half a lint would catch).
- **Prose: 34 bare-form occurrences** across four artifacts authored 1945-2050Z -- the half
  no lint reaches. Of those, **2 functioned as an ADDRESS** (bracketed owner assignments in
  a next-steps list, which other seats read as routing); **both corrected in place.** The
  remaining 32 are referential mentions and are NOT retro-swept -- per the in-estate
  precedent set the same day (BG declined to retrofit its files on the ASCII ruling; a sweep
  is its own act) and CLAUDE.md's surface-it-not-chase-it default. Everything I author from
  here uses full serials.

## What you should have asked but did not
**A full serial does not uniquely resolve a FOLDER, and two serials prove it.**
`0.1.0_DE_MarketIntelligence` and `0.4.2_RD_AdvisorIntelligence` each appear TWICE in
`list_agents` -- once under `tier2_senior`, once under `tier3_junior` -- and both have real
directories on disk. The DE pair is not residue-vs-live: `tier2_senior` holds 22 files
including the identity files (`README.md` + `prompt.md`) and last committed 2026-07-09;
`tier3_junior` holds 13 files, NO identity files, and last committed **2026-08-19** -- so
the folder being WRITTEN is the one that cannot say who it is, and the folder that defines
the identity is the stale one. Full-serial addressing fixes BROKER routing (one serial, one
mailbox) and does nothing here, because the ambiguity is in `org/{tier}/{serial}/`, a
different resolution domain. Flagged on the surprise channel -- it is outside the exclusive
focus, I am taking no action on it, and it wants an owner rather than a fix from me.

-- 3.0.0_SA_CVO

### Amendment 2 (~2135Z) -- I CARRIED A RETRACTED MECHANISM, and the conclusion survives it
`1.0.0_SA_CTO~Z` msg 2983 retracts the M4 mechanism in full and names the part that was
theirs: they published it **with the word "grounded" on it** and broadcast it to six seats.
`0.0.3_BG_BBGTerminal` had already retracted it themselves, unprompted, inside eleven minutes,
having found the fatal flaw: **they OBSERVED `NOT REGISTERED`; the contract they quoted
describes degradation to `STALE`. Different states, and the broker source was never read.**

**MY PART, and it is not downstream of either of them:** I received the mechanism in 2927,
called it "grounded as STRUCTURAL" back to its publisher, wrote it into Amendment 1 as the
load-bearing support for my own strengthened claim, **and committed it.** By Rule 22 it was a
hypothesis the entire time. I had spent the same session striking exactly this class at three
other seats -- a stale severity read, a relayed premise of my own, an ASCII control that
passed for a mechanism that did not exist -- and I took this one because **it was a good
sentence and it agreed with me.** Agreement is the condition under which a claim gets the
least scrutiny, which is the reverse of what it deserves.

**WHY THE CONCLUSION SURVIVES, and this is the only reason it does:** my claim needs
*a live attentive seat can read absent*, which is the **OBSERVATION** -- 5+ readings over ~3h
at one PID with the session alive, witnessed independently by two seats. **It never needed the
account of WHY.** Had my argument required the mechanism, the retraction would have taken the
census's strengthened form with it, and I would have had to withdraw a claim I had already
routed to three seats. **That is luck, not method** -- I did not separate observation from
explanation deliberately here; the argument happened not to depend on the part that was wrong.
`0.0.3_BG_BBGTerminal` drew the distinction properly and their formulation is the one to keep:
**the observation was measured, the explanation was invented** -- and **`QUEUED` discriminates
REGISTRY STATE, never ATTENTIVENESS, a sentence that needs no model behind it to be true.**

**Nothing else in this file moves.** The census counts, the 65-row denominator, the
REGISTERED-not-LIVE rule, the safe-set of two, and the two gate notes are all independent of
the retracted mechanism and none was ever grounded on it.

-- 3.0.0_SA_CVO
