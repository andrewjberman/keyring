# `/self-drive 30m` every site-Z project -- ticks 7-8 (2026-10-09 ~10:4xZ to ~11:4xZ), `1.0.0_SA_CTO~Z`

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_074xZ_SELF_DRIVE_30M_EVERY_SITEZ_PROJECT.md` @4752d8dfcc.
Cron `fff05062`. Previous log: `ctoZ_self_drive_SITEZ_ALL_tick6.md` @dae519972f. **state: ARMED.**

## Scope

7 non-terminal SITEZ-placed projects; 2 of 9 closed. **Completion test: NOT DONE.** REACHABLE 6, UNREACHABLE 1 (NFRA_MCPMSP: G-MSPID).
The r29 window opened 11:00Z: `0.7.0_AE_CloudOps~Z` opened the r29 ledger entry at 11:14:14Z. NFRA_OPALAI, COMM_ASSIST r12, the 4-meeting
allowlist, MX-r-9, E2 and the metadata route all queue behind it. Inbox at tick 8: 0 unread. Open calls: 1 (Barron's sign-in, an act).

## Acts and rulings

| item | ruling / act | carrier |
|---|---|---|
| Codex heartbeat helpers died on Errno 36 (MSTR 32678) | the refused-beat handler catches OSError; running helpers take it on next launch | @5b403f569e |
| DQ-t18 C1 | VERIFIED by this seat: today's BBGTML run 07:00:13 ET, result 0, log closed 11:08:47Z; activation merge 04124013f9 at 11:10:51Z | (read) |
| dell2 4-meeting `/hx/transcripts` host allowlist | TAKE; first OPLGTW release after r29, its own pair; expect 3 of 4 (Research Team Meeting 403 on the delegated reach too) | @261e2c42a0 |
| COMM_ASSIST UB-f17d | FOLDED: CA-d-2 Phase A pre-flight now; the close-run fallback mail is human-sent by 19:30Z, option (b) refused (FWD-2) | @02c84f1029 |
| gateway host queue after r29 (COO~O 32710) | accepted: MP-x-4, allowlist, MX-r-9, E2, metadata; one release in flight at a time | msg 32708-reply |
| NFRA_OPALAI UB-fafc | FOLDED: r29 "serves" defined by a read; three spawns pre-cut; the counter rule PITCHED to CVO~Z as a governance fork (REC yes) | @6d0e23e25f |

## Never-widen halves signed

AMGT_RESAPP ii-1 @344af2c348 (fetch.py language stamp; 34 tests), ii-2 @4d6a429d98 (running-header strip; test_document 40/40).

## Governance calls pitched (awaiting verdict)

- `/unblock` counter: an in-progress owed act with an open ledger entry ticks WAITING, not empty. To `3.0.0_SA_CVO~Z`, REC yes.

## Acts only Andrew can do (cited)

- **Barron's sign-in** (AMGT_HARVST, call `sitez-20261008T231757Z-9f24`): his login.
- **COMM_ASSIST close-run fallback** (only if no admitted mail is texted by 19:30Z): he names the Opal staff member who sends one mail naming
  him, or sends the request himself (ruling @02c84f1029; no agent sends mail in his name, FWD-2).
- **G-MSPID** (NFRA_MCPMSP). **Forced worktree removal** (MCPORTAL, HELD). Both unchanged.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `Get-ScheduledTaskInfo` + log mtime + `git log` | PASS | verified DQ-t18's C1 ordering by measurement, not by the report |
| `git archive` + pytest | PASS / PARTIAL | ii-1 34/34, ii-2 test_document 40/40; 2 collection errors in the whole folder are scratch-only (registry files outside `lib/`) |
| `commit-gate.sh` + an errno control | PASS | Errno 36 is an OSError and not a PermissionError, so the old handler could not catch it |
| `unblock.py show/fold` | PASS | 2 folds this window |

-- 1.0.0_SA_CTO~Z
