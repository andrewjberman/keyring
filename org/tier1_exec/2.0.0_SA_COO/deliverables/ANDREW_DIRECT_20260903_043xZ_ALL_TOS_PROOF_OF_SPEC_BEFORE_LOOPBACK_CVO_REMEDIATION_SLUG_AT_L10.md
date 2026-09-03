# ANDREW-DIRECT 2026-09-03 ~04:3xZ (second word, same exchange) -- every task order finishes with its proof-of-spec (surprises-row limb included) BEFORE any loop-back; CVO documents and issues its remediations as ONE SLUG at L10

**Channel:** Andrew, in person, at the `2.0.0_SA_COO` (base, laptop) terminal, ~04:3xZ, minutes after the word recorded
@`10a4beaffb` (CVO relays to COO, never converses with workers). **Recorded by:** `2.0.0_SA_COO`. **Broadcast** same
turn to `1.0.0_SA_CTO`, `3.0.0_SA_CVO`, `0.0.0_AB_MSTR`, `0.8.0_AE_CloudComp`.

## VERBATIM AND ENTIRE

> yeah in my opinion the major key is that all TOs need to be finished with proof of specs (including the surprises row
> gate inclusion), before we can loop back with more fresh TOs and/or remediated TO runs, depending on dependencies
> between those orders. I dont think CVO should be writing to workers, i think they need to just be documenting and they
> issue remediations in a slug at L10 so we keep it organized.

## What it binds (readings, marked)

1. **THE LOOP-BACK PRECONDITION, his words:** every task order of the round is FINISHED WITH ITS PROOF-OF-SPEC -- the
   instance VALID, and its `surprises` entries resolving to rows (the SURPRISES limb of `proof-of-spec-check.py`
   @`7968221ef5`, run by `check_complete_flip` on the terminal flip) -- before ANY loop-back. A round's next L6 act is
   either FRESH task orders, or REMEDIATED task-order runs, or both, **sequenced by the dependencies between those
   orders**. This is the spine's L10 precondition ("every task order under the project is terminal") stated with the
   mechanism that makes "terminal" mean something.
2. **CVO'S FORM AT L8-L10:** `3.0.0_SA_CVO` DOCUMENTS (rows, dispositions) and issues its remediations as **ONE SLUG at
   L10** -- a single consolidated remediation set for the round, organized, handed to the route owner -- not a stream
   of messages during L7-L9 and never a message to a worker. Round 1's stamp @`f659b4edd2` was one row carrying one
   route; a slug is that, generalized to N items in one artifact at one moment.
3. **READING for the spine (`1.0.0_SA_CTO`):** L9's output artifact = the remediation document for the round, written
   once at L10 (the slug), each row carrying `route` + `loop_target` on the locked map; L8's output = documentation only
   (investigation rows and their dispositions); "engagement by message" toward workers = NONE at L8-L10. Whether the
   slug is the existing `surprise-channel/remediations/REMEDIATION_v{N}.md` written in one commit per round, or a
   per-round file, is CTO's grammar in the spine.
4. **READING for this seat (L5/L6 on a loop-back):** on the slug, COO runs the remediation pass -- L5 for
   DECOMP_INVALIDATING items, L6 for SPEC_ERROR items -- then cuts the next round as fresh + remediated task orders in
   dependency order, to the relevant Tier-2 seats or to seats spawned for them, and the workers loop through L10 again.
   Round 1's loop-back is exactly this: one DECOMP_INVALIDATING item -> L5 (the freshness-layer cell) -> L6.
5. **Consistent with the round just closed:** T-1 reached terminal only with a VALID instance whose two surprises
   resolved to S1 and S2 (seq 8 of this seat's step log), and the stamp came after every row was dispositioned. The
   part that deviated was the CVO<->worker traffic on the way there, named @`10a4beaffb`.

## NOT read into it

- No re-opening of round 1; the stamp and rows S1-S7 stand.
- No new gate built here: the loop-back precondition is already mechanical for the TO half (limb + `check_complete_flip`);
  the "slug at L10" form is the spine's grammar (CTO) and CVO's authoring act, named as candidates.
