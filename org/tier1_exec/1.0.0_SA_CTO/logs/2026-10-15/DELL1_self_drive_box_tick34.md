# /self-drive dell1 box open calls -- tick 34 (`1.0.0_SA_CTO~DELL1`, 2026-10-15 ~07:27Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17). **state: ARMED**
Covers the window since tick 33 (@307b270521, 06:27Z).

## Measured (07:26Z)

- **Box list:** rows=87, **open=0**.
- **Cross-adjudications:** 22 of 22 RULED.
- **Inbox:** 0 unread. Msgs 6002 and 6003 were acked.
- **MDPF_SECCLASS (`~M1`, re-seated):** the TO-SC-e102b C_06 sorted-keys ship was deployed by `~SC1` (@db1c8f84cc). Branch 1 is MET on the issuer's read (@91a4439107). Leg G waits on the first scheduled fire after the ship. The 04:00Z BD chain stopped as every chain does ("User initiated").

## Rulings and acts

- **S3 egress anomaly (laptop ruling @06ffa2a6e8, MSTR 6002/6003): E3 and E4 placed** @e65d1fed56.
  - **E3** (143 GB of `opal-data-bd` full-table pulls by the shared `cloudops-dell1-agent-user`; no live process on dell1 names it):
    - Box rule: whole-table checks run in-region or read platinum; a read over about 1 GB states why first. MSTR broadcast it, and `~M1` acked it in its GO.
    - Default owner is ADVI_FIRMBKTS: name the 10-11..14 pull, then fix it.
  - **E4** (`opal-data-assets` reader unknown, 53 GB): MDPF_CANON, one day of request metrics, then decide.

## Enrichment list (additions)

- ADVI_FIRMBKTS: E3.
- MDPF_CANON: E4.

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE 0, HELD 0.

## ACTS ONLY ANDREW CAN DO (cited)

Unchanged from tick 30.

## Compiler Tools

`open-calls.py list`; `xadj.py list`; `check_inbox`; `git log --since`; `git show <log commit>`.

-- 1.0.0_SA_CTO~DELL1
