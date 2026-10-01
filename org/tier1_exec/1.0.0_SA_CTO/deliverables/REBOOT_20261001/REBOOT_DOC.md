# Laptop reboot -- 2026-10-01 -- who is relaunched, on what, in what order

**Order:** Andrew-direct ~16:1xZ, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_161xZ_DEVICE_SLOW_REBOOT_BRIEFS_AND_RESPAWN.md`
@223a35bb6b ("Every agent should write a brief ... then you write a reboot doc with who needs to be spawned and we launch them
with their briefs"; "i do not want them cut off mid-stream"). **Author:** `1.0.0_SA_CTO`, ~16:4xZ.

## State at the reboot

- Ten sessions were live (process census 16:17Z). Each stopped at its own checkpoint and wrote a brief; nothing is
  half-landed. Every open ledger entry waits only on a scheduled run or a read (each brief's section 3 names them).
- Briefs in: 9 of 10 at writing. `0.4.0_DS_ClientPlatform~S`: see its row.
- Memory: the endpoint-protection service grew about 450 MB an hour and only a reboot clears it (`0.0.0_AB_MSTR` msg 103882).
- Push state: laptop CLOUD about 537 commits ahead of origin `0abf99fcd4`; SITE Z is about 430 ahead of the same base. The
  first push after the reboot needs ONE merge of the two trunks, on Andrew's word (MSTR brief section 5a). A reboot keeps
  the disk, so nothing is lost by rebooting first.
- Walker: site-Z `2.0.0_SA_COO~D` armed the shared walker at 16:33Z. No laptop walk is cleared until site Z's DISARMED arrives.

## Relaunch order

Every seat starts the same way: `/watcher` once, read its brief, read and ack its inbox. ZERO crons at launch. Each `--say`
names only what to read.

| # | serial | brief (path @ commit) | why respawn | first act after reading | clock it must meet |
|---|---|---|---|---|---|
| 1 | `0.0.0_AB_MSTR` | `org/tier0_exec/0.0.0_AB_MSTR/deliverables/REBOOT_BRIEF_20261001_0.0.0_AB_MSTR.md` @a5b57cac89 | integrator and the bus to site Z; spawns the rest | post on the bus that the laptop is back; then seat rows 3-10 by `/mstr-spawn` with the hints below | -- |
| 2 | `1.0.0_SA_CTO` | `org/tier1_exec/1.0.0_SA_CTO/deliverables/REBOOT_20261001/REBOOT_BRIEF_20261001_1.0.0_SA_CTO.md` @fcfc0263d0 | rulings and every CTO half | re-arm `/self-drive 60m laptop directives` from its arming record (tick 79) | sign or refuse the 19 seed rows before 23:00Z if not overtaken |
| 3 | `2.0.0_SA_COO~M` | `org/tier1_exec/2.0.0_SA_COO/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_M.md` @6cd972d8ff | three ledgers close on tonight's runs; two packets owed (split accounts, seed rows) | read the 22:10Z and 23:00Z runs against its open legs | 22:10Z and 23:00Z today |
| 4 | `2.0.0_SA_COO~Y` | `org/tier1_exec/2.0.0_SA_COO~Y/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_Y.md` @07d17ac44f | the st10 packet (900 s release, built and merged) | cut the st10 packet | lease to 19:52Z |
| 5 | `2.0.0_SA_COO~P` | `org/tier1_exec/2.0.0_SA_COO/deliverables/REBOOT_BRIEF_20261001_2.0.0_SA_COO_P.md` @9a1eb08bab | Inflection serving packet; dashboard drain | re-spawn the DB-b-2 worker in its existing worktree; check for Andrew's delete word | -- |
| 6 | `2.0.0_SA_COO~D` | `org/tier1_exec/2.0.0_SA_COO~D/REBOOT_BRIEF_20261001_2.0.0_SA_COO_D.md` @b15b042e69 | three FAST leases; the Multi-Comp page walk | re-arm lapsed leases; restart the dev server on 5174 | leases to 19:02Z and 20:28Z |
| 7 | `3.0.0_SA_CVO` | `org/tier1_exec/3.0.0_SA_CVO/deliverables/REBOOT_BRIEF_20261001_3.0.0_SA_CVO.md` @79b8a2c5f0 | grades every pin the lanes land | grade new pins since 16:3xZ; compile MDPF_SECCLASS | -- |
| 8 | `4.0.0_SA_CRO` | `org/tier1_exec/4.0.0_SA_CRO/deliverables/REBOOT_BRIEF_20261001_4.0.0_SA_CRO.md` @b0bb251e63 | gold hookup leg V2 | read the function's configuration; wait for the run | **2026-10-02 13:30Z**, same-day rollback if it fails |
| 9 | `4.0.0_SA_CRO~X` | `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/REBOOT_BRIEF_20261001_4.0.0_SA_CRO_X.md` @ce7fdbabe6 | research partner of the CTO's self-drive | heartbeat IDLE, wait for an ask | -- |
| 10 | `0.4.0_DS_ClientPlatform~S` | brief NOT YET RECEIVED at writing | IRPT_DASHBD worker seat; holds the TO-DB-b-3 flip on `~P`'s 0.2.0 contract bump | read the brief once it lands; until then, `~P` (its issuer) reseats it on need | -- |

Rows 3 to 6 are four COO lanes: Andrew's IRPT exception to the cap of three stands; no fifth lane.

`--say` for each row: "Read <its brief path>, then your inbox." (Row 4 adds `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md`.)

## Left as found

- A worktree of lane `4.0.0_SA_CRO~T` (not a live seat) holds uncommitted Terraform files (`4.0.0_SA_CRO`'s brief, section
  3). The reboot keeps them on disk. Nobody commits or deletes them without reading them first.

## Acts only Andrew can do (unchanged by the reboot)

The ten cards of 13:34Z and the nine-object delete in the Inflection gold
(`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/PACKET_INF_GOLD_STALE_GAP_DAYS_DELETE_FOR_ANDREW_20261001.md` @3cc5b831aa).
The CLOUD push now also needs the merge with site Z's trunk.
