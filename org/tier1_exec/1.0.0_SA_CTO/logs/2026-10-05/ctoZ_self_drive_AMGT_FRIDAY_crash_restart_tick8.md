# /self-drive AMGT_FRIDAY -- tick 8 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-05 ~01:2xZ -> ~02:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 7 @5989108a37.

## Calls, rulings, halves (since tick 7)

| item | act | commit |
|---|---|---|
| **Z-S230 re-ruled** (CVO msg 29374) | This seat's premise ("the password was never exposed") was WRONG. The pre-fix `fingerprint()` printed `pw_len` and a 48-bit unsalted sha256 verifier, which allows offline guess confirmation; re-read at `ab796d0520^`. **Rotation IS owed. It is Andrew's account act, carded to him.** Timing: between daily pulls, the BBGTerminal seat writes the new secret, and the next 13:00Z fire is the check. The row stays ARMED until it is done. | 1696185649 |
| HARVST as-1b THE collection run (msg 29379) | CTO half SIGNED, 5 conditions. "One run" = each (publisher, name) job concludes once; a checkpoint resume is the same run; a fresh pass needs Andrew's word. **LAUNCHED 01:44:37Z** @56e9339c65. | 138b152f2a |
| RESAPP r68 ar-3 redeploy (msg 29384) | CTO half SIGNED, 3 conditions. Base `2rFeF57l` read live; diff 2 files; **0 new S3 read paths, re-scanned by this seat**. GO @36c2eaf2d6; entry open. | 090ba579d3 |
| RESAPP FWD-36 | **c24 SERVED YES on the deployed function** after HARVST r46 as-2 widened `chatter_window` (ar-4 @4b2caa5a17). The 21-name gap is closed. | -- |
| HARVST ft leg | ft hard-stopped `sign_in_refused`. COO~H WITHDREW the hand-sign-in ask (@22eca07ba8): hand-solved ft sessions died at about 75 and 24 minutes (Z-W92-S20), and FWD-7 needs only one publisher at 191/191. **Driver's ruling:** ft stays stopped for this run. Collecting ft needs a sign-in route that lasts, which is a later design item and not a blocker. | -- |

No design forks went to CRO~Z and no governance forks went to CVO~Z this window.

## The collection run, first report (@dc8848cd23, 02:16Z, 32 minutes in)

sa 2/191, barrons 0 (queued behind sa), ft 0 (sign_in_refused), bbg 2/191, wsj 4/191. Declared set: EMPTY, as expected this early.
The sa bound is about 9.7 days at the pacing limit.

## Scope state (register read 02:18Z, denominator 5)

| project | status | dep_stage | in flight |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | r37: am-2/am-5 wait on the 2026-10-05 13:00Z fire |
| AMGT_HARVST | active | EXECUTING | r46: as-2 written, as-3 landed, as-1b collection running (4 drivers) |
| AMGT_RESAPP | active | EXECUTING | r68: ar-1/ar-2 drained, ar-4 closed (c24 YES), ar-3 redeploy entry OPEN |
| DSGN_AMGTV1 | active | EXECUTING | r36 on DEV; grading |
| ETFS_RIVALS | active | EXECUTING | r8 built (A 5 + B 4) |

Open TOs, directive-wide: D5 137, D13 1. Sequence: 5 UNPLACED. Active commitments: 0. Open deploys in scope: 1 (RESAPP ar-3, under its
pair).

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. **The Bloomberg terminal password rotation** (his vendor account; Z-S230 re-ruling @1696185649), between daily pulls.
2. Each further product-file DEV push (CLAUDE.md Portal).
3. The DSGN and ETFS_RIVALS FWD-1 signed-in reads (his login).
4. The rivalfunds OpenAI project key: deferred by his word.

## Compiler Tools

`directives-check.py --json`, `sequence-check.py --project` x5, `active-commitments.py`, `aws lambda get-function-configuration`
(the ar-3 base), and a `git diff` scan for new S3 read paths (0 added lines). **Self-correction recorded:** the first Z-S230 ruling
argued from the row's prose ("the password was never printed"), not from the code. The CVO read the code and caught it. A security
ruling reads the code that produced the artifact.
