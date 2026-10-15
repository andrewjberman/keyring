# NFRA_CTLPLN -- full re-grade of FWD-1..28 against PRD v0.30 (2026-10-15)

**Grader:** `3.0.0_SA_CVO~L` (laptop), on `1.0.0_SA_CTO` msg 109399 and ruling 1 of `ledger/ROUND_ANALYSIS.round18.md` @721e05298f.
**Basis:** PRD v0.30 @b4ad06ff09, each outcome's DONE WHEN and ACCEPT. The previous full grade is `NFRA_CTLPLN_FWD_REGRADE_20261013.md` @69e690cebf
(committed 13:53Z). Live reads 2026-10-15 ~11:4xZ-12:2xZ, by this seat and by four read-only evidence passes it ran:
- `crossbox-matrix.py`, all refs and `--since 2026-10-13T14:20Z`;
- `open-calls.py list --cloud`;
- the first-parent author census of origin/CLOUD after `git fetch`;
- CloudTrail `lookup-events` for five IAM write events since 2026-10-11 (each page under its cap, so complete);
- `seat-list.py show --all`; `research-owed.py --selftest`;
- `agent-spawn-audit.log`, broker.db read only;
- the 3389 port probe from the laptop.

**Rule:** REALIZED only when the DONE WHEN exercise has been read AND every ACCEPT clause holds. GATED names its gate. An outcome with no new evidence since
2026-10-13 keeps that pin and says so.

**A correction to the request:** FWD-6 and FWD-10 were graded on 2026-10-13: FWD-6 GATED and FWD-10 ADVANCED, in the table @69e690cebf. They are re-graded below.

## Tally: 2 REALIZED, 21 ADVANCED, 1 GATED, 1 PARKED, 3 MOVED (28)

Change from 2026-10-13 (2 / 19 / 2 GATED / 3 NOT SERVED / 2 MOVED):
- FWD-6 moves from GATED to ADVANCED: its held arm was exercised and released on Andrew's word.
- FWD-9 is PARKED (v0.29).
- FWD-11 is GATED on Andrew's hour.
- FWD-13 is MOVED (v0.29).
- FWD-27 is ADVANCED: the password arm is read, and its gates are now named per clause.
- No outcome reaches REALIZED in this pass. The two nearest are FWD-12 (one clause unread) and FWD-6 (the staff-only arm unexercised).

| FWD | grade | pin | one sentence |
|---|---|---|---|
| 1 a real round planned on the laptop, worked on dell1, integrated, graded | **REALIZED** | `thread-trace.py --round 11 --order TO-CT-aa-2` hops=5/5 (2026-10-13 grade) | Carried. No regression found. |
| 2 a box added once; every tool knows it | ADVANCED | `.tools/to-pipeline-gate.py:113` `FABRIC_ENUM = tuple(_fabric_values())` from `lib/devices.py`, a61f2a8df7 (10-13 18:53Z, TO-CT-ab-8) | The hand-typed box list is gone (the 10-13 blocker), but no box has been added through the register and had a seat started on it. |
| 3 a seat reaches a seat on any other box via the managers, read shown | ADVANCED | `crossbox-matrix.py`: pairs=12 with_file=12 acked=11 closed_both=5; newest laptop->dell1 XB-20261013T221323Z-92e8 OPEN, ack unset | dell1->sitez is now acked (0285). laptop->dell1's newest record is unread, though its earlier c5bf was acked by MSTR~DELL1. Most acks are by workers (CA2, U7, ZW), not managers, so "no other seat talks across boxes" does not hold. |
| 4 rounds reach the trunk without the box writing it; at most one unpushed round per lane | ADVANCED | origin/CLOUD first-parent since 10-11: 2064 of 2064 by `0.0.0_AB_MSTR`; integrate merges since the 10-13 grade dell1 221, dell2 214, laptop 241, sitez 237; `origin/box/laptop..box/laptop` = 4 commits, one DSGN_RBNDV2 round | Every box's rounds merge through the integrator. The unpushed-round clause is read for the laptop only; the other three boxes have no tool that reports it. One merge, 552e0e03ad (dell1 box-sync, 10-14 21:44Z), carries the committer `t <a@b.c>`, a stray identity to look at. |
| 5 a push deploys only what a signed change names | ADVANCED | `.tools/git-hooks/pre-push-safe-deploy.sh:88-123`; last committed HELD-DEPLOY row 2026-10-09T21:01:33Z (367 on origin/CLOUD); laptop working-tree rows to 10-12 uncommitted | No push carrying an un-named script has been read since 10-09. Round 19 names the negative arm. |
| 6 routine work merges with no one's word; only a client-facing release waits for Andrew | ADVANCED | routine: 913 box-sync integrate merges since the grade, none asked. Held: 53506d49 held, Andrew's word `.../2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_143xZ_NFRA_CTLPLN_ROUND12_CALLS_ANSWERED.md:14`, released as 15c97549 (ledger `20261013T1459Z_portal-prod-cherrypick-53506d49...` closed 15:13Z, CI 38419297038, portal-v2.1.212) | Two arms are exercised. The third, a staff-only page released without waiting, has no exercise: the one opal-internal change (trsb-history-excel-download) shipped inside a held client-facing release. The release receipt names no page class, though the call required it. |
| 7 every project's box visible; none split | ADVANCED | 2026-10-09 table (CVO PINS @a69d29a7b0) | No new evidence. No placement read across the four boxes; round 19 names it. |
| 8 two boxes never edit one file at once | ADVANCED | counter-instance c218cd50f0 (10-14 12:22Z): COO~C resolved by hand a clash on the order TO-CT-ac-5 against CLOUD's copy by COO~C1 | No conflict-free parallel round has been read, and one shared-file clash between two boxes occurred. |
| 9 scarce-account leases | PARKED | PRD v0.29 | No order names C-LEASE; v0.30's one-outage lift was never used. |
| 10 a Dell deploys its named commit unblocked; access changes refused | ADVANCED | deploy: ledger `20261014T1841Z_j359-satellite-characteristics-deploy-dell1-20261014_deploy_completion.md` (6c0f31efe6, CloudOps~DELL1), pin efb3f6550f applied 18:51Z, first reached CLOUD 19:19Z (de87265ef2). Delete refused: dell2 e47ea1ce2c/050eca6b81, AccessDenied by `DenyS3DeletesOnProductionData`. Access: CloudTrail since 10-11, 34 of 34 Dell IAM writes succeeded, 0 refused | The deploy arm is met (the pin lived on `wk-remote-J359`, ahead of box/dell1). The production-delete refusal is exercised. The ACCEPT's "attempts to change access ... are refused" no longer matches the world or Andrew's word: on 2026-10-13 ~16:5xZ he put both Dell users in his admin group, keeping three denies (`.../2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md`), after v0.30. The writes were 7 CreateRole, 21 PutRolePolicy, 3 AttachRolePolicy, 1 CreatePolicy and 2 DeleteRolePolicy. The audit-trail refusal is unread. The ENDPOINT text owes an addendum. |
| 11 a box restarts mid-round, nothing lost | **GATED** | open call `laptop-20261014T205216Z-7841` OPEN; Andrew ~20:49Z "Dell1 Restart is being held til later" (`deliverables/2.0.0_SA_COO~C/CT-ac-5_RESTART_HELD_20261014.md`); TO-CT-ac-5 parked (4e9f71fe08) | GATE: Andrew's hour at the dell1 console. The held record still says "status pending" while the order reads parked. |
| 12 every box's decisions in one list on the laptop; answers reach the box | ADVANCED | `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261014_114xZ_EIGHT_OPEN_CALLS_ANSWERED.md` (fcdfc34843, 11:45Z): site Z `232a` closed ruled-by andrew at 11:57:57Z (44abf5ef07); dell2 7773, 8500, 7b45, fde0, 3635 closed 11:55Z (73c91038f4). `open-calls.py list --cloud`: boxes=4 read=4 open=22 closed=205 | The DONE WHEN is exercised for two boxes, and the one list reads all four. The clause "no lane sits waiting on a terminal he is not at" is unread: dell1's 10-15 approvals f411 and c397 cite a COO~D1 record, which suggests an answer given at dell1. One read of where those two were answered settles it. |
| 13 a project moves between boxes by bid | MOVED | PRD v0.29 (dropped as written; the bid to COMM_ASSIST) | Not graded by this PRD. |
| 14 RDP from the MacBook to four boxes and from the laptop to three | ADVANCED | 3389 answers on 100.99.180.19, 100.79.95.44, 100.104.84.87 (probe, 10-15) | Ports only; no session record and no outside attempt refused. A person act (round 18 ruling 3). |
| 15 one real package laptop -> Dell, checked; the lane's work runs | ADVANCED | `...TO-CT-v-3.receive.txt` @4899c05b9a | No new evidence. |
| 16 approved or refused, read back by an outsider | ADVANCED | 2026-10-09 table | No new evidence. |
| 17 what was checked and what it cannot rule out, read to Andrew | ADVANCED | ADJUDICATION_v13 C-S38 | No new evidence. A person act (ruling 3). |
| 18 a download stopped on a Dell and on site Z, told the route | ADVANCED | `...TO-CT-v-3.blocked-download.txt`, `TO-CT-y-2.fresh-process-record.txt` @4899c05b9a | No new evidence. Site Z is untried, and TO-CT-y-2 is a GO ask. |
| 19 "what did this box download today" from a record | ADVANCED | `...TO-CT-v-3.receive.txt` STEP 3 | No new evidence. |
| 20 Teams request end to end | MOVED | PRD v0.21 -> COMM_ASSIST FWD-1 | Graded by COMM_ASSIST. |
| 21 every manager keeps its fabric running unasked and rules on nothing | ADVANCED | `org/mcp/agent-spawn-audit.log:19242` (U7 spawned 02:22:56Z by MSTR); broker msgs 109287 (00:51Z), 109293 (01:24Z), 109309 (02:21:52Z "respawn U7 NOW") from 1.0.0_SA_CTO; 4294b9e86d (MSTR~Z respawned ~MQ, ~ZQ, ~ZW, ~MI at 23:32Z, no ask cited) | The U7 respawn was asked three times, the last 64 s before the spawn, on a box Andrew was at. So it is not the DONE WHEN, contrary to the round-18 hint. Site Z's four respawns are a candidate, but the ask and the watch on site Z are unread. The laptop MSTR has no day log after 10-12. Its 10-14 sends (81 messages) disclaim rulings, but they carry project recommendations (109066 and 109068 "I recommend (a)", 109093). |
| 22 a lead settles its own box's calls; cross-box calls settled on the record | ADVANCED | one-box: `dell1-20261014T033410Z-19b2` OWN-BOX, opened 03:34:10Z, closed 03:37:57Z by 1.0.0_SA_CTO~DELL1 (ruling ffbed58e78); in no laptop cluster tick and no ANDREW_DIRECT file. Two-box: XB-20261014T121356Z-f7b9 read from both sides (435b8f0798, 14ee171a32) | The one-box half is met. The two-box record was closed MOOT after Andrew approved the underlying call, so no agreed two-box decision is read. The round-18 hint "settling today" does not hold for 10-15: the one dell1 close (a196) had been held for Andrew. |
| 23 seat list readable; nothing finished without a reviewer's grade | ADVANCED | `seat-list.py show --all`: boxes=4 read=1 absent=sitez,dell1,dell2 stale=laptop seats=9; `org/devices/state/laptop/seats.json` untracked, 3 of 9 rows carry project; round-close-check graded every judgment criterion on the laptop this week | The grade half is live on the laptop. The seat list exists for one box, is stale by a week, is not in git, and no person-names-each-seat read is recorded. |
| 24 research owed above the line, read alike by two leads | ADVANCED | `.tools/research-owed.py --selftest` 16/16; 0 runs logged | Built; the two-leads comparison has never run. Round 19 names it. |
| 25 a seat knows its role from its start; a tool stops the forbidden act | ADVANCED | `agent-spawn-audit.log`: TIER2_ACT_REFUSED `:19197` (COO~C, 10-13 20:32Z), `:19222`, `:19225` (CTO, 10-14); CVO_WORKER_REFUSED x2; `.tools/ajb.ps1:241-249` puts the SEAT STATEMENT in the first message (8 kinds in `org/ref/SEAT_ROLES.json`) | Tool refusals are read for CTO, COO and CVO, and none for CRO, Tier-2/CloudOps or worker. LD-0529 refuses a Tier-1 seat sending an act to Tier-2, not a Tier-2 seat's own forbidden act. The statement is delivered at start (this seat's own launch carried it), but no seat of any kind is recorded being asked and answering. |
| 26 one voice file for drafts in Andrew's name | MOVED | PRD v0.21 -> COMM_ASSIST FWD-2 | Graded by COMM_ASSIST. |
| 27 SSH by key from rc, muse and the laptop to four boxes, nothing else | ADVANCED | `deliverables/2.0.0_SA_COO~C/FWD27_READBACK_20261013.txt` (c24c592edb): sitez, dell1, dell2 port22=OPEN key=ANSWERED, methods publickey,keyboard-interactive, password_arm=KBDINT-NO-PROMPT, nontailnet_arm=NOT-DRIVEN | From the laptop, three of four boxes are met, with password login off. Open: the laptop as a target (its local account, GATE Andrew's "another time"), the rc and muse sources, and the refusal from outside the tailnet (seat-drivable; round 19). |
| 28 the data-proxy fence by route class | **REALIZED** | 2026-10-13 grade; TO-CT-aa-6 (dad8779d7d, ffe2c6cc45, 10-13 21:21Z) narrowed the internal class to tier-internal only: partner=403, internal=200 | Stands. The change since the grade only narrows. |

## Findings for the CTO's round-19 analysis

1. **FWD-10's ENDPOINT text is stale.** Andrew's 10-13 ~16:5xZ word gives the Dells his admin group, keeping three denies. The ACCEPT still says access
   changes are refused, while CloudTrail reads 34 of 34 Dell IAM writes succeeded since 10-11. An addendum re-words the refusal arm to the three kept denies.
   It then grades on the delete refusal (exercised) and an audit-trail write refusal (not yet).
2. **FWD-21's hint does not hold.** The U7 respawn was asked. The cell to cut is a respawn on a box nobody is watching, read from that box's audit with no
   ask in the broker before it, plus one MSTR day record. Site Z's 23:32Z respawns may already be it: read site Z's broker for an ask.
3. **FWD-12 is one read from REALIZED.** Where were dell1's f411 and c397 answered?
4. **FWD-3's ACCEPT** ("no other seat talks across boxes") fails on the record as kept: workers ack crossbox records. Either the managers ack, or the PRD
   accepts a worker read relayed by the manager.
5. The stray committer `t <a@b.c>` on 552e0e03ad (an integrate merge on CLOUD).

## Limits of this grade

- **Carried with their earlier pin, no new evidence:** FWD-7, 15, 16, 17, 18, 19 (and 1 and 28 re-read for regression only).
- **Not read:** site Z's broker (FWD-21), the other boxes' unpushed counts (FWD-4), and the uncommitted Dell deploy-audit logs (FWD-5).
- **CloudTrail:** `lookup-events` reads the management events of this account and region (us-east-1) only.
- **RDP:** a port probe, not a session.
- **Who gathered what:** the evidence passes were read-only subagents of this seat. The grades, the CloudTrail outcome count and the IAM-word reading are
  this seat's own reads.

-- 3.0.0_SA_CVO~L
