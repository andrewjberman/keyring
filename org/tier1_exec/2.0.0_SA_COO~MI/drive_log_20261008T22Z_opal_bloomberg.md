# /canonical-drive NFRA_MCPINDEX -- 2.0.0_SA_COO~MI -- 2026-10-08 22Z -> 23:4xZ (host opal_bloomberg)

**archetype:** COORDINATE

Re-seated by 0.0.0_AB_MSTR~Z on 1.0.0_SA_CTO~O msg 32039: the site Z reboot left the lane dark. Arm: LIVE_ARMS row
`1.0.0_SA_CTO~O /self-drive 30m` paired with `~MI /canonical-drive NFRA_MCPINDEX 30m (+15m)`. Cron `16,46 * * * *`.
Lease FULL.

## Tick 1

| project | limb | round | TOs t/T | thread | act fired |
|---|---|---|---|---|---|
| NFRA_MCPINDEX | L7 | 7 | 6/7 (was 5/7) | n/a this round (BD ops cells) | DRIVE FORWARD: ledger V1, MX-s-18 grade, drain |

- **Ledger `nfra-mcpindex-r7-bd-runner-sentinel` CLOSED @f2422adb7f.** Leg V1 is the 2026-10-08 00:00:19Z scheduled run,
  RequestId 9c228e2b-4c66-424e-ba30-170c887d7ea5. It printed `OK: bronze sentinel emitted for 2026-10-08
  (tables=[transactions, realized])`, and the deployed code prints that only after head_object. Independent
  head-object: 00:11:37Z, 277 B. The author seat (AE~MI) is dark, so the issuer finished the entry (NEVER-2).
- **MX-s-18 `complete` @a74b50e525.** The issuer graded it: s18.AC1-AC4 PASS 4 of 4, and the mutant fired. The mutant was
  an OK print placed before head_object; under it AC1 read 2 of 3, and it read PASS again after the restore. The proof
  instance reads VALID. It sits in `deliverables/2.0.0_SA_COO~MI/` because owned-paths refuses the worker folder.
  `<instance_path>` was re-pointed as an issuer amendment, graded by to-pipeline-gate layer 1.
- **Drain @8376b446f0.** `wk-nfra_mcpindex-r7-24` was merged through safe-merge. The channel conflict was resolved
  as a row union: 243 + 5 = 248, no id collision, no in-place edits. Every guard passed. The worktree is KEPT
  because MX-s-19 A2 tells its assignee to work there.
  - DEFECT (mine): the conflicted merge sat open in the SHARED tree for about 10 minutes. It blocked every site-Z
    commit (0.0.0_AB_MSTR~Z msg 32108). Next time: drain in a drain-* worktree.
- **MX-s-19 A4 @e78ae4ff4b.** Re-addressed from AE~MI to `0.7.0_AE_CloudOps~Z` on Andrew-direct ~22:0xZ (msg 32063).
  The precondition is unchanged.
- **Row Z-S83 @9b04bf1ed4.** It adjudicates Z-W24-S11 (grant applied, live read-back passed) and Z-W24-S9 (s-17
  cancelled, nothing published). Both are DISMISSED_WITH_REASON, and ARMED for the project fell from 16 to 14.
  - DEFECT (mine): a `23:2xZ` surfaced_at sat in the shared tree uncommitted for about 5 minutes. It failed the
    corpus schema and blocked every commit (2.0.0_SA_COO~Z msg 32120). Fixed.

## Open (each with its condition)

- **MX-s-18 A2 reads.** Monday 2026-10-12 and Tuesday 2026-10-13, read from the 00:00Z runs with the evening rules
  still enabled. Each read is a sentinel `OK` line, or a `WARN` naming tables. On 2 of 2, GO MX-s-19 PHASE B to
  0.7.0_AE_CloudOps~Z, and disarm rows Z-W24-S4 (empty-window cause) and Z-W24-S3 (stale evening script) on the
  disable.
- **MX-s-19.** The only non-terminal order. The wait is essential and qualified: Andrew said "we need to confirm the
  shape first before making that move" (A2).
- **L8 compile and round-7 slug.** At the round's drain-end, after MX-s-19. Six ARMED rows owned by this seat are
  carried: Z-W8-S3, Z-W11-S2, Z-W22-S1, Z-W24-S3, Z-W24-S4, Z-W24-S8.
- **Push state.** Every commit above is LOCAL on box/sitez. Pushes are 0.0.0_AB_MSTR~Z's.

## Compiler Tools

- `deploy_ledger.py close-leg/close`: OK.
- `proof-of-spec-check.py`: INVALID once (an IAM row named a resource, not a path), then VALID.
- `to-pipeline-gate`: refused twice. The gate's stem search reaches only one level under `deliverables/`; the second
  attempt landed.
- `safe-merge.sh`: rc 4 (conflict), then `--continue` rc 0.
- `comp-surprise --armed`: 14.
- `surprise-row-gate`: refused once (schema: a surfaced_at with `2x`). Lesson: never type a placeholder minute into a
  machine-graded timestamp.
- `.tools/aws`: logs get-log-events and s3api head-object.
