# /self-drive AMGT_FRIDAY -- tick 14 after the SentinelOne crash (1.0.0_SA_CTO~Z, 2026-10-05 ~07:2xZ -> ~08:2xZ)

**archetype:** COORDINATE

state: ARMED. Cadence 60m, cron `29c8b141`. Arming record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261004_194xZ_SELF_DRIVE_60M_AMGT_FRIDAY_RESTART_AFTER_SENTINELONE_CRASH.md`
@2b18064b99. Previous log: tick 13 @fab19f112f.

## Inbox measurement

`get_delivery_state` since 07:25Z: 1 message, READ (1 of 1). 0 unread.

## Calls, rulings and acts (since tick 13)

| item | act | commit |
|---|---|---|
| RESAPP r70 at-6: a grant leg (one prefix) and a code redeploy at e041c86791 (COO~Z msg 29526) | **CTO half SIGNED**, 5 conditions. Read live: OcKZF34X/1769, no open entry. Simulated: the new prefix implicitDeny, the `sec/` control allowed, and the `issuer-site/harvest/bronze/` negative control implicitDeny, which must stay so after the grant. The cross-firm guard lists only cottonwood. In flight: the grant leg L1 has applied; L2's AC4 is PASS on the applied plane, with its control. | 179e01a471 |
| HARVST row Z-S87 (COO~H) | INERT, no call. sa's old-path upload hit the 14,400 s job timeout and the driver exited without catching TimeoutExpired. The outbox is intact. sa resumed at 07:57:37Z on the batched path. Carried to the round-47 analysis: catch TimeoutExpired as a transport-class stop. | 3b17f76be3 (COO~H) |
| DSGN r38 AV-zp-1, AMENDMENT 1 (harness loaders) | The issuer's own amendment; no call. | 237bf4df8d (COO~D) |

No design forks went to CRO~Z and no governance forks went to CVO~Z. **No open calls in scope (tick 14).**

## Scope state (register read 08:18Z, denominator 5)

| project | status | dep_stage | in flight |
|---|---|---|---|
| AMGT_CORPUS | active | EXECUTING | r37: am-2 and am-5 wait on the 13:00Z fire |
| AMGT_HARVST | active | EXECUTING | r47: the run resumed on the batched path (all legs) |
| AMGT_RESAPP | active | EXECUTING | r70 at-6 deploy in flight (1 open entry, AE~A) |
| DSGN_AMGTV1 | active | EXECUTING | r38 AV-zp-1 in flight; the r37 DEV push awaits Andrew |
| ETFS_RIVALS | active | EXECUTING | r8 drain due ~07:41 ET; Z-S24 BQL recovery set |

Open TOs: D5 147, D13 2. Sequence: 5 UNPLACED, no flags. Open deploys in scope: 1 (at-6, in flight).

**Completion test: NOT DONE.** 0 of 5 complete; all 5 REACHABLE.

## Acts only Andrew can do (each cited)

1. **The DSGN r37 DEV push** (CLAUDE.md Portal, per-push word), held at MSTR~Z.
2. The 5 carried pre-sleep cards.
3. Row Z-W227-S1, a Bloomberg exec-officer pull (a vendor use no word of his names). Z-S230, the Bloomberg rotation (his account). The
   DSGN and RIVALS FWD-1 signed-in reads (his login). The FT route ("Dont attempt FT until I return").

## Compiler Tools

`get_delivery_state`, `directives-check.py --json`, `sequence-check.py`, `aws iam simulate-principal-policy` (rail-checked: a
per-key decision), `aws lambda get-function-configuration`, the cross-firm guard lists in `.tools/ds-precommit-check.py`.
