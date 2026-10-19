# ANDREW-DIRECT 2026-10-19 ~14:4xZ -- the Cottonwood carrier-value morning fix, now

**Author:** 4.0.0_SA_CRO~DDD. **Channel:** the 4.0.0_SA_CRO~DDD terminal on dell1, ~14:4xZ 2026-10-19 (~10:4x ET).

## VERBATIM

"which cloudops lane is on this? We need that fix now"

## What it settles

- **The lane question.** No CloudOps lane held the durable fix (findings ADDENDUM 3 spec,
  `COTTONWOOD_SUPERVISED_GAP_FINDINGS_20261017.md`). None of the six live 0.7.0_AE_CloudOps lanes on dell1 was assigned it.
- **The direction.** Andrew wants it fixed now. This seat executes it, as it executed the rest of FWD-10 on his
  2026-10-17 ~01:5xZ word ("probably have you just do it"). The never-widen pair and the CTO's apply gate still apply.
- **The deadline.** The first exposure is the 2026-10-20 07:30 ET bronze pull (as-of 10-19). The fix lands before it.

## ADDENDUM 1 -- ~16:4xZ, the roll-forward supersedes the wait

**VERBATIM** (answering "should I replace the wait with the roll-forward?"): "1.) Yes, the t+2 aspect for insurance does
not need to be separately labeled."

**Context:** Andrew's own proposal to Stephen Shipley (Teams, 2026-10-19 16:09Z): keep the 07:30 ET pull timing and roll
the prior day's insurance values forward, so the morning shows T+1 values with insurance at T+2, filtered to supervised.

**What it settles:** the carrier-value WAIT deployed at ~15:08Z (@67df6e6db1) is replaced by a carry-forward
(@e7d897445f). The carried values carry no separate label on the page.

**Open with Andrew (question 2):** whether MDPF restates a date when BD revises it (as ADVI does inside its 5-bday sweep),
or ADVI locks. Not settled by this addendum.
