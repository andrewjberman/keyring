# /self-drive SITEZ fabric (relaunch) -- tick 23, 2026-10-08 ~05:50Z -- `1.0.0_SA_CTO~Z`

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_082xZ_SELF_DRIVE_60M_SITEZ_FABRIC_RELAUNCH_AFTER_REBOOT.md`
**Covers:** tick 22's log (author time 2026-10-08T00:54:02-04:00 by `git log`) to ~06:0xZ. Cadence 60m, cron `12f228ad`.
**state: ARMED**

## Measurements

- Sequence (`.tools/sequence-check.py --project`, 5 of 5 read): AMGT_CORPUS, AMGT_HARVST, AMGT_RESAPP NEEDS-SLOT=1 each;
  DSGN_AMGTV1 and ETFS_RIVALS none. No DRIFT, no WAITING. Unchanged.
- Inbox: 0 files unread in the folder; 2 broker messages at this tick's read, acked (31591, 31592).
- Origin CLOUD `885658894e` (ls-remote). Wheel files in `C:/tmp/mstrz-relay/taildrop-in`: **6 of 6**.
- Not run this tick: `directives-check`, `active-commitments`.

## Calls ruled since tick 22

| call | ruling | carrier |
|---|---|---|
| AMGT_HARVST gold rebuild #9 (`2.0.0_SA_COO~H` 31577) | CTO half SIGNED for one act; four true pairs lost by name; three conditions; runs BEFORE bb-18 (31582) | `deliverables/CTO_HALF_AMGT_HARVST_GOLD_REBUILD9_20261008.md` @d4eb3dc22f |
| ETFS_RIVALS tw-1, does its merge need a pair (`2.0.0_SA_COO~RV` 31583) | yes, short, after the 11:00Z run is read | msgs 31584, 31585 |
| ETFS_RIVALS tw-1's merge (31587) | CTO half SIGNED; the switch is set nowhere on this box | `deliverables/CTO_HALF_ETFS_RIVALS_R27_TW1_MERGE_20261008.md` @d969c62f46 |
| ETFS_RIVALS rounds 25 to 27, L10 (slugs 31525, 31548, 31592) | ADDENDUM 5: R15 to R18; round 28 | `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round22.md`, this commit |
| AMGT_RESAPP bb-18, the sixth wheel's use (`0.0.0_AB_MSTR~Z` 31591) | its delivery statement read whole; accepted for the one scratch-venv use; the GO waits on rebuild #9's end stamp | msgs 31593, 31594 |

Governance forks at the CVO: 0. Design forks at the CRO: 0.

## Received

- The sixth wheel, `rpds_py-2026.6.3-cp314-cp314-win_amd64.whl`, 220,380 B, sha256 `0be972be84cf...` by `0.0.0_AB_MSTR~Z`'s hash,
  equal to its manifest. Delivery statement, read by this seat: checks 1, 2, 4, 5, 7, 8 passed; 3 and 6 not applicable (the laptop
  holds no installed copy of that version; it runs 0.30.0), so the compiled contents were compared with nothing.
- `3.0.0_SA_CVO~RV` 31592: ho-1 J1 MET, 742 securities and 184,600 units owed; rk-1 J1 MET; tw-1 not measurable until merged.

## Scope state (register read, 5 of 5)

All five `status: active`, `dep_stage: EXECUTING`. **COMPLETION TEST: NOT DONE -- 0 of 5 complete.** All five REACHABLE.
Waiting: AMGT_HARVST on rebuild #9's act and end stamp; AMGT_RESAPP bb-18 on that stamp, then its GO; ETFS_RIVALS on the 11:00Z
run, then tw-1's merge; AMGT_CORPUS on the 13:00Z fire and four captures (port 5174); DSGN_AMGTV1 on RESAPP's deploy.

## Acts only Andrew can do (cited)

- The sign-in of `opal-gateway-bbg`, `/mcp` in the `0.0.3_BG_BBGTerminal` window, before the 2026-10-08 07:00 America/New_York
  send (his Microsoft login); and his word on the prepared one-session config move.
- His answer on a standing daily Bloomberg request of closes for the rivalfunds securities (CLAUDE.md, vendor use by his word).
- His word on force-removing drained worktrees that hold untracked scratch files (CLAUDE.md, recursive deletion).
- His word on whether "no fetch on any box" covers an AWS host at deploy; his word that the smoke on port 5174 is finished.

## Compiler Tools

- `sequence-check.py` x5; `s3api list-objects-v2` (rail-checked, a signing read); `Get-ScheduledTask`; native Read and Grep.
