# /self-drive AMGT_CORPUS AMGT_RESAPP AMGT_HARVST DSGN_AMGTV1 -- ticks 1-2 (2026-09-28 ~22:3xZ-22:4xZ), `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE
**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_220xZ_SELF_DRIVE_AMGT_AND_DSGN_AMGTV1.md`
@`a0186c364b`. **state: ARMED.** Cadence 30m, cron `13,43 * * * *` (session-only).

## Scope

- **Device:** sitez (`agentbus-sqs.sh device`). **Register:** D5 SITEZ, 3 members = the three AMGT projects (15 live
  directives read). DSGN_AMGTV1: sequence-check UNKNOWN, not in the register -- driven from its L3 registration.
- **Sequence:** the three AMGT projects UNPLACED (driven under D5). CAPACITY: 7 live COO lanes, no cap ruled for this box.

## Tick 1 (~22:3xZ)

| project | status | dep_stage | open TOs (LAST `<status>` tag) |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | 1 of 39 (`TO-CRPS-i-5`); `to-check --all` reads 13 -- row `AMGT_CORPUS-Z-S50` |
| AMGT_RESAPP | active | EXECUTING | round 46 issuing (COO~Z, cells 1-4) |
| AMGT_HARVST | active | EXECUTING | round 12 to be cut (COO~H, analysis @91276ffa94) |
| DSGN_AMGTV1 | -- | unregistered | brief in progress (Andrew + `4.0.0_SA_CRO~Z`) |

- **Inbox:** 0 unread after acting on msg 26250 (`1.0.0_SA_CTO~O`, SEQUENCE.yaml fabric drift -> fixed @`2bed2ad08b`).
- **Call at Andrew:** DSGN_AMGTV1's COO (he said "COO~D"; `2.0.0_SA_COO~D` is live on the laptop). REC: a site-Z lane
  such as `~DA`. ADJUDICABLE: 0; nothing pitched to `3.0.0_SA_CVO~Z`.
- **Acts:** arming record + LIVE_ARMS row @`a0186c364b`; paired half offered to COO~H / ~X / ~Z (msgs 26256-26258);
  SEQUENCE.yaml fix @`2bed2ad08b`; row `AMGT_CORPUS-Z-S50`.
- **Docs vs state:** the three `project.json` `blocking` fields are pre-reboot; named here, not rewritten by the driver.

## Tick 2 (~22:4xZ)

- **Andrew answered the call:** DSGN_AMGTV1 seats on `2.0.0_SA_COO~D` on site Z (REC declined; record
  `ANDREW_DIRECT_20260928_224xZ_DSGN_AMGTV1_SEATS_ON_COO_D_SITEZ.md`). 0 calls open in scope.
- **Scope on the LAST `<status>` tag:** CORPUS 0 of 39 (round 7's `i-5` drained @4ef91aedfe; L10 now waits on the CVO~Z
  slug); RESAPP 4 of 238 (round 46); HARVST 7 of 39 (round 12). DSGN_AMGTV1 still UNKNOWN.
- **Inbox:** 0 unread. **Verdicts:** 0. **Completion:** NOT DONE, 0 of 3; REACHABLE 3, UNREACHABLE 0.

## Loss and recovery

The tick-1/2 log, the COO~D record and the Z-S50 row were written in the shared tree. `safe-commit` refused twice (a
peer's NFRA_OPALAI drain merge open; then "staged index contains files not in declared pathspec"), and the staged-new
files were then removed by a peer's `reset: moving to HEAD` (shared-tree reflog, 3 entries). Nothing of them reached
any ref (`git log --all` on both paths: empty). Re-written from this seat's own session in its linked worktree
`C:/tmp/ctoz-sd` (branch `ctoz-selfdrive-amgt-20260928`), per CLAUDE.md 14b.

## Compiler Tools

`directives-check.py --json` (15 live; D5 members read), `sequence-check.py --project` x4 and `--compile`,
`to-check.py --all` beside a last-tag census (13 vs 1: the first-match parse, row Z-S50), `active-commitments.py`
(1 line in 24h, not in scope), `git reflog` on the shared tree to find the loss.
