# PRD REVIEW -- DSGN_REBRND v0.9 @928a3df671 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96709 (19:27:29Z).

**Prior:** v0.8 was SIGNED, review @54cc53f2a1 and stamp @ec7b02d3f9.

**Read, UTC 2026-09-14, after 19:27Z:**
- The PRD @`928a3df671`, the one commit on the path since v0.8, diffed against it section by section. The DesignContract row was also diffed character by character.
- `1.0.0_SA_CTO`'s round-1 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_DSGN_REBRND_ROUND1_20260914.md` @928a3df671, section 2 (RULINGS A and V).
- Row W1-S20 on `feature/d13-visual-elevation`.
- Andrew-direct 96712 (~19:0xZ, recorded @7c7fbe30f3).

**Half hash:** the notifier's `fd2484178259`. The stamp is bound with `--expect-half-hash`.

## VERDICT: SIGN -- the two text changes are verbatim to the CTO's two rulings

## THE DIFF OF THIS HALF, v0.8 -> v0.9

- **ENDPOINT, FWD-4 (RULING A):**
  - DONE WHEN: "ONE PERSISTENT primary action" becomes "AT MOST ONE PERSISTENT primary action -- none on a view that has no primary action".
  - ACCEPT gains "on any screen that has an action ... and a screen without one carries no accent posing as an action".
  - PROOF: "one primary action per view" becomes "at most one"; "the primary action visible" becomes "... where the view has one"; "the persistent ACTION count stays one" becomes "does not rise".
- **ENDPOINT, FWD-8 (RULING V):** the PROOF's census reads one charting library "with the word cloud (TopicCloud, `@visx`) as its one named exception, its reason in the contract". The CONSTRAINT names it as the case its own clause describes: "it has no axis, tick or legend to share, and the incumbent library draws no word cloud".
- **CONTRACTS, the `DesignContract` row (RULING A):** "one PERSISTENT primary-action emphasis per view" becomes "at most one ... (none on a view with no primary action)".
- Nothing else in ENDPOINT or CONTRACTS moved. MEASURED and the preamble are byte-unchanged from v0.8.

## FIDELITY TO THE RULINGS

- **RULING A** (the analysis, section 2): *"A view with no primary action (/positioning, /market) spends the accent on no action, and that meets FWD-4. What FWD-4 forbids is a SECOND action accent, not a view without one."* The text says exactly this, in all three FWD-4 clauses and in CONTRACTS.
  - W1-S20 shows why: on /positioning and /market "every accent fill ... was a state control", so there was no action to accent.
  - Round 1's 0/1/0 persistent-action reading is therefore compliant under the ruling. It is not a FAIL recast as a PASS.
- **RULING V:** the text names the exception where FWD-8's own CONSTRAINT says it must be named, and does not leave it quiet. It gives the reason, and the census still counts one library plus one named case.

## NOTES (non-blocking)

- **NA -- the cap admits zero on a view that HAS a primary action.**
  - Read literally, "AT MOST ONE" is met by a view that has a primary action and puts no accent on it.
  - Brief O4 (`:62`) says the view "spends its accent colour on the one primary action".
  - The ruling, in its own words, forbids only a second action accent, and ACCEPT still requires "the one thing that is clearly the action" on a screen that has one. So the text is faithful to the ruling, and the choice is the CTO's to make.
  - If the zero case on an action view is not intended, one phrase closes it at the next bump: *"exactly one on a view that has a primary action, none on a view that has none"*.
- **NB -- Andrew's ~19:0xZ word (96712) postdates this text and bears on the next addendum, not on this stamp.**
  - He confirmed /market pass 1.
  - He ruled tooltips one look ("solid indigo no outlines"). That answers the question FWD-12's CONSTRAINT holds open, and is consistent with its single tooltip role.
  - He restored the Fear & Greed chart's original gradient on /market. That sets R4/R5's ramp aside for that chart by his word, and FWD-3 will need to name it, as FWD-8 now names the word cloud.
- **NC -- the grade pattern:** the analysis records `^[A-Za-z0-9]+-(AC|J)[0-9]+R?$`, which remedies LGIC_NAMING-C-S10 and DSGN_REBRND-C-S14. This seat reads that as done in the CTO's lane, and will measure it at the next grade commit.
- **N3 and N4 carry.**

## NOT CLAIMED

- **The brief half.** It is `2.0.0_SA_COO~D`'s.
- **Any grade of the round-1 outcomes.** Those are the CTO's, in the analysis.
