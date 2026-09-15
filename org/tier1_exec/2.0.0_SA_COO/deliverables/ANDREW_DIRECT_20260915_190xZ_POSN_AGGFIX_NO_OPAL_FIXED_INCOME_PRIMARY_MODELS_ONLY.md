# ANDREW-DIRECT 2026-09-15 ~19:0xZ -- at 2.0.0_SA_COO~Z: POSN_AGGFIX does not need Opal Fixed Income; only the Primary Models (UST ST INT LT ULT) are of interest

**Received at:** the `2.0.0_SA_COO~Z` terminal (site Z), in-session, two messages a few minutes apart, while POSN_AGGFIX round 1 was
EXECUTING (issuance `ed1db8f1db`). **Recorded by:** `2.0.0_SA_COO~Z`, the same turn. Clock: the first arrived before 19:03:08Z (a
`date -u` read in the same turn), the second just after.

## VERBATIM AND ENTIRE

> "We do not need Opal Fixed Income for any of this, please note that."

> "We are only interested in the Primary Models , that is UST ST INT LT and ULT."

## WHAT WAS MEASURED BESIDE IT (context for the reader, not a ruling)

- `s3://opal-data-portal-v2/platinum/mdpf/global/aum-metrics.json` (VersionId `OVcFBOpgjFywfYJGYjowX2VSVwLdiyez`, period 2026-09-14)
  `by_model` carries 7 rows: Ultra Short-Term, Short-Term, Intermediate, Long-Term Conservative, Long-Term Aggressive, Opal Blend 5050 Int
  Ltc, Opal Blend 5050 St Int. **Opal Fixed Income is not one of them.**
- `git grep -i "opal[ _-]?fixed[ _-]?income" HEAD` over `data/mdpf`, `org/standards`, the POSN_AGGFIX tree and the positioning producer
  (192 files): 11 hits, all in the MDPF gold layer -- `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py:140` (`opal_fixed_income`,
  id-less, cohort `model`, added 2026-08-26 for Cottonwood), `:217-231`; `dim_mdpf_aggregate_aua_timeseries.py:127-140, :2477`
  ("10 = 5 core + 2 sma[49F] + 2 blends[inflection] + opal_fixed_income[cottonwood]"); a test fixture. So Opal Fixed Income is a model the
  gold fold counts; whether its assets are the 8,324,465.16 gap between the served `by_model` rows and `total.model_aum` is UNMEASURED here
  and is exactly what `TO-A1-1`'s A1-AC1 measures.

## WHAT IT RULES -- READ NARROWLY, AND THE ONE QUESTION IT OPENS

- **Opal Fixed Income: NOT NEEDED for POSN_AGGFIX.** It is not a member of the aggregate, no cell needs it, and no cell chases it. Where it
  surfaces (the gap explanation, a `left_out` list, a census), it is reported as outside the project and nothing more. This is consistent
  with PRD v0.2 C-MEMBERS as written (primary models and blends of primary models only), so it changes no order.
- **"Only interested in the Primary Models, that is UST ST INT LT and ULT":** read narrowly, the aggregate is the five primary models'
  book. **This seat does NOT adjudicate whether it also removes the two 50/50 blends.** Andrew's own word at ~17:0xZ (record
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_170xZ_POSN_AGGFIX_L2_ANSWERS_DONE_WHEN_D4_FULL_FLOW.md`) was
  *"f) yes blends count but only of primary models UST ST INT LT ULT"*, and the confirmed FWD-6 reads "Every primary model's money counts in
  the aggregate, blends included". Two readings are open:
  - (a) blends of the five primary models still count through them (today's C-MEMBERS; this message restates the member set);
  - (b) blends are dropped and the aggregate is the five primary models' own assets only (FWD-6's "blends included" and C-MEMBERS would
    change: a PRD bump by `1.0.0_SA_CTO~Z`, the ratified-text half re-signed by `3.0.0_SA_CVO~Z`, the standard
    `org/standards/POSN_AGGREGATE_MODEL_SET.json` changed).
  The question goes back to Andrew in plain words. It is his call.

## WHAT THIS SEAT DOES WITH IT, AND WHAT IT DOES NOT

- **Holds its OWN hand-off of `TO-A2-1`** (the order that implements the membership and the weights) until Andrew picks (a) or (b). That is
  this seat's sequencing inside its own limb, not a gate on any other seat.
- **Does NOT stop** `TO-A1-1` (read-only; its blend census stays useful either way), `TO-C1-1` (the edge refusal does not depend on
  membership) or `TO-B1-1` (the page reads whatever aggregate block the producer serves).
- **Does NOT edit** the PRD, the standard or any issued order: under (b) the PRD bump is `1.0.0_SA_CTO~Z`'s, and the recut is this seat's at
  the round analysis.

## BROADCAST

One message to `1.0.0_SA_CTO~Z`, `0.0.0_AB_MSTR~Z` and `3.0.0_SA_CVO~Z`, quoting both sentences entire. Push state: LOCAL.
