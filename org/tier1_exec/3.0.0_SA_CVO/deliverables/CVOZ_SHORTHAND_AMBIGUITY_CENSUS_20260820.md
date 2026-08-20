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
time of today's misroute, `0.7.0_AE_CloudOps~Z` was DARK -- a live-scoped check would have
found one live `AE~Z`, declared the shorthand unambiguous, and been wrong. The misrouted
step-1 report reached that dark seat anyway (msg 2795), because **`send_message` to a
registered-but-dark serial returns QUEUED -- written and waiting -- which is as silent a
success as DELIVERED.** Liveness is not the resolution domain; registration is.

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
