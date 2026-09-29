# /self-drive tick 7 -- ~O fabric, four projects (1.0.0_SA_CTO~O)

**archetype:** COORDINATE

- Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md`
  @7612f001c4. Cron `0eef1ea2`.
- Tick covered: 7 (01:13Z). **state: ARMED**

## Scope

| project | status | dep_stage | open TOs |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 8 / 51 |
| NFRA_OPALAI | active | EXECUTING | 7 / 34 |
| NFRA_MCPORTAL | active | EXECUTING | 3 / 18 |
| NFRA_MCPINDEX | active | EXECUTING | 1 / 64 |

19 of 167 open, down from 21. Inbox: 0 unread. Sequence flags: none.

## Acts in this seat's lane since tick 6

- **OG-m-2 never-widen, CTO half: SIGNED** @c7510ec012, against the ask @14d3ce32a8. It covers the three dispatcher keys
  with per-key rollback; the read-only, single-firm IAM addition; the writer untouched (N=1); and both branches. The
  rider `e2be5c2f42` is bounded by the measured diff. The second half is asked of `3.0.0_SA_CVO~O`.
- **MX-r-4 delta re-sign: G-A plus the CTO half on pin `3371f18803`** @07a51e30c4. The delta against `2dedae93df` is
  exactly OA-r-1's live release (5 files, +505/-29, J1 PASS). Every MX-r-4 file is byte-identical, and G1-G8 carry.
  Rollback is now `mx-rb4` at `d287ffb346`.

## Calls closed on this seat's REC since tick 6

- **An asker grant with no `portal_channels`** (`3.0.0_SA_CVO~O`, OA-r-1 J1 @c180d84b36, row Z-W2-S1). RULED: an
  absent or empty `portal_channels` gives NO portal catalog key, never the whole opal-internal catalog. An absent
  allowlist fails closed. `2.0.0_SA_COO~AI` cuts it as a cell, with a test per negative arm, before the E3 switch-on
  (msgs 26343/26344). The CVO's J1 PASS was relayed to ~AI in the same message.

## Verdicts from CVO~O

0 pitched (no governance fork). CVO~O's J1 on OA-r-1 is a grade, recorded above.

## At Andrew

- The G-ACCT steps 5-6 sign-ins (after OA-f-6's ACL fix).
- His `sub` (G-SUB).
- Alyssa's Q1-Q3 post for his speed test.

## Completion test

NOT DONE: 0 of 4 complete. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `sequence-check.py --project` x4: flags none.
- The order-file census: 19 of 167 open.
- The pin delta: `git -C /c/tmp/mx-rel4 diff --stat 2dedae93df 3371f18803`, plus a per-file `git diff --quiet` over
  MX-r-4's 5 files. All read SAME.
- The gap: a `git diff` whose pathspec came from an empty `grep` printed the WHOLE diff (717 lines). An empty
  pathspec is not an empty diff. The per-file checks, not that count, were the evidence used.
