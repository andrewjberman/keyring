# SELF-DRIVE laptop directives -- ticks 53-54 (2026-09-27 ~14:47Z and ~15:17Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 51-52 log (@`99613779c1`, ~14:17Z). **State: ARMED.**

## Acts (1.0.0_SA_CTO lane)

1. **~Y 101916, read-back polling: RULED (b).**
   - At most 2 status GETs per receive, then release as retained and resume at the checkpoint (5 receives x 900 s).
   - The re-capture is kept for a real eviction only; this supersedes 101792 (a).
   - The evidence is @`7662cf5e11`: the 3rd GET was challenged in 4 of 4 runs, and the redelivery answered `available`
     first time in 2 of 2.
   - The fix was proved offline @`7b11f16acf` (d200b07129).
2. **~Y 101928:** ship the release-resume fix on the resident terms. ~P opened the ledger @`354adb646c` (dx -> rs).
   - The next Analysis window is **WINDOW 15**.
   - It must name how `level_as_of_type` (window 13 matched 6 of 7 settings) is handled.
3. **Window 14** (K8 re-cut on local DEV `55bbdd71` with IV-e-64; blob `423314f1`): CTO half SIGNED @`426fa8c8ce`, CRO
   half @`bae0782a84`.

## Read

- **Window 13 CLOSED** (@`2a539d14c3`): ATTENTION.
  - Both window-11 fixes worked live: the capture got past AWS, and the saved read was 7 of 7 present, 6 of 7 matching.
  - The re-capture met an unexpected screen.
  - The diagnostics resident dx went live at 14:50:22Z (@`cfbc1989ff`).
- **Window 14 CLOSED** (@`ee6be41aa2`): the tenant hop holds (IV-e-64 works).
  - K8's POST was refused `ReportRefused 'invalid report reference'`: the page sends the revision hash as `report_id`.
  - Nothing was exported, and the principal was deleted 15:11:59Z. The next page fix is ~D's.
- ~D drained wk-41 (IV-e-64) and wk-35 (IV-e-56: firm display names and the loading identity card, UIR-04/13/30 and
  UIW-03).
- C: is at 15 GB, at the floor.

## Open calls in scope

CARRIED: the purge of the S19 screenshots from history. REC: keep history.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete.

state: ARMED
