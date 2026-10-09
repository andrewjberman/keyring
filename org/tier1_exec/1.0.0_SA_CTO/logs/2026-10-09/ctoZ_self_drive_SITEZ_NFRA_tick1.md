# /self-drive SITEZ NFRA -- tick 1, 2026-10-09 ~05:3xZ -- `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_043xZ_SELF_DRIVE_60M_SITEZ_NFRA_AND_PUSHES_NEED_NO_ANDREW.md`
(@d0541027eb, addendum @0d2382ab0e). Cron `6403bef8`, hourly at :23.
**state: ARMED**

## Scope (8 projects, read 05:36Z)

| project | status | dep_stage | COO lane (live) |
|---|---|---|---|
| NFRA_SPRINTWIN | active | PRD (PRD admitted) | `2.0.0_SA_COO~SW` (live; coo_lane written this tick) |
| NFRA_IAMROLES202609 | active | EXECUTING | `2.0.0_SA_COO~ZI` (live; coo_lane written this tick) |
| NFRA_OPSEC202609 | active | CLOSED | none (round closed) |
| NFRA_REPORT | active | EXECUTING (tree: ROUND_CLOSE, uncommitted by ~ZZ) | `2.0.0_SA_COO~ZZ` (live; coo_lane in ~ZZ's commit) |
| NFRA_MCPMSP | active | EXECUTING | `2.0.0_SA_COO~MS` (live). Its row reads PARKED 2026-10-01 by `1.0.0_SA_CTO~O` ruling 28068; the COO reads that park first |
| NFRA_MCPORTAL | active | EXECUTING | `2.0.0_SA_COO~MP` (live, /canonical-drive cron 620d0d66) |
| NFRA_OPALAI | active | EXECUTING | `2.0.0_SA_COO~AI` (live, cron 102d96c4); opal_ai DEV and PROD at 8cdc7b9735 (msg 32400) |
| NFRA_MCPINDEX | active | EXECUTING | `2.0.0_SA_COO~MI` (live, cron e822f7e3) |

**COMPLETION TEST: NOT DONE -- 0 of 8 complete.** All 8 REACHABLE. Sequence: NFRA_SPRINTWIN PLACED (stage 5); the other 7 UNPLACED,
governed by their own directives. No DRIFT.

## Acts

- `coo_lane` written on IAMROLES (`~ZI`) and SPRINTWIN (`~SW`). NFRA_REPORT's row holds `2.0.0_SA_COO~ZZ`'s UNCOMMITTED edits (dep_stage
  ROUND_CLOSE, phase), so its `coo_lane` line is left to `~ZZ`'s own commit with the index `derive --write` it owes, not committed
  under this seat's name (the tree validator refused the mixed commit: INDEX-DRIFT on NFRA_REPORT).
- Inbox: 0 unread since 05:06Z.

## Open calls in scope

No open calls in scope (tick 1). The site-Z list's remaining OPEN act row is the Barron's sign-in (AMGT_HARVST, now dell1's
project, act on site Z): an Andrew act (his login), outside this scope.

## Acts only Andrew can do (cited)

- Any portal PROD push that touches anything clients see (his ~04:3xZ word).

## Compiler Tools

- liveness and tree-row read for all 8; `sequence-check.py --project` for the three re-laned rows.
