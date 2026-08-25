# ANDREW-DIRECT 2026-08-25 ~00:4xZ — answers to `/open-calls` at `0.4.0_DS_ClientPlatform~F`

**Terminal:** `0.4.0_DS_ClientPlatform~F` (D1_CATVIEWS round-1 DS lane).
**Trigger:** Andrew ran `/open-calls`; this lane returned 4 carried calls. He answered all four.
**Status:** RECORDED VERBATIM + BROADCAST SAME TURN (org/XXX.md law). Surfaced, NOT adjudicated.

## VERBATIM

> 1.) There seems to be some confusion here an "Opal Moderate Income Portfolio" sounds like a
> "Custom" Model, something that would appear in L2 View "Custom Models" Drilldown, where L0 has
> Models, L1 has Custom and Primary, and L2 would show any Custom Models, like that or Opal Fixed
> Income. 2.) Explain Exactly what you need here. 3.) These appear in SmartX for 49 Financial, not
> in Black Diamond or elsewhere; only 49 has "SMAs" category items at this point. 4.) Need more
> clarity on this.

## WHAT EACH ANSWER BINDS (surfaced, not adjudicated)

### (1) — CONFLICTS WITH A STANDING RULING. ROUTED, NOT EXECUTED.
His semantic: **"Opal Moderate Income Portfolio" is a CUSTOM MODEL**, belonging in the L2 "Custom
Models" drilldown alongside **Opal Fixed Income**. He restates the tree: L0 Models → L1
{Primary, Custom} → L2 enumerates the Custom models.

**THE CONFLICT, stated plainly because it moves a client-facing number:** the estate currently
routes that member to the **G8 named NON-MODEL residual**, on the **composition-absent
discriminator** — `fact_model_blend` carries ZERO rows for `fef636c2` as parent or child, so the
Strategy row was ruled not-a-model. It was minted as a model at `@0fa303f91` and **REVERTED the
same hour** (CRO 163744Z, CTO revert word 165357Z), and `build_cottonwood_mdpf_slice.py:147-152`
records that reversal explicitly. `Opal 15/85 Income Portfolio` joined the same set on 2026-08-24
under the same discriminator.

**Dollars at stake (measured, cot, assignment_date 2026-08-24 / value_date 2026-08-19):**
Moderate Income **$6,317,569.87 / 9 accts**; 15/85 **$304,880.53 / 1 acct**. Reclassifying them as
Custom models moves that out of the Client/residual bucket and into `Models > Custom` on a
client-facing view.

⛔ **AND IT LIKELY VINDICATES HIS OWN ESTIMATE.** PRD s.6.5 estimates Cottonwood Custom at **~$7M**.
Measured Custom under the standing ruling is **$0.00**. Under his reading, Custom ≈ **$6.32M** —
which is ~$7M. The hypothesis this lane raised in CALL 1 (that his ~$7M pointed at Moderate Income)
is **corroborated by his own answer to a different call**, arrived at independently.

**NOT EXECUTED HERE.** The composition-absent discriminator is a ruled mechanism with a documented
revert; his word is sovereign and supersedes it if he means it to, but a lane does not overturn a
CRO/CTO ruling on an inferred reading. Routed to CTO/COO with the question stated in one line:
*does his word supersede the composition-absent discriminator for the Income class (both members),
or is "Custom model" his DISPLAY intent for members whose stored class stays non-model?*

### (2) — "Explain Exactly what you need here."
Answered to him this turn: the per-Partner composition rulesets, reduced to the three concrete
things they decide (the 18 Satellite-family strategies, Custom-set completeness, the `global` tree).
No action pending here beyond that answer.

### (3) — ANSWERED, AND IT CORRECTS THIS LANE'S OWN MODEL. ACTIONABLE NOW.
**"These appear in SmartX for 49 Financial, not in Black Diamond or elsewhere; only 49 has 'SMAs'
category items at this point."**

This lane measured that `49financial`'s `by_model` carries `cohort_class='sma'` entries
(**$22,936,012.48**) while `inflection` and `cottonwood` carry none, and modelled the absence as a
**DATA-SOURCE GAP** — `separable: false`, `dollars_located_in: "Client"`. **That is wrong.** His
word says inf and cot **HAVE NO SMAs AT ALL**. The correct state is a TRUE ZERO / no members, not
an unavailable measurement.

**Consequences:**
- The `separable:false` marker is now itself the false frame for inf/cot — it tells a renderer that
  SMA dollars are hiding inside Client when there are none. **To be corrected in this lane.**
- The **inf/cot SMA source gap routed to CTO by COO (67046) is MOOT** — there is no gap and no
  source to find. Withdrawn to CTO by this lane.
- Rule 24(iv) reading is now sharper, not weaker: 49F is `separable`, inf/cot are `no-members` —
  still two states needing different remedies, but the second remedy is "register the truth", not
  "find a source".
- The SMA L1 node set and the crosswalk↔registry identity map (`opal_div_sma`→`divz`,
  `opal_growth_sma`→`pfoe`) are **unaffected and remain correct** — they are 49F-plane facts.

### (4) — "Need more clarity on this."
The third Client fee bucket. Answered to him this turn with the mechanism rather than the label.
No action pending here beyond that answer.

## LAW APPLIED
Record verbatim + broadcast same turn. His word binds the ADDRESSED question and nothing wider — no
gate manufactured, no sibling work held. (1) is routed because it collides with a standing ruling on
a served number; (3) is executed because it corrects this lane's own artifact and creates no
cross-lane hold.

**Author:** `0.4.0_DS_ClientPlatform~F`. **Project:** D1_CATVIEWS, round-1 DS lane.
