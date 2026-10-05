# /self-drive AMGT_FRIDAY -- ticks 2-3 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-04 ~20:1xZ -> ~21:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 1 @cc9ebe3820.

- **Tick 2 (20:18Z):** QUIET. 0 unread. The one peer delta was CORPUS's r35 ak-4 NEVER-2 entry CLOSED @66a15668e1.
- **Tick 3 (21:18Z):** this log.

## Andrew's word in the window

**/open-calls at this terminal (~20:4xZ), VERBATIM:** "yes to all but call 3 is not pressing right now, we will deal with that
later." Record @441338fdf7.

| call | act | receipt |
|---|---|---|
| 1 HARVST collection | hold lifted for ONE universe-scope run per publisher; routed to `2.0.0_SA_COO~H` (after FWD-12 DONE, on the round-45 analysis's list) | msg 20:43Z |
| 2 DSGN 055ba370 DEV push | routed to MSTR~Z. DONE: portal DEV 2c792c27 carries it; condition 1 re-run 0/0/0; CI run 37234623154 success | msgs 29238, 29240 |
| 3 rivalfunds OpenAI key | deferred, carried | -- |
| 4 five worktrees | removed (git deregistered). Two leftover dirs held only a `node_modules` JUNCTION into the shared `portal/node_modules`; only the junctions were removed (`rmdir`, non-recursive), and the shared folder read 263 entries before and after. Branches kept. | 20 worktrees remain |
| 4 (hold) wk-dsgn-amgtv1-92 | its hold was discharged by the push, but **NOT removed**: `2.0.0_SA_COO~D` is using it live for round 35 (`dsgn-r35-onto-dev`, 6 unpushed commits, merged 21:09Z) | -- |

**Signed-in smoke at the COO~RV terminal (~21:0xZ, record @1c31a5f6ce):** S7/S8 changed ratified ENDPOINT text, so this seat
landed **ETFS_RIVALS PRD v0.14** @4cc8e40575. It makes the last 30 trading days the default, then a divider, then MTD/QTD/YTD. Windows
are stated up front, and the switch is linked in "What drove the return" and "Buying trend". The no-script rule stands.
`3.0.0_SA_CVO~Z` re-signed @acdb709768 (review @510a275af3, msg 29246); the PRD is ADMITTED. COO~RV was told that LIMB 6 no
longer withholds round 8. Round-8 workstream A issued @5f6b2a22d7.

## Calls closed, halves signed, analyses

| item | ruling / act | commit |
|---|---|---|
| CORPUS r35 slug 29221 | **Round 35 CLOSED. FWD-22 REALIZED.** Round 36: FWD-20 V3 rows on the Model tab, a units judgment read, and a regression read of the 10-05 fire. The 802 UNRESOLVED serve with their reasons; Z-W1-S32 closes under that; Z-W1-S31's exemption is kept. The 36 legacy ARMED rows are the CVO's REMEDIATION_v1 and do not hold L10. | 02bbbc0208 |
| NFRA_SPRINTWIN never-widen (msg 29213) | CTO half SIGNED, 5 conditions: writer 2 (local `/daily-sprint`) covered, the rollback image held (ECR 5 of 5, `446603c3` newest), no served invoke before both halves. The transition seam measured 0 double-counted commits. COO~H's half SIGNED @740fb88d8b. | e92e21fef3 |
| RESAPP r67 aq-5 never-widen (msg 29222) | CTO half SIGNED, 5 conditions. Read live: base `FcVBPafw`, memory 1769; the scanner key implicitDeny. Grant first, then simulate `allowed`, then code. The 21 no-table-row names are a counted served change. | 786d5e992e |
| HARVST r45 issued (msg 29225) | Noted: the Z-S82 clip is already in effect at the routes (0 leaks), so ar-3 is a READ. No act. | -- |

No design forks went to CRO~Z and no governance forks went to CVO~Z.

## Scope state (register read 21:18Z, denominator 5)

| project | status | dep_stage | where it stands |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | round 36 owed by COO~X on @02bbbc0208 |
| AMGT_HARVST | active | EXECUTING | round 45 in flight (ar-1 worker ~93; ar-2 landed; ar-3 READ) |
| AMGT_RESAPP | active | EXECUTING | r67 aq-5 (grant + code) with AE~A under the signed pair |
| DSGN_AMGTV1 | active | EXECUTING | round 35: 3 cells drained (AV-zm-1..3); a portal candidate review will come to this seat |
| ETFS_RIVALS | active | EXECUTING | round 8 workstream A issued (5 TOs) on v0.14 |

Open TOs, directive-wide: D5 124, D13 1. Sequence: 5 UNPLACED, 0 flags. Active commitments: 0.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. The DEV push of each new portal product-file candidate (CLAUDE.md Portal): CORPUS round 36's Model tab and DSGN round 35.
2. The DSGN FWD-1 and ETFS_RIVALS FWD-1 signed-in reads (his login). RIVALS' smoke at ~21:0xZ was one; the round-8 grades follow.
3. The rivalfunds OpenAI project key: deferred by his word ("not pressing right now").

## Compiler Tools

- `directives-check.py --json`, `sequence-check.py --project` x5, `active-commitments.py`, `prd-signoff.py status` (ETFS_RIVALS
  WITHHELD -> ADMITTED), `aws lambda get-function(-configuration)`, `aws ecr describe-images`, `aws iam simulate-principal-policy`.
- What worked: before removing worktree dirs, `ls -la` / `readlink` / PowerShell `LinkType` exposed `node_modules` as a junction
  into the shared portal. A recursive delete would have emptied the live portal's dependencies. Non-recursive `rmdir` on the
  junction plus a before/after entry count (263/263) is the safe form.
- What failed: the first `rmdir` through MSYS `cmd //c` mangled the quoted path (rc "syntax incorrect"). It was redone from
  PowerShell. `git worktree remove --force` took over 5 minutes on two trees and ran in the background.
