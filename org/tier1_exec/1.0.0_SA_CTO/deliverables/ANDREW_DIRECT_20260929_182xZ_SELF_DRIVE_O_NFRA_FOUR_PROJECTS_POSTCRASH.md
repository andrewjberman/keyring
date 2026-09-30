# ANDREW-DIRECT 2026-09-29 ~18:2xZ -- /self-drive the active NFRA fabric ops, 30m, post-crash re-arm

**Channel:** Andrew, in the 1.0.0_SA_CTO~O Claude Code session (site Z), 2026-09-29 ~18:2xZ (~14:2x ET).
**Recorded by:** 1.0.0_SA_CTO~O, same turn, before tick 1 (self-drive section 0.5).

## Verbatim

> "Run /self-drive on the active NFRA fabric ops, 30m interval, adjudicating all calls, conferring with CVO~O to
> adjudicate reserved calls."

## Context

- This re-arms the scope of `ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md` (cron 0eef1ea2), which
  died with the session in the 11:34 ET site-Z crash. The prior loop's last log is `ctoO_self_drive_O4_tick32.md`
  (14:13Z, `state: ARMED`).
- The post-crash order (`org/tier0_exec/0.0.0_AB_MSTR~Z/deliverables/ANDREW_DIRECT_20260929_1755Z_POST_CRASH_RESIDUE_CLEANUP_AND_WORKTREE_ASSESSMENT.md`)
  runs as this loop's first work: residue cleanup and the worktree assessment with 3.0.0_SA_CVO~O come before any
  COO restarts its drive.

## ARM TERMS

| term | value |
|---|---|
| scope | NFRA_OPLGTW, NFRA_OPALAI, NFRA_MCPORTAL, NFRA_MCPINDEX ("the active NFRA fabric ops" = the four projects of the 09-28 arm) |
| device | site Z |
| cadence | 30m |
| call routing | self-drive Step 1: the driver rules every call on its own REC; a design fork goes to 4.0.0_SA_CRO~Z for pattern research first; a governance fork, and any call the driver would otherwise have treated as reserved, goes to 3.0.0_SA_CVO~O to adjudicate (Andrew's "conferring with CVO~O to adjudicate reserved calls") |
| acts listed for Andrew | only an act only he can perform, each with its citation (his login/MFA, a new M365 user in the tenant, a never-widen second approval, lifting a hold he set by name) |
| paired_with | `/canonical-drive NFRA_OPLGTW 30m` at 2.0.0_SA_COO~O and `/canonical-drive NFRA_MCPINDEX 30m` at 2.0.0_SA_COO~MI (+15m), each armed only after that COO's post-crash steps 1-2 close; NFRA_OPALAI (2.0.0_SA_COO~AI) and NFRA_MCPORTAL (2.0.0_SA_COO~MP) have no live COO at arm time, and a seat is asked of 0.0.0_AB_MSTR~Z when a cell needs one |
| stop-condition | all four `org/projects/<CODE>.json` read `status: complete`, HELD-AT-STOP (self-drive section 4), or Andrew's stand-down |

## Log

- 2026-09-29 ~18:3xZ ARMED by 1.0.0_SA_CTO~O.
- 2026-09-29 ~19:2xZ (tick 3): paired_with gains `/canonical-drive NFRA_OPALAI 30m` at 2.0.0_SA_COO~AI (respawned
  18:51Z). All three COO halves arm now, not after the checkout removals, which wait on Andrew's word and gate
  nothing (msgs 26668-26670).
