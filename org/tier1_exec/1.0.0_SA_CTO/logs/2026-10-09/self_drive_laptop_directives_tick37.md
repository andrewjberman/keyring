# /self-drive laptop directives -- tick 37 (2026-10-09 ~01:2xZ)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`
(re-armed per the last addendum of `ANDREW_DIRECT_20261008_153xZ_TWO_PRIORITIES_GITOPS_AND_PROCESS_GC.md`). Cron `1a0c2133`, :17.
**state: ARMED**

## Scope and measurements

- Register: `DIRECTIVES-CHECK-RESULT live=15 retired=1 projects=396 open_projects=66 open_tos=471`.
- Inbox: 0 unread at the tick (every message since tick 36 acted and acked in-session).
- Cluster open calls (`open-calls.py list --all --cloud`, 01:21:30Z): boxes 4 of 4 read, open=4 (fork 2, act 2), closed=32.
  laptop 0 open. Keep-driving switch: absent, default ON on all four boxes.

## Ranked first: GitOps, garbage collection, graph

- **GitOps.** Every box branch is 0 behind `CLOUD` @71aac4e90d (integrated 01:04:51Z); ahead of `CLOUD`: laptop 14, sitez 23,
  dell1 4, dell2 30, all pushed within 15 minutes of the read. Local `box/laptop` is 4 ahead of origin; the task "Opal box-sync" is
  Ready, next run 01:30Z. The dell1 hold is gone: the DUAL-MINT gate fix (4.0.0_SA_CRO~A, applied @5ce6b2121c) merged box/dell1
  into CLOUD with nothing held (msg 107559).
- **GC.** 0.0.0_AB_MSTR's /govern 01:00Z: laptop reaper live, 0 worktrees removable, 0 hung seats of 14.
- **Graph.** 4.0.0_SA_CRO: fabric overlay proven live (vintage 00:49Z, 4,819 nodes / 16,864 edges).

## Calls ruled since tick 36 (each in-session, on receipt)

| msg | call | ruling | record |
|---|---|---|---|
| 107565 | step H CTO half (Dells read `/opal/ui-walker/password`, targeted 0/1/0) | SIGNED, three added conditions | `CTO_HALF_NFRA_CTLPLN_DELL_IDENTITY_STEP_H_UI_WALKER_READ_20261009.md` @4d7f665001 |
| 107566 | svc-irpt reader window again for ledger st26 | YES, same terms, REMOVE at 06:00Z without waiting | addendum to `CTO_HALF_SVC_IRPT_READER_DELL2_WINDOW_20261008.md` @4d7f665001 |
| 107567 | Dells' standing read of `opal/auth/jwt-private-key` | INTENDED (PLATFORM-KEY since msg 106669); each read reported | `CTO_RULING_DELL_READ_PORTAL_JWT_PRIVATE_KEY_20261009.md` @4d7f665001 |
| 107560 | COMM_ASSIST round 9: OG-md-1 release + MAIL_BEARER from site Z | relayed to 1.0.0_SA_CTO~O, agentbus `eca52cef` (SENT, not acked) | -- |

Site Z's two CROSS-BOX forks (AMGT_RESAPP `-107a` ABNB Bloomberg pull, `-493c` ICT identity read, 01:17Z) are site Z's CTO's to rule
first; site Z's scan is not yet installed, so 1.0.0_SA_CTO~Z was nudged (agentbus `102b731c`, SENT) to rule or file each by xadj.

## Driver acts this tick

- LGIC_ENFORCE FWD-5 re-graded, owed by `LGIC_BLANKFIX/ledger/ROUND_ANALYSIS.round7.md:18-19`: still NOT_REALIZED, advanced from 13 to
  63 of 87 roots (`ledger/FWD5_GRADE_FROM_BLANKFIX_FWD9_20261008.md`, re-grade section).

## Standing backstops

- One-shot crons `470f3ba7` (05:55Z) and `faf86f37` (05:56Z): hard-close events for dell2's F1 windows (TO-APPLY-18 C, TO-APPLY-20 C2)
  and, by the 107566 addendum, the TO-APPLY-23 REMOVE, all at 06:00Z without waiting.

## Completion test

NOT DONE: 66 open projects on the register; the laptop directives stay ARMED.

## Acts only Andrew can do

- Barron's sign-in (site Z `-9f24`; his words "We can handle Barron's sign in any time"): his login.
- Alyssa's Analysis request on portal DEV (dell2 `-3cb1`): her act, on his word.
- W1-S15: CLAUDE.md rule 30 wording against the refusing naming gate; a law-locked edit (`ANDREW_LAW_EDIT_ORDER`).

## Compiler Tools

`directives-check.py`, `open-calls.py list --all --cloud`, `git rev-list` per box branch, `schtasks /query`, `agentbus-sqs.sh send`.
