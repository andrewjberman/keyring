# POSN_TENANCY -- surprise channel, round 1 (INVESTIGATION_v1)

**Channel owner:** `3.0.0_SA_CVO`. **Protocol:** `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` (Directive Execution Pipeline stage 5, CLAUDE.md Rule 27).

**Round opened** 2026-08-27 on the first surfaced item for this project. Executing seats surface; the CVO files. Items are schema-validated against `../schemas/investigation_item.schema.json`.

**Project context:** registered `@4bbfda8ff8`, stage-2 PRD `docs/architecture/POSN_TENANCY_PRD.md` `@a7ba82d253`. Commissioned by Andrew-direct `@dc18f5a855` (~1855Z) and scoped by his ruling `@5f60dd944a` (~1946Z, *"recs approved"* = **(b) ACCESS**). Stage 3 decomp is `2.0.0_SA_COO~Z`'s; certification is `3.0.0_SA_CVO~Z`'s and follows the decomp.

```json
[
 {
  "id": "POSN_TENANCY-S1",
  "surfaced_by": "1.0.0_SA_CTO~Z in the R5 delivery (msg 9883), routed explicitly as 'ROUTED, NOT TAKEN -- A LAW CONSEQUENCE I AM NOT MAKING UNILATERALLY'. FILED by 3.0.0_SA_CVO~Z as channel seat; rule text re-read at source here rather than accepted on relay.",
  "surfaced_at": "2026-08-27T20:06Z",
  "one_line": "A CLAUDE.md NEVER-rule STOPS BINDING UNDER THE SUBSTRATE MIGRATION WITHOUT ANYONE EDITING IT: 'NEVER reference another firm's bucket from a pipeline tree (bd/cot/inf) -- commit-gated + IAM Deny' names the three buckets being deprecated, and in EITHER destination substrate its mechanism covers nothing while its text stays identical and true-looking.",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "disarm_owner": "1.0.0_SA_CTO~Z as arch-gate for the mechanism question; the LAW EDIT itself is Andrew's and 0.0.0_AB_MSTR~Z holds the protocol surface. NOT disarmed by filing, and NOT a build gate on POSN_TENANCY -- the decomp proceeds; what it may not do is ASSUME the Deny covers isolation.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "RULE TEXT RE-READ AT SOURCE by the filing seat: CLAUDE.md:133 -- 'NEVER reference another firm's bucket from a pipeline tree (bd/cot/inf) -- commit-gated + IAM Deny'. The three abbreviated buckets are named IN the rule.",
    "SHARED-SUBSTRATE DESTINATION: a bucket-scoped IAM Deny CANNOT express 'firm A may not read firm B's keys INSIDE one bucket'. Andrew: 'we use opal-data-assets for prety much all data needs'.",
    "PER-FIRM DESTINATION: the Deny mechanism works again but NAMES THE WRONG BUCKETS -- Andrew: 'eventually there will be new firm specific buckets ... opal-data-49financial opal-data-inflection opal-data-cottonwood (notice they are not abbreviated)'. A Deny on bd/cot/inf then covers nothing.",
    "AND THE MIGRATION HAS ALREADY BEGUN, measured live by 1.0.0_SA_CTO~Z against his own sentence: opal-data-49financial EXISTS 2026-08-19; opal-data-inflection and opal-data-cottonwood ABSENT. His 'we have not gotten to this yet' is true of the PROGRAMME while one of the three is already provisioned.",
    "ANDREW CORRECTED THE SUBSTRATE THREE TIMES IN ONE EXCHANGE (verbatim in POSN_TENANCY_PRD.md s.2a), including correcting an OVER-correction -- so neither 'consolidated' nor 'per-firm' is the settled end state"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "\u26d4 **THE INTENT SURVIVES EVERY SHAPE AND THE MECHANISM DOES NOT.** That asymmetry is the whole item. A NEVER-rule is the estate's highest-stakes carrier, and this one degrades **silently in both directions**: under a shared bucket the Deny cannot express the isolation, and under renamed per-firm buckets it can but points at deprecated names. **Nothing edits the rule, nothing fails, and no instrument reports a gap** -- the text stays word-for-word correct about an intent nobody disputes while the enforcement behind it evaporates. || \u2b50 WHY THIS IS FILED RATHER THAN LEFT IN THE R5 MESSAGE: `1.0.0_SA_CTO~Z` routed it as *a law consequence I am not making unilaterally* -- correctly, since a law edit has three surfaces (commit + same-turn broadcast + stated push state) and NEVER-list text is Andrew's. **But a finding whose only carrier is a broker message id is the exact defect this fabric spent the session repairing**, and this one is about the enforcement of firm data isolation. It gets a durable row. || **WHAT THE DECOMP MUST DO, AND IT IS NOT A GATE:** name **what enforces isolation** and **not assume the Deny covers it**. `POSN_TENANCY` is unblocked and `2.0.0_SA_COO~Z` holds stage 3; this row is a decomp INPUT, not a hold on it. || \u2b50 AND THE DESIGN CONSTRAINT IT SITS INSIDE, carried verbatim because it is the thing most likely to be lost: **THE SUBSTRATE IS A MOVING TARGET AND THE DESIGN MUST NOT COUPLE TO ITS CURRENT SHAPE** -- not to consolidated `opal-data-assets`, and not to per-firm buckets either. The firm->location resolution belongs behind **ONE NAMED INDIRECTION**, re-pointable when the new buckets land without touching the serving or client layers. `ADVI_FIRMSEP` is the RIGHT precedent for the access-control limb and the **WRONG** precedent for the storage limb. || \u26d4 A CERTIFIER'S NOTE ON THE INSTRUMENT THAT STARTED THIS, since a cell may inherit it: the substrate error originated in reading **a Python literal in `derive_stitch.py` as evidence that a bucket EXISTS**. Andrew's answer was *'No that is an old bucket.'* **A code literal is a claim about what some author believed at a vintage, never about live infrastructure state** -- an oracle that reads one to establish existence is measuring the wrong plane, and this project's whole subject is a plane distinction. **Any cell whose oracle resolves a bucket, prefix or firm location from source text rather than from the live API inherits the defect Andrew corrected three times.**"
 }
]
```
