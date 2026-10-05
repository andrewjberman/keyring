# /self-drive AMGT_FRIDAY -- tick 5 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-04 ~22:2xZ -> ~23:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 4 @7b782a9c37. The verdict ledger commits with this log (row 2).

## Andrew's word in the window

| word | what it answered | record | routed |
|---|---|---|---|
| "recs approved" (~22:2xZ) | the RESAPP Z-S346 ruling: no aq-5 rollback; aq-6 forward-fix grant | @c700426bc9 | COO~Z |
| "rec approved" (~22:4xZ) | the CORPUS al-2 portal 75efe9d6 DEV push | @40cd6d2680 | MSTR~Z pushed: DEV 75efe9d6, CI 37241631766 success (msg 29300) |

Not read into either word: standing authority for future product-file DEV pushes. That was asked, and he has not answered it.

## Calls, verdicts, halves (since tick 4)

| item | act | commit |
|---|---|---|
| RESAPP aq-6 COO half (msg 29283) | CTO half SIGNED. Live read: chatter_window implicitDeny, chatter_daily allowed, code `aoQ+WrefJ` | 5468d18362 |
| aq-6 condition 3 (msg 29289) | Reversed. aq-5's entry had closed at 22:27Z, so aq-6 runs after CORPUS al-5 under its own entry. al-5 CLOSED Branch A at 23:11Z @e2790c8b2b, and aq-6's entry is now open. | 5a8f3ce6ff |
| CORPUS al-2 reworked (msg 29292) | portal 75efe9d6 APPROVED: fast-forward of DEV, 3 files, DSGN checks pass. Currency labels carried to the r36 analysis. | 60d69ec86e |
| **GOVERNANCE: PROOF_OF_SPEC schema vs AE deploy instances** (AE~A msg 29302) | Pitched to CVO~Z (29303), REC: a DEPLOY genre. **Verdict (msg 29306): (a), with 3 conditions** (issuer-marked at cut; at least one DISCRIMINATING control, DID-NOT-DISCRIMINATE is INVALID, a named rollback; no grandfathering). Ledger row 2. The build is in flight in worktree `C:/tmp/ctoz-pos-deploy` (subagent); it lands after review. | ledger row |
| HARVST ar-1 silver re-derive (msg 29305) | CTO half SIGNED for digest 9d7b7d57c651, 4 conditions. Rollback is append-only; a delete takes Andrew's word. | 16eb97eae5 |
| HARVST collection universe (msg 29308) | **(a) the rank's 191 names.** 191/191 resolution before any request; the sa bound printed before the GO; order FWD-12 DONE -> ar-1 verified -> run. | a142505a06 |
| HARVST `closer_contract` (msg 29309) | REMOVED. The H03 2a entry closed @64df5daa18. | a142505a06 |

## Scope state (register read 23:18Z, denominator 5)

| project | status | dep_stage | in flight |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | r36: al-5 CLOSED, al-2 on DEV; analysis after CVO's slug |
| AMGT_HARVST | active | EXECUTING | r45: ar-1 silver re-derive entry OPEN |
| AMGT_RESAPP | active | EXECUTING | r67: aq-6 grant entry OPEN |
| DSGN_AMGTV1 | active | EXECUTING | r35 on DEV; r36 next |
| ETFS_RIVALS | active | EXECUTING | r8 A issued; B in prep |

Open TOs, directive-wide: D5 131, D13 1. Sequence: 5 UNPLACED. Active commitments: 0. Open deploys in scope: 2, both under
signed pairs.

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. Each further product-file DEV push (CLAUDE.md Portal), unless he grants standing authority.
2. The DSGN and ETFS_RIVALS FWD-1 signed-in reads (his login).
3. An S3 delete, if HARVST ar-1's rollback ever chose one over the append-only form (CLAUDE.md Agent Autonomy).
4. The rivalfunds OpenAI project key: deferred by his word.

## Compiler Tools

- `directives-check.py --json`, `sequence-check.py --project` x5, `active-commitments.py`, `aws iam simulate-principal-policy` (the
  live grant read, rail-checked: `comp-iam` renders the declared view and cannot evaluate it),
  `aws lambda get-function-configuration`, and `git merge-base --is-ancestor` for the fast-forward check.
- A sparse worktree (`--no-checkout` + cone: .tools, org/standards, org/missions, org/ref, lib) isolates the schema build from the
  live gates that read the schema in the shared tree.
