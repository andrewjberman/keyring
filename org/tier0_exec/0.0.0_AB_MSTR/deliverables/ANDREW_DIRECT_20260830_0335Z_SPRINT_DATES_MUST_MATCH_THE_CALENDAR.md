# ANDREW-DIRECT 2026-08-30 ~03:35Z — sprint render dates must be accurate to the calendar

**Channel:** Andrew, typed at the `0.0.0_AB_MSTR` terminal (laptop). **Clock:** 2026-08-30 ~03:35Z (23:35 ET, 08-29).
**Recorded by:** `0.0.0_AB_MSTR`, same turn, VERBATIM. The phrasing IS the ruling.

## VERBATIM

> Something I just noticed, when you ran the /daily-sprint earlier, you wrote "Friday August 29". Today is August 29,
> however it is Saturday. We need to make sure that however dates are put together for the sprint render that it is
> accurate to calendar

## Measured before acting (the defect is wider than the instance he saw)

| report | typed `display_date` | derived from `date` | |
|---|---|---|---|
| 2026-08-27 | Wednesday, August 27, 2026 | **Thursday**, August 27, 2026 | wrong |
| 2026-08-28 | Thursday, August 28, 2026 | **Friday**, August 28, 2026 | wrong |
| 2026-08-29 | Friday, August 29, 2026 | **Saturday**, August 29, 2026 | wrong (the one he saw) |

Every report is exactly one weekday early: the first was mistyped and the scaffold-from-yesterday step carried the
pattern forward. `display_date` was a HAND-TYPED field in `daily_reports/data/*.json` sitting beside the ISO `date`
it should have been derived from — a typed value beside a derived one always goes stale.

## Reading (labelled as a reading)

"However dates are put together" = the mechanism, not the instance. So: (1) the renderer DERIVES the display date
from the ISO `date` and REFUSES a JSON whose typed `display_date` disagrees (fail loud, fix the JSON); (2) the three
published reports are corrected and republished; (3) the grounding packet prints the weekday so the writer never
types it from memory.

## Broadcast

MCP to `1.0.0_SA_CTO` (owner of the daily_reports template/scripts) + `2.0.0_SA_COO`, same turn; msg-ids appended
below by the sender after the send.

- broadcast msg-ids (03:4xZ): 85184 (1.0.0_SA_CTO) · 85185 (2.0.0_SA_COO) — 2 DELIVERED / 0 QUEUED / 0 REFUSED.
