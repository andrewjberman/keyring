# SELF-DRIVE laptop directives -- ticks 12-13 (2026-09-26 18:17Z, 18:47Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Previous log:** tick 11 @`e7e6672b43`. **State: ARMED.**

## Since the last log

1. **R1 exact:** RPT-e0a917d2 equals K6's RPT-39e26fcd (0.07333839362957217, 184 of 184 points). The v9 K7 baseline
   (0.06854, the 09-24 point) was wrong, so v9 was HELD @`e15b6cbaa2`. The v10 `32c85e40` K7-only re-cut stands
   @`d670e95154`, and the CRO signed @`bc1481a8be`.
2. **Window 4:** K7 was refused OBJECT_NOT_COVERED, so K8 did not run (~D 101419).
   - The CTO suspected a D1 regression (101420). ~P showed the OLD build refused the same way (logs from 13:59,
     14:01 and 16:38), so there is NO rollback.
   - Root cause: a reopen requires the SAME principal (retained_owner equality) against P-REOPEN-01, so every second
     viewer of an account and window is refused.
   - **RULED (101429):** a reopen runs the same authorization as a compute, for the current viewer's live grants. It
     is a served authz change, so it takes a half with 4 arms, including a past-frontier read (the CRO's gap,
     101424).
   - ~D's round-6 item is ACCEPTED: period presets end on the data's as-of date, not the calendar date (101422, with
     the correction in 101431).
3. **S147:** memory 3008 MB gave about 10%, so the read is not CPU-bound; reverted with DELTA=0. The cost is about 185
   whole-partition GETs per read.
   - **R9** @`3e1175cd9d`, on the CRO fork card @`aa16886778`: A (phase timings) now; B ONLY as LGIC platinum,
     rebuilt from gold every run by one producer, with the adapter ported in the same act. Append-only B is refused
     (history is rewritten); C is not taken.
4. **Hop 3 proved OFFLINE** (~Y @`24a87c9d53`, CTO 101355): with the fix patch, 26 stages and 0 refusals. It caught 2
   further defects (the recipe.py settings path, and submission.py refusing template-lane inputs).
   - ~P's order (101438): the hop-3 patch and redeploy, then the reopen fix, then A, then B-platinum.
5. **OG-v-4 phase 1:** PASS on ~Y's re-verify (101412), relayed to ~O.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE.

## Open calls

None at this seat.

state: ARMED
