# ANDREW-DIRECT 2026-08-25 ~15:55Z -- SPRING CLEAN: systematic close-out of old projects/TOs under a dormancy/superseded tag

**Channel:** CTO terminal, direct to `1.0.0_SA_CTO`, mid-turn during the /directives-check state assessment.
**Recorded by:** `1.0.0_SA_CTO`. **Broadcast:** COO + MSTR, same turn (record+broadcast law).

## VERBATIM

> "Yeah we may need to do a little spring cleaning here and take this as an opportunity to
> systematically start closing out old projects/TOs with some kind of tag that signifies that it was
> closed for dormancy/potentially superseded but regardless irrelevant now."

## The preceding instruction in the same exchange (~15:47Z), also verbatim

> "What we want to do here is assess current state /directives-check and correspond with various
> underlying projects, maybe need to build out the directives-check skill to tie those in harder if
> it does not already, then figure out if we need to adjust/expand any PRDs/project registrations,
> then figure out how to sequence this work and what agents need to be brought online to handle. I
> will bring on COO now so they can get started up while you figure this out, then once you have
> more clarity on how to sequence this, relay that to them and they can issue spawn requests to MSTR
> and we pick up there."

## SCOPE -- surfaced, NOT adjudicated

He said "spring cleaning", "old projects/TOs", "some kind of tag", "closed for dormancy/potentially
superseded but regardless irrelevant now." He did NOT name a threshold, a tag vocabulary, or a
population. Those are open and are carded back to him rather than inferred -- per the no-inferred-
scope law, the breadth of his word is his to set.

## WHAT THE RECEIVING SEAT MEASURED BEFORE PROPOSING ANYTHING (all live, this turn)

1. **Rule 25's ratified 90-day dormancy bar authorizes closing ZERO projects today.** 0 of 111
   active/scoping projects are >=90d. Oldest is `YALP_YCUTVR` at 68d. Two independent age signals
   (last commit touching the project JSON; last commit subject naming the code) agree at 0.
   Checked for a bulk clock-reset that could manufacture this: the only commit touching >=15 project
   JSONs is `44c6925b35` (2026-05-22), three months old, and it was itself a dormancy close-out.
2. **The status axis is already a Rule-24 violation:** 17 distinct status strings over 333 project
   JSONs. The HOLD concept alone carries four spellings (`inactive` 6, `on-hold` 3, `on_hold` 2,
   `suspended-indefinite` 1). STATE (`active`/`complete`) and DISPOSITION (`merged`/`cancelled`/
   `complete-as-superseded`/`deprecated`) are fused on one axis -- postulate (iii). One value,
   `superseded-into-OPAL_TAXONOMY`, encodes its successor INSIDE the value -- postulate (ii) grain.
3. **The estate already has the procedure and most of the vocabulary.** `44c6925b35` (2026-05-22,
   COO, Andrew-approved) closed 17 dormant projects via a documented **3-step atomic close**
   (JSON status+completed+phase+blocking -> REGISTRY row move -> PRD Status-line update) under three
   dispositions: CLOSE-COMPLETE (13), CLOSE-SUPERSEDED (4, each naming its successor), ON-HOLD (2).
   The missing value is a true DORMANT-no-successor close. Build-ladder rung 2 applies: extend the
   existing vocabulary, do not mint an 18th string beside it.
4. **A naive close-out predicate would destroy live work.** "active + zero open TOs + member of no
   directive" = 47 projects, but 12 of them are <14d old and 8 are <=5d (`OPAL_KIMIPIPELINE` 0d,
   `DATA_PIPMAP` 0d, `MDPF_PROVCANON` 1d) -- freshly minted and pre-decomp, not dormant. Age and
   TO-count measure different things and the two populations take OPPOSITE remedies (Rule 24(iv)).

## THE OPEN CALLS THIS GENERATES (carded to Andrew, not decided here)

- **The bar.** Rule 25 says 90d and yields zero. This sweep needs either a declared shorter bar for
  a one-time pass, or a per-project judgment act. His call, because a threshold that closes work is
  a sovereign act, not a tooling default.
- **Whether DORMANT-closed is reversible** and under whose word it reopens.
- **Retro-tagging volume** (already open from 2026-08-24): all orphans now, or as-touched.

## BINDING NOTES

- **Rule 25 stands: DORMANT IS NOT A DELETION WARRANT.** This is a status flip plus a registry move.
  Nothing is deleted, no served key moves.
- **Rule 25's successor check binds every close:** dormant-because-ABANDONED and dormant-because-
  SUPERSEDED are byte-identical from age alone and take opposite actions. Andrew's own phrasing
  ("dormancy/potentially superseded") already names both -- the tag must DISTINGUISH them, not fuse
  them, or it reproduces the exact defect Rule 24 postulate (iii) prohibits.
- **Rule 24 binds the tag itself.** Any new value on the status axis is a schema-enumeration act and
  arrives with the four-postulate test plus a token-hygiene census, or it is not a proposal.
