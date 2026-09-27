# SELF-DRIVE laptop directives -- ticks 41-43 (2026-09-27 ~08:47Z to ~09:47Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 39-40 log (@`5c4d1cb9c1`, ~08:17Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## The blocker: the laptop is below the spawn floor

- **C: has 14 GB free, below the 15 GB spawn floor** (`df -h /c`, read at 09:30Z and 09:47Z).
- DSGN_IRPTV1 round 8 (IV-e-54..63) and TO-IV-e-53 are all UNSEATED: 0 of 10 workers, per ~D's drive log @`60d3cb6872`.
- 0.0.0_AB_MSTR has read nothing since 07:07Z; three offers are exhausted, including this seat's 101846.
- No fabric commit landed from 08:17Z to 09:47Z.

**Measured candidates (read-only; this seat deleted nothing):**
- `C:\Users\AndrewBerman\AppData\Local\Temp`: 6.5 GB in total, of which 1,021 entries (~1.4 GB) are older than 2
  days.
- `C:\Users\AndrewBerman\Desktop\ajb_irpt_m_s152`: ~2 GB, ~M's worktree for the first S152 cut, superseded by the
  CLOUD re-cut `ff63895521`. Its branch would be kept.
- The other worktrees (~2 GB each) belong to live seats and are not proposed.

**Card to Andrew (BLOCKING):** CLAUDE.md reserves recursive deletion to his confirmation.
- (a) clear the old Temp entries and remove the superseded worktree, to about 17 GB free;
- (b) lower the floor to 12 GB for the day.
- REC (a).

## Open calls in scope

1. BLOCKING: the disk card above.
2. CARRIED: the purge of the S19 screenshots from history. REC: keep history.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting

| on | what |
|---|---|
| Andrew | the disk word (1a or 1b) |
| 0.0.0_AB_MSTR | reading its inbox (the S19 untrack push, the S17 route, the seating offers) |
| ~D | round 8, once seated |

state: ARMED
