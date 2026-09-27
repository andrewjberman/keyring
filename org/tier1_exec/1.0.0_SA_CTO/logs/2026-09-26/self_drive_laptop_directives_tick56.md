# SELF-DRIVE laptop directives -- ticks 55-56 (2026-09-27 ~15:47Z to ~16:17Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 53-54 log (@`1ab07743dd`, ~15:17Z). **State: ARMED.**

## Acts

1. **S158, the owner of the COT Black Diamond session refresh (~P 101941): ruled at CTO 101946.**
   - The refresh is automated. SSM document `opal-cot-bd-session-fetch` runs from Scheduler
     `cot-bd-session-daily-et`, which is ENABLED at cron(30 7) America/New_York.
   - The owner is `0.6.2_AE_PartnerETL` (ADVI_COTETL), per `infra/aws/terraform/cot-pipeline/ssm.tf:4`.
   - Measured, read-only:
     - the last Success was 09-16;
     - it Failed on 09-24, 09-25, 09-26 and 09-27 (latest `60650bfe`, rc 1);
     - the failed runs return empty output, because `set -e` aborts before the S3 log upload (`ssm.tf:65-68`);
     - `blackdiamond/cot/session` was last changed 09-16.
   - Ruling: nobody signs in by hand. S157 re-arms only on a new AWSCURRENT, as a new signed use. ~P recorded it
     @`2ad3d16ebc`.
   - The owner lane is NOT REGISTERED. The seat ask went to 0.0.0_AB_MSTR at 15:57:50Z.
2. **Window 15 (the Analysis chain, sixth attempt, resident lt): the CTO half is SIGNED on blob `51362fca`** @`04d670fd75`.
   - The CRO half is @`6901753e46`. Its named line: a stored level_as_of_type other than prior_close is audited
     against the certified PDF's level basis.
   - The principal was created at 16:03:44Z (@`dc102ceda7`). The window is running.
3. The inbox watcher expired and was re-armed (buv1693gh). Acked: 101941, 101943, 101949.

## State

- C: has **15 GB** free, at the spawn floor (read at 16:17Z).
- Active commitments in the last 24 h: 0 lines in 0 of 69 ledgers.

## Open calls in scope

1. CARRIED, at Andrew: the purge of the S19 screenshots from history. REC: keep history.

## Completion test

NOT DONE: 0 of 2 IRPT projects are complete (IRPT_BCKEND and DSGN_IRPTV1 are both `active`). D10 is UNMEASURABLE (no
members).

## Waiting

| on | what |
|---|---|
| ~Y / ~P | the window 15 terminal state, then the audit against the signed bounds |
| 0.0.0_AB_MSTR | seating 0.6.2_AE_PartnerETL for S158 |
| ~D | TO-IV-e-65 (the export report_id fix), then the export re-cut packet |

state: ARMED
