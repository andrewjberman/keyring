# Andrew-direct 2026-10-14 ~18:5xZ (dell1, `1.0.0_SA_CTO~DELL1` terminal) -- one DT on the box handles the promotes

## VERBATIM

> "Is there a reason you have two differnet DTs active for promoting? why not just have one DT on the box handle? As long as they dont step on each other its fine, but seems counterintuitive"

## Context

Within the hour, this seat had asked `0.0.0_AB_MSTR~DELL1` for one `0.4.0_DT_ClientPlatform` lane per project, in order to promote:
- `~R1`, AMGT_RESAPP bm-4, already done;
- `~H1`, MDPF_SECHIST c822;
- `~D1`, MDPF_CANON 6e63, since held for its repair.

The reason was CLAUDE.md rule 27, "Seating: ONE PROJECT PER TIER-2 SEAT INSTANCE", which `.tools/to-decomp-ref-lint.py`'s seating check and `/mstr-spawn` step 1d enforce. MSTR's
step 1d refused the base DT for bm-4 because it held another project's open order.

## Applied on dell1, by this seat

- **One DT lane on dell1 runs the box's portal PROD promotes**, one after another, never two at once ("as long as they dont step on each other").
- The promotes are sequential by construction: each release is rebuilt on the PROD the previous one left.
- No further per-project DT lane is requested.

## What this seat cannot change alone

The one-project-per-Tier-2-seat rule is CLAUDE.md law (rule 27). Its gate (the seating check) may refuse a single DT lane holding orders from two projects. Changing the law
or its gate is the laptop `1.0.0_SA_CTO`'s act, under the law lock. This record is routed to that seat. Until then, the one DT runs the promotes as each issuer's order arrives,
and a gate refusal is surfaced, never overridden.

-- 1.0.0_SA_CTO~DELL1
