# SELF-DRIVE laptop directives -- ticks 37-38 (2026-09-27 ~06:47Z and ~07:17Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 35-36 log (@`ba7de52fc7`, ~06:17Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## Read (other seats' acts)

- **Window 10 CLOSED** (@`16f05ab61c`):
  - K7 reopened 49F RPT-b5e0a16e (8.05%);
  - **K8 NOT RUN:** the page's Export preview refused client-side (`resolveBundle.ts:255`);
  - 0 export POSTs, nothing written;
  - the principal was deleted 06:32:17Z, 0 requests outside the classes, 0 new media in git.
- **Root cause** (~P @`605296de70`): the Export preview's Performance fetch omits `selected_tenant`. Rows
  DSGN_IRPTV1-S20/S22 are filed.
- **The fix** is cut as ~D's direct act TO-IV-e-53 (@`fd78957113`): the Export preview and print carry selectedTenant.
  The next window's K8 waits on it.
- **S19** (the client-data screenshots): untracked @`cfed2c067b` with `*.shots/` ignored, and the row disarmed. The
  history purge stays at Andrew (CARRIED card).
- **DSGN_IRPTV1 round 7 DRAINED; its L8 packet was sent to 3.0.0_SA_CVO** (@`ce13f9af66`, @`f4ba212f9f`).
  - TO-IV-e-50 was drained and PARKED: the suite went from 17 to 8 failing, 0 new; the instance is INVALID.
  - L9 grades are next (on window 9's walk), then the CVO's slug to this seat for the round-N analysis.

## Acts (1.0.0_SA_CTO lane)

- The inbox watcher re-armed on each expiry.
- No ruling was owed this interval.

## Open calls in scope

One, CARRIED at Andrew: the purge of the S19 screenshots from git history. REC: keep history; untracking is done.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| 3.0.0_SA_CVO | round 7 L9 grades, then the slug; the round-5 slug |
| ~D | TO-IV-e-53 (the Export tenant fix), then a window for K8; the round-7 push to origin DEV |
| ~P | window 11's K8 packet once IV-e-53 lands |
| ~M | Monday 09-28: R1, then the COT cash-line act (S155 alone) |

## Round-N analysis enrichment (carried for the L10)

1. The R10 exception label.
2. S18, a request-list route so the page shows another session's Analysis job.
3. S20/S22 if IV-e-53 does not close them.
4. S157, the COT retained face.
5. S152, INF holdings lagging the frontier (R4).

state: ARMED
