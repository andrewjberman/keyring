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

## MEASURED 2026-10-08 ~10:5xZ -- the two things that outlive the projects (read by 0.7.0_AE_CloudOps~E, msg 106887)

Read-only; file `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/ANSWER_TO_CTO_106590_49F_GOLD_CHAIN_TWO_FACTS_20261008.md`
@a88c35ede4. Not re-read by this seat.

1. **The insurance stage DOES run today.** The newest chain log of 765, `chain_20261008T094733Z.log`, reads `stages=18` and
   `STAGE OK insurance_nav_current rc=0`. At the 2026-09-03 vintage the header read 17 with no insurance stage. So a closed
   project's stage runs every day in 49 Financial's live gold chain. Removing it is a deploy and a decision; closing the
   project did neither.
2. **The trigger race is not seen in the last four runs.** Zero of 4 logs at the 09:4xZ fire end in an abort (2026-10-05 has no
   such log, so the denominator is 4, not 5); all four end CHAIN OK. The abort was real at the record's vintage
   (`chain_20260903T094635Z.log`: "CHAIN ABORT stage=a00_dim_account rc=1"). NOT established: why it stopped; 2026-09-05 to
   2026-10-01 was not swept. It is not shown fixed; it is shown absent in four runs.

Both items are no longer parked on a missing read. Item 1 is put to Andrew as what it is. Item 2 stays an open defect of
unknown state, owned by this seat to place with the pipeline's owner.

## RULING (1.0.0_SA_CTO, 2026-10-08 ~13:2xZ, under /self-drive): the insurance stage stays in the chain until its readers are measured

This seat had listed "whether the insurance stage stays" for Andrew. It is a decision, not an act only he can do, so the
driver rules it. Ruling: the stage keeps running. Removing a stage from a client firm's live gold chain is a deploy with a
rollback; leaving a clean stage running costs one stage's run time a day. What is not known is whether anything reads
`gold/advi/insurance/insurance_nav_current/` in 49 Financial's bucket. That read is asked for next. If nothing reads it, the
stage's removal is cut as an ordinary order under a pair; if something does, the stage stays and its owner is named.

## RULING (1.0.0_SA_CTO, 2026-10-08 ~14:3xZ): the readers are measured -- none; the stage comes out of the chain

`0.7.0_AE_CloudOps~E` (msg 106958, answer @3fb4d8e263): no code names the output as an input (11 hits over 18,582 files for
the table, 3 over 20,038 for the prefix; each the writer, its runner, its schema census or a comment; the portal included); no
later stage of the chain reads it; the audit trail's data events for the newest object's whole life (98,676 events) show three
HeadObject calls by the chain's own runner and zero GetObject, with that seat's own seven reads as the control. Unswept: the
write itself, 24 older objects, 16 regions.

Ruling: the insurance stage is removed from 49 Financial's gold chain, as an ordinary order under a pair, by the box that owns
that chain. The stored objects under `gold/advi/insurance/insurance_nav_current/` are left in place: deleting them is an S3
delete, which is Andrew's act, and nothing gains from it.
