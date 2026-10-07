# ANDREW-DIRECT 2026-10-07 ~20:5xZ (1.0.0_SA_CTO terminal) -- close ADVI_INSURE and ADVI_49F

## His words, VERBATIM AND ENTIRE

> "These two ADVI products should be closed down almost certainly (INSURE and 49F, as they are very old and i do not know if their vision is still relevant)."

## Reading

- The two projects named at ~19:2xZ as freed by the lifted D2 hold, ADVI_INSURE and ADVI_49F, are closed. "almost certainly"
  is his hedge; with his standing answer 4 of 06:5xZ (this seat may park or close the quiet and cold projects), this seat
  closes them and states below what closing does NOT remove, so he can see whether the hedge matters.
- NOT said: that anything deployed is removed, or that any task order's work is undone.

## What was done

- `org/projects/ADVI_49F.json` and `org/projects/ADVI_INSURE.json`: `status` active to closed; `phase` prefixed with his words.
  `dep_stage` left at EXECUTING in both: no completion report or grades exist and none is invented.
- Both were last touched 2026-09-03 (`git log` on each row). Neither is in the sequence or its parked list.
- NOT done: their four pending task orders are not edited (ADVI_49F.c02-REEMITRETIRE, 38 days old; ADVI_INSURE.TO-H2-AE,
  TO-H3-AE and one more, 34 days old), all issued to seats that are no longer live. They read pending under a closed project.

## What outlives the two projects (read from their own rows, NOT re-measured today)

1. **A stage of ADVI_INSURE is in the live 49 Financial nightly gold chain.** Its row, 2026-09-03: the insurance stage was
   re-armed and deployed that day ("Runner fixed + stage RE-ARMED @e9b070d842, deployed 13:0xZ"), acceptance being the next
   scheduled fire at 19 stages. Whether that stage runs today, and whether it should, is not known to this seat. Closing the
   project removes nothing from the chain; removing a stage is a deploy.
2. **A defect in the live 49 Financial chain's trigger, recorded on ADVI_49F's row** (2026-09-03): the event-driven 09:46Z fire
   starts on the session-fetch command succeeding, which is not the account-fact write completing, so the chain's first check
   and that write run at the same time; on 2026-09-02 two runs two seconds apart reached opposite verdicts. Its owner class
   was cloud operations. It is a defect of the pipeline, not of the project, and closing the project does not fix it.

Both are carried to the next tick's log as open items owned by this seat to place, not dropped with the close.
