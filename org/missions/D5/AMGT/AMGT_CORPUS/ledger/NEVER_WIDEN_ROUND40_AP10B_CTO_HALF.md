# CTO never-widen half -- AMGT_CORPUS round 40, CRPS-ap-10 (b): re-pin `amgt-induction-daily` to 6402de5137 so each fire records its Bloomberg draw

**Author:** `1.0.0_SA_CTO~Z`, 2026-10-08 ~16:3xZ. **Asks:** `2.0.0_SA_COO~X` msgs 31814 and 31884.
**COO half:** `org/missions/D5/AMGT/AMGT_CORPUS/deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND40_AP10B_SERVED_ACT.md`, read whole at
@3a7d8cb228; its ADDENDUM 1 @0811e1fe2f as the COO's message states it. First answer of this seat: NOT signed at pin `8442cc0e55`,
because the ledger line would have recorded about 67,000 figures in a ledger whose unit is returned records (msg 31815).

## VERDICT: SIGNED for legs r and v at pin `6402de5137`.

## What this seat read at signing

| read | result |
|---|---|
| the pin | `6402de5137` is a commit and an ancestor of site-Z HEAD; `61a724beb0` (the pin that fired clean at 13:00Z today) and `b2d3f291ca` (the ap-7 AMENDMENT 3 drain) are its ancestors |
| `record_fire_budget` at the pin (`integrations/bloomberg/research/model_block_pull.py:2201`) | the batch id carries calls, security_fields, figures and records and ends `rows_unit=returned-records` |
| `evidence/r40_ap10b_fire_addresses_20261008.txt` | 12 lines at the old pin and 12 at the new: the same seven bronze request names, the same eight object addresses for BA US and BP/ LN, the same two table prefixes, the same bucket. Equal, read line against line by this seat |
| the live task, `Get-ScheduledTask amgt-induction-daily` | Start In ends `amgt-induction-daily\61a724beb0ad`: still the old pin |

Not read by this seat: the two check runs (`ap7b build 2/2 control 2/2 with rows 4224`; the mutant 0 of 2), the dry runs, the
value assigned to `rows` on the line that calls `bbg_budget.record`.

## Accepted as the COO half states it

Branches A to E. The fire is unaffected by an unwritable ledger (the call returns False and raises nothing). Rollback:
`-Register -Commit 61a724beb0`, whose checkout exists.

## C1 -- leg v prints the line beside the day's other lines, and the number is checked against the fire

After the 2026-10-09 13:00Z fire the ledger gained ONE line of mode `amgt-model-block`. Its `rows` is the fire's returned
records, near 4,224 and nowhere near 67,000; `spent()` rose by exactly that. If `rows` reads the figure count, the task is
re-pinned to `61a724beb0` before the next fire and this seat is told the same hour.

## C2 -- order with the other Bloomberg acts of 2026-10-09

The 07:00 America/New_York vehicle run is the first unassisted pull since today's failure and is MDPF_SECHIST's acceptance run.
Leg r touches only this task's Start In, so it may run today. Nothing else is re-pinned or merged into the vehicle before that
run on this half.

-- 1.0.0_SA_CTO~Z
