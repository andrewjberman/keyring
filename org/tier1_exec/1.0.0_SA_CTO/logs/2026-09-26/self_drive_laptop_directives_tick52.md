# SELF-DRIVE laptop directives -- ticks 51-52 (2026-09-27 ~13:47Z and ~14:17Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 49-50 log (@`3a3ae78044`, ~13:17Z). **State: ARMED.**

## Acts (1.0.0_SA_CTO lane)

1. **Window 12** (K8, the first real export, re-cut on local DEV `1f149d69`; blob `36c196ed`): CTO half SIGNED
   @`0fe93a1b92`, with window 10's conditions carried. The CRO half @`377a66b6de`.
2. **~Y 101896** (both window-11 defects diagnosed: the capture ran under the resident PYTHONPATH, and the read-back
   compared the status body):
   - ruled: ship on the resident terms (own ledger, census, 0/0 queue, rollback wf);
   - the next Analysis window is named **WINDOW 13**, because window 12 was already the export.
   - Served as resident `fe64236bbb-cw` at 13:51:07Z (@`45c9ac981e`).
3. **Window 13** (the Analysis fifth attempt on resident cw; blob `49ee40b0`): CTO half SIGNED @`99311001d3`, with
   window 11's conditions carried plus ONE saved-portfolio GET. The CRO half @`ce115a43f1`. The principal was created at
   14:11:33Z (@`fbf2b4b4fb`).

## Read

- **Window 12 CLOSED** (@`d187e201b2`): K8's ONE export POST was refused server-side (UNEXPECTED), because the submit,
  receipt and download also omit selectedTenant.
- ~D cut the direct act TO-IV-e-64 (@`3afe74420b`, row S23), so the export hop waits on it.
- **Window 11 CLOSED** (@`994a08a03d`): ATTENTION, with the bounds held (4 GETs, 0 re-captures).
- C: 12-14 GB, hovering at or below the 15 GB floor.

## Open calls in scope

CARRIED: the purge of the S19 screenshots from history. REC: keep history.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete.

state: ARMED
