# DELL1 self-drive box -- ticks 204-205, 2026-10-20 ~20:48-21:18Z (delta: Andrew's hand sign-in, password accepted, PRD v0.5)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 21:18Z. Acked since tick 203: 8787, 8792, 8794, 8797, 8802, 8806.
- open_calls.json: 163 rows, 4 OPEN: 89c9, ea86, and 3bc7 and 5013, which are done or withdrawn in substance. The tool refuses to
  close the last two as CROSS-BOX.

## Acts and rulings
- **Andrew's hand sign-in on the box, done ~20:53Z.** I installed TigerVNC on dell1, ran `tmp/fidupl/02` and the SSM tunnel, and he
  signed in to the Wealthscape home page in the puller's profile. `05` freed the profile.
- **Andrew-direct ~20:5xZ:** daily pulls cover every G number in the G Number Switcher; the agent recovers the full browser sign-in
  when the trust token dies. Record and PRD v0.5 @c4f8dc3d51 (ADMITTED). The CRO mapped the switcher read @d44cc40cb6; both cells go
  to round 3.
  - The commit was refused twice first: my Python rewrite gave the PRD CRLF endings, which broke the gate's ENDPOINT heading match,
    and the header schema takes two version components. Both fixed.
- **Attempts after the seed** (P1 8792, 8794, 8797, 8806):
  - ATT present. Two runs PASSED the password. The 20:59Z run was signed in (text delivered, fresh ATT and JSESSIONID) and died at the
    final authorize step, which accepted only an exact 200.
  - A trace at 21:05Z got 403 with ATT present. The likely cause is the live session (cookies to 21:29Z) or four sign-ins in 20 min.
  - ATT lives one hour (expires 21:59:33Z) and renews only through a full sign-in (CRO @f210db95ed, with the two logout DELETEs).
  - Ruled: REPAIR 12 (authorize accepts any 2xx; logout on close and on a failed open), then ONE attempt in 21:35-21:55Z, after the
    session cookies expire and before ATT does. No old-code run if the repair misses 21:50Z. The IAM fix (ssm:ListCommands,
    ListCommandInvocations) is cut as FU-s-13.
- **2 objects under `fidelity/`:** both are run records (`alongside/bronze/_runs/20261020/`), not data.

## Scope state
- **NFRA_FIDUPL:** pending FU-s-10 (REPAIR 12 delivery), FU-s-11, FU-s-13 and FU-x-1. 0 data objects. The 3 fetch rules are DISABLED.
- **AMGT_HARVST:** round 100, co-6 on Fargate.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).

## Compiler Tools
- `winget`, `Test-NetConnection`, `ssm start-session` (the hand sign-in setup).
- `prd-signoff.py status`.
- `list-objects-v2`.
