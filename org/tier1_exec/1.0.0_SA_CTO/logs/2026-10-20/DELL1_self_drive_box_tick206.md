# DELL1 self-drive box -- tick 206, 2026-10-20 ~21:48Z (delta: windowed attempt 403, Track B ruled, seat ends)

**archetype:** COORDINATE
**state:** ARMED (cron 520f0ff2, record ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md @fa59eb8dec). The FIDUPL drive loop,
cron 19710f50, runs beside it.

## Inbox and open calls
- 0 unread at 21:48Z. Acked since tick 205: 8816, 8821, 8822.
- open_calls.json: 163 rows, 4 OPEN: 89c9, ea86 (Andrew's), plus 3bc7 and 5013, done or withdrawn, which the tool holds as CROSS-BOX.

## Acts and rulings
- **The windowed attempt at 21:36Z** (P1 8816): with ATT valid and no live session, the password POST still answered 403. The two passes
  (20:53Z, 20:59Z) were within ten minutes of Andrew's sign-in by hand; every refusal came after the scripted run minted its own ATT.
- **Ruled: GO Track B, one attempt.** The plain google-chrome unit driven over CDP, with the box-side fill helper, logout first, and
  `navigator.webdriver` recorded in both browsers as the control. The CRO's research @71919c25a0 (8822) confirms the lever: a
  Playwright-launched browser sets `navigator.webdriver=true`, which cfa and ThreatMetrix read as a primary bot tell, so an ATT minted
  in it scores untrusted. No Certified Browser enrollment exists to reproduce.
  - If Track B is also refused, the next test pairs Andrew's sign-in by hand with a Track B run inside five minutes.
- **FU-s-13:** CloudOps held the apply because the full-root plan carries FR-s-5's resources. Ruled: amend to the whole root, one
  apply, after the attempt reports. P1 amended it @2447c6ab931.
- **Seat ends at 21:34Z** (MSTR 8821): W1, SC1 and CloudOps~DELL1, the same shape as S21 to S25 (a queued task-notification as the
  last entry; two 1 ms apart). Ruled: respawn W1 and SC1; not CloudOps~DELL1, which is idle. Row S26.

## Scope state
- **NFRA_FIDUPL:** FU-s-11 (Track B attempt), FU-s-13 and FU-x-1 pending. 2 run records, 0 data objects. The 3 fetch rules are
  DISABLED.
- **AMGT_HARVST:** round 100 at W1, respawning.
- **ADVI_COTBOOKS:** L2, waiting on ea86.
- **Completion test:** NOT DONE.

## ACTS ONLY ANDREW CAN DO
- **ea86:** confirm ADVI_COTBOOKS v2's DONE WHEN lines (L2).
- **89c9:** the SOC2_MSLOGS re-derive (his MFA).
- **Conditional:** one more sign-in by hand on the box, paired with a Track B run, only if Track B is refused (his login).

## Compiler Tools
- `list-objects-v2`.
- `open-calls.py list`.
