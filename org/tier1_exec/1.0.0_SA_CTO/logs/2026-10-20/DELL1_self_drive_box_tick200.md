# DELL1 self-drive box -- tick 200, 2026-10-20 ~18:49Z (delta: Track A launch cause, Track B re-cut and custody, HARVST host escalated)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 18:49Z. Acked since tick 199: 8744, 8745, 8748, 8753, 8756.
- open_calls.json: 162 rows, 4 OPEN.
  - Three are acts only Andrew can do (89c9, ea86, and 5013, which is withdrawn in substance).
  - One is a fork (3d0c), escalated.

## Acts and rulings
- **NFRA_FIDUPL Track A** (P1 8745): the one attempt died at browser launch again. There was no Fidelity traffic, so no attempt
  counted against Fidelity.
  - The true cause: the Playwright driver started before DISPLAY was set.
  - REPAIR 10 is complete (18:25Z). I asked for a launch-only `about:blank` probe on the box before the one Fidelity attempt.
- **NFRA_FIDUPL Track B, on Andrew's steer** (CRO 8748, @657d7fef6f): no Claude account on the box.
  - Ruled (8750): a dell1 agent drives the box's headful Chrome with Playwright `connect_over_cdp`, through an SSM forward to the box's
    localhost debug port.
  - Act 5013 is withdrawn. `open-calls.py` refused the close because the row is CROSS-BOX, so it stays OPEN in the file.
- **Track B custody** (P1 8753, ruled in 8754 and 8755):
  - (1) MSTR installs session-manager-plugin on dell1. Done: 1.2.896.0, signature Valid (MSTR 8756).
  - (2) The Wealthscape credential and the Quo code never leave the box. A box-side fill helper, called over SSM and attached to the
    same Chrome, does those two steps.
- **The 49F `dim_account_xref`** (laptop CTO via MSTR 8744): RESTORE, not retired.
  - Cause: dim-convert runs out of memory at 1024 MB on trading days; the newest xref is 2026-09-28.
  - The laptop's CloudOps lane fixes it (@b58716bd17). My datum "the producer runs" was incomplete: it runs and crashes.
- **AMGT_HARVST call 3d0c** (the gold rebuild host): the scan measures it CROSS-BOX, so it is ESCALATED as XA-20261020T184817Z-72a8 to
  the laptop CTO.
  - My position: Fargate, because wall time is about 1550 s in-region against the 900 s Lambda cap.
  - W1 builds co-6 on Fargate against fakes now. The co-7 apply waits on the ruled cross-adjudication file.

## Scope state
- **NFRA_FIDUPL:**
  - Pending: FU-s-10 (eighth delivery), FU-s-11, FU-s-12 and FU-x-1.
  - 0 objects under `fidelity/`. The 3 fetch rules are DISABLED.
- **AMGT_HARVST:** round 100 in flight at W1.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **The Fidelity hand sign-in** (`tmp/fidupl`), only if Track A stops at device trust (his login).

## Compiler Tools
- `xadj.py open`.
- `open-calls.py scope`.
- `ssm list-commands`.
- `lambda get-function-configuration`.
