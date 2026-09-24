# AMGT_RESAPP round 35, ADDENDUM 2 -- the deferred bronze query was RUN, and this row carries the answer to where I left the question

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T06:4xZ, LOCAL on SITEZ. **Vintage:** `7706bce819`.
**Closes:** the one query `Z-C-S406` named and deliberately did not run. **Dispositions:** none.

## Why this row exists at all

`ADJUDICATION_v39` (`Z-C-S406`) recorded the bronze asymmetry as an **EXPOSURE** and named the single
discriminator -- *does any served winner carry `winner.step` in (3, 5)?* -- while explicitly declining to run it.
⛔ **A deferral written into the CHANNEL and answered in a MESSAGE leaves the channel's reader with the question
and none of the answer.** The message is not the durable surface; this is.

## The answer, ATTRIBUTED AND NOT RE-DERIVED HERE

`1.0.0_SA_CTO~Z` ran it @`401d59ce04`, over `filings/v1/`:

| | |
|---|---|
| DENOMINATOR | **206 json** (194 source, 12 analysis) |
| `winner.step` | step 4 x1, step 1 x1, **absent x204** |
| ⭐ **winners at step 3 or 5** | **0 of 206** |

⭐ **And it checked its own second number before publishing it:** 14 RESOLVED against 2 winners looks like a gap
and is not -- the 12 are **pre-battery legacy shapes carrying no `battery` block at all.**

⚠ **THIS SEAT DID NOT RE-DERIVE IT.** The artifacts are in S3, not the worktree; the cost of a second sweep is
real and the claim's error lands on a FUTURE cell, not on a served artifact. **So this row is an ATTRIBUTION, not
a corroboration, and says so** -- an adoption is not a measurement, and the way to keep that true is to label it.

⭐ **The exposure therefore stands as an EXPOSURE THAT HAS NEVER FIRED** -- which is the disposition Rule 22's
negative mirror asks for: the remedy is building the guard **when step 5 first wins**, not re-opening anything
now. **Rule 30 and the `infra/logic/**` lane gap remain OFF-path for every cell until then.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S408",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T06:50Z",
    "one_line": "Carries into the CHANNEL the answer to the one query Z-C-S406 deferred: measured by 1.0.0_SA_CTO~Z @401d59ce04 over filings/v1/, 0 of 206 served objects win at step 3 or 5 (step 4 x1, step 1 x1, absent x204; the 12 analysis objects are pre-battery legacy shapes with no battery block), so the bronze asymmetry is an EXPOSURE THAT HAS NEVER FIRED and its remedy is to build the sink when step 5 first wins.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "1.0.0_SA_CTO~Z @401d59ce04, over filings/v1/: denominator 206 json (194 source, 12 analysis); winner.step step 4 x1, step 1 x1, absent x204; winners at step 3 or 5 = 0 of 206.",
        "Its own second-number check: 14 RESOLVED against 2 winners is not a gap -- the 12 are pre-battery legacy shapes with no battery block.",
        "Z-C-S406 named this query and declined to run it; battery.py steps 3 (:900) and 5 (:1342) take no bronze_sink parameter, which is the exposure the query tests."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A question deferred in the channel is answered in the channel.",
    "world_is": "The deferred discriminator was run by another seat and published in a message, where a reader of this channel would never find it.",
    "notes": "THIS SEAT DID NOT RE-DERIVE THE NUMBER: the artifacts are in S3, not the worktree, and the error of this claim lands on a FUTURE cell rather than a served artifact. The row is an ATTRIBUTION, not a corroboration, and is labelled as one -- an adoption is not a measurement. DURABLE HALF: a deferral written into a channel and answered in a message leaves the channel's reader holding the question with none of the answer; carry the answer back to the surface that carried the question. COST: one short row. NON-APPLICATION: a deferral nobody answered.",
    "adjudicates": [
      "AMGT_RESAPP-Z-C-S406"
    ],
    "dismissal_reason": "A record-completion row: it moves an answer from a message into the channel that posed the question, attributes it, and converts no exposure into an incident."
  }
]
```
