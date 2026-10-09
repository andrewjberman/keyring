# SELF-DRIVE dell2 every project -- tick 25 (2026-10-09 ~16:48Z) -- 1.0.0_SA_CTO~DELL2

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_034xZ_SELF_DRIVE_30M_EVERY_DELL2_PROJECT_AND_DISCRETION_ON_THREE_ACTS.md`
@35fabf20c8. Cron c17cb1c7. **state: ARMED**

## Scope (11 projects, device dell2)

- **Status `closed`:** IRPT_CUSTDY (superseded).
- **Active at EXECUTING:** the other 10.
- **Inbox:** 0 unread. Every message since tick 24 has been acted on and acked.
- **Push state:** origin box/dell2 reads 4359059f3a. Local HEAD was b874540474 before this log (ls-remote 16:48Z).

## INCIDENT 2: irpt-status rev 4 live outage

| time (Z) | event |
|---|---|
| 15:43:11 | rev 4 applied (`VC/r14ka`); every request raised TypeError (split ship: `composition.py` lacked the kwarg) |
| 16:24 | `~G2` msg 3676 reports 52 events and HTTP 500 to every caller |
| 16:2x | Branch B ordered (release 1 half AMENDMENT 5); CloudOps~DELL2 restored rev 3 bytes to S3 (B1, no apply) |
| 16:29 | Branch B substituted to `0.7.0_AE_CloudOps~AR2` (@5ff94852a6, MSTR msg 3688); ledger opened 16:41:06 |
| 16:43:50 | live `t6OJTCcm` (rev 3) by this seat's monitor; MSTR read 16:44:00 |

**Duration about 61 minutes.** Rulings:
- AMENDMENT 4's "only an R2 failure rolls back" is withdrawn.
- **A live-call arm (one real GET answering 200 within a minute of the promote) is now standard in this seat's halves for every served Lambda release.**
- Rev 4 is re-cut with `composition.py` co-staged and a call-signature closure read.
- AR2's B3 after-reads (GET 200, errors flat) are owed in its ledger.

## INCIDENT 1 progress: client account data in tracked files (ruling @0e8209c33c)

- **AMENDMENT 1** (@f616e46440): dell1's carve-outs adopted. dell1 adopted the bare-account-number point (msg 3671), so it is one test on both boxes.
- **AMENDMENT 2** (@b849a11a9b): ONE token form, `acct#<sha8 of "firm:account">`. The CVO re-tokenized @751d0de81a. The cot id shapes were added.
- **Moves and redactions:**
  - IRPT_DASHBD: 61 evidence files @df127f168c, 13 docs, PRD @6d0b2b1103.
  - IRPT_BCKEND: 10 evidence files @12b257c3ab, docs @c75b937bb2, CTO ledgers @6d3163fdc3.
  - Channel rows: the CVO, @22a636941b, @e0023e4cc9, @ae1c3f61dc.
  - ADVI_COTBKF: census 179 then 79 more (shapes); redaction under way.
- **Blocked:** 5 terminal orders (DASHBD DB-b-6/10/13/15, BCKEND er-201). The TO gate's Layer 1 refuses any edit after their proofs moved out. A redaction-only
  limb is PROPOSED to the laptop gate owner (msg 3695).
- **Built by the laptop:** `client-data-check.py` @8c1d8a1966. `~P2` owns the hash-list builder.

## Other calls since tick 24

| # | call | ruling | record |
|---|---|---|---|
| 1 | COTBKF W77-S3 (`~C2` 3705) | pin `legacy_addresses.json` beside the writer; fail-closed; FIRMBKTS row read, never edited | COTBKF 22.1 |
| 2 | DASHBD r53 (CVO 3715) | heaviest day at 96.8% of the memory line: a memory-step pair before Monday plus a producer peak-memory cell | DASHBD 20 |
| 3 | CloudOps~DELL2 3702 (live invoke as standard?) | yes, for every served Lambda release | half AMENDMENT 5 |

## Acts only Andrew can do

- **Purge client-data paths from git history** on origin box/dell2 and CLOUD. MSTR holds the growing list (`C:/dev/_purge_list_for_andrew_20261009.txt`).
  Citation: CLAUDE.md Agent Autonomy (destructive git).
- **One meeting read through the live FWD-5 silver reader role.** Citation: the FWD-5 CTO half @91e314b74e, condition 2.
- **PROD push of the 49 Financial fee panel;** the other client-facing pages separately. Citation: CLAUDE.md Agent Autonomy, push law exception.
- **Research Meeting membership for the reading account** (open call 3082). Citation: CLAUDE.md, entitlements beyond his grants.
- **S3 deletes, each named by key.** Citation: CLAUDE.md Agent Autonomy (S3 deletes).
- Delete `C:/dev/_scratch265` (open call 62ea). Citation: CLAUDE.md Agent Autonomy (recursive deletion).

## Completion test

**NOT DONE.** 0 of 11 projects complete. All 11 are REACHABLE.

-- 1.0.0_SA_CTO~DELL2
