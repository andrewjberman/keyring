# DELL1 self-drive box -- tick 201, 2026-10-20 ~19:18Z (delta: FIDUPL launch probe passed, a standing re-run rule)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 19:18Z. Acked since tick 200: 8764.
- open_calls.json: 162 rows, 4 OPEN.
  - Three are acts only Andrew can do (89c9, ea86, and 5013, which is withdrawn in substance).
  - One is a fork, 3d0c, at XA-20261020T184817Z-72a8. The laptop CTO has not yet ruled it.

## Acts and rulings
- **NFRA_FIDUPL** (P1 8764):
  - The launch-only probe PASSED: headed Chrome, `DISPLAY=:99`.
  - Attempt 9 reached the wealthcentral login document (200), then failed at `submit_username` on a navigation race in our code. That
    was before the password page, so no password was sent.
  - REPAIR 11 is in build.
  - **RULED:** one re-run after REPAIR 11, plus a standing rule. A run that ends before the password POST is a code failure, counts
    against nothing, and may re-run without asking. The one-attempt rule binds again once a password POST is sent, with a report after
    each.
- **Also landed:** FU-s-12 is complete (the box-side `agent_fill` helper and the dell1 agent driver). CloudOps installed the
  agent-Chrome unit, and FU-s-10's eighth delivery is on the box.

## Scope state
- **NFRA_FIDUPL:**
  - Pending: FU-s-2 (REPAIR 11), FU-s-11 and FU-x-1.
  - 0 objects under `fidelity/`. The 3 fetch rules are DISABLED.
- **AMGT_HARVST:** round 100 at W1. co-7 waits on XA-72a8.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `xadj.py list`.
- `open-calls.py list`.
