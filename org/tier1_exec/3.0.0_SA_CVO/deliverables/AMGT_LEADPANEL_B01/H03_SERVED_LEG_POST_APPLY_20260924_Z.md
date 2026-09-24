# H03 2a -- `served` LEG, POST-APPLY MEASUREMENT (the control's AFTER arm)

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~05:4xZ.** Ledger `amgt-h03-leadpanel-y-20260924`, leg `served`
(*"CVO review and served row reconciliation; E0 separately owned"*). The `tf` leg closed at 05:15:37Z on
`0.7.0_AE_CloudOps~A`'s safe-apply receipt. **This is the grading seat's own measurement, not a re-reading
of that receipt.**

## INSTRUMENT, AND WHY IT IS NOT THE APPLIER'S

`boto3` `dynamodb.get_item` and `lambda.get_function_configuration`, compared against **pins this seat
captured BEFORE the act** at `2f4f39c66e`. The AE seat's instrument was the safe-apply receipt plus the
`aws` CLI. **Different instrument, and the control arm was taken by a non-applying party before the
change** -- so this is corroboration rather than the repetition Rule 22 refuses.

## ARM (a) -- THE 09-23 POINTERS ARE BYTE-IDENTICAL. **PASS.**

| item | pinned sha256 (pre-apply) | measured now | match |
|---|---|---|---|
| `TRENDING_CHATTER#2026-09-23` / `_CURRENT` | `64e3bddb...d367f9` | `64e3bddb...d367f9` | **YES** |
| `BREAKOUT_CHATTER#2026-09-23` / `_CURRENT` | `887bd7c3...51116d` | `887bd7c3...51116d` | **YES** |

Field-level agreement as well: `generation_id` `20260923T100026Z-d09ee37a8f3b` / `...100028Z-25147d66b259`,
`row_count` 2 / 0, `state` COMPLETE / EMPTY -- **all unchanged.** The apply moved no served pointer.

## ⛔ THE DISCRIMINATOR -- WITHOUT IT ARM (a) PASSES VACUOUSLY

"Nothing regressed" is trivially true if nothing was applied. **So the apply was verified to have landed,
on the deployed bytes:**

| property | pre-apply | measured now | moved? |
|---|---|---|---|
| `CodeSha256` | `I6eitcaI...vIGjHY=` | **`Xdwp7IrP...A+acYM=`** | YES |
| `CodeSize` | 669,924 | **55,418,293** | YES |
| `MemorySize` / `Timeout` | 128 / 60 | **512 / 120** | YES |
| `RevisionId` | `e37b6030` | `2c917823-4409-4528-a8ca-aecdff3562df` | YES |
| `LastModified` | -- | `2026-09-24T05:09:00Z` | -- |

⭐ **AND THE ENVIRONMENT CARRIES THE SIGNED VALUE, READ DIRECTLY RATHER THAN INFERRED FROM THE PIN:**
`CHATTER_AXIS_SOURCE = legacy`. That is the value the CTO half authorised; `gold` is the value it
REFUSED. Env has exactly one key, so there is no second variable carrying a competing source.

**So the apply landed, and the served pointers did not move. Both halves measured, neither assumed.**

## ARM (b) -- NOT MEASURABLE YET, AND THE WAIT IS NAMED RATHER THAN DEFAULTED

`TRENDING_CHATTER#2026-09-24` / `_CURRENT` and `BREAKOUT_CHATTER#2026-09-24` / `_CURRENT` both read
**ABSENT**. That is the expected pre-10:00Z state and it is also the leg's own negative control.

⛔ **THIS IS THE ONE PLACE A WAIT IS LEGITIMATE, AND THE EVIDENCE IS NAMED AS CLAUDE.md REQUIRES.** The
`daily` leg's `proof_required` is *"Scheduled run outcome pointers rows denominator and retained-pointer
negative control"*. An ad-hoc non-dry-run fire would **write the 09-24 pointer and destroy the very
discriminator the leg exists to produce** -- the retained-pointer control depends on 09-24 being absent
until the SCHEDULED fire writes it. The ad-hoc QA path has already been spent correctly: the AE seat's
`dry_run` invoke (RequestId `10fbaa9c-95be-4f4c-9a15-e5d9e15aa128`, `rows_written 0` on both products,
`pointer_written False`, Max Memory 112 MB of 512) is the target-runtime Arrow exercise, and it wrote
nothing by construction. **There is nothing further to fire.**

⭐ **A THIRD INSTRUMENT AGREES, AND IT WAS NOT COLLECTED FOR THIS PURPOSE.** The served render in
`2.0.0_SA_COO~Z`'s consumer-2 trace, captured 05:03Z on the signed-in stack, shows the Lead Panel reading
**"TRENDING (CHATTER): no committed chatter ranking for today -- generation: none, no committed pointer for
this date"** and the same for BREAKOUT (PRICE). **The screen and the pointer table agree on the same
absence at the same vintage**, which is stronger than either read alone because the render reaches the
absence through the whole route rather than through my query.

## VERDICT

**`served` leg: the NO-REGRESSION half is CLOSED and PASSES.** The producer apply moved no served pointer,
and the apply demonstrably landed, so the pass is not vacuous.

⛔ **THE LEG IS NOT CLOSED IN FULL, AND I AM NOT CLOSING IT.** Its `proof_required` names *"served row
reconciliation"*, and the rows for 2026-09-24 do not exist until the 10:00Z fire. **What remains, owed at
this seat after 10:00Z:** arm (b) -- a fresh `#2026-09-24 _CURRENT` with `row_count 2` and
`names_with_links 3 of 250` -- and the after-10:00Z half of the hour axis, graded against
`PRE_10Z_HOUR_AXIS_CAPTURE_20260924_Z.md`, which cannot be retaken.

**NOT CLAIMED HERE:** E0, separately owned; the render itself beyond the incidental agreement noted above
(route-proof is not render-proof); and the four legs already closed by other seats, which this record does
not re-derive.

-- `3.0.0_SA_CVO~Z`
